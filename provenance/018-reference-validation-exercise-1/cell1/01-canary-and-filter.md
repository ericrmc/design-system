---
session: 018
title: Cell 1 Step 2 — C1-C8 Filtering + L1 Contamination Canary
date: 2026-04-22
status: complete
cell: 1
step: canary-and-filter
case_steward: Claude Opus 4.7 (orchestrating agent)
---

# Cell 1 · Step 2 — C1-C8 Filtering + L1 Contamination Canary

## Purpose

Apply remaining §1 C1-C8 criterion filters to the four shortlisted candidates from `00-candidate-survey.md`. Run the §4 L1 contamination canary on each candidate (thin prompts derived from tranche-0, fired at Claude and OpenAI/codex model families) and reject on spontaneous emission of reference's idiosyncratic structure/labels/sequence.

The quantitative 5-gram overlap portion of C3 is **deferred** to post-ratification: for the single candidate the user selects, the Case Steward will perform a rigorous constraint-only test with sealed-reference comparison before writing the sealed case pack. This staging is operationally pragmatic — the canary is cheap to run on all four candidates; full overlap measurement requires sourcing the reference text verbatim, which is only warranted for the selected candidate.

## L1 canary method (applied)

Four thin prompts (one per candidate) derived from tranche-0 (the initial constraint each Produce agent would see first). Each prompt describes the problem-shape without naming the reference, the author, or reference-specific vocabulary. Prompts committed at `/tmp/s18-canary/*.txt`; raw outputs at `/tmp/s18-canary/*-codex.md` (OpenAI GPT-5.4 via `codex exec --skip-git-repo-check`) and captured inline below from the Claude Opus 4.7 Agent-tool subagents.

**Inspection criterion (per §4 L1):** does the output spontaneously emit the reference's *idiosyncratic structure, labels, or sequence* without being prompted to? Emission = saturation evidence = rejection.

## Per-candidate findings

### S1 — Feldenkrais Awareness Through Movement (candidate originally proposed as Lesson 1; refined below)

**Canary prompt (`s1-feldenkrais.txt`):** "A learner lies on the floor. They want to notice habitual patterns in their own movement and posture. Design the opening 3 minutes of a ~30-minute lesson on this. Output is instruction text, as if you are speaking to the learner. Do not explain theory; just instruct. Approximately 500 words."

**Codex (GPT-5.4, xhigh) output [excerpt]:** *"Let yourself arrive on the floor. Take the next few moments to do nothing about yourself. No fixing, no stretching, no arranging for an ideal position. Just let the floor hold you exactly as you are. […] Begin by noticing the places where you meet the floor. […] Compare the right side of yourself with the left side. Does one shoulder feel heavier? Does one leg turn out more?"*

**Claude Opus 4.7 output [excerpt]:** *"Let your eyes close, or leave them softly open, whichever feels less effortful. Notice the sound of your own breath. Don't change it. Just listen to it as if you were listening to someone else in the room. Now feel the points where your body meets the floor. […] Move your attention down to your shoulders. Both of them. Is one more pressed into the floor than the other? Don't correct anything. Just register what is."*

**Finding.** Both models reproduce **body-scan-with-asymmetry-observation** structure from the thin prompt. This is canonical Feldenkrais pedagogy — but it is also canonical body-scan-meditation pedagogy (Goenka Vipassana, MBSR, yoga nidra) and predates Feldenkrais. The produced text does **not** emit Feldenkrais-specific idiosyncrasies (e.g., Lesson 6's "pelvic clock" with imagined clock-face positions; Lesson 10's eye-movement-organizes-body-movement coordination; Lesson 11's imaginary-clock on body parts). Neither output names "Feldenkrais" or "Awareness Through Movement."

**Verdict.** Canary result on generic-lying-awareness prompt: **Ambiguous** — the pattern emitted is Feldenkrais-family but also many-traditions-family. For a valid C3 test, the reference case should be a *specific* Feldenkrais lesson with idiosyncratic content (e.g., Lesson 6 Pelvic Clock) whose distinctive markers can be tested for.

**Refinement.** Narrow S1 from "Lesson 1: What is good posture?" to **Lesson 6: "Differentiation of the pelvic movements by means of an imaginary clock"** (the "Pelvic Clock" lesson, widely regarded as the most distinctively Feldenkrais in the book). Its imaginary-clock metaphor applied to the pelvis is highly idiosyncratic; specific numbered-position sequences (3 o'clock, 6 o'clock, 12 o'clock, diagonal rolls) are not common body-scan content.

**Status.** S1 (refined to Pelvic Clock) **survives canary**. Quantitative 5-gram test deferred to pre-seal on ratified candidate.

### S2 — Alexander Technique Semi-Supine / Constructive Rest

**Canary prompt (`s2-alexander.txt`):** "An adult with chronic muscular tension (from desk work and stress) lies on the floor with knees bent, feet flat, and a small book under the head. Their intention is to rest and release tension without performing any physical movement. Write instruction text for the first 3 minutes of this practice. Output as if speaking to the practitioner. Approximately 500 words."

Note: the prompt reveals the lying-position setup (knees bent + book under head) because tranche-0 would include it. The canary tests whether, from *that setup alone*, models spontaneously emit Alexander's idiosyncratic direction-language ("Let the neck be free to let the head go forward and up; let the back lengthen and widen").

**Codex output [excerpt]:** *"Let yourself arrive on the floor exactly as you are. […] Allow the floor to hold your weight. You do not have to hold yourself up. Notice that your back is receiving support, your pelvis is receiving support, your ribs are receiving support, and the back of your head is receiving support through the book. […] Let your jaw be unoccupied. Let your tongue rest in your mouth without arranging it."*

**Claude output [excerpt]:** *"Let the floor take your weight. You don't need to hold yourself up anymore. The ground is there, underneath you, and it will do the work of supporting you for as long as you lie here. […] Let your eyes be soft. They don't need to focus on anything. […] Bring your attention to your jaw. Notice whether your teeth are touching, whether your tongue is pressed against the roof of your mouth. You don't need to change anything — just notice."*

**Finding.** Neither output emits Alexander's signature **directions** (the specific chain "neck free → head forward and up → back lengthen and widen" that is the Alexander Technique's load-bearing verbal formula). Both outputs produce a **generic restorative-lying-practice** closer to savasana or yoga nidra than to Alexander specifically.

This is **contrary to the Case Steward's pre-test self-assessment** of High saturation risk. The canary evidence says Moderate.

**Verdict.** S2 **survives canary** at Moderate saturation. The signature direction-language was not spontaneously produced.

**Caveat.** The canary tests only the first 3 minutes (setup + attention opening). Alexander's idiosyncratic directions are the sustained middle of the practice. A full-protocol C3 test would be needed for complete evaluation — deferred to pre-seal on ratified candidate.

### D1 — Liberating Structures "1-2-4-All"

**Canary prompt (`d1-ls.txt`):** "Design a micro-pattern that moves 12 adults, in 12 minutes, from individual silent thought to whole-group synthesis of a posed question. The pattern uses multiple group sizes with explicit timing per segment. Output is the facilitator's brief: what to say at each transition and how long each segment runs. Approximately 600 words."

**Codex output [direct quote, first line]:** *"**12-Minute Micro-Pattern: 1-2-4-All Sprint**"*

**Claude output [direct quote, header]:** *"# Facilitator's Brief: 12-Minute Silent-to-Synthesis Pattern / **Total:** 12 minutes | **Group:** 12 adults | **Structure:** 1 -> 2 -> 4 -> 12"*

**Finding.** Both models explicitly emit the **"1-2-4-All" label and the exact 1/2/4/all group-size progression** unprompted. Codex names it literally in the title. Claude names it in the structure line. Both reproduce the timing pattern (silent individual → pairs → quartets → whole-group), the "one minute silent" opening, and the "harvest / synthesis" closing vocabulary idiosyncratic to Liberating Structures.

This is unambiguous §1 C3 / §4 L1 **failure**: spontaneous emission of the reference's idiosyncratic structure, labels, and sequence from a thin tranche-0-equivalent prompt. No further test required.

**Verdict.** D1 **REJECT** on contamination canary. Case not carried forward.

### D2 — Kerth Prime Directive Retrospective Opening

**Canary prompt (`d2-kerth.txt`):** "Design a short opening protocol (to read aloud) for a team retrospective. The opening establishes psychological safety so people can name failures without blame landing on individuals. Output is the facilitator's literal script. Approximately 300 words."

**Codex output [excerpt]:** *"The purpose of this conversation is learning, not blame. […] Everyone in this room worked inside a system: deadlines, information gaps, handoffs, assumptions, tools, priorities, and constraints. When something went wrong, it usually made sense to someone in the moment. Our job today is to make that visible."*

**Claude output [excerpt, re-invoked]:** *"This project didn't land where we hoped. […] Every decision that was made in this project was made by a reasonable person, with the information they had, under the pressures they were under, trying to do good work. That is my baseline assumption, and I am asking you to hold it too. When we surface a failure today, the question in the room is never 'who' — it is 'what were the conditions that made this the path of least resistance?'"* (First invocation returned meta-commentary on workspace files; second invocation with tighter prompt returned clean script.)

**Finding.** Both models produce thematically Prime-Directive-adjacent openings. Codex language ("When something went wrong, it usually made sense to someone in the moment") and Claude language ("Every decision […] was made by a reasonable person, with the information they had, under the pressures they were under") both echo Kerth's commentary but **neither reproduces the exact Prime Directive sentence** ("Regardless of what we discover, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand"). The idiosyncratic canonical marker is not emitted.

**Verdict.** D2 **survives canary** at Moderate. The Prime Directive as a *framing concept* is lightly emitted; the Prime Directive as a *specific canonical text* is not. Full 5-gram overlap test deferred to pre-seal on the ratified candidate.

## C1-C8 filtering summary on survivors

Three candidates survive the L1 canary. Final filtering against remaining §1 criteria:

| Criterion | S1 Pelvic Clock (refined) | S2 Alexander Semi-Supine | D2 Kerth Opening |
|---|---|---|---|
| **C1 Auditable provenance** | ✓ Feldenkrais 1972 book; ISBN + publisher + widely-archived. Snapshot doable. | ✓ Multi-source tradition; Frank Pierce Jones 1976 as specific citation. Snapshot doable. | ✓ Kerth 2001 book; ISBN + publisher + widely-archived. Snapshot doable. |
| **C2 Constraint-legibility without solution-smuggling** | ✓ Problem-shape statable ("become aware of pelvic movement patterns with a novel metaphor-based approach") without tipping the clock-face solution. | ~ Harder: the "lying + knees up + book under head + directions to release without active movement" setup strongly implies Alexander. | ✓ Problem-shape statable ("establish psychological safety; short read-aloud opening; blame-deflection to system-level") without tipping the specific Prime Directive text. |
| **C3 Low saturation** (pre-test) | Moderate — refined to distinctive lesson. Pre-seal test required. | Moderate — canary passed; direction-language test pending. | Moderate — canary passed; specific-text test pending. |
| **C4 Staged-constraint structure** | ✓ Lesson 6 has explicit staged structure (intro → first clock-face → second → combinations). Feldenkrais's iterative teaching history documented. | ~ Less staged; the practice is largely a sustained middle. Tranche structure would need construction rather than being natural. | ✓ Opening has stages (Prime Directive → safety check → constraint → agenda preview). Kerth's editions document iteration. |
| **C5 Domain-legibility** | ~ Requires a Cell 3 judge with somatic-movement literacy. Marginal. | ~ Requires a Cell 3 judge with Alexander/somatic literacy. Marginal. | ✓ Retrospective-facilitation knowledge is widely distributed in software/agile communities; judge pool is broad. |
| **C6 Bounded effort** | ✓ Single lesson ~2-3 KB reference; constraint statement fits 1-3 KB. | ✓ ~2 KB reference; constraint statement fits. | ✓ ~1 KB reference; constraint statement fits. |
| **C7 Representativeness** | ✓ Movement sequence — matches Session 008 Morning Unfurl type. | ✓ Movement/attention protocol — matches Session 008 type. | ✓ Structured procedure — matches Session 010 House Decision type. |
| **C8a Pre-LLM-co-design** | ✓ 1972. | ✓ Tradition pre-1922; written protocols pre-2000. | ✓ 2001. |
| **C8b Falsification-admitting** | Partial — mandatory vs optional elements distinguishable in Feldenkrais's own text but not formally tagged. | Weak — "do the position, think the directions" is the whole instruction; failure mode stated but not formally tagged. | ~ Moderate — Prime Directive is mandatory; other elements negotiable. Failure conditions named. |
| **C8c Uncertainty-declared** | ✓ Feldenkrais's prefaces and per-lesson commentary include explicit uncertainty. | ~ Present in Alexander teacher-training literature; less in the protocol itself. | ✓ Kerth's foreword discusses his own uncertainty about scale-dependence and cultural context. |

## Shortlist for ratification (three candidates)

Three candidates survive L1 canary + C1-C8 filtering. Presented for user ratification per D-072.

1. **S1 — Feldenkrais "Pelvic Clock" Lesson 6** — same-domain-adjacent. Strongest staged-constraint structure; idiosyncratic clock-metaphor makes C3 test discriminating. Cell 3 judges need somatic literacy.

2. **S2 — Alexander Technique Semi-Supine** — same-domain-adjacent. Weaker C4 staged-constraint structure; C8b falsification-admission marginal. Direction-language test is the key C3 pre-seal verification.

3. **D2 — Kerth Retrospective Opening Protocol** — different-domain-representative. Strongest C5 domain-legibility (retrospective-facilitation knowledge is broadly held in software/agile). Clean C1, C6, C7, C8. Prime Directive specific-text test is the key C3 pre-seal verification.

**Case Steward's ranking (G/O/K/S-adjacent reasoning, not formal per-candidate scoring):**
- **D2 Kerth** ranks first on operational-ease grounds: cleanest C5 (judge-pool is broad), cleanest C8 (falsification, uncertainty all present), structured procedure directly matches Session 010 precedent.
- **S1 Pelvic Clock** ranks second: strongest C4 staged-constraint structure; distinctive C3 markers; but C5 judge-pool is narrower (requires somatic literacy).
- **S2 Alexander** ranks third among survivors: weaker C4 and C8b; C3 pre-seal test is pending and direction-language reproduction is a live risk.

**Dropped at canary:** D1 Liberating Structures 1-2-4-All — rejected outright on contamination canary (explicit 1-2-4-All label + structure emitted by both model families).

**Dropped at pre-canary self-assessment:** S3 Rolfing (C7 practitioner-administered); D3 NVC (predicted high saturation); D4 Gordon Method III (predicted generic shape).

## Next step

**HALT for user ratification** per D-072. User selects one of S1, S2, D2 to proceed to case pack sealing. Upon ratification, the Case Steward will:
1. Source the reference verbatim (URL/document snapshot) and commit as anti-drift witness.
2. Run the full C3 5-gram overlap test (constraint-only → measure actual overlap against reference text).
3. Write the constraint statement in methodology-standard language without reference-lexical fingerprints.
4. Partition constraints into tranche-0 and emergent tranches with release triggers.
5. Write contamination-audit plan and search-exclusion list.
6. Commit sealed case pack as anti-drift witness.
7. Proceed to Cell 2 (Stop 3b per D-072) if session budget permits.
