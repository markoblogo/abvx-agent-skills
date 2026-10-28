# Skill Card: codex-review-loop

## Description
Review a code change with one independent OpenAI reviewer and at most three rounds. Use when the user explicitly requests bounded independent review or invokes codex-review-loop. Do not trigger on a casual mention of review or start a loop for trivial edits.

## Owner
ABVX / markoblogo

## License
MIT. See repository LICENSE and references/tstack-MIT.txt for the upstream notice.

## Intended Use
Review a code change with one independent OpenAI reviewer and at most three rounds. Use when the user explicitly requests bounded independent review or invokes codex-review-loop. Do not trigger on a casual mention of review or start a loop for trivial edits.

## Out of Scope
Provider changes, permission bypasses, automatic merging, deployment and package releases. Respect the user's authorized scope for external writes.

## Sources and Attribution
Adapted from Theo Browne's MIT-licensed t3dotgg/tstack workflows (sol-loop), reviewed on 2026-10-28. https://github.com/t3dotgg/tstack
Rewrite for Codex-native tools, explicit authority boundaries and bounded execution. No Claude or T3 Code runtime is required.

## Inputs and Outputs
Inputs: the user's goal, repository instructions, scoped Git changes and available GitHub evidence.
Outputs: evidence-backed findings or an explicit PR/workflow state, with unresolved gates and verification limits.

## Risks and Mitigations
A reviewer may approve stale code or encourage scope creep. Freeze the base, tie approval to the final diff, verify findings and stop after three rounds.

## Model Sensitivity
Requires native independent OpenAI subagents for the independent-review claim; quality depends on reviewer capability. No provider or model is silently substituted.

## Composable With
- pr-ready
- minimal-diff-builder
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
