import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "run_chisle_benchmark.py"
SPEC = importlib.util.spec_from_file_location("chisle_benchmark", SCRIPT)
benchmark = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(benchmark)


def test_case_mix_and_arm_rotation():
    cases = benchmark.cases()
    assert len(cases) == 8
    assert sum(case["kind"] == "coding" for case in cases) == 5
    assert sum(case["kind"] == "explanation" for case in cases) == 3
    assert {item for order in benchmark.ARM_ORDERS for item in order} == set(benchmark.ARMS)


def test_explanation_grader_counts_retained_information(tmp_path):
    case = next(item for item in benchmark.cases() if item["id"] == "release-claim-explanation")
    complete = '{"summary":"new123 build; old999 deploy; health lacks version; browser absent; approval pending", "retained_point_ids":["R1","R2","R3","R4","R5"], "evidence_files":["evidence.md","draft.md"], "caveat":"approval pending", "next_step":"verify browser and deployment"}'
    grade = benchmark.grade(case, tmp_path, complete)
    assert grade["passed"]
    assert grade["information_retained"] == grade["information_total"] == 5

    incomplete = '{"summary":"new123 build", "retained_point_ids":["R1"], "evidence_files":["evidence.md","draft.md"], "caveat":"unknown", "next_step":"check"}'
    grade = benchmark.grade(case, tmp_path, incomplete)
    assert not grade["passed"]
    assert grade["information_retained"] == 1


def test_prompt_arms_are_distinct():
    case = benchmark.cases()[0]
    baseline = benchmark.prompt_for(case, "baseline", "ABVX", "CHISLE")
    abvx = benchmark.prompt_for(case, "abvx", "ABVX", "CHISLE")
    combined = benchmark.prompt_for(case, "abvx_chisle", "ABVX", "CHISLE")
    assert "ABVX" not in baseline and "CHISLE" not in baseline
    assert "ABVX" in abvx and "CHISLE" not in abvx
    assert "ABVX" in combined and "CHISLE" in combined
