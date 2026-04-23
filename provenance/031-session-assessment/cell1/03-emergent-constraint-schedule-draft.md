---
session: 031
title: Emergent-Constraint Schedule (Draft, not sealed)
date: 2026-04-23
status: draft-not-sealed
cell: 1
step: emergent-constraint-schedule
candidate: S1 Feldenkrais "Awareness Through Movement" Lesson 1 "What Is Good Posture?"
---

# Emergent-Constraint Schedule (Draft)

Per `reference-validation.md` v2 §2 Stage 0: Cell 1 outputs include an emergent-constraint schedule with tranche-1..N constraints tagged with release triggers stated in methodology terms only. This file drafts the schedule for the S1 Feldenkrais Lesson 1 exercise pending sealing in Session 032+.

**Marked draft-not-sealed** because the full sealing exercise (including the reference envelope with byte-identical reference text) cannot complete in Session 031 per L1b verdict §5. The draft is committed for continuity; Session 032+ (if operator ratifies continuing Cell 1) will adjust per any new considerations surfaced.

## Tranche-0 (initial brief for Cell 2 Produce agents at session open)

Tranche-0 is the constraint statement committed at `cell1/01-constraint-statement.md` and `cell1/constraint-prompt.txt`. This is the same text fed to the L1b test; it serves as Cell 2 tranche-0 unchanged if the exercise proceeds to sealing.

Tranche-0 coverage: ~60% of the final constraint set per C4 requirement (not more than 60% up-front). Deferred constraints appear in tranche-1 and tranche-2 below, released during Cell 2 per trigger conditions.

## Tranche-1 (first emergent release)

**Constraint T1**: The exploration must include an investigation in which the reader's attention is directed specifically to the range of motion between two contrasting postures. The investigation must ask the reader to try the two contrasting postures in turn, without prescribing which is "correct," and then invite the reader to rest somewhere in between.

**Release trigger**: Fires when Cell 2 Produce agents commit a first-draft artefact that does NOT include any contrasting-posture range-of-motion investigation. If the first-draft artefact already includes such an investigation (i.e., the Produce agents chose this design without prompting), T1 is released at the end of the first Produce round anyway so the exercise does not depend on the agents happening to ask the right question.

**Purpose**: Probes whether the methodology, given a tranche-0 describing the problem at a general level, can be led (via staged constraint release) toward the signature pedagogical move of Lesson 1 — investigation of what "good posture" means via a range-of-motion inquiry. Does not tip the specific pelvic-tilt instantiation (the Produce agent chooses whether to instantiate the range-of-motion in the pelvis, neck, shoulders, or elsewhere; the tranche-1 constraint is shape-only).

## Tranche-2 (second emergent release)

**Constraint T2**: The exploration's range-of-motion investigation must include at least one instance where the reader is prompted to notice that their habitual "good posture" is not a relaxed neutral state — it occupies a specific position in the range, and that position is not obvious to the reader before the investigation.

**Release trigger**: Fires after T1 is released and the Cell 2 Produce agents have committed a revised artefact that includes a range-of-motion investigation but does NOT include the insight-about-habitual-posture-as-specific-position. Alternatively, fires at end of round 2 regardless, per the trigger-dependency-floor rule.

**Purpose**: Probes whether the methodology can be led toward Lesson 1's conceptual payoff — the insight that "good posture" is a felt position within a range, discovered through investigation, not prescribed by anyone. Again does not tip the specific content (does not say "pelvic tilt", does not say "lumbar"); the Produce agent chooses how to instantiate.

## Anti-drift structure

The tranche-1 and tranche-2 triggers are observable methodology events (artefact committed; round N finished). Triggers do not depend on the Produce agents asking the right question.

The trigger-release floor (tranche-1 at end of round 1; tranche-2 at end of round 2) ensures the exercise completes even if the Produce agents naturally converge on the design without prompting.

Per §3 Cell 2 shape, the exercise runs at most 2 internal Produce rounds. With tranche-0 at open, tranche-1 end-of-round-1, tranche-2 end-of-round-2, the emergent-constraint-release schedule spans the full Cell 2 budget.

## Contamination-audit plan (draft)

Per v2 §4 L7 (distinctive-marker audit): Cell 3 contamination auditor will be asked to check specifically for:

- Reproduction of Lesson 1 title ("What Is Good Posture?") or question-as-title form.
- Pelvic-tilt instruction sequence (pressing lumbar to floor + arching lumbar).
- Any arbitrary count matching Lesson 1's counts ("five times" on specific moves).
- Feldenkrais-teacher stock phrases documented in the Case Steward's L2 flag annotation.

Per v2 §4 L6 (process-trace requirement): Cell 2 Produce agents must emit the constraint-to-decision trace alongside the artefact. The trace is consulted at Cell 3 to verify each major artefact element traces to a released constraint + methodology decision, not to genre retrieval.

Per v2 §4 L5 (counterfactual probe): after Cell 2 Produce completes, Case Steward modifies one constraint to be off-distribution (e.g., "lying prone instead of supine" or "standing instead of lying") and asks the methodology to re-produce. If the methodology produces a genuinely different artefact tracking the new constraint, positive design evidence; if it produces a near-copy of the supine version ignoring the constraint change, retrieval evidence.

## Pending-sealing fields

These fields would be filled at sealing (Session 032+ pending operator reference-text provision):

- `reference-envelope/00-reference-scope-and-attribution.md` — would be authored post-sealing to describe what portion of Lesson 1 is the reference for this exercise.
- `reference-envelope/01-lesson-1-text.md` — would contain the byte-identical reference text (provided by operator).
- `reference-envelope/02-author-uncertainty-commentary.md` — Feldenkrais's own account of what he is uncertain about in Lesson 1, sourced from his preface or per-lesson commentary in *Awareness Through Movement*.
- `reference-envelope/99-anti-drift-witnesses.md` — URLs or scan-provenance for the reference source + fetch/scan dates.
- `brief-gatekeeper.md` (at exercise-provenance root) — committed with sealing commit-hash as the anti-tampering witness per v2 §3 Cell 1.

Session 031 leaves these fields explicitly unfilled.

## Summary

Session 031 produced:
- Candidate reselection (S1 carried from Session 018 survived-canary pool) — `cell1/00-candidate-reselection.md`
- Constraint statement (Cell 2 tranche-0) — `cell1/01-constraint-statement.md` + `cell1/constraint-prompt.txt`
- L1b saturation test (codex + independent Claude) — `cell1/02a-l1b-codex-raw.txt` + `cell1/02b-l1b-claude-raw.md`
- L1b verdict (PASS with genre-saturation observation) — `cell1/02-l1b-verdict.md`
- Emergent-constraint schedule draft (tranche-1, tranche-2, contamination-audit plan) — this file

Session 031 did not produce (deferred to Session 032+):
- Reference envelope sealed with byte-identical source text
- Anti-drift witness URLs/scan dates
- `brief-gatekeeper.md` with sealing commit-hash
- `participants.yaml` (no deliberation; no multi-perspective convening this session)
- Any `manifests/` entries (no v4-schema participants required for Cell 1 single-steward orchestrator work)

The L1b PASS is a provisional finding; sealing the case pack and proceeding to Cell 2 Produce in Session 032+ requires operator reference-text provision and operator ratification of Cell 2 convening.
