from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

from .packaged import packaged_skills_root
from .validator import validate_skills_root


def default_install_dir() -> Path:
    return Path.home() / ".codex" / "skills"


def list_skills(skills_root: Path) -> list[str]:
    return sorted(path.name for path in skills_root.iterdir() if path.is_dir())


def iter_skill_dirs(root: Path) -> list[Path]:
    if (root / "SKILL.md").is_file():
        return [root]
    return sorted(
        path for path in root.iterdir() if path.is_dir() and (path / "SKILL.md").is_file()
    )


def cmd_list(args: argparse.Namespace) -> int:
    skills_root = packaged_skills_root()
    for name in list_skills(skills_root):
        print(name)
    return 0


def copy_skill(source: Path, target: Path, force: bool) -> None:
    if target.exists():
        if not force:
            raise FileExistsError(f"Destination already exists: {target}")
        shutil.rmtree(target)
    shutil.copytree(source, target)


def cmd_install(args: argparse.Namespace) -> int:
    skills_root = packaged_skills_root()
    destination = args.destination.expanduser().resolve()
    destination.mkdir(parents=True, exist_ok=True)

    names = args.skills or list_skills(skills_root)
    missing = [name for name in names if not (skills_root / name).is_dir()]
    if missing:
        print(f"Unknown skills: {', '.join(sorted(missing))}", file=sys.stderr)
        return 2

    installed: list[str] = []
    for name in names:
        copy_skill(skills_root / name, destination / name, force=args.force)
        installed.append(name)

    print(f"Installed {len(installed)} skill(s) to {destination}")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    skills_root = args.skills_dir.expanduser().resolve() if args.skills_dir else packaged_skills_root()
    failures = validate_skills_root(skills_root)
    if failures:
        print("Validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("All skills valid.")
    return 0


def severity_rank(value: str) -> int:
    order = {"LOW": 1, "MEDIUM": 2, "HIGH": 3, "CRITICAL": 4}
    return order.get(str(value).upper(), 0)


def cmd_audit_security(args: argparse.Namespace) -> int:
    skillspector_bin = shutil.which(args.skillspector_bin)
    if not skillspector_bin:
        print(
            f"Could not find '{args.skillspector_bin}' in PATH. Install SkillSpector first.",
            file=sys.stderr,
        )
        return 2

    skills_root = args.skills_dir.expanduser().resolve() if args.skills_dir else packaged_skills_root()
    skill_dirs = iter_skill_dirs(skills_root)
    if not skill_dirs:
        print(f"No skills found in: {skills_root}", file=sys.stderr)
        return 2

    output_dir = args.output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    scan_errors: list[str] = []

    for skill_dir in skill_dirs:
        report_path = output_dir / f"{skill_dir.name}.json"
        cmd = [
            skillspector_bin,
            "scan",
            str(skill_dir),
            "--format",
            "json",
            "--output",
            str(report_path),
        ]
        if args.no_llm:
            cmd.append("--no-llm")

        completed = subprocess.run(cmd, capture_output=True, text=True)

        # SkillSpector uses exit 1 for risky findings; treat it as a completed scan.
        if completed.returncode not in (0, 1):
            detail = completed.stderr.strip() or completed.stdout.strip() or "unknown error"
            scan_errors.append(
                f"{skill_dir.name}: scan failed with exit code {completed.returncode}: {detail}"
            )
            continue

        data = json.loads(report_path.read_text(encoding="utf-8"))
        risk = data.get("risk_assessment", {})
        score = int(risk.get("score", 0))
        issues = data.get("issues", [])

        severities = sorted(
            {str(issue.get("severity", "LOW")).upper() for issue in issues},
            key=severity_rank,
            reverse=True,
        )
        max_severity = severities[0] if severities else "LOW"
        print(
            f"{skill_dir.name}: score={score} severity={risk.get('severity', 'LOW')} "
            f"issues={len(issues)} max_issue_severity={max_severity}"
        )

    if scan_errors:
        print("Security audit failed:")
        for item in scan_errors:
            print(f"- {item}")
        return 2

    print(f"Security audit passed for {len(skill_dirs)} skill(s). Reports: {output_dir}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="abvx-skills")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List packaged skills")
    list_parser.set_defaults(func=cmd_list)

    install_parser = subparsers.add_parser("install", help="Install packaged skills")
    install_parser.add_argument("skills", nargs="*", help="Skill names to install; defaults to all packaged skills")
    install_parser.add_argument(
        "-d",
        "--destination",
        type=Path,
        default=default_install_dir(),
        help="Destination directory for installed skills",
    )
    install_parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Overwrite existing destination directories",
    )
    install_parser.set_defaults(func=cmd_install)

    validate_parser = subparsers.add_parser("validate", help="Validate skill structure")
    validate_parser.add_argument(
        "skills_dir",
        nargs="?",
        type=Path,
        help="Directory containing skills; defaults to packaged skills",
    )
    validate_parser.set_defaults(func=cmd_validate)

    audit_parser = subparsers.add_parser("audit-security", help="Run SkillSpector against skills")
    audit_parser.add_argument(
        "skills_dir",
        nargs="?",
        type=Path,
        help="Directory containing skills; defaults to packaged skills",
    )
    audit_parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("artifacts/skillspector"),
        help="Directory for JSON reports",
    )
    audit_parser.add_argument(
        "--skillspector-bin",
        default="skillspector",
        help="SkillSpector executable name or path",
    )
    audit_parser.add_argument(
        "--no-llm",
        action="store_true",
        help="Run static analysis only",
    )
    audit_parser.set_defaults(func=cmd_audit_security)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
