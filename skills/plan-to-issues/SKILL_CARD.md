# Skill Card: plan-to-issues

## Description
Breaks PRDs and plans into thin, end-to-end slices that can be executed by agents or humans.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when a plan or PRD needs to become concrete tickets, task slices, or issue-tracker-ready work units.

## Out of Scope
Do not use for horizontal decomposition when the real work should ship in vertical slices.

## Sources and Attribution
ABVX adapted from Matt Pocock's `to-issues`, rewritten for output-neutral issue slicing and ABVX execution flows.

## Inputs and Outputs
Inputs: PRDs, plans, specs, codebase seams, user approval on granularity.

Outputs: issue-ready vertical slices with acceptance criteria and blockers.

## Risks and Mitigations
- Risk: slices too large. Mitigation: bias toward thinner end-to-end paths.
- Risk: slices too abstract. Mitigation: require verifiable acceptance criteria.
- Risk: wrong dependency graph. Mitigation: review blockers before publishing.

## Evaluation
Evaluated by structural validation and manual review against execution-planning workflows.

## Version
0.7.0

## Reporting Issues
Open an issue in the repository.
