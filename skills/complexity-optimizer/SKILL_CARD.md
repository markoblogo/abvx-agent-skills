# Skill Card: complexity-optimizer

## Description
Finds and fixes algorithmic complexity and performance hotspots with behavior-preserving discipline.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for codebase performance audits, slow paths, large input handling, rendering churn, N+1 calls, and safe optimization work.

## Out of Scope
Do not use for broad rewrites, premature micro-optimizations, or semantic changes without user intent and verification.

## Sources and Attribution
ABVX adapted from local complexity optimization workflow.

## Inputs and Outputs
Inputs: codebase, performance symptoms, test commands, benchmarks, traces, profiling output.

Outputs: ranked findings, scoped patches, before/after complexity estimates, verification evidence.

## Risks and Mitigations
- Risk: breaking behavior while improving speed. Mitigation: establish tests or invariants first.
- Risk: optimizing cold code. Mitigation: rank by impact and data size.
- Risk: unsafe batching. Mitigation: recheck authorization, ordering, pagination, and filters.

## Evaluation
Evaluated by structural validation and manual review against complexity-audit workflows.

## Version
0.2.0

## Reporting Issues
Open an issue in the repository.
