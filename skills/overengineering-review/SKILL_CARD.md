# Skill Card: overengineering-review

## Description
Reviews code specifically for unnecessary complexity and replaceable architecture, dependencies, and layers.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for diffs, files, or repo slices where the main question is what can be deleted, collapsed, replaced with stdlib/native behavior, or reduced to a simpler shape.

## Out of Scope
Do not use as a full correctness, security, or performance review. Do not auto-apply edits unless the user separately requests implementation.

## Sources and Attribution
ABVX adapted from Dietrich Gebert `ponytail` review and audit modes, rewritten as a review-grade simplification pass with explicit boundaries and ranked actionable findings for Codex-style project work.

## Inputs and Outputs
Inputs: diff, file set, repo slice, dependency list, current design intent.

Outputs: ranked simplification findings, deletion/replacement opportunities, and compact line/file/dep reduction estimate.

## Risks and Mitigations
- Risk: oversimplifying intentional architecture. Mitigation: require a replacement and rationale for each finding.
- Risk: deleting safety-critical behavior. Mitigation: explicit boundaries for security, accessibility, trust boundaries, and data-loss prevention.
- Risk: noisy stylistic review. Mitigation: restrict findings to real complexity reductions.

## Evaluation
Evaluated by structural validation and manual review against simplification-focused code review workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
