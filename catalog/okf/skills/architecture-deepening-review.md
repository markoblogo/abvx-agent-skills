---
type: "Skill Catalog Entry"
title: "Architecture Deepening Review"
description: "Reviews codebases for deeper modules, clearer seams, lower coupling, and better testability."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/architecture-deepening-review"
tags:
  - "skill"
  - "coding-debugging-architecture"
  - "experimental"
  - "adapted"
canonical: "skills/architecture-deepening-review"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Reviews codebases for deeper modules, clearer seams, lower coupling, and better testability.

# Trigger
Review a codebase for architecture deepening opportunities: shallow modules, weak seams, scattered domain logic, low testability, high coupling, and AI-navigability friction. Use when the user asks for architecture improvement, refactoring opportunities, modularity, test seams, or maintainability review.

# Intended Use
Use for architecture audits, maintainability reviews, refactoring candidates, testability analysis, and AI-navigability improvements.

# Out Of Scope
Do not use to execute large refactors without confirmation or to re-litigate documented decisions without evidence.

# Inputs And Outputs
Inputs: repositories, README, architecture docs, ADRs, tests, domain glossary, user goals.

Outputs: ranked architecture candidates, migration suggestions, testability notes, top recommendation.

# Risks
- Risk: speculative architecture astronautics. Mitigation: tie every candidate to observed friction.
- Risk: broad churn. Mitigation: recommend one vertical slice.
- Risk: ignoring domain language. Mitigation: read glossary/docs first when available.

# Metadata
* Group: [Coding, Debugging & Architecture](../groups/coding-debugging-architecture/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.2.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/architecture-deepening-review/SKILL.md)
* [SKILL_CARD.md](../../skills/architecture-deepening-review/SKILL_CARD.md)

# Attribution
ABVX adapted from local codebase architecture review workflow.
