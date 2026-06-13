---
type: "Skill Catalog Entry"
title: "Design Critique Polish"
description: "Runs a focused critique-and-polish pass for frontend interfaces before shipping."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/design-critique-polish"
tags:
  - "skill"
  - "frontend-ux-product"
  - "experimental"
  - "adapted"
canonical: "skills/design-critique-polish"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Runs a focused critique-and-polish pass for frontend interfaces before shipping.

# Trigger
Critique and polish frontend interfaces before shipping. Use when a page, component, or app surface feels unclear, inconsistent, flat, awkward, under-tested, or not yet production-grade, and when the next step should be a focused design/UX pass rather than a broad rewrite.

# Intended Use
Use after a frontend surface exists and needs critique, prioritization, and final quality improvements rather than a greenfield build.

# Out Of Scope
Do not use as a substitute for initial product definition, browser testing itself, or full accessibility/performance audits across an entire large product without scoping.

# Inputs And Outputs
Inputs: screenshots, routes, files, URLs, existing design context, and known constraints.

Outputs: ranked critique findings, high-leverage fix list, ship blockers, and polish guidance.

# Risks
- Risk: generic critique. Mitigation: force ordered review categories and concrete findings.
- Risk: over-polishing. Mitigation: separate ship blockers from later refinements.
- Risk: hiding structural issues behind visual tweaks. Mitigation: call out wrong core design language explicitly.

# Metadata
* Group: [Frontend, UX & Product Surfaces](/groups/frontend-ux-product/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/design-critique-polish/SKILL.md)
* [SKILL_CARD.md](../../skills/design-critique-polish/SKILL_CARD.md)

# Attribution
ABVX adapted from pbakaus `impeccable` critique/polish/audit workflow ideas, plus local browser verification and web quality review practice.
