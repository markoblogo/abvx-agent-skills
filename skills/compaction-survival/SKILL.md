---
name: compaction-survival
description: Preserve working state across long sessions and context compaction by checkpointing decisions, edited files, blockers, open hypotheses, and unresolved errors into compact resumable artifacts. Use on long coding tasks, audits, research, or any session at risk of losing state after compaction.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Compaction Survival

Save tokens by keeping the right state alive across compaction instead of re-deriving it after memory loss.

## Goal

When a session is getting long, preserve only the working state that would be expensive to reconstruct.

## What To Preserve

- current objective;
- active subtask list;
- key decisions and reversals;
- files changed or inspected deeply;
- unresolved errors and their current hypothesis;
- blockers, constraints, and pending verifications;
- exact artifact paths for large outputs or generated files.

## What Not To Preserve

- long narrative history;
- repeated summaries of already-resolved steps;
- raw logs that can be regenerated cheaply;
- generic project documentation already available on disk.

## Checkpoint Workflow

1. Detect compaction risk:
   - long session;
   - many files touched;
   - many turns of debugging or research;
   - user explicitly worried about token budget.
2. Emit a compact handoff artifact:
   - objective;
   - done / next / blocked;
   - decisive evidence only;
   - exact paths for deeper artifacts.
3. Keep the checkpoint stable unless the working state materially changes.
4. After compaction or resume, recover from the checkpoint first instead of replaying the whole session.

## Recommended Shapes

- concise handoff note;
- checked-location ledger;
- issue-specific status file in `docs/ai/tasks/` or equivalent;
- compact bullets over narrative prose.

## Guardrails

- Do not checkpoint secrets.
- Do not create noisy per-turn diary files.
- Do not preserve stale hypotheses after the evidence changed.
- Do not replace real verification with checkpoint confidence.

## Final Report

Say what was checkpointed, where it lives, and what should be reused first after resuming.
