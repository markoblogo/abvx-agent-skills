# Skill Card: phase-spec-execution

## Description
Runs large implementation tasks through explicit, falsifiable phases with per-phase criteria, verification, and lightweight state tracking.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for medium and large coding tasks, migrations, feature slices, and brownfield changes where one-pass implementation would blur sequencing and verification.

## Out of Scope
Do not introduce formal phase specs for small edits that can be completed and verified in one loop.

## Sources and Attribution
ABVX adapted from robzilla1738 `supergoal` phase-spec and state-tracking ideas, reduced into a smaller composable workflow for ABVX skillpacks.

## Inputs and Outputs
Inputs: target outcome, repo context, dependencies, verification surface.

Outputs: ordered phases, phase-level acceptance criteria, verification commands, and lightweight execution state.

## Risks and Mitigations
- Risk: ceremonial overplanning. Mitigation: require the smallest useful phase count.
- Risk: vague phases. Mitigation: force explicit acceptance criteria and verification commands.
- Risk: stale state. Mitigation: update status only after each verification pass.

## Evaluation
Evaluated by structural validation and manual review against medium and large delivery tasks.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
