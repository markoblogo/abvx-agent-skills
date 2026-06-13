---
type: "Skill Catalog Entry"
title: "Dynamic Workflow Packets"
description: "Plans and runs large Codex tasks with compact workflow packets, risk gates, integration, and verification."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/dynamic-workflow-packets"
tags:
  - "skill"
  - "workflow-handoffs-multitrack"
  - "experimental"
  - "original"
canonical: "skills/dynamic-workflow-packets"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Plans and runs large Codex tasks with compact workflow packets, risk gates, integration, and verification.

# Trigger
Plan and run large Codex tasks with compact dynamic workflow packets, risk gates, integration, and verification. Use when the user explicitly asks for dynamic workflows, packets, subagents, swarm, orchestration, long-running audits, multi-track coding/research work, job or client search agent design, migrations, repo-wide reviews, or tasks where independent discovery, implementation, review, and verification tracks would reduce drift.

# Intended Use
Use for large coding, research, audit, migration, or job/client-search workflows where independent packets reduce drift and improve verification.

# Out Of Scope
Do not use for small one-shot tasks. Do not use to bypass user approval for destructive, external, expensive, or privacy-sensitive actions.

# Inputs And Outputs
Inputs: task goals, repositories, sources, constraints, approval context.

Outputs: packet plans, workflow artifacts, integration decisions, verification evidence, final reports.

# Risks
- Risk: process overhead on small tasks. Mitigation: decision rule says to work directly when orchestration is unnecessary.
- Risk: unsafe delegation. Mitigation: risk gates and disjoint packet ownership.
- Risk: raw packet dumps hide conflicts. Mitigation: explicit integration phase.

# Metadata
* Group: [Workflow, Handoffs & Multi-Track Work](../groups/workflow-handoffs-multitrack/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/dynamic-workflow-packets/SKILL.md)
* [SKILL_CARD.md](../../skills/dynamic-workflow-packets/SKILL_CARD.md)

# Attribution
Inspired by DannyMac180 `codex-dynamic-workflows`, CodexSaver bounded delegation patterns, and ABVX workflow practice.
