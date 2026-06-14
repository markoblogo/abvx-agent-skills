#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from abvx_agent_skills.catalog import dump_catalog


def main() -> int:
    dump_catalog(ROOT / "skills", ROOT / "README.md", ROOT / "docs" / "catalog.json")
    print("Wrote docs/catalog.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
