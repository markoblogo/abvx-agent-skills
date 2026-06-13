---
type: "Skill Catalog Entry"
title: "Prototype Lab"
description: "Guides creation of throwaway prototypes that answer one concrete design, logic, or integration question."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/prototype-lab"
tags:
  - "skill"
  - "frontend-ux-product"
  - "experimental"
  - "adapted"
canonical: "skills/prototype-lab"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Guides creation of throwaway prototypes that answer one concrete design, logic, or integration question.

# Trigger
Build throwaway prototypes to answer a specific product, UI, state-machine, data-model, or workflow question before committing production code. Use when the user asks to prototype, explore variants, sanity-check logic, try designs, make a playable mock, or learn quickly with code that will be deleted or absorbed.

# Intended Use
Use for UI variants, state-machine exploration, data-model sanity checks, interaction sketches, and unknown integration behavior.

# Out Of Scope
Do not use to ship production code without tests, review, or cleanup.

# Inputs And Outputs
Inputs: question to answer, repo context, constraints, target users, existing app patterns.

Outputs: runnable prototype, observed learning, decision note, cleanup/absorb plan.

# Risks
- Risk: prototype rots in repo. Mitigation: mark throwaway and close with delete/absorb decision.
- Risk: polishing too early. Mitigation: focus on one question and one command.
- Risk: wrong prototype type. Mitigation: choose logic, UI, or integration branch first.

# Metadata
* Group: [Frontend, UX & Product Surfaces](/groups/frontend-ux-product/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.2.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/prototype-lab/SKILL.md)
* [SKILL_CARD.md](../../skills/prototype-lab/SKILL_CARD.md)

# Attribution
ABVX adapted from local prototype workflow.
