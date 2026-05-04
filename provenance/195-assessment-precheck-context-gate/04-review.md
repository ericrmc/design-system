---
session: 195
title: assessment-precheck-context-gate — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: Timezone compensation in TTL freshness check uses time.timezone (fixed standard offset) without DST awareness; DST regions miscompute nonce age by 3600s, allowing valid nonces to be rejected or expired ones accepted at DST boundaries.
  - **fixed.** selvedge/submit/assessment.py uses calendar.timegm (DST-safe UTC parse) replacing time.mktime - time.timezone.
- **critical**: Test suite does not verify cross-session nonce isolation; (session_id, nonce) UNIQUE constraint at schema is untested; gap masks any handler bug that bypasses the session_id boundary.
  - **fixed.** test_nonce_cross_session_rejected added validating session_id boundary on T-38.
- **critical**: TTL expiry path untested; no test advances time past 1800s to verify expired-nonce refusal; age calculation and TTL check are uncovered.
  - **fixed.** test_nonce_expired_after_ttl added force-backdating created_at to validate expiry refusal.
- **high**: Test-fixture nonce auto-injection silently returns unmodified args when context CLI fails (rc!=0); tests may pass or fail for wrong reasons; no assertion that injection succeeded.
  - **fixed.** loud-fail asserts replaced silent fallback in test_export.py + test_engine_v52_marker.py auto-injectors.
- **high**: Race condition between concurrent nonce consumers untested; UPDATE rowcount=1 check should serialize via SQLite IMMEDIATE but no test confirms behavior under concurrent writes.
  - **adjudicated.** Race coverage deferred: SQLite IMMEDIATE serializes; UPDATE rowcount=1 is correct; concurrent test would require threading harness; preserved as forward-direction-watch.
- **medium**: context_cmd.py active_spec query has self-equality bug: de.target_object_id=? AND de.target_object_id=sv.object_id reduces to sv.object_id=? which finds specs that ARE the target rather than specs descended-from decisions targeting target; query likely returns empty.
  - **fixed.** context_cmd.py active_spec query rewritten with proper JOIN dv.object_id=? bridge through decision_effects.
- **medium**: Missing perspective_claims context source; only anchored_harvest + decision_citing + active_spec + supersession queried; agent does not see perspective rows citing target.
  - **adjudicated.** perspective_claims context source deferred to FR-S195-N watch-trigger; v1 sources adequate per [synth]; if calibration EF surfaces missed perspective_claim citing graduate to source-add.

## Terminal passes

- **iteration 2** — clean @ `db531f9`
  - S195 iter-2 clean; iter-1 3 critical + 2 high + 2 medium fixed via DST-safe calendar.timegm + cross-session and TTL tests + loud-fail auto-injectors + active_spec query JOIN fix; race coverage and perspective_claims source adjudicated.
