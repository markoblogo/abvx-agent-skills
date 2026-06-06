---
name: private-vs-publishable-skill-audit
description: Audit a private skill, prompt pack, or assistant workflow before publishing it. Use when extracting public reusable method from client, product, team, or repository-specific agent instructions. Mark private vs mixed vs reusable content, rewrite the mixed layer, and gate release on decontextualization.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---

# Private Vs Publishable Skill Audit

Audit a private skill pack before turning any part of it into a public release.

## Goal

Separate:

- private operating detail that must stay internal;
- mixed content that needs rewriting;
- reusable method that can be published.

## Workflow

1. **Inventory the source pack**
   - list skills, references, templates, examples, and policy notes;
   - note which files carry product, client, or repo-specific detail.
2. **Classify each item**
   - `private`: should not be published;
   - `mixed`: useful core, but still carries contextual leakage;
   - `reusable`: already abstract enough to publish.
3. **Check for leakage**
   - product names;
   - internal role names;
   - routes, paths, commands, and runbooks;
   - operational constraints that only make sense inside the private system;
   - examples that reveal the original environment.
4. **Rewrite the mixed layer**
   - remove names and internal identifiers;
   - convert narrow examples into generic ones;
   - preserve the method, not the original context.
5. **Run the publication gate**
   - after cleanup, ask whether the artifact still makes sense outside the source environment;
   - if not, keep rewriting or keep it private.
6. **Package the release set**
   - publish only the reusable artifacts;
   - keep the private source pack separate from the public one.

## Release Gate

An artifact is publishable only if both are true:

- it remains useful after private names, paths, and roles are removed;
- it does not expose constraints or operating detail that belong only to the private source.

## Final Report

Return the classified inventory, the release-safe set, the rewritten mixed items, and the reasons for anything left private.
