# Skill Card: session-retrospective

## Description
Reads session reflection artifacts and turns them into a compact retrospective with concrete next-session changes.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when `agentsgen reflect sessions` artifacts already exist and you want to understand drift, redirects, long-session behavior, or where the next workflow change should land.

## Out of Scope
Do not replay or summarize full transcripts when the derived reflection artifacts are present. Do not overfit one anomalous session into a durable rule.

## Sources and Attribution
ABVX original, built to consume the experimental reflection artifacts emitted by `AGENTS.md_generator`.

## Inputs and Outputs
Inputs: `docs/ai/agent-signals.json`, `docs/ai/session-patterns.md`, `docs/ai/agent-sessions.json`, repo-local context docs, recent workflow changes.

Outputs: a compact retrospective, strongest patterns, proposed next-session changes, and owning skills or docs.

## Risks and Mitigations
- Risk: reading noise as pattern. Mitigation: prefer repeated signals across sessions.
- Risk: duplicating transcript analysis. Mitigation: start from generated artifacts.
- Risk: vague recommendations. Mitigation: tie each change to one observed signal.

## Evaluation
Evaluated by structural validation and manual review against long-running Codex session retrospectives.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
