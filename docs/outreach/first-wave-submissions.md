# First-Wave Submission Drafts

These are ready-to-use submission drafts for the first outreach wave.

## 1. hesreallyhim/awesome-claude-code

Current route: manual GitHub UI issue, not CLI, because the repo's issue template explicitly forbids programmatic resource submissions and the README is in reorganization.

Recommended issue type: `Recommend New Resource`

### Issue Fields

- `Display Name`: `ABVX Agent Skills`
- `Category`: `Agent Skills`
- `Sub-Category`: `General`
- `Primary Link`: `https://github.com/markoblogo/abvx-agent-skills`
- `Author Name`: `markoblogo`
- `Author Link`: `https://github.com/markoblogo`
- `License`: `MIT`

### Description

Small, auditable agent skills for coding work: smaller diffs, evidence-led debugging, token control, and real verification. The pack focuses on reviewable `SKILL.md` workflows rather than broad prompt bundles, with validation, static security audit, and a generated catalog.

### Validate Claims

Preview or install one skill and compare its behavior on one narrow coding task instead of treating the pack as a generic prompt collection. The fastest proof points are smaller diffs, less speculative debugging, less shell noise, and explicit browser verification before "done."

### Specific Task(s)

1. Ask the agent to fix a small bug with the smallest possible patch.
2. Ask the agent to debug one reproducible failing test without guessing.
3. Ask the agent to verify a frontend change in a real browser instead of only by code inspection.

### Specific Prompt(s)

1. `Use minimal-diff-builder. Implement the smallest correct fix for this issue and avoid broad refactors.`
2. `Use diagnose. Reproduce the failing test, rank hypotheses from evidence, and verify the fix before changing anything else.`
3. `Use browser-verification. Check the changed page in a real browser and report any layout, state, or console issues before calling the work done.`

### Additional Comments

- The repo is older than one week: first public commit was on `2026-06-03`.
- The strongest starter skills are `minimal-diff-builder`, `diagnose`, `token-efficient-execution`, `rtk-assisted-shell`, and `browser-verification`.
- The repository includes a generated text catalog and a live searchable catalog on ABVX Lab.

## 2. VoltAgent/awesome-agent-skills

Recommended placement: `### Community Skills` -> `Development and Testing`

### Suggested List Entry

- **[markoblogo/abvx-agent-skills](https://github.com/markoblogo/abvx-agent-skills)** - Small, auditable coding-agent skillpack for smaller diffs, evidence-led debugging, token control, browser verification, and reviewable `SKILL.md` workflows with validation and static security audit

### Suggested PR Summary

Add ABVX Agent Skills to the community `Development and Testing` section. The pack is focused on practical coding-agent work rather than broad prompt collections, and its strongest entry points are `minimal-diff-builder`, `diagnose`, `token-efficient-execution`, `rtk-assisted-shell`, and `browser-verification`.

## 3. Prat011/awesome-llm-skills

Recommended placement: `### Development & Code Tools`

### Suggested List Entry

- [ABVX Agent Skills](https://github.com/markoblogo/abvx-agent-skills) - Small, auditable skillpack for Codex-style coding workflows: smaller diffs, evidence-led debugging, shell-output compaction, token-efficient execution, and browser verification. *By [@markoblogo](https://github.com/markoblogo)*

### Suggested PR Summary

Add ABVX Agent Skills under `Development & Code Tools`. It is a strong fit for the repo's multi-agent / multi-CLI audience because it emphasizes practical coding workflows, compact reviewable skill files, and verification-first execution rather than general-purpose prompt bundles.
