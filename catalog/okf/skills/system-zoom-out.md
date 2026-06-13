---
type: "Skill Catalog Entry"
title: "System Zoom Out"
description: "Maps a local code area back to the wider system so users can reason about modules, boundaries, and blast radius."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/system-zoom-out"
tags:
  - "skill"
  - "coding-debugging-architecture"
  - "experimental"
  - "adapted"
canonical: "skills/system-zoom-out"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Maps a local code area back to the wider system so users can reason about modules, boundaries, and blast radius.

# Trigger
Go up one layer of abstraction and explain how a local piece of code fits into the larger system. Use when the current focus is too narrow, the user is unfamiliar with an area, an audit needs broader context, or a refactor should be explained through modules, seams, and callers instead of line-by-line detail.

# Intended Use
Use when the current discussion is too local and a higher-level system view would improve understanding or decision quality.

# Out Of Scope
Do not use for exhaustive code walkthroughs when the user needs exact local mechanics instead of the system map.

# Inputs And Outputs
Inputs: local area of focus, repo docs, relevant modules and callers.

Outputs: a higher-level module map, boundaries, and a broader explanation of the change surface.

# Risks
- Risk: abstract fluff. Mitigation: tie every map back to real modules, callers, and boundaries.
- Risk: contradiction with docs. Mitigation: align with existing architecture docs or call the mismatch out.

# Metadata
* Group: [Coding, Debugging & Architecture](/groups/coding-debugging-architecture/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.7.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/system-zoom-out/SKILL.md)
* [SKILL_CARD.md](../../skills/system-zoom-out/SKILL_CARD.md)

# Attribution
ABVX adapted from Matt Pocock's `zoom-out`, rewritten for architecture and audit workflows.
