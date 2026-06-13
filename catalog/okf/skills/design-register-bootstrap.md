---
type: "Skill Catalog Entry"
title: "Design Register Bootstrap"
description: "Creates or refreshes compact frontend design context, with an explicit `brand` versus `product` register split, before implementation begins."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/design-register-bootstrap"
tags:
  - "skill"
  - "frontend-ux-product"
  - "experimental"
  - "adapted"
canonical: "skills/design-register-bootstrap"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Creates or refreshes compact frontend design context, with an explicit `brand` versus `product` register split, before implementation begins.

# Trigger
Establish frontend design context before implementation. Use when a project lacks a clear PRODUCT.md or DESIGN.md, when the model needs to distinguish brand surfaces from product UI, or when design direction keeps drifting because audience, register, anti-references, and visual constraints are not explicit.

# Intended Use
Use when a frontend project lacks stable design context, when `PRODUCT.md` or `DESIGN.md` should be created or updated, or when the surface classification materially changes design choices.

# Out Of Scope
Do not use as a substitute for actual implementation, browser verification, or accessibility/performance review.

# Inputs And Outputs
Inputs: brief, screenshots, reference URLs, existing tokens, CSS, components, and any current context files.

Outputs: compact design register, updated `PRODUCT.md` and/or `DESIGN.md`, downstream design constraints.

# Risks
- Risk: over-documenting instead of shipping. Mitigation: keep context compact and implementation-oriented.
- Risk: wrong register choice. Mitigation: classify `brand` versus `product` explicitly and ask one clarifying question only when needed.
- Risk: reinvention. Mitigation: preserve coherent existing design systems and document them before changing them.

# Metadata
* Group: [Frontend, UX & Product Surfaces](/groups/frontend-ux-product/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/design-register-bootstrap/SKILL.md)
* [SKILL_CARD.md](../../skills/design-register-bootstrap/SKILL_CARD.md)

# Attribution
ABVX adapted from pbakaus `impeccable` project setup and register split concepts, plus local PRODUCT.md / DESIGN.md workflow practice.
