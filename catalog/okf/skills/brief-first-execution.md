---
type: "Skill Catalog Entry"
title: "Brief First Execution"
description: "Creates and maintains a single working brief for non-trivial tasks so scope, non-goals, risks, verification, and done criteria do not drift."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/brief-first-execution"
tags:
  - "skill"
  - "research-knowledge-methods"
  - "experimental"
  - "original"
canonical: "skills/brief-first-execution"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Creates and maintains a single working brief for non-trivial tasks so scope, non-goals, risks, verification, and done criteria do not drift.

# Trigger
Create a single working brief before substantial implementation, audit, or migration work. Use when tasks are non-trivial, risks are real, or the session is likely to drift without one source of truth for scope, non-goals, verification, and done criteria.

# Intended Use
Use before substantial implementation, audits, migrations, or long-running tasks that need one stable source of truth.

# Out Of Scope
Do not force a brief onto tiny low-risk edits where the ceremony costs more than the clarity.

# Inputs And Outputs
Inputs: user request, repo context, blast radius, known risks, expected verification.

Outputs: a compact task brief that can be updated as the work evolves.

# Risks
- Risk: stale briefs. Mitigation: require updates when scope changes materially.
- Risk: empty ceremony. Mitigation: skip for trivial work and keep the brief compact.
- Risk: verification added too late. Mitigation: define checks before deep implementation starts.

# Metadata
* Group: [Research, Knowledge & Reusable Methods](/groups/research-knowledge-methods/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/brief-first-execution/SKILL.md)
* [SKILL_CARD.md](../../skills/brief-first-execution/SKILL_CARD.md)

# Attribution
ABVX original, shaped by repeated long-session execution where drift and implicit scope caused more waste than the coding itself.
