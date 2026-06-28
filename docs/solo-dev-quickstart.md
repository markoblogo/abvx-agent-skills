# Solo Dev Quickstart

Use this path when you want ABVX skills working in one local environment with minimal setup.

## Fastest Path

```bash
pip install abvx-agent-skills
abvx-skills install
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

## First 10 Minutes

1. Install 3-5 skills, not the whole repo by default.
2. Start one real task with `minimal-diff-builder` or `diagnose`.
3. Add `rtk-assisted-shell` if shell output gets noisy.
4. Add `handoff` only when sessions start spanning multiple resumptions.

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
