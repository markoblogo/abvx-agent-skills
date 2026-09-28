# Skill Card: test-driven-execution

## Description
Guides feature work and bug fixes through a vertical-slice red-green-refactor loop centered on behavior, not implementation details.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for coding tasks, regressions, and bug fixes where tests should drive the implementation and provide stable feedback.

## Out of Scope
Do not force TDD where the repo has no realistic test seam and the cost would outweigh the feedback benefit.

## Sources and Attribution
ABVX adapted from Matt Pocock's `tdd`, rewritten for compact ABVX execution loops. Scoped isolation, evidence separation, and visual before/after proof were additionally informed by [michaelshimeles/skills](https://github.com/michaelshimeles/skills).

## Inputs and Outputs
Inputs: desired behavior, current code, existing tests, public seams.

Outputs: behavior-focused tests, minimal implementation slices, evidence-bounded verification, and safer refactor steps.

## Risks and Mitigations
- Risk: implementation-coupled tests. Mitigation: require public-interface and refactor-survival checks.
- Risk: horizontal slicing. Mitigation: enforce one failing test at a time.
- Risk: overtesting. Mitigation: confirm priority behaviors before writing tests.
- Risk: overstating evidence or release status. Mitigation: report local checks, CI, deployment, and release as separate gates.

## Evaluation
Evaluated by structural validation and manual review against feature and bug-fix workflows.

## Version
0.8.0

## Reporting Issues
Open an issue in the repository.
