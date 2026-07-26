from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "loop-hardening-contract" / "SKILL.md"


def test_loop_hardening_contract_keeps_three_bounded_modules() -> None:
    text = SKILL.read_text(encoding="utf-8")
    assert "## 1. Harness Stripping" in text
    assert "## 2. Runtime-Path Sprint Packet" in text
    assert "## 3. Broken-Window Revalidation" in text
    assert all(status in text for status in ("STILL_GREEN", "REOPENED", "INCONCLUSIVE"))


def test_loop_hardening_contract_forbids_unsafe_shortcuts() -> None:
    text = SKILL.read_text(encoding="utf-8")
    assert "Do not auto-revert" in text
    assert "executor cannot accept its own result" in text
    assert "Compilation is not Cardputer device proof" in text
    assert "Never strip sandboxing, budgets, stop conditions, human gates, root verification" in text
