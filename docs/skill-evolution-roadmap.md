# Bounded Skill Evolution

ABVX treats a reusable skill as a versioned procedural artifact that may improve from real task evidence. The initial direction is inspired by [SkillOpt](https://arxiv.org/abs/2605.23904), but this repository does not run a general self-improving agent runtime.

## Pilot scope

Start with one or two repeated workflows:

- `minimal-diff-builder`
- `reversible-agent-task`

The pilot should produce small, inspectable skill edits and evidence for whether they improve the target workflow. It must not rewrite the whole skill or silently mutate the published pack.

## Update loop

```text
baseline -> rollout evidence -> bounded proposal -> held-out validation
         -> accept/version or reject/record
```

The researcher-loop structure for future automation is:

```text
source -> mechanism -> proposal -> novelty_check -> validation -> pr_ready
```

This is a state machine for evidence and review, not permission to self-edit. Sources identify external papers, repos, traces, or failures. Mechanisms describe reusable behavior changes. Proposals are bounded edits. Novelty checks reject duplicates or weaker versions of existing rules. Validation uses fixtures, activation cases, deterministic checks, or bounded evaluation. `pr_ready` means the artifact is ready for human review, not automatically merged.

Each proposal is an `add`, `delete`, `replace`, or `move` operation with:

- target skill and current version;
- evidence references;
- expected behavior change;
- edit budget;
- validation command or evaluator;
- result, score delta, and decision.

Before validation, generate a small set of alternative bounded proposals rather than accepting the first plausible edit. Use `hypothesis-diversification` when candidate generation needs an explicit diversity-first pass. The point is not to vote on model confidence; it is to expose different edit shapes before the validation gate chooses what is worth testing.

The first implementation may be manual or script-assisted. A proposal remains separate until validation passes and a maintainer explicitly accepts it.

Use `bounded-evaluation` for pairwise checks, position-bias mitigation, activation fixtures, and LLM-as-judge guardrails. Use `context-degradation-review` when a proposed skill change might add prompt bloat, stale context, or conflicting instructions.

## Current contract

The pilot manifest lives at [`benchmarks/skill-evolution/manifest.json`](../benchmarks/skill-evolution/manifest.json). It names the candidate skills, the evidence and validation requirements, and the limits for the first experiments.

Rejected proposals belong in the rejected-edit buffer. Record why a plausible edit was rejected so later iterations do not repeat overfit, duplicate, or guardrail-weakening changes.

The first researcher artifacts should stay small:

- source registry: curated sources and why they matter;
- mechanism ledger: accepted behavior changes with provenance;
- rejected mechanism ledger: duplicates, overfit ideas, and weak evidence;
- activation cases: prompts that check whether the right skill loads;
- skill health gate: structural checks for trigger fit, actionability, generalization, non-regression, and cost.

## Gates

An evolution proposal is eligible for acceptance only when:

1. the behavior is procedural and reusable rather than tied to one incident;
2. the change is within the edit budget and keeps the skill readable;
3. at least one prior scenario and one new scenario are checked when feasible;
4. held-out or independently selected validation does not regress;
5. safety, accessibility, validation, data-loss, and reversibility rules remain intact;
6. the accepted version and evidence are reviewable in git.

If reliable scoring is unavailable, keep the proposal as a note or rejected candidate. Do not infer improvement from a persuasive explanation or one successful run.

## Non-goals for the pilot

- no always-on self-editing agent;
- no automatic publishing of skill changes;
- no autonomous `pr_ready` to merge path;
- no large skill library optimizer;
- no model-weight training;
- no verbalized-probability scoring as proof of improvement;
- no benchmark claims until fixtures, arms, model, host, run count, and captured artifacts are committed.

## Revisit trigger

Increase automation only after the pilot has repeated tasks, stable evaluators, captured rollout artifacts, and several accepted/rejected proposals that demonstrate the loop is worth its cost.
