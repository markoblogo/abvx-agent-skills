---
name: confidence-fragility-review
description: Review whether an artifact's confident claims are backed by evidence, tests, contracts, or operational safeguards. Use before shipping, publishing docs, accepting generated plans, or trusting a workflow that may present fragile assumptions as certainty.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Confidence Fragility Review

Stress-test the gap between how confident an artifact sounds and how much evidence actually supports it.

## Use When

- a plan, release note, README, landing page, or SET bundle sounds ready but proof is thin;
- generated docs imply stronger guarantees than the repo can support;
- final review needs a fear-oriented lens before ship;
- a user asks what could go wrong if people trust the artifact at face value.

## Workflow

1. Identify confident claims:
   - readiness claims;
   - safety claims;
   - completeness claims;
   - compatibility claims;
   - performance or reliability claims.
2. For each claim, ask what backs it:
   - tests or CI;
   - schema or type contracts;
   - runtime checks;
   - docs links;
   - human approval;
   - explicit limitations.
3. Classify the concern:
   - tactical: a specific path can fail;
   - structural: a category of failure has no defense;
   - epistemic: confidence is not earned by evidence.
4. Separate justified fragility from projected worry.
5. Recommend the smallest evidence step that would make confidence warranted.

## Output Shape

Use:

- verdict: `CONFIDENCE_WARRANTED` or `FRAGILITY_MASKED`;
- confidence claims reviewed;
- evidence found;
- fragility register: tactical, structural, or epistemic;
- smallest proof step.

## Guardrails

- Do not turn this into a generic risk audit.
- Do not demand proof for every harmless claim.
- Do not perform security analysis unless the artifact makes security claims.
- Be explicit when a fear is plausible but not evidenced.

## Provenance

Adapted from the `anxiety-reader` pattern in `aself101/agents-and-pipelines`, reframed as a compact confidence-vs-evidence review skill.
