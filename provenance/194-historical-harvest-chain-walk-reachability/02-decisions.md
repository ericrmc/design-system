---
session: 194
title: historical-harvest-chain-walk-reachability — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S194 ships option C engine_feedback_anchors typed-FK + option E orient surfacing extension at v1 with in-session backfill of 22 EF-S193-* harvest rows; rejects D as premature per DV-S190-2.

**Kind:** schema_migration.  **Outcome:** adopt migration `045-engine-feedback-anchors`.

**Why.**

- (deliberation) D-S194-1 4-perspective sealed deliberation converges on option C primary + option E concurrent at v1 + reject D + 22-row in-session backfill; M-1 + M-2 + M-3 minorities preserved. [P-4-P-1]
- (engine_feedback) EF-S194-1 codex shape-consult endorsed C + light E + single-arc kind=coding + in-session backfill per motivating-failure-case framing; gpt-5.5 xhigh review. [EF-S194-1]
- (prior_decision) DV-S081-1 substrate-loss-defense-v1 substrate canonical markdown is generated export binds; FTS5-on-body_md violates the framing; FK-only at v1 honors typed-substrate contract. [DV-S081-1]
- (prior_decision) DV-S189-1 markdown-only-recovery binds: pre-S180 substrate continuity broken at wipe; zero-anchor-acceptable for backfill rows resolving to no current-substrate alias; no synthetic alias creation. [DV-S189-1]

**Effects.**

- adds_migration 045-engine-feedback-anchors typed-FK table
- creates process_rule: anchor-graph + orient surfacing v1
- modifies engine_feedback submit: harvest-prefixed requires anchors

**Rejected alternatives.**

- **R-1.1.** Ship option A engine_feedback_topics with free-form atom topic strings as primary discovery mechanism.
  - (inferior_tradeoff) P-1 + P-3 reject as untyped pseudo-links reachable only via string-match heuristics; ungrounded categorical labels drift and synonym-fragment.
- **R-1.2.** Ship option B FTS5 fulltext virtual table on engine_feedback.body_md as primary discovery mechanism.
  - (violates_gate) FTS5-on-body_md treats prose surface as canonical-queryable inverting DV-S081-1 markdown-as-generated-export; FTS5 is search not graph reachability.
- **R-1.3.** Ship option D mandatory T-NN deliberation-open precheck refusing without history-query receipt at v1.
  - (violates_gate) DV-S190-2 graduation-discipline binds: substrate-receipt gates wait until calibration-EFs prove necessity; operator did NOT preclude DV-S190-2 for S194; CF-1 deferred to FR-S194-1 watch-trigger.
- **R-1.4.** Defer 22-row EF-S193-* backfill to S195 separate session; ship migration only at S194.
  - (inferior_tradeoff) Codex shape-consult motivating-failure-case framing: leaving 22 unmoored rows after shipping the mechanism makes S194 incomplete; orient surfacing on empty table trains agents to ignore section.
- **R-1.5.** Ship option C alone at v1 (typed anchor graph + walker extension) without option E orient surfacing.
  - (inferior_tradeoff) Operator-named purpose putting relevant knowledge in agent context; [synth] concurrent-ship-load-bearing: anchor-FK without surfacing leaves agents blind per P-2 M-1; typed graph unused without read-side affordance.
