---
name: knowledge-base-enrichment
description: Enrich a Markdown knowledge base with durable tags, source provenance, existing-note links, and reviewed wiki synthesis while keeping raw notes read-only by default. Use when organizing Obsidian-style notes, refreshing generated wikis, or preparing source-grounded context for agents.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Knowledge Base Enrichment

Turn raw Markdown notes into a traceable knowledge base without silently rewriting the source layer.

## Use When

- enriching one note with tags, source attribution, or related-note links;
- organizing a vault or Markdown corpus into generated wikis;
- refreshing a wiki from new or changed source notes;
- preparing durable, source-grounded context for an agent or reader workflow.

## Default Layout

```text
vault/
  raw/       # source notes; read-only by default
  wikis/     # generated synthesis; writable only in the selected scope
  tags.md    # shared tag registry
  .knowledge-base/
    state.json
    proposals/
    logs/
```

Adapt to an existing layout after inspecting it. Do not create a parallel vault when a clear local structure already exists.

## Workflow

1. State the source root, writable output scope, and whether the user explicitly authorized apply.
2. Read the local tag registry and the target wiki's `AGENTS.md`/`index.md` before proposing changes.
3. Read the target note and inspect existing frontmatter without rewriting its body.
4. Propose only evidence-backed metadata:
   - reusable kebab-case topic tags;
   - `source` and `url` when the origin is real and known;
   - links to related notes that actually exist.
5. Keep the proposal under `.knowledge-base/proposals/` until it is inspected and explicitly applied.
6. On apply, write derived metadata/state and generated wiki pages in the selected scope. Keep `raw/` content unchanged unless the user explicitly authorizes a source edit.
7. Record changed sources, skipped ambiguities, unresolved links, and the verification result in a log.

## Idempotence

- Track enrichment state in `.knowledge-base/state.json`, not by adding silent stamps to raw notes.
- Skip notes whose content hash and enrichment inputs are unchanged.
- Reuse existing tags; add a new tag only when it is broadly reusable and record why.
- Never invent source URLs, related-note targets, claims, or wiki entities.

## Optional Memory Capability

When a runner exposes a project-memory capability, use it through this order:

1. `search` the current project scope before planning or mutating;
2. `read` the complete source document behind a relevant result;
3. draft a proposed `write` for a durable decision, constraint, or lesson;
4. audit and inspect the proposal before applying it.

Prefer hybrid retrieval (`full_text` plus `semantic`) with full-text fallback. Keep cross-project reads disabled unless explicitly authorized. Treat memory writes as derived artifacts, never as implicit completion evidence.

## Wiki Refresh

For each selected wiki:

1. Read its local schema first; it overrides this skill.
2. Find new or changed source notes that fit the wiki scope.
3. Update source summaries, concept/entity pages, index counts, and source backlinks.
4. Update the overview only for durable synthesis changes.
5. Lint unresolved links, orphan pages, stale claims, duplicate concepts, missing provenance, and skipped ambiguities.

If scope is ambiguous, skip the note and log the question instead of guessing.

## Bulk Mode

Bulk enrichment is opt-in and review-gated. Before running it, report the note count, writable paths, model/provider, and expected artifacts. Prefer a small sample first. Do not sync a private vault to a cloud runner or use web research unless the user explicitly authorizes it.

## Hard Boundaries

- Raw notes are read-only by default; never delete or rewrite them in unattended mode.
- Do not expose private notes, credentials, or vault contents to external services without explicit approval.
- Do not treat generated wiki prose as a source of truth; retain source links and provenance.
- Do not apply bulk changes when the proposal, source scope, or evaluator is unclear.

## Pair With

- `reversible-agent-task` for proposal -> inspect -> select/apply/discard settlement;
- `rabbithole-doc-exploration` for human review of dense source/wikis;
- `confidence-fragility-review` for checking generated claims against sources;
- `skillopt-evolve-skills` when repeated enrichment failures justify improving this skill.

## Verification

Before reporting completion, check:

- raw files are unchanged unless explicitly authorized;
- every emitted link resolves to an existing note;
- every generated claim has a source or is marked as synthesis;
- state is idempotent on a second run;
- skipped or ambiguous items are logged;
- the final diff stays within the approved writable scope.

## Final Report

Report source scope, derived files changed, raw files preserved, tags/provenance/link decisions, skipped ambiguities, verification, and whether the result is still a proposal or explicitly applied.
