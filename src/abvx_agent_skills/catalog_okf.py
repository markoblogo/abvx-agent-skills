from __future__ import annotations

import difflib
from dataclasses import dataclass
from pathlib import Path

import yaml


GROUP_SPECS: list[tuple[str, str, tuple[str, ...]]] = [
    (
        "token-economy-context-control",
        "Token Economy & Context Control",
        (
            "rtk-assisted-shell",
            "shell-output-compaction",
            "graph-guided-code-reading",
            "token-efficient-execution",
            "token-frugal-mode",
            "lean-context-layout",
            "compaction-survival",
            "token-usage-audit",
        ),
    ),
    (
        "coding-debugging-architecture",
        "Coding, Debugging & Architecture",
        (
            "diagnose",
            "repo-debugging-ledger",
            "complexity-optimizer",
            "architecture-deepening-review",
            "test-driven-execution",
            "system-zoom-out",
            "agents-best-practices",
            "skillopt-evolve-skills",
        ),
    ),
    (
        "frontend-ux-product",
        "Frontend, UX & Product Surfaces",
        (
            "design-register-bootstrap",
            "frontend-taste-layer",
            "design-critique-polish",
            "frontend-product-builder",
            "designmd-brand-kit",
            "browser-verification",
            "web-quality-audit",
            "prototype-lab",
        ),
    ),
    (
        "html-artifacts-visual-deliverables",
        "HTML Artifacts & Visual Deliverables",
        (
            "html-diagram-artifact",
            "html-brief-artifact",
        ),
    ),
    (
        "project-context-onboarding",
        "Project Context & Onboarding",
        (
            "project-context-bootstrap",
            "durable-context-maintenance",
        ),
    ),
    (
        "discovery-planning-delivery",
        "Discovery, Planning & Delivery",
        (
            "rapid-grilling",
            "doc-grounded-grilling",
            "spec-to-prd",
            "plan-to-issues",
            "repo-issue-triage",
        ),
    ),
    (
        "research-knowledge-methods",
        "Research, Knowledge & Reusable Methods",
        (
            "evidence-ledger-research",
            "loopops-protocol",
            "book-to-skill",
            "role-skill-pack-design",
            "workflow-policy-layering",
            "brief-first-execution",
            "private-vs-publishable-skill-audit",
            "skill-effectiveness-audit",
        ),
    ),
    (
        "workflow-handoffs-multitrack",
        "Workflow, Handoffs & Multi-Track Work",
        (
            "dynamic-workflow-packets",
            "handoff",
            "session-retrospective",
        ),
    ),
    (
        "long-run-delivery-control",
        "Long-Run Delivery Control",
        (
            "delivery-preflight-gate",
            "phase-spec-execution",
            "recovery-loop-3strike",
            "delivery-baseline-audit",
        ),
    ),
    (
        "structured-data-spreadsheet-work",
        "Structured Data & Spreadsheet Work",
        (
            "spreadsheet-workbook-forensics",
        ),
    ),
]


@dataclass(frozen=True)
class SkillRecord:
    name: str
    title: str
    short_description: str
    trigger_description: str
    group_slug: str
    group_title: str
    status: str
    origin: str
    owner: str
    intended_use: str
    out_of_scope: str
    inputs_outputs: str
    risks: list[str]
    version: str
    attribution: str
    repo_path: str
    resource: str


@dataclass(frozen=True)
class FileResult:
    path: Path
    action: str
    message: str
    changed: bool = False
    diff: str = ""


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def _frontmatter_and_body(path: Path) -> tuple[dict[str, object], str]:
    text = _read_text(path)
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError(f"{path}: unterminated YAML frontmatter")
    data = yaml.safe_load(text[4:end]) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: frontmatter must be a mapping")
    return data, text[end + 5 :]


def _parse_card_sections(path: Path) -> dict[str, str]:
    text = _read_text(path)
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(line)
    return {
        key: "\n".join(lines).strip()
        for key, lines in sections.items()
    }


def _display_title(skill_dir: Path, frontmatter: dict[str, object]) -> str:
    yaml_name = str(frontmatter.get("name", "")).strip()
    yaml_title = yaml_name.replace("-", " ").title()
    openai_path = skill_dir / "agents" / "openai.yaml"
    if openai_path.is_file():
        try:
            data = yaml.safe_load(_read_text(openai_path)) or {}
            interface = data.get("interface") or {}
            display_name = str(interface.get("display_name", "")).strip()
            if display_name:
                return display_name
        except yaml.YAMLError:
            pass
    return yaml_title or skill_dir.name.replace("-", " ").title()


def _group_lookup() -> tuple[dict[str, tuple[str, str]], tuple[str, str]]:
    lookup: dict[str, tuple[str, str]] = {}
    for slug, title, names in GROUP_SPECS:
        for name in names:
            lookup[name] = (slug, title)
    fallback = ("uncategorized", "Uncategorized")
    return lookup, fallback


def iter_skill_dirs(root: Path) -> list[Path]:
    return sorted(path for path in root.iterdir() if path.is_dir() and (path / "SKILL.md").is_file())


def resolve_skills_root(path: Path) -> Path:
    if (path / "SKILL.md").is_file():
        return path.parent
    if (path / "skills").is_dir():
        return path / "skills"
    return path


def load_skill_records(skills_root: Path) -> list[SkillRecord]:
    skills_root = resolve_skills_root(skills_root)
    group_lookup, fallback = _group_lookup()
    records: list[SkillRecord] = []
    for skill_dir in iter_skill_dirs(skills_root):
        frontmatter, _body = _frontmatter_and_body(skill_dir / "SKILL.md")
        card = _parse_card_sections(skill_dir / "SKILL_CARD.md")
        group_slug, group_title = group_lookup.get(skill_dir.name, fallback)
        metadata = frontmatter.get("metadata") or {}
        if not isinstance(metadata, dict):
            metadata = {}
        records.append(
            SkillRecord(
                name=skill_dir.name,
                title=_display_title(skill_dir, frontmatter),
                short_description=str(card.get("Description", "")).strip()
                or str(frontmatter.get("description", "")).strip(),
                trigger_description=str(frontmatter.get("description", "")).strip(),
                group_slug=group_slug,
                group_title=group_title,
                status=str(metadata.get("abvx_status", "experimental")).strip() or "experimental",
                origin=str(metadata.get("abvx_origin", "original")).strip() or "original",
                owner=str(card.get("Owner", "")).strip(),
                intended_use=str(card.get("Intended Use", "")).strip(),
                out_of_scope=str(card.get("Out of Scope", "")).strip(),
                inputs_outputs=str(card.get("Inputs and Outputs", "")).strip(),
                risks=[
                    line.strip()
                    for line in str(card.get("Risks and Mitigations", "")).splitlines()
                    if line.strip()
                ],
                version=str(card.get("Version", "")).strip(),
                attribution=str(card.get("Sources and Attribution", "")).strip(),
                repo_path=f"skills/{skill_dir.name}",
                resource=f"https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/{skill_dir.name}",
            )
        )
    return records


def _yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _render_concept(record: SkillRecord) -> str:
    lines = [
        "---",
        f'type: {_yaml_quote("Skill Catalog Entry")}',
        f"title: {_yaml_quote(record.title)}",
        f"description: {_yaml_quote(record.short_description)}",
        f"resource: {_yaml_quote(record.resource)}",
        "tags:",
        f"  - {_yaml_quote('skill')}",
        f"  - {_yaml_quote(record.group_slug)}",
        f"  - {_yaml_quote(record.status)}",
        f"  - {_yaml_quote(record.origin)}",
        f"canonical: {_yaml_quote(record.repo_path)}",
        f"source: {_yaml_quote('abvx-agent-skills')}",
        f"status: {_yaml_quote(record.status)}",
        f"kind: {_yaml_quote('skill')}",
        "---",
        "",
        "# Summary",
        record.short_description,
        "",
        "# Trigger",
        record.trigger_description or "See the skill source files for the exact trigger contract.",
        "",
        "# Intended Use",
        record.intended_use or "See the skill card for intended use.",
        "",
        "# Out Of Scope",
        record.out_of_scope or "Not specified.",
        "",
        "# Inputs And Outputs",
        record.inputs_outputs or "Not specified.",
        "",
        "# Risks",
    ]
    if record.risks:
        lines.extend(record.risks)
    else:
        lines.append("No explicit risks recorded.")
    lines.extend(
        [
            "",
            "# Metadata",
            f"* Group: [{record.group_title}](../groups/{record.group_slug}/index.md)",
            f"* Status: `{record.status}`",
            f"* Origin: `{record.origin}`",
            f"* Version: `{record.version or 'unspecified'}`",
            f"* Owner: {record.owner or 'unspecified'}",
            "",
            "# Citations",
            f"* [SKILL.md](../../{record.repo_path}/SKILL.md)",
            f"* [SKILL_CARD.md](../../{record.repo_path}/SKILL_CARD.md)",
        ]
    )
    if record.attribution:
        lines.extend(["", "# Attribution", record.attribution])
    return "\n".join(lines).strip() + "\n"


def _render_root_index(records: list[SkillRecord]) -> str:
    lines = [
        "---",
        'okf_version: "0.1"',
        'title: "ABVX Skills Catalog"',
        'description: "Open Knowledge Format export of the ABVX Agent Skills catalog."',
        'source: "abvx-agent-skills"',
        'status: "active"',
        "---",
        "",
        "# ABVX Skills Catalog",
        "",
        "## Groups",
        "",
    ]
    counts = {slug: 0 for slug, _title, _names in GROUP_SPECS}
    counts["uncategorized"] = 0
    titles = {slug: title for slug, title, _names in GROUP_SPECS}
    titles["uncategorized"] = "Uncategorized"
    for record in records:
        counts[record.group_slug] = counts.get(record.group_slug, 0) + 1
    for slug, title, _names in GROUP_SPECS:
        count = counts.get(slug, 0)
        if count:
            lines.append(f"* [{title}](groups/{slug}/index.md) - {count} skills")
    if counts["uncategorized"]:
        lines.append(f"* [Uncategorized](groups/uncategorized/index.md) - {counts['uncategorized']} skills")
    lines.extend(["", "## Skills", ""])
    for record in records:
        lines.append(f"* [{record.title}](skills/{record.name}.md) - {record.short_description}")
    return "\n".join(lines).strip() + "\n"


def _render_group_index(group_slug: str, group_title: str, records: list[SkillRecord]) -> str:
    lines = [f"# {group_title}", ""]
    for record in records:
        lines.append(f"* [{record.title}](../../skills/{record.name}.md) - {record.short_description}")
    lines.append("")
    return "\n".join(lines)


def _render_group_concept(group_slug: str, group_title: str, records: list[SkillRecord]) -> str:
    description = f"Catalog grouping for {group_title.lower()}."
    resource = (
        "https://github.com/markoblogo/abvx-agent-skills/tree/main/"
        f"catalog/okf/groups/{group_slug}"
    )
    lines = [
        "---",
        f'type: {_yaml_quote("Skill Group")}',
        f"title: {_yaml_quote(group_title)}",
        f"description: {_yaml_quote(description)}",
        f"resource: {_yaml_quote(resource)}",
        "tags:",
        '  - "skill-group"',
        f"  - {_yaml_quote(group_slug)}",
        'canonical: "README.md"',
        'source: "abvx-agent-skills"',
        'status: "active"',
        'kind: "skill-group"',
        "---",
        "",
        f"# {group_title}",
        "",
        "## Skills",
        "",
    ]
    for record in records:
        lines.append(f"* [{record.title}](../../skills/{record.name}.md) - {record.short_description}")
    lines.append("")
    return "\n".join(lines)


def _unified_diff(path: Path, old: str, new: str) -> str:
    return "".join(
        difflib.unified_diff(
            old.splitlines(keepends=True),
            new.splitlines(keepends=True),
            fromfile=str(path),
            tofile=str(path),
        )
    )


def _write_or_diff(path: Path, content: str, dry_run: bool, print_diff: bool) -> tuple[str, bool, str]:
    normalized = content.replace("\r\n", "\n")
    if path.exists():
        current = _read_text(path)
        if current == normalized:
            return "skipped", False, ""
        diff = _unified_diff(path, current, normalized) if print_diff else ""
        if not dry_run:
            _write_text(path, normalized)
        return "updated", True, diff
    diff = _unified_diff(path, "", normalized) if print_diff else ""
    if not dry_run:
        _write_text(path, normalized)
    return "created", True, diff


def export_okf_catalog(
    skills_root: Path,
    output_dir: Path,
    *,
    dry_run: bool,
    print_diff: bool,
) -> list[FileResult]:
    records = load_skill_records(skills_root)
    grouped: dict[str, list[SkillRecord]] = {}
    titles: dict[str, str] = {}
    for record in records:
        grouped.setdefault(record.group_slug, []).append(record)
        titles[record.group_slug] = record.group_title

    files: list[tuple[Path, str]] = [
        (output_dir / "index.md", _render_root_index(records)),
    ]
    for record in records:
        files.append((output_dir / "skills" / f"{record.name}.md", _render_concept(record)))
    for slug, group_records in sorted(grouped.items()):
        title = titles.get(slug, "Uncategorized")
        files.append((output_dir / "groups" / slug / "index.md", _render_group_index(slug, title, group_records)))
        files.append((output_dir / "groups" / slug / "group.md", _render_group_concept(slug, title, group_records)))

    results: list[FileResult] = []
    for path, content in files:
        action, changed, diff = _write_or_diff(path, content, dry_run, print_diff)
        message = {
            "created": "created OKF catalog file",
            "updated": "updated OKF catalog file",
            "skipped": "already up to date",
        }[action]
        results.append(FileResult(path=path, action=action, message=message, changed=changed, diff=diff))
    return results
