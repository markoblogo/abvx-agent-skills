# Skill Card: project-context-bootstrap

## Description
Bootstraps durable project context through stack detection, user discovery, compact context docs, and approval-gated updates.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when entering an unfamiliar repo, preparing a project for repeatable agent work, installing a workflow layer into an existing codebase, or replacing stale guesswork with durable project context.

## Out of Scope
Do not use to force a large harness, overwrite good existing docs, or create a sprawling process directory without clear need.

## Sources and Attribution
ABVX adapted from vibecode-pro-max-kit setup and context-generation flows, rewritten as a compact Codex-style onboarding skill.

## Inputs and Outputs
Inputs: repo manifests, existing docs, user answers, current code structure.

Outputs: confirmed project understanding, compact context entrypoints, and approval-gated context updates.

## Risks and Mitigations
- Risk: generic docs. Mitigation: require code inspection plus user confirmation before writing.
- Risk: context sprawl. Mitigation: keep startup docs small and defer deeper material behind explicit paths.
- Risk: clobbering good repo docs. Mitigation: study existing context first and ask before reorganizing.

## Evaluation
Evaluated by structural validation and manual review against repo-onboarding and context-bootstrap scenarios.

## Version
0.6.0

## Reporting Issues
Open an issue in the repository.
