# Skill Card: bug-evidence-protocol

## Description
Captures and classifies auditable red-to-green bug evidence without replacing diagnosis or test-driven implementation.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use after a credible reproducer exists, especially for regressions, production incidents, device failures, flaky behavior, and recurring CI/runtime defects.

## Out of Scope
Not an autonomous bug scanner, static-analysis finding generator, general test runner, production executor, protected evidence store, or mandatory approval workflow for ordinary scoped local changes.

## Sources and Attribution
Adapted from `Kappaemme-git/codex-bug-reproducer`, narrowed to an ABVX evidence protocol with risk-based approval and machine-captured broader checks.

## Inputs and Outputs
Inputs: targeted before/after commands, symptom-match decision, captured broader checks, Git state, route evidence, optional `cpat_id`.

Outputs: bounded command records and a classified JSON evidence packet.

## Risks and Mitigations
- Risk: false `FIX_PROVEN`. Mitigation: same command hash plus captured passing broader checks.
- Risk: setup failure mislabeled as bug. Mitigation: explicit symptom-match requirement.
- Risk: sensitive output retained. Mitigation: bounded redaction, no environment dump, mandatory inspection before publication.
- Risk: ceremony on ordinary fixes. Mitigation: opt-in use after a credible reproducer or where auditability matters.
- Risk: approval deadlock. Mitigation: gates are risk-based and preserve existing scoped authorization.

## Composable With
- `diagnose`
- `test-driven-execution`
- `git-native-context-contract`
- `repo-debugging-ledger`

## Evaluation
Unit and smoke checks cover command identity, redaction, mismatched commands, missing broader evidence, broader regressions, and valid red-to-green classification.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
