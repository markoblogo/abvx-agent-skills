# ABVX Agent Skills

Small, reviewable, validation-gated agent skills for Codex-style project work.

This repository publishes opinionated ABVX skillpacks: compact `SKILL.md` workflows with clear triggers, attribution, risk notes, and validation. These are not prompt dumps. They are portable, versioned agent capabilities meant to be loaded on demand through the Agent Skills progressive-disclosure model.

## Skills

| Skill | Use When | Status | Origin |
|---|---|---|---|
| `dynamic-workflow-packets` | Large multi-track coding, research, audit, or job/client-search workflows | experimental | ABVX adapted |
| `designmd-brand-kit` | Brand-aware frontend work, landing pages, pitch pages, redesigns, client audits | experimental | ABVX adapted |
| `evidence-ledger-research` | Source-sensitive research, document QA, calculations, citation checks | experimental | ABVX original |
| `repo-debugging-ledger` | Debugging with hypotheses, checked locations, and loop breakers | experimental | ABVX original |
| `skillopt-evolve-skills` | Improving skills or AGENTS.md-style instructions after real task experience | experimental | ABVX adapted |
| `spreadsheet-workbook-forensics` | Excel/workbook edits where structure and cell verification matter | experimental | ABVX original |

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
