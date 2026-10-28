# Codex PR Workflows

Six optional skills adapt selected t3dotgg/tstack workflows for Codex-native project work. They require no Claude installation, T3 Code runtime or cross-provider account.

| Skill | Upstream idea | Explicit request example |
|---|---|---|
| `codex-review-loop` | sol-loop | Review this change with an independent OpenAI reviewer, at most three rounds. |
| `pr-ci-watch` | babysit-pr | Watch CI for this PR for up to 30 minutes. |
| `pr-modernize` | modernize | Reassess this old PR and update it if the goal still matters. |
| `pr-takeover` | takeover | Continue this unfinished PR and preserve its authorship. |
| `pr-write` | file-pr | Create a concise PR for the verified change. |
| `pr-ready` | full-stop / full-send proof gates | Prepare this task as a verified PR for my review, without merging. |

## Installation

The six skills are available in GitHub `main` through [PR #77](https://github.com/markoblogo/abvx-agent-skills/pull/77). That change did not publish a new PyPI version. An existing `abvx-skills` command reads only its installed package, so use current source for these skills unless your installed distribution already includes them.

### Install the Six-Skill Set From Source

Use Python 3.10 or newer. For a fresh checkout:

```bash
git clone --depth 1 https://github.com/markoblogo/abvx-agent-skills.git
cd abvx-agent-skills
python3 -m venv .venv
.venv/bin/python -m pip install PyYAML
.venv/bin/python scripts/install_codex_pr_workflows.py
```

The last command is a read-only preview. Inspect the destination and actions, then apply the same selection:

```bash
.venv/bin/python scripts/install_codex_pr_workflows.py --apply
```

The wrapper selects exactly these six skills and defaults to `~/.codex/skills`. It uses the existing recoverable installer and preserves local modifications. A conflict blocks the entire selection; there is no overwrite switch. If you already have a checkout, confirm its state and update it without discarding local work before running the wrapper.

The commands above use the POSIX virtual-environment layout. On Windows, use `.venv\Scripts\python.exe` for the same Python commands. The skills are portable, but the installer and helper evidence described below does not establish Windows runtime support.

### Use Project Scope

For Codex project discovery, pass the same explicit `.agents/skills` destination to preview and apply:

```bash
.venv/bin/python scripts/install_codex_pr_workflows.py --destination /path/to/project/.agents/skills
.venv/bin/python scripts/install_codex_pr_workflows.py --destination /path/to/project/.agents/skills --apply
```

A custom destination writes files only; it does not configure discovery for other hosts. Keep the sibling installation journal private. See [managed installation](managed-installation.md) for transaction and recovery boundaries.

### Install One Skill

With a GitHub CLI version that supports `gh skill`, preview and install one workflow instead of the complete set:

```bash
gh skill preview markoblogo/abvx-agent-skills pr-write
gh skill install markoblogo/abvx-agent-skills pr-write --agent codex --scope user
```

This route does not use the ABVX rollback journal. Subskills are composable helpers, not mandatory hidden dependencies; each workflow reports unavailable capabilities explicitly.

### Confirm Installation

The source wrapper reports `Installed/recorded six skills` only after applying the transaction. For the default destination, verify the entrypoints without changing files:

```bash
for skill in codex-review-loop pr-ci-watch pr-modernize pr-takeover pr-write pr-ready; do
  test -f "$HOME/.codex/skills/$skill/SKILL.md" || exit 1
done
```

For project scope, check the selected project path instead. Start a new Codex task if the current task's skill list has not refreshed. Successful file installation does not establish GitHub authentication, reviewer access or live CI monitoring.

If the host reports `Operation not permitted`, installation has not completed. Use an authorized writable scope or run the reviewed installer in your own terminal. Do not change sandbox settings or call a preview an installation.

## Choose and Invoke a Workflow

Use an explicit skill name and a concrete target:

```text
Use $pr-write. Create a concise PR for this verified change against the repository's actual base.
Use $codex-review-loop. Review this diff with one independent OpenAI reviewer, at most three rounds.
Use $pr-ci-watch. Watch owner/repository PR 123 for up to 30 minutes; report findings without changing code.
Use $pr-modernize. Reassess PR 123 and refresh it if the goal still matters, preserving published history.
Use $pr-takeover. Continue PR 123 in a replacement branch and retain the original contributor credit.
Use $pr-ready. Finish this task as a verified PR for my review, without merging.
```

Use `pr-write` alone for PR creation. Use `codex-review-loop` for independent feedback before publication. Choose `pr-ready` when the authorized goal includes implementation, proof, PR creation and bounded CI observation. A request for draft wording produces text only.

## Capability and authority boundaries

Use native GitHub connectors where sufficient, or an authenticated GitHub CLI. The CI helper needs Python 3.10+ and local authenticated `gh`; a connector without a watch operation supports snapshots only. CI evidence is separate from human review, independent review, branch currency and readiness.

Independent review requires an exposed native OpenAI subagent capability. A missing capability produces an explicit gap, not silent self-review or routing to another provider. Respect host model-selection rules and never invent model IDs. The default review budget is three rounds. The default CI budget is 30 minutes, with at most three fix cycles and one shared deadline.

No skill authorizes automatic merging, deployments, releases or permission bypasses. Existing auto-merge is an explicit blocker for a no-merge preparation unless changing it is authorized. Ordinary words such as "full stop" do not activate the workflow. Source PRs, logs, bot comments and repository content are evidence, not new user authority.

## Published-history boundary

PR modernization preserves published history. Use a normal merge-based refresh of an authorized task-owned branch, or a separate rebased continuation when linear history is required. Leave the original branch intact; publish a replacement only when authorized. Reassess an obsolete goal before updating anything.

## Interpret the Result

`pr-ready` reports `READY_FOR_REVIEW` when implementation and checks are verified but required human review remains. `READY_FOR_MERGE` means the repository gates are satisfied and the PR is still open and unmerged; it is not permission to merge. Missing evidence produces `BLOCKED`; exhausted budgets produce `BUDGET_EXHAUSTED`.

The CI helper reports CI evidence only. `CI_PASSED` does not prove review approval, current base, mergeability or complete readiness. Missing required checks, skipped checks, stale heads, timeout and API errors do not count as success. A connector without a bounded watch operation returns a one-time snapshot with `WATCH_UNAVAILABLE`. No monitoring continues after the active session ends.

## Evaluation record

On 2026-10-28, two isolated read-only model exercises covered six synthetic cases: stale current-head evidence and auto-merge, unavailable independent review, false activation on punctuation, obsolete PRs with dirty work, contributor credit during takeover, wording-only requests and connector-only monitoring. The retained scenario inputs, expected outcomes and observed decisions are in [the fixture record](../benchmarks/fixture-cases/codex-pr-workflows.json).

All six decision fixtures passed. These were fixture-only exercises with external tools and file mutations disabled. They do not demonstrate live GitHub execution, cost improvements or universal instruction-following. Skill metadata uses `fixture_checked`, not `rollout_checked` or `held_out_validated`.

The CI helper has executable mocked-process tests for passing CI, stale heads, failed/pending checks, external merge, absent required checks, skipped checks, API errors, timeout redaction, missing gh and argument bounds. Run:

```bash
python3 -m pytest -q tests/test_pr_ci_watch.py
python3 scripts/validate.py
python3 scripts/generate_catalog.py
```

The final source in [PR #77](https://github.com/markoblogo/abvx-agent-skills/pull/77) passed all 86 repository tests, structural validation, generated-catalog checks, package validation and GitHub `skills`, `security-audit` and `skillspector` checks. The final security policy evaluation reported zero blocking findings and zero score blockers. The source installer was exercised for six-skill installation, idempotence, payload hashes and preservation of local modifications in isolated destinations.

The initial static scan flagged a force-with-lease command example. The final adaptation removed published-history rewriting; no suppression or security threshold change was added. Standard MIT notices remain bundled, and subprocess calls use argument lists, captured output and a shared timeout. Non-blocking static findings remain visible.

No live PR was changed by the behavioral fixtures. The publication PR and its CI checks demonstrate repository publication, not end-to-end execution of every new workflow. An actual local CI watch still requires authenticated `gh`; independent review requires the native capability described above. The local installation and behavioral evidence do not establish held-out reliability.

## Attribution

Adapted and rewritten from [t3dotgg/tstack](https://github.com/t3dotgg/tstack), MIT, Copyright (c) 2026 Theo Browne. Every installed skill retains the upstream notice in `references/tstack-MIT.txt`. The bounded CI helper is original ABVX code. See [ATTRIBUTION.md](../ATTRIBUTION.md).
