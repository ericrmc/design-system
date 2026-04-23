---
session: 043
perspective: Work-Shape Proposer
perspective_index: 1
lineage: claude
---

# Perspective 1: Work-Shape Proposer

## Reading performed

- `provenance/043-session-assessment/01-brief-shared.md`
- `provenance/043-session-assessment/00-assessment.md`
- `specifications/methodology-kernel.md` v6
- `specifications/multi-agent-deliberation.md` v4
- `specifications/read-contract.md` v4
- `SESSION-LOG.md` (42 thin-index rows)
- `open-issues/index.md`

No archive-surface files were read. SESSION-LOG rows and the in-assessment summaries provided sufficient timeline context for this perspective's work.

## Q1 — Is warrant-firing sparse by design?

Mixed. The **activation warrants** attached to §5-series preserved minorities and §10.4 observational windows are by-design sparse: each is tied to a specific operational event (a re-fire, a threshold-cross, a retention-exception accumulation), and the engine is correct not to synthesise such events. But **warrant-firing is not the only mechanism the engine has for generating work**. It also has:

- Operator-surfaced agendas (Session 032, 036, 041-by-ratification, 043).
- §9 trigger conditions in `reference-validation.md`.
- Open-issue advancement warrants (required-trigger deliberations per MAD §When Non-Claude Participation Is Required).
- §6.2 post-v-bump audit cadence.

Of these, the open-issue-advancement channel has narrowed to near-zero since OI-004 closed at S041 (the only OI with a substantive advancement cadence is now OI-016, whose counter sits at 2-of-3 with no near-term fire). §9 trigger 7's re-fire counter has been 0-of-3 since Session 032. §6.2 audits fire only post-bump. The operator-surfaced channel is operator-dependent by construction.

What this means: the **engine-internal generators of non-A work have concentrated into a small number of event types, most of which have low current activity**. This is not the same as warrant-firing being sparse by design in the abstract; it is that the current configuration has quieted most of the channels simultaneously. Under-articulation is real but specific: the engine does not have a mechanism for generating work from the **absence of events in channels that normally produce events**. It has the inverse (§10.4 zero-event watchpoints, which observe absence but do not generate work from it).

## Q2 — Observational metrics: evidence of what?

(d) Both simultaneously, with a load-bearing caveat. No-growth streaks, preservation depths, and zero-event windows are metrics **about the engine's metabolism, not about the engine's output**. They are evidence that the engine is not producing drift-type failures (spec churn; unjustified bumps; forced remediation). They are **not** evidence that the engine is producing the work it should be producing. A dead engine and a disciplined engine produce the same zero-event metric readings.

Cite S041 retrospective: §5.3 was strongly vindicated exactly because twenty successor sessions produced positive-looking metric readings while OI-004 advancement stalled. The vindication shows that observational metrics read as positive in the very regime the operator is now asking about. Using those metrics as evidence that Path A is correct is the self-referential trap the brief names.

## Q3 — Work-shapes the current default does not generate

**This is my primary question.** I name candidates beyond the three the operator seeded. For each, I state defect/feature/indeterminate and why.

**(a) Specification-coherence deliberation without an activation warrant.** The engine revises specs in response to warrants (§5-series activations, §9 triggers, operator agendas) but does not schedule spec-coherence review *as work in itself*. A session whose shape is "read the eight active specs together and look for cross-spec incoherence introduced by independent revisions" has never occurred. The D-126 minor documentary update is the closest adjacent shape but was triggered by OI-004 closure, not by coherence review. **Absence: probably a defect at the current engine age.** Eight active specs, multiple substantive revisions per spec, and no scheduled cross-spec coherence pass means incoherence can accumulate below any single-session activation threshold. Operational hook: a Path CC session every N sessions reading all active specs for mutual consistency.

**(b) Re-reading of archive surface for drift patterns the retention window occludes.** §2c's 6-session window is correct for per-session read-load, but it means drift patterns with periods >6 sessions are structurally invisible to default-read. The Session 027 §C minority explicitly flagged this ("single-session self-audits cannot catch cross-sectional drift"). The §10.4 six-minority windows *approach* this shape but are tied to specific minorities, not to drift patterns in general. **Absence: indeterminate leaning defect.** The §2c window is cheap in per-session read cost; a periodic long-baseline read is not cheap and might produce mostly-nothing findings. But the S041 vindication shows that a 20-successor-session pattern can pass unnoticed session-to-session. Operational hook: a Path LB (long-baseline) session every 10–15 sessions reading the full SESSION-LOG thin-index + selected archive-surface closes.

**(c) Deliberate stress-testing of machinery that is not currently exercised.** The brief's seed (2) names this (external-problem mode; non-GPT non-Claude). I extend: the engine has acceptable-participant-kinds enumerated in MAD v4 §Acceptable Participant Kinds that have **never been operationally exercised** — locally hosted open-weight model; human reviewer recruited externally; aggregator-mediated non-Anthropic model. The §5.1 Skeptic strict-enumeration minority (preserved in the S021 articulation) explicitly warned about enumerating kinds the methodology has not exercised. S041 closed OI-004 with a cumulative record exercising exactly one non-Claude lineage (GPT via codex). **Absence: defect.** The engine is carrying specification weight for participant kinds it cannot verify from its own operational history. Operational hook: scheduled stress-test sessions that deliberately exercise an unexercised kind, even if the substantive question is synthetic.

**(d) External-problem application in this workspace.** The engine's architecture supports both self-development and external-problem modes (per `MODE.md` + dispatcher). Self-development has 42 sessions of exercise. External-problem mode has Sessions 007–018's reference-validation exercises, which are a **bounded probe shape**, not a sustained application. There has been no "apply the engine to someone else's actual problem for N sessions" exercise since Session 018. **Absence: defect.** The engine is optimising against its own self-development baseline, and its claims of general applicability (the kernel explicitly claims to apply to external-problem work) are weakly grounded. Operational hook: an external-problem workspace spun up with a real operator problem, with at least one session of cross-workspace reference back to this workspace's engine.

**(e) Targeted negative-result probes.** The engine has produced positive results (L1a/L1b PASS at Session 031; OI-004 closure at S041) and negative results that emerged naturally (S018 D2 REJECT; S032 PD-A L1b REJECT). It has never **deliberately sought** a negative result — e.g., "attempt a substantive revision that should fail our own validation and confirm it fails." Validation-machinery confidence relies entirely on observed-in-the-wild firings. **Absence: indeterminate.** The cost is fabrication risk (manufactured negative results teach little); the benefit is validator calibration. Probably a feature at current engine age, defect if the validator's checks grow to >30 without a deliberate failure-mode exercise.

**(f) Multi-session investigations with emerging constraints (operator seed 3).** I concur this is absent. The engine's session model is "one increment per session"; investigations spanning sessions happen only through OI advancement, which is event-gated. A work-shape where Session N opens an investigation whose constraints are explicitly unknown and Session N+k closes it has no current scaffolding. **Absence: indeterminate.** Scaffolding this risks session-coupling (losing the "each session reads workspace state fresh" property); not scaffolding it means certain investigation shapes cannot occur. Worth a separate deliberation; not a default-generate item.

**(g) Evolutionary increments without an activation warrant (operator seed 1).** I concur this is absent. The engine's increment model is warrant-driven; unwarranted evolution is exactly what §5.3 warned against in reverse (retrofitting paths to generate activity). **Absence: feature.** The engine should not generate evolutionary increments on demand. The operator's seed is wrong here, in my reading. The correct response to this concern is not "generate unwarranted increments" but "surface the pattern that work channels have concentrated so the operator can supply agenda" — which the operator has in fact done at S043.

**(h) Exercising under-tested machinery (operator seed 2).** I concur, and subsume under (c) above.

## Q4 — Should default-agent path recommendation surface non-Path-A alternatives with evidence?

Yes, but narrowly. The analogy to Rejected-alternatives in decision records is useful: the discipline forces the agent to **articulate what it considered and rejected**, not to generate activity. The specific convention I propose: the default-agent assessment must include a short section naming at least two non-Path-A shapes that were considered and state why they were not warranted. This is cheap, anti-laundering (it does not retrofit activity; it records the consideration explicitly), and discoverable (future readers can trace the assessment's shape-space).

This is distinct from requiring Path A to be justified by positive evidence (which collapses into the self-referential trap).

## Q5 — Periodic self-audit reading further back than §2c?

Net-positive if scoped carefully. The risk the operator frames as laundering is real: if the self-audit itself becomes a scheduled event whose firing generates activity, it becomes the activity channel it was meant to check. The mitigation is **scope and termination discipline**: the self-audit reads, produces findings-or-none, and terminates; it does not carry an activation obligation. Its output is a short finding list that either triggers other paths (by producing evidence that fires other warrants) or terminates with `[none]` recorded.

Proposed cadence: every 10 sessions, or at operator request. Scope: full SESSION-LOG thin-index + selected archive-surface closes named at convening time. Output: one file per session recording findings-or-none. **This is the Path LB shape from Q3(b).**

## Q6 — Does §5.3 S041 vindication imply path-selection-mechanism revision?

Yes, modestly. The discharge-as-vindicated is complete for §5.3's specific warrant; the vindication is a data point saying the warning was calibrated. But the **forward mechanism** that allowed the 20-session drift to accumulate unnoticed is unchanged: default-agent path recommendation still produces Path A whenever no warrant fires, and no mechanism routes the vindication event back into path-selection. The minimal revision is the Q4 Rejected-alternatives convention. A larger revision is the Q5 periodic self-audit. Both are consistent with discharge-as-vindicated being complete; neither requires re-opening §5.3.

## Q7 — Verdict on the operator's framing

Partially correct. The observation (6-of-10 Path A; self-reinforcing metric loop) is accurate. The framing "structural gap in path selection" is slightly wrong in direction: the gap is not in path selection but in **work-channel diversity**. Several of the engine's work-generating channels have quieted simultaneously (OI-advancement post-OI-004; §9 trigger 7 at 0-of-3; §5-series firings rare). Path selection is correctly warrant-gated; the question is whether the engine has enough **channels** producing warrants. The adjustment: keep warrant-gating; add (i) Rejected-alternatives convention in assessments; (ii) periodic long-baseline audit; (iii) scheduled exercise of under-tested machinery. Preserve operator-seed (1) "evolutionary increments without warrant" as a first-class minority-against; it is the correct instinct to reject.

## Independent claim

The engine's path-selection discipline is sound; what is weak is its **work-channel diversity**, which has concentrated into operator-surfaced agendas and rare §5-series firings. The fix is to widen the set of work-generating channels (scheduled coherence passes; long-baseline audits; under-tested-machinery exercise) rather than to loosen warrant-gating.

## Confidence and limits

Confident: enumeration of work-shapes (a)–(h) and their defect/feature/indeterminate classifications; the distinction between warrant-gating (sound) and channel diversity (weak); the Rejected-alternatives convention in Q4 as a cheap non-laundering intervention.

Not confident: cadence values (every 10 sessions vs every N); whether (c) stress-testing has a viable operational hook given operator-ratification bandwidth; whether the proposed Path LB can preserve termination discipline under repeat exercise.

Could not resolve in scope: whether an external-problem application (work-shape (d)) is warranted *now* or whether the self-development application has further to go first. This is an operator-direction question, not a work-shape-enumeration question.
