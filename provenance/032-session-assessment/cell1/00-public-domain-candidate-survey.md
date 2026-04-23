---
session: 032
title: Cell 1 Public-Domain Candidate Survey — Selection of Reference Case for L1a + L1b Saturation Test
date: 2026-04-23
status: complete
cell: 1
step: pd-candidate-survey
case_steward: Claude Opus 4.7 (orchestrating agent; L2 limitation per Session 018 D-076 carries forward)
---

# Cell 1 · Step 1 — Public-Domain Candidate Survey

## §1 Purpose and operator constraint

Per operator session-open input, Session 032 Path C-fresh executes Cell 1 with a candidate from outside the Session 018 pool, restricted to **public-domain references** (operator cannot provide copyrighted reference text per Session 031 D-102 sealing-deferred condition).

Per `reference-validation.md` v2 §1, a candidate must satisfy all eight criteria C1–C8. Per Session 018 cell1/00-candidate-survey.md precedent ([archive: provenance/018-reference-validation-exercise-1/03-close.md]), the survey enumerates 4–7 candidates, marks rejected-pre-test cases, and selects 1–2 for formal evaluation (L1a canary then L1b saturation).

**Operator constraint narrows but does not weaken the C1–C8 standard.** PD constraint guarantees C1 (auditable provenance via authoritative archives) and C8a (pre-LLM-co-design, since PD works are by construction pre-2022). The PD constraint **structurally elevates C3 saturation risk** because PD works are typically more heavily represented in language-model pretraining corpora than copyrighted works (free inclusion in training data; longer accumulation horizon for derivative quotations). The survey must navigate this tension via (a) selecting an obscure procedural sub-unit within a moderately-known PD source, or (b) selecting a procedure where constraint-set naturally over-determines structure regardless of saturation, or (c) selecting a procedure in a domain whose PD-canonical works are less popularly cited than the Western literary canon.

## §2 Candidate enumeration

Six candidates surveyed against C1–C8. Domain coverage spans community-admission-procedure (PD-A), classical-architecture-procedure (PD-B), classical-medicine-recipe-procedure (PD-C), Victorian-nursing-procedure (PD-D), early-20th-century-emergency-resuscitation-procedure (PD-E), and pre-1929-classical-physical-training-procedure (PD-F).

| ID | Candidate | Source | Domain | C3 risk (self-assessed) | C7 shape |
|----|-----------|--------|--------|-------------------------|----------|
| PD-A | Rule of St. Benedict Ch 58 "Of the Discipline of Receiving Brothers" | Latin original ~530 CE; Cardinal Gasquet 1909 English / Hunter Blair 1886 English (both PD) | Hierarchical-community admission procedure | Moderate | Decision-aid + sequenced procedure with binding ceremony |
| PD-B | Vitruvius Book I Ch 4 "Site Selection for Walled Cities" | Latin original ~25 BCE; Morgan 1914 English (PD) | Town-planning site-selection procedure | Moderate | Decision-aid (multi-criterion site evaluation) |
| PD-C | Hippocrates "Regimen in Acute Diseases" Ch 11 "Preparation of Ptisan" | Greek original ~400 BCE; Adams 1849 English (PD) | Classical medicine therapeutic-recipe procedure | Low-Moderate | Recipe procedure (preparation sequence) |
| PD-D | Florence Nightingale Notes on Nursing Ch 13 "Observation of the Sick" | Nightingale 1859 English (PD) | Bedside-observation procedure for nurses | Moderate | Sequenced observation procedure with decision-aid elements |
| PD-E | American Red Cross First Aid Text-Book (Lynch/Pilcher 1913) "Schaefer Prone-Pressure Method for Drowning Resuscitation" | Lynch 1913 English (US-PD; American Red Cross publication) | Emergency resuscitation procedure (now-obsolete pre-CPR) | Low | Sequenced emergency-action procedure |
| PD-F | Galen "On Exercise with the Small Ball" (de parvae pilae exercitio) | Greek original ~180 CE; Singer 1956 English NOT PD; older PD English translations exist (Brock 1916 / others) | Classical exercise procedure | Low | Exercise sequence with prescriptive elements |

## §3 Per-candidate assessment

### §3.PD-A — Rule of St. Benedict Ch 58 "Of the Discipline of Receiving Brothers"

**Source provenance.** Latin Rule of St. Benedict (Regula Sancti Benedicti) composed approximately 530 CE by Benedict of Nursia. Multiple PD English translations: Cardinal Aidan Gasquet (1909), Rev. D. Oswald Hunter Blair OSB (1886), and the Burns & Oates anonymous translation (1875). Latin original is also PD.

**Procedure description.** Chapter 58 specifies the procedure for admitting a new permanent member ("brother") to a Benedictine monastic community. The procedure includes: persistent knocking and being initially refused to test resolve; admission as a guest; transfer to the novitiate house under a senior monk's tutelage; periodic readings of the Rule at 2 months, 6 more months, and 4 more additional months (totaling 12 months); after each reading, the explicit offer "here is the law under which you wish to serve; if you can observe it, enter; if you cannot, freely depart"; final profession in the oratory with three vows (stability, conversion of life, obedience); written petition placed on the altar; prostration before each member; threefold singing of "Suscipe me, Domine."

**C1 auditable provenance.** ✓ Multiple authoritative PD English translations available on archive.org and Project Gutenberg. Latin original on multiple authoritative classical archives (e.g., Bibliotheca Augustana, The Latin Library).

**C2 constraint-legibility without solution-smuggling.** Achievable: the constraint set can describe "permanent-membership admission for a hierarchical community where the membership decision is irreversible and community success depends on member fit" without naming monastery, Benedictine, novice, abbot, oratory, or any procedural keyword.

**C3 low-saturation.** Self-assessed **Moderate**. RoSB is famous as a *concept* but specific Ch 58 procedural details (4 days at gate; 12-month novitiate divided 2/6/4; threefold Rule reading; "Suscipe me, Domine" formula) are less heavily quoted in popular pretraining corpora than e.g. the Hippocratic Oath or the Lord's Prayer. The risk is that L1b might surface generic monastic-tradition memory if the constraint statement signals "religious community" — careful constraint framing must hold the problem at the abstraction "permanent-membership-irreversible-community-fit-hierarchical" without religious vocabulary.

**C4 staged-constraint structure.** Strong: tranche-0 can describe "design admission process for hierarchical permanent-membership community"; tranche-1 can release "process must test resolve before commitment" and "process must allow graceful exit"; tranche-2 can release "process must demonstrate teaching content before final commitment" and "process must culminate in binding ceremony." Each release is methodology-internal-trigger-tied.

**C5 domain-legibility to validators.** Strong: hierarchical-community-admission procedures are universally legible (parallels to clubs, professional bodies, religious orders, military commissioning, citizenship). Cross-family validators (codex/Claude) can reason about admission-procedure structure without specialised expertise.

**C6 bounded effort.** Strong: Chapter 58 in the Hunter Blair 1886 English translation is approximately 700–900 words; constraint statement fits well within 1–3 KB.

**C7 representativeness.** Strong: decision-aid + sequenced-procedure + binding-ceremony hybrid maps directly to engine claim shapes. Adjacent to House Decision in Five Moves (decision aid for permanent action) and to Morning Unfurl (sequenced procedure). Distinct from any prior-tested domain (Session 018 pool was movement/somatic + facilitation/decision-aid; Session 032 PD-A is community-admission, structurally novel).

**C8a pre-LLM-co-design.** ✓ Authored ~530 CE; English translations 1886 and 1909.

**C8b falsification-admitting.** Strong: Chapter 58 carries explicit pass/fail criteria — the candidate "is to be sent away" if they refuse to accept the Rule; the threefold-reading-with-explicit-offer mechanism is a structured falsification pathway; the specific time intervals (2/6/4 months) are quantitatively falsifiable.

**C8c uncertainty-declared.** Moderate: the Rule's prologue contains explicit acknowledgement that the Rule is "a little Rule for beginners" and that "those who would hasten to the perfection of monastic life" must consult further authorities (Cassian, Basil) — explicit author-uncertainty about the Rule's sufficiency. Chapter 58 itself does not internally flag uncertainty in its specific provisions, but the corpus-level uncertainty-declaration carries.

**Summary.** Strong candidate across all eight criteria. Primary risk: C3 saturation if constraint framing inadvertently signals religious-community context.

### §3.PD-B — Vitruvius Book I Ch 4 "Site Selection for Walled Cities"

**Source provenance.** *De Architectura* by Marcus Vitruvius Pollio, ~25 BCE; Morgan 1914 English translation (Harvard University Press, PD).

**Procedure description.** Site-selection procedure for a Roman walled city: choose elevated ground avoiding marshes; check prevailing winds (the eight-wind enumeration governs orientation); examine grazing-animal livers to assess local salubrity; verify water sources; assess stone and timber availability; orient streets to avoid prevailing-wind alleys.

**C1 auditable provenance.** ✓ Morgan 1914 English on archive.org and Project Gutenberg.

**C2 constraint-legibility without solution-smuggling.** Achievable: "design site-selection procedure for permanent settlement of ~10,000 inhabitants without modern instruments" sets the problem-shape.

**C3 low-saturation.** Self-assessed **Moderate**. Vitruvius is famous as a foundational architectural text and is taught in architectural pretraining; the specific Book I Ch 4 site-selection procedure with eight-wind orientation and animal-divination component is moderately documented but the specific arbitrary count (eight winds; specific compass orientations) and non-obvious decision-elements (liver inspection) may surface.

**C4 staged-constraint structure.** Strong: the constraint set partitions naturally into geographic-physical (tranche-0: elevation, water, materials), atmospheric (tranche-1: winds, climate), and biological-empirical (tranche-2: grazing-animal divination) tranches.

**C5 domain-legibility.** Moderate-Strong: site-selection is broadly understood; specific Roman cosmological elements (eight winds, augury) are less universally legible.

**C6 bounded effort.** Strong: Book I Ch 4 is approximately 600 words.

**C7 representativeness.** Strong: decision-aid for siting/placement (parallel to House Decision in Five Moves).

**C8a pre-LLM-co-design.** ✓.

**C8b falsification-admitting.** Strong: specific quantitative recommendations (orientation by named winds; liver-color inspection criteria); explicit failure modes (a marshy site → disease).

**C8c uncertainty-declared.** Moderate: Vitruvius's preface acknowledges the synoptic-not-exhaustive scope; Ch 4 itself is prescriptive without much explicit uncertainty.

**Summary.** Strong candidate. Slightly lower C5 score than PD-A due to Roman-cosmological vocabulary; slightly higher C3 risk due to architectural-canon prominence.

### §3.PD-C — Hippocrates "Regimen in Acute Diseases" Ch 11 "Preparation of Ptisan"

**Source provenance.** Hippocratic Corpus *De Diaeta in Morbis Acutis* ~400 BCE; Adams 1849 English translation (PD; Sydenham Society).

**Procedure description.** Preparation procedure for ptisan (barley gruel): selection of barley grade; soaking duration; cooking water proportion; boiling duration; thickening criteria; salt and honey additions per patient state; consistency assessment.

**C1 auditable provenance.** ✓ Adams 1849 on archive.org.

**C2 constraint-legibility.** Achievable: "design preparation procedure for a therapeutic gruel for fever-convalescent patients in a pre-modern kitchen."

**C3 low-saturation.** Self-assessed **Low**. Hippocratic Corpus is famous in medical history but ptisan-preparation specifically is genuinely obscure even among Hippocrates readers; few popular sources reproduce the recipe in detail.

**C4 staged-constraint structure.** Moderate: ingredient-selection / cooking-method / patient-state-adaptation tranches.

**C5 domain-legibility.** Strong: cooking-procedure is universally understood; therapeutic-gruel preparation is a clear physical-chemical procedure.

**C6 bounded effort.** Strong: Ch 11 is approximately 400–600 words.

**C7 representativeness.** Moderate: recipe-procedure is structurally similar to Morning Unfurl (sequenced action) but more linear (less decision-tree). The engine has not produced a recipe-shaped artefact previously; this would extend the artefact-type breadth (per §6 methodology-pass-criteria coverage requirement).

**C8a pre-LLM-co-design.** ✓.

**C8b falsification-admitting.** Strong: specific consistency criteria; specific patient-response criteria; named adjustments for named symptoms.

**C8c uncertainty-declared.** Moderate-Strong: Hippocratic style explicitly reasons about exceptions and patient variation throughout; Adams 1849 preface is methodologically uncertain about specific identifications.

**Summary.** Strong candidate; lowest C3 risk in pool. Primary concern: C7 shape is recipe (linear) rather than decision-aid (branching), narrowing methodological evidence breadth relative to PD-A.

### §3.PD-D — Florence Nightingale Notes on Nursing Ch 13 "Observation of the Sick"

**Source provenance.** Nightingale 1859 English (PD; multiple editions on archive.org and Project Gutenberg).

**Procedure description.** Procedure for systematic observation of bedside-patient state by a nurse: note distinguishing features (pulse, skin, breathing); note diet/intake/output; note bedclothes and surrounds; sequence observations over time to detect change; interpret deviations from baseline; record observations for the visiting physician.

**C1 auditable provenance.** ✓.

**C2 constraint-legibility.** Achievable.

**C3 low-saturation.** Self-assessed **Moderate**. Nightingale's *Notes on Nursing* is famous as a foundational nursing text; specific observational sequences and her aphoristic style are moderately reproduced.

**C4 staged-constraint structure.** Strong: physical-observation / temporal-sequencing / interpretive / recording tranches.

**C5 domain-legibility.** Strong: bedside-nursing observation is universally understood as a procedure-domain.

**C6 bounded effort.** Strong (Ch 13 approximately 1,200–1,800 words; selectable sub-section under 1,000).

**C7 representativeness.** Strong: sequenced-observation-procedure with decision-aid components.

**C8a pre-LLM-co-design.** ✓.

**C8b falsification-admitting.** Moderate-Strong: explicit recommendations with implied failure modes.

**C8c uncertainty-declared.** Strong: Nightingale's prefaces and asides explicitly address her own uncertainty and the limits of her experience.

**Summary.** Strong candidate. Slightly higher C3 saturation risk than PD-A due to Nightingale's wider quotability.

### §3.PD-E — American Red Cross First Aid Text-Book "Schaefer Prone-Pressure Method for Drowning Resuscitation"

**Source provenance.** *American Red Cross Text-Book on First Aid* by Major Charles Lynch, 1913 (US-PD; American Red Cross was a federal-charter quasi-governmental publication; pre-1929 publication in any case).

**Procedure description.** Schaefer prone-pressure resuscitation method: position victim prone with head turned; rescuer kneels astride victim's hips; rescuer places palms on victim's lower thoracic vertebrae; rescuer rocks forward applying full body weight every 4–5 seconds and rocks back to release; continue for at least one hour or until victim revives or is pronounced.

**C1 auditable provenance.** ✓ Lynch 1913 on archive.org.

**C2 constraint-legibility.** Achievable; constraint must specify pre-modern-medical-equipment context to push toward Schaefer-era response.

**C3 low-saturation.** Self-assessed **Low**. Schaefer prone-pressure is genuinely obsolete (replaced by Holger-Nielsen back-pressure 1932, then mouth-to-mouth 1956, then CPR 1960). Modern AI training corpora are dominated by current CPR procedures, not Schaefer. L1b would very likely produce modern-CPR-shaped output rather than Schaefer.

**C4 staged-constraint structure.** Moderate: positioning / pressure-mechanics / timing tranches.

**C5 domain-legibility.** Strong: emergency resuscitation is universally legible.

**C6 bounded effort.** Strong (Schaefer description in Lynch 1913 is approximately 300–500 words).

**C7 representativeness.** Strong: sequenced-emergency-action-procedure with falsification.

**C8a pre-LLM-co-design.** ✓.

**C8b falsification-admitting.** Strong: specific positioning, specific pressure cycles, specific timing, specific durations; explicit failure mode (death).

**C8c uncertainty-declared.** Moderate: Lynch 1913 acknowledges variability in patient response.

**Summary.** Lowest C3 saturation risk in pool BUT this creates a *test-design problem*: if Cell 2 produces modern CPR (because constraint cannot avoid signalling "drowning resuscitation") and the reference is Schaefer, structural-correspondence will be low not because of methodology failure but because the constraints underdetermine the era. The L1b PASS would be near-certain (modern CPR is not Schaefer); the Cell 3 verdict would likely be Fail-methodology-gap due to era-mismatch even though the methodology operated correctly. **This breaks the validation logic** of L1b PASS → useful Cell 2/3 evidence. Disqualifying for the present session.

### §3.PD-F — Galen "On Exercise with the Small Ball"

**Source provenance.** Galen *de parvae pilae exercitio* ~180 CE. PD English translations exist in older editions (e.g., Brock 1916 *Galen on the Natural Faculties* PD; specific translation of *de parvae pilae* in pre-1929 medical-history compilations); operator may need to confirm the specific PD English version exists on archive.org.

**Procedure description.** Galen advocates handball as superior exercise; details: posture, ball handling, pace variation, rest cycles, integration with other exercise.

**C1 auditable provenance.** ✓ pending PD-translation confirmation.

**C2 constraint-legibility.** Achievable but the text is partly rhetorical-encomium rather than purely-procedural.

**C3 low-saturation.** Self-assessed **Low**. Galen is famous in medical history but this specific text is among his more obscure.

**C4 staged-constraint structure.** Weak: text is more discursive than tranchable.

**C5 domain-legibility.** Strong.

**C6 bounded effort.** Strong (text is short, ~2,000 words total).

**C7 representativeness.** Moderate-Weak: more advocacy than prescriptive procedure.

**C8a/b/c.** ✓ / Moderate / Moderate.

**Summary.** Genuinely low C3 risk but C7 representativeness is weak (text is rhetorical advocacy, not prescriptive procedure with falsification). Disfavoured.

## §4 Selection

**Selected: PD-A — Rule of St. Benedict Chapter 58 "Of the Discipline of Receiving Brothers"** (Cardinal Gasquet 1909 English translation OR Hunter Blair 1886 English translation, whichever is reliably available on archive.org at fetch time).

**Rationale.**

1. **Best balance across C1–C8.** PD-A is strong on all eight criteria; only PD-C and PD-E score lower on C3 (saturation), but PD-E breaks the validation logic via era-mismatch and PD-C narrows artefact-type breadth.

2. **C7 representativeness extends engine claim.** PD-A is decision-aid + sequenced procedure + binding ceremony; this hybrid shape extends the methodology's external-artefact pool (Morning Unfurl is pure sequence; House Decision is pure decision-aid; PD-A combines both with a ceremonial-commitment terminus). A successful run would generate evidence for the methodology's hybrid-artefact capability that prior runs do not establish.

3. **Domain structurally distinct from D2 (agile-retrospective) AND from S1 (movement/somatic).** Per `reference-validation.md` v2 §9 trigger 7 framing, "structurally-different-domain" is the salient axis. PD-A is in the **community-admission-and-binding-commitment** domain — distinct from both Session 018 D2 (agile-retrospective facilitation) and Session 031 S1 (somatic-movement). If PD-A rejects at L1b in this third structurally-different domain, that would extend the §9 trigger 7 pattern (counter would advance to 2-of-2 and trigger 7 fires); if PD-A passes, it provides the *first* L1b PASS in a non-Session-018-pool domain.

4. **Rejected alternatives preserved with rationale** for forward audit (§3.PD-B/C/D/E/F above). Operator may direct revisitation in Session 033+ if PD-A rejects.

5. **PD source text fetchable in-session.** Cardinal Gasquet 1909 and Hunter Blair 1886 are both on archive.org with full page images and OCR text. WebFetch in §5e of `00-assessment.md` will commit byte-identical text to `cell1/reference-envelope/01-source-text.md` with SHA-256 anti-drift witness.

**Single-candidate evaluation matches Session 031 precedent and bounded session scope.** Session 031 tested one candidate at L1b (S1) per Cell 1 single-session shape; Session 032 follows the same shape with PD-A.

## §5 Predicted L1b risk for PD-A

Per Session 018 precedent (D2 ~94% overlap; verbatim heading reproduction in Claude family) and Session 031 precedent (S1 PASS with genre-saturation observation), the predicted L1b outcome for PD-A is:

- **Most likely**: PASS on all three §1 C3 Stage (b) rejection conditions (overlap; verbatim distinctive phrase; cross-family asymmetry), with a Session-031-style genre-saturation observation if the constraint statement inadvertently activates "religious-community" / "monastic" / "membership-rite" priors. The constraint statement (next file) will be drafted to hold abstraction at "hierarchical-permanent-membership-community-with-irreversible-decisions-and-time-bounded-evaluation" without religious-vocabulary triggers.
- **Plausible**: REJECT at condition 2 (verbatim distinctive phrase) if either model spontaneously emits "Suscipe me, Domine" / "Rule of St. Benedict" / "novice" / "abbot" / "twelve months" + "two months" + "six months" + "four months" specific intervals / "stability obedience conversion" three-vow formula. Mechanical grep audit (per Session 031 §2b protocol) will check for these markers exhaustively.
- **Plausible**: REJECT at condition 3 (cross-family retrieval asymmetry) if Claude family produces RoSB-shaped output while codex produces from-scratch (or vice versa, less likely given Claude's higher-density Western religious-canon training).
- **Unlikely**: REJECT at condition 1 (>30% 5-gram overlap) without conditions 2 or 3 also firing — overlap-without-distinctive-phrase emission would suggest paraphrase saturation, possible but uncommon for procedural texts.

If REJECT, §9 trigger 7 fires (n=2 structurally-different-domain rejection: D2 agile-retrospective + PD-A community-admission). Per Session 031 close §4c counter state, this advances trigger 7 from 1-of-2 to 2-of-2 = activated. Trigger 7 activation requires:
- Activate Session 014 Skeptic "provisional substitute" minority warrant as required kernel §7 revision consideration in next session (Session 033).
- Re-open OI-016 to Open state pending that consideration.
- Make saturation-gate false-negative pattern observable as pattern.

Session 032 records the trigger-counter advance in D-105 if REJECT; does not propose kernel §7 revision in-session (anti-laundering: do not retrofit spec in same session that surfaces pattern).

If PASS, sealing proceeds in-session per §5e of `00-assessment.md`.

## §6 Honest limits at this step

- **L2 orchestrating-agent-Case-Steward contamination flag carries forward** from Session 018 D-076 and Session 031 §4. The Case Steward (Claude Opus 4.7 orchestrating agent) has Western-religious-canon pretraining including RoSB at high density. This is acknowledged residual-risk; mitigations apply per Session 031 (grep mechanical audit; codex cross-family evidence; Session 018/031 precedent invoked).

- **5-gram overlap mechanical computation pending sealed reference text.** Per Session 031 §4 limitation, in-session 5-gram computation is qualitative (distinctive-phrase detection; structural correspondence) not mechanical-quantitative until sealed reference text is committed. PD-A's PASS-track sealing in §5e will commit byte-identical reference text from PD source, enabling subsequent mechanical 5-gram computation in Cell 3 (Session 033+).

- **Multiple PD English translations exist for RoSB.** Cardinal Gasquet 1909 and Hunter Blair 1886 are both authoritative; comparison should use one canonical translation as the reference. Session 032 commits to the more reliably-archive-org-fetchable of the two; if both fetch successfully, the older Hunter Blair 1886 is preferred (longer PD horizon; closer to scholarly consensus on faithful Latin rendering).

- **Latin original is also PD.** The Latin Regula Sancti Benedicti is on the Latin Library and Bibliotheca Augustana. For L1b purposes, the **English translation** is the operative reference because L1b tests whether models reproduce the *English* lexical surface — Latin reproduction is a different (and likely less probable) attack surface. Session 032 uses English translation; Latin original is a fallback comparison point.

- **C3 saturation framing risk.** The candidate survey explicitly named "religious community" and "monastic" in PD-A description above; the L1b constraint statement (next file) will scrupulously avoid these triggers, framing the problem as "permanent-membership-community-with-irreversible-decision-process." If Cell 2 / Cell 3 in Session 033+ require the constraint statement to be re-tightened, the operator-facing Cell 1 work this session is the iteration-zero commit.

- **No PD-A operator pre-ratification.** Per Session 031 precedent (operator ratified Path C; Case Steward selected S1; no further operator ratification halt). Session 032 operator ratified Path C-fresh with PD constraint; Case Steward selected PD-A. If operator wishes to redirect to PD-B/C/D/F (or to a candidate not in this survey), Session 033+ may execute the alternative; Session 032's PD-A L1b verdict stands as evidence for PD-A specifically.

## §7 Next step

Proceed to `cell1/01-constraint-statement.md` (draft the problem-shape constraint with religious-vocabulary-fingerprint-removal discipline), then `cell1/constraint-prompt.txt` (plain-text version for codex invocation), then L1a thin-prompt canary (`cell1/02a-l1a-canary-verdict.md`), then L1b full-constraint saturation test (raw outputs + verdict), then sealing if PASS.
