---
type: "Skill Catalog Entry"
title: "Session Retrospective"
description: "Reads session reflection artifacts and turns them into a compact retrospective with concrete next-session changes."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/session-retrospective"
tags:
  - "skill"
  - "workflow-handoffs-multitrack"
  - "experimental"
  - "original"
canonical: "skills/session-retrospective"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Reads session reflection artifacts and turns them into a compact retrospective with concrete next-session changes.

# Trigger
Review recent agent sessions through derived artifacts such as docs/ai/agent-sessions.json, docs/ai/agent-signals.json, and docs/ai/session-patterns.md. Use when a repo already exports session reflection artifacts and you need a compact retrospective on drift, redirects, prompt shape, long-session behavior, or what should change before the next run.

# Intended Use
Use when `agentsgen reflect sessions` artifacts already exist and you want to understand drift, redirects, long-session behavior, or where the next workflow change should land.

# Out Of Scope
Do not replay or summarize full transcripts when the derived reflection artifacts are present. Do not overfit one anomalous session into a durable rule.

# Inputs And Outputs
Inputs: `docs/ai/agent-signals.json`, `docs/ai/session-patterns.md`, `docs/ai/agent-sessions.json`, repo-local context docs, recent workflow changes.

Outputs: a compact retrospective, strongest patterns, proposed next-session changes, and owning skills or docs.

# Risks
- Risk: reading noise as pattern. Mitigation: prefer repeated signals across sessions.
- Risk: duplicating transcript analysis. Mitigation: start from generated artifacts.
- Risk: vague recommendations. Mitigation: tie each change to one observed signal.

# Metadata
* Group: [Workflow, Handoffs & Multi-Track Work](../groups/workflow-handoffs-multitrack/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/session-retrospective/SKILL.md)
* [SKILL_CARD.md](../../skills/session-retrospective/SKILL_CARD.md)

# Attribution
ABVX original, built to consume the experimental reflection artifacts emitted by `AGENTS.md_generator`.
