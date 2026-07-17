---
name: git-native-context-contract
description: Create or review minimal Git-native project context using only adr, rfc, rule, spec, plan, rnd, and cpat documents; human-gated draft/accepted/rejected lifecycle; implements, depends_on, extends, and related relations; and evidence-backed code-change patterns. Use when a project needs durable decisions, specifications, research, plans, incident lessons, or the SET git-native-context capability without installing a context runtime.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Git-Native Context Contract

Use this skill to retain a small amount of durable project truth in reviewable Markdown. It is opt-in and provider-neutral. It does not install Archcore, configure MCP, add hooks, inject session context, or create a competing memory runtime.

## Authority and storage

Prefer the repository's existing documentation layout: `docs/`, `docs/ai/`, `docs/adr/`, architecture records, or another documented project-owned path. Create a new context directory only when the user explicitly requests one or no suitable durable location exists.

Project truth already encoded in code, tests, signed agreements, product contracts, protected evidence stores, runtime ledgers, or approved docs remains authoritative. Never copy secrets, private customer data, protected evidence, transcripts, or hidden reasoning into these documents.

All writes are proposal-first:

```text
proposal -> inspect -> apply
```

## Minimal types

Use only:

- `adr`: a finalized architecture or technical decision, alternatives, and consequences.
- `rfc`: a significant proposed change still open for review.
- `rule`: an imperative engineering or operating standard with enforcement guidance.
- `spec`: a normative behavior contract for a component, interface, schema, protocol, or subsystem.
- `plan`: bounded implementation work with dependencies, acceptance criteria, and verification.
- `rnd`: a time-boxed investigation ending in a recommendation and next action.
- `cpat`: a durable code-change or incident pattern.

Do not invent another type because the topic feels different. Additional types require an explicit project-level contract change.

## Type selection

- Decision already made: `adr`; still proposed: `rfc`.
- Required human/team practice: `rule`; required system behavior: `spec`.
- Open question: `rnd`; committed execution sequence: `plan`.
- Reusable lesson from a defect, incident, CI failure, or production/runtime repair: `cpat`.

If none fits, do not create a document.

## Frontmatter

Use the repository's existing format when one exists. Otherwise use:

```yaml
---
id: <stable-project-id>
type: adr | rfc | rule | spec | plan | rnd | cpat
title: <human-readable title>
status: draft | accepted | rejected
created: YYYY-MM-DD
updated: YYYY-MM-DD
approved_by: null
approved_at: null
approval_reference: null
---
```

IDs remain stable across moves and revisions. Do not encode secrets or personal identifiers in IDs or approval references.

## Lifecycle

Every new document starts as `draft`.

Allowed transitions:

```text
draft -> accepted
draft -> rejected
accepted -> rejected
```

`rejected` is terminal unless the project explicitly defines a supersession workflow. Preserve rejected documents when they capture a useful dead end or superseded decision.

An agent may recommend acceptance but must not set `accepted` without explicit human approval. Acceptance requires all three fields:

- `approved_by` — a project-approved human identifier;
- `approved_at` — an ISO date or timestamp;
- `approval_reference` — the review, issue, PR, meeting record, or explicit user instruction authorizing acceptance.

Missing or inferred approval keeps the document `draft`. Do not use agent completion, CI success, a merge, or silence as human approval.

## Directed relations

Use only:

- `implements`: source realizes or formalizes target.
- `depends_on`: source requires target.
- `extends`: source builds upon target.
- `related`: symmetric conceptual association.

Represent relations in the repository's existing index or document metadata. If none exists, add a compact `relations` list to frontmatter:

```yaml
relations:
  - type: depends_on
    target: ADR-003
```

Rules:

1. Source and target must exist before recording the relation.
2. `implements`, `depends_on`, and `extends` are directed.
3. `related` is semantically symmetric; store it once unless the project index requires both directions.
4. Reject duplicate, self-referential, unknown-target, and unknown-type relations.
5. A relation never changes lifecycle status automatically.

## Code Change Pattern

Use `cpat` only when the lesson is likely to recur or materially improves diagnosis. Required sections:

```markdown
## Symptom

## Root cause

## Change

## Scope

## Verification

## Prevention
```

Content rules:

- `Symptom`: exact user-visible, test, compiler, device, CI, production, or runtime evidence.
- `Root cause`: confirmed causal mechanism; label uncertainty when not fully proven.
- `Change`: the bounded correction, not a transcript of attempts.
- `Scope`: affected and explicitly unaffected modules, versions, environments, or data.
- `Verification`: observed commands, results, device behavior, deployment checks, or evidence. Intended future testing is insufficient.
- `Prevention`: durable test, guard, diagnostic, runbook, contract, or process change.

For hardware, production, financial, or protected systems, source reasoning alone cannot satisfy `Verification`.

When `bug-evidence-protocol` was used, reference its stable evidence ID in `Verification`. Summarize the observed result in the `cpat`; keep bulky or protected command output in its authoritative evidence store.

## Workflow

1. Search existing durable docs for the decision, rule, spec, plan, research, or incident.
2. Update the existing canonical document when it owns the subject; do not create a duplicate.
3. Select one minimal type and identify authoritative sources.
4. Draft with `status: draft` and validate required fields/sections.
5. Propose relations only after both endpoints exist.
6. Show the proposed diff or document for inspection.
7. Apply only within the user's authorized scope.
8. Keep `draft` unless explicit human approval satisfies the acceptance gate.
9. Run the smallest useful link, schema, docs, or repo-native check.

## Review output

Use:

```text
verdict: CONTRACT_OK | CONTRACT_AMBIGUOUS | CONTRACT_UNSAFE
document: <path or proposed path>
type: adr | rfc | rule | spec | plan | rnd | cpat
status: draft | accepted | rejected
approval: confirmed | missing | not-required-for-current-status
relations: valid N, invalid N
required sections: complete | missing <names>
verification: <checks and result>
```

`CONTRACT_OK` requires a valid type, lifecycle state, approval record when accepted, valid relation endpoints/directions, complete required sections, and no conflict with an existing source of truth.

## Attribution

Adapted from the minimal reusable patterns in `archcore-ai/cli`: typed Git-native documents, lifecycle states, directed relations, and code-change patterns. Rewritten for ABVX proposal-first workflows without adopting Archcore's CLI, MCP server, hooks, session injection, full document taxonomy, or sync runtime.
