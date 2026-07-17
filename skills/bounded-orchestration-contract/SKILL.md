---
name: bounded-orchestration-contract
description: Coordinate an opt-in Planner, Reviewer, and bounded Executor workflow with stable findings, at most five review rounds, disjoint write ownership, explicit route evidence, and root-owned verification. Use when the user asks for plan review, multi-agent orchestration, routed executors, parallel implementation, or the SET bounded-orchestration capability.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Bounded Orchestration Contract

Use this skill only when separate planning, review, or independent execution slices materially improve a non-trivial task. Small or tightly coupled work stays with the root.

This is an opt-in coordination discipline, not a scheduler, model router, provider bridge, permission grant, or persistent configuration layer.

## Authority

The root owns intent, canonical plan state, delegation decisions, integration, safety, verification, and the final answer. Planner and Reviewer are read-only. Executors receive only their bounded slice. Explicit `no subagents` or equivalent instructions disable delegation.

## Plan protocol

Version every canonical plan. Use exactly these first-line states:

- `PLAN_DRAFT`: first complete candidate plan.
- `PLAN_REVISE`: the current version has material findings.
- `PLAN_APPROVED`: the exact reviewed version may release executor work.

The Reviewer returns `PLAN_APPROVED` or `PLAN_REVISE`. Stop immediately on approval. Never exceed five total review rounds. If round five still returns `PLAN_REVISE`, halt before executor release and report unresolved findings.

## Findings ledger

Assign stable IDs in discovery order: `F-001`, `F-002`, and so on. Never renumber or silently drop a finding.

Each entry contains:

```text
ID: F-001
Status: OPEN | INCORPORATED | REJECTED
Summary:
Reason:
Plan version introduced:
Plan version disposed:
```

Every latest finding must be `INCORPORATED` or `REJECTED` with a concrete reason before approval. `OPEN`, missing, duplicated, stale-version, or empty-reason entries block `PLAN_APPROVED`. Rejection means the root or Planner has supplied an evidence-based reason; it does not mean the finding disappeared.

## Review loop

1. Root prepares the task constraints, acceptance criteria, repo facts, risks, proposed slices, and verification.
2. Planner or root emits `PLAN_DRAFT` version 1.
3. Reviewer checks only the canonical current version and returns a state plus findings.
4. Planner or root revises the complete plan and updates every finding disposition.
5. Root validates version and ledger integrity before another review.
6. Repeat only while material findings remain, up to five reviews.

Planner and Reviewer report to root only. They do not edit, execute, spawn, contact each other, or release work.

## Bounded executor packet

Release executor work only from an approved plan, unless the user explicitly chose a reviewer-free workflow. Each packet must be self-contained:

```text
Packet ID:
Objective:
Boundaries:
Context / repo facts:
Owned files or read-only scope:
Dependencies:
Stop conditions:
Acceptance criteria:
Smallest useful verification:
Required handoff:
```

Require executors to preserve unrelated changes, avoid descendants, avoid Reviewer contact, stay within ownership, and report blockers rather than guess.

Parallelize only genuinely independent packets. Write ownership must not overlap by file, generated artifact, migration, shared registry, lockfile, or other coupled surface. Unclear or overlapping ownership blocks parallel release; run sequentially or keep integration with root.

## Route states

Report only:

- `route accepted`: the host accepted and validated requested route controls. Runtime identity is not proven.
- `used and confirmed`: host metadata exposes the effective runtime model, provider, or route.
- `unavailable`: the requested route cannot run or cannot satisfy required controls.

Saved files, prompt preferences, tool acceptance, and child prose claiming a model name do not prove runtime identity. Never upgrade `route accepted` to `used and confirmed` without host evidence. Required unavailable Planner or Reviewer routes halt before executor work unless the user explicitly allowed best-effort degradation for this task.

## Executor handoff

Require a compact result:

```text
Packet ID:
Status: COMPLETE | BLOCKED | PARTIAL
Work completed:
Files or evidence:
Checks run:
Remaining risks:
```

Executor `COMPLETE` means the packet returned evidence. It is not final acceptance.

## Root verification gate

Before reporting completion, root must:

1. inspect every handoff and reject stale, unsupported, conflicting, or out-of-scope output;
2. integrate the accepted outputs;
3. inspect the combined diff or final artifact;
4. run the smallest sufficient tests, lint, build, source check, or manual verification;
5. record integrated outputs, checks run, result, and remaining risks.

If the root cannot verify a material claim, label it unverified. Child completion, a green isolated test, or `route accepted` cannot substitute for integrated verification.

## Output

Keep the user-facing report compact:

```text
Plan: PLAN_APPROVED vN | NOT_APPROVED vN
Review rounds: N/5
Findings: incorporated N, rejected N, open N
Routes: <role> — route accepted | used and confirmed | unavailable
Execution: <packet statuses>
Root verification: <checks and result>
Remaining risks: <only material items>
```

## Attribution

Adapted from the role, findings-ledger, bounded handoff, route-evidence, and root-verification discipline in `Cjbuilds/Codex-Orchestration`. Rewritten as a provider-neutral, opt-in ABVX skill without adopting its plugin runtime or persistent routing configuration.
