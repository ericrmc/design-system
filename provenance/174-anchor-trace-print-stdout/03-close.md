---
session: 174
title: anchor-trace-print-stdout — close
engine_version_at_close: engine-v47
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S174 ships FR-S173-1 --print stdout mode on bin/selvedge export --provenance --anchor; first FR-driven coding session post-DV-S173-1.

## Engine version

- engine-v47 unchanged.
## What was done

- Added --print flag (dest=print_stdout) on export subparser in selvedge/cli.py.
- cmd_export in selvedge/export/__init__.py emits result preview to stdout under --print and refuses non-anchor or --write combos with rc=2.
- Added 3 pytest cases in state/tests/test_export.py covering --print emission and rejection paths; full test_export.py 15/15 green.
- DV-S174-1 substantive adopt with 3 supports + 3 alternatives R-1.1 (argparse-mutex inferior_tradeoff) R-1.2 (cross-mode violates_gate) R-1.3 (strip-JSON breaks_invariant).
- Reviewer subagent §7 clean iteration 1 with 1 low-severity acknowledgment finding only.
- Disposed FR-S173-10 (FR-S173-1) citing DV-S174-1; FR-S173-11..15 remain queued for next sessions.
## State at close

- Anchor-trace tool now has tactical-usage ergonomic per S173 D-26 mandate; FR-S173-2 spec_only and FR-S173-3 calibration-watch remain queued.
## Open issues

- EF-S173-1/2/3 still untriaged plus EF-S172-1/2 plus this session emits EF-S174-1 + EF-S174-2; 5 untriaged EFs.
## What the next session should address

- FR-S173-2: spec_only session amends prompts/development.md §5 with chain-walk recommended-clause naming invocation points + depth defaults per D-26 synthesis.
- FR-S173-3 calibration-watch begins: track tactical anchor-trace invocation count across S175..S179; surface calibration-EF if non-use pattern continues despite --print landing.
- Triage EF-S173-1 seal-grade plus EF-S172-1 plus EF-S174-1 at next operator-present session; v19 §1.5 disqualifies EF-S173-2/3 + EF-S172-2 + EF-S174-2 audit-step rows as procedural self-dispose.
- If bare-PROMPT.md auto-proceed, prefer FR-S173-2 spec_only single-clause edit (priority-2 tractable MEDIUM-OI substitute under v19 §1.5 since FR-driven and execution-shaped).
## Validator at close

- test_export.py 15 passed; --print smoke test against DV-S173-1 produced 12-node 27-edge markdown body to stdout with no provenance/anchor-traces/ disk write.
