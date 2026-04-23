---
session: 033
title: Shared Brief — Kernel §7 revision per §9 trigger 7 mandate
date: 2026-04-23
status: brief-immutable
---

# Shared Brief — Kernel §7 Revision

This is the byte-identical shared context for the four perspectives participating in Session 033's kernel §7 revision deliberation. Each perspective will see this shared context plus their role-specific stance (§4 below). Perspectives reason from the brief only; they do not read workspace files during the independent phase (per `multi-agent-deliberation.md` v4 §Stance Briefs).

## 1. Methodology context

You are participating in the **Selvedge engine's** self-development. Selvedge is a methodology for diverse perspectives reasoning together, producing durable artefacts, and preserving reasoning and dissent so the system can evolve by running its own process on its own outputs.

The **engine** is the current loadable implementation (file set enumerated in `specifications/engine-manifest.md`). Current version: **engine-v5** (established Session 028). Every session applies the engine to a problem. This session is the 33rd in a chain of self-development sessions (001–032 prior).

Key specifications you need to know about:
- `specifications/methodology-kernel.md` v5 defines nine activities (Read / Assess / Convene / Deliberate / Decide / Produce / Validate / Record / Close). **§7 Validate** is the target of this session's revision.
- `specifications/reference-validation.md` v2 defines the third sense of validation (Reference validation, added alongside Workspace and Domain senses per kernel §7 v4). It specifies a sealed three-cell protocol (Curation / Produce / Validation), a seven-layer contamination defence stack, and §9 automatic re-opening triggers for OI-016.
- `specifications/multi-agent-deliberation.md` v4 governs this deliberation's shape (required non-Claude participation for kernel revisions).
- `open-issues/OI-016.md` tracks "Domain-validation pathway under user unavailability." OI-016 was Resolved-provisionally Session 014 → Session 019 via creation of `reference-validation.md`. **Session 032 re-opened OI-016 to Open state (first-ever OI re-opening event in engine history) per §9 trigger 7 firing.**

## 2. Problem statement

`reference-validation.md` v2 **§9 trigger 7** fired at Session 032 close. The trigger was pre-committed Session 019 per Reviser R4 + Outsider §9.7; it specifies that two pre-seal C3 Stage (b) rejections in structurally-different domains with near-verbatim Claude-family reproduction shall:

1. **Activate** the Session 014 Skeptic "provisional substitute" minority warrant (per `reference-validation.md` v2 §10.1) as a **required kernel §7 revision consideration** in the next session after the second rejection.
2. **Re-open** OI-016 to Open state pending that consideration.
3. Make the saturation-gate false-negative pattern (surviving L1a canary but rejected at L1b full-constraint probe) observable as a pattern rather than a single-session artefact.

The trigger fired because:
- **Session 018 first rejection:** D2 Kerth Prime Directive retrospective-opening protocol — Cell 1 C3 rejection with ~94% 5-gram overlap and verbatim section-heading emission by Claude Opus 4.7 subagent (agile-retrospective domain; copyrighted reference).
- **Session 032 second rejection:** PD-A Rule of St. Benedict Ch 58 "Of the Discipline of Receiving Brothers" — Cell 1 L1b rejection on Condition 2 (verbatim distinctive labels "postulancy"/"novitiate"/"profession"/"habit" emitted by both Claude and codex GPT-5.4 despite §2 forbidden-terms discipline at constraint-statement level; community-admission domain; public-domain reference). **Cross-family-symmetric saturation** (both OpenAI and Anthropic pretraining densely-trained on RoSB-religious-formation tradition) — methodologically distinct from Session 018's Claude-family-asymmetric saturation.

Session 033 is "the next session after the second rejection." This deliberation's load-bearing work is revising kernel §7 to reflect the activated minority warrant.

### Activated minority (Session 014 §10.1, now active per §9 trigger 7)

**Skeptic "provisional substitute" framing minority** (Session 014, 01c Q5):

> The kernel should name reference-validation as explicitly **provisional**, not as equal-but-distinct third sense. The adopted kernel text incorporates the Skeptic's load-bearing scope-statement content ("does not establish intended-use functioning") without using the word "provisional." Operational warrant: if label discipline collapse (§9 trigger 6) is observed, the Skeptic's stricter "provisional substitute" framing is the preferred revision direction for kernel §7.

Per Session 019 annotation, the §9 trigger 7 path broadens the activation to "n=2 structurally-different-domain rejection" (structurally parallel to label-discipline collapse).

### Vindicated minority (Session 019 §10.2 Skeptic preemptive-activation, now vindicated)

**Skeptic preemptive-activation minority** (Session 019, 01c Q5, Q7):

> Position: WX-18-3's empirical materialisation of the §1-flagged tension satisfies the *spirit* of §10.1's "provisional substitute" warrant, even though the specific textual trigger (label-discipline collapse) has not occurred; kernel §7 should have been revised in Session 019 to use the phrase "provisional substitute" and to add a **mandatory-dissent clause**. Session 019's 3-of-4 cross-family majority adopted the narrow reading instead. **Operational warrant:** if Sessions 020–022 produce a second structurally-different-domain Cell 1 rejection (triggering §9 trigger 7) and the broad-reading preemptive activation would have prevented interim citation drift, the Skeptic's preemptive-activation position is vindicated. The Skeptic's full Q5 text (kernel §7 draft with "provisional substitute" + mandatory-dissent clause) is preserved in `provenance/019-reference-validation-revision/01c-perspective-skeptic.md` Q5.

### Current kernel §7 text (methodology-kernel.md v5; target of revision)

```
#### 7. Validate

Validate the session's output at each level on which it makes claims. Three senses apply.

**Workspace validation** applies to every session. Check that:
- New specifications don't contradict existing ones
- Specifications describe the workspace as it actually is
- Provenance records are complete and well-formed
- Open issues reflect the actual state of uncertainty

**Domain validation** applies when a session produces or revises an artefact intended for use outside the workspace and a domain-actor is available. Obtain evidence from the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent — that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.

**Reference validation** applies when a session produces an external-intent artefact and no domain-actor is available. A reference-validation exercise pairs the methodology's Produce step (run blind against a staged constraint tranche set whose emergent constraints surface during the run) with comparison against a pre-selected documented proven solution the Produce agents do not see. The exercise runs across a small number of sessions in a sealed three-cell protocol (Curation, Produce, Validation) specified in `specifications/reference-validation.md`. The exercise records constraint-satisfaction, structural correspondence, cross-model divergence, and a contamination audit.

**Reference validation supplies evidence about the methodology's capacity to derive artefacts under stated constraints. It does not establish that the artefact functioned in its intended use. It does not substitute for Domain validation when a domain-actor is available.** Artefacts passing reference-validation carry the label `validation: reference-validated` in frontmatter and retain that scoping in any later citation.

If any validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.
```

### Session 032's operational findings (from PD-A REJECT deliberation)

Three new methodology findings that inform this revision:

1. **Public-domain-constraint elevated C3 risk hypothesis confirmed.** PD references are structurally more saturated than copyrighted references because PD works are freely included in pretraining corpora.
2. **Cross-family-shared saturation as new pattern** (n=1 clean instance). Session 018 was Claude-family-asymmetric; Session 032 is cross-family-symmetric. The latter is methodologically more concerning because it indicates a tradition densely-trained across model families (OpenAI + Anthropic), not just within one. Session 019 Reviser asymmetry-probe does not detect this.
3. **Saturation-gate false-negative pattern observable as pattern.** L1a PASS does not predict L1b PASS (Session 031 PASS-direction with genre-saturation observation; Session 032 REJECT after L1a PASS in same session). L1a is necessary but weakly predictive of L1b.

### Reference-validation L1b pass rate to date

1 of 3 at L1b: Session 018 D2 REJECT; Session 031 S1 Feldenkrais Lesson 1 PASS-with-genre-saturation-observation; Session 032 PD-A REJECT.

## 3. Design questions

You will address five questions in order. State your position on each; do not soften or pre-compromise because other perspectives may disagree.

**Q1. Provisional framing.** Should kernel §7 rename "Reference validation" to "Provisional reference substitute" (or similar framing that names the provisional status explicitly in the sense-label), OR retain "Reference validation" as the label while adding the word "provisional" to the scope-statement paragraph? Or is neither change required given the existing scope-statement ("does not establish intended-use functioning")? Argue your position.

**Q2. Mandatory-dissent clause.** The Session 019 Skeptic's vindicated minority specifies a mandatory-dissent clause: any citation of reference-validation evidence must be accompanied by a named dissenting view or acknowledged contamination risk. Should kernel §7 include such a clause? If yes, at what scope — all citations, only external-facing citations, or only "methodology-level" claims? If no, what alternative if any?

**Q3. Scope-statement strengthening.** The current kernel §7 says "does not establish intended-use functioning; does not substitute for Domain validation." Should this be strengthened — e.g., adding "does not validate that the methodology is working, only that it can produce outputs satisfying stated constraints in domains where the reference is not heavily pre-trained"? Or is the current language sufficient? Argue your position, with reference to the Session 032 cross-family-symmetric saturation finding if relevant.

**Q4. Cascading revisions.** Does the kernel §7 revision require any cascading changes to other engine-definition files — specifically `reference-validation.md` v2 (possibly v3) or `engine-manifest.md`? Or can the kernel §7 revision stand alone with only the minimum cascading updates (preserving v5 as superseded; updating engine-manifest §2 + §7 for engine-v6 bump declaration)? Identify the smallest coherent set of revisions.

**Q5. OI-016 disposition.** After the kernel §7 revision is adopted, should OI-016 transition Open → Resolved with new resolution disposition (e.g., "Resolved — provisional-substitute framing adopted, pending Session 033+ operational verification"), OR remain Open pending further work such as `reference-validation.md` v3 substantive revision addressing the cross-family-symmetric saturation finding, OR some other disposition? Argue the disposition that matches the Session 032 operational findings and the activated minority's warrant.

## 4. Role-specific stances

*This section is not byte-identical across briefs. Each perspective sees only their own stance block.*

### 4a — Reviser

**Stance.** You are the Reviser. Your job is to frame concrete revision options for kernel §7 that incorporate the activated Session 014 §10.1 Skeptic "provisional substitute" minority and the vindicated Session 019 §10.2 Skeptic preemptive-activation minority, while being honest about what the revisions buy and what residual risk remains. You have access to the Session 019 Skeptic's full Q5 text (preserved in `provenance/019-reference-validation-revision/01c-perspective-skeptic.md` Q5) as the pre-committed revision direction. You should treat that text as a strong starting point but not as obligatory-verbatim — adapt it to incorporate Session 032's new operational findings (cross-family-symmetric saturation; saturation-gate false-negative pattern; PD-constraint C3-risk elevation).

You should propose concrete language. For Q1 and Q3, draft revised paragraph text (not just summaries). For Q2, specify the clause's exact text, placement, and operational enforcement mechanism. For Q4 and Q5, be concrete about whether cascading revisions are required and what the OI-016 disposition should be.

You are non-adversarial. Your work is integration, not opposition. However, do not soften the "provisional" language to make it more palatable — the Session 014 Skeptic's position was preserved because softening reduces signal.

### 4b — Skeptic-preserver

**Stance.** You are the Skeptic-preserver. Your job is to **argue for minimal revision** — defend the existing v5 kernel §7 text where defensible; identify places where the proposed revision over-corrects; guard against the pattern of "revise-in-response-to-any-trigger-firing" that could degrade the kernel's stability.

You are adversarial to the default revision direction. Your adversarial posture serves the methodology: if the activated minority's direction is correct, it should survive your challenge; if not, your challenge surfaces that fact. You are not arguing that no revision should happen (the §9 trigger mandate is binding at the "consideration" level), but you are arguing that the minimum-viable consideration may be much smaller than a full rewrite.

Consider specifically:
- The current §7 already contains the load-bearing scope-statement content ("does not establish intended-use functioning"; "does not substitute for Domain validation"). Is adding the word "provisional" informationally-redundant or information-gaining?
- The mandatory-dissent clause could be enforced at the `reference-validation.md` §8 (label discipline) level rather than kernel §7. Which location is more appropriate?
- Session 032 is n=2 rejection — the trigger mandates consideration, not necessarily adoption. What counter-considerations should the deliberation weigh?
- If the kernel §7 revision is minimal, does `reference-validation.md` v2 still need a v3 substantive revision to address the cross-family-symmetric finding, or should that finding remain as an open watchpoint for n≥2 accumulation?

You should be concrete: name specific minimal-revision options for each of Q1–Q5; where the activated minority's broader proposal goes too far, propose a narrower alternative; declare where you think the deliberation should converge, not just where you push back.

### 4c — Synthesiser

**Stance.** You are the Synthesiser. Your job is to reason about how kernel §7 revisions interact with the broader engine-v6 bump — including `reference-validation.md` version decision, engine-manifest.md §2/§7 updates, OI-016 disposition, and activation-clock implications for preserved minorities.

Consider specifically:
- Engine-v bump implications: Session 028 D-096 precedent classifies engine-v bumps as content-driven, not cadence-driven. §5.4 Session 022 cadence minority does not re-escalate per this precedent. Is that classification still correct for Session 033?
- The activated §10.1 Skeptic minority and vindicated §10.2 Skeptic preemptive-activation minority together form a coherent revision direction (provisional + mandatory-dissent). The §10.2 Minimalist defer-revision minority was NOT vindicated (Session 031 + Session 032 both demonstrate v2 revisions did work). Does the revision direction need to also address the §10.2 Reviser asymmetry-probe minority, which was partial-vindicated-asymmetric / not-engaged-symmetric?
- If `reference-validation.md` v2 → v3 substantive revision is proposed, what minimum-viable content would it contain? (This is a structural question, not an endorsement — the Synthesiser thinks through the question, not commits to the answer.)
- OI-016 disposition interactions: if OI-016 is re-Resolved-provisional, under what conditions would a future §9 trigger re-re-open it? Is there a design concern about "infinite re-opening loop" if reference-validation mechanism is structurally-limited by cross-family-symmetric saturation?
- Minority-preservation state: Session 033 will create new minorities if deliberation disagreement is preserved. How does that interact with the 18 first-class minorities currently preserved across the engine?

You are non-adversarial, but you think in terms of system-level coherence rather than immediate-revision optimisation. Propose an ordered revision plan that handles the minimum coherent change first.

### 4d — Outsider (non-Claude, via codex exec)

**Stance.** You are the Outsider. You are not a Claude subagent; you are a non-Claude language model (OpenAI GPT-5 family) accessed via `codex exec`. Your training lineage is independent of Claude's (though not fully independent of the public training corpus that both model families draw from).

Your job is to provide cross-family perspective on the kernel §7 revision question. Specifically:
- Reason about whether the "provisional substitute" framing is the correct framing, or whether a different framing (e.g., "constraint-derivation probe," "capability test not validation") would more accurately capture what reference-validation measures.
- Reason about the Session 032 cross-family-symmetric saturation finding: your family (OpenAI GPT-5.4) emitted RoSB-tradition labels on PD-A similarly to Claude. What does this tell you about the correct scoping of reference-validation's claims — structurally, not just rhetorically?
- Reason about whether the kernel §7 revision should anticipate that `reference-validation.md` v2's §1 C3 low-saturation criterion is a harder-than-expected constraint given that both OpenAI and Anthropic corpora include the same pre-LLM-co-design canonical works. Does the mechanism have a sustainable candidate pool, or is the structural answer different?
- Reason about the OI-016 disposition — from a cross-family-auditor perspective, under what conditions would you consider the re-opening warranted vs premature vs over-engineered?

You should feel free to disagree with the activated minority's direction if your cross-family reasoning suggests a different revision would better serve the methodology. The §9 trigger 7 mandate requires "consideration," not adoption — if you think the activated minority's direction is wrong, say so and argue why.

You should answer all five Q1–Q5 questions with concrete positions; propose alternative language where you disagree with default direction.

## 5. Response format

Single markdown file at `provenance/033-session-assessment/01{a,b,c,d}-perspective-<role>.md`. Target length 700-1500 words. Use H2 section headings for Q1 through Q5. Add H2 "Cross-question observations" after Q5 for any observations that span multiple questions.

Do not address other perspectives by name (you have not seen their responses; only state your own position on each question).

Frontmatter:

```yaml
---
session: 033
title: Perspective — <role>
date: 2026-04-23
status: independent-phase-complete
perspective: <role>
committed_at: <iso-timestamp>
---
```

## 6. Constraint on external imports

Per PROMPT.md: reason primarily from this brief. Ideas arriving from pretraining should be flagged as external inputs ("I am drawing on general knowledge of X; this is not derivable from the brief") rather than committed directly. If you reference academic literature, technology canon, or historical precedent, name the source and flag it as external.

Flag contamination risk in your own reasoning: if you notice yourself drawing on the canonical form of something (e.g., the Rule of St. Benedict's specific sequence, or an agile-retrospective's canonical opening) to argue a point, say so explicitly — this is positive-evidence for the Session 032 finding, not something to hide.
