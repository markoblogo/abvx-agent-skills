# Skill Card: pr-write

## Description
Create or update a concise GitHub pull request for an already verified code change. Use when the user asks to open or file a PR, or invokes pr-write. Do not publish a PR when the user only asks for draft wording.

## Owner
ABVX / markoblogo

## License
MIT. See repository LICENSE and references/tstack-MIT.txt for the upstream notice.

## Intended Use
Create or update a concise GitHub pull request for an already verified code change. Use when the user asks to open or file a PR, or invokes pr-write. Do not publish a PR when the user only asks for draft wording.

## Out of Scope
Provider changes, permission bypasses, automatic merging, deployment and package releases. Respect the user's authorized scope for external writes.

## Sources and Attribution
Adapted from Theo Browne's MIT-licensed t3dotgg/tstack workflows (file-pr and leaving-pr-comments), reviewed on 2026-10-28. https://github.com/t3dotgg/tstack
Rewrite for Codex-native tools, explicit authority boundaries and bounded execution. No Claude or T3 Code runtime is required.

## Inputs and Outputs
Inputs: the user's goal, repository instructions, scoped Git changes and available GitHub evidence.
Outputs: evidence-backed findings or an explicit PR/workflow state, with unresolved gates and verification limits.

## Risks and Mitigations
Creating a PR can expose unrelated changes or private details. Distinguish text-only requests, inspect the diff and draft, and verify the returned URL.

## Model Sensitivity
Works with connected GitHub tools or authenticated gh; publication is unavailable without write access.

## Composable With
- pr-ready
- pr-takeover
- pr-ci-watch

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
