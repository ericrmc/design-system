---
session: 160
title: autonomous-drain-and-friction — assessment
engine_version_at_open: engine-v46
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

Engine-v46 active; operator directive S159-end: build autonomous-drain mode and friction-reduction CLI for agent-self-tooling.

## Agenda

1. Ship bin/selvedge drain shell driver invoking claude -p per iteration with halt-on-conditions.
2. Add §1.5 autonomous-mode branch in prompt-development v15 to v16 keyed on SELVEDGE_AUTONOMOUS=1 env var.
3. Add bin/selvedge submit-help <kind> CLI introspecting handler signatures to print payload shape lengths enums.
4. Add bin/selvedge drain-status JSON CLI exposing queue-depth halt-pending open-session for the drain script.
5. Configure .claude/settings.local.json permissions allowlist for headless drain invocations.
6. Run coding review loop and ship; engine-v46 to engine-v47 if methodology kernel touched.
