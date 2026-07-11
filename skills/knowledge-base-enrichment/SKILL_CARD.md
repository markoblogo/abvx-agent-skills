# Skill Card: knowledge-base-enrichment

## Description
Enriches Markdown knowledge bases with traceable tags, source provenance, related-note links, and reviewed wiki synthesis while keeping raw notes read-only by default.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for Obsidian-style vaults, Markdown research corpora, durable agent context, and source-grounded wiki refreshes.

## Out of Scope
Do not use as a general RAG service, cloud vault synchronizer, note-taking UI, or unattended writer of private source notes.

## Sources and Attribution
Adapted from `bholmesdev/llm-knowledge-base-skills`: raw-note immutability, shared tag registry, source attribution, existing-note backlinks, idempotent enrichment, generated wiki layers, and wiki linting. Rewritten for ABVX proposal-first and privacy boundaries. https://github.com/bholmesdev/llm-knowledge-base-skills

## Inputs and Outputs
Inputs: Markdown source corpus, local schema, tag registry, selected wiki scope, optional `search/read/write` memory capability, explicit apply decision.

Outputs: enrichment proposal, derived metadata/state, generated wiki updates, provenance links, and a compact verification log.

## Risks and Mitigations
- Risk: raw-note mutation. Mitigation: read-only raw layer and explicit apply boundary.
- Risk: fabricated links or sources. Mitigation: resolve targets and preserve provenance.
- Risk: private-vault leakage. Mitigation: no cloud sync or web research without approval.
- Risk: wiki drift. Mitigation: source backlinks, logs, stale-claim and orphan-link checks.
- Risk: bulk overreach. Mitigation: sample first, report scope, and require review.
- Risk: unscoped memory writes. Mitigation: per-project isolation, hybrid retrieval with source paths, and audit-gated proposal-first writes.

## Composable With
- `reversible-agent-task`
- `rabbithole-doc-exploration`
- `confidence-fragility-review`
- `skillopt-evolve-skills`

## Evaluation
Evaluate on single-note enrichment, idempotent rerun, wiki refresh, ambiguous-scope skip, and raw-layer preservation scenarios.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
