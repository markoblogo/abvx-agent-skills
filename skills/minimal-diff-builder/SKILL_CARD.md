# Skill Card: minimal-diff-builder

## Description
Builds the smallest correct implementation path for scoped tasks using a YAGNI, stdlib-first, native-first, minimal-diff ladder.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for scoped implementation work where small reviewable diffs, dependency avoidance, and local correctness matter more than extensibility theater.

## Out of Scope
Do not use to erase necessary security, accessibility, validation, or data-safety behavior. Do not force tiny diffs when the user explicitly wants a more extensible architecture.

## Sources and Attribution
ABVX adapted from Dietrich Gebert `ponytail`, rewritten as a controlled minimal-implementation workflow with explicit safety exceptions and verification expectations for Codex-style project work.

## Inputs and Outputs
Inputs: task request, local repo context, existing dependencies, verification commands.

Outputs: smallest correct patch, skipped-heavier-design note, and concise verification evidence.

## Risks and Mitigations
- Risk: underbuilding a requirement. Mitigation: restate the narrow task and report skipped heavier paths explicitly.
- Risk: simplifying away safety-critical behavior. Mitigation: hard exceptions for trust boundaries, security, accessibility, and data loss.
- Risk: unreadable tiny patches. Mitigation: prefer the smallest readable local change, not code golf.

## Model Sensitivity
Works well on strong coding models that can keep the ladder order intact without collapsing into code golf. Weaker models may need firmer reminders that "minimal" does not mean skipping correctness or safety constraints.

## Composable With
- `delivery-preflight-gate`
- `test-driven-execution`
- `overengineering-review`

## Anti-Patterns
- using this skill when the user explicitly wants a reusable framework or public extension surface
- shrinking the diff by removing validation, accessibility, or error handling that should remain
- confusing smallest correct patch with shortest possible code regardless of readability

## Evaluation
Evaluated by structural validation and manual review against scoped implementation and simplification workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
