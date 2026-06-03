---
name: project-context-bootstrap
description: Bootstrap usable project context before deep implementation work. Use when entering a new or unfamiliar repo, installing agent workflows into an existing codebase, auditing stale docs, or preparing a project for repeatable long-running agent work. Detect the stack, ask the user about the project, summarize understanding, propose compact context artifacts, and update only with approval.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Project Context Bootstrap

Create a compact, durable working model of a repo before the agent starts inventing one from guesswork.

## Goal

Turn a repo with weak or missing agent-facing context into a repo with:

- a clear stack and structure summary;
- known commands and verification paths;
- durable context files or notes with real content;
- explicit approval before reorganizing existing docs.

## Workflow

1. **Detect**
   - inspect project manifests, lockfiles, workspace layout, test commands, and major directories;
   - detect whether context already exists: `AGENTS.md`, `docs/ai/`, runbooks, plans, or other agent-facing docs.
2. **Study existing context first**
   - if the repo already has useful docs, read them before proposing replacements;
   - separate what looks good, stale, missing, or conflicting.
3. **Ask**
   - have a real project-discovery conversation with the user;
   - cover what the product is, who uses it, main features, risky areas, workflow conventions, and external dependencies;
   - follow up until the project is actually understandable.
4. **Summarize**
   - restate your understanding in concise project language;
   - confirm accuracy before writing or reorganizing context.
5. **Propose**
   - suggest the smallest useful context structure:
     - top-level `AGENTS.md` or compact startup doc;
     - `docs/ai/architecture.md`;
     - `docs/ai/how-to-test.md`;
     - task-specific notes only if needed;
   - ask before reorganizing or overwriting anything durable.
6. **Populate**
   - write real content from code and user input, not placeholders;
   - include concrete commands, file paths, key modules, and current conventions.
7. **Validate**
   - verify the new context is small, accurate, and actually useful for the next session.

## Existing Repo Rules

- Preserve good context; do not replace it with generic scans.
- Show what you want to keep, improve, and add before changing layout.
- Never silently move or delete user-written docs.

## Compression Rules

- Keep startup context compact.
- Put deeper material behind explicit paths.
- Prefer one good entrypoint per topic instead of many tiny fragmented notes.

## Final Report

Include what was detected, what was confirmed by the user, what context was added or updated, and what should be read first in the next session.
