# Skill Card: compaction-survival

## Description
Preserves the minimum high-value working state so long sessions survive compaction without expensive re-derivation.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use on long coding tasks, audits, research sessions, and any workflow where context compaction or resume loss would be expensive.

## Out of Scope
Do not use as a replacement for good repo docs, or as a license to store large stale histories and raw logs.

## Sources and Attribution
ABVX adapted from Token Optimizer ideas around compaction survival, compact checkpoints, and state restoration after long sessions.

## Inputs and Outputs
Inputs: current task state, touched files, unresolved issues, existing handoff artifacts.

Outputs: compact checkpoints, resumable state summaries, and explicit artifact pointers.

## Risks and Mitigations
- Risk: stale checkpoints. Mitigation: update only when state materially changes and remove invalidated hypotheses.
- Risk: checkpoint bloat. Mitigation: preserve only objective, evidence, next steps, and artifact paths.
- Risk: false confidence. Mitigation: keep verification and blockers explicit.

## Evaluation
Evaluated by structural validation and manual review against long-running coding and audit sessions.

## Version
0.5.0

## Reporting Issues
Open an issue in the repository.
