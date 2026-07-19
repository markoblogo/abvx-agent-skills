from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "frontend-taste-layer" / "SKILL.md"


def test_taste_layer_has_bounded_route_and_review_packet() -> None:
    text = SKILL.read_text(encoding="utf-8")
    assert "For marketing, editorial, portfolio" in text
    assert "use Lazyweb evidence first" in text
    assert all(axis in text for axis in ("variance", "motion", "density"))
    assert "Audit First On Redesigns" in text
    assert "Layout Rhythm Review" in text
    assert "Every animation must communicate" in text
    assert "prefers-reduced-motion" in text
    assert "every visible string" in text
    assert "INSUFFICIENT_VISUAL_EVIDENCE" in text
