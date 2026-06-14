from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml


def parse_skill_frontmatter(skill_md: Path) -> dict[str, Any]:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data = yaml.safe_load(text[4:end]) or {}
    return data if isinstance(data, dict) else {}


def parse_openai_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, dict) else {}


def parse_markdown_sections(path: Path) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = line[3:].strip().lower()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)
    return {key: "\n".join(value).strip() for key, value in sections.items()}


def markdown_list_items(section: str) -> list[str]:
    items: list[str] = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            items.append(stripped[2:].strip())
    return items


def category_map_from_readme(readme_path: Path) -> dict[str, str]:
    current_category: str | None = None
    categories: dict[str, str] = {}
    skill_row = re.compile(r"^\|\s*`([a-z0-9-]+)`\s*\|")

    for raw_line in readme_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("### "):
            current_category = line[4:].strip()
            continue
        match = skill_row.match(line)
        if match and current_category:
            categories[match.group(1)] = current_category
    return categories


def build_catalog(skills_root: Path, readme_path: Path) -> dict[str, Any]:
    categories = category_map_from_readme(readme_path)
    skills: list[dict[str, Any]] = []
    github_root = "https://github.com/markoblogo/abvx-agent-skills/blob/main"

    for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        card_md = skill_dir / "SKILL_CARD.md"
        openai_yaml = skill_dir / "agents" / "openai.yaml"
        frontmatter = parse_skill_frontmatter(skill_md)
        card_sections = parse_markdown_sections(card_md) if card_md.is_file() else {}
        ui = (parse_openai_yaml(openai_yaml).get("interface") or {}) if openai_yaml.is_file() else {}

        category = categories.get(skill_dir.name, "Uncategorized")
        composable_with = markdown_list_items(card_sections.get("composable with", ""))
        anti_patterns = markdown_list_items(card_sections.get("anti-patterns", ""))
        intended_use = card_sections.get("intended use", "")
        risks = card_sections.get("risks and mitigations", "")
        model_sensitivity = card_sections.get("model sensitivity", "")

        skills.append(
            {
                "name": skill_dir.name,
                "display_name": ui.get("display_name") or skill_dir.name,
                "category": category,
                "description": frontmatter.get("description", ""),
                "short_description": ui.get("short_description", ""),
                "intended_use": intended_use,
                "model_sensitivity": model_sensitivity,
                "composable_with": composable_with,
                "anti_patterns": anti_patterns,
                "risks": risks,
                "path": f"skills/{skill_dir.name}/SKILL.md",
                "card_path": f"skills/{skill_dir.name}/SKILL_CARD.md",
                "github_skill_url": f"{github_root}/skills/{skill_dir.name}/SKILL.md",
                "github_card_url": f"{github_root}/skills/{skill_dir.name}/SKILL_CARD.md",
                "origin": (frontmatter.get("metadata") or {}).get("abvx_origin", ""),
                "status": (frontmatter.get("metadata") or {}).get("abvx_status", ""),
            }
        )

    by_category: dict[str, int] = {}
    for item in skills:
        by_category[item["category"]] = by_category.get(item["category"], 0) + 1

    return {
        "skill_count": len(skills),
        "categories": by_category,
        "skills": skills,
    }


def dump_catalog(skills_root: Path, readme_path: Path, output_path: Path) -> None:
    payload = build_catalog(skills_root, readme_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def render_catalog_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# ABVX Agent Skills Catalog",
        "",
        "Generated from `docs/catalog.json`.",
        "",
        "| Skill | Category | Use case | Install |",
        "|---|---|---|---|",
    ]

    for skill in sorted(payload.get("skills", []), key=lambda item: item["name"]):
        use_case = skill.get("short_description") or skill.get("description") or skill.get("intended_use") or ""
        use_case = " ".join(str(use_case).split())
        install = f"`gh skill install markoblogo/abvx-agent-skills {skill['name']}`"
        lines.append(
            f"| `{skill['name']}` | {skill['category']} | {use_case} | {install} |"
        )

    lines.append("")
    return "\n".join(lines)


def dump_catalog_markdown(skills_root: Path, readme_path: Path, output_path: Path) -> None:
    payload = build_catalog(skills_root, readme_path)
    output_path.write_text(render_catalog_markdown(payload), encoding="utf-8")
