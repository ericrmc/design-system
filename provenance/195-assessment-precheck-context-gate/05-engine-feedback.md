---
session: 195
title: assessment-precheck-context-gate — engine-feedback
generated_by: selvedge export --session
---

# Engine feedback

## EF-S195-1

- **flag.** observation
- **disposition.** addressed-by-DV-S195-1 (codex shape-consult endorsed shape; concretization-not-deliberation per operator-named-mandate)

**codex-shape-consult:** S195 opens kind=coding to repair S194 surfacing-location mistake (relevant_history_anchored in orient is wrong place; agents skim orient under context pressure). Operator-named-mandate at S194-close: wait-for-evidence approach precluded after 194 sessions of evidence that agents avoid the substrate; ship the gate. Codex (gpt-5.5 xhigh) shape-consult per §1.5 confirmed: bootstrap-by-ordering works (S195 own assessment-submit happens before migration applies; gate fires from S196 onward); kind=meta zero-precheck is too broad (meta sessions still modify durable state via FR/EF dispositions and substrate writes); gate ALL session kinds with no admit-zero scoping per operator-named substrate-friction-is-the-point principle; default no-target behavior (undisposed FRs + open HIGH OIs) is correct substrate-presented floor not operator-curated; required atomic-consume-on-submit + sha256-over-rendered-pack-content (not current substrate state to prevent substrate-drift invalidating receipts) + short-but-not-hostile TTL + audit-detail in stored row + missing-nonce-refusal-explains-CLI.

## EF-S195-2

- **flag.** observation
- **disposition.** (none)

**audit-step:** 5 load-bearing interpretive choices, all accepted-implicit under sealed-decision-and-EF exclusions.

1. No multi-perspective deliberation per operator-named-mandate concretizing prior synthesis (§1.5 admissibility): accepted-implicit — covered by EF-S195-1 codex-shape-consult + DV-S195-1 supports + 5 R-1.x alternatives recording rejected variants (R-1.1 keep-orient + R-1.2 wait-for-evidence + R-1.3 operator-curated-targets + R-1.4 kind=meta-admit-zero + R-1.5 hardcoded-S195-exemption).

2. All-kinds-gate (no kind=meta exemption) at T-38: accepted-implicit — covered by codex shape-consult and DV-S195-1 R-1.4 rejection per operator substrate-friction-is-the-point principle.

3. Bootstrap-by-ordering (S195 own assessment-submit before migration applies): accepted-implicit — covered by codex shape-consult endorsement and DV-S195-1 R-1.5 rejection of hardcoded session-id exemption.

4. Default no-target context behavior (substrate-presented floor of undisposed FRs + open HIGH OIs) admitted at v1: accepted-implicit — covered by codex shape-consult and DV-S195-1 supports per operator-named substrate-presented-not-operator-curated principle.

5. context_md TEXT NOT NULL stored on assessment_prechecks row to enable sha256 verification against rendered pack (not current substrate) per codex caution: accepted-implicit — covered by codex shape-consult and DV-S195-1 schema design.

## EF-S195-3

- **flag.** observation
- **disposition.** (none)

**S195 success-signal — relocated context-surfacing from orient-time (S194 location-error) to assessment-time substrate-enforced T-38 refusal per operator-named-mandate at S194-close.** Mechanism: migration 047 creates assessment_prechecks table mirroring decision_prechecks shape (engine-v49 T-33 pattern); handler-side T-38 refuses assessment-submit without precheck_nonce when table exists (bootstrap-by-ordering: S195 own assessment-submit predated migration; gate fires from S196 onward); bin/selvedge context CLI (selvedge/context_cmd.py) walks substrate read-only to gather anchored harvest EFs + decisions citing target + active spec_versions descended-from target + recent supersessions; substrate-presented floor (undisposed FRs + open HIGH OIs) auto-included always (operator-named substrate-not-frictionless-agents-avoid-substrate principle); selvedge/orient.py removed relevant_history_anchored section + 2 tests (S194 location-error reverted). All-kinds-gate (no kind=meta admit-zero) per operator framing that triage-only meta still modifies durable state. Reviewer iter-1 surfaced 3 CRITICAL (timezone DST bug + cross-session test gap + TTL expiry test gap) + 2 HIGH (auto-injector silent skip + race coverage gap) + 2 MEDIUM (active_spec self-equality query bug + missing perspective_claims source); fixed via calendar.timegm DST-safe parse + test_nonce_cross_session_rejected + test_nonce_expired_after_ttl + loud-fail asserts in 3 test files + active_spec JOIN rewrite; race + perspective_claims adjudicated as forward-direction watch-triggers. Test-fixture nonce auto-injection added to test_export.py (_run_cli_in) + test_engine_v52_marker.py (_run) + test_monitor_external.py (_peer_submit) so existing fixtures keep passing without per-call-site changes. pytest 359 pass up 5 from S194 354 (+7 new test_assessment_precheck.py tests + 2 fixture-helper assertions; -2 removed orient-surfacing tests). Operator-quote satisfied: agent at next session-open must run bin/selvedge context (cannot skip; substrate refuses assessment-submit otherwise) and the rendered pack lands in the agent context window via stdout BEFORE deliberation begins.
