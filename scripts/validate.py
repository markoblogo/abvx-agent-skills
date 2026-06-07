#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from abvx_agent_skills.validator import validate_skills_root


def main() -> int:
    failures = validate_skills_root(ROOT / "skills")
    if failures:
        print("Validation failed:")
        for item in failures:
            print(f"- {item}")
        return 1
    print("All skills valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
