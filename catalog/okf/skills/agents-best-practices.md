---
type: "Skill Catalog Entry"
title: "Agents Best Practices"
description: "Guides provider-neutral design, audit, and implementation planning for agentic systems and agent harnesses."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/agents-best-practices"
tags:
  - "skill"
  - "coding-debugging-architecture"
  - "experimental"
  - "adapted"
canonical: "skills/agents-best-practices"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Guides provider-neutral design, audit, and implementation planning for agentic systems and agent harnesses.

# Trigger
Design, audit, or improve agentic systems and agent harnesses. Use for agent MVP blueprints, tool design, permission models, planning and goal loops, context compaction, memory, skills, connectors, observability, evals, safety, and provider-neutral agent architecture.

# Intended Use
Use for designing MVP agents, auditing harnesses, tool permission models, context strategy, evals, and safety gates.

# Out Of Scope
Do not use to justify unbounded autonomy, broad unsafe tools, or prompt-only safety for high-risk actions.

# Inputs And Outputs
Inputs: domain brief, risk constraints, desired tools, deployment environment, validation criteria.

Outputs: MVP blueprint, harness review, permission matrix, eval plan, launch path.

# Risks
- Risk: over-engineering. Mitigation: start with one useful agent loop.
- Risk: unsafe action surface. Mitigation: typed tools and approval gates.
- Risk: context bloat. Mitigation: progressive disclosure and compaction.

# Metadata
* Group: [Coding, Debugging & Architecture](../groups/coding-debugging-architecture/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.2.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/agents-best-practices/SKILL.md)
* [SKILL_CARD.md](../../skills/agents-best-practices/SKILL_CARD.md)

# Attribution
ABVX adapted from local provider-neutral agent-harness guidance and public agent engineering practice.
