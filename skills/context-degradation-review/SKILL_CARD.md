# Skill Card: context-degradation-review

## Description
Reviews agent context for poisoning, lost-in-the-middle failures, distraction, clashes, and stale carryover.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use before long-session handoffs, SET runner handoffs, skill changes, memory writes, and complex tasks where too much or conflicting context may degrade behavior.

## Out of Scope
Do not use as a generic prose critique, automatic memory deletion tool, or substitute for source verification.

## Sources and Attribution
Adapted from context-degradation patterns in `muratcankoylan/Agent-Skills-for-Context-Engineering`.

## Inputs and Outputs
Inputs: user request, memory excerpts, repo docs, handoffs, SET bundles, logs, generated summaries.

Outputs: context degradation verdict, reviewed sources, failure-mode findings, smallest context repair.

## Risks and Mitigations
- Risk: over-compressing useful context. Mitigation: demote only low-signal, stale, or conflicting material.
- Risk: overriding the current user. Mitigation: current user instructions outrank memory and summaries.
- Risk: generic critique. Mitigation: require named failure mode and repair.

## Evaluation
Evaluated by structural validation and manual review against handoff, memory, SET bundle, and long-session tasks.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
