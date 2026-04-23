---
session: 033
title: Perspective — Reviser
date: 2026-04-23
status: independent-phase-complete
perspective: reviser
committed_at: 2026-04-23T00:00:00Z
---

## Q1 — Provisional framing

**Position.** Rename the third sense in kernel §7 from "Reference validation" to "Provisional reference substitute," and update downstream label language accordingly. Retain "reference-validation exercise" as the name of the *procedure* (the sealed three-cell protocol); the sense-name change applies to what the procedure *produces* at the level of claim.

Rationale. The Session 014 Skeptic warrant was preserved because softening reduces signal. The adopted v4 / v5 text took the content of that warrant — "does not establish intended-use functioning" — but omitted the word "provisional." §9 trigger 7 firing (n=2 structurally-different-domain rejections, now including a cross-family-symmetric instance) is exactly the operational signal the Skeptic named as sufficient to force the stronger framing. A scope-paragraph qualifier alone leaves the sense-name load-bearing in citations, frontmatter, and session summaries; readers and downstream authors will refer to "the reference-validation result" and drop the paragraph. Renaming the sense puts provisionality on the label that travels.

Draft replacement paragraph (kernel §7, third bullet block):

> **Provisional reference substitute** applies when a session produces an external-intent artefact and no domain-actor is available. It is a *provisional substitute* for Domain validation, not an equal-but-distinct sense of validation. A reference-validation exercise — the procedure by which the substitute is produced — pairs the methodology's Produce step (run blind against a staged constraint tranche set whose emergent constraints surface during the run) with comparison against a pre-selected documented proven solution the Produce agents do not see. The exercise runs across a small number of sessions in a sealed three-cell protocol (Curation, Produce, Validation) specified in `specifications/reference-validation.md`. The exercise records constraint-satisfaction, structural correspondence, cross-model divergence, and a contamination audit.

Label update. Artefacts passing the exercise carry `validation: reference-substitute-provisional` in frontmatter (not `reference-validated`). Any prior artefact carrying the old label is grandfathered with a note in its frontmatter; no retroactive rewriting of sealed session records.

## Q2 — Mandatory-dissent clause

**Position.** Yes, include a mandatory-dissent clause. Scope: any citation of a provisional-reference-substitute result that either (a) leaves the workspace (external-facing) or (b) is used as premise for a methodology-level claim inside the workspace. Not required for purely internal session-to-session reference (where the sealed record already carries the dissent).

Exact clause text, to be inserted as a fourth paragraph in the v6 §7 block, immediately after the scope-statement paragraph:

> **Citation discipline.** Any citation of a provisional-reference-substitute result outside the producing session — in external-facing artefacts, in methodology-level claims, or in subsequent sessions treating it as evidence for the methodology's capacity — must be accompanied by (i) the `reference-substitute-provisional` label, (ii) a named dissenting view from the sealed record or, if no dissent was recorded in the exercise, an explicit acknowledgement of contamination risk naming the saturation profile of the reference domain (copyrighted / public-domain; single-family / cross-family-symmetric), and (iii) a pointer to the contamination audit. Citations that drop any of (i)–(iii) are workspace-invalid and must be repaired before the containing artefact seals.

Enforcement mechanism. Three layers, in decreasing strength:

1. **Sealing gate.** The Validate activity (§7) checks any artefact citing a provisional-reference-substitute result for the three required elements before the session closes. Failure returns to Produce. This is a session-scoped check; it does not require new tooling.
2. **Frontmatter propagation.** The `validation: reference-substitute-provisional` label propagates into any artefact that cites the result. If an artefact cites multiple validation sources, the most-provisional label wins at the frontmatter level. (This is the contamination-label analogue of the seven-layer defence stack: once provisional, always provisional downstream.)
3. **Close-rotation check.** Add to the close-rotation checklist: "verify citation discipline on any provisional-reference-substitute citations introduced this session." This catches drift across sessions without requiring a separate activity.

Why this scope and not broader. Requiring dissent on every internal citation would be costly and would dilute the signal by making the discipline routine. Requiring it only at external-facing citations would miss the case where a methodology-level claim inside the workspace (e.g., "the methodology can produce X") is built on a provisional result without the dissent travelling. The (a)-or-(b) scope captures the load-bearing cases.

## Q3 — Scope-statement strengthening

**Position.** Strengthen. Current language ("does not establish that the artefact functioned in its intended use. It does not substitute for Domain validation when a domain-actor is available") is necessary but not sufficient after Session 032. It says nothing about *what kind of evidence it is even when it passes* — specifically, it does not address the saturation-gate false-negative pattern or the cross-family-symmetric case.

Draft replacement for the bold scope-statement paragraph (kernel §7):

> **Provisional reference substitute supplies evidence about the methodology's capacity to derive artefacts under stated constraints *in domains where the reference is not heavily represented in pretraining corpora*. It does not establish that the methodology is working, only that it can produce outputs satisfying stated constraints under conditions where pretraining contamination does not dominate. It does not establish that the artefact functioned in its intended use. It does not substitute for Domain validation when a domain-actor is available. Where pretraining saturation is cross-family-symmetric — i.e., the reference tradition is densely represented across multiple model families — the substitute's evidential value further diminishes, because cross-model divergence (a primary signal in the contamination audit) degrades as a detector. Passing L1a (asymmetry probe) does not predict passing L1b (label-discipline check); both must be cleared, and neither alone is sufficient.**

Grounding in Session 032. The PD-A Rule of St. Benedict result is the empirical hook for the cross-family-symmetric clause. The saturation-gate false-negative pattern (L1a PASS / L1b REJECT in Session 032; analogous cell-level pattern in Session 018) is the hook for the L1a-does-not-predict-L1b clause. The public-domain-constraint elevated-risk finding is captured indirectly by the "heavily represented in pretraining corpora" phrase, which names the mechanism (corpus representation) rather than the proxy (public-domain status), and therefore generalises beyond the PD case to any densely-trained tradition.

## Q4 — Cascading revisions

**Position.** Minimum cascading, but more than engine-manifest alone. The smallest coherent set:

1. **methodology-kernel.md** bumps to v6. §7 replaced per Q1/Q2/Q3 drafts above. No other §-level changes required; the nine activities and their names are unchanged.
2. **reference-validation.md** bumps to v3. Required changes:
   - §1 (or equivalent framing section): update to describe the spec as governing the procedure that produces a *provisional reference substitute*, not a third sense of validation.
   - §9: add a new trigger 8 (or extend trigger 7) covering the cross-family-symmetric saturation case as a distinct pattern from the original single-family rejection pattern, since Session 032 established these as methodologically different signals.
   - Label section: update the label from `reference-validated` to `reference-substitute-provisional` with grandfathering note.
   - Contamination-audit section: add a requirement that the audit record the saturation profile (single-family / cross-family-symmetric) explicitly, since the Reviser asymmetry-probe does not detect the cross-family case and this must be surfaced elsewhere.
3. **engine-manifest.md** §2 (version index) and §7 (validation senses or equivalent) updated for the v6 kernel bump and v3 reference-validation bump.
4. **multi-agent-deliberation.md** — no change required. v4 already governs this session's shape.

Why reference-validation.md v3 is required rather than deferrable. The label change and the saturation-profile audit requirement are load-bearing for the citation-discipline clause in Q2 to be enforceable. If reference-validation.md still names the output `reference-validated`, the kernel text and the spec conflict, and operators will default to the spec when producing frontmatter. The v3 bump is not a gold-plating option; it is the minimum to keep the kernel and the procedural spec coherent.

Why multi-agent-deliberation.md does not cascade. The required-non-Claude-participation property already active in v4 handled this session's deliberation correctly. Nothing in the Q1–Q3 revisions changes the shape of deliberation.

## Q5 — OI-016 disposition

**Position.** Transition Open → Resolved-provisionally (v2), with the new disposition being: *the provisional-substitute framing is the resolution, and the resolution is itself labelled provisional because cross-family-symmetric saturation is a newly-observed pattern (n=1 clean instance in Session 032) whose behaviour under further exercises is not yet characterised.* Do not transition to Resolved (unqualified), because that would assert confidence the n=1 evidence does not support. Do not keep Open, because Open-with-no-revision-pending is a stale state; the revision is happening this session.

Operational form. OI-016 frontmatter status becomes `resolved-provisionally-v2`, with a history entry recording: Session 014 resolved-provisionally → Session 032 re-opened (§9 trigger 7 fire) → Session 033 resolved-provisionally-v2 (kernel v6 + reference-validation v3 adopted). A new §9 trigger (trigger 8 or extended trigger 7) governs any future re-opening: if a third rejection fires in a further structurally-different domain, or if a cross-family-symmetric L1a PASS / L1b REJECT recurs, OI-016 re-opens to Open and the Session 033 resolution is itself contested.

Residual risk the disposition acknowledges. The substitute remains provisional; the citation discipline is new and untested across multiple sessions; the cross-family-symmetric pattern has n=1 and may behave differently under different tradition densities. A second OI (call it OI-017 — cross-family-symmetric saturation detection) may be appropriate to open now, separate from OI-016, to track the detection-mechanism gap (Reviser asymmetry-probe does not see it) as its own problem rather than folding it into the validation-pathway OI.

## Cross-question observations

The five answers above form a coherent package: rename the sense (Q1) so provisionality travels on the label; mandate dissent (Q2) so citations cannot quietly shed it; strengthen the scope statement (Q3) to name the saturation mechanism rather than the proxy; cascade to reference-validation v3 (Q4) so the spec and kernel do not diverge; resolve OI-016 provisionally-v2 (Q5) with a new trigger covering the cross-family-symmetric pattern, and consider opening OI-017 to track the detection gap separately.

What the revisions buy. They remove the single-word gap between the Session 014 Skeptic warrant and the kernel text. They make the citation-time behaviour match the production-time caution. They give the cross-family-symmetric pattern a place to live in the spec rather than floating as a session-artefact finding. They vindicate the Session 019 preemptive-activation warrant structurally without requiring retroactive rewriting of Session 019's decision.

What residual risk remains. The substitute is still a substitute; no amount of relabelling converts capacity-evidence into intended-use-functioning-evidence. The citation-discipline clause depends on session-level enforcement and has not yet been tested across a sealing cycle. Cross-family-symmetric saturation is n=1; a single further instance could invalidate the "pattern" framing or reveal a sub-pattern. The Reviser asymmetry-probe detection gap is named but not closed by this session's work.

External-input flag. The phrase "corpus representation" in Q3 is a general machine-learning framing ordinary in public pretraining discussion; I use it as plain language, not as citation. No academic sources are imported.
