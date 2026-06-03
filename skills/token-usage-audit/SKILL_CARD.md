# Skill Card: token-usage-audit

## Description
Audits token waste categories and maps them to the smallest useful corrective skill or policy change.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when token budget is tight, sessions are degrading, or a Codex setup needs measurement-driven context optimization.

## Out of Scope
Do not build heavyweight telemetry or dashboards when a dominant waste category is already obvious from local evidence.

## Sources and Attribution
ABVX adapted from Token Optimizer ideas around waste categorization, intervention loops, and verifying whether optimization actually helped.

## Inputs and Outputs
Inputs: current session behavior, startup docs, shell usage, repeated-read patterns, compaction pain points.

Outputs: a ranked waste diagnosis, corrective skills or config changes, and expected savings.

## Risks and Mitigations
- Risk: over-instrumentation. Mitigation: use coarse categories and local evidence first.
- Risk: optimizing the wrong layer. Mitigation: rank waste categories before acting.
- Risk: audit churn. Mitigation: record only the highest-value findings and interventions.

## Evaluation
Evaluated by structural validation and manual review against constrained-budget agent sessions.

## Version
0.5.0

## Reporting Issues
Open an issue in the repository.
