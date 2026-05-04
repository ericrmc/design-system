---
session: 198
title: typed-assumption-ledger-primitive — engine-feedback
generated_by: selvedge export --session
---

# Engine feedback

## EF-S198-1

- **flag.** observation
- **disposition.** addressed-by-DV-S198-1 (5 of 6 named edits adopted; 1 rejected per P-1+P-2 convergence; 1 deferred per CF-4)

**codex-shape-consult:** S198 OI-S196-1 typed-assumption-ledger v1; codex (gpt-5.5 xhigh) verdict SHIP-WITH-NAMED-EDITS with 6 edits: (1) drop [P3] as status; omit priority for v1; (2) ship 3 sub-types closed-CHECK no escape hatch; (3) ship assumption-status-update + assumption_status_changes history table at v1 (closure-state authority on the primitive not split with supersession_ledger); (4) history receipts include from_status/to_status/changed_at/origin_decision_object_id/basis_atom_id/note_atom_id; (5) confirm AR-S<wno>-<seq> alias scheme over A-NNN; (6) conflict four-field discipline applies at INSERT AND status-update transitions; sub_type NOT NULL when status=active-with-conflict. Strongest M-1 dissent preserved: insert-only with all transitions via supersession_ledger (compositionally elegant but mixes closure-state with replacement semantics weakening audit readability).

## EF-S198-2

- **flag.** observation
- **disposition.** (none)

**audit-step:** 7 load-bearing interpretive choices, all accepted-implicit under sealed-decision-and-EF exclusions plus 1 lifted to AR-S198-1.

1. OI-S196-1 picked over OI-S196-5 + OI-S196-7 alternatives: accepted-implicit — covered by FR-S197-13 codex C-2-then-C-1 sequencing + DV-S198-1 R-1.5 wait-for-evidence rejection.
2. 6-status enum chosen over 9-value (P-2 + P-3): accepted-implicit — covered by DV-S198-1 R-1.1 + R-1.2 alternatives + synthesis_md + D-1 divergence + M-2/M-3 minorities.
3. 3-sub-type disaster-recovery values chosen over P-2 use-case-discriminator: accepted-implicit — covered by DV-S198-1 D-2 + M-1 minority.
4. Mutable-status-update over P-2 supersession-only over P-3 history-table: accepted-implicit — covered by DV-S198-1 R-1.3 + R-1.4 alternatives + synthesis_md + M-1/M-3 minorities.
5. object_kind=assumption (drop _ledger suffix): accepted-implicit — covered by DV-S198-1 R-1.7 + synthesis_md D-4.
6. Spec amendment in-session per DV-S197-1 precedent (rather than separate session): accepted-implicit — covered by DV-S198-1 effects + SPEC-prompt-development-v4 row.
7. Migration 048 sha-drift repair via direct UPDATE on schema_migrations: lifted-to AR-S198-1 (engine-self lift demo + load-bearing recovery choice not covered by sealed decision).

## EF-S198-3

- **flag.** observation
- **disposition.** (none)

**success-signal:** S198 ships typed-assumption-ledger v1 closing OI-S196-1 by-mechanism in-session per FR-S197-13 codex C-2-then-C-1 sequencing. Pass criteria: (a) substrate-canonical typed primitive sealed at SQL CHECK + handler-side actionable refusal layer; (b) 3-perspective deliberation D-6 sealed with 13 synthesis-points + 4 counterfactuals; (c) 10 chain-walks completed at decision-record submit (T-32); (d) closes_issue OI-S196-1 dispatched in-band; (e) spec amendment shipped in-session as SPEC-prompt-development-v4; (f) reviewer iter-2 clean (1 critical RF-75 fixed exposing handler bug; 1 high RF-76 adjudicated per S197 precedent; 5 medium/low addressed); (g) pytest 395 ok up 20 from S197 375; (h) bias-toward-build-now per EF-S196-2 honored; (i) codex-shape-consult discipline preserved via EF-S198-1 with 5/6 named edits adopted (1 rejected per P-1+P-2 convergence, 1 deferred per CF-4 out-of-scope); (j) AR-S198-1 lifted in-session demonstrates engine-self consumer of the new primitive — §8.5 referential gap closed.
