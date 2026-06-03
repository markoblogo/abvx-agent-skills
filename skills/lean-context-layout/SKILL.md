---
name: lean-context-layout
description: Restructure agent-facing docs so the always-loaded context stays small and the rest is loaded on demand. Use when a repo has bloated AGENTS.md or CLAUDE-style docs, too many always-loaded notes, stale session history, oversized runbooks, or high startup token waste for coding agents.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Lean Context Layout

Save tokens by changing what loads at startup. Keep the default context small, stable, and operational.

## Goal

Separate:

- always-loaded essentials;
- on-demand reference material;
- archival history that should not auto-load.

## Default Layout

Prefer a compact startup surface:

- top-level agent entry file with rules and pointers;
- quick-start commands;
- architecture map or repo map entrypoint;
- common mistakes or sharp edges;
- optional issue-specific or domain-specific notes loaded only when needed.

Everything else should move behind explicit paths in `docs/`, `.claude/`, `docs/ai/`, or equivalent repo-local structures.

## Workflow

1. Measure the current startup burden:
   - which files are always loaded;
   - which of them are large, stale, duplicated, or historical;
   - which content is needed every session versus occasionally.
2. Identify the four startup essentials:
   - how to work here;
   - how to run or test;
   - where the code lives;
   - what recurring mistakes to avoid.
3. Move long histories, completed tasks, old sessions, generated artifacts, and bulky narrative docs out of the always-loaded path.
4. Replace bulky text with short index pointers:
   - “for X, read Y”;
   - “for domain map, open Z”;
   - “for completed work, see archive path”.
5. Keep startup files stable. Frequent churn reduces cache utility and raises reread cost.
6. Re-measure after restructuring and report the delta.

## Codex And agentsgen Guidance

- Keep `AGENTS.md` small and procedural.
- Push deeper material into `docs/ai/` or other explicit reference paths.
- Prefer compact summaries over completed-session logs in startup files.
- Preserve enough orientation that a fresh agent can still start productively.

## Guardrails

- Do not delete durable project knowledge; relocate and index it.
- Do not hide critical safety or production constraints in optional docs.
- Do not create six tiny files when one clear compact file would do.
- Do not optimize only for token count if navigability becomes worse.

## Final Report

Include old layout, new layout, what moved, what stayed always-loaded, and the expected token savings.
