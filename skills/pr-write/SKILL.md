---
name: pr-write
description: Create or update a concise GitHub pull request for an already verified code change. Use when the user asks to open or file a PR, or invokes pr-write. Do not publish a PR when the user only asks for draft wording.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
  abvx_eval_tier: fixture_checked
---

# PR Write

Explain the concrete problem and resulting behavior. Match the repository's PR template and conventions. A request for text alone authorizes drafting only.

## Verify the final scope

Before updating an existing PR branch, inspect auto-merge and merge-queue state. If either can merge it automatically, stop updates unless changing that state is authorized. Never disable it silently or promise no merge while it remains enabled.

Resolve the repository, current branch, actual target base and complete diff, including relevant untracked files. Check for an existing PR before creating one. Never stage, commit or include unrelated user work.

Read the repository template and recent titles for conventions. Confirm intended behavior with appropriate evidence, and distinguish pre-existing failures. Do not claim tests ran when they did not.

If the authorized creation requires committing and pushing this task's change, do so on a task-owned non-default branch after verification. Inspect exactly what is staged first. Do not rewrite unrelated commits or push the default branch.

## Write

Lead the title and description with the problem and resulting behavior, not an inventory of files. Use a concrete before/after example where it helps. For small changes, one or two sentences and a validation line are sufficient.

Include:

- why the change matters and what now happens;
- verification actually observed, with material gaps;
- source PR/contributor credit when continuing another person's work.

Use accurate model/harness attribution only when repository policy requires it. Follow the user's language and formatting preferences; do not force an emoji signature. Never invent a model name.

Check the whole draft and attachments for secrets, private local paths, customer data and private transcript excerpts. Do not upload private logs to prove a public claim.

## Publish only the requested artifact

Use the connected GitHub tools when sufficient, otherwise authenticated `gh`. Pass multiline bodies as structured text, or save a UTF-8 body file and use `--body-file`; never interpolate body text into shell code.

Honor an explicit draft request. Otherwise create a normal PR when verification is sufficient and the repository expects it; use a draft with an honest blocker if the task calls for preserving incomplete work. For a wording-only request, return the text without creating or changing anything.

Verify the returned PR URL and head/base. Update the existing PR rather than creating a duplicate. Attach the PR to the current Codex task if that host exposes an attachment tool.

Do not post unsolicited comments, resolve reviews, enable auto-merge, merge, create a release, or start indefinite monitoring. If explicitly asked to watch CI, continue with `pr-ci-watch` or its native equivalent.

## Report

Return the PR link or clearly labelled draft text, head/base, publication/draft state and concise validation. State any remaining gap.

## Provenance

Adapt t3dotgg/tstack `file-pr` and its comment-formatting discipline. Keep factual attribution and concise writing while removing mandatory model signatures and emoji.
