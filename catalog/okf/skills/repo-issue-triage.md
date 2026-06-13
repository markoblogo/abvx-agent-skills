---
type: "Skill Catalog Entry"
title: "Repo Issue Triage"
description: "Moves bugs and enhancements through a compact state machine so backlog items become actionable instead of lingering in vague limbo."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/repo-issue-triage"
tags:
  - "skill"
  - "discovery-planning-delivery"
  - "experimental"
  - "adapted"
canonical: "skills/repo-issue-triage"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Moves bugs and enhancements through a compact state machine so backlog items become actionable instead of lingering in vague limbo.

# Trigger
Triage bugs, enhancements, and backlog items through a small state machine that works with or without a formal issue tracker. Use when reviewing incoming requests, preparing work for an agent, deciding whether more info is needed, or keeping a multi-project backlog healthy.

# Intended Use
Use for issue review, backlog hygiene, agent-readiness checks, and multi-project operational queues.

# Out Of Scope
Do not use as a substitute for actual reproduction or decision-making; the state machine is a tool, not the judgment itself.

# Inputs And Outputs
Inputs: issues, requests, comments, codebase signals, prior notes.

Outputs: category/state recommendations, triage notes, and readiness decisions.

# Risks
- Risk: vague triage. Mitigation: require explicit established facts and exact missing info.
- Risk: state confusion. Mitigation: enforce one category and one state.
- Risk: premature delegation. Mitigation: verify reproduction or clarification before `ready-for-agent`.

# Metadata
* Group: [Discovery, Planning & Delivery](../groups/discovery-planning-delivery/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.7.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/repo-issue-triage/SKILL.md)
* [SKILL_CARD.md](../../skills/repo-issue-triage/SKILL_CARD.md)

# Attribution
ABVX adapted from Matt Pocock's `triage`, rewritten for issue-tracker-neutral repo operations.
