# Skill Card: handoff

## Description
Creates compact, operational handoff documents for continuation across agents, sessions, or humans.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for long-running work, context compaction, paused tasks, audits, debugging, research, and multi-repo workflows.

## Out of Scope
Do not use for transcript dumps, private data archives, or replacing durable project docs.

## Sources and Attribution
ABVX adapted from local handoff workflow.

## Inputs and Outputs
Inputs: conversation state, repo status, plans, commands, commits, URLs, decisions.

Outputs: compact handoff document and next-step summary.

## Risks and Mitigations
- Risk: leaking sensitive data. Mitigation: redact and link instead of copying.
- Risk: losing active state. Mitigation: include status, commands, blockers, and next steps.
- Risk: stale handoff. Mitigation: include concrete timestamps or commit IDs.

## Evaluation
Evaluated by structural validation and manual review against long-running task transfers.

## Version
0.2.0

## Reporting Issues
Open an issue in the repository.
