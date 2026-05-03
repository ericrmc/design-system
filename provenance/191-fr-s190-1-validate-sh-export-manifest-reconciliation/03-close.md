---
session: 191
title: fr-s190-1-validate-sh-export-manifest-reconciliation — close
engine_version_at_close: engine-v52
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S191 ships FR-S190-1 first-step of sealed DV-S190-2 D-B FR-D: tools/manifest_reconcile.sh plus validate.sh extension plus 13 pytest cases.

## Engine version

- engine-v52 unchanged (no engine bump; bash extension plus pytest only).
## What was done

- tools/manifest_reconcile.sh standalone script with pass 1 manifest-row integrity (all kinds incl NULL session_no) plus pass 2 L5 orphan discovery scoped to post-adoption sessions.
- tools/validate.sh wires bash tools/manifest_reconcile.sh as a step between substrate validate --precommit and pytest.
- state/tests/test_manifest_reconcile.py 13 cases: clean pass, missing on disk, sha mismatch, L5 orphan, pre-adoption skip, NULL session_no, absolute, traversal, missing DB, slug regression.
- DV-S191-1 records the ship plus 3 alternatives (R-1.1 ship FR-E now, R-1.2 fold FR-S190-18 harness, R-1.3 inline validate.sh block) with chain-walks against DV-S190-2 plus DV-S188-1 plus EF-S191-1.
- Reviewer iter-1 surfaced 2 HIGH plus 2 MEDIUM (45 SQL inject, 46 slug no CHECK, 53 error suppression, 54 parameterized discipline) all fixed by pass-2 grep-qxF restructure plus bash slug+wno guards; iter-2 clean.
## State at close

- kind=coding closed clean; review-loop converged iter-2 with one adjudicated finding 57 confirming iter-1 closures sound and no new issues introduced.
## Open issues

- Zero substantive open issues; FR-S188-14 harness lifecycle plus FR-S187-15 cross-session anchoring remain pending and tracked as separate non-blocking FRs.
## What the next session should address

- FR-S190-3 refuse-substrate-md.py substrate-side telemetry plus FR-S190-4 stderr imperative-first tweak both small tractable D-A follow-ups admissible under operator-absent §1.5 priority-4.
- FR-E substrate-receipt graduation stays deferred per DV-S191-1 R-1.1 until validate.sh surfaces stale-L5-on-commit warnings across N closes per FR-S190-17 watch-trigger.
- If operator-present, harness lifecycle FR-S188-14 plus cross-session anchoring FR-S187-15 are next concrete coding tasks blocked by L4 anchor design need.
## Validator at close

- validate.sh 18 ok / 0 fail; pytest 347 passed (was 334 at S190); manifest-reconcile 36 rows ok / 0 divergent against live workspace.
