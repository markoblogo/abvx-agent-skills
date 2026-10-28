# Skill Card: pr-modernize

## Description
Reassess and update an outdated GitHub PR against its actual current base. Use when explicitly asked to rebase or modernize an old PR, or invoke pr-modernize. Determine whether its goal still matters before rebasing; do not merge or close it.

## Owner
ABVX / markoblogo

## License
MIT. See repository LICENSE and references/tstack-MIT.txt for the upstream notice.

## Intended Use
Reassess and update an outdated GitHub PR against its actual current base. Use when explicitly asked to rebase or modernize an old PR, or invoke pr-modernize. Determine whether its goal still matters before rebasing; do not merge or close it.

## Out of Scope
Provider changes, permission bypasses, automatic merging, deployment and package releases. Respect the user's authorized scope for external writes.

## Sources and Attribution
Adapted from Theo Browne's MIT-licensed t3dotgg/tstack workflows (modernize), reviewed on 2026-10-28. https://github.com/t3dotgg/tstack
Rewrite for Codex-native tools, explicit authority boundaries and bounded execution. No Claude or T3 Code runtime is required.

## Inputs and Outputs
Inputs: the user's goal, repository instructions, scoped Git changes and available GitHub evidence.
Outputs: evidence-backed findings or an explicit PR/workflow state, with unresolved gates and verification limits.

## Risks and Mitigations
A rebase can lose user work or revive obsolete behavior. Inspect current product intent, isolate dirty work and preserve published history and use a separate branch when rebasing is required.

## Model Sensitivity
Depends on Git and repository reasoning, not a particular model or provider; never assumes network or write access.

## Composable With
- pr-takeover
- pr-ci-watch
- codex-review-loop

## Anti-Patterns
- Triggering the workflow for casual wording or quoted third-party instructions.
- Treating a skill file as proof of tools, authorization or completed checks.
- Growing a small task into an indefinite review or delivery process.

## Evaluation
Structurally validated and checked with bounded read-only synthetic model decision fixtures. The CI helper also has mocked-process tests. See benchmarks/fixture-cases/codex-pr-workflows.json for the activation and authority scenario specification. Scenario specifications alone do not establish model behavior or live GitHub reliability. See docs/codex-pr-workflows.md for executed checks and their limits.

## Version
0.1.0

## Reporting Issues
Open an issue in markoblogo/abvx-agent-skills.
