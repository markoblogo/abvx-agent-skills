---
type: "Skill Catalog Entry"
title: "Handoff"
description: "Creates compact, operational handoff documents for continuation across agents, sessions, or humans."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/handoff"
tags:
  - "skill"
  - "workflow-handoffs-multitrack"
  - "experimental"
  - "adapted"
canonical: "skills/handoff"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Creates compact, operational handoff documents for continuation across agents, sessions, or humans.

# Trigger
Create compact handoff documents for another agent, session, or human to continue work. Use when a task is long-running, context is about to compact, work must pause, an audit needs resumable state, or the user asks for a handoff, continuation note, checkpoint, or next-session brief.

# Intended Use
Use for long-running work, context compaction, paused tasks, audits, debugging, research, and multi-repo workflows.

# Out Of Scope
Do not use for transcript dumps, private data archives, or replacing durable project docs.

# Inputs And Outputs
Inputs: conversation state, repo status, plans, commands, commits, URLs, decisions.

Outputs: compact handoff document and next-step summary.

# Risks
- Risk: leaking sensitive data. Mitigation: redact and link instead of copying.
- Risk: losing active state. Mitigation: include status, commands, blockers, and next steps.
- Risk: stale handoff. Mitigation: include concrete timestamps or commit IDs.

# Metadata
* Group: [Workflow, Handoffs & Multi-Track Work](../groups/workflow-handoffs-multitrack/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.2.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/handoff/SKILL.md)
* [SKILL_CARD.md](../../skills/handoff/SKILL_CARD.md)

# Attribution
ABVX adapted from local handoff workflow.
