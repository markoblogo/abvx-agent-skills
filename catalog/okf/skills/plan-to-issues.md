---
type: "Skill Catalog Entry"
title: "Plan To Issues"
description: "Breaks PRDs and plans into thin, end-to-end slices that can be executed by agents or humans."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/plan-to-issues"
tags:
  - "skill"
  - "discovery-planning-delivery"
  - "experimental"
  - "adapted"
canonical: "skills/plan-to-issues"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Breaks PRDs and plans into thin, end-to-end slices that can be executed by agents or humans.

# Trigger
Break a PRD, plan, or spec into independently executable vertical slices. Use when a product artifact needs to become agent-ready or human-ready implementation tickets, especially for client, product, and multi-track project workflows. Prefer thin end-to-end slices, explicit blockers, and issue-tracker-neutral output.

# Intended Use
Use when a plan or PRD needs to become concrete tickets, task slices, or issue-tracker-ready work units.

# Out Of Scope
Do not use for horizontal decomposition when the real work should ship in vertical slices.

# Inputs And Outputs
Inputs: PRDs, plans, specs, codebase seams, user approval on granularity.

Outputs: issue-ready vertical slices with acceptance criteria and blockers.

# Risks
- Risk: slices too large. Mitigation: bias toward thinner end-to-end paths.
- Risk: slices too abstract. Mitigation: require verifiable acceptance criteria.
- Risk: wrong dependency graph. Mitigation: review blockers before publishing.

# Metadata
* Group: [Discovery, Planning & Delivery](/groups/discovery-planning-delivery/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.7.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/plan-to-issues/SKILL.md)
* [SKILL_CARD.md](../../skills/plan-to-issues/SKILL_CARD.md)

# Attribution
ABVX adapted from Matt Pocock's `to-issues`, rewritten for output-neutral issue slicing and ABVX execution flows.
