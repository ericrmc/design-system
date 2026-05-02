---
session: 171
title: fix-section-1-5-closed-loop — deliberation
generated_by: selvedge export
---

# Deliberation

## D-25 — §1.5 priority-order edit and operator-absent-default scope to escape five-session EF-triage-only closed-loop

sealed_at: 2026-05-02T02:21:11.808Z

### P-1 (anthropic)

**Position.** Operator diagnosis correct but bare priority-reorder insufficient; combine four edits: (A) insert MEDIUM-OI tractable-solo before EFs, (B) disqualify self-referential EFs, (C) cap N=2 auto-proceed-tactical, (D) admit MEDIUM-OI as tactical.

**schema_sketch.**
- Edit prompt-development §1.5 priority-order list: insert MEDIUM-priority open issues (tractable solo) as item 2.
- Define tractable solo inline as: concrete coding/migration/single-clause spec task not requiring perspective convening or methodology change.
- Edit operator-absent-default scope clause to enumerate tractable MEDIUM-OI burndown alongside single-clause spec edits as tactical paths.
- Add self-referential-EF disqualification: EFs about dispatcher pattern, audit-step:0 procedural rows, or session-watch calibration are not priority-2 and self-dispose at session-open.
- Add cap clause: after two consecutive auto-proceed sessions whose only effect was EF triage + FR disposition + close ceremony, next bare-prompt selects most tractable MEDIUM OI.
- No substrate schema change — purely prompt-edit; engine version unchanged unless cap clause is later promoted to substrate gate.
**what_not.**
- Do not introduce new substrate columns, EF tags, or migrations for this edit; the failure is dispatcher heuristic, not substrate shape.
- Do not move HIGH OIs from priority-1; HIGH dominance is correct and uncontested.
- Do not require operator ratification for bare-PROMPT.md auto-proceed; that defeats DV-S164-1.
- Do not add new perspective-convening requirement to escape the loop; the convening is here, in S171.
- Do not preserve audit-step:0 rows as next-session leverage; they are evidence only, not queue items.
- Do not classify all MEDIUM OIs as automatically tactical; tractability heuristic remains gating.
**migration_path.**
- One spec-version bump v18 to v19 carrying the §1.5 edits; no migration SQL.
- Cite EF-S165-1, EF-S167-1, FR-S165-9 as origin trail; cite EF-S170-1 fifth-recurrence threshold as trigger.
- New session-close discipline: bare-prompt session whose only substrate work was EF/FR/close-ceremony emits structural_no_progress flag in close-record items so cap clause is substrate-detectable.
- Defer any substrate gate (T-NN refusing nth tactical-only auto-proceed) to a later session if the prompt-only cap clause proves operator-policed insufficient.
**risk.**
- Tractability heuristic is judgment-call surface; agent might mis-classify a substantive OI as tractable and ship under-deliberated work.
- Self-referential-EF disqualification too broad could hide a real dispatcher regression EF that names a genuine gap.
- Cap N=2 may fire too early if a tactical session legitimately addresses operator-signal EFs.
- MEDIUM-OI burndown may starve important fresh operator-signal EFs unless those EFs are explicitly elevated.
- New cap-clause introduces consecutive-tactical-counting which itself is bookkeeping the agent must perform without substrate gating.
**open_question.**
- Which MEDIUM OIs in the current 25-row backlog satisfy the tractable-solo definition without perspective convening?
- Should the cap N=2 trigger off session count or off no-substantive-progress signal (codex P-2 raised this)?
- Should operator-signal EFs (those naming operator-authored direction) be explicitly carved out of the self-referential disqualification?
- Is no-non-meta-progress substrate-detectable from close-record items facets without new tagging?
- Does the operator explicit diagnosis in S171 constitute a permanent meta-rule that operator-named-loop is itself a HIGH-priority repair signal?
**what_lost.**
- Pure priority-order simplicity lost: §1.5 grows from four-item list to four-item list plus tractability gate plus disqualification clause plus cap clause.
- Some immediate responsiveness to fresh procedural EFs (audit-step:0, calibration of dispatcher) is lost — these now self-dispose rather than being triaged.
- Maintained: HIGH-OI dominance, bare-PROMPT.md auto-proceed without ratification (DV-S164-1), tactical-vs-substantive distinction, codex shape-consult requirement for substantive paths.
**position.**
- Operator explicit diagnosis-of-loop and direction to repair constitutes a named mandate at S171 itself; substantive work proceeds without further deferral.
- Pattern (operator names dispatcher loop, agent repairs same turn) is a meta-rule worth recording: operator-diagnosed-loop is admissible substantive scope under operator presence regardless of priority queue.

### P-2 (openai)

**Position.** Mostly agree with P-1 but make C less stateful: prefer starvation breaker keyed to no-non-meta-progress over fixed N=2 cap. A, B, D load-bearing; hard consecutive-session counter risks becoming new ceremony.

**schema_sketch.**
- Add MEDIUM-OI selection before EF in v18 section 1.5, limited to tractable solo work.
- Mark EF rows with meta_self_ref, audit_only, or operator_signal routing tags.
- Auto-dispose meta_self_ref and audit_only EFs at session-open unless they contain new operator direction.
- Define tractable MEDIUM-OI as concrete, bounded, and not requiring perspective convening.
- Amend operator-absent-default to classify tractable MEDIUM-OI burndown as tactical.
- Add a starvation breaker keyed to absence of non-meta progress, not just session count.
- Treat explicit operator diagnosis here as a named mandate to repair the dispatcher.
**what_not.**
- Do not blanket demote all EF below MEDIUM-OI; operator-signal EF can be urgent.
- Do not require operator ratification for every bare-PROMPT.md auto-proceed choice.
- Do not add a new perspective-convening requirement to escape the loop.
- Do not let audit-step:0 certifications create next-session priority leverage.
- Do not define all MEDIUM-OI work as substantive by default.
- Do not preserve FR emission if it only recreates the same tactical mandate.
**risk.**
- P-1 C may create another bookkeeping loop around counting tactical sessions.
- Direct reorder alone can still fall through to EF if operator-absent-default blocks MEDIUM-OI.
- Self-disposal of EFs could hide a real dispatcher regression if tagging is too broad.
- Tractability heuristics can be gamed unless examples are concrete.
- MEDIUM-OI burndown may starve important fresh EF unless operator-signal EF remains elevated.
**open_question.**
- Which MEDIUM OIs are currently tractable without perspective convening?
- Should starvation breaker trigger after one no-progress session or two?
- What exact EF tags already exist in the substrate, if any?
- Are audit-step:0 rows intended as evidence only or actionable queue items?
- Should FRs emitted by tactical sessions inherit a lower priority unless operator-authored?
**what_lost.**
- Some immediate responsiveness to fresh procedural EF is lost.
- The current purity of EF-before-MEDIUM priority is lost.
- Maintained: HIGH-OI dominance remains unchanged.
- Maintained: operator-signal feedback can still override routine backlog.
- Maintained: bare-PROMPT.md auto-proceed remains usable under DV-S164-1.

### Synthesis

## Synthesis (D-25)

P-1 and P-2 converge on three of four edits and diverge on the fourth. Adopt P-1's A/B/D verbatim and adopt P-2's starvation-breaker shape for C in place of P-1's fixed counter. Decline P-2's substrate-tagging proposal in this session; preserve it as graduation path M-1 if recurrence pressure builds. Record P-2's operator-diagnosis-as-named-mandate as a new clause.

The edit composes: (A) inserts MEDIUM-OI as priority-2 ahead of untriaged EFs, gated by tractable-solo definition; (D) admits tractable MEDIUM-OI burndown as tactical under operator absence so the new path is executable without operator presence; (B) disqualifies self-referential EFs (calibration about the dispatcher itself, audit-step:0 procedural rows, watch-cycle calibration the prior session explicitly emitted) from priority-2 leverage so they self-dispose at next session-open; (C-starvation) fires when the prior auto-proceed session's only substrate effect was EF/FR/close ceremony, forcing the next bare-prompt to pick the most tractable MEDIUM-OI before EF.

P-2's substrate-tagging proposal (meta_self_ref / audit_only / operator_signal) is not adopted because (i) prompt-side prose pattern-match can do the disqualification work without schema change, (ii) DV-S109-1 ceremony-subtraction discipline argues against substrate-side enforcement until prompt-only proves insufficient, and (iii) introducing tag columns now would require migration plus handler plus operator policing for which the recurrence evidence is one-loop-of-five not multi-loop. Preserved as M-1 graduation path: if a future calibration-EF names a session that fell into a similar loop despite the prompt-only B clause, the next session opens an OI to ship the substrate tags.

P-2's operator-diagnosis-as-named-mandate clause is adopted: when the operator names a dispatcher loop (or any §1.5 failure mode) in their input, that diagnosis itself is a HIGH-priority repair signal admissible as substantive scope under operator presence regardless of priority-order queue. This codifies what S171 itself demonstrated.

Dissent preserved: M-1 substrate-tagging graduation path; M-2 P-1's fixed-counter shape for C (replaced by starvation-breaker on grounds the counter is itself bookkeeping ceremony).

### Synthesis points

- **convergence C-1.** Insert MEDIUM-OI tractable-solo as priority-2 between HIGH OIs and untriaged EFs.
- **convergence C-2.** Disqualify self-referential EFs from priority-2 leverage (dispatcher calibration, audit-step:0, watch-cycle).
- **convergence C-3.** Admit tractable MEDIUM-OI burndown as tactical under operator-absent default.
- **convergence C-4.** HIGH-OI dominance and bare-PROMPT.md auto-proceed without ratification (DV-S164-1) preserved unchanged.
- **convergence C-5.** No substrate schema change in this edit; prompt-only spec-version bump v18 to v19.
- **convergence C-6.** Operator-diagnosis-of-loop is itself a named substantive mandate; admissible regardless of priority-order queue.
- **divergence D-1.** C shape: P-1 fixed N=2 counter vs P-2 starvation-breaker; resolved by adopting P-2 shape.
- **minority M-1.** P-2 substrate-tagging proposal (meta_self_ref / audit_only / operator_signal columns) deferred as graduation path if prompt-only proves insufficient.
- **minority M-2.** P-1 fixed-counter shape for C preserved as alternative if starvation-breaker proves under-triggering.
