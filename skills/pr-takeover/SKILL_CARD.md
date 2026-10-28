# Skill Card: pr-takeover

## Description
Continue an existing PR, branch or handoff after verifying its intent, current code and remaining work. Use when explicitly asked to take over unfinished development or invoke pr-takeover. Preserve user changes and contributor credit.

## Owner
ABVX / markoblogo

## License
MIT. See repository LICENSE and references/tstack-MIT.txt for the upstream notice.

## Intended Use
Continue an existing PR, branch or handoff after verifying its intent, current code and remaining work. Use when explicitly asked to take over unfinished development or invoke pr-takeover. Preserve user changes and contributor credit.

## Out of Scope
Provider changes, permission bypasses, automatic merging, deployment and package releases. Respect the user's authorized scope for external writes.

## Sources and Attribution
Adapted from Theo Browne's MIT-licensed t3dotgg/tstack workflows (takeover), reviewed on 2026-10-28. https://github.com/t3dotgg/tstack
Rewrite for Codex-native tools, explicit authority boundaries and bounded execution. No Claude or T3 Code runtime is required.

## Inputs and Outputs
Inputs: the user's goal, repository instructions, scoped Git changes and available GitHub evidence.
Outputs: evidence-backed findings or an explicit PR/workflow state, with unresolved gates and verification limits.

## Risks and Mitigations
A handoff may conceal stale code, unrelated dirty work or lost authorship. Reconstruct from source, preserve commits and verify the original behavior.

## Model Sensitivity
Works with native Git/GitHub tools; independent review is optional and must be reported separately when unavailable.

## Composable With
- pr-modernize
- pr-write
- pr-ready

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
