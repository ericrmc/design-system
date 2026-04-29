---
session: 121
title: fix-s119-test-regressions — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Restore green pytest suite (test_migrate import fix; delete obsolete test_monitor_external md-glob tests; OI-S121-1 tracks substrate-direct rewrite); wire pytest into tools/validate.sh.

**Kind:** substantive.  **Outcome:** adopt process_rule `test-suite-close-gate`.

**Why.**

- (operator_directive) Operator surfaced that the pytest suite was red and the close gate did not exercise it; ratified opening S121 to fix.
- (prior_decision) S119 modular-cli refactor moved _t15_violations from selvedge.cli to selvedge.migrations without updating the test imports.
- (prior_decision) S110 substrate-direct harvest-ef rewrite invalidated the md-glob tests in test_monitor_external; never updated.
- (constraint) tools/validate.sh now invokes uv run pytest as a final check; future test regressions surface at validator time.

**Effects.**

- modifies state/tests/test_migrate.py imports _t15_violations from selvedge.migrations (was selvedge.cli)
- modifies state/tests/test_monitor_external.py: status tests updated to ef_rows; 8 md-glob tests deleted
- modifies tools/validate.sh adds Pytest suite section invoking uv run pytest --no-header
- opens_issue OI-S121-1 — OI-S121-1 tracks the substrate-direct test rewrite for harvest-ef coverage

**Rejected alternatives.**

- **R-1.1.** Mark obsolete test_monitor_external tests as pytest.skip rather than deleting them, so the rewrite intent stays visible.
  - (preserves_legacy_path) Skipped tests rot; OI-S121-1 carries the rewrite intent more durably than skipped asserts drifting further from the implementation.
- **R-1.2.** Rewrite test_monitor_external substrate-direct tests in-session rather than deferring to OI-S121-1.
  - (too_large_for_session) Substantive fixture work (seeding peer engine_feedback rows via _peer_submit and ledger semantics) is its own session.
- **R-1.3.** Skip the validate.sh pytest integration; document pytest as a developer-discipline step instead.
  - (violates_gate) Documented-only discipline already failed twice (S119 and S120 reviewers both missed pytest); the close gate is the right place to enforce.
