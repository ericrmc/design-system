---
session: 108
title: monitor-external — close
engine_version_at_close: engine-v31
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S108 ships bin/selvedge monitor-external (status, next-input, harvest-ef) per DV-S106-3 with four-iteration T-30 review loop converging clean.

## Engine version

- engine-v31 to engine-v31, no bump (capability-only addition).
## What was done

- Implemented cmd_monitor_external + helpers in selvedge/cli.py with three subcommands.
- Added 21 pytest cases in state/tests/test_monitor_external.py covering refusals and happy paths.
- Ran four iterations of the engine-v31 substrate-enforced coding review loop.
## State at close

- monitor-external CLI ships generic across external workspaces; harvest-ef requires explicit SELVEDGE_WORKSPACE.
- OI-S106-2 closed via DV-S108-1 closes_issue effect; full test suite passes 161 tests.
## Open issues

- No new issues opened; existing OIs from prior sessions remain unchanged.
## What the next session should address

- S109 operator-discretionary: run tools/bootstrap-external-workspace.sh against /Users/ericmccowan/Development/selvedge-disaster-response with slug disaster-response.
- After bootstrap, populate applications/001-disaster-response/brief.md from archived v7 source for the first external session.
- FR-S107-11 still pending: spec_only session refreshing engine-manifest section three file-set enumeration through migration 018.
## Validator at close

- pytest 161 of 161 passed; T-30 review_pass iter 4 outcome clean.
