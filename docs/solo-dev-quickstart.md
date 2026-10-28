# Solo Dev Quickstart

Use this path when you want ABVX skills working in one local environment with minimal setup.

## Choose One Starter Profile

```bash
pip install abvx-agent-skills
abvx-skills profiles
abvx-skills install --profile context --dry-run
abvx-skills install --profile context
abvx-skills doctor
```

If PyPI is temporarily unavailable, use GitVerse's PyPI mirror for that install command only:

```bash
python -m pip install abvx-agent-skills --index-url https://pypi-mirror.gitverse.ru/simple/
```

If you prefer GitHub CLI agent-skills installation:

```bash
gh skill install markoblogo/abvx-agent-skills minimal-diff-builder --agent codex --scope user
gh skill install markoblogo/abvx-agent-skills diagnose --agent codex --scope user
gh skill install markoblogo/abvx-agent-skills frontend-product-builder --agent codex --scope user
```

Swap `--agent codex` for `cursor`, `claude-code`, or `gemini-cli` if that is your primary host.

## Recommended Starter Stack

- `minimal-diff-builder`: shortest correct implementation path
- `diagnose`: debugging discipline
- `rtk-assisted-shell`: reduce shell noise
- `token-efficient-execution`: reduce wasted reads and narration
- `frontend-product-builder`: only if you regularly ship UI

Choose `context`, `debug`, or `delivery`; names are also supported. Bare install is an error and the full pack requires `--all`. See [managed installation](managed-installation.md) for update previews, local edits, manifest, rollback and recovery.

## First 10 Minutes

1. Install 3-5 skills, not the whole repo by default.
2. Start one real task with `minimal-diff-builder` or `diagnose`.
3. Add `rtk-assisted-shell` if shell output gets noisy.
4. Add `handoff` only when sessions start spanning multiple resumptions.

## Add Codex PR Workflows When Needed

For PR writing, start with `pr-write`; for substantial independent review, add `codex-review-loop`. Use `pr-ready` when the task explicitly includes implementation, verification and a PR ready for review without merging. Use `pr-ci-watch`, `pr-modernize` and `pr-takeover` for their specific jobs rather than installing a large default process.

The six skills are available in GitHub `main`. Their introduction did not publish a new PyPI version. Follow the [source installation and capability checks](codex-pr-workflows.md#installation), including preview and project-only options. No Claude or T3 Code installation is needed. Independent review needs native OpenAI subagents; continuous local CI observation needs authenticated `gh`.

Example request after installation:

```text
Use $pr-ready. Prepare this change as a verified PR for my review, without merging.
```

The workflow never merges the PR. Unknown checks, unavailable review or existing auto-merge are reported as explicit gaps instead of success.

## Good Default Pairings

- Debugging: `diagnose` + `repo-debugging-ledger`
- Small feature work: `minimal-diff-builder` + `delivery-preflight-gate`
- Frontend polish: `frontend-product-builder` + `design-critique-polish`
- Long sessions: `handoff` + `compaction-survival`

## Verification

```bash
abvx-skills list
abvx-skills validate
```

If you installed via `gh skill`, use:

```bash
gh skill list
```
