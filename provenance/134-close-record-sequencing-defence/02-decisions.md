---
session: 134
title: close-record-sequencing-defence — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Ship T-3X close-record-required trigger and uniform parse-time atom validator; engine-v40 to engine-v41

**Kind:** substantive.  **Outcome:** adopt engine_version `engine-v41`.

**Why.**

- (deliberation) C-1 convergence across P-1, P-2 (cross-family openai), P-4: T-3X SQL trigger refusing session-close UPDATE when no close_records row exists, matching T-18/19/20/27/28/31 precedent.
- (deliberation) C-2 convergence across P-1, P-2, P-4: uniform parse-time atom validator in selvedge/cli.py with structured E_ATOM_* codes raised before any handler write_tx opens.
- (constraint) Constraints property 5 (subtracted at S109, evidence retained): detection without structural feedback loop into prevention creates clean-up service rather than improving past.
- (engine_feedback) EF-S134-1 records S133 closing without close_record row; unguarded close-record + session-close sequencing surfaced as structural-coupling gap requiring substrate defence. [EF-S134-1]

**Effects.**

- bumps_engine engine-v40 to engine-v41 ships T-3X close-record gate and CLI atom validator
- adds_migration Migration 027: T-3X trigger refusing session-close without close_record row
- modifies selvedge/cli.py gains parse-time atom validator raising structured E_ATOM_* codes
- modifies prompts/development.md step 9 names new close-record-required and atom pre-check contract

**Rejected alternatives.**

- **R-1.1.** Operator-side fix only: script-level return-code guard plus prose addendum to prompts/development.md step 9; no substrate defences ship.
  - (no_feedback_loop) Cross-family P-2 independently chose SQL trigger placement; script-level guard is exhortation in code form for non-script callers and does not close the structural feedback loop.
- **R-1.2.** Combined atomic close-record-and-session-close submit kind that performs both writes in one transaction.
  - (redundant_with_existing) T-3X already removes unguarded-sequence risk while preserving composability; combined kind adds CLI surface without adding enforcement that the trigger does not provide.
