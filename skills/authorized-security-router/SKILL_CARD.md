# Skill Card: authorized-security-router

## Description
Routes authorized defensive security and reverse-analysis tasks by scope, target type, intent, and toolchain before taking action.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for APK review, static binary triage, frontend JavaScript security review, firmware inventory, malware/YARA analysis, API/LLM/supply-chain audit, and security issue intake when the task needs evidence-led classification and safe next steps.

## Out of Scope
Do not use for exploit development, EDR/AV bypass, credential extraction, persistence, phishing, C2, destructive testing, WAF bypass, live brute force, or unauthorized scanning.

## Sources and Attribution
ABVX adapted the routing pattern from `zhaoxuya520/reverse-skill` while removing offensive execution flows and adding explicit authorization, blocked-action, and defensive-reporting gates.

## Inputs and Outputs
Inputs: authorization statement, target boundary, artifact type, user intent, allowed toolchain, and desired report/remediation outcome.

Outputs: route decision, paired skills, evidence ledger fields, defensive analysis plan, blocked-action handling, and report shape.

## Composable With
- `evidence-ledger-research`
- `delivery-preflight-gate`
- `repo-issue-triage`
- `browser-verification`
- `web-quality-audit`

## Risks and Mitigations
- Risk: sliding from triage into exploitation. Mitigation: require route classification and blocked-action checks before tool use.
- Risk: unclear authorization. Mitigation: stop at `ROUTE_UNCLEAR` until scope is explicit.
- Risk: unsupported security claims. Mitigation: require evidence location and confidence per finding.
- Risk: copying offensive playbooks. Mitigation: route to defensive alternatives only.

## Evaluation
Evaluated by structural validation and manual review against defensive security triage workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
