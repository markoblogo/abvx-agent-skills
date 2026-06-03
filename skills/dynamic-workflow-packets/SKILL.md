---
name: dynamic-workflow-packets
description: Plan and run large Codex tasks with compact dynamic workflow packets, risk gates, integration, and verification. Use when the user explicitly asks for dynamic workflows, packets, subagents, swarm, orchestration, long-running audits, multi-track coding/research work, job or client search agent design, migrations, repo-wide reviews, or tasks where independent discovery, implementation, review, and verification tracks would reduce drift.
---

# Dynamic Workflow Packets

Use this skill to coordinate big work without turning small tasks into process overhead.

## Decision Rule

Use packet orchestration when at least two are true:

- The task has independent coding, research, data, UX, security, docs, review, sourcing, or verification tracks.
- A clear success contract would prevent drift.
- The task is risky, broad, expensive, external-facing, or long-running.
- Separate review would likely catch mistakes.
- The workflow pattern may be reused.
- The user explicitly asks for packets, swarm, subagents, dynamic workflow, or orchestration.

If the task is small, do it directly and mention that packet orchestration is unnecessary.

## Operating Contract

1. Restate the goal and success criteria.
2. Identify risks and approval gates before execution.
3. Split only genuinely independent work into packets.
4. Keep critical-path work local; delegate or simulate sidecar work.
5. Use subagents only if available and appropriate. Otherwise simulate packets with isolated notes.
6. Integrate results explicitly; never paste raw packet dumps as the final answer.
7. Verify against the original success criteria.
8. Save reusable artifacts only when they will help future work.

## Risk Gates

Ask one clear approval question before:

- deleting, overwriting many files, mass-renaming, force-pushing, or rewriting history,
- deploying, publishing, emailing, messaging, posting, applying to jobs, or mutating external systems,
- running migrations, broad codemods, dependency upgrades, or expensive jobs,
- touching credentials, secrets, billing, production data, user accounts, private customer data, resumes, contacts, or outreach history,
- creating public resources or changing third-party accounts,
- spawning many agents or long-running compute.

If risk is ambiguous, do a read-only inspection, draft the exact action, explain likely effect, then ask.

## Workflow Artifact

Create a local run directory only for substantial tasks:

```text
.workflow/<slug>/
|-- plan.md
|-- state.json
|-- packets/
|-- results/
`-- final-report.md
```

For smaller tasks, keep the packet plan in the chat or a temporary note.

`plan.md` should contain:

```text
Goal:
Success criteria:
Context:
Constraints:
Risks and approvals:
Packets:
Integration policy:
Verification:
Reusable artifacts:
```

## Packet Template

Each packet must be bounded and self-contained:

```text
Packet ID:
Objective:
Context:
Sources / files:
Ownership:
Do:
Do not:
Expected output:
Verification:
Risk level:
Status:
```

Good packet types:

- repo discovery,
- API or market research,
- implementation slice,
- tests and fixtures,
- UX/product review,
- security or privacy review,
- job/client sourcing,
- outreach message drafting,
- CRM/data-model design,
- final verification.

For code packets, assign non-overlapping files or modules. Tell workers or simulated packet passes not to revert unrelated changes.

## Domain Patterns

### Coding

Use packets for discovery, implementation, tests, docs, security review, and final verification. Keep edits scoped by module. The parent agent owns final patch quality and runs the checks.

### Research

Use packets for source discovery, primary-source verification, synthesis, counter-evidence, and final citation review. Track source, date, unit, and uncertainty.

### Job And Client Search

Use packets for market/source mapping, opportunity scoring, profile/resume positioning, outreach drafts, follow-up schedule, CRM schema, and risk/privacy review. External messages, applications, profile changes, and public posting require user approval.

### Long-Running Audits

Use packets for inventory, risk triage, deep dives, fix candidates, verification plan, and final report. Prefer one highest-confidence fix over broad speculative churn.

## Integration

After packets complete, synthesize:

```text
Accepted:
Rejected:
Conflicts:
Decisions:
Final changes:
Verification evidence:
Remaining risks:
Reusable follow-up:
```

If packets disagree, inspect the authoritative source before choosing. Reject outputs that are stale, unsupported, duplicate, unsafe, or outside scope.

## Verification

Run the narrowest reliable checks first, then broaden as risk warrants:

- unit, integration, or e2e tests,
- lint, typecheck, build,
- script dry run,
- browser/UI smoke test,
- source citation check,
- migration dry run,
- outreach/privacy review,
- manual checklist for non-code work.

Do not call the workflow complete until evidence satisfies the original success criteria. Report skipped checks honestly.

## Reusable Recipes

When a run produces a reusable pattern, save a concise recipe only if useful:

```text
Trigger:
Plan shape:
Packet list:
Approval gates:
Verification checklist:
Known risks:
```

Do not save transcripts, secrets, bulky logs, credentials, private contacts, resumes, or sensitive personal details.
