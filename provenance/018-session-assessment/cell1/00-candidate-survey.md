---
session: 018
title: Cell 1 Candidate Survey — Reference-Validation Exercise 1
date: 2026-04-22
status: complete
cell: 1
step: candidate-survey
case_steward: Claude Opus 4.7 (orchestrating agent)
l2_contamination_flag: orchestrating-agent-Case-Steward carries workspace-context and Claude-family pretraining; flagged per D-072 for eventual contamination-audit.md inclusion
---

# Cell 1 · Step 1 — Candidate Survey

## Purpose

This file executes the Case Steward's first Cell 1 activity under `reference-validation.md` §3: enumerate candidate reference cases, surface their provenance transparently (anti-silent-import rule per `PROMPT.md`/`prompts/development.md`), and apply a first-pass §1 C1–C8 self-assessment to identify survivors worth taking to the C3 saturation gate and L1 contamination canary.

Per D-072 (Session 015) the shortlist must span a **mixed direction**: same-domain-adjacent to the Session 008/010 external artefacts (movement sequences; household-decision protocols) *and* different-domain-representative cases where the methodology's external-artefact claim would need to hold if challenged.

## Provenance source (transparency)

All candidates below are surfaced from the Case Steward's pretraining (Claude Opus 4.7 training distribution). Per `reference-validation.md` §4 L2 known-limitation flag, this is a contamination vector: candidates pre-selected because *I remember them* are, by construction, at elevated C3 saturation risk. The survey step exposes the full consideration set and applies the 8 criteria to filter down, rather than committing directly to any candidate. This matches the PROMPT.md anti-silent-import rule: my pretraining knowledge enters the session through an **explicit surveying step**, not silently into selection.

## Candidate set (seven candidates surveyed; four nominated for formal evaluation)

### Same-domain-adjacent candidates (movement / somatic / self-care sequences)

#### S1. Feldenkrais Awareness Through Movement: Lesson 1 "What Is Good Posture?"

- **Source.** Moshe Feldenkrais, *Awareness Through Movement: Health Exercises for Personal Growth*, Harper & Row, 1972 (continuously in print; HarperOne/HarperCollins reprints).
- **Shape.** ~30-minute lying-down lesson with staged micro-movements, observation prompts, asymmetry explorations.
- **Published.** 1972 (54 years before 2026). Pre-LLM by decades.
- **C7 representativeness.** Movement sequence; same shape as Session 008 Morning Unfurl.
- **C4 staged-constraint structure.** Plausibly strong — the lesson is explicitly staged, and Feldenkrais's own prefaces document that his lessons evolved iteratively through teacher training and book editions.
- **C8a pre-LLM-co-design.** Yes (1972).
- **C8b falsification-admitting.** Partial — the book has explicit optional variations and "if you feel discomfort" cautions; mandatory vs optional elements distinguishable but not formally tagged.
- **C8c uncertainty-declared.** Yes — Feldenkrais's preface and per-lesson commentary include explicit uncertainty ("each person will experience this differently", "I cannot know exactly what you will find").
- **C3 saturation risk (self-assessment).** Moderate. Feldenkrais method is well-represented in pretraining corpora but *specific numbered lessons* with their exact sequence and wording are less canonical than the aggregate Feldenkrais concept. Operational test required.
- **C6 bounded effort.** Yes. Single lesson fits well under 10,000 tokens; constraint statement fits in 1–3 KB.
- **Weakness.** Reference-faithful reader would need some Feldenkrais literacy; validator panel must include at least one judge with enough somatic-work exposure to read the lesson structurally rather than lexically (C5).

#### S2. Alexander Technique: Constructive Rest / Semi-Supine protocol

- **Source.** Tradition originating with F. M. Alexander (1869–1955); specific documented protocol in Frank Pierce Jones, *Body Awareness in Action* (Schocken 1976); Missy Vineyard, *How You Stand, How You Move, How You Live* (Da Capo 2007); Walter Carrington's recorded teachings.
- **Shape.** ~15-minute lying practice with specific position (head-on-books, knees up), attention-direction ("let the neck be free, the head go forward and up, the back lengthen and widen"), duration.
- **Published.** Decades of documentation; individual protocols pre-date 2000.
- **C7 representativeness.** Movement/attention sequence; same-domain-adjacent to Morning Unfurl.
- **C4 staged-constraint structure.** Moderate — the practice has an opening setup (position) and a sustained middle (attention cycling); "emergent constraints" in the Feldenkrais/Alexander style show up as teacher corrections to student habits during the practice, less as formal tranche releases.
- **C8a.** Yes (tradition pre-1922; book documentation pre-LLM).
- **C8b falsification-admitting.** Weak. The practice is "do the position, think the directions, do not try to do anything"; the failure mode ("I strained, pulled, imposed") is stated but not operationally falsifiable from an artefact.
- **C8c uncertainty-declared.** Present across the literature but mostly in teacher-training contexts; less in the protocol itself.
- **C3 saturation risk (self-assessment).** High. The "neck free, head forward and up, back lengthen and widen" language is extremely canonical and specific; Claude would likely emit it verbatim given even a thin prompt.
- **C6.** Yes.
- **Weakness.** C3 saturation is the dominant concern. C8b weakness (low falsification-admission) further weakens discriminability.

#### S3. Ida Rolf's Ten-Session Structural Integration opening session

- **Source.** Ida Rolf, *Rolfing: The Integration of Human Structures*, Harper & Row 1977.
- **Shape.** First of 10 body-work sessions; specific body regions, specific maneuvers, documented session goals.
- **Weakness.** Practitioner-administered (not self-administered); doesn't fit the Morning-Unfurl-adjacent self-administered shape that the methodology has actually produced. C7 representativeness weaker. **Dropped from formal-evaluation shortlist.**

### Different-domain-representative candidates (decision aids / structured procedures / protocols)

#### D1. Liberating Structures "1-2-4-All" micro-structure

- **Source.** Henri Lipmanowicz & Keith McCandless, *The Surprising Power of Liberating Structures: Simple Rules to Unleash a Culture of Innovation*, Liberating Structures Press 2013.
- **Shape.** 12-minute group facilitation pattern: 1 minute silent individual reflection → 2 minutes pairs → 4 minutes quartets → whole-group synthesis. Documented timing, grouping progression, purpose statement, don'ts.
- **Published.** 2013 (13 years before 2026). Pre-LLM (late 2022).
- **C7 representativeness.** Structured procedure / decision aid; adjacent to Session 010 House Decision.
- **C4 staged-constraint structure.** Strong. Timing and grouping are explicit staged releases; the book documents iteration history through practitioner reports.
- **C8a.** Yes (2013).
- **C8b falsification-admitting.** Yes — "Minimum Specifications" list in the book enumerates mandatory vs optional elements explicitly, and failure-modes ("micromanaging, skipping rounds, mixing patterns") are named.
- **C8c uncertainty-declared.** Yes — the book's back-matter and online companion explicitly discuss variations, when a pattern doesn't fit, what authors remain uncertain about.
- **C3 saturation risk (self-assessment).** Moderate. 1-2-4-All is well-known in facilitation circles but the specific mandatory-elements list, exact timing, and prohibitions are less canonical than the name. Operational test required.
- **C6.** Yes. Pattern page fits ~2 KB.
- **Weakness.** Domain literacy: validator panel must include at least one judge familiar with group-facilitation literature to distinguish structural match from lexical coincidence.

#### D2. Norm Kerth's "Prime Directive" retrospective opening

- **Source.** Norman Kerth, *Project Retrospectives: A Handbook for Team Reviews*, Dorset House 2001.
- **Shape.** Specific opening-the-retrospective protocol: Prime Directive reading (exact text, ~40 words), safety check, constraint-affirmation, agenda preview. ~10 minutes. Pre-LLM.
- **C7 representativeness.** Structured procedure. Adjacent-ish to House Decision (both facilitate a potentially-charged conversation).
- **C4 staged-constraint structure.** Moderate. Kerth documents revisions across editions; explicit stages within the opening sequence.
- **C8a.** Yes (2001).
- **C8b.** Moderate — Prime Directive is mandatory; agenda-preview is optional; failure conditions named ("blame surfaces; psychological safety collapses").
- **C8c.** Present — Kerth's foreword discusses his own uncertainty about scale-dependence.
- **C3 saturation risk (self-assessment).** Moderate. The specific Prime Directive text ("Regardless of what we discover, we understand and truly believe that everyone did the best job they could…") is extremely canonical for agile-practitioner pretraining; however, the full opening sequence (Prime Directive + safety check + constraint-affirmation + agenda preview as a bundled protocol) is less canonical than the Prime Directive in isolation.
- **C6.** Yes. Protocol fits ~2 KB.
- **Weakness.** Validator panel should include at least one judge with agile/retrospective literacy.

#### D3. Nonviolent Communication 4-step expression framework

- **Source.** Marshall Rosenberg, *Nonviolent Communication: A Language of Life*, PuddleDancer Press 1999/2003.
- **Shape.** Observation + Feeling + Need + Request 4-step grievance-expression template.
- **Weakness.** C3 saturation risk: **very high.** NVC's 4-step is one of the most canonical decision-aid frameworks in pretraining corpora; Claude and GPT both emit it reliably from thin prompts. **Dropped from formal-evaluation shortlist** on predicted C3 failure.

#### D4. Thomas Gordon's Method III (6-step No-Lose conflict resolution)

- **Source.** Thomas Gordon, *Parent Effectiveness Training*, Wyden 1970.
- **Shape.** 6-step procedure: identify problem → generate possible solutions → evaluate → decide → implement → follow up.
- **Weakness.** C3 saturation risk: high (generic problem-solving shape that Claude/GPT will trivially approximate from any reasonably-worded constraint statement). The sequence is also borderline-trivial structurally ("identify, generate, evaluate, decide, implement, follow up" is close to the generic engineering/management loop). **Dropped from formal-evaluation shortlist.**

## Formal-evaluation shortlist (four candidates)

Carrying forward to §1 C1–C8 filtering and C3/L1 operational tests:

| ID | Candidate | Direction | Predicted C3 risk |
|---|---|---|---|
| S1 | Feldenkrais Lesson 1 "What Is Good Posture?" | Same-domain-adjacent (movement) | Moderate |
| S2 | Alexander Semi-Supine protocol | Same-domain-adjacent (movement) | High |
| D1 | Liberating Structures 1-2-4-All | Different-domain-representative (facilitation) | Moderate |
| D2 | Kerth Prime Directive retrospective opening | Different-domain-representative (facilitation) | Moderate |

Dropped at this stage without operational test (pre-test self-assessment): S3 Rolfing (C7 practitioner-administered, doesn't match methodology's external-artefact shape); D3 NVC 4-step (predicted C3 failure); D4 Gordon Method III (predicted C3 failure + near-trivial generic shape).

Three candidates carried forward at "Moderate" C3 risk; one (S2) at "High" risk, retained because its same-domain-adjacent shape is valuable diversity and the operational test will either confirm or falsify the high-risk self-assessment.

## Next step

Proceed to Step 2: apply remaining C1–C8 criterion filters (C1 auditability, C2 constraint-legibility, C6 bounded-effort confirmation) to the four shortlist candidates; write constraint statements for each suitable for the C3 saturation gate; run C3 test + L1 contamination canary; present final shortlist to user for ratification per D-072.
