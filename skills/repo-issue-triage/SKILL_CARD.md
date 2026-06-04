# Skill Card: repo-issue-triage

## Description
Moves bugs and enhancements through a compact state machine so backlog items become actionable instead of lingering in vague limbo.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for issue review, backlog hygiene, agent-readiness checks, and multi-project operational queues.

## Out of Scope
Do not use as a substitute for actual reproduction or decision-making; the state machine is a tool, not the judgment itself.

## Sources and Attribution
ABVX adapted from Matt Pocock's `triage`, rewritten for issue-tracker-neutral repo operations.

## Inputs and Outputs
Inputs: issues, requests, comments, codebase signals, prior notes.

Outputs: category/state recommendations, triage notes, and readiness decisions.

## Risks and Mitigations
- Risk: vague triage. Mitigation: require explicit established facts and exact missing info.
- Risk: state confusion. Mitigation: enforce one category and one state.
- Risk: premature delegation. Mitigation: verify reproduction or clarification before `ready-for-agent`.

## Evaluation
Evaluated by structural validation and manual review against issue-review and backlog workflows.

## Version
0.7.0

## Reporting Issues
Open an issue in the repository.
