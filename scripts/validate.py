#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("Missing PyYAML. Install with: python -m pip install PyYAML") from exc


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "metadata", "allowed-tools"}
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"gho_[A-Za-z0-9_]{20,}"),
    re.compile(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"]?[A-Za-z0-9_./+-]{16,}"),
]


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def parse_frontmatter(path: Path, failures: list[str]) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML frontmatter", failures)
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path}: unterminated YAML frontmatter", failures)
        return {}
    try:
        data = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError as exc:
        fail(f"{path}: invalid YAML: {exc}", failures)
        return {}
    if not isinstance(data, dict):
        fail(f"{path}: frontmatter must be a mapping", failures)
        return {}
    return data


def scan_file(path: Path, failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "TODO" in text or "[TODO]" in text:
        fail(f"{path}: TODO placeholder found", failures)
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            fail(f"{path}: possible secret pattern found", failures)


def validate_skill(skill_dir: Path, failures: list[str]) -> None:
    skill_name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    card = skill_dir / "SKILL_CARD.md"
    openai_yaml = skill_dir / "agents" / "openai.yaml"

    for required in (skill_md, card, openai_yaml):
        if not required.is_file():
            fail(f"{skill_dir}: missing {required.relative_to(skill_dir)}", failures)

    if skill_md.is_file():
        data = parse_frontmatter(skill_md, failures)
        extra = set(data) - ALLOWED_FRONTMATTER_KEYS
        if extra:
            fail(f"{skill_md}: unexpected frontmatter keys: {sorted(extra)}", failures)
        if data.get("name") != skill_name:
            fail(f"{skill_md}: name must match directory ({skill_name})", failures)
        description = data.get("description")
        if not isinstance(description, str) or not description.strip():
            fail(f"{skill_md}: description is required", failures)
        elif len(description) > 1024:
            fail(f"{skill_md}: description exceeds 1024 characters", failures)
        name = data.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(name)):
            fail(f"{skill_md}: invalid skill name", failures)

    for path in skill_dir.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml", ".py", ".json"}:
            scan_file(path, failures)


def main() -> int:
    failures: list[str] = []
    if not SKILLS.is_dir():
        fail("Missing skills/ directory", failures)
    else:
        skill_dirs = sorted(path for path in SKILLS.iterdir() if path.is_dir())
        if not skill_dirs:
            fail("No skills found", failures)
        for skill_dir in skill_dirs:
            validate_skill(skill_dir, failures)

    if failures:
        print("Validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("All skills valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
