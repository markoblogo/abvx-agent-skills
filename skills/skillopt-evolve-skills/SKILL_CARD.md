# Skill Card: skillopt-evolve-skills

## Description
Improves local skills, AGENTS.md rules, and reusable agent workflows through validation-gated edits.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when repeated task experience reveals a reusable rule, failure mode, or workflow improvement worth capturing.

## Out of Scope
Do not use to bloat always-loaded context, rewrite unrelated instructions, or merge unvalidated prompt changes.

## Sources and Attribution
Inspired by Microsoft SkillOpt and ABVX skill iteration practice.

## Inputs and Outputs
Inputs: task traces, failures, successful workflows, candidate rules, existing skill files.

Outputs: bounded skill edits, rejected-edit notes, validation reports.

## Risks and Mitigations
- Risk: overfitting a single task. Mitigation: generalization and non-regression checks.
- Risk: duplicate rules. Mitigation: check existing instructions before adding.
- Risk: weakening guardrails. Mitigation: validation gate and rejected-edit buffer.

## Evaluation
Evaluated by structural validation and manual review against local skill updates made in project work.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
