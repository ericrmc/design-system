---
session: 121
title: fix-s119-test-regressions — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high** against `DV-S121-1`: Reviewer claimed OI-S121-1 did not exist before decision-record submission, predicting T-31 refusal.
  - **adjudicated.** Incorrect — OI-S121-1 was registered first via submit issue (issue_id 55, status=open) before DV-S121-1 was submitted; T-31 enforcement passed. Substrate confirms ordering.
- **medium** against `DV-S121-1`: tools/validate.sh wrote pytest log to a hardcoded /tmp path; concurrent validator runs would race and overwrite the log.
  - **fixed.** Fixed: switched to mktemp -t selvedge-pytest.XXXXXX with trap-on-EXIT cleanup. Per-process isolation, no shared file.
- **high** against `DV-S121-1`: Coverage erosion: 8 deleted harvest-ef tests (dry-run, idempotency, since-session, unparseable filename, missing dir, prose-flag, db-path override, ef listing) now untested; tracked by OI-S121-1.
  - **adjudicated.** Intentional per DV-S121-1 R-1.2; OI-S121-1 carries the substrate-direct rewrite intent.
## Iteration 2

- **low** against `DV-S121-1`: Trap-on-EXIT cleanup removes the pytest log before post-mortem; tail -20 inline output is the only surviving artifact on failure.
  - **adjudicated.** Acceptable tradeoff for race safety; tail -20 inline output already covers diagnosis.

## Terminal passes

- **iteration 2** — clean @ `ef8c0c976bad`
  - Iter-2 reviewer confirmed mktemp+trap fix to medium race finding; only LOW (log-unavailable-post-exit) adjudicated.
