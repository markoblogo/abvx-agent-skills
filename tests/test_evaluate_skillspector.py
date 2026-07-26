from __future__ import annotations

import json
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
