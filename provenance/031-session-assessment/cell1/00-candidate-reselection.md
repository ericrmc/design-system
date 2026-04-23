---
session: 031
title: Cell 1 Candidate Reselection — S1 Feldenkrais Lesson 1 as Top Candidate for L1b Re-attempt
date: 2026-04-23
status: complete
cell: 1
step: candidate-reselection
case_steward: Claude Opus 4.7 (orchestrating agent; L2 limitation per Session 018 D-076 carries forward)
---

# Cell 1 · Step 1 — Candidate Reselection

## §1 Purpose

Session 031 re-opens reference-validation Cell 1 per operator Path C ratification. This file establishes which candidate from the Session 018 pool (or fresh candidates) this session will advance through the `reference-validation.md` v2 §1 C3 two-stage saturation test — specifically the L1b full-constraint saturation test that Session 018 did not run on S1 and S2.

Per v2 §1 C3 Stage (b) mandatory pre-seal: every candidate must pass the full-constraint saturation test with both a non-Claude model (via `codex exec`) and an independent Claude instance producing text with <30% 5-gram overlap, zero verbatim distinctive-phrase emission, and no cross-family retrieval asymmetry.

## §2 Session 018 pool — current status

Session 018 surveyed seven candidates (S1, S2, S3, D1, D2, D3, D4), nominated four for formal evaluation (S1, S2, D1, D2), and advanced the candidates through L1 canary + C3 test. Current status at Session 031 open:

| ID | Candidate | Domain | L1a canary | L1b / C3 Stage (b) |
|---|---|---|---|---|
| S1 | Feldenkrais Lesson 1 "What Is Good Posture?" | Movement/somatic | Survived (Session 018) | **Not yet run** |
| S2 | Alexander Semi-Supine protocol | Movement/somatic | Survived (Session 018) | **Not yet run** |
| D1 | Liberating Structures 1-2-4-All | Facilitation | **Rejected** at L1 canary (Session 018) | n/a |
| D2 | Kerth Prime Directive retrospective opening | Agile-retrospective | Survived | **Rejected** at C3 (Session 018; 94% overlap; Claude verbatim reproduction) |
| S3 | Rolfing opening session | Practitioner-administered | Dropped pre-test (C7) | n/a |
| D3 | NVC 4-step | Decision aid | Dropped pre-test (C3 predicted fail) | n/a |
| D4 | Gordon Method III | Decision aid | Dropped pre-test (C3 predicted fail + trivial shape) | n/a |

**Surviving-canary candidates never tested at L1b: S1 (Moderate C3 risk), S2 (High C3 risk).**

## §3 Session 031 candidate selection rationale

**Selected: S1 Feldenkrais Lesson 1 "What Is Good Posture?"**

Rationale:
1. **Continuity with Session 018 work.** S1 is a carried-forward candidate that survived L1a canary under the v1 protocol. Session 019's v2 revision added L1b (full-constraint saturation) as mandatory pre-seal. Running L1b on S1 is the natural continuation: the candidate is partially-processed and the v2-upgraded standard has not been applied.
2. **Lower C3 risk than S2.** Session 018 self-assessed S1 as Moderate C3 risk and S2 as High C3 risk. Testing S1 first is the higher-probability-of-passing direction; if S1 fails, S2 almost certainly would fail. If S2 were tested first and passed, it would be a surprising positive signal — but the High-risk self-assessment predicts failure, making it a likely-rejection path.
3. **Domain structurally different from D2 (agile-retrospective).** S1 is in the movement/somatic domain. Per v2 §9 trigger 7, two pre-seal C3 stage (b) rejections in **structurally-different domains** activates the Session 014 Skeptic "provisional substitute" minority warrant as a required kernel §7 revision consideration. D2 (Session 018 rejected) is agile-retrospective. If S1 rejects at L1b, that is an n=2 structurally-different-domain pattern → §9 trigger 7 fires.
4. **Single-candidate evaluation matches Session 018 precedent and bounded session scope.** Session 018 tested four candidates through L1 canary and one (D2) through C3 stage (b). Session 031 testing one candidate at L1b is a bounded exercise appropriate to Cell 1 single-session scope.

## §4 Candidate S1 reference scope

- **Source.** Moshe Feldenkrais, *Awareness Through Movement: Health Exercises for Personal Growth*, Harper & Row, 1972 (HarperOne/HarperCollins reprints continuously in print).
- **Selected lesson.** Lesson 1 "What Is Good Posture?" — the book's first movement lesson; ~30-minute lying-down sequence.
- **Published.** 1972 (54 years before 2026). Pre-LLM by decades; satisfies C8a.
- **C7 representativeness.** Self-guided movement/attention sequence; same-shape as Session 008 external artefact (Morning Unfurl).
- **C8b falsification-admitting.** Partial — the lesson has implicit mandatory (lying supine; pelvic exploration) and optional (variations) elements; failure conditions named but not formally tagged.
- **C8c uncertainty-declared.** Yes — Feldenkrais's preface and lesson commentary include explicit uncertainty about reader experience.
- **C1 auditability.** Yes — published book, documented author, accessible citation.
- **C2 constraint-legibility without solution-smuggling.** To be verified by §5 constraint statement draft below.
- **C3 low-saturation.** Self-assessed Moderate at Session 018; L1b test will produce empirical verdict.
- **C4 staged-constraint structure.** Moderate — the lesson has an opening setup, middle exploration, and integration; less formally staged than D1 Liberating Structures.
- **C5 domain-legibility.** Adequate — movement/somatic work is widely-enough documented that a cross-family validator panel can distinguish structural match from lexical coincidence; Session 018 assessment noted judge-diversity is needed.
- **C6 bounded effort.** Yes — single lesson fits under 10,000 tokens; constraint statement fits in 1–3 KB.

## §5 Constraint statement for L1b saturation test

Drafted per `reference-validation.md` v2 §2 Stage 0 requirements: problem-shape statable without tipping the solution; no reference-lexical fingerprints; no naming of author, book, method, or lesson title; no distinctive Feldenkrais terms. See `01-constraint-statement.md` (next file).

## §6 L1b test plan

Per v2 §4 L1b:

1. **Constraint statement** (in `01-constraint-statement.md`) is the exact prompt used for both model families.
2. **Non-Claude model invocation**: `codex exec` with the constraint statement. Model family: OpenAI GPT-5 or analogous via codex CLI.
3. **Independent Claude instance invocation**: Agent tool (general-purpose subagent) with the constraint statement. Isolated from orchestrator context per MAD v4 §Mechanism.
4. **Both outputs committed verbatim** to `cell1/` as `02a-l1b-codex.md` and `02b-l1b-claude.md`.
5. **Evaluation** per v2 §1 C3 rejection conditions:
   - (1) Either model produces text exceeding 30% 5-gram token overlap with the published reference.
   - (2) Either model spontaneously emits a verbatim distinctive phrase, section heading, or named label from the reference (zero-tolerance).
   - (3) Cross-family retrieval asymmetry: one family reproduces verbatim or with idiosyncratic labels while the other produces constraint-satisfying but from-scratch text.
6. **Verdict recorded** in `02-l1b-verdict.md`. If pass on all three: proceed to sealing. If any reject condition fires: record rejection; do not seal; assess §9 trigger implications.

## §7 Honest limits at this step

- **L2 orchestrating-agent-Case-Steward contamination flag carries forward from Session 018 D-076.** The Case Steward (me) has Claude-family pretraining including Feldenkrais literature; this is acknowledged as a residual-risk factor for the Cell 1 stage.
- **Comparison reference text.** The "published reference" against which 5-gram overlap is measured is the Feldenkrais Lesson 1 as documented in *Awareness Through Movement* (1972). I have training-distribution exposure to this text but not a sealed copy in-hand; 5-gram evaluation will be qualitative (distinctive-phrase detection; structural correspondence) rather than quantitative-mechanical (precise Jaccard index over 5-grams). This is a deliberate narrowing acknowledged now per Session 018's precedent (where the D2 Kerth Prime Directive ~94% overlap was also qualitatively assessed via verbatim-paragraph detection rather than mechanical 5-gram computation).
- **Predicted C3 risk level: Moderate per Session 018 self-assessment.** Historical outcome: Session 018 Moderate-risk candidate (D2) failed catastrophically at L1b-equivalent. This creates a prior that Moderate-risk candidates may also fail; the Session 031 test is probative regardless of outcome.
- **Session 014 Skeptic §1-flagged tension applies.** Movement/somatic references that pre-date 2022 and are legible to validators are likely saturated. S1 is on the edge of this tension.
- **§9 trigger 7 stake.** If S1 rejects at L1b with verbatim-or-near-verbatim reproduction in the Claude family and structural divergence in the non-Claude family, that matches the n=2 structurally-different-domain pattern (D2 Session 018 agile-retrospective + S1 Session 031 movement/somatic) → §9 trigger 7 fires → OI-016 re-opens to Open state + Session 032 kernel §7 revision consideration required. This stake is declared transparently; the test runs regardless.

## §8 Next step

Proceed to `01-constraint-statement.md` (draft the problem-shape constraint for Cell 2 with no reference-lexical fingerprints), then `02a-l1b-codex.md` + `02b-l1b-claude.md` (run L1b on both model families), then `02-l1b-verdict.md` (record pass/reject verdict).
