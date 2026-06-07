from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from .packaged import packaged_skills_root
from .validator import validate_skills_root


def default_install_dir() -> Path:
    return Path.home() / ".codex" / "skills"


def list_skills(skills_root: Path) -> list[str]:
    return sorted(path.name for path in skills_root.iterdir() if path.is_dir())


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

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
