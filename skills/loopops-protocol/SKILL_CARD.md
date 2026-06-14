# Skill Card: loopops-protocol

## Description
Designs reusable agent behavior as the smallest reliable artifact: prompt, skill, checklist, script, workflow, or cost-bounded loop.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when repeated agent work should be captured, promoted, pruned, or compiled into a workflow or autonomous loop with evaluator, memory, and stop rules.

## Out of Scope
Do not use to turn small one-off tasks into process overhead, run unbounded autonomous agents, or replace deterministic tests with model judgment when real checks exist.

## Sources and Attribution
Inspired by ABVX skill iteration practice, SkillOpt-style skill evolution, dynamic workflow patterns, Claude Code `/goal` and workflow concepts, and public discussion around loop engineering.

## Inputs and Outputs
Inputs: repeated task traces, existing skills, candidate prompts, workflow notes, test commands, logs, review findings, evaluator options, and cost constraints.

Outputs: artifact-level decision, supervisor contract, loop budget, memory policy, validation plan, and bounded skill/workflow/script edits.

## Risks and Mitigations
- Risk: token burn from unbounded loops. Mitigation: require budget, stop rules, and escalation.
- Risk: over-engineering small tasks. Mitigation: choose the lowest reliable artifact.
- Risk: weak self-evaluation. Mitigation: prefer deterministic evaluators and separate review where feasible.
- Risk: skill bloat. Mitigation: update skills only with procedural, reusable, testable lessons.

## Model Sensitivity
Works best on models that reliably follow multi-step procedural instructions and respect explicit budgets and stop rules. Smaller or more improvisational models may over-promote prompts into heavier artifacts unless the boundary language is kept sharp.

## Composable With
- `dynamic-workflow-packets`
- `skillopt-evolve-skills`
- `delivery-preflight-gate`
- `token-efficient-execution`

## Anti-Patterns
- using LoopOps for one-off tasks with no repeated failure or cost signal
- promoting directly from prompt to loop without proving that a checklist, skill, or script is insufficient
- relying on model judgment where a deterministic test or script already exists

## Evaluation
Evaluated by structural validation, manual review, and application to ABVX skill design decisions where prompt-like guidance is promoted only when reliability or reuse justifies it.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
