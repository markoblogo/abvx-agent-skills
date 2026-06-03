# ABVX Skillpack Profile

ABVX skillpacks are small, reviewable agent skills for project work.

## Required Files

Each public skill should include:

```text
skills/<skill-name>/
  SKILL.md
  SKILL_CARD.md
  agents/openai.yaml
```

Optional resources:

```text
scripts/
references/
assets/
```

## Frontmatter

Use conservative frontmatter for Codex compatibility:

```yaml
---
name: skill-name
description: What this skill does and when to use it.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---
```

Keep the description trigger-rich and under 1024 characters.

## Skill Card

`SKILL_CARD.md` documents:

- description,
- owner,
- license,
- intended use,
- out of scope,
- sources and attribution,
- inputs and outputs,
- risks and mitigations,
- evaluation,
- version,
- reporting issues.

## Quality Bar

- Actionable rules beat explanations.
- Avoid broad process for small tasks.
- Do not store secrets, bulky logs, personal data, private contacts, or copied book chapters.
- Add approval gates for destructive, external, expensive, or privacy-sensitive work.
- Report verification honestly.
