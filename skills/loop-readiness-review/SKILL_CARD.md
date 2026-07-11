# Skill Card: loop-readiness-review

## Description
Reviews whether a recurring or semi-autonomous agent loop is ready to run.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use before scheduling or promoting repeated agent workflows such as CI sweeping, PR babysitting, issue triage, dependency sweeping, changelog drafting, daily triage, or SET runner handoffs.

## Out of Scope
Do not use as a loop runtime, scheduler, auto-merge policy, or approval substitute.

## Sources and Attribution
Adapted from readiness and loop engineering patterns in `cobusgreyling/loop-engineering`.

## Inputs and Outputs
Inputs: loop plans, SET bundles, workflow docs, state files, run logs, budget rules, verifier evidence, human gate rules.

Outputs: readiness level, blockers, budget and stop rules, human gate, smallest next step, and go/no-go decision.

## Risks and Mitigations
- Risk: premature autonomy. Mitigation: require state, verifier, budget, run log, rollback, and human gate before governed loops.
- Risk: verifier theater. Mitigation: require deterministic or independently reviewable evidence.
- Risk: runaway cost. Mitigation: require time, token, run-count, and retry caps.

## Evaluation
Evaluated by structural validation and manual review against loop plans, SET bundles, and recurring agent workflow designs.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
