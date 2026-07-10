# Skill Card: reversible-agent-task

## Description
Runs risky or multi-file agent work as a retained, inspectable proposal before anything is applied to the target workspace.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when an agent task needs reversible execution discipline: proposal output first, inspection next, then an explicit select/apply/discard settlement.

## Out of Scope
Do not use as a full agent runtime, sandbox implementation, PR manager, or replacement for Git review.

## Sources and Attribution
Adapted from reversible trace and retained-output patterns in `shepherd-agents/shepherd`, expressed as a host-agnostic ABVX skill.

## Inputs and Outputs
Inputs: task brief, target workspace, proposal workspace, expected artifacts, verification commands, SET bundle if present.

Outputs: lifecycle state, retained-output location, artifacts, verification evidence, settlement action, blockers, and assumptions.

## Risks and Mitigations
- Risk: fake reversibility while mutating the target workspace. Mitigation: state the target/proposal boundary before running.
- Risk: process overhead on tiny edits. Mitigation: skip for low-risk one-file changes.
- Risk: unreviewed apply. Mitigation: require inspect before select/apply.

## Evaluation
Evaluated by structural validation and manual review against SET bundle, worktree, and retained-output scenarios.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
