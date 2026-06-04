---
name: spec-to-prd
description: Turn the current conversation, repo understanding, and clarified decisions into a PRD. Use when a vague feature, client request, internal roadmap item, or discovery thread needs to become a durable product artifact. Prefer repo/domain language, explicit scope, implementation decisions, testing decisions, and issue-tracker-neutral output.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Spec To PRD

Convert current understanding into a durable PRD without re-running the whole discovery session.

## Workflow

1. Synthesize what is already known from the conversation and repo.
2. Use the project's domain language and existing architectural decisions.
3. Identify the highest useful seams for implementation and testing.
4. Confirm only the few assumptions that would distort the PRD if wrong.
5. Produce one PRD artifact:
   - issue tracker body;
   - markdown file;
   - handoff-ready document.

## PRD Shape

Include:

- problem statement;
- solution from the user's perspective;
- extensive user stories;
- implementation decisions;
- testing decisions;
- out of scope;
- further notes and open assumptions.

## Rules

- Do not dump file paths unless they are durable anchors.
- Do not include code unless a small shape encodes a real decision more precisely than prose.
- Keep scope sharp; explicitly name what is out of scope.
- If discovery is too weak, route back to `rapid-grilling` or `doc-grounded-grilling` first.

## Final Report

State where the PRD lives, what assumptions remain, and the best next step: issue breakdown, prototype, or execution.
