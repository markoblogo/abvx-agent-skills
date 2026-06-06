# Skill Card: recovery-loop-3strike

## Description
Adds a bounded retry-escalate-handoff loop so agents stop spinning on the same failure and preserve useful evidence when blocked.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when verification has failed, when autonomous execution needs a hard stop condition, or when environment noise and partial fixes make repeated retries expensive.

## Out of Scope
Do not invoke for one-off typos that are already understood and fixed within the same loop.

## Sources and Attribution
ABVX adapted from robzilla1738 `supergoal` three-strike recovery model, rewritten into a host-agnostic recovery discipline for ABVX skills.

## Inputs and Outputs
Inputs: failing signal, attempted verification, current phase or task context.

Outputs: bounded retries, focused fix-spec escalation, or a blocked handoff with evidence.

## Risks and Mitigations
- Risk: premature handoff. Mitigation: require one evidence-bearing retry and one focused fix-spec first.
- Risk: repetitive spinning. Mitigation: cap the loop at three materially different attempts.
- Risk: vague blocker reports. Mitigation: require a per-strike failure record.

## Evaluation
Evaluated by structural validation and manual review against debugging and autonomous execution scenarios.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
