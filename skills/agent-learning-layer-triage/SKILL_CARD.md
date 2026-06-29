# Skill Card: agent-learning-layer-triage

## Description
Routes lessons from agent errors, successful patterns, review findings, and repeated workflows into the right durable layer: prompt, memory, repo docs, checklist, SKILL.md, script/tool, eval, golden fixture, or rejection buffer.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use after a task reveals a reusable lesson and the team needs to decide where that learning should live without bloating global prompts or over-promoting every note into a skill.

## Out of Scope
Do not use as a model-training claim, autonomous memory writer, secret store, or generic knowledge-base replacement. It classifies and routes learning artifacts; it does not train models.

## Sources and Attribution
ABVX original, informed by LoopOps practice, SkillOpt-style skill evolution, durable context maintenance, and public discussion of agent learning layers: model, context/memory/skills, and harness/workflow.

## Inputs and Outputs
Inputs: task trace, review finding, repeated failure, successful pattern, existing docs/skills/scripts/evals, and candidate lesson.

Outputs: compact decision record with chosen layer, rationale, target artifact, verification threshold, rejected higher layers, and one next action.

## Risks and Mitigations
- Risk: skill bloat. Mitigation: prefer the lowest durable layer that solves the repeated problem.
- Risk: overfitting a single anecdote. Mitigation: require recurrence or strong expected recurrence.
- Risk: hiding private context in publishable artifacts. Mitigation: classify private vs publishable before writing.
- Risk: replacing tests with prose. Mitigation: route regression-prone failures to evals or golden fixtures.

## Model Sensitivity
Works best on models that can separate facts, procedures, deterministic tools, and regression tests. Weaker models may need the output shape filled as a template.

## Composable With
- `skillopt-evolve-skills`
- `durable-context-maintenance`
- `goal-loop-designer`
- `delivery-preflight-gate`
- `private-vs-publishable-skill-audit`

## Anti-Patterns
- promoting every lesson into a global skill
- storing repo-local facts in global behavior layers
- creating scripts for judgment-heavy workflows
- using memory as a dumping ground for stale task history
- creating evals without a stable fixture or observable pass/fail

## Evaluation
Evaluated by structural validation and by checking whether post-task lessons are routed to smaller, more auditable artifacts than broad prompt rewrites.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
