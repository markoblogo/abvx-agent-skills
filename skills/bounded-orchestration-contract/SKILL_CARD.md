# Skill Card: bounded-orchestration-contract

## Description
Coordinates opt-in Planner, Reviewer, and bounded Executor work with a five-round cap, stable findings, disjoint ownership, explicit route evidence, and root verification.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for non-trivial planning, adversarial review, or independent multi-agent implementation slices where a separate review gate reduces material risk.

## Out of Scope
Not a scheduler, model router, provider bridge, permission grant, persistent policy, or replacement for root and human authority. Avoid on small or tightly coupled tasks.

## Sources and Attribution
Adapted from `Cjbuilds/Codex-Orchestration`, reduced to a provider-neutral ABVX contract without adopting the plugin runtime.

## Inputs and Outputs
Inputs: task constraints, acceptance criteria, repo facts, risks, route evidence, executor slices, and verification requirements.

Outputs: versioned plan state, stable findings ledger, bounded executor packets, route states, handoffs, and root verification record.

## Risks and Mitigations
- Risk: ceremony on small tasks. Mitigation: explicit non-trivial-task trigger.
- Risk: false route claims. Mitigation: three exact evidence states and host-metadata requirement for confirmation.
- Risk: parallel write collisions. Mitigation: disjoint ownership gate.
- Risk: rubber-stamp review. Mitigation: stable findings, reasoned dispositions, and five-round fail-closed cap.
- Risk: child output treated as accepted. Mitigation: mandatory root integration and verification.

## Model Sensitivity
Weaker models need smaller packets, explicit file ownership, and stricter ledger/version checks.

## Composable With
- `dynamic-workflow-packets`
- `agent-tool-contract-review`
- `test-driven-execution`
- `handoff`

## Anti-Patterns
- using Planner and Reviewer as the same supposedly independent route
- renumbering or dropping findings between rounds
- parallelizing shared files, lockfiles, registries, migrations, or generated artifacts
- reporting `used and confirmed` from child prose or accepted tool parameters
- skipping root verification after executor completion

## Evaluation
Structural validation plus scenario review for approval, round exhaustion, finding disposition, ownership collision, route evidence, and root verification.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
