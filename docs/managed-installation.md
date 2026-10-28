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
abvx-skills install --profile debug -d ./.agents/skills --dry-run
abvx-skills install --profile debug -d ./.agents/skills
abvx-skills doctor -d ./.agents/skills
```

For Codex project discovery, use `.agents/skills`. The default user destination remains `~/.codex/skills`. Custom destinations do not change an agent's discovery configuration.

## Current Source Versus Installed Package

`abvx-skills` reads its installed package, not GitHub `main`. A source merge does not update PyPI or already installed skills. The six [Codex PR workflows](codex-pr-workflows.md) landed in [PR #77](https://github.com/markoblogo/abvx-agent-skills/pull/77) without a new package release.

Use `scripts/install_codex_pr_workflows.py` from a current repository checkout for that six-skill set. It previews by default and requires `--apply` to install. It uses the same transaction, hash and local-change protections as the packaged installer, with no overwrite switch. It is a source wrapper, not an additional named CLI profile.

The source wrapper records state beside its selected destination. An older packaged CLI's `doctor` compares against its own bundled source and may not recognize skills added later; do not treat that as proof that current-source installation failed. Compare against the checkout that supplied the installation, or install that checkout as the CLI package before using package-relative update checks. See the workflow guide for reproducible setup and verification.

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

State is stored beside, not inside, the skill discovery root: for `~/.codex/skills`, use `~/.codex/.skills.abvx-skills/manifest.json`. For `/project/.agents/skills`, use `/project/.agents/.skills.abvx-skills/`. The doctor output includes the exact path. Archived SKILL.md files therefore do not become discoverable skills inside the managed destination.

Manifest schema 1 records selected profiles, installed package/skill versions, upstream identity, per-file hashes and executable bits, payload digests and the latest transaction. Hashes prove local equality, not publisher authenticity. Doctor reports `ok`, `modified`, `missing`, `unsafe` (files, symlinks or unreadable payloads), package updates available and unmanaged skills; it compares against the locally installed package, not a live registry. Runtime bytecode and .DS_Store are excluded. Unmanaged skills are listed, not claimed verified or automatically adopted.

Backups and journals are retained in the sibling state's transactions directory. They may contain private customized instructions: new POSIX state uses a private 0700 directory and 0600 metadata files. Keep this state private and do not commit it by default. No automatic history deletion or background polling is performed.

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
