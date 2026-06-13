---
type: "Skill Catalog Entry"
title: "Delivery Baseline Audit"
description: "Performs an end-of-task audit against the starting baseline and the full working tree so declared deliverables are checked as shipped artifacts, not just as transcript claims."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/delivery-baseline-audit"
tags:
  - "skill"
  - "long-run-delivery-control"
  - "experimental"
  - "adapted"
canonical: "skills/delivery-baseline-audit"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Performs an end-of-task audit against the starting baseline and the full working tree so declared deliverables are checked as shipped artifacts, not just as transcript claims.

# Trigger
Audit claimed delivery against the starting baseline and the current working tree. Use when a task has declared deliverables, when a long run might say 'done' before shipping real changes, or when final verification must check the actual artifact set rather than only the transcript or commits.

# Intended Use
Use at the end of multi-step delivery, autonomous runs, migrations, and feature slices with explicit deliverables or high regression risk.

# Out Of Scope
Do not force a baseline audit for trivial edits where the deliverable is obvious and fully covered by one direct verification loop.

# Inputs And Outputs
Inputs: baseline reference, declared deliverables, final working tree, mandatory verification commands.

Outputs: delivery audit record, gap list, and a complete-or-fix verdict.

# Risks
- Risk: over-auditing trivial work. Mitigation: reserve for declared-deliverable or long-run tasks.
- Risk: missing untracked or unstaged outputs. Mitigation: require full working-tree inspection.
- Risk: stale verification. Mitigation: re-run final commands once at the end.

# Metadata
* Group: [Long-Run Delivery Control](/groups/long-run-delivery-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/delivery-baseline-audit/SKILL.md)
* [SKILL_CARD.md](../../skills/delivery-baseline-audit/SKILL_CARD.md)

# Attribution
ABVX adapted from robzilla1738 `supergoal` baseline-reference and final-audit concepts, condensed into a standalone audit skill.
