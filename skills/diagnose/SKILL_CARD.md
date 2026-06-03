# Skill Card: diagnose

## Description
Provides a feedback-loop-first diagnostic process for bugs, regressions, flaky behavior, and performance failures.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for hard debugging tasks that need reproduction, hypotheses, instrumentation, and regression checks.

## Out of Scope
Do not use to justify speculative fixes without a feedback loop or evidence.

## Sources and Attribution
ABVX adapted from local disciplined diagnosis workflow.

## Inputs and Outputs
Inputs: symptoms, logs, failing commands, code, traces, screenshots, performance data.

Outputs: repro loop, hypotheses, probes, scoped fix, regression evidence.

## Risks and Mitigations
- Risk: fixing the wrong bug. Mitigation: verify symptom match before editing.
- Risk: anchoring. Mitigation: ranked hypotheses.
- Risk: leaked debug code. Mitigation: tagged instrumentation cleanup.

## Evaluation
Evaluated by structural validation and manual review against debugging workflows.

## Version
0.2.0

## Reporting Issues
Open an issue in the repository.
