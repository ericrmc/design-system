---
session: 201
title: closure-shape-enum-on-assumption-ledger — deliberation
generated_by: selvedge export
---

# Deliberation

## D-8 — closure-shape enum on assumption_ledger: 5 canonical shapes + status-conditional CHECK

sealed_at: 2026-05-04T19:56:46.472Z

### P-1 (anthropic)

### P-2 (openai)

### P-3 (anthropic)

### Synthesis

**Synthesis.** Adopt P-1 + P-2 convergent ship-shape: closure_shape TEXT NULL on assumption_ledger only, with closed 5-value CHECK and four status-shape coupling CHECKs. P-3 spec-only stance is rejected as rejection-basis=operator_override per EF-S196-2 (graduation-discipline does not authorize watch-FR-deferral or vocabulary-only deferral for engine primitives evidenced by operator-curated multi-session disaster-recovery synthesis). P-3 minority preserved as M-1 watch-trigger: if calibration-EFs across N>=3 future sessions surface containment-resolved-vs-convergence collapse, the next session opens a gate-promotion OI for shape-merge migration. Five canonical values land closed (no escape hatch) per DV-S020-5 + M-3 S194 schema-correctness threshold; status='closed' requires closure_shape NOT NULL (no anonymous closure); status IN (unverified/assumed/active-with-conflict) requires closure_shape IS NULL (no premature labelling); status='superseded' allows NULL or 'supersession' only (P-1 + P-2 convergence on superseded narrowing); status='invalidated' forbids closure_shape (P-2 named invalidation as ontologically distinct). Handler accepts closure_shape on initial assumption submit only when payload status='closed' (rare init path), and on assumption-status-update with status-aware required/forbidden checks. T-15-CALIBRATED rebuild required: status-coupling CHECKs span multiple columns and SQLite ALTER ADD COLUMN cannot land cross-column CHECKs cleanly. Methodology spec-only ship (P-3 stance) preserved as M-2 minority forward-direction if substrate-column never sees a query-by-shape read pattern across N>=5 sessions. P-2 codex shape-consult adopted whole, including 5 named edits, with one P-1 tightening: handler-side actionable refusal NAMING the offending field before SQL CHECK fires (parity with sub_type four-field discipline at migration 049).

**Convergence (C-1 through C-5).** C-1: closure_shape on assumption_ledger only at v1 (P-1 + P-2). C-2: 5-value closed CHECK with no escape hatch (P-1 + P-2). C-3: status='closed' requires closure_shape NOT NULL (P-1 + P-2). C-4: status IN (unverified/assumed/active-with-conflict) requires closure_shape IS NULL (P-1 + P-2). C-5: status='superseded' narrowing to NULL or 'supersession' only; status='invalidated' forbids any shape (P-1 + P-2 convergence rejecting semantic-stretching).

**Divergence (D-1, D-2).** D-1: ship-substrate (P-1 + P-2) vs spec-only-ship (P-3). Resolved by EF-S196-2 binding precluding P-3. D-2: handler refuses-before-CHECK-fires (P-1) vs CHECK-as-canonical-refusal (P-2 implicit). Resolved by adopting P-1 tightening for actionable error messages.

**Minority preserved (M-1, M-2).** M-1 P-3 5-shape-overbreadth-watch: if calibration-EFs name containment-resolved-vs-convergence collapse OR supersession-double-encoding across N>=3 sessions, gate-promotion OI for shape-merge. M-2 P-3 spec-only-as-substrate-canonical: if zero query-by-shape read pattern surfaces across N>=5 sessions, retrospective calibration-EF candidate to remove the column and revert to spec-only vocabulary.

### Synthesis points

- **convergence C-1.** closure_shape lands on assumption_ledger only at v1; not on issues, not on close_records.
- **convergence C-2.** 5-value closed CHECK with no TEXT escape hatch and no DEFAULT; explicit-or-NULL only.
- **convergence C-3.** status=closed requires closure_shape NOT NULL; no anonymous closure.
- **convergence C-4.** status in (unverified, assumed, active-with-conflict) requires closure_shape IS NULL; no premature labelling.
- **convergence C-5.** status=superseded allows NULL or supersession only; status=invalidated forbids closure_shape entirely.
- **divergence D-1.** ship-substrate (P-1+P-2) vs spec-only-ship (P-3); resolved by EF-S196-2 binding precluding P-3.
- **divergence D-2.** handler-refuses-before-CHECK-fires (P-1 actionable error) vs CHECK-as-canonical-refusal (P-2 implicit); P-1 tightening adopted.
- **minority M-1.** P-3 5-shape overbreadth watch: containment-resolved-vs-convergence collapse OR supersession double-encoding across N>=3 sessions opens gate-promotion OI for shape-merge.
- **minority M-2.** P-3 spec-only-as-substrate-canonical: zero query-by-shape read pattern across N>=5 sessions opens retrospective calibration-EF to remove the column.
