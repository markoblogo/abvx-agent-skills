# Team Rollout Playbook

Use this path when you want a small, stable skill layer that standardizes how agents work across one repository or team.

## Start Small

Roll out one stack for repo onboarding and one stack for delivery control before adding domain-specific skills.

Recommended baseline:

- `project-context-bootstrap`
- `durable-context-maintenance`
- `brief-first-execution`
- `delivery-preflight-gate`
- `handoff`

Add `dynamic-workflow-packets` only when work regularly splits into parallel tracks or long-running packets.

## Suggested Rollout Order

1. Establish the repo context surface with `project-context-bootstrap`.
2. Keep it current with `durable-context-maintenance`.
3. Require one live brief before substantial work with `brief-first-execution`.
4. Gate long implementation runs with `delivery-preflight-gate`.
5. Normalize continuation quality with `handoff`.

## Project-Scoped Installation

For teams using GitHub CLI agent skills:

```bash
gh skill install markoblogo/abvx-agent-skills project-context-bootstrap --agent codex --scope project
gh skill install markoblogo/abvx-agent-skills durable-context-maintenance --agent codex --scope project
gh skill install markoblogo/abvx-agent-skills handoff --agent codex --scope project
```

For teams using the packaged installer:

```bash
pip install abvx-agent-skills
abvx-skills install --destination ./.agents/skills project-context-bootstrap durable-context-maintenance handoff
```

For Codex, use `.agents/skills` for project discovery and `~/.codex/skills` for the existing user installation path used by this pack. A custom destination only writes files; it does not configure another agent's discovery rules.

## Optional PR Workflow Rollout

Introduce `pr-write` and `codex-review-loop` for a small pilot before adopting `pr-ready`. Add `pr-ci-watch`, `pr-modernize` or `pr-takeover` only for a demonstrated workflow need. Use the [Codex PR workflow guide](codex-pr-workflows.md) to install from current source and check capabilities; the new source skills are not implied by an older installed PyPI package.

Agree on the PR base, required checks, reviewer access and the scope of authorized writes. Keep independent review distinct from self-review, and CI success distinct from human approval. Use one watcher per PR, a shared observation deadline and bounded fix cycles.

The six skills do not merge, deploy or publish releases. `pr-modernize` preserves published history and uses a separate continuation when a linear-history policy requires rebasing. Existing auto-merge or queue state must be handled explicitly before branch updates. Keep team-specific instructions in repository guidance rather than editing every installed skill.

## Repo Hygiene Pattern

- Keep startup instructions compact.
- Push bulky process docs into referenced files.
- Treat skills as behavior layers, not as giant prompt dumps.
- Add or revise skills only after repeated evidence from real work.

## When To Expand The Stack

- Add `dynamic-workflow-packets` when one task repeatedly fans out into separate tracks.
- Add `loopops-protocol` when repeated prompts keep turning into ad hoc process.
- Add `delivery-baseline-audit` when long tasks are being called complete against a broken baseline.
