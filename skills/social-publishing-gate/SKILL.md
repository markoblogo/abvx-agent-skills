---
name: social-publishing-gate
description: "Review and route social content before publishing. Use when drafting, adapting, auditing, scheduling, or monitoring posts for LinkedIn, X, Threads, Telegram, newsletters, or other distribution channels where brand voice, factual claims, platform fit, approvals, and no-spam guardrails matter. Enforce draft -> audit -> approval -> publish -> monitor, and never post or message externally without explicit user approval."
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Social Publishing Gate

Gate social distribution work so agents draft useful content without silently posting, spamming, or flattening brand voice.

## Core Rule

Treat every external post, reply, comment, DM, schedule, or reaction as a side effect. Drafts are safe. Publishing requires explicit approval.

Default path:

```text
source -> draft -> audit -> approval -> publish -> monitor
```

## Workflow

1. **Source**
   - identify the source idea, artifact, product update, thread, transcript, or link;
   - capture the intended audience, channel, goal, and non-goals;
   - preserve the user's point of view instead of inventing generic thought leadership.
2. **Draft**
   - create channel-native drafts, not one generic post copied everywhere;
   - keep one clear claim or insight per post;
   - mark assumptions, missing proof, and claims that need checking.
3. **Audit**
   - check factual claims, dates, numbers, links, names, and attribution;
   - remove generic AI phrasing, empty hype, fake certainty, and engagement bait;
   - check brand voice, privacy, legal, client confidentiality, and platform norms;
   - verify that calls to action are appropriate and not spammy.
4. **Approval**
   - show the final draft and the audit notes;
   - ask for explicit approval before any external write action;
   - if the user approves with edits, re-audit the changed draft.
5. **Publish**
   - use only approved channels, accounts, and tools;
   - preserve a record of the final text, destination, timestamp or schedule, and tool used;
   - stop if credentials, account identity, or target destination are ambiguous.
6. **Monitor**
   - collect read-only response signals when available;
   - draft follow-ups for review instead of auto-replying;
   - route reusable lessons into `agent-learning-layer-triage`.

## Channel Notes

- **LinkedIn**: be extra strict about over-optimized hooks, fake virality language, engagement bait, and automated comment behavior.
- **X / Threads**: split long ideas into native threads only when each post still has standalone value.
- **Telegram / MediaHub**: distinguish posting to owned channels from replying in communities; use approvals for both.
- **Newsletters**: check subject, preview text, links, unsubscribe/compliance expectations, and source attribution.

## Allowed Automation

Allowed without extra approval:

- drafting;
- content audit;
- formatting variants;
- read-only analytics summaries;
- scheduling plan proposals;
- monitoring recommendations.

Requires explicit approval:

- publishing;
- scheduling;
- commenting;
- replying;
- reacting;
- sending DMs;
- scraping private or authenticated data;
- using third-party publishing or scraping APIs with user credentials.

## Output Shape

Return:

- channel and audience;
- final draft;
- audit notes;
- approval status: `draft_only`, `needs_approval`, `approved_to_publish`, or `published`;
- destination and schedule if approved;
- monitoring plan or follow-up drafts.

## Anti-Patterns

- Do not auto-post because a draft looks good.
- Do not optimize for vanity engagement at the cost of truth or trust.
- Do not imitate a person without their provided voice samples or approval.
- Do not scrape, message, or enrich prospects without explicit permission and policy review.
- Do not hide uncertainty in confident marketing language.

## Final Report

State what was drafted, what was audited, what still needs approval, and whether any external side effect happened.
