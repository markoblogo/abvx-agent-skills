# Skill Card: filesystem-context-discipline

## Description
Uses files as durable context without polluting the live prompt.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for scratchpads, plan persistence, evidence ledgers, retained outputs, proposal folders, handoffs, and repo-local context.

## Out of Scope
Do not use to persist every thought, hide important decisions in untracked files, or turn scratchpads into authoritative docs.

## Sources and Attribution
Adapted from filesystem-context patterns in `muratcankoylan/Agent-Skills-for-Context-Engineering`.

## Inputs and Outputs
Inputs: task state, generated outputs, plans, logs, evidence, settlement decisions.

Outputs: typed filesystem artifacts with authority level, discovery cues, and update or expiry triggers.

## Risks and Mitigations
- Risk: stale files become false authority. Mitigation: include status and update triggers.
- Risk: context sprawl. Mitigation: choose the narrowest sensible location.
- Risk: accidental commit of transient files. Mitigation: clean or classify before commit.

## Evaluation
Evaluated by structural validation and manual review against long-running repo tasks and proposal-first workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
