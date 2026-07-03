# Skill Card: social-publishing-gate

## Description
Gates social distribution work through source, draft, audit, approval, publish, and monitor steps so agents can help with posts and replies without unsafe automation.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for LinkedIn, X, Threads, Telegram channels, newsletters, and MediaHub-style distribution workflows where the agent should draft or audit content, then wait for approval before publishing, replying, scheduling, or sending.

## Out of Scope
Do not use as an auto-growth bot, lead-spam workflow, private-data scraper, or bypass for platform policies. It does not provide LinkedIn automation, Apify scraping, Publora posting, or any bundled external connector.

## Sources and Attribution
ABVX adapted. Informed by ABVX approval-gate practice and the draft, audit, approval, read-side monitoring, and publishing-side separation patterns observed in sergebulaev `linkedin-skills`. The ABVX version is rewritten as a platform-neutral publishing gate and does not install, vendor, or depend on the upstream skill pack.

## Inputs and Outputs
Inputs: source content, target channels, audience, brand voice, publishing constraints, destination accounts, approval state, and optional read-only analytics.

Outputs: channel-native draft, audit notes, approval status, destination or schedule record, monitoring plan, and follow-up drafts that still require approval.

## Risks and Mitigations
- Risk: accidental external side effects. Mitigation: classify every publish, reply, reaction, schedule, and DM as approval-required.
- Risk: spam or engagement bait. Mitigation: audit for platform fit, useful substance, and trust impact.
- Risk: inaccurate claims. Mitigation: mark unverifiable claims and require fact checks before approval.
- Risk: voice flattening. Mitigation: preserve provided source voice and avoid generic AI phrasing.
- Risk: platform or credential misuse. Mitigation: stop when account identity, destination, or permission is unclear.

## Model Sensitivity
Works best on models that can separate drafting from side effects and can preserve a specific voice without over-optimizing for engagement.

## Composable With
- `evidence-ledger-research`
- `designmd-brand-kit`
- `idea-to-ship-gates`
- `agent-learning-layer-triage`
- `private-vs-publishable-skill-audit`
- `web-quality-audit`

## Anti-Patterns
- auto-posting without approval
- engagement farming
- fake authority or invented metrics
- private-data scraping without explicit permission
- generic cross-posting that ignores channel norms

## Evaluation
Evaluated by structural validation and by checking whether social tasks produce auditable drafts and approval records before any external side effects.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
