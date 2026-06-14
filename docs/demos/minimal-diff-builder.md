# Demo: minimal-diff-builder

## Problem

Coding agents often turn a small bug into a broad refactor.

## Task

Patch one narrow failing path without widening scope, introducing new abstractions, or rewriting unrelated tests.

## Without the skill

Likely failure mode:

- changes unrelated files
- introduces wrappers or abstractions that were not needed
- rewrites tests before isolating the actual failure

## With the skill

Expected behavior:

- inspect only the relevant files first
- patch the narrow failing path
- add or update one focused test if behavior changed
- run targeted verification before claiming the task is done

## Try it

```bash
gh skill preview markoblogo/abvx-agent-skills minimal-diff-builder
gh skill install markoblogo/abvx-agent-skills minimal-diff-builder --agent codex --scope user
```

Then tell the agent:

```text
Use minimal-diff-builder. Implement the smallest correct fix for this issue.
```
