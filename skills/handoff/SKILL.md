---
name: handoff
description: Create compact handoff documents for another agent, session, or human to continue work. Use when a task is long-running, context is about to compact, work must pause, an audit needs resumable state, or the user asks for a handoff, continuation note, checkpoint, or next-session brief.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Handoff

Capture operational state, not a transcript. The next agent needs facts, paths, decisions, and next actions.

## When To Use

Use for:

- long-running audits;
- multi-repo publication work;
- paused implementation;
- debugging sessions with active hypotheses;
- research with source ledgers;
- job/client-search workflows;
- context compaction or thread transfer.

## Handoff Contents

Include:

- objective and current status;
- repos, branches, important paths, URLs, and local servers;
- decisions made and why;
- files changed, commits, PRs, or releases;
- commands already run and their result;
- active hypotheses, blockers, or pending checks;
- suggested skills for the next session;
- exact next steps in priority order.

## Compression Rules

- Link to artifacts instead of copying them.
- Do not duplicate full diffs, logs, PRDs, plans, or source docs.
- Preserve concrete dates and versions when relevant.
- Redact secrets, credentials, private contacts, and unnecessary personal data.
- Separate confirmed facts from assumptions.

## Output Location

If creating a file, write it outside the project unless the user asks for an in-repo artifact. Use the OS temp directory or a clear `handoff/` location approved by the repo conventions.

## Final Response

Tell the user where the handoff lives, what it covers, and what the next agent should do first.
