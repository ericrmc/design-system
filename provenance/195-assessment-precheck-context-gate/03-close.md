---
session: 195
title: assessment-precheck-context-gate — close
engine_version_at_close: engine-v52
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S195 ships T-38 assessment-precheck gate + bin/selvedge context CLI + migration 047; relocates context-surfacing from orient to assessment-time; removes S194 relevant_history_anchored per operator-named-mandate.

## Engine version

- engine-v52 unchanged (kind=coding feature ship; no engine-version bump warranted at v1).
## What was done

- Migration 047 creates assessment_prechecks table mirroring decision_prechecks (T-33) with role-capability INSERT inline (S194 lesson).
- T-38 in selvedge/submit/assessment.py refuses assessment-submit without precheck_nonce when table exists; atomic UPDATE rowcount; calendar.timegm DST-safe TTL parse.
- selvedge/context_cmd.py + bin/selvedge context CLI: walks anchored harvest + citing decisions + active specs + supersessions; substrate-presented floor.
- selvedge/orient.py removed relevant_history_anchored section (S194 location-error) + 2 tests; engine_feedback_anchors typed-FK graph stays.
- Reviewer iter-1: 3 CRITICAL + 2 HIGH + 2 MEDIUM; fixed timezone DST + cross-session test + TTL test + loud-fail auto-injectors + active_spec JOIN.
## State at close

- T-38 active all-kinds starting S196; bootstrap-by-ordering preserved S195 own assessment-submit before migration applied.
## Open issues

- No HIGH or MEDIUM open issues remain post-close; 4 new EF-S195-* + EF-S194-2 smoke-test residue from prior sessions.
## What the next session should address

- FR-S195-1 watch: race coverage between concurrent nonce consumers; threading test if calibration EF surfaces double-consume.
- FR-S195-2 watch: perspective_claims context source addition if calibration EF surfaces missed perspective citation at deliberation-open.
- FR-S195-3: bin/selvedge context default no-target floor may widen if calibration EF names empty-floor incidents.
- Bare-PROMPT auto-proceed at S196 must run bin/selvedge context after orient before assessment-submit; T-38 carries exact CLI in error.
## Validator at close

- pytest 359 pass up 5 from S194 354; manifest-reconcile + validate.sh run at close.
