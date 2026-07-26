#!/usr/bin/env python3
"""Run one command and write a bounded, redacted evidence record."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SECRET_PATTERNS = [
    re.compile(r"(?i)(authorization\s*:\s*bearer\s+)[^\s]+"),
    re.compile(r"(?i)((?:api[_-]?key|access[_-]?token|token|password|secret)\s*[:=]\s*)[^\s]+"),
    re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|npm_[A-Za-z0-9]{20,})\b"),
]
LOCKFILES = ("package-lock.json", "pnpm-lock.yaml", "yarn.lock", "uv.lock", "poetry.lock", "Cargo.lock", "go.sum")


def redact(value: str) -> str:
    result = value
    for pattern in SECRET_PATTERNS:
        result = pattern.sub(r"\1[REDACTED]" if pattern.groups else "[REDACTED]", result)
    return result


def bounded(value: str, maximum: int) -> tuple[str, bool]:
    cleaned = redact(value)
    if len(cleaned) <= maximum:
        return cleaned, False
    head = maximum // 2
    tail = maximum - head
    return cleaned[:head] + "\n... [output truncated] ...\n" + cleaned[-tail:], True


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def git_value(cwd: Path, *args: str) -> str | None:
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else None


def repository_record(cwd: Path) -> dict[str, Any]:
    root_value = git_value(cwd, "rev-parse", "--show-toplevel")
    root = Path(root_value) if root_value else cwd
    status = git_value(root, "status", "--porcelain") if root_value else None
    lockfiles = {}
    for name in LOCKFILES:
        path = root / name
        if path.is_file():
            lockfiles[name] = sha256_bytes(path.read_bytes())
    return {
        "root": str(root.resolve()),
        "head": git_value(root, "rev-parse", "HEAD") if root_value else None,
        "dirty": bool(status) if status is not None else None,
        "environment_ids": lockfiles,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", default="evidence")
    parser.add_argument("--cwd", type=Path, default=Path.cwd())
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--max-output", type=int, default=6000)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("provide a command after --")
    if args.timeout <= 0 or args.max_output < 500:
        parser.error("timeout must be > 0 and max-output must be >= 500")
    cwd = args.cwd.expanduser().resolve()
    if not cwd.is_dir():
        parser.error(f"cwd is not a directory: {cwd}")

    started = time.perf_counter_ns()
    timed_out = False
    try:
        completed = subprocess.run(command, cwd=cwd, capture_output=True, timeout=args.timeout, check=False)
        exit_code: int | None = completed.returncode
        stdout_raw = completed.stdout.decode("utf-8", errors="replace")
        stderr_raw = completed.stderr.decode("utf-8", errors="replace")
    except subprocess.TimeoutExpired as error:
        timed_out = True
        exit_code = None
        stdout_raw = (error.stdout or b"").decode("utf-8", errors="replace")
        stderr_raw = (error.stderr or b"").decode("utf-8", errors="replace")

    stdout, stdout_truncated = bounded(stdout_raw, args.max_output)
    stderr, stderr_truncated = bounded(stderr_raw, args.max_output)
    repository = repository_record(cwd)
    record = {
        "schema_version": 1,
        "label": args.label,
        "argv": command,
        "command_sha256": sha256_bytes(json.dumps(command, separators=(",", ":")).encode()),
        "cwd": str(cwd),
        "runtime": f"Python {platform.python_version()} on {platform.system()} {platform.machine()}",
        "repository": repository,
        "environment_ids": repository["environment_ids"],
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "duration_ms": round((time.perf_counter_ns() - started) / 1_000_000, 3),
        "exit_code": exit_code,
        "timed_out": timed_out,
        "stdout": stdout,
        "stderr": stderr,
        "truncated": stdout_truncated or stderr_truncated,
        "secrets_redacted": True,
    }
    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"{args.label}: {'TIMEOUT' if timed_out else f'exit {exit_code}'} -> {output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except OSError as error:
        print(f"capture failed: {error}", file=sys.stderr)
        raise SystemExit(1)
