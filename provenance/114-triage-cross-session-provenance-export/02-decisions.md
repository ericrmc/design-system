---
session: 114
title: triage-cross-session-provenance-export — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt anchor-only markdown projection as cross-session provenance v1; defer workspace-wide mode and --graph HTML pending recurring need.

**Kind:** substantive.  **Outcome:** adopt open_question `cross-session-provenance-export-shape`.

**Why.**

- (engine_feedback) EF-S110-7 reframes cross-session provenance as a delivery requirement when stakeholders ask how a decision was reached. [EF-S110-7]
- (deliberation) Cross-family deliberation converged on markdown-only first release with --graph HTML deferred and synthesised prose refused.
- (prior_decision) DV-S113-1 backfilled decision_effects/supports target FKs so cross-session joins are now reachable from the substrate. [DV-S113-1]
- (deliberation) P-2 boundary-discipline concern about transitive workspace closure took priority over P-1 workspace-mode default.

**Effects.**

- creates scope-spec for cross-session anchor-trace export: bin/selvedge export --provenance --anchor <alias>
- opens_issue OI-S114-1 implementation of anchor-mode cross-session provenance export

**Rejected alternatives.**

- **R-1.1.** Ship anchor mode and workspace mode together as a single generator unioned across all sessions per P-1.
  - (inferior_tradeoff) Workspace mode is a surface whose appetite grows with use; defer until composing several anchor traces proves insufficient.
- **R-1.2.** Ship `--graph` HTML in first release per the original EF-S110-7 remedy proposal.
  - (inferior_tradeoff) No proven need yet; markdown is sufficient first answer; HTML adds render dependency without load-bearing capability.
- **R-1.3.** Decline to ship cross-session export, treating per-session export plus bin/selvedge query as sufficient.
  - (inferior_tradeoff) Substrate-canonical-rows pay-off is unrealised when stakeholders cannot read cross-session provenance without raw SQL.
