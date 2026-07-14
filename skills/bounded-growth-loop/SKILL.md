---
name: bounded-growth-loop
description: Design a small recurring product, content, SEO, analytics, or go-to-market review loop with evidence checks, durable state, explicit stop rules, and approval-gated outputs. Use before scheduling recurring growth work or turning a repeated marketing task into an agent loop.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Bounded Growth Loop

Turn a proven recurring review into a safe, useful loop. The default output is a report or draft, never an unreviewed external action.

## Use When

- a content freshness, SEO, funnel, partner, activation, or market-positioning review repeats on a cadence;
- a team wants a weekly or monthly operating rhythm without a full marketing runtime;
- a recurring agent task needs state, deduplication, evidence checks, and a clear human gate.

## Loop Contract

Specify all of these before scheduling:

- cadence and trigger;
- action condition, distinct from the check itself;
- one intended outcome and bounded scope;
- source and product context inputs;
- self-check and evidence threshold;
- durable state, dedupe key, cooldown, and run log;
- proposal output location;
- stop, error, and escalation rules;
- approval boundary and rollback/discard path.

## Workflow

1. Read `docs/product-context.md` or the repo's equivalent.
2. Select one narrow loop; begin report-only or proposal-first.
3. Match cadence to signal speed and sample size; do not create daily noise for slow signals.
4. Define the condition that authorizes a recommendation or draft.
5. Retain the report, evidence, and state outside ephemeral chat.
6. Run a verifier before proposing action; distinguish tracking defects, seasonality, and real changes.
7. Send external copy, publishing, scheduling, spend, pricing, outreach, or product mutations through explicit approval.
8. Review whether the loop is still useful; pause it when it creates noise or no one acts on its output.

## Default Levels

- `L1 report-only`: reads and summarizes with no external mutation.
- `L2 proposal-first`: creates reviewable drafts or PRs behind a human gate.
- `L3 governed`: only after durable state, verifier evidence, budget limits, run log, rollback, and controlled settlement exist.

## Guardrails

- Do not auto-publish, auto-send, shift ad spend, alter pricing, or contact people.
- Do not act on sparse, stale, personally identifiable, or unverified data.
- Do not treat a dashboard movement as causation; record alternative explanations.
- Keep the loop product-specific and delete it when it no longer earns its operating cost.

## Pair With

- `product-context` for approved product language and boundaries;
- `loop-readiness-review` for readiness classification;
- `bounded-evaluation` for the verifier;
- `reversible-agent-task` and `social-publishing-gate` for proposal and publication settlement.

## Provenance

Adapted from `coreyhaines31/marketingskills` recurring-loop structure, aligned with ABVX proposal-first execution and loop-readiness gates rather than a marketing automation runtime.
