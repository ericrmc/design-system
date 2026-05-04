---
session: 197
title: typed-supersession-ledger-primitive — engine-feedback
generated_by: selvedge export --session
---

# Engine feedback

## EF-S197-1

- **flag.** observation
- **disposition.** addressed-by-DV-S197-1 (codex shape-consult SHIP-WITH-NAMED-EDITS verdict integrated; 6 named edits all adopted into v1 design + spec amendment)

**EF-S197-1 codex (gpt-5.5 xhigh) shape-consult on S197 OI-S196-2 typed-supersession-ledger primitive.** Reviewed S196 close named C-2 ship-first per biggest-schema-gap; bias-toward-build-now framing with EF-S196-2 bounded-scope binding precluding watch-FR deferral.

**Verdict: SHIP-WITH-NAMED-EDITS.** Six edits accepted into design path:

(1) Polymorphism shape: source_object_id + target_object_id FK to objects.alias graph; NO source_kind/target_kind enum columns; kind derived from referenced object. Forward-compatible with C-1 typed-assumption-ledger landing later.

(2) Relation enum: 7 values {supersedes, replaces, refines, deprecates, narrows, contradicts, withdraws}. Closed CHECK constraint. Each value documented in spec amendment.

(3) Event-origin handling: OMIT origin column at v1; let C-4 add origin_event_id when external_events table exists. Avoid forward-FK schema debt; nullable TEXT origin_descriptor risks becoming untyped event sink.

(4) decision_effects.supersedes disposition: supersession_ledger becomes primary channel; migrate the 1 historical row if reconstructible OR seal-leave with migration note; keep effect_kind enum value temporarily-deprecated (not hard-removed) to avoid breaking historical replay.

(5) Object-registration: supersession_ledger rows MUST register as first-class objects (alias SL-S<wno>-<seq>) so they participate in objects.alias graph and can be cited + chain-walked.

(6) Spec amendment in-session, NOT split to OI-S196-7: new submit kind changes active substrate interface and should ship with its governing prompt-development clause.

**Perspectives recommendation: 3** (schema-minimality + backcompat-and-objects-graph + adversarial failure-modes). Design space bounded but durable schema semantics warrant adversarial framing per S194 4-perspective precedent for engine_feedback_anchors.

**Sequencing-advice:** migration + object-registration first, then handler, then backcompat for legacy supersedes row, then tests, then adversarial Explore review, then prompt-development v3 spec amendment + DV-S197-1 before close.

**Named risks:** (a) C-1 forward-compat hinges on object-FK polymorphism; (b) decision_effects.supersedes second-channel risk unless handler routes new submissions only to supersession_ledger; (c) relation_kind overbreadth risk if v1 admits relations beyond replacement/narrowing/contradiction/withdrawal/deprecation; (d) chain-walk T-32 integration depends on object-registration; (e) origin_descriptor sink risk argues for omission.

Cites OI-S196-2 + EF-S196-1 (S196 prior consult) + EF-S196-2 bounded-scope binding.

## EF-S197-2

- **flag.** observation
- **disposition.** (none)

**EF-S197-2 audit-step S197 supersession-ledger v1 ship.** Records load-bearing interpretive choices made during the session; all under sealed-decision-and-EF exclusions per S195/S196 audit-step pattern.

**Choices recorded:**

(1) Picked OI-S196-2 over OI-S196-1 + OI-S196-5 from priority-1 HIGH queue. Covered by S196 close-record naming OI-S196-2 ship-first per codex EF-S196-1 sequencing + FR-S196-12 sealed marker.

(2) 5-value relation enum (P-1 stance) over P-3 4-value-tight + codex 7-value-starting-set. Covered by DV-S197-1 R-1.1 + R-1.2 sealed rejections; D-S197-1 D-1 synthesis-point preserves P-3 minority + watch-trigger.

(3) Soft-deprecation of decision_effects.supersedes (P-1+P-2 stance) over P-3 hard-cutover. Covered by DV-S197-1 R-1.3 sealed rejection + D-S197-1 D-3 synthesis + M-1 minority preserved as dead-channel watch-trigger.

(4) Object-registration of ledger rows via SL-S<wno>-<seq> (P-2 stance) over P-3 defer-until-citation. Covered by DV-S197-1 R-1.5 sealed rejection + D-S197-1 D-2 synthesis.

(5) Spec amendment in-session per codex sequencing-advice (not split to OI-S196-7). Covered by EF-S197-1 sealed shape-consult naming new-submit-kind-changes-active-substrate-interface as load-bearing binding.

(6) Ship-now vs DV-S190-2-defer. Covered by DV-S197-1 R-1.4 sealed rejection citing EF-S196-2 bounded-scope binding (21-session arc + retrospective sufficient evidence).

(7) 3-perspective convening (not 4 like S194 engine_feedback_anchors). Covered by EF-S197-1 codex recommendation citing bounded design space + 3-perspective sufficiency for adversarial framing.

(8) Conditional backfill via WHERE EXISTS pattern (vs hardcoded INSERT). Covered by reviewer F-71 + iter-1 fix; preserves migration determinism on fresh-init test substrates per clean_substrate fixture compatibility.

**Zero novel interpretive choices outside sealed substrate.** All 8 choices trace to either codex shape-consult (EF-S197-1), sealed decision-record alternatives (DV-S197-1 R-1.1 through R-1.6), sealed synthesis-points (D-S197-1 D-1/D-2/D-3 + M-1/M-2/M-3), or operator-named-mandate (S196 close + EF-S196-2 bounded-scope binding). Audit-step records no triage-author-only judgments outside these chains.

## EF-S197-3

- **flag.** observation
- **disposition.** (none)

**EF-S197-3 success-signal S197 supersession-ledger v1 ship.** Records pass-criteria met against operator-state at session-open (bare-PROMPT.md auto-proceed selecting OI-S196-2 typed-supersession-ledger ship-first per S196 close-record).

**Pass criteria met:**

(a) Substrate-canonical typed primitive shipped: migration 048 creates supersession_ledger table with objects-FK polymorphism + 5-value relation enum + UNIQUE(source,target,relation_kind) + CHECK source!=target + role_write_capabilities INSERT inline (S194 split-out lesson honored). Engine version bumped v52->v53. PASS.

(b) Handler dispatch shipped: selvedge/submit/supersession.py with FK alias-resolution + atom-pin reason + object-registration via SL-S<wno>-<seq>; registered as submit kind in cli.py. PASS.

(c) DV-S197-1 sealed with 9 chain-walks all completed depth_capped: P-5-P-1 + P-5-P-2 + P-5-P-3 perspectives + EF-S197-1 codex consult + EF-S196-2 + EF-S196-1 + DV-S081-1 + DV-S189-1 + OI-S196-2 closes_issue. PASS.

(d) closes_issue OI-S196-2 by-mechanism via DV-S197-1 effects array; target resolved via _submit_issue_disposition handler dispatch transitioning OI-S196-2 status to resolved. PASS.

(e) prompt-development v3 spec amendment shipped in-session per codex EF-S197-1 sequencing-advice (not split to OI-S196-7); body amended with supersession-ledger submit kind documentation + 5-value relation enum semantics + soft-deprecation clause + objects-FK polymorphism note. PASS.

(f) Reviewer iter-1 surfaced 8 findings (2 HIGH 3 MEDIUM 3 LOW) all dispositioned: F-67 alias-collision adjudicated forward-direction per IMMEDIATE serialization + F-68 soft-deprecation routing fixed via spec-v3 amendment + F-69 back-pointer-index adjudicated low-volume + F-70 concurrent-test-gap adjudicated forward-direction-FR + F-71 spec-amendment-not-yet fixed + F-72 atom-length-doc fixed in handler + F-73 object_kind-test adjudicated polymorphism-by-design + F-74 self-supersession-redundancy adjudicated defense-in-depth. Iter-2 review-pass clean. PASS.

(g) Pytest 375 pass up 16 from S196 359 net (+16 new test_supersession_ledger tests). PASS.

(h) EF-S196-2 bounded-scope binding honored: bias-toward-build-now applied; zero watch-FR deferral; DV-S197-1 R-1.4 explicit rejection of DV-S190-2 graduation-discipline as deferral basis citing EF-S196-2 as bounding interpretation per FR-S196-15 binding. PASS.

(i) Codex shape-consult discipline preserved per FR-S196-16 + S193/S194/S195/S196 precedent; EF-S197-1 records SHIP-WITH-NAMED-EDITS verdict + 6 named edits all adopted into final substrate state. PASS.

**Headline outcome.** Engine now has a typed cross-artefact supersession primitive composing with chain_walks T-32 via objects.alias graph; the 196-session decision_effects.supersedes gap (1 row across 196 sessions) is closed by the typed primitive plus soft-deprecation discipline. The legacy SPEC-prompt-development v1->v2 supersession is migrated as SL-S186-1 typed row preserving historical chain-walk reachability.
