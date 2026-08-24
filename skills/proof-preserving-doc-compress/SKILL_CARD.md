# Skill Card: proof-preserving-doc-compress

## Description
Compresses ABVX project documents without silently losing facts, decisions, constraints, provenance, or uncertainty.

## Intended Use
Use for context packs, handoffs, proposals, evidence notes, task briefs, and release or operational documents.

## Out of Scope
Not a free summarizer, quality reviewer, contract approver, publisher, or automatic memory writer.

## Sources and Attribution
Adapted from `ML-SystemDesign/MLSystemDesign/skills/lossless-doc-compress`; the local contract adds ABVX provenance, privacy, approval, and explicit-unknown boundaries.

## Inputs and Outputs
Inputs: complete source document, source identity, project contract, and owner intent.

Outputs: compressed document, removal log, and scorecard. Judgment calls remain visible as flags.

## Risks and Mitigations
- Semantic drift: preserve sacred fields and use `FLAG` when equivalence is uncertain.
- False losslessness: record baseline and run a structural fidelity check.
- Context leakage: respect the target project's scope and privacy boundary.

## Evaluation
`fixture_checked`; see `benchmarks/fixture-cases/proof-preserving-doc-compress.json`.

## Version
0.1.0
