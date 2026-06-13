---
type: "Skill Catalog Entry"
title: "SkillOpt Evolve Skills"
description: "Improves local skills, AGENTS.md rules, and reusable agent workflows through validation-gated edits."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/skillopt-evolve-skills"
tags:
  - "skill"
  - "coding-debugging-architecture"
  - "experimental"
  - "original"
canonical: "skills/skillopt-evolve-skills"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Improves local skills, AGENTS.md rules, and reusable agent workflows through validation-gated edits.

# Trigger
Evolve Codex skills and agent instructions with a SkillOpt-style loop. Use when creating, refining, or auditing local skills, AGENTS.md rules, prompt playbooks, or reusable agent workflows after repeated task experience, especially when the user asks to "improve your skills", "capture this lesson", "make this reusable", or "update agent instructions".

# Intended Use
Use when repeated task experience reveals a reusable rule, failure mode, or workflow improvement worth capturing.

# Out Of Scope
Do not use to bloat always-loaded context, rewrite unrelated instructions, or merge unvalidated prompt changes.

# Inputs And Outputs
Inputs: task traces, failures, successful workflows, candidate rules, existing skill files.

Outputs: bounded skill edits, rejected-edit notes, validation reports.

# Risks
- Risk: overfitting a single task. Mitigation: generalization and non-regression checks.
- Risk: duplicate rules. Mitigation: check existing instructions before adding.
- Risk: weakening guardrails. Mitigation: validation gate and rejected-edit buffer.

# Metadata
* Group: [Coding, Debugging & Architecture](../groups/coding-debugging-architecture/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/skillopt-evolve-skills/SKILL.md)
* [SKILL_CARD.md](../../skills/skillopt-evolve-skills/SKILL_CARD.md)

# Attribution
Inspired by Microsoft SkillOpt and ABVX skill iteration practice.
