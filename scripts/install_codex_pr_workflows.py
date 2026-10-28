#!/usr/bin/env python3
"""Preview or install the six optional Codex PR skills from this checkout."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from abvx_agent_skills import installer

NAMES = ['codex-review-loop', 'pr-ci-watch', 'pr-modernize',
         'pr-takeover', 'pr-write', 'pr-ready']


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Install after a successful full-set preflight')
    parser.add_argument('--destination', type=Path, default=Path.home() / '.codex/skills')
    args = parser.parse_args()
    destination = args.destination.expanduser().resolve()
    try:
        plan = installer.plan(ROOT / 'skills', destination, NAMES, False)
        print(json.dumps({'destination': str(destination), 'preview': [
            {key: op[key] for key in ('name', 'action', 'local_changes')}
            for op in plan]}, indent=2))
        if any(op['action'] == 'conflict' for op in plan):
            print('Existing local changes preserved; installation not applied.', file=sys.stderr)
            return 2
        if args.apply:
            transaction = installer.install(ROOT / 'skills', destination, NAMES, False)
            print('Installed/recorded six skills; transaction ' + transaction)
        return 0
    except (installer.InstallError, OSError) as exc:
        print('Installation blocked: ' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
