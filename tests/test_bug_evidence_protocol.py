from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_ROOT = ROOT / "skills" / "bug-evidence-protocol" / "scripts"


def load_module(name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, SCRIPT_ROOT / f"{name}.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def record(command_hash: str, exit_code: int, *, timed_out: bool = False) -> dict[str, object]:
    return {
        "argv": ["python3", "-m", "pytest", "tests/test_regression.py"],
        "command_sha256": command_hash,
        "exit_code": exit_code,
        "timed_out": timed_out,
        "repository": {"root": "/repo", "head": "abc"},
    }


def test_fix_proven_requires_same_command_and_captured_broader_checks() -> None:
    classifier = load_module("classify_evidence")
    before = record("same", 1)
    after = record("same", 0)
    broader = [record("suite", 0)]
    status, _ = classifier.classify(before, after, broader, "confirmed")
    assert status == "FIX_PROVEN"
    status, _ = classifier.classify(before, after, [], "confirmed")
    assert status == "FIX_UNVERIFIED"


def test_mismatched_command_and_broader_failure_fail_closed() -> None:
    classifier = load_module("classify_evidence")
    status, _ = classifier.classify(record("before", 1), record("after", 0), [record("suite", 0)], "confirmed")
    assert status == "INCONCLUSIVE"
    status, _ = classifier.classify(record("same", 1), record("same", 0), [record("suite", 1)], "confirmed")
    assert status == "FIX_REGRESSION"


def test_capture_redacts_and_bounds_output() -> None:
    capture = load_module("capture_command")
    value, truncated = capture.bounded("token=supersecret " + "x" * 600, 500)
    assert "supersecret" not in value
    assert "[REDACTED]" in value
    assert truncated is True
