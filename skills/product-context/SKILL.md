---
name: product-context
description: Build or refresh a compact, evidence-backed product context before marketing, positioning, SEO, analytics, sales-enablement, or launch work. Use when an agent needs to understand the product, audience, proof, conversion goal, terminology, and claim boundaries without inventing commercial facts.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Product Context

Create a small, durable context artifact that lets later product work start from evidence instead of generic positioning.

## Use When

- entering marketing, content, SEO, analytics, sales, or launch work in a repo;
- the product, audience, conversion action, or proof boundary is unclear;
- existing public copy and internal product behavior have drifted.

## Workflow

1. Read existing product docs, public copy, analytics contracts, and relevant implementation surfaces.
2. Separate confirmed facts from assumptions, placeholders, and claims needing owner confirmation.
3. Draft or update `docs/product-context.md` unless the repo already defines a better canonical path.
4. Keep only: product and audience, jobs and conversion action, terminology, proof and known limits, approved voice, prohibited claims, source surfaces, and last-reviewed date.
5. Ask for confirmation where positioning, ICP, pricing, competitor claims, or proof cannot be established from the repo.
6. Link future work to the context; do not treat it as permission to publish, spend, contact people, or change product behavior.

## Guardrails

- Never invent customer quotes, metrics, market position, availability, pricing, partner status, or legal/compliance claims.
- Keep personal data and private sales evidence out of a committed context file.
- Treat a product context as a reviewable input, not a source of truth over code, current policy, or human direction.
- Preserve domain-specific safety language such as financial, booking, or approval boundaries.

## Output Shape

Use these headings where applicable: `Product`, `Audience and jobs`, `Conversion action`, `Proof and limits`, `Language`, `Claim boundaries`, `Source surfaces`, `Maintenance`.

## Pair With

- `evidence-ledger-research` for external facts;
- `social-publishing-gate` before distribution;
- `bounded-growth-loop` before recurring optimization;
- `loop-readiness-review` before scheduling any loop.

## Provenance

Adapted from the shared-context architecture in `coreyhaines31/marketingskills`, narrowed to evidence-backed, product-neutral context with explicit claim boundaries.
