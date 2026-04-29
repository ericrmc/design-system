---
session: 121
title: fix-s119-test-regressions — assessment
engine_version_at_open: engine-v34
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S119 modular-cli refactor moved symbols out of selvedge.cli; pytest suite (state/tests, 161 tests) has 17 stale-import regressions that S119+S120 reviewers missed because tools/validate.sh never invokes pytest.

## Agenda

1. Diagnose all 17 failures in test_migrate.py (7) and test_monitor_external.py (10): identify each stale import and locate the new module home.
2. Fix the test imports so the suite passes against the post-S119 module layout.
3. Decide whether tools/validate.sh should run pytest (close-gate integration) or whether pytest stays a developer-discipline step; record either way as a decision-record.
4. Open OI tracking the gap (validate.sh does not exercise pytest, so test regressions can ship under reviewer clean verdicts) and close it via this session if validate.sh is updated.
5. Run the coding review loop with a distinct reviewer subagent until pytest is green and findings clean.
