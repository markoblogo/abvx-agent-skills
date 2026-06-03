# Skill Card: durable-context-maintenance

## Description
Maintains repo-local durable context so agent-facing docs stay accurate, compact, and useful after code and workflow changes.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use after feature work, architecture changes, test-flow changes, docs drift, or repeated repo rediscovery by agents.

## Out of Scope
Do not use to dump task history into permanent docs or to create sprawling context trees that cost more than they save.

## Sources and Attribution
ABVX adapted from vibecode-pro-max-kit context-generation and context-maintenance ideas, rewritten for compact durable repo context.

## Inputs and Outputs
Inputs: current context files, recent code changes, repo structure, workflow changes.

Outputs: refreshed durable docs, corrected routing entrypoints, and a cleaner read order for future sessions.

## Risks and Mitigations
- Risk: stale docs survive unnoticed. Mitigation: tie refreshes to real code and workflow changes.
- Risk: too many files. Mitigation: split only when a topic is genuinely separable and repeatedly needed.
- Risk: permanent docs become session logs. Mitigation: keep history out and preserve only durable operational knowledge.

## Evaluation
Evaluated by structural validation and manual review against repo-drift and context-refresh scenarios.

## Version
0.6.0

## Reporting Issues
Open an issue in the repository.
