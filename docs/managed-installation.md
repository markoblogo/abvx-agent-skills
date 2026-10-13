# Managed installation and updates

Version 0.16 adds explicit selection, whole-set preflight, staged writes, retained backups and a per-destination manifest. It does not enable agent jobs or install every skill automatically.

## Choose a small profile

| Profile | Skills |
|---|---|
| context | token-efficient-execution, shell-output-compaction, lean-context-layout, compaction-survival |
| debug | diagnose, bug-evidence-protocol, test-driven-execution |
| delivery | delivery-preflight-gate, delivery-baseline-audit, public-release-verification |

```sh
abvx-skills profiles
abvx-skills install --profile context --dry-run
abvx-skills install --profile context
abvx-skills doctor
```

Profiles select only the named workflows; they do not install companion tools or grant permissions. Review any optional companion mentioned by a skill separately. Profiles can be installed sequentially; the manifest records their union. Named skills remain supported. Installing the whole catalog requires explicit `--all`.

For a project-local setup, pass the same destination to each command:

```sh
abvx-skills install --profile debug -d ./.codex/skills --dry-run
abvx-skills install --profile debug -d ./.codex/skills
abvx-skills doctor -d ./.codex/skills
```

## Preview and local changes

The preview checks every selected package payload and destination before any write. It lists install/update/adopt/unchanged/conflict actions and added, removed and changed file paths. Preview and doctor do not create an absent destination.

An unchanged managed skill can be updated to the package currently installed for the CLI. A different unmanaged skill or locally edited managed skill blocks the entire selection. Identical unmanaged files can be adopted without changing them. `--force` explicitly permits replacement, retaining the old directory in transaction history; it does not discard the old payload.

```sh
python -m pip install --upgrade abvx-agent-skills
abvx-skills doctor
abvx-skills install --profile context --dry-run
# Only when the preview and preservation of old payloads are understood:
abvx-skills install --profile context --dry-run --force
abvx-skills install --profile context --force
```

## Manifest and history

State is stored beside, not inside, the skill discovery root: for `~/.codex/skills`, use `~/.codex/.skills.abvx-skills/manifest.json`. For `/project/.codex/skills`, use `/project/.codex/.skills.abvx-skills/`. The doctor output includes the exact path. Archived SKILL.md files therefore do not become discoverable skills inside the managed destination.

Manifest schema 1 records selected profiles, installed package/skill versions, upstream identity, per-file hashes and executable bits, payload digests and the latest transaction. Hashes prove local equality, not publisher authenticity. Doctor reports `ok`, `modified`, `missing`, package updates available and unmanaged skills; it compares against the locally installed package, not a live registry. Runtime bytecode and .DS_Store are excluded. Unmanaged skills are listed, not claimed verified or automatically adopted.

Backups and journals are retained in the sibling state's transactions directory. They may contain private customized instructions: keep this state private and do not commit it by default. No automatic history deletion or background polling is performed.

## Rollback and recovery

```sh
abvx-skills rollback
abvx-skills recover
```

Rollback restores the latest committed transaction and previous manifest; earlier installed profiles are retained. Post-install local changes block normal rollback. `rollback --force` preserves the current directories under that transaction's replaced history before restoring. Recover restores an interrupted applying transaction and also retains any current directories it displaces. Use the same `-d` destination as installation.

The installer stages the complete set on the same filesystem, rechecks destination files, serializes cooperating CLI commands with an OS lock, and journals the previous manifest before applying. Ordinary commit failures restore the complete set. Process interruption releases the OS lock; new installs are blocked until recover completes. Prepared/staging-only transactions have made no skill changes.

Renames are atomic per skill directory. Multiple directories cannot become visible simultaneously through a single filesystem operation; external agents/readers may see intermediate state during commit. Finish updates before starting a new agent session. Recovery is tested for process termination and ordinary filesystem failures; arbitrary hardware/power failure and interference by programs that ignore the installer lock are not guaranteed atomic.

## Compatibility and migration

`abvx-skills install` with no selection now returns an error instead of installing everything. Use names, one profile, or `--all`. The CLI remains Python 3.10+. Core transaction tests run on macOS and Linux; Windows lock support is implemented but not verified in this release.

Existing copies from manual cp or gh skill are unmanaged until an explicit named/profile install adopts matching bytes or replacement is approved with --force. Those external installers do not acquire ABVX transaction guarantees. Installation state is per destination; no hosted service or cross-machine synchronization is introduced.
