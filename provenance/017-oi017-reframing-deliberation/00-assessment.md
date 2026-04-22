---
session: 017
title: Assessment — Session 016 Audit; OI-017 Deliberation Plan (H2 Preference Stated)
date: 2026-04-22
status: complete
---

# Assessment — Session 017

## 1. Read (workspace state)

Ran `tools/validate.sh` at session open: **375 pass, 2 expected-WIP fail** (Session 017 missing from SESSION-LOG.md; `017-oi017-reframing-deliberation` directory pending content). This is the Session 013 / Session 015 pattern — session-opener WIP fails that clear at close.

Active specifications (6) unchanged from Session 016 close snapshot. OI count: **13 active** (OI-017 opened Session 016). 4 resolved.

Session 016 opened OI-017 (engine-vs-methodology reframing) with three competing hypotheses surveyed in `016-operator-reframing-assessment/00-assessment.md` §4:

- **H1 — No reframing.** Retain current framing; record observation as clarifying prose; no specification changes.
- **H2 — Full reframing.** Split PROMPT.md; add engine-definition manifest; update kernel, workspace-structure, identity; specify application-initialisation pattern.
- **H3 — Partial reframing.** New `engine-manifest.md` spec; minor updates to identity.md and PROMPT.md; no PROMPT.md split.

Session 017 operator steering (preserved verbatim at `00-operator-steering.md`): "Continue with OI-017 as preference (full reframe)." Parsed: elect OI-017 deliberation path (not Cell 1 per D-072); operator preference is H2.

## 2. Audit of Session 016 synthesis fidelity

Session 016 close directed Session 017 to audit a narrower surface: (a) Session 015 audit citations in `016-operator-reframing-assessment/00-assessment.md` §2; (b) §3 word-usage survey accuracy across specifications; (c) D-073 `[none]` triggers declaration consistency; (d) OI-017 activation trigger and preferred starting point operationally meaningful.

### 2.1 — Session 015 audit citations (Session 016 §2)

Session 016 §2.1 verified four cited raw-output locations in Session 015's `00-assessment.md` §2. Re-verification: citations to Session 014 files at `01a-perspective-architect.md` Q3 lines 67–91, `01c-perspective-skeptic.md` Q5 lines 106–122, Q7 lines 146–177, and `01d-perspective-outsider.md` Q7 line 760 are all present in the files and the content described matches. **Consistent; carries forward.**

### 2.2 — §3 word-usage survey accuracy

Session 016 §3.1 claimed "methodology" appears 15 times in PROMPT.md in two distinct senses. Spot-check via grep on PROMPT.md returns 15 occurrences (`grep -c methodology PROMPT.md` confirms). The two-sense framing (abstract-approach vs. concrete-implementation) is supportable on re-reading — PROMPT.md line 3 uses it as "building a design methodology" (the workspace's product, i.e., concrete-implementation-in-progress), while line 9 uses "The methodology itself — the mechanic of diverse perspectives reasoning together" (abstract-approach). Both senses present; §3.1 survey accurate.

Cross-check on methodology-kernel.md v4: line 15 "core process of the methodology" (concrete-implementation sense). Line 36 "This is a receptive activity" discusses Read-activity in process-level terms (concrete-implementation). The document's title "Methodology Kernel" treats "methodology" as the named thing. §3.1's claim that methodology-kernel.md uses "operational language" for "methodology" is accurate.

Cross-check on identity.md: line 27 "The methodology is referred to as Selvedge" — concrete-implementation (you can name a concrete thing; an abstract approach has harder-to-pin-down referents). §3.1's reference-handle framing accurate.

**§3 word-usage survey: verified accurate in the three highest-stakes specifications.**

### 2.3 — D-073 `[none]` triggers declaration consistency

D-073 declares `triggers_met: [none]` with rationale citing no kernel change (no d023_1), no spec revision (no d023_2, d023_3), no OI-004 state change (no d023_4), no multi-perspective originated design output (no d016_*). Reading D-073's Decision text: ratifies Option α; opens OI-017; preserves D-072. No specification file edited. No kernel edited. OI-004 unchanged. OI-017 is a new OI (not OI-004), so d023_4 does not apply per `multi-agent-deliberation.md` v3 §D-023 wording. The `[none]` declaration is consistent. **Verified.**

### 2.4 — OI-017 activation trigger and preferred-starting-point operational meaningfulness

OI-017's recorded activation trigger: "first Session 017+ electing to deliberate OI-017." Session 017 has elected, per operator steering. The activation trigger has fired cleanly; this session is the activation. Preferred starting point: H1/H2/H3 hypothesis frame with explicit permission for additional hypotheses. This is the design frame for the current deliberation; operational meaningfulness is demonstrated by the deliberation being executable against it. **Verified.**

### Audit overall verdict

Session 016 is clean on all four audit dimensions. No substantive new-eyes findings; no revision-triggering items surfaced. The §3 surveying and §4 hypothesising steps are preserved as input-to-deliberation for this session.

## 3. Deliberation plan

### 3.1 — Scope

OI-017 deliberation:
- Primary question: should the workspace adopt the engine-vs-methodology reframing? (H1 / H2 / H3, or additional hypothesis)
- If reframing is adopted: which specifications change, how does PROMPT.md reorganise, is a new `engine-manifest.md` specification warranted, how does identity.md interact, how is external-application initialisation specified?
- Adversarial counter-position required: Skeptic carrying identity.md Reopening-condition-1 (external adoption unmet) and Session 012 refuse-to-name minority forward.

### 3.2 — Perspectives to convene

Four perspectives per the Sessions 005–014 pattern (3 Claude + 1 non-Claude Outsider via `codex exec`):

- **Architect (Claude Opus 4.7).** Assigned hypothesis: **H2 advocate**. Role: structural-clarity designer; argue that pre-specifying engine/application separation pays down the latent-ambiguity debt and enables external use as a first-class concern. Named after Session 014's Architect role (mechanism-designer); consistency of role-name across sessions aids future reading.
- **Operationalist (Claude Opus 4.7).** Assigned hypothesis: **H3 advocate**. Role: viability-focused, step-size-reasoning; argue that partial reframing is the right increment — name the distinction, defer the full restructure until an actual external application forces it. Named after Session 014's Operationalist.
- **Skeptic (Claude Opus 4.7).** Assigned hypothesis: **H1 advocate (no reframing)**. Role: adversarial, carries forward Session 012 refuse-to-name minority and Session 013 Skeptic strong-pause pattern; argues identity.md Reopening condition 1 (external adoption) is unmet, so pre-specifying engine-vs-application infrastructure is speculative design the methodology's preservation discipline argues against.
- **Outsider (non-Claude via codex exec to OpenAI GPT-5).** Unassigned hypothesis; instructed to reason from scratch. May advocate any of H1/H2/H3 or propose an additional hypothesis. Role: cross-model variance; per Sessions 005–014 precedent, Outsider's independent position is the primary cross-model-honesty signal.

Adversarial requirement (kernel §3): Skeptic. Non-Claude requirement (D-023_1 fires if kernel revised under H2/H3; d016_2 fires if new spec created under H2/H3): Outsider.

### 3.3 — Brief discipline

Per `multi-agent-deliberation.md` v3 §Stance Briefs: shared sections (methodology context, problem statement, design questions, response format, external-imports constraint) are byte-identical across perspectives; only role-specific stance varies.

The operator's preference (H2) is included in the shared Methodology Context section so all perspectives see it as input. Role-specific stances do NOT re-state the preference — each perspective is assigned their hypothesis independently of operator preference. This handling is designed to:

- Honour the PROMPT.md anti-silent-import discipline (operator preference is surfaced, not hidden).
- Honour the OI-015 laundering-enforcement requirement (preference is re-examined as a choice, not absorbed as given).
- Preserve the brief-priming-absent streak (seven consecutive sessions) — role-specific stances do not tilt perspectives toward the operator-preferred hypothesis.

### 3.4 — Convergence-vs-preference interpretation rule

If deliberation converges on H2 (matching operator preference), the synthesis must distinguish reasoning-led convergence (three independent rationales supporting H2) from preference-primed anchoring (all perspectives agreeing because the operator said so). The distinction is verifiable by checking whether each perspective's raw output reproduces the operator's stated reasons verbatim (preference-priming signal) or reaches H2 from distinct reasoning paths (genuine convergence).

If deliberation converges on H1 or H3 (reasoning-led conclusion departing from operator preference), the Decide activity must reconcile: either adopt the reasoning-led conclusion (operator's own Session 016 framing authorises this — "engine to determine"), or return to user for further steering. The default is the former; the latter is available if the decision-maker judges the reasoning insufficient.

### 3.5 — Design questions for the deliberation

Seven questions for each perspective to address:

- **Q1.** Should the workspace adopt a reframing? State your assigned hypothesis and give your strongest reasoning for it, including the main cost.
- **Q2.** If reframing is adopted, which existing specifications need to change, and in what shape? (Identify specific files and specific changes.)
- **Q3.** How should PROMPT.md be reorganised under your hypothesis? (Split into multiple files / single PROMPT.md with internal branches / no change / other.)
- **Q4.** Should a new `engine-manifest.md` (or similarly-named) specification be created? If yes, what does it contain at minimum? If no, why not?
- **Q5.** How does the reframing interact with `identity.md`'s Selvedge naming and Reopening conditions? (Does Selvedge name the engine, the methodology, both?)
- **Q6.** What is the activation path for external applications under your hypothesis? How does someone else initialise a fresh application workspace?
- **Q7.** State the strongest argument AGAINST your assigned hypothesis (or, for Outsider, against your independently-reached position). What evidence or condition would cause you to abandon it?

### 3.6 — Decision surface

Expected decisions after deliberation:
- **D-074:** hypothesis selection (H1 / H2 / H3 / other). If H2 or H3: specification revisions authorised.
- **D-075:** OI-017 state change (resolved or narrowed). OI-007 count adjustment.
- **D-076:** OI-004 housekeeping (this is a required-trigger deliberation; tally advances 5-of-3 → 6-of-3; criterion-3 cumulative gains Outsider-sourced contributions).

Depending on hypothesis selected, additional decisions may be needed for specific revisions (kernel v4 → v5 if H2; new spec creation if H2 or H3; identity.md revision if H2).

### 3.7 — Budget and stop-points

Candidate stop-points:
- **Stop 3a — Decision-only.** Deliberate and decide; defer revision execution to a subsequent session. Minimises Session 017 risk; provides user ratification opportunity before revisions execute.
- **Stop 3b — Execute if adopted.** If H2 or H3 is decided, execute revisions within Session 017. Follows Sessions 009/011/014 precedent (kernel revision + spec creation in the same session).

**Proposed default:** Stop 3b (execute if adopted), with halt-for-user-ratification after synthesis and before execution if the deliberation's outcome departs materially from H2. This honours the operator's H2 preference — if the deliberation reaches H2 and the user has already preferenced H2, further ratification is redundant; if the deliberation diverges, user ratification is the circuit-breaker.

## 4. Proceeding

Proceeding now to:
1. Draft shared brief (`01-brief-shared.md`).
2. Draft role-specific stances.
3. Launch 3 Claude subagents in parallel + Outsider via `codex exec`.
4. Synthesize.
5. Decide.
6. If H2 or H3 decided: execute revisions (halt for user ratification if convergence departs from H2).
7. Record manifests, participants.yaml, close.
8. Update SESSION-LOG and open-issues.
9. Commit and push.
