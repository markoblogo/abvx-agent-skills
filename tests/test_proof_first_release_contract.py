from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_skill(name: str) -> str:
    return (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")


def test_public_release_verification_separates_proof_domains_and_statuses() -> None:
    text = read_skill("public-release-verification")
    for value in (
        "repository/commit identity",
        "build/package proof",
        "deployment proof",
        "HTTP/route proof",
        "SEO/metadata proof",
        "browser desktop/mobile proof",
        "locale/content proof",
        "visual/public availability proof",
        "human approval",
        "PROVEN",
        "PARTIAL",
        "BLOCKED",
        "UNKNOWN",
    ):
        assert value in text
    assert "Do not auto-publish" in text
    assert "Build proof is not live proof" in text


def test_skill_health_audit_is_review_only_and_covers_evaluation_drift() -> None:
    text = read_skill("skill-health-audit")
    for value in (
        "trigger fit",
        "false activation",
        "fixture/held-out evidence",
        "prompt bloat",
        "catalog/README drift",
        "ACCEPT",
        "REVISE",
        "INSUFFICIENT_EVIDENCE",
        "REJECT",
    ):
        assert value in text
    assert "must not edit" in text


def test_fixture_checked_skills_have_activation_and_negative_cases() -> None:
    fixtures = ROOT / "benchmarks" / "fixture-cases"
    expected = {
        "minimal-diff-builder",
        "diagnose",
        "reversible-agent-task",
        "browser-verification",
        "public-release-verification",
    }
    for name in expected:
        path = fixtures / f"{name}.json"
        assert path.is_file(), name
        text = path.read_text(encoding="utf-8")
        assert '"activation"' in text
        assert '"negative"' in text
