---
name: doc-grounded-grilling
description: Stress-test a plan, feature, or design against the repo's existing docs, domain language, ADRs, and context files. Use when a task is ambiguous, terminology is fuzzy, architecture trade-offs matter, or the user wants alignment before implementation. Ask one question at a time, inspect the codebase when answers are already present, and sharpen the project's language as decisions crystallize.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Doc Grounded Grilling

Use structured questioning to align a plan with the repo's actual language, constraints, and existing decisions.

## Workflow

1. Read the nearest relevant context first:
   - `AGENTS.md`
   - `docs/ai/*`
   - ADRs
   - repo docs
   - `designmd-brand-kit` artifacts when frontend or brand work is involved
2. Ask one question at a time.
3. If the answer is already in the code or docs, verify there before asking.
4. For each question:
   - identify the ambiguity;
   - give a recommended answer or framing;
   - wait for user feedback before continuing.
5. Walk down the branches of the design tree until:
   - terms are precise;
   - boundaries are understood;
   - key trade-offs are named;
   - critical scenarios are covered.

## What To Challenge

- terminology that conflicts with existing domain language;
- assumptions contradicted by code or ADRs;
- vague nouns like "account", "session", "client", "job", "draft", "campaign";
- plans that skip the test seam, integration seam, or rollout seam;
- frontend ideas that ignore the current design system or brand shape.

## Output

The session should leave behind:

- sharper language;
- clarified decisions;
- explicit open questions;
- identified docs that should be updated through `durable-context-maintenance` when the decision settles.

## Guardrails

- Do not interrogate for its own sake; stop when the plan is clear enough to execute.
- Do not invent domain language when the repo already has one.
- Do not batch ten questions at once.

## Final Report

Summarize resolved terms, decisive trade-offs, remaining open questions, and which docs should be refreshed next.
