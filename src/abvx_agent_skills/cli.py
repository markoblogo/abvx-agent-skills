from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

from .catalog import dump_catalog
from . import installer
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


def cmd_install(args: argparse.Namespace) -> int:
    source = packaged_skills_root()
    options = bool(args.skills) + bool(args.profile) + bool(args.all)
    if options != 1:
        raise installer.InstallError("Choose skill names, --profile, or explicit --all")
    names = args.skills or (installer.PROFILES[args.profile] if args.profile else list_skills(source))
    destination = args.destination.expanduser().resolve()
    if args.dry_run:
        selection = installer.plan(source, destination, names, args.force)
        print(json.dumps({'preview': [{k: op[k] for k in ('name', 'action', 'local_changes', 'added', 'removed', 'changed')} for op in selection]}, indent=2))
        return 2 if any(op['action'] == 'conflict' for op in selection) else 0
    tx = installer.install(source, destination, names, args.force, args.profile)
    print(f"Installed/recorded {len(set(names))} skill(s); transaction {tx}; backups retained")
    return 0


def cmd_profiles(args: argparse.Namespace) -> int:
    print(json.dumps(installer.PROFILES, indent=2))
    return 0


def cmd_state(args: argparse.Namespace) -> int:
    destination = args.destination.expanduser().resolve()
    if args.command == 'doctor':
        report = installer.doctor(packaged_skills_root(), destination)
        print(json.dumps(report, indent=2))
        return 1 if report['pending_transactions'] or any(s['status'] != 'ok' for s in report['skills']) else 0
    if args.command == 'rollback':
        print('Rolled back transaction ' + installer.rollback(destination, args.force))
    else:
        print('Recovered transactions: ' + ', '.join(installer.recover(destination)))
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


def cmd_catalog(args: argparse.Namespace) -> int:
    skills_root = args.skills_dir.expanduser().resolve() if args.skills_dir else packaged_skills_root()
    readme_path = args.readme.expanduser().resolve()
    output_path = args.output.expanduser().resolve()
    dump_catalog(skills_root, readme_path, output_path)
    print(f"Wrote catalog: {output_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="abvx-skills")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List packaged skills")
    list_parser.set_defaults(func=cmd_list)

    install_parser = subparsers.add_parser("install", help="Install packaged skills")
    install_parser.add_argument("skills", nargs="*", help="Explicit skill names to install")
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
    install_parser.add_argument('--profile', choices=installer.PROFILES)
    install_parser.add_argument('--all', action='store_true', help='Explicitly select the entire pack')
    install_parser.add_argument('--dry-run', action='store_true', help='Read-only full-set preview')
    install_parser.set_defaults(func=cmd_install)
    profiles_parser = subparsers.add_parser('profiles', help='List the three small starter profiles')
    profiles_parser.set_defaults(func=cmd_profiles)
    for command in ('doctor', 'rollback', 'recover'):
        state_parser = subparsers.add_parser(command)
        state_parser.add_argument('-d', '--destination', type=Path, default=default_install_dir())
        if command == 'rollback':
            state_parser.add_argument('--force', action='store_true', help='Retain post-install edits in history before restoring')
        state_parser.set_defaults(func=cmd_state)


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

    catalog_parser = subparsers.add_parser("catalog", help="Generate machine-readable skill catalog")
    catalog_parser.add_argument(
        "output",
        type=Path,
        help="Output JSON path",
    )
    catalog_parser.add_argument(
        "--skills-dir",
        type=Path,
        help="Directory containing skills; defaults to packaged skills",
    )
    catalog_parser.add_argument(
        "--readme",
        type=Path,
        default=Path("README.md"),
        help="README path used to infer skill categories",
    )
    catalog_parser.set_defaults(func=cmd_catalog)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (installer.InstallError, OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
