# Happy Handoff Pilot

`happy-handoff` was checked at two levels on 2026-09-08.

## Deterministic checks

- macOS and Linux `script` command shapes: covered by tests;
- unsupported platform: rejected explicitly;
- dry run: preserves the exact task ID and working directory;
- CI path: uses fake `happy` and `script` executables and does not contact a device.

## Observed local rollout

One macOS pilot used Happy 1.2.3 with Codex Desktop and an Android client. One message sent from Android reached the Mac-hosted Codex task, and one Codex response returned to the same Happy session. The test workspace remained unchanged.

This is one observed rollout, not a general reliability benchmark. A launcher receipt proves only `scheduled`; Android receipt remains unproven until the user sees it in Happy.
