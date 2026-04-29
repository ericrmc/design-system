---
session: 124
title: stage-validation-no-domain-actor — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Subtract third validation sense clause from methodology line 38 and ship methodology v6 with two senses plus skipped-domain-validation note.

**Kind:** substantive.  **Outcome:** adopt spec_version `methodology-v6`.

**Why.**

- (deliberation) P-2 and P-3 converge on removing the trailing clause per synthesis C-4; the clause as written is undefined and harmful. [P-14-P-2]
- (deliberation) Cross-family critique C-3 from P-2 and P-4 lands against workspace-identity-as-validation-primitive; subtraction is consistent. [P-14-P-4]
- (prior_decision) Selvedge cautions in the kernel itself warn against importing kernel concepts to retrofit-justify a single in-flight arc. [DV-S106-1]

**Effects.**

- creates methodology spec_version v6 with two-sense enumeration plus skipped-domain-validation clarifying note
- supersedes methodology spec_version v5 from S116
- closes_issue OI-S105-1 — kernel coherence restored by deletion of undefined third sense clause

**Rejected alternatives.**

- **R-1.1.** Keep the third sense and define it as the operator's two-tier review pattern per P-1 framing.
  - (inferior_tradeoff) Cross-family critique C-3 surfaced workspace identity is not the validation primitive; two-tier framing fails this test.
- **R-1.2.** Keep the third sense and define it as reference_harness now per P-4 framing as a kernel primitive without pilot evidence.
  - (too_large_for_session) Promoting harness to kernel before any pilot evidence violates subtraction-discipline cautions; pilot must run first.
- **R-1.3.** Defer the line 38 subtraction without acting; let OI-S105-1 stay open with undefined clause pending arc close.
  - (preserves_legacy_path) Leaving an undefined clause preserves the inconsistency the issue surfaced; subtraction is cheaper than further deferral.

## D-2. Commission reference_harness as workspace-experimental substrate kind for disaster-response arc stage 2 onward pilot; not yet a kernel sense.

**Kind:** substantive.  **Outcome:** adopt process_rule `harness-pilot-disaster-response`.

**Why.**

- (deliberation) P-4 supplied the harness primitive with claim_set, stress_protocols, falsification_triggers, expiry as substantive design content. [P-14-P-4]
- (deliberation) P-2 epistemic guardrails (passing harness never upgrades to domain_validated) are baked into the row shape per synthesis C-2. [P-14-P-2]
- (prior_decision) S106 commissioned the arc final phase to surface empirical material on validation-without-domain-actor; harness is the substrate pathway. [DV-S106-1]

**Effects.**

- creates process rule scoping harness as workspace-experimental, not kernel sense, until arc-close evaluation
- opens_issue OI-S124-2 — implementation issue for reference_harness substrate kind

**Rejected alternatives.**

- **R-2.1.** Promote harness to kernel third sense in methodology v7 immediately per full P-4 framing without pilot.
  - (too_large_for_session) Promoting before pilot evidence violates subtraction-discipline; the arc was commissioned to produce that evidence.
- **R-2.2.** Implement two-tier stage_validation per P-1 framing instead of harness.
  - (inferior_tradeoff) Synthesis C-3 cross-family critique against workspace-identity-as-primitive rules out two-tier framing as the kernel mechanism.
- **R-2.3.** Adopt nothing new now per P-2 and P-3 minimalism; no harness substrate kind.
  - (inferior_tradeoff) Without harness rows the arc final phase has no substrate-row evidence to aggregate; markdown EFs decay per S106 reasoning.

## D-3. Defer kernel-promotion decision for reference_harness until disaster-response arc-close evaluation per OI-S124-1 trigger.

**Kind:** procedural.  **Outcome:** defer open_question `harness-as-kernel-third-sense`.

**Why.**

- (deliberation) Synthesis selects S-C path: subtract now, pilot harness, defer kernel-promote until arc-close empirical material is available. [P-14-P-3]
- (prior_decision) DV-S092-1 deferred OI-016 until new signal warrants reopening; the harness pilot at arc close is that named signal. [DV-S092-1]
- (operator_directive) Operator ratified the S-C path (subtract plus pilot plus defer) explicitly during this deliberation.

**Effects.**

- creates deferred decision: kernel-promotion of harness to methodology v7 third sense pending arc close
- opens_issue OI-S124-1 — re-evaluation tracker for harness kernel-promotion at arc close

**Rejected alternatives.**

- **R-3.1.** Promote harness to kernel third sense in methodology v7 in this session without arc evidence.
  - (too_large_for_session) Promoting before pilot violates the subtraction-discipline cautions; arc was commissioned to surface this evidence.
- **R-3.2.** Reject harness as ceremony immediately per P-2 full-rejection minority M-2 without pilot.
  - (preserves_legacy_path) Rejecting before pilot deprives the arc final phase of the substrate-row evidence S106 commissioned it to produce.
