---
name: rapid-grilling
description: Lightweight grilling session for brainstorming, product clarification, and early design shaping. Use when the user wants fast alignment but there is not yet enough repo context to ground a heavier doc-based review. Ask one question at a time, propose a recommended answer, and keep momentum high.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Rapid Grilling

Use a fast questioning loop to turn a vague idea into something crisp enough to plan.

## Workflow

1. Ask one question at a time.
2. For each question, offer a recommended answer or likely framing.
3. Follow the decision tree branch-by-branch.
4. Prefer product, user, workflow, and boundary questions before implementation detail.
5. Stop when the next artifact is obvious:
   - PRD;
   - issue breakdown;
   - prototype;
   - implementation plan.

## Best Questions

- Who is this for?
- What exact problem changes for them?
- What is in scope vs out of scope?
- What is the happy path?
- What breaks, conflicts, or needs approval?
- What would make this demonstrably done?

## Guardrails

- Keep the session moving; do not over-formalize early brainstorming.
- If repo docs become relevant, switch to `doc-grounded-grilling`.
- If the idea becomes concrete enough, hand off to `spec-to-prd` or `plan-to-issues`.

## Final Report

Summarize the clarified idea, the key decisions, and the best next artifact to create.
