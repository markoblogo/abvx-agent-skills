---
name: bounded-evaluation
description: Design small evaluation gates for agent outputs, skill changes, prompts, and tool contracts. Use when a change needs rubric checks, pairwise comparison, position-bias mitigation, regression fixtures, or LLM-as-judge discipline without building a heavy eval platform.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Bounded Evaluation

Use this skill when a change needs a small, explicit evaluation gate.

## Use When

- reviewing skill changes, AGENTS.md rules, prompt playbooks, or SET bundle changes;
- comparing two agent outputs or proposals;
- using an LLM judge where bias or weak rubrics could mislead;
- creating activation tests, regression cases, or ship gates for agent behavior;
- deciding whether a repeated workflow improved after a bounded edit.

## Evaluation Contract

A bounded eval must state:

- target artifact or behavior;
- candidate outputs or versions;
- rubric dimensions and weights, if any;
- pass/fail threshold;
- fixtures or scenarios;
- judge type: deterministic check, human review, LLM judge, or hybrid;
- known bias risks and mitigation.

## Pairwise And Judge Rules

- Compare A/B outputs against the same rubric.
- Swap candidate order when using an LLM judge to detect position bias.
- Require reasons before scores, but treat reasons as evidence to inspect, not truth.
- Mark the eval invalid when swapped order changes the winner without a defensible reason.
- Prefer deterministic checks for syntax, schema, file existence, and command success.
- Keep human approval for high-stakes or ambiguous decisions.

## Workflow

1. Define the smallest behavior being evaluated.
2. Pick 1-5 representative fixtures or scenarios.
3. Choose deterministic checks before LLM judging.
4. If using pairwise judging, run both candidate orders.
5. Record results, invalidations, and decision.
6. Feed accepted/rejected outcomes back into the relevant ledger.

## Output Shape

Use:

- eval target;
- fixtures;
- rubric;
- judge type;
- results;
- bias checks;
- decision: `accept`, `reject`, `revise`, or `invalid`;
- follow-up artifact or ledger update.

## Guardrails

- Do not publish benchmark claims without committed fixtures, arms, model, host, run count, and captured artifacts.
- Do not let an LLM judge approve its own rubric changes.
- Do not use pairwise preference as proof of correctness.
- Do not hide invalid or inconsistent judge results.

## Provenance

Adapted from advanced-evaluation patterns in `muratcankoylan/Agent-Skills-for-Context-Engineering`, aligned with ABVX SkillOpt validation gates.
