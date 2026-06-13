---
type: "Skill Catalog Entry"
title: "Spec To PRD"
description: "Turns current discovery and repo understanding into a durable PRD for product, client, and internal roadmap work."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/spec-to-prd"
tags:
  - "skill"
  - "discovery-planning-delivery"
  - "experimental"
  - "adapted"
canonical: "skills/spec-to-prd"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Turns current discovery and repo understanding into a durable PRD for product, client, and internal roadmap work.

# Trigger
Turn the current conversation, repo understanding, and clarified decisions into a PRD. Use when a vague feature, client request, internal roadmap item, or discovery thread needs to become a durable product artifact. Prefer repo/domain language, explicit scope, implementation decisions, testing decisions, and issue-tracker-neutral output.

# Intended Use
Use when a request is clear enough to become a PRD but still needs a structured product artifact before issue slicing or implementation.

# Out Of Scope
Do not use when discovery is still too vague; clarify first.

# Inputs And Outputs
Inputs: current conversation context, repo understanding, clarified decisions.

Outputs: a PRD as markdown, issue body, or another durable planning artifact.

# Risks
- Risk: weak synthesis. Mitigation: send vague work back to grilling first.
- Risk: stale implementation detail. Mitigation: favor durable decisions over path-specific prose.
- Risk: fuzzy scope. Mitigation: require explicit out-of-scope and testing sections.

# Metadata
* Group: [Discovery, Planning & Delivery](../groups/discovery-planning-delivery/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.7.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/spec-to-prd/SKILL.md)
* [SKILL_CARD.md](../../skills/spec-to-prd/SKILL_CARD.md)

# Attribution
ABVX adapted from Matt Pocock's `to-prd`, rewritten for issue-tracker-neutral output and ABVX planning flows.
