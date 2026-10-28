#!/usr/bin/env python3
"""Bound gh's own CI watcher; never infer PR readiness from CI alone."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import time


class WatchError(Exception):
    pass


def watch(pr: int, repo: str, timeout: int) -> tuple[str, int]:
    deadline = time.monotonic() + timeout

    def run(args: list[str]) -> subprocess.CompletedProcess:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise subprocess.TimeoutExpired(args, timeout)
        # Capture output to avoid leaking remote logs or credentials in a receipt.
        return subprocess.run(args, capture_output=True, text=True, timeout=remaining)

    def head() -> dict:
        result = run(['gh', 'pr', 'view', str(pr), '--repo', repo,
                      '--json', 'headRefOid,state'])
        if result.returncode != 0:
            raise WatchError('PR metadata unavailable')
        try:
            value = json.loads(result.stdout)
        except (ValueError, TypeError) as exc:
            raise WatchError('Invalid PR metadata') from exc
        if not isinstance(value, dict) or not value.get('headRefOid') or value.get('state') not in ('OPEN', 'MERGED', 'CLOSED'):
            raise WatchError('Incomplete PR metadata')
        return value

    def terminal(value: dict) -> tuple[str, int] | None:
        if value['state'] == 'MERGED':
            return 'MERGED_EXTERNALLY', 3
        if value['state'] == 'CLOSED':
            return 'CLOSED', 3
        return None

    first = head()
    if terminal(first):
        return terminal(first)
    checks = run(['gh', 'pr', 'checks', str(pr), '--repo', repo,
                  '--required', '--json', 'name,bucket,state,link'])
    if checks.returncode not in (0, 1, 8):
        raise WatchError('Required checks unavailable')
    try:
        items = json.loads(checks.stdout)
    except (ValueError, TypeError) as exc:
        raise WatchError('Required checks unavailable') from exc
    if not isinstance(items, list) or any(not isinstance(x, dict) or not x.get('name') for x in items):
        raise WatchError('Invalid required check set')
    if not items:
        return 'NO_REQUIRED_CHECKS', 3

    result = run(['gh', 'pr', 'checks', str(pr), '--repo', repo,
                  '--required', '--watch', '--fail-fast', '--interval', '60'])
    final = head()
    if terminal(final):
        return terminal(final)
    if final['headRefOid'] != first['headRefOid']:
        return 'HEAD_CHANGED', 3
    if result.returncode == 0:
        verified = run(['gh', 'pr', 'checks', str(pr), '--repo', repo,
                        '--required', '--json', 'name,bucket,state,link'])
        if verified.returncode != 0:
            return 'CI_INCONCLUSIVE', 3
        try:
            current = json.loads(verified.stdout)
        except (ValueError, TypeError):
            return 'CI_INCONCLUSIVE', 3
        if not isinstance(current, list) or not current or any(
                not isinstance(x, dict) or not x.get('name') or x.get('bucket') != 'pass'
                for x in current):
            return 'CI_INCONCLUSIVE', 3
        # A push during the final check read invalidates that evidence too.
        latest = head()
        if terminal(latest):
            return terminal(latest)
        if latest['headRefOid'] != first['headRefOid']:
            return 'HEAD_CHANGED', 3
        return 'CI_PASSED', 0
    if result.returncode == 8:
        return 'CI_PENDING', 3
    # gh uses exit 1 for a failed check and some API errors. Do not guess which.
    return 'CI_FAILED_OR_UNAVAILABLE', 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pr', type=int)
    parser.add_argument('--repo', required=True)
    parser.add_argument('--timeout', type=int, default=1800)
    args = parser.parse_args()
    if args.pr < 1 or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', args.repo) or not 1 <= args.timeout <= 1800:
        parser.error('Use a positive PR number, owner/repository and a timeout of 1..1800 seconds')
    started = time.monotonic()
    try:
        state, code = watch(args.pr, args.repo, args.timeout)
    except subprocess.TimeoutExpired:
        state, code = 'TIMEOUT', 3
    except (WatchError, OSError):
        state, code = 'BLOCKED', 2
    print(json.dumps({'state': state, 'repo': args.repo, 'pr': args.pr,
                      'elapsed_seconds': round(time.monotonic() - started, 2),
                      'scope': 'required CI only; reviews and readiness unverified'}))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
