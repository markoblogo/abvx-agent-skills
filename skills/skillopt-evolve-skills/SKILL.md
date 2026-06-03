---
name: skillopt-evolve-skills
description: Evolve Codex skills and agent instructions with a SkillOpt-style loop. Use when creating, refining, or auditing local skills, AGENTS.md rules, prompt playbooks, or reusable agent workflows after repeated task experience, especially when the user asks to "improve your skills", "capture this lesson", "make this reusable", or "update agent instructions".
---

# SkillOpt Evolve Skills

Use this skill to improve reusable agent behavior as a versioned artifact, not as a one-off prompt rewrite.

## Loop

1. Identify the target artifact: `SKILL.md`, `AGENTS.md`, checklist, prompt, or workflow note.
2. Define the behavior to improve in one sentence.
3. Gather evidence from real traces: user requests, command logs, diffs, failures, review comments, screenshots, or final outputs.
4. Propose bounded edits only:
   - `append`: add a missing rule to the right section.
   - `replace`: tighten a vague rule.
   - `delete`: remove a harmful or redundant rule.
   - `move`: relocate a rule to where it will trigger.
5. Accept edits only when they are procedural, reusable, and testable.
6. Validate against at least one old scenario and one new scenario when feasible.
7. Record rejected ideas if they looked plausible but would overfit, duplicate existing rules, or weaken a guardrail.

## Edit Budget

Keep skill updates small:

- Prefer 1-4 accepted edits per update.
- Keep each rule action-oriented and no longer than needed.
- Do not add examples unless they prevent a likely mistake.
- Do not duplicate rules already enforced by system, developer, AGENTS.md, or a more specific skill.
- Preserve the existing voice and structure of the artifact.

## Validation Gate

Before finalizing a skill change, check:

- **Trigger fit**: The frontmatter description names the real situations where the skill should load.
- **Actionability**: The body tells Codex what to do differently, not what to admire or remember abstractly.
- **Generalization**: The rule applies to a class of tasks, not a single observed example.
- **Non-regression**: The new rule does not conflict with higher-priority instructions or common workflows.
- **Cost**: The extra tokens are justified by avoided errors or repeated work.

If validation is weak, leave the candidate as a note instead of merging it into the skill.

## Rejected Edit Buffer

When a candidate is rejected, capture the reason briefly:

```text
Rejected: <candidate rule>
Reason: <overfit/conflict/too broad/not validated/duplicate>
Evidence: <trace, task, or check>
```

Use rejected edits to avoid repeating bad prompt changes.

## Final Report

When updating a skill, report:

- changed artifact paths,
- accepted edits in plain language,
- validation performed,
- rejected edits or assumptions if relevant.
