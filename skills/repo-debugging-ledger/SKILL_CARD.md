# Skill Card: repo-debugging-ledger

## Description
Debugs repositories with a hypothesis ledger, checked-location ledger, loop breakers, and verification.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for failing tests, CI failures, regressions, flaky bugs, local tooling errors, and investigations that risk repeated searches.

## Out of Scope
Do not use to justify speculative fixes without a repro signal. Do not skip project checks when they are available.

## Sources and Attribution
ABVX original, informed by repeated debugging loops and Codex-style repo work.

## Inputs and Outputs
Inputs: failing commands, stack traces, codebases, logs, test results, reproduction notes.

Outputs: hypotheses, probes, checked-location ledger, scoped fixes, verification evidence.

## Risks and Mitigations
- Risk: anchoring on first plausible cause. Mitigation: ranked hypotheses before edits.
- Risk: repeated broad searches. Mitigation: checked-location ledger.
- Risk: false confidence. Mitigation: rerun original repro and project checks.

## Evaluation
Evaluated by structural validation and manual review against debugging and CI-failure workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
