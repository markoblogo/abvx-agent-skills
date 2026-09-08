from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "skills" / "happy-handoff" / "scripts" / "launch.py"
THREAD_ID = "11111111-2222-4333-8444-555555555555"


def load_launcher():
    spec = importlib.util.spec_from_file_location("happy_handoff_launcher", LAUNCHER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_build_script_command_supports_macos_and_linux() -> None:
    launcher = load_launcher()
    command = ["/opt/happy", "codex", "--resume", THREAD_ID]
    log = Path("/tmp/handoff.log")

    assert launcher.build_script_command("Darwin", "/usr/bin/script", log, command) == [
        "/usr/bin/script", "-q", str(log), *command
    ]
    linux = launcher.build_script_command("Linux", "/usr/bin/script", log, command)
    assert linux[:3] == ["/usr/bin/script", "-q", "-c"]
    assert linux[-1] == str(log)
    assert "--resume" in linux[3]


def test_build_script_command_rejects_unsupported_platform() -> None:
    launcher = load_launcher()
    with pytest.raises(ValueError, match="unsupported platform"):
        launcher.build_script_command("Windows", "script", Path("log"), ["happy"])


def test_dry_run_reports_exact_thread_and_workspace(tmp_path: Path) -> None:
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    for name in ("happy", "script"):
        executable = bin_dir / name
        executable.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
        executable.chmod(0o755)

    env = os.environ.copy()
    env["PATH"] = f"{bin_dir}{os.pathsep}{env['PATH']}"
    completed = subprocess.run(
        [
            sys.executable,
            str(LAUNCHER),
            "--thread-id",
            THREAD_ID,
            "--cwd",
            str(tmp_path),
            "--dry-run",
        ],
        check=True,
        capture_output=True,
        text=True,
        env=env,
    )
    receipt = json.loads(completed.stdout)
    assert receipt["status"] == "dry-run"
    assert receipt["thread_id"] == THREAD_ID
    assert receipt["cwd"] == str(tmp_path)
    assert receipt["command"][-2:] == ["--resume", THREAD_ID]
