---
type: "Skill Catalog Entry"
title: "LoopOps Protocol"
description: "Designs reusable agent behavior as the smallest reliable artifact: prompt, skill, checklist, script, workflow, or cost-bounded loop."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/loopops-protocol"
tags:
  - "skill"
  - "research-knowledge-methods"
  - "experimental"
  - "original"
canonical: "skills/loopops-protocol"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Designs reusable agent behavior as the smallest reliable artifact: prompt, skill, checklist, script, workflow, or cost-bounded loop.

# Trigger
Design and evolve agent skills into cost-bounded loops, workflows, scripts, and memory updates. Use when creating or auditing reusable agent methods, converting prompts or skills into workflows, designing open or closed agent loops, defining supervisor/evaluator contracts, or deciding whether repeated agent work should become a skill, checklist, script, workflow, or autonomous loop.

# Intended Use
Use when repeated agent work should be captured, promoted, pruned, or compiled into a workflow or autonomous loop with evaluator, memory, and stop rules.

# Out Of Scope
Do not use to turn small one-off tasks into process overhead, run unbounded autonomous agents, or replace deterministic tests with model judgment when real checks exist.

# Inputs And Outputs
Inputs: repeated task traces, existing skills, candidate prompts, workflow notes, test commands, logs, review findings, evaluator options, and cost constraints.

Outputs: artifact-level decision, supervisor contract, loop budget, memory policy, validation plan, and bounded skill/workflow/script edits.

# Risks
- Risk: token burn from unbounded loops. Mitigation: require budget, stop rules, and escalation.
- Risk: over-engineering small tasks. Mitigation: choose the lowest reliable artifact.
- Risk: weak self-evaluation. Mitigation: prefer deterministic evaluators and separate review where feasible.
- Risk: skill bloat. Mitigation: update skills only with procedural, reusable, testable lessons.

# Metadata
* Group: [Research, Knowledge & Reusable Methods](../groups/research-knowledge-methods/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/loopops-protocol/SKILL.md)
* [SKILL_CARD.md](../../skills/loopops-protocol/SKILL_CARD.md)

# Attribution
Inspired by ABVX skill iteration practice, SkillOpt-style skill evolution, dynamic workflow patterns, Claude Code `/goal` and workflow concepts, and public discussion around loop engineering.
