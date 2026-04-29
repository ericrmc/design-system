---
session: 120
title: submit-dry-run — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Add --dry-run to bin/selvedge submit via ROLLBACK-instead-of-COMMIT in write_tx, with FS side-effect suppression via contextvar.

**Kind:** substantive.  **Outcome:** adopt process_rule `submit-dry-run`.

**Why.**

- (engine_feedback) EF-S118-1 named smoke-testing decision-record handlers leaking rows as the friction; --dry-run is the named remedy. [EF-S118-1]
- (operator_directive) Operator ratified FR-S119-10 to land FR-S118-10 this session.
- (prior_decision) S119 modular cli surface keeps the change scoped to one argparse arg, one write_tx kwarg, one contextvar.
- (constraint) Substrate has no DEFERRABLE constraints; statement-time triggers fire during fn(conn) so ROLLBACK at the end preserves refusal semantics.

**Effects.**

- modifies selvedge/connection.py write_tx accepts dry_run=False kwarg; ROLLBACK on success when set
- modifies selvedge/cli.py p_submit gains --dry-run flag (dest=dry_run)
- modifies selvedge/submit/__init__.py cmd_submit threads dry_run via contextvar and emits dry_run:true in envelope
- modifies selvedge/submit/_helpers.py adds _dry_run_var contextvar and is_dry_run() helper
- modifies selvedge/submit/spec.py _submit_spec_version suppresses body-file write when is_dry_run()

**Rejected alternatives.**

- **R-1.1.** Thread dry_run as an explicit kwarg through every submit handler signature instead of via contextvar.
  - (too_large_for_session) Would touch ~25 handler signatures for a flag only _submit_spec_version actually consults; contextvar stays scoped to the one reader.
- **R-1.2.** Implement dry-run as a separate sandboxed SQLite copy populated from migrations on each invocation.
  - (inferior_tradeoff) Schema replication churn and slower per-call cost for no gain over BEGIN IMMEDIATE/ROLLBACK on the live connection, which is already isolated.
- **R-1.3.** Defer --dry-run; keep the S118 manual DELETE pattern when smoke-testing handlers.
  - (violates_gate) EF-S118-1 named the friction explicitly; FR-S119-10 was ratified to land it; deferral leaves provenance pollution risk in place.
