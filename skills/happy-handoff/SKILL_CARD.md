# Skill Card: happy-handoff

## Description
Schedules the current Codex Desktop task to resume through Happy on Android, while preserving its task ID, workspace, and approval boundaries.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use after the user says `ухожу`, explicitly asks to continue in Happy, or invokes the skill during an active Codex Desktop task.

## Out of Scope
Do not use it to install or authenticate Happy, create an unrelated session, enable permissive execution, or treat a scheduled process as proof of Android receipt.

## Sources and Attribution
Original ABVX workflow using the external MIT-licensed `slopus/happy` CLI.

## Inputs and Outputs
Inputs: `CODEX_THREAD_ID`, current working directory, authenticated Happy CLI, and a concise checkpoint.

Outputs: a scheduling receipt, retained task checkpoint, and an explicit Android-observation boundary.

## Risks and Mitigations
- Risk: resuming the wrong task. Mitigation: validate and pass the exact `CODEX_THREAD_ID`.
- Risk: losing dirty work. Mitigation: preserve the current directory and prohibit cleanup, stash, or commit during handoff.
- Risk: weakening approvals. Mitigation: prohibit `--yolo` and permission bypasses.
- Risk: false success. Mitigation: distinguish scheduling from observed Android receipt.

## Evaluation
Fixture-checked for activation and false activation. Launcher tests cover macOS/Linux command construction, unsupported platforms, and exact dry-run task/workspace receipts. One local macOS-to-Android rollout is documented separately and is not a universal reliability claim.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
