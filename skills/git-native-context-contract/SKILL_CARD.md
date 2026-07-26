# Skill Card: git-native-context-contract

## Description
Creates or reviews minimal Git-native project context with seven document types, human-gated lifecycle, directed relations, and evidence-backed code-change patterns.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for durable decisions, proposals, rules, specifications, plans, bounded research, and recurring incident/code-change lessons that should remain reviewable in Git.

## Out of Scope
Not a memory service, RAG system, MCP server, hook installer, session injector, protected evidence store, runtime ledger, transcript archive, or replacement for existing project truth.

## Sources and Attribution
Adapted from `archcore-ai/cli`, reduced to a provider-neutral ABVX contract without adopting its runtime or full taxonomy.

## Inputs and Outputs
Inputs: authoritative project evidence, existing documentation layout, proposed document type/status, approval evidence, relations, and verification.

Outputs: proposal-first typed Markdown, validated lifecycle state, relation records, and verification result.

## Risks and Mitigations
- Risk: competing source of truth. Mitigation: update existing canonical docs and preserve project truth hierarchy.
- Risk: documentation bureaucracy. Mitigation: seven types only; create nothing when no type fits.
- Risk: agents self-approve. Mitigation: three-field explicit human acceptance record.
- Risk: relation graph noise. Mitigation: existing endpoints, four relation types, no duplicates or self-links.
- Risk: incident folklore. Mitigation: `cpat` requires observed verification and durable prevention.

## Model Sensitivity
Weaker models need explicit type-selection examples, authoritative source paths, and mechanical lifecycle/relation validation.

## Composable With
- `durable-context-maintenance`
- `evidence-ledger-research`
- `agent-tool-contract-review`
- `repo-debugging-ledger`

## Anti-Patterns
- creating a new directory when existing docs already own the subject
- accepting a document without explicit human approval fields
- using `related` for every nearby document
- writing a `cpat` from an unverified hypothesis
- storing secrets, protected evidence, transcripts, or hidden reasoning

## Evaluation
Structural validation and scenario review for type choice, lifecycle transitions, approval gating, relation integrity, source-of-truth conflicts, and complete `cpat` evidence.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
