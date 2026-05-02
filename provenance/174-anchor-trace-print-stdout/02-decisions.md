---
session: 174
title: anchor-trace-print-stdout — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Ship --print stdout mode on bin/selvedge export --provenance --anchor; scope to anchor mode and refuse --write combination.

**Kind:** substantive.  **Outcome:** adopt process_rule `anchor-trace-print-stdout-mode`.

**Why.**

- (prior_decision) DV-S173-1 adopted the tactical-usage shape with --print stdout coding FR as lead deliverable; this session executes the mandated FR. [DV-S173-1]
- (prior_decision) DV-S109-1 ceremony-subtraction restricts scope to FR-S173-1; broader batch FR-S173-13 (--summary --json --limit-open) stays deferred. [DV-S109-1]
- (review_finding) Reviewer subagent iteration 1 returned clean with one low-severity acknowledgment finding only.

**Effects.**

- modifies selvedge/cli.py: add --print flag (dest=print_stdout).
- modifies selvedge/export/__init__.py: --print emits preview to stdout, refuses --write combo.
- creates state/tests/test_export.py: three new pytest cases for --print.

**Rejected alternatives.**

- **R-1.1.** Use add_mutually_exclusive_group for --print vs --write at argparse level instead of a runtime check.
  - (inferior_tradeoff) Argparse mutex would not catch --print + --session/--issues invalid combo; runtime check carries both rejections with clearer text.
- **R-1.2.** Extend --print to --session and --issues exports for cross-mode consistency.
  - (violates_gate) Out of FR-S173-1 scope which names anchor-trace only; cross-mode --print belongs to deferred FR-S173-13 batch.
- **R-1.3.** Strip JSON metadata wrapper from existing dry-run path so dry-run emits raw markdown by default; skip --print flag.
  - (breaks_invariant) Dry-run JSON+preview shape is documented operator-facing surface; --print preserves dry-run contract while adding opt-in raw channel.
