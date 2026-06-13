---
type: "Skill Catalog Entry"
title: "Skill Effectiveness Audit"
description: "Reads skill reflection artifacts and turns them into a bounded audit of which skills to keep, tighten, split, or de-emphasize."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/skill-effectiveness-audit"
tags:
  - "skill"
  - "research-knowledge-methods"
  - "experimental"
  - "original"
canonical: "skills/skill-effectiveness-audit"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Reads skill reflection artifacts and turns them into a bounded audit of which skills to keep, tighten, split, or de-emphasize.

# Trigger
Audit whether installed or proposed skills appear to help, drift, or add noise using docs/ai/skill-usage.json and docs/ai/skill-effectiveness.md. Use when a repo exports skill reflection artifacts and you need to decide which skills to keep, tighten, de-emphasize, or rewrite before adding more agent instruction surface.

# Intended Use
Use when `agentsgen reflect skills` artifacts exist and you want evidence-led guidance on whether a skill is helping, weakly positioned, noisy, or ready for a small rewrite.

# Out Of Scope
Do not score skills from aesthetics alone. Do not perform broad skill rewrites without a specific signal from the reflection artifacts and local repo context.

# Inputs And Outputs
Inputs: `docs/ai/skill-usage.json`, `docs/ai/skill-effectiveness.md`, related `SKILL.md` and `SKILL_CARD.md` files, local workflow context.

Outputs: ranked skill findings, likely causes, and a smallest-useful edit set for the next iteration.

# Risks
- Risk: overreacting to low-signal data. Mitigation: distinguish rare from harmful.
- Risk: changing too many skills at once. Mitigation: recommend the smallest testable edit set.
- Risk: blaming the wrong layer. Mitigation: check trigger wording, startup context, and overlapping instructions before rewriting the skill body.

# Metadata
* Group: [Research, Knowledge & Reusable Methods](../groups/research-knowledge-methods/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/skill-effectiveness-audit/SKILL.md)
* [SKILL_CARD.md](../../skills/skill-effectiveness-audit/SKILL_CARD.md)

# Attribution
ABVX original, informed by the repository's skill-quality evaluation stance and the experimental reflection outputs from `AGENTS.md_generator`.
