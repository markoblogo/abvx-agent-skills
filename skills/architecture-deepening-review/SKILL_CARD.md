# Skill Card: architecture-deepening-review

## Description
Reviews codebases for deeper modules, clearer seams, lower coupling, and better testability.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for architecture audits, maintainability reviews, refactoring candidates, testability analysis, and AI-navigability improvements.

## Out of Scope
Do not use to execute large refactors without confirmation or to re-litigate documented decisions without evidence.

## Sources and Attribution
ABVX adapted from local codebase architecture review workflow.

## Inputs and Outputs
Inputs: repositories, README, architecture docs, ADRs, tests, domain glossary, user goals.

Outputs: ranked architecture candidates, migration suggestions, testability notes, top recommendation.

## Risks and Mitigations
- Risk: speculative architecture astronautics. Mitigation: tie every candidate to observed friction.
- Risk: broad churn. Mitigation: recommend one vertical slice.
- Risk: ignoring domain language. Mitigation: read glossary/docs first when available.

## Evaluation
Evaluated by structural validation and manual review against architecture-audit workflows.

## Version
0.2.0

## Reporting Issues
Open an issue in the repository.
