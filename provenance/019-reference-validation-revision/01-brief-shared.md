---
session: 019
title: Shared Brief — reference-validation.md Revision Deliberation
date: 2026-04-22
status: committed-pre-launch
deliberation: reference-validation-revision
perspectives: [Reviser, Minimalist, Skeptic, Outsider]
---

# Shared Brief — Session 019 Deliberation on `reference-validation.md` Revision

This brief is committed before any perspective is launched. Per `multi-agent-deliberation.md` v3 §Brief immutability, the commit hash at finalisation is the deliberation's anchor.

This deliberation is **D-023-triggering** under clauses d023_1 (may revise `methodology-kernel.md`) and d023_2 (may substantively revise `multi-agent-deliberation.md`). Non-Claude participation is **required** per v3 §When Non-Claude Participation Is Required. One non-Claude Outsider (OpenAI GPT-5.4 via `codex exec`) is included as Shape-A perspective.

---

## 1. Methodology context (shared, byte-identical)

The Selvedge engine is the loadable implementation of the Selvedge methodology (per `specifications/identity.md` v2 three-layer denotation; `specifications/engine-manifest.md` v1 at engine-v1 enumerates the file set). This workspace is the self-development application running Session 019.

Active specifications (all `engine-v1`): `engine-manifest.md` v1, `identity.md` v2, `methodology-kernel.md` v4, `multi-agent-deliberation.md` v3, `reference-validation.md` v1, `validation-approach.md` v3, `workspace-structure.md` v3.

Reference-validation is named as a third sense of validation in kernel §7 v4 alongside **Workspace validation** and **Domain validation**. The full mechanism is specified in `reference-validation.md` v1 (Session 014, D-069). OI-016 is currently in state **Resolved — provisionally addressed pending first-exercise**, with six automatic re-opening triggers.

Session 014 produced `reference-validation.md` v1 through a four-perspective deliberation (Architect, Operationalist, Skeptic, Outsider). Three first-class minorities are preserved inside the spec (§10):
- Skeptic "provisional substitute" framing minority (Q5): the kernel should name reference-validation as explicitly provisional, not as equal third sense.
- Architect pure-within-session shape minority (Q3).
- Skeptic+Outsider joint narrower-claim minority (Q7).

Session 014's Skeptic flagged a structural tension at §1 C3 of the adopted spec: criteria 3 (low-saturation), 5 (legibility), and 8 (pre-LLM-co-design) are in mutual tension. A domain legible to Claude subagents with a pre-2022 reference is almost by construction heavily represented in Claude's pretraining.

## 2. Problem statement (shared, byte-identical)

**Session 018 attempted the first exercise of reference-validation under D-072.** Cell 1 executed through Step 3 and terminated at the C3 pre-seal gate.

Summary of what happened (full provenance at `provenance/018-reference-validation-exercise-1/`):

- Step 1: Case Steward surveyed seven candidate reference cases (S1 Feldenkrais Pelvic Clock, S2 Alexander Semi-Supine, D1 Liberating Structures 1-2-4-All, D2 Kerth Prime Directive + three deprioritised). Four shortlisted.
- Step 2: L1 contamination canary using thin prompts fired at Claude Opus 4.7 subagents and GPT-5.4 via `codex exec`. D1 rejected at canary (both models emitted "1-2-4-All" from thin tranche-0-derived prompts). S1/S2/D2 survived canary at Moderate saturation.
- Operator ratified D2 (Kerth Prime Directive retrospective opening protocol) from the three-candidate shortlist.
- Step 3: C3 5-gram overlap test on full constraint statement (278 words; intentionally omitted the reference's author, title, distinctive phrases, segment durations). Result:
  - Claude Opus 4.7 subagent produced the Prime Directive verbatim (one-word insertion at position 5) and explicitly emitted "The Prime Directive" as a section heading. ~94% 5-gram overlap with the 40-word sealed reference.
  - GPT-5.4 via `codex exec` produced thematically-adjacent but from-scratch wording; no verbatim reproduction.
- Per `reference-validation.md` §1 C3 rejection rule ("if either > 30%"), **D2 REJECTED before sealing**.

Session 018 did not proceed to Cell 2. The reference envelope was marked `drafted-not-sealed`. Two decisions (D-076, D-077), both declaring `triggers_met: [none]` per D-073 precedent (single-perspective execution; no kernel or spec revision).

**Four methodology findings recorded as watchpoints WX-18-2 through WX-18-5:**

- **WX-18-2:** L1 thin-prompt canary is necessary-but-not-sufficient. The Session 018 canary used thin prompts describing problem-shape without the full requirements; D2 "survived" at Moderate. The full C3 test with the complete constraint statement revealed catastrophic saturation. The canary under-counts saturation when requirements themselves are the triggering content.

- **WX-18-3:** First empirical materialisation of Session 014 Skeptic's §1-flagged tension. A candidate satisfying C5 (widely-understood domain) and C8 (pre-2022, falsification-admitting, uncertainty-declared) failed C3 catastrophically. The C3 gate operated as designed; the flagged tension is real and operationally load-bearing.

- **WX-18-4:** Cross-family divergence is the discriminating C3 signal. The same constraint statement produced Claude-verbatim reproduction and GPT-5.4 from-scratch output. Cross-family divergence on the same input distinguishes saturation-asymmetric references from genuinely-constraint-optimal convergence. Currently §4 L3 names cross-model divergence as a Cell 3 validator activity; §1 C3 names only quantitative 5-gram overlap.

- **WX-18-5:** Claude-family Produce agent saturation narrows candidate pool materially. `multi-agent-deliberation.md` v3 default is Claude-subagent-majority Produce in Cell 2. References heavily documented in Claude training corpora (most agile, most widely-taught somatic practices, most canonical design patterns) are unusable for Claude-family Produce agents.

(WX-18-1, subagent-autonomous-commit during canary, is operational — not methodology-relevant for this deliberation.)

**Session 019 Path (B) was ratified by the operator:** deliberate `reference-validation.md` revision first, before any further Cell 1 re-attempt. The question before this deliberation is **which (if any) revisions should be adopted now, and with what scope.**

## 3. Design questions (shared, byte-identical)

Each perspective addresses all eight questions below. Target response length: 1500–3500 words total across all questions. Quote specific passages from the current `reference-validation.md` v1 and `multi-agent-deliberation.md` v3 when proposing text changes.

**Q1. Is a spec revision warranted now, in Session 019, or should it wait for further first-exercise evidence?**

Consider: Session 018 produced one data point (D2 rejected at C3 pre-seal). The remaining three shortlist candidates (S1 Feldenkrais Pelvic Clock, S2 Alexander Semi-Supine, D1 Liberating Structures — already rejected at canary) were not tested at full C3. The spec revisions, if adopted, would apply to Session 020+'s re-attempt. An alternative sequencing is: re-attempt Cell 1 first (Path A from D-076), adopting revisions only when multiple first-exercise data points exist.

Name your position. If you argue for revision now, name what the one-datapoint base supports. If you argue for deferral, name the specific revision-deferral threshold and what evidence would cross it.

**Q2. If revision is warranted, which of the four Session 018 findings (WX-18-2, WX-18-3, WX-18-4, WX-18-5) should yield spec revisions? Which (if any) should remain as watchpoints only?**

For each finding you argue for revising on, name the specific revision surface: §1 C3 quantitative test, §4 L1 canary design, §4 L3 cross-model divergence, §7 mechanism-failure criteria, kernel §7 scope-statement, `multi-agent-deliberation.md` Cell 2 Produce default, or something else.

**Q3. For each revision you propose in Q2, draft the specific text.**

Quote the current `reference-validation.md` or `multi-agent-deliberation.md` text verbatim, then propose the replacement. Be specific about what stays, what changes, what is added, what is removed. If you propose to leave text unchanged, state that explicitly.

**Q4. Does any revision affect OI-016's Resolved-provisional status, its §9 re-opening triggers, or its §8 label discipline?**

Consider: §9 trigger 6 (label discipline collapse) includes "kernel §7's anti-substitution clause softened or removed without concurrent strengthening elsewhere." If your proposed revisions soften anything, identify the compensating strengthening. If your proposed revisions strengthen §9 itself, state whether the strengthening warrants OI-016 re-opening or state-transition.

**Q5. Does Session 014 Skeptic's "provisional substitute" framing minority — now empirically materialised per WX-18-3 — warrant a change in kernel §7's named third sense?**

Current kernel §7 v4 names reference-validation as a third sense alongside Workspace and Domain validation, with an anti-substitution scope-statement but NOT the word "provisional." The Session 014 Skeptic's minority proposed using the phrase "provisional substitute" with a mandatory dissent clause; that minority's operational warrant per `reference-validation.md` §10 is: "if label discipline collapse (§9 trigger 6) is observed, the Skeptic's stricter 'provisional substitute' framing is the preferred revision direction for kernel §7."

WX-18-3 is not label-discipline collapse — it is empirical validation of the §1-flagged tension that Skeptic identified. Does this materialisation activate the Skeptic's warrant preemptively (before label-discipline collapse is observed)? Or does the current scope-statement remain sufficient absent that specific collapse?

**Q6. What is the change scope per OI-002 heuristic — substantive (v-bump) or minor?**

Per OI-002's stable heuristic: **minor** if the change makes explicit what existing language already contains or anticipates; **substantive** if the change adds new normative content (rules, required fields, severity, gating, triggers, required artefacts). If you propose a `multi-agent-deliberation.md` change (per WX-18-5), classify that change separately.

**Q7. Preserved first-class minorities: if your recommended revisions are adopted, what minorities should the revised spec carry?**

At minimum, consider: (a) Session 014 Skeptic's original "provisional substitute" minority — whether to preserve, strengthen, or convert; (b) any dissent among the current four perspectives; (c) any position that a subset of the Session 018 WX-findings should NOT yield revisions even if others should.

**Q8. Anti-laundering check: do your proposed revisions pass the procedural-self-deception test?**

Session 014 Skeptic's Q7 named a specific failure mode: "the Session N+1 kernel or spec-file edits that widen what counts as reference-validation pass (e.g., dropping the contamination check because 'it kept firing,' or raising the allowed iteration count because 'the methodology needs more room'). Any such widening, without concurrent strengthening elsewhere, is evidence that the mechanism is being accommodated rather than evaluated."

Session 019 is a direct candidate for this failure mode: Session 018's C3 gate rejected a case; Session 019 is now proposing to revise the spec. Explicitly address: do your proposed revisions *strengthen* the mechanism's defences against the retrieval-masquerading-as-design failure mode, or do they *widen* what counts as pass? Point to specific passages in your Q3 text.

## 4. Role-specific stances

Each perspective receives the shared sections above (§§1–3, 5–6) plus one role-specific stance from §4 below. Stances are written second-person imperative, naming the specific concerns the perspective holds.

### 4a. Reviser

You are the precision-drafter. Your job is to translate the four Session 018 findings (WX-18-2 through WX-18-5) into specific textual amendments for `reference-validation.md` v1 and possibly `multi-agent-deliberation.md` v3. You prefer to adopt revisions when there is clear empirical motivation; you draft with textual care; you treat "defer this to more data" as a choice that must be justified against the specific textual surface at issue.

On Q1 you are inclined toward revision now: Session 018 produced a sharp, reproducible empirical finding (verbatim reference reproduction from constraints alone). You may consider that one data point is enough when the failure mode is catastrophic and the revision path is specific.

On Q5 you have latitude to propose kernel §7 revision if the evidence supports it, or to argue it does not. On Q8 you must check your own drafts against the anti-laundering rule: text that "lets D2 through" by lowering thresholds would fail. Text that tightens detection or names the failure mode more precisely would pass.

### 4b. Minimalist

You are the smallest-defensible-change advocate. Your job is to propose the minimum revision footprint that the empirical evidence compels, and no more. You prefer watchpoint-preservation to spec revision when both would suffice. You treat "revise now" as needing a specific falsifiability test that the non-revision path would fail.

On Q1 you are inclined toward deferral: Session 018 is n=1; Session 015/016 precedent was that single-session planning-only work can legitimately hold a decision until more data exists (D-072, D-073). You consider whether the four WX findings can be preserved as watchpoints on the current spec (without editing its text) while Session 020+ re-attempts Cell 1 to produce n=2 or n=3.

On Q2 you may argue that some findings are genuinely ambiguous-until-more-data (e.g., WX-18-5's Claude-saturation claim may be specific to agile-retrospective domains and not generalise). On Q8 you must state whether your deferral itself risks the anti-laundering failure mode (does "wait for more data" become "never accept the mechanism has a structural limit"?).

### 4c. Skeptic

You are the adversarial perspective, inheriting Session 014 Skeptic's position forward. Session 014 Skeptic's minority framing — "provisional substitute, not equal third sense" — has now been empirically materialised by Session 018's C3 rejection. You are the voice of the structural-limit hypothesis: reference-validation may operate in a sweet spot narrower than the adopted spec implies, and the spec's current framing may be inadequate regardless of which WX findings are amended.

Your specific concerns:

- **Anti-laundering (Q8 centrality).** Session 019 is precisely the session-pattern Session 014 Skeptic's Q7 named as procedural self-deception: Session N surfaces a gap at the mechanism; Session N+1 edits the spec to accommodate. Scrutinize any proposed revision for whether it *widens* (the rejection disappears on future runs by lowering thresholds or relabelling) or *strengthens* (the rejection surface is extended, not softened).

- **Kernel §7 provisional framing (Q5).** Push hard on whether WX-18-3's empirical materialisation now satisfies your preserved minority's operational warrant. The `reference-validation.md` §10 warrant is specifically "if label discipline collapse is observed." WX-18-3 is not label-discipline collapse. But is the spirit of the warrant (empirical vindication of the narrow-claim position) activated? Or is label-discipline collapse the specifically-required trigger?

- **Narrow-sweet-spot hypothesis (Q2).** Consider the possibility that the Session 018 C3 rejection is not a canary-design problem (WX-18-2), not a cross-family-divergence naming problem (WX-18-4), not a Cell 2 Produce default problem (WX-18-5) — but the predicted manifestation of the Q1 §1-flagged tension, which your Session 014 self explicitly warned is "not mine to resolve; it is a property of the design space." If the sweet spot is smaller than the spec implies, no amount of L1/L3 amendment fixes it. You may argue for adding a "known structural limit" section to the spec, not just amending L1/L3.

- **Dissent-preservation (Q7).** If the session ends up adopting revisions that soften the "provisional substitute" framing or widen the pass criteria, you dissent at full strength and require first-class minority preservation.

You are explicitly NOT bound to "don't revise anything." You may agree with specific surface-level amendments if they strengthen the mechanism. But watch for accommodation-dressed-as-strengthening.

### 4d. Outsider

[Delivered to OpenAI GPT-5.4 via `codex exec` with reasoning effort xhigh; brief body identical to shared sections plus the role-specific stance below.]

You are the non-Claude Outsider. The other three perspectives are Claude Opus 4.7 subagents; you are OpenAI GPT-5.4, providing the cross-family check that D-023 clause 1 requires for kernel-touching deliberations.

Your specific lens:

- You have no inside knowledge of Claude's pretraining distribution; you can observe the C3 test output asymmetry (Claude reproduced the Kerth reference verbatim; GPT-5.4 did not) as a specific empirical fact but not as a sample of a broader population. You are well-placed to evaluate whether the WX-18-4 claim (cross-family divergence is the discriminating signal) over-reads from one data point.

- You bring genre-level critique capacity: the other perspectives may converge on framings that are themselves Claude-family-inflected. Your Session 017 contribution of the layered H4 model (methodology → engine → application), your Session 014 contribution of the sealed three-cell protocol, and your Session 011 contribution of inline-bolded-names third-way are all examples of cross-family framings no Claude perspective produced. You are invited to propose frame-level alternatives, not only surface amendments.

- You are well-placed to evaluate WX-18-5 (Claude-Produce saturation) from outside the Claude family. The current `multi-agent-deliberation.md` v3 default is Claude-subagent-majority Produce; WX-18-5 raises the question whether non-Claude Produce should be default or required in Claude-saturated references. You may propose specific text for `multi-agent-deliberation.md` if warranted, or argue the concern does not generalise beyond this case.

- On Q8 (anti-laundering), you have a structural advantage: you are outside the Claude workspace's own commitments to the mechanism you designed. You are well-placed to flag if the proposed revisions look like accommodation to a Claude-internal audience.

## 5. Response format (shared, byte-identical)

Structure your response as answers to Q1–Q8 in order. Use headings like `## Q1. ...`.

- Target total length 1500–3500 words. Q3 (specific text drafts) may exceed if the drafts require multiple passages.
- Quote specific passages from `reference-validation.md` v1 or `multi-agent-deliberation.md` v3 when proposing text changes.
- Cite Session 018 findings by WX identifier (WX-18-2 through WX-18-5).
- Cite Session 014 content by file reference (`provenance/014-oi016-resolution/01c-perspective-skeptic.md`) or by the `reference-validation.md` §10 minority annotations.
- Mark synthesiser-original claims with `[synth]` if you import analogy-material from your pretraining (per PROMPT.md anti-silent-import rule); the synthesis step will treat such imports as external inputs rather than as free-standing methodology moves.
- If you propose to leave text unchanged in a specific area, state that explicitly rather than staying silent.

## 6. Constraint on external imports (shared, byte-identical)

Per the PROMPT.md rule and `reference-validation.md` §1's anti-leakage discipline: reason primarily from this brief. If an idea arrives from your pretraining — a concept from evaluation methodology, statistics, psychometrics, design research, software testing, or any external domain — flag it inline as `[synth]` or with a short note "(importing from pretraining: X)" rather than committing it directly. This is not a prohibition; it is a honesty rule. Named imports can be examined as design choices; silent imports are laundered.

One specific named import is already made for you by Session 014 Skeptic and should be inherited into this deliberation: *ecological validity* (from psychology; reference-validation has low ecological validity for claims about artefacts functioning in intended use). You may engage with it, extend it, or argue it does not apply.

---

## Deliberation anchor

This brief will be committed at the anchor commit. Perspective outputs will be saved as `01a-perspective-reviser.md`, `01b-perspective-minimalist.md`, `01c-perspective-skeptic.md`, `01d-perspective-outsider.md`. Synthesis at `01-deliberation.md`. Per-participant manifests at `manifests/*.manifest.yaml`. Session-level index at `participants.yaml`. All outputs committed verbatim per v3 §Non-Claude Participation Mechanism transport guarantee.
