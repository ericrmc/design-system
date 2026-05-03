---
session: 190
title: gate-promotion-deliberations — engine-feedback
generated_by: selvedge export --session
---

# Engine feedback

## EF-S190-1

- **flag.** observation
- **disposition.** (none)

**S190 success-signal — dual-deliberation arc landed substrate-receipts validating gate-promotion discipline as the engine-self-application of DV-S152-1 + DV-S109-1 + DV-S176-1 lineage.** Two methodology-changing deliberations (D-A OI-S083-1 reminder pathway, D-B L5 close-time substrate-filesystem divergence gate) bundled in one operator-present session under kind=spec_only. 8 perspective subagents + 2 capture subagents dispatched in parallel; codex CLI worked end-to-end for both cross-family P-2 slots; both seals admitted T-36 counterfactuals. D-A shipped close-by-mechanism (3-of-4 ship-nothing convergence, M-1 P-1 ship-now preserved); D-B sealed two-step graduation design (validate.sh smaller-first, substrate-receipt as graduation target, M-1 P-3 ship-nothing preserved). Cross-family signal (P-2 codex independently arriving at substrate-receipt for D-B) treated as load-bearing per [synth] in D-B synthesis; counterfactual addressed-in-synthesis explicitly addresses skip-validate.sh-route alternative. 13 chain-walks recorded across both DVs. 4 FRs disposed. Pytest 334 pass unchanged from S189.

## EF-S190-2

- **flag.** observation
- **disposition.** (none)

**audit-step:** 4 load-bearing interpretive choices.

1. Choosing kind=spec_only over kind=coding at session-open: accepted-implicit — exclusion: micro-decision-adjacent under operator-presence; the alternative kind=coding would have admitted ship of validate.sh extension OR substrate-receipt migration in-session but neither deliberation outcome warranted irreversible kind-immutability commitment before perspectives returned; T-29 reversibility cost was higher than the deferral cost.

2. D-A synthesis routing P-2 substrate-detectability observation as deferred-FR rather than primary OI resolution: addressed-in-synthesis via counterfactual_id=4 (deliberation_id=2 seq=1) disposition addressed-in-synthesis citing C-5 + [synth] substrate-detectability-gap; would change synthesis if adopted by reframing OI question.

3. D-B synthesis adopting two-step graduation (validate.sh first, substrate-receipt as graduation target) rather than P-1+P-2 substrate-receipt-now per cross-family + architect convergence: addressed-in-synthesis via counterfactual_id=5 (deliberation_id=3 seq=1) disposition addressed-in-synthesis routing through validate.sh-first because P-3+P-4 transactional-coupling concerns warrant intermediate measurement.

4. Bundling D-A + D-B in one session vs splitting: accepted-implicit — exclusion: operator-directed at session-open (Track A bundled the substrate-side gate per operator confirmation); not synthesizer-interpretive; included for audit completeness.

## EF-S190-3

- **flag.** calibration
- **disposition.** (none)

**S190 close-record bookkeeping slip — initial submit ran on stale /tmp/close-record.json carrying S189 text.** Mechanism: prior session left the file at /tmp; my Write tool refused (file pre-existed without prior Read) and I did not notice; the subsequent Bash submit ran with the OLD content. The submit succeeded (atom validation passed; text was structurally well-formed for S189) producing close_record_id=11 with C-S190 alias carrying S189 narrative. Recovery: operator authorised destructive repair after backup; sqlite3 DELETE removed close_records row 11 + 11 close_state_items + objects.alias C-S190 inside one transaction (PRAGMA foreign_keys=ON; FK clean after DELETE-children-first ordering); resubmit landed correctly. Lesson: /tmp paths persist across sessions; use session-scoped filenames OR Read-before-Write discipline. Remedy options: (a) rename payload tmp files with workspace_session_no suffix at session-open, (b) prefer Write to a fresh path under tmp/<wno>/, (c) discipline-only — Read existing /tmp file before Write. Substantive S190 work was unaffected (DV-S190-1 + DV-S190-2 + EF-S190-1/2 + 4 FR-dispositions + 13 chain-walks all correct in substrate); only the close-record narrative was wrong.
