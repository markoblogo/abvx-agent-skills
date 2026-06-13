---
type: "Skill Catalog Entry"
title: "Durable Context Maintenance"
description: "Maintains repo-local durable context so agent-facing docs stay accurate, compact, and useful after code and workflow changes."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/durable-context-maintenance"
tags:
  - "skill"
  - "project-context-onboarding"
  - "experimental"
  - "adapted"
canonical: "skills/durable-context-maintenance"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Maintains repo-local durable context so agent-facing docs stay accurate, compact, and useful after code and workflow changes.

# Trigger
Keep repo-local agent context accurate after code and workflow changes. Use when docs/ai, AGENTS.md, runbooks, or context entrypoints have drifted from the codebase, after major feature work, after architecture changes, or when an agent keeps rediscovering the same repo facts. Refresh durable context, split groups only when needed, and preserve compact read order.

# Intended Use
Use after feature work, architecture changes, test-flow changes, docs drift, or repeated repo rediscovery by agents.

# Out Of Scope
Do not use to dump task history into permanent docs or to create sprawling context trees that cost more than they save.

# Inputs And Outputs
Inputs: current context files, recent code changes, repo structure, workflow changes.

Outputs: refreshed durable docs, corrected routing entrypoints, and a cleaner read order for future sessions.

# Risks
- Risk: stale docs survive unnoticed. Mitigation: tie refreshes to real code and workflow changes.
- Risk: too many files. Mitigation: split only when a topic is genuinely separable and repeatedly needed.
- Risk: permanent docs become session logs. Mitigation: keep history out and preserve only durable operational knowledge.

# Metadata
* Group: [Project Context & Onboarding](../groups/project-context-onboarding/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.6.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/durable-context-maintenance/SKILL.md)
* [SKILL_CARD.md](../../skills/durable-context-maintenance/SKILL_CARD.md)

# Attribution
ABVX adapted from vibecode-pro-max-kit context-generation and context-maintenance ideas, rewritten for compact durable repo context.
