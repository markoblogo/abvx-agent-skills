from __future__ import annotations

from importlib.resources import files
from pathlib import Path


def packaged_root() -> Path:
    return Path(str(files("abvx_agent_skills")))


def packaged_skills_root() -> Path:
    return packaged_root() / "skills"
