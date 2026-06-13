---
type: "Skill Catalog Entry"
title: "Workflow Policy Layering"
description: "Separates workflow steps from authority, forbidden actions, escalation paths, and validation gates so assistant specs stop contradicting themselves."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/workflow-policy-layering"
tags:
  - "skill"
  - "research-knowledge-methods"
  - "experimental"
  - "original"
canonical: "skills/workflow-policy-layering"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Separates workflow steps from authority, forbidden actions, escalation paths, and validation gates so assistant specs stop contradicting themselves.

# Trigger
Separate workflow instructions from safety, authority, escalation, and validation rules. Use when an assistant, agent, or skill pack is getting muddled because process steps, permissions, forbidden actions, and review gates are mixed together.

# Intended Use
Use when agent instructions are getting muddled because process, permissions, review, and safety are all mixed into one unstable block.

# Out Of Scope
Do not use as a substitute for actual legal, safety, or product policy review. It organizes policy; it does not invent trustworthy policy from nothing.

# Inputs And Outputs
Inputs: current workflow description, authority assumptions, escalation expectations, validation needs.

Outputs: layered spec with explicit workflow, authority, escalation, and validation sections.

# Risks
- Risk: fake certainty about authority. Mitigation: require explicit allowed / confirm / forbidden separation.
- Risk: vague refusals. Mitigation: define escalation as concrete next-step guidance.
- Risk: policy hidden in prose. Mitigation: split layers before rewriting.

# Metadata
* Group: [Research, Knowledge & Reusable Methods](../groups/research-knowledge-methods/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/workflow-policy-layering/SKILL.md)
* [SKILL_CARD.md](../../skills/workflow-policy-layering/SKILL_CARD.md)

# Attribution
ABVX original, distilled from repeated assistant-boundary and workflow-layering work across product and development settings.
