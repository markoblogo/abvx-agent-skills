"""Check that the published demo grader distinguishes correctness from fluency."""
import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "run_measured_demos.py"
SPEC = importlib.util.spec_from_file_location("measured_demos", SCRIPT)
demos = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(demos)


def test_original_patch_fixtures_fail_and_correct_solutions_pass(tmp_path):
    fixes = {
        "page-count": "def pages(total,size):\n if total<0 or size<=0: raise ValueError()\n return (total+size-1)//size\n",
        "stable-unique": "def unique(values):\n return list(dict.fromkeys(values))\n",
        "inclusive-window": "def within(value,lower,upper):\n if lower>upper: raise ValueError()\n return lower<=value<=upper\n",
    }
    for case in demos.cases():
        if case["kind"] != "patch":
            continue
        (tmp_path / "app.py").write_text(case["files"]["app.py"])
        assert not demos.grade(case, tmp_path, "Fixed!")["passed"]
        (tmp_path / "app.py").write_text(fixes[case["id"]])
        assert demos.grade(case, tmp_path, "")["passed"]


def test_release_grader_rejects_unsupported_live_claim(tmp_path):
    import json
    case = next(c for c in demos.cases() if c["id"] == "build-only")
    answer = dict(case["expected"])
    assert demos.grade(case, tmp_path, json.dumps(answer))["passed"]
    answer["can_announce_live"] = True
    assert not demos.grade(case, tmp_path, json.dumps(answer))["passed"]
    assert not demos.grade(case, tmp_path, "It is live!")["passed"]


def test_lookup_grader_rejects_archived_value(tmp_path):
    import json
    case = next(c for c in demos.cases() if c["kind"] == "lookup")
    answer = dict(case["expected"])
    assert demos.grade(case, tmp_path, json.dumps(answer))["passed"]
    answer["value"] = 100
    assert not demos.grade(case, tmp_path, json.dumps(answer))["passed"]


def test_isolation_rejects_local_skill_loading():
    event = {"type": "item.completed", "item": {"command": "cat /Users/demo/.agents/skills/ast-index/SKILL.md"}}
    assert demos.isolation_violations([event])
    assert not demos.isolation_violations([{"type": "item.completed", "item": {"command": "cat app.py"}}])
