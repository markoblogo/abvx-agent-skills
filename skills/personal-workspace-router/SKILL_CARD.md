# Skill Card: personal-workspace-router

## Description

Designs and maintains a local personal AI workspace with a root router, isolated domain folders, user-triggered memory, decision logs, and sparse routing corrections.

## Owner

ABVX / Anton Biletskiy-Volokh

## License

MIT. See repository LICENSE.

## Intended Use

Use when a user wants one agent workspace spanning multiple projects, products, or personal domains without mixing context or loading every memory on every task.

## Out of Scope

Do not use for a single repo with normal docs, for automatic memory capture, or for storing secrets/private transcripts. Use `project-context-bootstrap` for ordinary repo onboarding.

## Sources and Attribution

ABVX adapted. Informed by personal AI workspace patterns in Bykov Digital's public `CLAUDE.md — Universal Personal AI Workspace Template`: root routing, isolated folder memory, decision logs, and routing corrections. The ABVX version is rewritten for Codex-style repo work, sparse logging, and user-triggered memory only.

## Inputs and Outputs

Inputs: user domains, routing signals, repo paths, safety boundaries, memory policy, and existing local workspace files.

Outputs: root `AGENTS.md`, isolated domain folders, user-triggered `MEMORY.md` files, `DECISIONS.md`, and `ROUTING-LOG.md` policy.

## Risks and Mitigations

- Risk: memory bloat. Mitigation: user-triggered writes only.
- Risk: routing ritual slows work. Mitigation: state routing only when it materially affects the task.
- Risk: private data leakage. Mitigation: never store secrets, credentials, private contacts, or bulky transcripts.
- Risk: workspace rules override repo safety. Mitigation: repo-local `AGENTS.md`, tests, and approval gates remain authoritative for implementation.

## Evaluation

Evaluated by structural validation and manual review against multi-domain ABVX local workspace setup and repo-routing workflows.

## Composable With

- `project-context-bootstrap`
- `durable-context-maintenance`
- `doc-grounded-grilling`
- `agent-learning-layer-triage`

## Anti-Patterns

- one giant memory file for every domain;
- writing memory without explicit user instruction;
- logging every successful route;
- asking for confirmation before every routine micro-step.

## Version

0.1.0

## Reporting Issues

Open an issue in the repository.
