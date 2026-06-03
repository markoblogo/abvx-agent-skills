# ABVX Agent Skills

<p>
  <img src="assets/skillslogo.png" alt="ABVX Agent Skills logo" width="1536" height="1024">
</p>

Small, reviewable, validation-gated agent skills for Codex-style project work.

This repository publishes opinionated ABVX skillpacks: compact `SKILL.md` workflows with clear triggers, attribution, risk notes, and validation. These are not prompt dumps. They are portable, versioned agent capabilities meant to be loaded on demand through the Agent Skills progressive-disclosure model.

## Start Here

- **Need to save tokens?** Start with `rtk-assisted-shell`, `shell-output-compaction`, `token-efficient-execution`, and `lean-context-layout`. Add `compaction-survival` if your sessions run long enough to forget their own state.
- **Need to debug a repo?** Start with `diagnose`, `repo-debugging-ledger`, and `graph-guided-code-reading`.
- **Need to build frontend?** Start with `frontend-product-builder`, `designmd-brand-kit`, and `browser-verification`.
- **Need long-session continuity?** Start with `handoff`, `compaction-survival`, and `token-usage-audit`.
- **Need to onboard a new repo?** Start with `project-context-bootstrap` and follow with `durable-context-maintenance`.
- **Need a full multi-track workflow?** Start with `dynamic-workflow-packets`.

## Skills

These skills are grouped by the job they do. The token-economy layer is intentionally visible first: for many teams, the easiest win is not “a smarter prompt”, but less wasted context.

### Token Economy & Context Control

| Skill | What It Does | Status | Origin |
|---|---|---|---|
| `rtk-assisted-shell` | Routes noisy shell workflows through RTK-style filtering. On shell-heavy tasks this can cut command-output tokens dramatically, often in the same range as RTK's reported 60-90% savings on common dev commands. | experimental | ABVX adapted |
| `shell-output-compaction` | Shrinks logs, diffs, and repo search output into counts, slices, and error-first excerpts. Usually the fastest way to turn multi-screen stdout into a small, usable artifact. | experimental | ABVX adapted |
| `graph-guided-code-reading` | Replaces broad repo reading with entrypoints, symbols, dependencies, and blast radius. On large codebases this can turn “read everything” into a much smaller focus set. | experimental | ABVX adapted |
| `token-efficient-execution` | Cuts waste from repeated reads, broad rewrites, and low-value narration. Best for long coding sessions where the loop, not the final answer, is burning the budget. | experimental | ABVX adapted |
| `token-frugal-mode` | Compresses final answers without dropping the decisive technical signal. Useful when the session is tight and you want shorter replies without caveman-style degradation. | experimental | ABVX adapted |
| `lean-context-layout` | Shrinks always-loaded agent docs into a compact startup core and pushes the rest on demand. Best for bloated `AGENTS.md`, `CLAUDE.md`, and repo runbooks. | experimental | ABVX adapted |
| `compaction-survival` | Preserves the high-value working state before long sessions collapse into compaction. Saves the turns you would otherwise spend reconstructing “what were we doing?”. | experimental | ABVX adapted |
| `token-usage-audit` | Diagnoses where the budget is really going: startup bloat, shell noise, repeated reads, oversized summaries, or compaction loss. Use this before over-optimizing the wrong layer. | experimental | ABVX adapted |

### Coding, Debugging & Architecture

| Skill | What It Does | Status | Origin |
|---|---|---|---|
| `diagnose` | Runs a disciplined debugging loop around one reproducible signal, ranked hypotheses, and narrow verification. | experimental | ABVX adapted |
| `repo-debugging-ledger` | Keeps a checked-location ledger so debugging does not keep reopening the same code and repeating the same dead ends. | experimental | ABVX original |
| `complexity-optimizer` | Finds safe complexity and performance simplifications without turning the codebase into a refactor festival. | experimental | ABVX adapted |
| `architecture-deepening-review` | Reviews deeper module seams, coupling, change surfaces, and testability, not just top-level architecture slogans. | experimental | ABVX adapted |
| `agents-best-practices` | Hardens agent harnesses around permissions, context shape, safety, and evaluation discipline. | experimental | ABVX adapted |
| `skillopt-evolve-skills` | Improves agent instructions and skills from real task evidence rather than from theory alone. | experimental | ABVX adapted |

### Frontend, UX & Product Surfaces

| Skill | What It Does | Status | Origin |
|---|---|---|---|
| `frontend-product-builder` | Builds usable frontends, landing pages, pitch pages, dashboards, and prototypes with a product-first interaction model. | experimental | ABVX adapted |
| `designmd-brand-kit` | Turns a website or brand surface into an agent-usable design system: structure, identity, and reusable UI cues. | experimental | ABVX adapted |
| `browser-verification` | Verifies real browser rendering, responsive layout, and interaction behavior instead of trusting static code inspection. | experimental | ABVX adapted |
| `web-quality-audit` | Audits accessibility, performance, UX, privacy, and browser security as one practical web quality pass. | experimental | ABVX adapted |
| `prototype-lab` | Rapid throwaway builds for testing interaction, logic, and product direction before committing to heavier implementation. | experimental | ABVX adapted |

### Project Context & Onboarding

| Skill | What It Does | Status | Origin |
|---|---|---|---|
| `project-context-bootstrap` | Detects the stack, asks the right project questions, and turns a weakly documented repo into a compact, agent-usable context surface. | experimental | ABVX adapted |
| `durable-context-maintenance` | Keeps repo-local context current after architecture, workflow, and test-flow changes so agents stop rediscovering the same facts. | experimental | ABVX adapted |

### Research, Knowledge & Reusable Methods

| Skill | What It Does | Status | Origin |
|---|---|---|---|
| `evidence-ledger-research` | Keeps claims, sources, calculations, and open questions in a disciplined evidence ledger. | experimental | ABVX original |
| `book-to-skill` | Converts books, papers, and long documents into reusable, progressive-disclosure agent skills. | experimental | ABVX adapted |

### Workflow, Handoffs & Multi-Track Work

| Skill | What It Does | Status | Origin |
|---|---|---|---|
| `dynamic-workflow-packets` | Orchestrates large coding, research, audit, or client-search tracks without losing verification and risk gates. | experimental | ABVX adapted |
| `handoff` | Produces compact continuation briefs for long-running work, agent resumes, and human handoffs. | experimental | ABVX adapted |

### Structured Data & Spreadsheet Work

| Skill | What It Does | Status | Origin |
|---|---|---|---|
| `spreadsheet-workbook-forensics` | Repairs and edits spreadsheets where workbook structure, formulas, and cell-level verification matter. | experimental | ABVX original |

## Install

Install one skill into Codex:

```bash
git clone https://github.com/markoblogo/abvx-agent-skills
cp -R abvx-agent-skills/skills/dynamic-workflow-packets ~/.codex/skills/
```

Install all skills:

```bash
git clone https://github.com/markoblogo/abvx-agent-skills
cp -R abvx-agent-skills/skills/* ~/.codex/skills/
```

Start a new agent session after installation so the skill descriptions are discovered.

## Repository Profile

Each public skill includes:

- `SKILL.md` - executable agent instructions
- `SKILL_CARD.md` - intended use, attribution, risks, evaluation, and version
- `agents/openai.yaml` - Codex UI metadata

The project follows the open Agent Skills shape: `SKILL.md` plus optional `scripts/`, `references/`, and `assets/`. For Codex compatibility, top-level frontmatter is kept conservative: `name`, `description`, `license`, `metadata`, and supported fields only.

## Validate

```bash
python scripts/validate.py
```

The validator checks required files, frontmatter, directory/name alignment, TODO placeholders, cards, UI metadata, and basic secret patterns.

## Philosophy

- Keep always-loaded context small.
- Prefer procedural rules over vague advice.
- Make skills easy to audit in diffs.
- Attribute upstream inspiration.
- Pair useful automation with risk gates and verification.

See [docs/abvx-skillpack-profile.md](docs/abvx-skillpack-profile.md) for the repository standard.

## Attribution

Several skills are inspired by public work from the broader agent tooling ecosystem. See [ATTRIBUTION.md](ATTRIBUTION.md).

## License

MIT. See [LICENSE](LICENSE).
