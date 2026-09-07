from __future__ import annotations

import json
import hashlib
import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_baselined_findings_do_not_double_block_on_aggregate_score(tmp_path: Path, monkeypatch) -> None:
    reports = tmp_path / "reports"
    reports.mkdir()
    (reports / "example.json").write_text(
        json.dumps(
            {
                "risk_assessment": {"score": 80},
                "issues": [
                    {
                        "rule_id": "OH1",
                        "severity": "HIGH",
                        "location": {"file": "script.py", "start_line": 4, "end_line": 4},
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    policy = tmp_path / "policy.yaml"
    policy.write_text("thresholds:\n  max_risk_score: 50\npaths:\n  include: ['skills/**']\n", encoding="utf-8")
    baseline = tmp_path / "baseline.json"
    baseline.write_text(
        json.dumps({"findings": [{"fingerprint": "OH1:skills/example/script.py:4:4"}]}),
        encoding="utf-8",
    )
    monkeypatch.setattr(
        sys,
        "argv",
        ["evaluate", "--reports-dir", str(reports), "--policy", str(policy), "--baseline", str(baseline)],
    )
    module = runpy.run_path(str(ROOT / "scripts" / "evaluate_skillspector.py"), run_name="test_module")
    assert module["main"]() == 0


def test_content_bound_exception_stops_matching_after_source_changes(tmp_path):
    source = tmp_path / "skills/example/SKILL.md"
    source.parent.mkdir(parents=True)
    source.write_text("Generic file-type discussion.\n")
    fingerprint = "AE1:skills/example/SKILL.md:1:1"
    baseline = tmp_path / "baseline.json"
    baseline.write_text(json.dumps({"findings": [{
        "fingerprint": fingerprint,
        "source_path": "skills/example/SKILL.md",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "expires_on": "2099-01-01",
    }]}))
    module = runpy.run_path(str(ROOT / "scripts/evaluate_skillspector.py"), run_name="test_module")
    load = module["load_baseline"]
    assert fingerprint in load(baseline, repo_root=tmp_path)[0]
    source.write_text("Different instructions at the same line.\n")
    assert fingerprint not in load(baseline, repo_root=tmp_path)[0]
    source.unlink()
    assert fingerprint not in load(baseline, repo_root=tmp_path)[0]


def test_missing_or_empty_reports_cannot_pass_the_security_gate(tmp_path, monkeypatch):
    reports = tmp_path / "reports"
    monkeypatch.setattr(sys, "argv", ["evaluate", "--reports-dir", str(reports), "--policy", str(ROOT / ".abvx/skillspector-policy.yaml")])
    module = runpy.run_path(str(ROOT / "scripts/evaluate_skillspector.py"), run_name="test_module")
    assert module["main"]() == 1
    reports.mkdir()
    assert module["main"]() == 1
