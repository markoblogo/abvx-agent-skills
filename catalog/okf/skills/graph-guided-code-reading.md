---
type: "Skill Catalog Entry"
title: "Graph Guided Code Reading"
description: "Reduces repository-reading token waste by navigating code through entrypoints, symbols, dependencies, and blast radius instead of broad reading."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/graph-guided-code-reading"
tags:
  - "skill"
  - "token-economy-context-control"
  - "experimental"
  - "adapted"
canonical: "skills/graph-guided-code-reading"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Reduces repository-reading token waste by navigating code through entrypoints, symbols, dependencies, and blast radius instead of broad reading.

# Trigger
Reduce repository-reading token waste by navigating code through symbols, entrypoints, dependencies, changed files, and blast radius instead of broad whole-tree or whole-file reading. Use on medium-to-large repos, PR reviews, architecture questions, onboarding, debugging across modules, or long-running audits.

# Intended Use
Use on medium-to-large repos, PR reviews, architecture questions, onboarding, debugging across modules, and long-running audits.

# Out Of Scope
Do not force this workflow on tiny repos where direct reading is cheaper, or when exact raw artifacts matter more than structural navigation.

# Inputs And Outputs
Inputs: task goal, changed files or entrypoint, available code-navigation tools.

Outputs: a compact focus set, narrow reads around relevant nodes, and a smaller evidence surface.

# Risks
- Risk: missing an indirect dependency. Mitigation: expand one edge at a time and include nearby tests and contracts.
- Risk: overengineering on small repos. Mitigation: skip formal graphing when two or three files already answer the question.
- Risk: stale focus set. Mitigation: keep a checked-location ledger and refresh only when a new hypothesis appears.

# Metadata
* Group: [Token Economy & Context Control](../groups/token-economy-context-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.4.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/graph-guided-code-reading/SKILL.md)
* [SKILL_CARD.md](../../skills/graph-guided-code-reading/SKILL_CARD.md)

# Attribution
ABVX adapted from Code Review Graph ideas around persistent code graphs, targeted review context, and blast-radius-first reading.
