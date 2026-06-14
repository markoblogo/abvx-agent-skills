# Outreach Targets

This file tracks external listing and distribution targets for `abvx-agent-skills`.

Star counts below were checked on 2026-06-15 and will drift.

## Wave 1: Highest Priority

| Target | Stars | Fit | Angle | Status | Blocker |
|---|---:|---|---|---|---|
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 46,449 | Excellent | coding-agent starter pack | queued | need PR against list taxonomy |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 25,321 | Excellent | cross-agent, reviewable pack | queued | need category placement |
| [antfu/skills](https://github.com/antfu/skills) | 5,292 | Strong | curated skills collection | queued | need fit with maintainer taste |
| [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | 4,419 | Good | curated public skills | queued | likely needs compact pack description |
| [0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) | 3,956 | Strong | skills + tools + integrations | queued | need best Hermes-facing angle |
| [SamurAIGPT/awesome-hermes-agent](https://github.com/SamurAIGPT/awesome-hermes-agent) | 1,731 | Strong | established Hermes resource list | queued | need non-duplicate wording vs 0xNyk |
| [Prat011/awesome-llm-skills](https://github.com/Prat011/awesome-llm-skills) | 1,323 | Excellent | Codex / Claude / Gemini overlap | queued | add under `Development & Code Tools` |

## Wave 2: Good Fit, Lower Reach

| Target | Stars | Fit | Angle | Status | Blocker |
|---|---:|---|---|---|---|
| [kodustech/awesome-agent-skills](https://github.com/kodustech/awesome-agent-skills) | 83 | Excellent | exact agent-skills match | queued | verify section naming before PR |
| [Code-and-Sorts/awesome-copilot-agents](https://github.com/Code-and-Sorts/awesome-copilot-agents) | 536 | Good | verification + coding workflows | queued | verify listing style |
| [CommandCodeAI/agent-skills](https://github.com/CommandCodeAI/agent-skills) | 73 | Good | workflow customization | queued | may want install-surface angle |
| [gmh5225/awesome-skills](https://github.com/gmh5225/awesome-skills) | 38 | Good | broad multi-agent skills list | queued | verify maintenance level |
| [finfin/awesome-frontend-skills](https://github.com/finfin/awesome-frontend-skills) | 121 | Selective | frontend subset only | queued | pitch only `browser-verification` / `design-critique-polish` / `frontend-product-builder` |

## Wave 3: Specialized Targets

| Target | Stars | Fit | Angle | Status | Blocker |
|---|---:|---|---|---|---|
| `LLMQuant/awesome-trading-agents` | unverified | Selective | founder/trading crossover, agent discipline | research | verify public repo and submission path |
| `LLMSecurity/awesome-agent-skills-security` | unverified | Selective | safety / auditability / delivery gates | research | verify repo and whether static-audit positioning fits |
| `EvoMap/awesome-agent-evolution` | unverified | Selective | loopops / skill evolution / bounded loops | research | verify public repo and taxonomy |

## Recommended Order

1. `hesreallyhim/awesome-claude-code`
2. `VoltAgent/awesome-agent-skills`
3. `Prat011/awesome-llm-skills`
4. `antfu/skills`
5. `kodustech/awesome-agent-skills`
6. both Hermes lists

## Notes From Verification

- `hesreallyhim/awesome-claude-code` is currently in a README reorganization state. Resource intake is still active, but it is issue-first right now, not PR-first.
- `hesreallyhim/awesome-claude-code` explicitly forbids resource submissions through `gh` CLI in its issue template, so the submission should be posted manually through the GitHub web UI.
- `VoltAgent/awesome-agent-skills` has a live `Community Skills` area with a `Development and Testing` subsection that fits the ABVX pack well.
- `Prat011/awesome-llm-skills` currently has the cleanest near-term insertion point under `Development & Code Tools`.

## Suggested Initial Pitch By Target Type

- `awesome-claude-code` / `awesome-llm-skills`:
  lead with `minimal-diff-builder`, `diagnose`, `token-efficient-execution`, `browser-verification`
- broad agent-skill catalogs:
  lead with "small, auditable skillpack" and generated catalog
- security-leaning lists:
  lead with validation, static audit workflow, and verification-first execution
- frontend lists:
  lead only with the frontend subset, not the full pack
