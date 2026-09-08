#!/usr/bin/env python3
"""Schedule the current Codex task to resume in Happy with a pseudo-terminal."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import platform
import shlex
import shutil
import subprocess
import sys
import uuid


def fail(message: str) -> None:
    raise SystemExit(f"happy-handoff: {message}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--thread-id", default=os.environ.get("CODEX_THREAD_ID"))
    parser.add_argument("--cwd", default=os.getcwd())
    parser.add_argument("--delay", type=int, default=15)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def build_script_command(
    system: str, script: str, log_path: Path, command: list[str]
) -> list[str]:
    if system == "Darwin":
        return [script, "-q", str(log_path), *command]
    if system == "Linux":
        return [script, "-q", "-c", shlex.join(command), str(log_path)]
    raise ValueError(f"unsupported platform: {system}")


def main() -> int:
    args = parse_args()
    if not args.thread_id:
        fail("CODEX_THREAD_ID is unavailable")
    try:
        uuid.UUID(args.thread_id)
    except ValueError:
        fail("CODEX_THREAD_ID is not a UUID")

    cwd = Path(args.cwd).expanduser().resolve()
    if not cwd.is_dir():
        fail(f"working directory does not exist: {cwd}")
    if not 1 <= args.delay <= 120:
        fail("delay must be between 1 and 120 seconds")

    happy = shutil.which("happy")
    script = shutil.which("script")
    if not happy:
        fail("Happy CLI is not installed")
    if not script:
        fail("the system 'script' command is unavailable")

    command = [happy, "codex", "--resume", args.thread_id]
    receipt = {
        "status": "dry-run" if args.dry_run else "scheduled",
        "thread_id": args.thread_id,
        "cwd": str(cwd),
        "delay_seconds": args.delay,
        "command": command,
    }
    if args.dry_run:
        print(json.dumps(receipt, ensure_ascii=False))
        return 0

    auth = subprocess.run(
        [happy, "auth", "status"], capture_output=True, text=True, timeout=15
    )
    auth_text = auth.stdout + auth.stderr
    if auth.returncode != 0 or "Not authenticated" in auth_text or "Authenticated" not in auth_text:
        fail("Happy CLI is not authenticated")

    daemon = subprocess.run(
        [happy, "daemon", "status"], capture_output=True, text=True, timeout=15
    )
    if daemon.returncode != 0 or "Daemon is running" not in daemon.stdout:
        started = subprocess.run(
            [happy, "daemon", "start"], capture_output=True, text=True, timeout=30
        )
        if started.returncode != 0:
            fail("Happy daemon could not be started")

    log_dir = Path.home() / ".happy" / "handoffs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{args.thread_id}.log"
    try:
        scripted = build_script_command(platform.system(), script, log_path, command)
    except ValueError as exc:
        fail(str(exc))

    delayed = [
        "/bin/sh",
        "-c",
        'sleep "$1"; shift; exec "$@"',
        "happy-handoff",
        str(args.delay),
        *scripted,
    ]
    with open(os.devnull, "rb") as no_input, open(os.devnull, "ab") as no_output:
        process = subprocess.Popen(
            delayed,
            cwd=cwd,
            stdin=no_input,
            stdout=no_output,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )

    receipt.update({"launcher_pid": process.pid, "log": str(log_path)})
    print(json.dumps(receipt, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
