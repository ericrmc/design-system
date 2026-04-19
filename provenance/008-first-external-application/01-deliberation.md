---
session: 008
title: Deliberation — First External Application Target Selection (synthesized)
date: 2026-04-19
status: complete
synthesizer: session-008 orchestrating agent (Claude Opus 4.7, same model family as 3 of 4 deliberators; not the Outsider's model family)
synthesizer-independence: did not play any of the four perspectives (Explorer, Outsider, Pragmatist, Skeptic)
deliberation-anchor-commit: ddeb5172da8d79ff7c0cc9acaa9a9f2c4d3c2d4a
perspective-order: alphabetical by role name (Explorer, Outsider, Pragmatist, Skeptic)
participants_family: cross-model
cross_model: true
non_claude_participants: 1
---

# Deliberation — Session 008: First External Application Target Selection

## How This Deliberation Was Conducted

Four perspectives were convened under D-045 Branch B to produce a shortlist and recommended pick for the methodology's first non-self application. Three were parallel context-isolated Claude subagents (Claude Opus 4.7) launched via Claude Code's Agent tool: The Explorer, The Pragmatist, and The Skeptic (required adversarial). The fourth, The Outsider, was a non-Claude participant: OpenAI GPT-5 (model id `gpt-5.4`, OpenAI session id `019da3bb-53c2-7113-8e70-61fe62c953c1`) invoked via the `codex` CLI in non-interactive (`exec`) mode, `sandbox: read-only`, `reasoning effort: xhigh`. All four received the shared brief committed at `ddeb5172da8d79ff7c0cc9acaa9a9f2c4d3c2d4a`. None saw the others' outputs during the independent phase. The Outsider's response is committed verbatim per D-021's transport-faithfulness requirement (banner, prompt echo, primary response, `tokens used` line — 13,391 tokens — and the end-of-stream duplicated response). Raw outputs are preserved at:

- `01a-perspective-explorer.md` (Claude Opus 4.7)
- `01b-perspective-pragmatist.md` (Claude Opus 4.7)
- `01c-perspective-skeptic.md` (Claude Opus 4.7, required adversarial)
- `01d-perspective-outsider.md` (GPT-5 via Codex CLI)

Perspectives are presented alphabetically throughout this synthesis to reduce synthesizer-ordering bias (D-018).

**This is the methodology's fourth heterogeneous-participant deliberation.** Per Session 007 D-049 precedent, target selection does not trigger D-023 (no kernel modification, no spec revision, no OI-004 state change), so non-Claude inclusion is conservative rather than D-023-required; the sustained-practice tally does not advance from this deliberation unless a subsequent Session 008 decision (e.g., a spec-revision forced by Produce-activity findings) triggers D-023.

## Synthesis Conventions

Following D-018 and reaffirmed in Sessions 005, 006, 007: claims attributing a position to a perspective cite the source file and question; claims not directly sourced are marked `[synth]`; load-bearing language is quoted rather than paraphrased; dissent is preserved as dissent; convergence (all perspectives independently reached a similar conclusion) is distinguished from coverage (only one perspective raised a point, others silent). Where the brief's own language has seeded a phrase used by multiple perspectives, the synthesis calls this out rather than treating lexical echo as independent convergence.

**Brief-priming self-check.** Session 008's brief deliberately avoided seeding "load-bearing," "ritual-tracking," "drift-to-ritual," "overdue," and "domain-general" from Session 007's decisions, per the third-consecutive-brief-priming finding documented in the Session 008 assessment. D-046's eight criteria were quoted verbatim; that vocabulary ("bounded scope," "reversibility," "Validate analogue," "mid vocabulary distance," "externally legible," "not pre-shaped by agent," "domain-accessible," "software-adjacency") was shared across perspectives by necessity — the criteria themselves are the analytical structure the brief asked perspectives to apply. Beyond the criterion names, the brief used neutral operational language. Adoption of criterion-names across perspectives is expected and not lexical-echo in the concerning sense; it is shared vocabulary for the shared analytical task.

**New vocabulary coinages across perspectives in this deliberation** (substantive convergence indicators):

- **Document-shape / artefact-shape / representability bias** — coined independently by four perspectives to name the Q5 non-obvious agent bias. Explorer: "artefact-shape bias" / "document-adjacent" [`01a`, Q5]. Pragmatist: "medium bias" / "preference for targets that produce a single primary document" [`01b`, Q5]. Skeptic: "shape of the artefact — textual, structured, author-led, single document produced by a single author for a cooperative reader" [`01c`, Q5]. Outsider: "representability bias" / "the prior that the best first targets are the ones where the whole problem can be turned into text, tables, and rationale without residue" [`01d`, Q5]. No single phrase dominates; four distinct framings of the same underlying finding. **This is the deliberation's strongest four-way convergence and crosses the model-family axis.**

- **Methodology-talk** / **methodology-vocabulary leakage** — used by Pragmatist [`01b`, Q4], Skeptic [`01c`, Q4], and implied by Explorer [`01a`, Q4]. The concept is that the first external artefact should not contain the methodology's own internal vocabulary (specification, deliberation, manifest, trigger) as the load-bearing vocabulary; it should speak the target domain's language.

- **Lived use** / **executability in the body / kitchen / group** — three-of-four perspectives name lived-use as the Validate analogue's stronger form. Explorer (body tries the movement), Outsider (user cooks and eats), Skeptic (group runs the protocol). Pragmatist offers a weaker rule-comparison Validate for training plans, acknowledged explicitly as thinner.

---

## Q1: Candidate Targets — Four Distinct Recommendations, No Convergence on Pick

Each perspective produced three candidates and recommended one. **No two perspectives recommended the same target.** Candidates cluster into four loosely-shaped groups:

**Explorer's candidates** [`01a`, Q1]:
- **A (recommended): Movement / choreography** — a short solo sequence for a named constraint (mobility routine, thirty-second transition, short practice phrase).
- **B: Recipe design** — one dish built around a named constraint.
- **C: Garden / planting bed design** — small plot under stated conditions.

**Outsider's candidates** [`01d`, Q1]:
- **1 (recommended): Household meal-rotation and provisioning protocol** — two-week weekday dinner system (rotation, grocery cadence, prep windows, substitution rules).
- **2: Self-guided reading seminar** — six-week seminar on a user-chosen non-work topic.
- **3: Creative practice package for a user hobby** — four-session assignment ladder and critique sheet (e.g., photography, sketching).

**Pragmatist's candidates** [`01b`, Q1]:
- **A: Personal reading list curation with an argued spine** — 10–15 item list with rationale and spine.
- **B (recommended): Training-plan design** — 8–12 week plan for a named physical goal.
- **C: Household decision-design package** — decision package for a bounded one-off purchase.

**Skeptic's candidates** [`01c`, Q1]:
- **A: Personal reading-and-retention protocol** — reproducible protocol for processing a book or article cluster.
- **B: Recipe / cooking-process design** — menu and preparation sequence under a stated constraint.
- **C (recommended): Small-group governance or dispute-resolution protocol** — written decision protocol for a real interpersonal or small-group situation.

`[synth]` **Aggregate candidate set across perspectives (deduplicated by domain, not by exact problem):**

1. **Movement / choreography** — Explorer-only [A]. Non-document artefact. Lived-use Validate (body attempts).
2. **Household meal-rotation / recipe / menu design** — proposed by three of four perspectives in related forms. Outsider [1], Explorer [B], Pragmatist via rejection, Skeptic [B]. Document-shaped artefact; lived-use Validate (cook and eat).
3. **Training-plan / physical-skill programme** — Pragmatist-only [B]. Document artefact; thick rule-comparison Validate + session-1 coachability.
4. **Reading list / seminar / reading-retention protocol** — proposed by three of four in variations. Pragmatist [A], Outsider [2], Skeptic [A]. Document-shaped; validation via rival-list or comprehension check.
5. **Governance / small-group decision protocol** — Skeptic-only [C]. Document-shaped but domain-vocabulary-distant; thin Validate.
6. **Creative practice / hobby critique package** — Outsider-only [3]. Moderately document-shaped; lived-use Validate (produce work).
7. **Planting bed / garden design** — Explorer-only [C]. Document + diagram; seasonal Validate.
8. **Consumer-decision package** — Pragmatist-only [C]. Document-shaped; reviewer-pass Validate.

**Rejected across perspectives (convergent rejections):**

- **Vault / note-taxonomy / personal-knowledge-system reorganization** — rejected explicitly by Outsider [`01d`, Q5] on representability-bias grounds; rejected implicitly by Skeptic [`01c`, Q5] (personal AI-use policy class). Four-of-four silently reject via criterion 8 (software-adjacency).
- **Policy documents** (personal financial policy, household media policy, AI-use policy) — explicit Skeptic rejection [`01c`, Q5] on document-shape-bias grounds.
- **Fitness / nutrition plans with real health stakes** — Outsider rejects on criterion 2 [`01d`, Q1]; Skeptic rejects physical-training programmes on Validate-timeline grounds [`01c`, Q1]. (Note: Pragmatist accepts training-plan under adult-athlete-judgement caveat, which is the contested position.)
- **Software-topic curricula** — Skeptic explicit rejection [`01c`, Q1]; bound by criterion 8 regardless.
- **Three-variant-of-same-domain shortlists** — all four perspectives honoured the brief's explicit prohibition.

---

## Q2: Recommended Picks — Four Different Picks; Four Distinct Challenging Properties

**No convergence on a single recommended pick.** The four recommendations span:

| Perspective | Pick | Criterion-6 challenging property named |
|---|---|---|
| Explorer | Movement sequence | "Artefact-format problem — movement is primarily non-textual; textual notation may be specification-in-disguise" [`01a`, Q2] |
| Outsider | Meal-rotation | "Tacit, embodied, and sensory preferences hard to capture in a bounded brief; a cooking plan can become fake quickly" [`01d`, Q2] |
| Pragmatist | Training-plan | "Validate strain under adaptation uncertainty — Validate rests on rule-comparison and session-1 coachability, not outcome evidence" [`01b`, Q2] |
| Skeptic | Governance protocol | "Validate thinness — cannot manufacture a real contested decision; walk-through is a thinner test than lived use" [`01c`, Q2] |

`[synth]` **Each perspective named a different criterion-6 property for their pick, and each property is genuine rather than performative.** The criterion-6 property surfaces a different risk for each target:

- Movement → artefact-medium risk (text cannot carry movement design)
- Meal-rotation → brief-compression risk (lived constraints exceed what a brief holds)
- Training-plan → Validate-depth risk (rule comparison substitutes for outcome)
- Governance → Validate-legibility risk (walk-through substitutes for live deployment)

Three-of-four perspectives acknowledged that their pick carries a real risk they hold despite it. The Skeptic's pick is adversarially chosen — Skeptic explicitly states "a non-adversarial version of me would probably pick B" (Skeptic's B was the recipe target) [`01c`, Meta-note].

**Demotion pattern.** Each perspective names a fallback within their own candidate set:

- Explorer demotes A→C (movement to planting) if movement fails executability [`01a`, Q2].
- Outsider demotes 1→3 (meal-rotation to creative practice) if user cannot supply constraints [`01d`, Q2].
- Pragmatist demotes B→C (training-plan to consumer-decision) if Validate collapses on niche goals [`01b`, Q2].
- Skeptic's demotion path is explicit B→C to A, not C→B; Skeptic refuses to demote away from C on adversarial grounds [`01c`, Q2].

`[synth]` **Direction for the shortlist.** Because no single pick convergence exists, the synthesizer must construct a shortlist that honestly spans the four perspectives' tension axes. The selection is synthesis-work subject to D-046 criterion 6; the recommended pick record must name one target property expected to be challenging and the reason for proceeding.

---

## Q3: Failure Modes on the Recommended Picks — Domain-Specific, All Acknowledged

Each perspective produced failure modes specific to their own pick. `[synth]` The exercise confirms that each recommendation is held with eyes-open rather than optimistic.

**Explorer's failure modes on movement** [`01a`, Q3]:
- *Notation-as-specification.* A textual movement score may reproduce methodology-specification form under the guise of domain artefact.
- *Constraint under-specification by the user.* Too-loose or too-tight user constraint makes Deliberate's alternatives generic ("faster vs. slower") rather than constraint-native ("prioritise breath over tempo").
- Diagnostic: show the artefact to a movement-literate reader; if they say "document about a phrase" rather than "a phrase someone could learn," criterion-4 failure.

**Outsider's failure modes on meal-rotation** [`01d`, Q3]:
- *Preference instability rather than preference absence.* User can state preferences in the abstract, but dinner choices depend on contingent factors (mood, season, stress) that a clean system cannot capture.
- *Kitchen-context dependency.* The plan relies on unstated equipment, skill, cleanup tolerance, local shopping patterns.
- *Provisioning ecology mismatch.* Real design problem is not only meals but package sizes, perishability, shopping cadence, leftover reuse; some households cannot support a rotation without overbuying.
- Diagnostic: "If the brief contains enough domain constraints and the artefact still comes out generic, abstract, or jargon-laden, that is a methodology failure. If the artefact is concrete but falls apart against appetite variability, kitchen reality, or shopping ecology, that is a target-quality warning."

**Pragmatist's failure modes on training-plan** [`01b`, Q3]:
- *Generic-plan dressing.* Plan lifted wholesale from canonical programmes with user-name substitution; rejections reduce to "chosen option is more canonical" rather than domain-specific reasons.
- *Individualisation theatre.* Plan references user-specific facts cosmetically but progression/volume/recovery logic does not actually change based on those facts.
- Diagnostic: Validate asks "name two user-specific facts that meaningfully changed a choice and show the counterfactual plan without those facts."

**Skeptic's failure modes on governance protocol** [`01c`, Q3]:
- *Social texture illegible.* The group's real friction lives in implicit priorities, unstated loyalties, history — none of which compresses into a brief. Artefact reads as generic civic-textbook protocol, flat against the specific case.
- *Stakes collapse inward.* Drafting the protocol exposes something about the group the user did not want surfaced; artefact ceases to be external (criterion 5 fails retroactively).
- *Methodology-talk in validation.* User explaining what "Validate activity" means during walk-through rather than evaluating the protocol in domain terms.

`[synth]` **Structural parallel across the four failure-mode sets.** Every perspective's failure modes point to the same underlying risk: **the target's domain has tacit/contextual/embodied dimensions that resist bounded-brief compression**. Explorer's "constraint under-specification," Outsider's "preference instability" + "kitchen-context dependency," Pragmatist's "individualisation theatre," and Skeptic's "social texture illegible" are four surfacings of the same shape. This is itself a substantive convergence — across all four picks, the failure-risk is that the target's real difficulty lives in tacit context a first-session brief cannot fully capture. Whichever target the user ratifies, this risk applies.

---

## Q4: External Legibility — Convergence on "No Methodology-Vocabulary in the Artefact Itself"

**Four-way convergence on the external-legibility test.** All four perspectives articulate the same criterion in different words:

- Explorer: "The artefact would survive extraction... If extracted, it collapses into 'methodology notes about movement,' then the methodology is load-bearing in a way a real design package should not require" [`01a`, Q4]. No methodology-vocabulary (triggers, manifests, deliberation schema) in the artefact itself.
- Outsider: "The clean way to manage this is separation. The external artefact should stand alone as the thing being designed. Provenance can exist, but as a sidecar or appendix" [`01d`, Q4]. "A reader unfamiliar with the methodology should be able to ignore provenance entirely and still say, 'This is a usable dinner-system draft.'"
- Pragmatist: "The word 'specification' does not appear; 'deliberation' does not appear; provenance is framed as 'why this choice' in coach-speak, not decision-record language" [`01b`, Q4]. "Could they hand this plan to a friend and say 'follow this for eight weeks'?"
- Skeptic: "What the reader should *not* see, if the artefact is real domain work: the words 'activity,' 'deliberation,' 'provenance-record,' 'specification,' 'trigger,' or 'manifest' as the protocol's load-bearing vocabulary" [`01c`, Q4].

`[synth]` **This is a genuine four-way convergence at the substantive-claim level**, not mere lexical echo. The operational rule it produces: the first external artefact must be extractable from the session's provenance and must stand alone in its domain's own vocabulary. Provenance (reasoning trail, alternatives considered, deliberation record) may sit alongside as a sidecar, but the external artefact proper uses only domain-native language.

**Four-way convergence on the dual-reader test.** Each perspective proposes a second-reader check:

- Explorer: movement-literate reader (yoga teacher, physio, dancer) judges whether the score reads as "an instance of their domain's vocabulary."
- Outsider: household member reader asks "can I shop from this without guessing?" — ordinary operational questions in domain-terms.
- Pragmatist: coach or experienced trainee gives substantive feedback ("the deload at week 4 is too early given the volume in weeks 1-3"); if their feedback is "I can't tell what this is," legibility failed.
- Skeptic: show the artefact to a second analogous group (different household, different small group) and ask whether they can adapt it by changing parameters or would need to start over.

`[synth]` **This too is a four-way convergence**, and it establishes the operational test for criterion 5 across all four pick candidates: the artefact must pass a domain-native reader's judgement without the reader needing to know the methodology exists.

---

## Q5: Agent Bias — Four-Way Convergence on Document-Shape / Representability Bias

**This is the deliberation's strongest four-way convergence.** All four perspectives — three Claude and one non-Claude (Outsider) — independently named the same non-obvious agent bias with distinct phrasings:

- Explorer: "**artefact-shape bias** — the selecting agent over-weights domains whose work-products are textual and linear. Deeper than software-adjacent — it is document-adjacent. Curricula, recipes, essays, learning plans, style guides, policy briefs, editorial style-sheets — all feel 'natural' to methodology work because their native artefact is already a document. The methodology does not have to re-interpret how outputs exist; it only has to swap vocabulary" [`01a`, Q5].

- Outsider: "**representability bias** — the tendency to prefer targets whose success can be fully represented in a clean document. This is not exactly software bias, and not exactly 'expected to succeed' bias. It is the prior that the best first targets are the ones where the whole problem can be turned into text, tables, and rationale without residue" [`01d`, Q5].

- Pragmatist: "**medium bias** — a preference for targets that produce a single primary document as the artefact. This is not software-adjacency (criterion 8) and not expected-to-succeed (criterion 6 in its narrow form); it is medium bias. The methodology's apparatus (provenance, deliberation records, triggers-met annotations) slots neatly onto document-shaped outputs and strains on artefact-shaped outputs that are not primarily textual" [`01b`, Q5].

- Skeptic: "**shape of the artefact** — the agent prefers targets whose domain artefact shape is textual, structured, and author-led — a single document produced by a single author for a cooperative reader. The methodology was built in that shape. The agent will gravitate to targets whose deliverable looks like 'a specification' because specifications are what the agent has practised producing. This is distinct from software-adjacency (criterion 8) and distinct from expected-to-succeed (criterion 6); it is a bias about the shape of the artefact, not the domain" [`01c`, Q5].

`[synth]` **Four independent phrasings. Same underlying finding.** The convergence crosses the model-family axis: the non-Claude Outsider's "representability bias" is the same structural claim as the Claude perspectives' "document-shape," "medium," and "artefact-shape" biases. Each perspective arrives at it from a different direction:

- Explorer arrives via "vocabulary distance could be gamed by translation without actual re-interpretation."
- Outsider arrives via "best first targets should have lived-use residue beyond the text."
- Pragmatist arrives via "methodology's apparatus fits document outputs; strains on non-document outputs."
- Skeptic arrives via "all three of my own candidates share the bias — that is a real admission."

The four-way convergence is strong evidence that this bias is genuine rather than a lexical artefact of brief framing. The brief did not seed this vocabulary.

**Convergent candidate rule-outs on this bias** [all four, Q5]:

- Vault / note-taxonomy / personal-knowledge-system reorganization (Outsider explicit [`01d`, Q5]; Skeptic by extension; Pragmatist by implication; Explorer would reject).
- Curriculum / reading-path / learning-path targets (Explorer explicit [`01a`, Q5]; Skeptic demotes own reading-protocol candidate [`01c`, Q2]; Outsider flags curriculum-shape as "too easy a first victory" [`01d`, Q2]).
- Policy-document targets (Skeptic explicit [`01c`, Q5]).

**Convergent candidate pull-ins on this bias** (non-document-shaped artefacts):

- **Physical-space arrangement** — named by Explorer [`01a`, Q5] and Pragmatist [`01b`, Q5] (desk layout, room rearrangement, home-office flow). Neither pushed it to Q1 shortlist on executability grounds.
- **Ritual / routine design** — Pragmatist [`01b`, Q5] (morning start-sequence, weekly review practice).
- **Conversation-opening design** — Pragmatist [`01b`, Q5].
- **Designed schedule / visual reference / colour system** — Skeptic [`01c`, Q5].
- **Small hospitality / event package** — Outsider [`01d`, Q5] (hosting one dinner or salon: invitation framing, menu logic, room flow, contingency plan).

`[synth]` **The convergence's implication for Session 008's shortlist.** Three of four perspectives' picks produce document-shaped artefacts (meal-rotation, training-plan, governance protocol). Only Explorer's movement pick escapes document-shape bias. **The shortlist the user receives must honestly acknowledge that three of four options share the bias the deliberation identified.** Including Explorer's movement in the shortlist gives the user a genuine choice across the document-shape dimension.

**Cross-session implication.** This finding also produces a **session-after-next directive**: Session 009 or later should deliberately target a non-document artefact (per Skeptic's explicit proposal [`01c`, Q5] and Explorer's extended scrutiny [`01a`, Q5]). The methodology does not get to claim full generality until it has produced a provenance-record for something that is not a document.

---

## Points of Disagreement (preserved)

These are the positions not absorbed into consensus. Each is load-bearing and must survive into the decision record:

1. **Which target is the right recommended pick (four-way divergence on pick; no convergence).** Explorer: movement. Outsider: meal-rotation. Pragmatist: training-plan. Skeptic: governance protocol. The divergence is substantive — each pick optimises a different criterion within D-046. The synthesizer's recommendation (below) must make a judgement call the perspectives did not converge on.

2. **Training-plan is an acceptable agent-selection default (Pragmatist alone).** Skeptic explicitly rejects physical-training programmes ("validation timeline too long") [`01c`, Q1]; Outsider rejects fitness/nutrition plans on criterion 2 stakes [`01d`, Q1]; Explorer does not propose or address. Pragmatist argues training-plan clears criteria 1, 2, 3, 5, 7 strongly and is low-stakes under adult-athlete judgement [`01b`, Q2]. `[synth]` The disagreement is whether training-plan's Validate thinness (rule-comparison only in one session) is acceptable for first external application. Three-of-four say no; Pragmatist says yes with eyes-open.

3. **Movement / non-document artefacts should be in the Q1 shortlist (Explorer alone; others acknowledge the bias but exclude on executability).** Explorer holds movement as recommended pick; Pragmatist, Skeptic, and Outsider each name non-document candidates in Q5 but explicitly do not advance them to their own Q1 shortlists. Pragmatist: "I will not add these to the Q1 shortlist because I'm unsure any of them survive criterion 5 (external legibility to a reader outside the user's life) or criterion 3 (Validate analogue)" [`01b`, Q5]. Skeptic: "I do not add to my Q1 shortlist because I do not want to pretend I can execute it well within the criteria" [`01c`, Q5]. Outsider: hospitality package not in Q1 because "less obviously accessible than meal planning" [`01d`, Q5]. `[synth]` Explorer's willingness to proceed with movement despite these concerns represents a genuine dissent on how to weight criterion-4 (vocabulary distance) against criteria-5/7 (legibility/accessibility).

4. **Criterion 7 (accessibility) is a stronger floor than the brief admits (Skeptic).** Skeptic: "the brief treats criterion 7 (accessibility) as a floor and criterion 6 as the counter-weight, but in practice criterion 7's bounded-brief requirement narrows the domain far more than criterion 6 widens it. The real floor is higher than the brief admits" [`01c`, Meta-note]. `[synth]` This is a critique of D-046's internal balance; preserved as a finding that future sessions may revisit.

5. **"First external application" vs. "first-session-executable increment" conflation (Pragmatist).** Pragmatist: "the brief conflates 'first external application' with 'first-session-executable increment.' These may be different things. The first genuinely external application might rightly take two or three sessions; the pressure to close in one session biases toward small, document-shaped, legible-fast targets — which is itself the pre-shaping criterion 6 guards against" [`01b`, Meta-note]. `[synth]` This critiques D-046 criterion 1's bounded-scope framing. Preserved; future sessions may revisit whether a two-or-three-session first external application is consistent with D-046.

6. **Validate thinness trade-off — Skeptic's adversarial choice.** The Skeptic explicitly states they would not, as a non-adversarial self, pick their own recommended candidate [`01c`, Meta-note]. They hold C to ensure the shortlist contains one candidate that most strongly resists agent-comfort bias. `[synth]` This is a methodological honesty move the synthesis preserves: the Skeptic's adversarial pick is not the same as a sincere preference, and the synthesis's ultimate recommendation must weigh whether to follow the adversarial pick (honour criterion 6) or to follow the non-adversarial consensus (honour Validate-depth across criteria).

7. **The entire shortlist shares document-shape bias (Skeptic's explicit admission).** Skeptic: "Candidate A (reading protocol) looks suspicious for reasons beyond vocabulary-overlap: it produces a document. Candidate B (menu) produces a document. Candidate C produces a document. All three candidates I offered share the bias. That is a real admission" [`01c`, Q5]. `[synth]` The admission honours the methodology's preservation-of-dissent principle. The synthesizer's constructed shortlist must acknowledge this same constraint (three of four pick-options are document-shaped) or explicitly resist it by including a non-document candidate.

---

## Cross-Model Observations

This was the methodology's fourth heterogeneous-participant deliberation. Two distinct cross-model patterns surfaced:

**Pattern 1: Four-way convergence on representability / document-shape / artefact-shape / medium bias (Q5).** The non-Claude Outsider's "representability bias" is operationally identical to the Claude perspectives' "artefact-shape" (Explorer), "medium" (Pragmatist), and "shape of the artefact" (Skeptic) biases. Four independent framings of the same finding, each derived from a different argument line. **This is the strongest cross-model signal in Session 008's deliberation and one of the strongest cross-model signals across the four heterogeneous-participant deliberations run to date.** It is not lexical echo (no single phrase dominates; the brief did not seed this vocabulary). It is substantive cross-lineage convergence on a finding about agent-selection bias that criterion 6's generic "expected-to-succeed" framing did not previously name.

`[synth]` **Session 008 criterion-3 evidence for OI-004** (recorded impact on outcomes): the four-way convergence on document-shape bias shaped the shortlist composition. If the synthesizer had followed the Claude-subagent recommendations alone (three of three produce document-shaped picks), the shortlist would have been purely document-shaped. The Outsider's "representability bias" framing combined with Explorer's dissent provide the cross-perspective pressure that forces the synthesizer to either include Explorer's non-document pick in the shortlist or explicitly resist doing so with argued reason. This is a cross-model-impact-on-outcome in the criterion-3 sense, even though D-023 does not fire for this deliberation and the sustained-practice tally does not advance.

**Pattern 2: Cross-model convergence on meal-rotation as lived-use Validate (Outsider + Explorer).** The Outsider's Candidate 1 (meal-rotation) and Explorer's Candidate B (recipe) are in the same domain cluster. Both argue that cooking / meal-design passes the lived-use Validate test — the user can cook and eat, and failure is legible. They differ in scope (Outsider proposes two-week rotation system; Explorer proposes one dish) and in framing (Outsider argues affirmative criterion-6 challenge from tacit preferences; Explorer demotes B to shortlist because recipe-card output is document-shaped). The convergence on "cooking as a domain with real lived-use Validate" crosses the model-family axis on the Pro-cooking side; Pragmatist and Skeptic are Anti-cooking on criterion-6 concerns. This is a softer convergence pattern than Pattern 1 but is worth recording.

**Outsider-unique contributions (not present in any Claude response):**

- **"Preference instability rather than preference absence"** [`01d`, Q3]: the Outsider's distinctive failure-mode for meal-rotation. User can state preferences in the abstract, but dinner choices depend on contingent factors (mood, season, stress, appetite, tolerance for repetition) that a clean system cannot capture. No Claude perspective named this specific failure-mode for any target, though Skeptic's "social texture illegible" has the same underlying shape for a different domain.

- **"The target depends on tacit, embodied, and sensory preferences that are hard to capture in a bounded brief"** [`01d`, Q2]: the Outsider's criterion-6 challenging-property formulation for meal-rotation. No Claude perspective uses this exact framing; Explorer has "constraint under-specification," Pragmatist has "adaptation uncertainty," Skeptic has "social texture illegibility" — each is its own formulation.

- **"A small hospitality package"** [`01d`, Q5]: the Outsider's fourth-candidate addition on the representability-bias scrutiny. Invitation framing, menu logic, room flow, timing, contingency plan. Hospitality as a non-textual design domain where success cashes out in lived use. The Outsider does not advance this to Q1 shortlist on executability grounds but offers it for consideration. Pragmatist's and Skeptic's non-document extensions (physical-space arrangement, schedule design) are Claude analogues; hospitality is Outsider-unique in naming.

The Outsider's banner-recorded identity (OpenAI GPT-5 via Codex CLI v0.121.0, session id `019da3bb-53c2-7113-8e70-61fe62c953c1`, `reasoning effort: xhigh`, 13,391 tokens used) is the transport-layer evidence of non-Claude participation per D-029's Q6 honest-evidence requirement.

---

## Limitations

Required content for multi-agent deliberation records (v3 spec's Limitations requirement):

- **Three of the four perspectives share the Claude Opus 4.7 model family.** The Outsider's distinct-lineage participation does not remove the Claude-majority. Convergence that includes the Outsider is stronger evidence than convergence that does not; this synthesis has flagged both categories where they apply.
- **The Outsider was invoked via a CLI wrapper (`codex exec`), not a direct API.** Transport fidelity depends on convener integrity. The raw output is committed verbatim including banner and prompt echo; no automated integrity check verifies this.
- **Brief-writing had no adversary.** The shared brief was written by the synthesizer-orchestrator (a Claude Opus 4.7 agent). Session 008's brief made an explicit discipline to avoid seeding distinctive Session 007 vocabulary, per the third-consecutive-brief-priming finding. However, D-046's eight criteria were quoted verbatim; the shared analytical vocabulary ("criterion 4," "vocabulary distance," "lived-use Validate") is brief-derived by necessity. The synthesis has tried to distinguish substantive from lexical convergence, particularly on the Q5 four-way finding (which is substantive — the convergence is on the underlying claim, not on specific phrasings).
- **The synthesis step is a single-agent re-entry point** (Claude Opus 4.7, matching three of four deliberators' model family). The synthesizer has not played any perspective, per D-018.
- **The Outsider was selected by the session operator** (Claude Code orchestrating agent), not independently. `participant_selection_method: self` is the most honest classification. Same caveat as Sessions 005, 006, 007.
- **No D-023 trigger fires for target selection.** This is the methodology's fourth heterogeneous-participant deliberation but the second in which non-Claude participation is conservative-inclusion rather than D-023-required (Session 007 was the first). The sustained-practice tally does not advance from this deliberation alone. If a subsequent Session 008 Produce-activity decision triggers D-023 (e.g., a W1-finding forces a kernel clarification), that decision may advance the tally; this is contingent on content, not asserted here.
- **The synthesizer's shortlist-construction is a second-layer single-agent decision.** The four perspectives did not converge on a pick; the synthesizer must construct the shortlist from their inputs. This is a known re-entry point per `multi-agent-deliberation.md` v3 Limitations. The synthesizer's shortlist composition below names its reasoning explicitly.

---

## Structural honesty notes

- Every claim attributing a position to a perspective in this synthesis cites the source file and question section.
- `[synth]` marks synthesizer-original claims (convergence identifications, resolution proposals, direction-setting moves not found verbatim in any raw output).
- Dissent is preserved in the "Points of Disagreement" section at its strongest form.
- Majority/minority structure is reported explicitly where the four perspectives diverged.
- Quote over paraphrase was applied for all load-bearing attributions (particularly the Q5 four-way convergence's four distinct phrasings).
- Brief-priming discipline was applied to the brief itself (per Session 008 assessment); beyond D-046 criterion names, neutral operational language was used. The Q5 convergence on "document-shape / representability bias" is substantive — the brief did not use these phrases.

---

## Synthesis Output — Shortlist and Recommended Pick (for user ratification per D-045 Branch B)

The synthesizer constructs the following shortlist from the deliberation. Composition reasoning is recorded explicitly (per the known single-agent re-entry point at synthesis).

### Shortlist of three candidates (span across tension axes)

**Candidate 1 (recommended) — Household meal-rotation and provisioning protocol.**
- **Domain:** household operations / meal design.
- **Problem (illustrative shapes; user may specify or substitute):** design a two-week weekday dinner system under the user's stated constraints — dietary preferences, kitchen setup, weekly shopping rhythm, time-on-any-given-night ceilings, ingredient-fatigue tolerance. Artefact: dish roster, grocery cadence, prep-and-leftovers map, substitution rules, abort/fallback logic, validation sheet for first run.
- **Domain vocabulary:** rotation, cadence, provisioning, perishability, leftovers-map, substitution, operational sufficiency.
- **Validate analogue:** lived-use — user cooks and eats several nights from the plan; reports whether plan executed cleanly, where it broke, which dishes were rejected or modified at execution time.
- **Strongest criteria:** 1, 2, 3, 5, 7 (per Outsider's analysis; bounded, low-stakes, lived-Validate, externally legible to any household reader, user-accessible constraints).
- **Weakest fit:** 4 (recipe/menu form is document-shaped) and 6 (Skeptic's concern that recipe-class targets are agent-comfortable). Both are acknowledged.

**Candidate 2 — Small-group governance or dispute-resolution protocol.**
- **Domain:** human-process design for a real interpersonal or small-group context in the user's life (household-of-two, hobby project with one or two collaborators, volunteer group, shared-resource group).
- **Problem (illustrative shapes):** written protocol for a specific recurring decision-making situation — shared-purchase decisions above a threshold; hobby-project direction-change decisions; household standing-decisions on media, scheduling, hosting.
- **Domain vocabulary:** proposal, objection, standing decision, review period, quiet consent, fallback, escalation, amendment.
- **Validate analogue:** walk-through with a second participant (another group member) imagining how the protocol would have worked on a named past decision; secondary test — show to a different small-group analogue and see whether they adapt by parameters or start over.
- **Strongest criteria:** 4 (vocabulary distance from methodology-talk is real), 6 (most adversarial pick; resists agent-comfort most visibly).
- **Weakest fit:** 3 (Validate is thinner — walk-through substitutes for live deployment) and 2 (stakes-collapse risk if the protocol exposes something about the group the user did not want surfaced).

**Candidate 3 — Short movement sequence for a stated constraint.**
- **Domain:** movement design — mobility sequencing, short exercise or practice phrase, warm-up routine.
- **Problem (illustrative shapes):** a 60-second solo sequence for a named constraint (e.g., morning mobility for a stiff lower back; a thirty-second transition between two named postures; a practice-phrase built around one refused motion); or a graded mobility sequence the user could actually try over a week.
- **Domain vocabulary:** tempo, weight, impulse, phrasing, breath, orientation, transition, counts.
- **Validate analogue:** user attempts the sequence with their own body; reports felt-sense outcomes (does it flow, does the constraint hold, is tempo sustainable). Optional: movement-literate reader judges the score as "a phrase someone could learn" vs. "a document about a phrase."
- **Strongest criteria:** 4 (vocabulary distance maximal — none of the movement vocabulary maps to methodology-talk), 3 (Validate is unambiguous and fast).
- **Weakest fit:** 5 (external legibility — a reader without movement background may not be able to judge; mitigated if artefact is notated as a score rather than a numbered list) and the artefact-format problem (Explorer's own criterion-6 property: text may fail to carry movement).

### Recommended pick: Candidate 1 — Meal-rotation and provisioning protocol

**Composition reasoning.** The synthesizer adopts the Outsider's recommendation as the session's recommended pick. The reasoning:

- The deliberation produced no four-way convergence on pick. Among the four perspective picks, meal-rotation has the most balanced profile against D-046's eight criteria: it is strong on 1, 2, 3, 5, 7 and honestly weak on 4 and (partially) 6, with a genuine criterion-6 challenging property surfaced by the Outsider [`01d`, Q2] that is neither performative nor evasive.
- The Outsider (cross-model, non-Claude training lineage) independently surfaced meal-rotation as the recommended pick. This carries weight against the agent-comfort-bias concern: a non-Claude perspective, reasoning from a distinct training lineage, arrived at this candidate independently of any Claude-family preferences. Per D-046 criterion 6's "not pre-shaped by orchestrating agent" requirement, cross-model independent reach for the same candidate reduces the pre-shaping risk.
- Candidate 2 (governance protocol) is the Skeptic's adversarial pick and carries genuine Validate thinness that the Skeptic themselves acknowledges would make them demote it from a non-adversarial stance [`01c`, Meta-note]. It is preserved in the shortlist for the user who wants the maximum criterion-6 test, but is not the synthesizer's recommendation because its Validate-depth risk is too load-bearing for a first external application. A session whose Validate reduces to walk-through-of-hypothetical produces weaker first-application evidence than a session whose Validate involves lived execution.
- Candidate 3 (movement) is Explorer's pick and the only shortlist option that escapes document-shape bias. It is preserved as a genuine choice for the user who wants a non-document first test. It is not the synthesizer's recommendation because three of four perspectives concluded that its external-legibility and executability concerns are too load-bearing for a first external application, and Explorer's own criterion-6 property (artefact-format problem) is a real risk the deliberation did not resolve.
- Training-plan (Pragmatist's pick) is **not** in the shortlist. Three-of-four perspectives argued against it (Skeptic: validation timeline too long; Outsider: stakes too close to health; Explorer: not addressed but inconsistent with Explorer's artefact-shape-distance priority). Pragmatist's position — that adult-athlete judgement makes stakes tractable and rule-comparison-against-published-programs is adequate Validate — is preserved as a dissenting minority position but does not survive into the shortlist. The synthesis honours this majority-pattern honestly: training-plan does not advance.

**Criterion-6 challenging property for the recommended pick.** Quoted verbatim from the Outsider's raw output [`01d`, Q2]:

> "The target depends on tacit, embodied, and sensory preferences that are hard to capture in a bounded brief. A cooking plan can become fake very quickly. It can sound organized while failing at the level of appetite, stove-time, leftovers, or ingredient fatigue."

**Reason for proceeding nonetheless** (per D-046 criterion 6 requirement):

The tacit-preferences difficulty is a feature of the test, not a reason to avoid it. A first external target whose lived-use Validate is real produces legible failure in domain-terms (user cannot execute the plan; nights fall apart against kitchen reality; rotation over-buys or produces ingredient fatigue) rather than methodology-terms (the artefact was well-reasoned in the abstract). Meal-rotation sits in the useful middle the Outsider named: the artefact is documentable, but its success is constrained by lived use. If the methodology can produce something here that looks and behaves like a real household design package, that is better evidence than a polished document on any target whose Validate degenerates to "does the spec read coherently" (D-046 criterion 3's disqualification).

Additionally: all four perspectives flagged that the target's real difficulty commonly lives in tacit, contextual, embodied dimensions that resist bounded-brief compression (see Q3 structural parallel). This risk applies to every candidate in the shortlist. Choosing meal-rotation does not evade the risk; it chooses the target where the risk is most legibly detected by a domain-native reader.

### Additional selection-record content (per D-046 criterion 6 expectation)

The recommended pick inherits the deliberation's **four-way acknowledgement of document-shape bias**. Two shortlist options (meal-rotation, governance protocol) are document-shaped artefacts. Only Candidate 3 (movement) escapes. The synthesizer does not claim that choosing meal-rotation over movement resolves the document-shape-bias concern; it claims that within the document-shape space, meal-rotation's lived-use Validate and tacit-preferences criterion-6 property make it the strongest first-application target, and that Session 009 or a subsequent session should deliberately pursue a non-document target per the deliberation's coverage-finding (Skeptic, Explorer, Pragmatist, Outsider all named non-document candidates but declined to advance them this session on executability grounds).

### User-ratification halt

The synthesis now halts for user ratification per D-045 Branch B: "the user's accept/reject is recorded as provenance before Session 008's Produce activity begins." The user may:

- **Ratify Candidate 1 (recommended pick, meal-rotation)** — Session 008 proceeds to Produce on meal-rotation with the user's constraints.
- **Ratify a different shortlist candidate (Candidate 2 governance protocol; Candidate 3 movement)** — Session 008 proceeds to Produce on the chosen candidate.
- **Reject the shortlist and propose a user-directed target** — Session 008 pivots to D-045 Branch A handling per the Session 008 assessment (agent checks the user-directed target against D-046 criteria; user-direction overrides criteria 1 and 8 only).
- **Reject the shortlist entirely without providing an alternative** — Session 008's binding constraint under D-048 activates: a newly-surfaced, specifically-named blocker must be recorded with its load-bearing claim defended; OI-009 activates hard if no such blocker is surfaced.

A narrower ratification (e.g., "Candidate 1, and the specific problem is a two-week weekday dinner system for a vegetarian high-protein rotation with one batch-prep block") is welcomed and preferable to a bare accept — it lets the user inject domain constraints that the Produce activity's brief requires.
