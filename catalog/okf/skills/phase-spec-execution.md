---
type: "Skill Catalog Entry"
title: "Phase Spec Execution"
description: "Runs large implementation tasks through explicit, falsifiable phases with per-phase criteria, verification, and lightweight state tracking."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/phase-spec-execution"
tags:
  - "skill"
  - "long-run-delivery-control"
  - "experimental"
  - "adapted"
canonical: "skills/phase-spec-execution"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Runs large implementation tasks through explicit, falsifiable phases with per-phase criteria, verification, and lightweight state tracking.

# Trigger
Execute large tasks through explicit phases with acceptance criteria, required commands, and state updates. Use when work is too large for one implementation pass but too important to leave as a vague checklist. Keep phases falsifiable, end-to-end, and small enough that each one can be verified honestly before moving on.

# Intended Use
Use for medium and large coding tasks, migrations, feature slices, and brownfield changes where one-pass implementation would blur sequencing and verification.

# Out Of Scope
Do not introduce formal phase specs for small edits that can be completed and verified in one loop.

# Inputs And Outputs
Inputs: target outcome, repo context, dependencies, verification surface.

Outputs: ordered phases, phase-level acceptance criteria, verification commands, and lightweight execution state.

# Risks
- Risk: ceremonial overplanning. Mitigation: require the smallest useful phase count.
- Risk: vague phases. Mitigation: force explicit acceptance criteria and verification commands.
- Risk: stale state. Mitigation: update status only after each verification pass.

# Metadata
* Group: [Long-Run Delivery Control](../groups/long-run-delivery-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/phase-spec-execution/SKILL.md)
* [SKILL_CARD.md](../../skills/phase-spec-execution/SKILL_CARD.md)

# Attribution
ABVX adapted from robzilla1738 `supergoal` phase-spec and state-tracking ideas, reduced into a smaller composable workflow for ABVX skillpacks.
