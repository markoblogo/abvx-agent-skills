from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "anti-slop-review" / "SKILL.md"
CATALOG = ROOT / "skills" / "anti-slop-review" / "references" / "review-catalog.md"


def test_review_contract_separates_defects_from_taste() -> None:
    text = SKILL.read_text(encoding="utf-8")
    assert all(label in text for label in ("HARD_DEFECT", "COHERENCE", "TEMPLATE_RISK"))
    assert "A familiar pattern is not a defect merely because it is familiar." in text
    assert "Return at most seven findings per pass." in text
    assert "AS-001" in text


def test_original_unlicensed_source_is_not_distributed() -> None:
    references = list((SKILL.parent / "references").iterdir())
    assert references == [CATALOG]
    assert "not a ban list" in CATALOG.read_text(encoding="utf-8")
