---
type: "Skill Catalog Entry"
title: "Rapid Grilling"
description: "Runs a lightweight one-question-at-a-time grilling session to sharpen vague ideas before heavier planning."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/rapid-grilling"
tags:
  - "skill"
  - "discovery-planning-delivery"
  - "experimental"
  - "adapted"
canonical: "skills/rapid-grilling"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Runs a lightweight one-question-at-a-time grilling session to sharpen vague ideas before heavier planning.

# Trigger
Lightweight grilling session for brainstorming, product clarification, and early design shaping. Use when the user wants fast alignment but there is not yet enough repo context to ground a heavier doc-based review. Ask one question at a time, propose a recommended answer, and keep momentum high.

# Intended Use
Use for brainstorming, product clarification, and early design exploration when fast alignment matters more than deep repo grounding.

# Out Of Scope
Do not use once repo docs, ADRs, or code constraints become central; switch to `doc-grounded-grilling`.

# Inputs And Outputs
Inputs: a vague plan, design idea, product concept, or change request.

Outputs: a clarified idea, resolved core questions, and a recommended next artifact.

# Risks
- Risk: shallow alignment. Mitigation: escalate to doc-grounded grilling when repo-specific constraints matter.
- Risk: endless questioning. Mitigation: stop when the next concrete artifact is obvious.

# Metadata
* Group: [Discovery, Planning & Delivery](../groups/discovery-planning-delivery/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.7.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/rapid-grilling/SKILL.md)
* [SKILL_CARD.md](../../skills/rapid-grilling/SKILL_CARD.md)

# Attribution
ABVX adapted from Matt Pocock's `grill-me`, rewritten as a lightweight companion to the ABVX planning stack.
