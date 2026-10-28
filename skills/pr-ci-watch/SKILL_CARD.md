# Skill Card: pr-ci-watch

## Description
Monitor a specific GitHub pull request through CI and review within a bounded active session. Use when explicitly asked to watch CI, babysit a PR, or invoke pr-ci-watch. Monitoring alone does not authorize code fixes, public replies, or merging.

## Owner
ABVX / markoblogo

## License
MIT. See repository LICENSE and references/tstack-MIT.txt for the upstream notice.

## Intended Use
Monitor a specific GitHub pull request through CI and review within a bounded active session. Use when explicitly asked to watch CI, babysit a PR, or invoke pr-ci-watch. Monitoring alone does not authorize code fixes, public replies, or merging.

## Out of Scope
Provider changes, permission bypasses, automatic merging, deployment and package releases. Respect the user's authorized scope for external writes.

## Sources and Attribution
Adapted from Theo Browne's MIT-licensed t3dotgg/tstack workflows (babysit-pr), reviewed on 2026-10-28. https://github.com/t3dotgg/tstack
Rewrite for Codex-native tools, explicit authority boundaries and bounded execution. No Claude or T3 Code runtime is required.

## Inputs and Outputs
Inputs: the user's goal, repository instructions, scoped Git changes and available GitHub evidence.
Outputs: evidence-backed findings or an explicit PR/workflow state, with unresolved gates and verification limits.

## Risks and Mitigations
Green CI can hide stale heads, missing reviews or missing required checks. Pin the head, report CI separately from readiness, and bound observation time.

## Model Sensitivity
Requires complete GitHub metadata and authenticated gh for continuous local watching; connector-only environments may support only a snapshot.

## Composable With
- pr-ready
- pr-write
- bug-evidence-protocol

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
