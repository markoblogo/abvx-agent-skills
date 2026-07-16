# Skill Card: hook-rule-fixtures

## Description
Tests opt-in project hook rules with synthetic match, no-match, exception, verifier, bypass, and regression fixtures before rollout.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use after a project hook rule is designed and before it moves from disabled to warn or block.

## Out of Scope
Do not use live session observation, production data, raw protected artifacts, or global-hook telemetry as a substitute for fixtures.

## Sources and Attribution
ABVX original fixture discipline, informed by ECC's pattern-and-condition rule structure.

## Inputs and Outputs
Inputs: frozen rule version, event schema, synthetic cases, expected outcomes, and rollout target.

Outputs: fixture matrix, assertion results, regressions, and a disabled/warn/block recommendation.

## Risks and Mitigations
- Risk: testing with sensitive data. Mitigation: require minimal synthetic fixtures and redacted evidence assertions.
- Risk: blocking on untested logic. Mitigation: require match, no-match, exception, and bypass cases.
- Risk: silent rule drift. Mitigation: freeze rule version and retain regressions.

## Evaluation
Evaluated by deterministic synthetic fixture runs and manual review of rollout decisions.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
