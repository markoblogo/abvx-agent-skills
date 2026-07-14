# Skill Card: agent-friction-ledger

## Description
Captures material agent-development friction as a local, privacy-safe report with durable improvement proposals.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use after explicit request or repeated, evidenced friction involving blockers, error quality, documentation gaps, tool incompatibility, or manual workarounds.

## Out of Scope
Do not use as passive surveillance, a complete transcript, telemetry, an issue tracker, or an external reporting service.

## Sources and Attribution
Adapted from `aurorascharff/agent-friction-skill`.

## Inputs and Outputs
Inputs: task boundary, material friction events, attempted actions, evidence, and redaction constraints.

Outputs: a local Markdown report with root-cause confidence, resolution, durable fix proposal, and categorized actions.

## Risks and Mitigations
- Risk: sensitive leakage. Mitigation: local-only report, no raw transcripts/logs, and abstract sensitive cases.
- Risk: noisy process. Mitigation: explicit trigger and material-friction threshold.
- Risk: speculative fixes. Mitigation: mark confidence and require normal authorization before applying follow-ups.

## Evaluation
Evaluated by structural validation and manual review against repeated developer-tooling blockers and clean sessions where the skill should not run.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
