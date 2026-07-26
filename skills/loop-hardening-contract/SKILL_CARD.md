# Skill Card: loop-hardening-contract

## Description
Hardens repeated delivery with harness-stripping experiments, immutable runtime-path sprint packets, and broken-window revalidation without automatic revert.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for repeated Cardputer, browser, CI, runtime, or production sprints after the loop has passed a readiness review.

## Out of Scope
Not a runner, scheduler, automatic rollback mechanism, deployment policy, or substitute for device/production evidence.

## Sources and Attribution
Adapted from selected ideas in `Archive228/loopkit`.

## Inputs and Outputs
Inputs: accepted result, runtime path, sprint boundary, predicates, budgets, harness inventory, and verification evidence.

Outputs: versioned sprint packet, revalidation status, optional harness experiment verdict, root verification, settlement, and remaining risks.

## Risks and Mitigations
- Risk: removing a safety control as “overhead.” Mitigation: protected controls are never candidates for stripping.
- Risk: executor self-certification. Mitigation: runtime-path evidence and root-owned verification are mandatory.
- Risk: destructive recovery. Mitigation: reopen and repair; never auto-revert.

## Composable With
- `loop-readiness-review`
- `bounded-evaluation`
- `bug-evidence-protocol`
- `git-native-context-contract`
- `bounded-orchestration-contract`

## Anti-Patterns
- changing multiple harness components in one experiment;
- rewriting an accepted sprint packet in place;
- claiming device or production behavior from compilation;
- automatic revert after a failed revalidation.

## Evaluation
Validate the contract structure and apply it to one repeated runtime-path sprint with independently reviewable evidence.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
