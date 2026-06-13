---
type: "Skill Catalog Entry"
title: "Role Skill Pack Design"
description: "Designs compact role-specific or workflow-specific skill packs with explicit base layers, difference layers, references, boundaries, and rollout order."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/role-skill-pack-design"
tags:
  - "skill"
  - "research-knowledge-methods"
  - "experimental"
  - "original"
canonical: "skills/role-skill-pack-design"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Designs compact role-specific or workflow-specific skill packs with explicit base layers, difference layers, references, boundaries, and rollout order.

# Trigger
Design role-specific or workflow-specific agent skill packs without collapsing everything into one prompt. Use when creating assistant layers for teams, products, functions, or operating roles. Define base-vs-difference layers, pack boundaries, references, triggers, and rollout order.

# Intended Use
Use when building assistant layers for teams, products, operating roles, or workflow stages and you need a reusable pack structure instead of one large prompt.

# Out Of Scope
Do not use to write product-specific policy from scratch, replace domain docs, or force a role matrix where one base workflow is enough.

# Inputs And Outputs
Inputs: role list, workflow inventory, operating boundaries, existing docs, current assistant behavior.

Outputs: pack structure, initial skill set, role layering model, and rollout order.

# Risks
- Risk: too many skills too early. Mitigation: start with the smallest proving set.
- Risk: duplicate logic across roles. Mitigation: define a base workflow first and add difference layers.
- Risk: burying details in one giant file. Mitigation: keep `SKILL.md` short and push detail into references.

# Metadata
* Group: [Research, Knowledge & Reusable Methods](../groups/research-knowledge-methods/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/role-skill-pack-design/SKILL.md)
* [SKILL_CARD.md](../../skills/role-skill-pack-design/SKILL_CARD.md)

# Attribution
ABVX original, informed by practical extraction of private role/workflow skill packs into reusable public method.
