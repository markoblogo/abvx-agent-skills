# Skill Card: graph-guided-code-reading

## Description
Reduces repository-reading token waste by navigating code through entrypoints, symbols, dependencies, and blast radius instead of broad reading.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use on medium-to-large repos, PR reviews, architecture questions, onboarding, debugging across modules, and long-running audits.

## Out of Scope
Do not force this workflow on tiny repos where direct reading is cheaper, or when exact raw artifacts matter more than structural navigation.

## Sources and Attribution
ABVX adapted from Code Review Graph ideas around persistent code graphs, targeted review context, and blast-radius-first reading.

## Inputs and Outputs
Inputs: task goal, changed files or entrypoint, available code-navigation tools.

Outputs: a compact focus set, narrow reads around relevant nodes, and a smaller evidence surface.

## Risks and Mitigations
- Risk: missing an indirect dependency. Mitigation: expand one edge at a time and include nearby tests and contracts.
- Risk: overengineering on small repos. Mitigation: skip formal graphing when two or three files already answer the question.
- Risk: stale focus set. Mitigation: keep a checked-location ledger and refresh only when a new hypothesis appears.

## Evaluation
Evaluated by structural validation and manual review against architecture, review, debugging, and audit workflows.

## Version
0.4.0

## Reporting Issues
Open an issue in the repository.
