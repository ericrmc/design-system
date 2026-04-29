---
session: 125
title: reference-harness-substrate-kind — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Ship reference_harness substrate kind (engine-v37) closing OI-S124-2 with workspace-experimental scope and P-2 guardrails.

**Kind:** schema_migration.  **Outcome:** adopt migration `023+024+025-reference-harness`.

**Why.**

- (prior_decision) DV-S124-2 commissioned reference_harness as workspace-experimental substrate kind for disaster-response stage-2-onward pilot. [DV-S124-2]
- (prior_decision) Methodology v6 keeps kernel at two validation senses; substrate kind is not yet third sense per S124 S-C synthesis. [DV-S124-1]
- (review_finding) T-30 review iteration 3 reports clean after migrations 024 and 025 close all medium-or-higher findings.

**Effects.**

- adds_migration 023 adds reference_harnesses + 6 sub-tables + T-32/T-33/T-34
- adds_migration 024 adds assumptions table + T-32 UPDATE/DELETE + T-36 + T-37 + widened T-34
- adds_migration 025 strengthens T-36 lifecycle-column rule and adds T-38 parent DELETE refusal
- creates 10 harness-* submit handlers in selvedge/submit/harness.py
- bumps_engine engine-v34 to engine-v37
- closes_issue OI-S124-2 — OI-S124-2 reference_harness substrate kind
- opens_issue OI-S125-1 — alias not in objects deferred
- opens_issue OI-S125-2 — expiry-window enforcement deferred to expire CLI
- opens_issue OI-S125-3 — auto-OI on broken load-bearing claim deferred
- opens_issue OI-S125-4 — replay-on-same-harness re-evaluation pending pilot

**Rejected alternatives.**

- **R-1.1.** Ship bin/selvedge harness CLI verbs (create/replay/stress/expire/triggers/summarize) in the same session per P-4 cli_surface.
  - (too_large_for_session) Substrate kind plus 3-iteration T-30 review already produced three migrations; CLI sugar can wait for pilot ergonomics.
- **R-1.2.** Promote reference_harness to methodology v7 third validation sense in this session per S124 P-4 framing.
  - (violates_gate) DV-S124-3 deferred kernel-promotion to arc close per OI-S124-1; promoting now violates the deferred-decision gate.
- **R-1.3.** Admit new triggers and additional fires on the same harness post-reopen rather than replay-creates-new-harness.
  - (inferior_tradeoff) Immutability after seal is cleaner; replay-creates-new-harness preserves it; OI-S125-4 reopens if pilot needs alternative.
