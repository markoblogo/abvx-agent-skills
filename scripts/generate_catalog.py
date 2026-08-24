#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from abvx_agent_skills.catalog import build_catalog, render_catalog_markdown


def main() -> int:
    tracked_skill_names = {
        Path(path).parent.name
        for path in subprocess.check_output(
            ["git", "-C", str(ROOT), "ls-files", "skills/*/SKILL.md"], text=True
        ).splitlines()
    }
    payload = build_catalog(ROOT / "skills", ROOT / "README.md", tracked_skill_names)
    (ROOT / "docs" / "catalog.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )
    (ROOT / "CATALOG.md").write_text(
        render_catalog_markdown(payload),
        encoding="utf-8",
    )
    print("Wrote docs/catalog.json")
    print("Wrote CATALOG.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
