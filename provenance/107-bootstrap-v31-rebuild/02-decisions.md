---
session: 107
title: bootstrap-v31-rebuild — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Archive v7-era selvedge-disaster-response workspace into archive/v7-trial-2026-04-24-disaster-response per S106 D-4 disposition

**Kind:** procedural.  **Outcome:** adopt process_rule `v7-disaster-response-archive`.

**Why.**

- (prior_decision) S106 DV-S106-4 ratified hard-reset disposition with archive-as-source-material discipline. [DV-S106-4]

**Effects.**

- closes_issue OI-S106-3 — Archive v7 disaster-response workspace

## D-2. Implement tools/bootstrap-external-workspace.sh per DV-S106-2 minimal scope; iter-2 review clean after fixing injection vector and adding partial-failure cleanup trap.

**Kind:** procedural.  **Outcome:** adopt process_rule `bootstrap-external-workspace-v31`.

**Why.**

- (prior_decision) S106 DV-S106-2 ratified the file-set scope and exclusion list; this decision records the implementation that realises it. [DV-S106-2]
- (review_finding) Iter 1 surfaced critical SQL injection on workspace-id arg; iter 2 verified fix via kebab-case validation matching the slug check.
- (review_finding) Iter 1 surfaced medium idempotency gap on partial-failure; iter 2 verified trap-on-EXIT cleanup confirmed by happy-path retention plus injection-refusal target-absence test.

**Effects.**

- creates tools/bootstrap-external-workspace.sh (engine-v31 minimal bootstrap)
- closes_issue OI-S106-1 — Bootstrap rebuild for engine-v31 per S106 D-2
