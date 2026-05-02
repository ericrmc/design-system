---
session: 165
title: spec-version-alias-example-alignment-and-bare-prompt-validation — close
engine_version_at_close: engine-v47
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S165 ships prompt-development v17 §6 example alignment per EF-S164-1, triages 2 S164 EFs, disposes 3 S164 FRs, and validates first bare-PROMPT.md auto-proceed run via EF-S165-1.

## Engine version

- engine-v47 unchanged.
## What was done

- DV-S165-1 bumps prompt-development v16 to v17; §6 spec-version supersedes example aligned from <spec>@<n> to SPEC-<spec>-v<n> form per EF-S164-1.
- EF-S164-1 disposed (addressed by DV-S165-1); EF-S164-2 disposed (procedural audit-step:0 self-disposes).
- FR-S164-7 disposed (substantive cluster deferred to operator-present session per §1.5 tactical-skip); FR-S164-8 disposed (validated by S165 plus EF-S165-1 friction calibration); FR-S164-9 disposed (addressed by DV-S165-1).
- EF-S165-1 surfaces bare-PROMPT.md first-run friction: tactical-vs-substantive path choice is itself load-bearing under operator absence; FR-S164-8 conflates two satisfaction routes.
## State at close

- Active specs: engine-manifest v47, methodology v12, prompt-application v3, prompt-development v17, workspace v3.
## Open issues

- 0 HIGH, 25 MEDIUM, 19 LOW open-issues unchanged this session; 49 total.
## What the next session should address

- Pick from FR-S164-7 substantive cluster (FR-S162-12 self-dev subtraction-discipline arc, FR-S161-15 submit-help schema registry plus orient §Why ext, or FR-S163-7 cluster work) under operator presence.
- If second bare-PROMPT.md session also opts tactical, consider tightening §1.5 to name operator-absent default (prefer tactical scope) explicitly per EF-S165-1 friction observation.
- Triage EF-S165-1 calibration and EF-S165-2 audit-step rows at next session-open.
## Validator at close

- tools/validate.sh to be run pre-commit; spec-version v17 ships single-clause edit, no migration, no executable change.
