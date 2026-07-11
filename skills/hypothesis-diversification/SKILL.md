---
name: hypothesis-diversification
description: Generate diverse hypotheses, explanations, or solution candidates before evidence review. Use for research, incident analysis, market or product reasoning, adversarial review, and SkillOpt proposal generation when first-answer mode collapse would hide alternatives.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Hypothesis Diversification

Use this skill to make the agent produce multiple plausible alternatives before it argues for one.

## Use When

- a research answer, diagnosis, plan, or market explanation may collapse onto the first plausible story;
- you need adversarial review before accepting a confident recommendation;
- a SkillOpt run should generate several bounded edit proposals before validation;
- a SET bundle or agent handoff needs review lenses that ask for alternatives, not runtime autonomy.

## Workflow

1. State the decision or question in one sentence.
2. Generate 3-8 distinct hypotheses or candidate proposals.
3. For each candidate, record:
   - claim: what would be true if this candidate is right;
   - evidence needed: what would support it;
   - disconfirming signal: what would weaken or falsify it;
   - cost of being wrong: low, medium, or high.
4. Run an adversarial pass:
   - merge duplicates;
   - remove candidates that are only wording variants;
   - add at least one non-obvious or contrarian alternative when the domain allows it.
5. Rank candidates by evidence readiness, not by model confidence.
6. Hand off to the relevant validation gate, evidence ledger, reviewer, or domain process.

## SkillOpt Mode

When used with `skillopt-evolve-skills`, generate multiple bounded edit proposals before the validation gate:

- each proposal must fit the edit budget;
- each proposal must name the target artifact and operation: `append`, `replace`, `delete`, or `move`;
- do not combine several unrelated improvements into one proposal;
- reject plausible proposals that are overfit, duplicate existing rules, or weaken a guardrail.

## Output Shape

Use:

- question or decision;
- candidate set;
- evidence needed;
- disconfirming signals;
- adversarial notes;
- validation handoff;
- rejected candidates, if any.

## Guardrails

- Do not treat verbalized or model-estimated probabilities as calibrated probabilities.
- Do not use this as a standalone financial, legal, medical, or safety decision method.
- Do not use candidate diversity as completion evidence; every accepted candidate still needs validation.
- Do not add runtime autonomy, trading execution, or position-sizing logic from this pattern.
- Keep the candidate set small enough to review.

## Provenance

Inspired by "Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity" (arXiv:2510.01171), adapted as an ABVX research and adversarial-review pattern rather than a decision engine.
