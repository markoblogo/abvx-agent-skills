---
type: "Skill Catalog Entry"
title: "Doc Grounded Grilling"
description: "Aligns plans against the repo's existing docs, domain language, and decisions through a one-question-at-a-time grilling session."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/doc-grounded-grilling"
tags:
  - "skill"
  - "discovery-planning-delivery"
  - "experimental"
  - "adapted"
canonical: "skills/doc-grounded-grilling"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Aligns plans against the repo's existing docs, domain language, and decisions through a one-question-at-a-time grilling session.

# Trigger
Stress-test a plan, feature, or design against the repo's existing docs, domain language, ADRs, and context files. Use when a task is ambiguous, terminology is fuzzy, architecture trade-offs matter, or the user wants alignment before implementation. Ask one question at a time, inspect the codebase when answers are already present, and sharpen the project's language as decisions crystallize.

# Intended Use
Use before implementation when a plan is ambiguous, terminology is fuzzy, or existing docs and ADRs must shape the decision.

# Out Of Scope
Do not use as endless interrogation or as a replacement for implementation planning once the plan is already clear.

# Inputs And Outputs
Inputs: user plan, repo docs, codebase signals, ADRs, context files.

Outputs: clarified language, resolved trade-offs, explicit open questions, and doc-refresh pointers.

# Risks
- Risk: over-questioning. Mitigation: stop when ambiguity is materially reduced.
- Risk: doc drift. Mitigation: cross-check answers against code and flag docs needing maintenance.
- Risk: terminological confusion. Mitigation: force canonical terms early.

# Metadata
* Group: [Discovery, Planning & Delivery](/groups/discovery-planning-delivery/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.7.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/doc-grounded-grilling/SKILL.md)
* [SKILL_CARD.md](../../skills/doc-grounded-grilling/SKILL_CARD.md)

# Attribution
ABVX adapted from Matt Pocock's `grill-with-docs`, rewritten for ABVX repo docs, ADRs, design assets, and Codex-style project work.
