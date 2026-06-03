# Skill Card: dynamic-workflow-packets

## Description
Plans and runs large Codex tasks with compact workflow packets, risk gates, integration, and verification.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for large coding, research, audit, migration, or job/client-search workflows where independent packets reduce drift and improve verification.

## Out of Scope
Do not use for small one-shot tasks. Do not use to bypass user approval for destructive, external, expensive, or privacy-sensitive actions.

## Sources and Attribution
Inspired by DannyMac180 `codex-dynamic-workflows`, CodexSaver bounded delegation patterns, and ABVX workflow practice.

## Inputs and Outputs
Inputs: task goals, repositories, sources, constraints, approval context.

Outputs: packet plans, workflow artifacts, integration decisions, verification evidence, final reports.

## Risks and Mitigations
- Risk: process overhead on small tasks. Mitigation: decision rule says to work directly when orchestration is unnecessary.
- Risk: unsafe delegation. Mitigation: risk gates and disjoint packet ownership.
- Risk: raw packet dumps hide conflicts. Mitigation: explicit integration phase.

## Evaluation
Evaluated by structural validation and manual review against multi-track coding, research, and job/client-search scenarios.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
