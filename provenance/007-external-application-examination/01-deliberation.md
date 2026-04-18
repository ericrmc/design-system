---
session: 007
title: Deliberation — External Application Re-examination (synthesized)
date: 2026-04-19
status: complete
synthesizer: session-007 orchestrating agent (Claude Opus 4.7, same model family as 3 of 4 deliberators; not the Outsider's model family)
synthesizer-independence: did not play any of the four perspectives (Generalist, Outsider, Skeptic, Steward)
deliberation-anchor-commit: cfb761751c0f8681012c9eebd5ffcfdcc54a358a
perspective-order: alphabetical by role name (Generalist, Outsider, Skeptic, Steward)
participants_family: cross-model
cross_model: true
non_claude_participants: 1
---

# Deliberation — Session 007: External Application Re-examination

## How This Deliberation Was Conducted

Four perspectives were convened. Three were parallel context-isolated Claude subagents (Claude Opus 4.7) launched via Claude Code's Agent tool: The Generalist, The Steward, and The Skeptic (required adversarial). The fourth, The Outsider, was a non-Claude participant: OpenAI GPT-5 (model id `gpt-5.4`, OpenAI session id `019da2e3-d854-72c2-bd39-42545da77631`) invoked via the `codex` CLI in non-interactive (`exec`) mode, `sandbox: read-only`, `reasoning effort: xhigh`. All four received the shared brief committed at `cfb761751c0f8681012c9eebd5ffcfdcc54a358a`. None saw the others' outputs during the independent phase. The Outsider's response is committed verbatim — including the CLI banner, the prompt echo, the primary response, the `tokens used` line (18,723 tokens), and the end-of-stream duplicated response — per D-021's transport-faithfulness requirement. Raw outputs are preserved at:

- `01a-perspective-generalist.md` (Claude Opus 4.7)
- `01b-perspective-steward.md` (Claude Opus 4.7)
- `01c-perspective-skeptic.md` (Claude Opus 4.7, required adversarial)
- `01d-perspective-outsider.md` (GPT-5 via Codex CLI)

Perspectives are presented alphabetically throughout this synthesis to reduce synthesizer-ordering bias (D-018).

**This is the methodology's third heterogeneous-participant deliberation.** Session 005 was the first; Session 006 was the second. Whether this session's deliberation advances OI-004's sustained-practice tally from 2 of 3 toward 3 of 3 depends on whether any D-023 trigger in fact fires for the resulting decisions; that is determined in the Decide activity and recorded in D-049 (OI state).

## Synthesis Conventions

Following D-018 and reaffirmed in Sessions 005 and 006: claims attributing a position to a perspective cite the source file and question; claims not directly sourced are marked `[synth]`; load-bearing language is quoted rather than paraphrased; dissent is preserved as dissent; convergence (all perspectives independently reached a similar conclusion) is distinguished from coverage (only one perspective raised a point, others silent). Where the brief's own language has seeded a phrase used by multiple perspectives, the synthesis calls this out rather than treating lexical echo as independent convergence.

**Brief-priming self-check.** The brief used phrases "domain-generality" (quoted from PROMPT.md, §2), "load-bearing," "drift-to-ritual" (quoted from OI-009), "overdue," "ritual-tracking" (implicit — brief uses "ritual," perspectives produced "ritual-tracking"), "ceremony-accumulation" (brief quoted from Session 006's close), and "heavy-handed" (quoted from Session 006). All four perspectives adopted "load-bearing" pervasively — this is lexical echo carried from the brief. All four adopted "domain-generality" — also lexical echo, but substantively accurate; the frame is what the methodology actually claims. "Ritual-tracking" appeared as a coinage in the Generalist's Q6 and was adopted by the Steward — the Generalist's framing propagated to Steward but not to Skeptic or Outsider. This is single-perspective-to-synthesis lexical propagation flagged. Substantive convergence on Position A is genuine across all four (each gave a different primary reason); the frame ("domain-generality is untested") is brief-derived but accurate. This continues the brief-priming finding pattern from Sessions 005 and 006 and is flagged explicitly for OI-009 audit purposes.

---

## Q1: Overdueness versus readiness — four-way convergence on Position A, with four distinct rationales

**Convergence on direction, divergence on basis.** All four perspectives identify Position A as more load-bearing. The reasons diverge:

- **Generalist** — confirmation-bias framing: "These two hypotheses are indistinguishable from inside the self-frame. Only an external application, where vocabulary is *not* native, can break the tie" [`01a-perspective-generalist.md`, Q1]. Position B's "load-bearing in situ" is not the relevant predicate; the relevant predicate is "prerequisite for first external" [`01a`, Q1].
- **Outsider** — highest-value-uncertainty framing: "A methodology that claims domain-generality but keeps improving its own internal governance before first use starts to look optimized for discussing application rather than doing it" [`01d-perspective-outsider.md`, Q1]. B "confuses past validity with present priority."
- **Skeptic** — rejects the framing. "Position A and Position B both accept a premise I reject: that 'self-work vs. external application' is the axis along which OI-009 drift is meaningfully measured" [`01c-perspective-skeptic.md`, Q1]. *If forced to pick*, Position A "slightly more load-bearing, but for a different reason" — the accumulating validation-against-one-domain is a "methodological conflict of interest that compounds with each session" [`01c`, Q1].
- **Steward** — process-gap framing: "Position A is correct that domain-generality is the asserted-but-untested central claim... Position A's weakness is that it can be weaponised into reactive pivoting" [`01b-perspective-steward.md`, Q1]. Session 006's deferral was a *process* objection, not a *readiness* objection, and Session 007 can resolve the process gap without executing external application.

`[synth]` The four-way Position A convergence is genuine at the direction level. The frames do not reduce to one another: confirmation-bias (Generalist), highest-uncertainty (Outsider), accumulating-validation-conflict (Skeptic), and process-gap-not-readiness-gap (Steward) are four independent rationales. The synthesizer finds no single dominant framing; the decision record must preserve all four.

**Skeptic's audit of the OI-009 redefinition.** The Skeptic uniquely flags that Session 006's close "redefined OI-009 without deliberation" — specifically, that OI-009's *originating content criterion* ("multi-agent applied to typos, renames, reordering, or decisions with no genuinely articulable alternative positions") is distinct from the *count-based criterion* ("three consecutive self-sessions") that Session 006's close introduced [`01c`, Q1]. `[synth]` This audit finding is load-bearing for Q6 and for OI-009's future handling; no other perspective raised it. It stands as a coverage-only finding that must be preserved in the decision record.

**Evidence that would change the Position A finding** (quoted):

- *Generalist*: "a specific, articulable blocker — something that, if missing, would make the first external application unsafe, incomplete, or uninterpretable" [`01a`, Q1].
- *Outsider*: "a demonstrated execution blocker... an accessibility blocker... contrary user direction" [`01d`, Q1].
- *Skeptic*: "a specific, named weakness in the current specifications that (i) would make first external application produce misleading validation results, and (ii) can be fixed only through self-work" [`01c`, Q1].
- *Steward*: "a specific concrete spec weakness surfaces during this deliberation that demonstrably blocks external application... If the user explicitly directs a target domain during or before Session 007... If Q3 analysis reveals that no domain is accessible to the orchestrating agent's tools/permissions" [`01b`, Q1].

`[synth]` The four evidence-criteria converge on: a concrete, named, articulable blocker. No perspective surfaced one in this deliberation. The convergence on "no blocker named" is four-way.

**`[synth]` Resolution direction on Q1.** Position A carries. The basis is plural — confirmation-bias, highest-uncertainty, accumulating-validation-conflict, process-gap-is-resolvable — and the decision record preserves all four rationales. The Skeptic's audit of the Session-006 OI-009 redefinition is preserved as coverage-finding.

---

## Q2: Selection mechanism — three-of-four convergence on criteria-first plus user-direction/ratification; Skeptic dissents

**Three-of-four alignment on combination.** Generalist, Outsider, and Steward independently propose variants of: **criteria-first (in Session 007) + user-direction or user-ratification + multi-agent validation of selected target (in Session 008).**

- *Generalist*: "user-direction solicited in parallel with criteria-first production this session, with multi-agent validation of the eventual target when one is named" [`01a`, Q2]. Fallback: if user silent past a stated window, orchestrating agent picks from shortlist with retroactive ratification.
- *Outsider*: "criteria-first in Session 007, then user-direction or user-ratification before the first full external session proceeds... define criteria now, obtain user nomination or ratification next, and only then launch the first external session" [`01d`, Q2].
- *Steward*: "Criteria-first + user-direction, with multi-agent validation of the chosen target... The orchestrating agent never selects alone without a record of the user's assent" [`01b`, Q2].

**Skeptic dissent.** The Skeptic rejects all five brief candidates on specific failure-mode grounds: user-direction alone fails under user-pressure-to-produce; multi-agent selection is still self-application; unilateral-for-ratification is what Session 006 already rejected; criteria-first is circular (criteria validated against prior self-work); combinations inherit constituent failure modes. The Skeptic's position: **"ask the user, with the explicit framing that the purpose is to stress-test the methodology, and with an explicit offer of 'none of the above' as a user response"** [`01c`, Q2]. The Skeptic further argues: "the objection was to *unilateral selection*, not to *asking*. Asking is not heavy-handed. The honest move is to acknowledge that Session 006's rationale has been in place for two sessions without the orchestrating agent actually asking. That is the real drift: using 'heavy-handed' as a shield against asking" [`01c`, Q2].

`[synth]` The Skeptic's "just ask, with explicit none-of-the-above" is operationally consistent with the three-of-four convergence's user-direction step. The disagreement is over **whether criteria come first or simultaneously with the ask**. Generalist/Outsider/Steward: criteria plus ask. Skeptic: ask first, cleanly. The practical difference is small but the framing difference is real: if criteria are produced first, they may constrain what the user proposes; if the ask is cleanly first, the user's domain choice is unconstrained.

**Skeptic's additional structural concern.** "Session 007's close should be written by a different perspective than the assessment. If the orchestrating agent writes both the assessment (which argued for external application) and the close (which defers again), the same voice is on both sides of the deliberation. This is a structural weakness the brief does not name" [`01c`, Q6, applied here for relevance]. `[synth]` This is a procedural point about the session's own honesty that applies regardless of Q2's resolution; preserved.

**Accountability convergence (four-way).** All four perspectives specify that ownership is split and recorded: user owns the domain choice (or its delegation); orchestrating agent owns the scoping and any proposal; deliberation owns the criteria. The three-of-four convergence makes this an explicit protocol; the Skeptic's "just ask" achieves the same through simpler means.

**`[synth]` Resolution direction on Q2.** Adopt the three-of-four convergence: criteria-first in Session 007, user-direction or user-ratification solicited in this session's close, Session 008 opens under the user's response (or documented absence thereof). Skeptic's "criteria are circular, just ask" dissent is preserved in the decision record. The Skeptic's additional concern — that the same voice is on both sides of the deliberation — is addressed by making the Session 007 close explicit about the Skeptic's audit of OI-009's redefinition and by the four-perspective synthesis itself being the counter-weight to any single-voice framing.

---

## Q3: Criteria for a good first target — four-way convergence on shape; divergence on software-adjacency

**Convergence on properties (four-way):**

- **Bounded scope.** Generalist: "2–4 sessions of external work" [`01a`, Q3]. Outsider: "one-session-executable in the sense that Session 008 can produce a real design increment, not necessarily finish the whole problem" [`01d`, Q3]. Skeptic: "multi-session is more honest... first external should not be open-ended" [`01c`, Q3]. Steward: "Multi-session, with the *first session of external work* scoped to one session's executable increment" [`01b`, Q3]. `[synth]` Minor phrasing divergence; substantive agreement on bounded, not-open-ended.
- **Low stakes / reversibility.** Four-way: first external is a sandbox design exercise, advisory artifact, or low-stakes real target; not commit-now irreversible action.
- **Validation accessibility.** Four-way: the target must admit a non-trivial Validate activity analogue within the methodology's terms. All four perspectives name this as the sharpest filter. Absence of a translatable Validate disqualifies.
- **Mid vocabulary distance.** Four-way: target's vocabulary should differ from the methodology's but overlap enough to translate. Divergence in degree (see below).

**Divergence on software-adjacency.** A notable cross-axis split:

- *Outsider*: "the best first candidates are software design, small research-plan design, curriculum design, or internal process design" [`01d`, Q3]. Explicitly includes software.
- *Steward*: "software, research programs, curricula, policy" are listed as domains with written artifacts that "translate more naturally to a provenance-centric methodology" [`01b`, Q3]. Accepts software.
- *Generalist*: Rules out software-adjacent as first target: "designing another CLI-tool validator, designing another deliberation format... fail the generality test by confirmation bias" [`01a`, Q3]. Rules in "curriculum design, a short research programme, a small policy intervention, an organisational process design, a non-software engineering specification."
- *Skeptic*: Rejects software-adjacent strongly: "The methodology was *built in a software-shaped workspace using software-shaped tooling* (git, shell scripts, Markdown specs). Any first target that sits in that dialect is a rigged game" [`01c`, Q3].

`[synth]` **This is a two-two split that cuts non-obviously across the model-family axis.** The non-Claude Outsider and one Claude perspective (Steward) accept software-adjacent as first-target-candidate; two Claude perspectives (Generalist and Skeptic) reject software-adjacent as "rigged" or confirmation-biased. The model-family axis does not predict the argumentative alignment — inverting what a naive cross-model hypothesis would suggest.

**Skeptic-unique concerns:**

- *Rejects "accessibility" as a filter.* "If the orchestrating agent and workspace already have the tools and context, the domain is probably too close. Accessibility should be a *problem to solve*, not a *criterion to satisfy*" [`01c`, Q3].
- *"Not pre-shaped by the orchestrating agent"* added as a criterion. "If the agent picks the target... it will — consciously or not — pick a target where it expects to succeed. This is the most insidious failure mode" [`01c`, Q3].
- *"Externally legible"* added as a criterion. "Someone outside this workspace should be able to read the output and judge whether the methodology did useful work" [`01c`, Q3].

`[synth]` The Skeptic's three additions are coverage — no other perspective named them. All three are load-bearing and survive into the decision record.

**`[synth]` Resolution direction on Q3.** Adopt the four-way convergence on shape (bounded scope, low stakes, Validate analogue, mid-distance). Preserve the software-adjacency split as a named choice in the decision record: the decision either includes software-adjacent as acceptable (Outsider + Steward position) or rules it out as too close (Generalist + Skeptic position). Adopt Skeptic's three additional criteria (not-pre-shaped; externally legible; accessibility-is-problem-not-filter).

---

## Q4: Specification and kernel changes before first use — two-two split, cross-model

**Two-of-four for minor pre-use changes.** Generalist and Steward propose minor, targeted changes:

- *Generalist*: Three concrete gaps to close: (1) kernel Read activity clarification for external domains; (2) workspace-structure addition of `applications/` top-level; (3) validation-approach self-reference audit [`01a`, Q4].
- *Steward*: Same three gaps; adds "possibly multi-agent brief construction" as a further check. Notes the workspace-structure addition "can be deferred to Session 008 if Session 007 runs out of scope" [`01b`, Q4].

**Two-of-four against pre-use changes.** Skeptic and Outsider converge (cross-model!) on no-pre-use-changes:

- *Outsider*: "I do not think first external application requires a specification or kernel change before first use. In fact, pre-emptive changes would be a warning sign... Let the first external application identify where wording actually breaks" [`01d`, Q4]. Explicitly rejects `applications/` directory as speculative.
- *Skeptic*: "I argue against making changes in advance... Pain is the signal. Removing the pain removes the learning" [`01c`, Q4]. Allows one narrow concession — the `applications/`-vs-mixed-tree question is a genuine spec gap — but leans toward "we will see how this unfolds and add structure reactively" [`01c`, Q4].

`[synth]` **This is a genuine cross-model convergence against pre-use changes.** The non-Claude Outsider and the adversarial Claude Skeptic independently arrive at the same position: pre-emptive changes contaminate the test; the first external application's role is to surface where the existing specs break; protecting the specs from contact defeats the test. The two Claude perspectives that argued for minor changes (Generalist and Steward) did so with different emphasis — Generalist named three gaps as "minor, targeted," Steward named the same three with deferability notes. Neither argued for substantial pre-use revision.

**Narrow convergence: watchpoints without revision.** All four perspectives, read carefully, support **recording stress-test watchpoints** (which activities are expected to require clarification on first external use) without pre-committing specification revisions. Outsider: "an explicit stress-test stance recorded in Session 007 or Session 008: the first external application is expected to probe whether Read and Validate need clarification outside self-work. That is an execution note, not a prerequisite specification revision" [`01d`, Q4]. Skeptic: "Stress test that would surface hidden assumptions: pick a target in a genuinely non-software domain and attempt each of the nine activities literally. Where the activity produces a shrug or a category error, that is a finding" [`01c`, Q4]. Generalist: "an explicit commitment to record (as provenance) every point at which a spec's phrasing required on-the-fly reinterpretation" [`01a`, Q4]. Steward: "read the four active specifications end-to-end with the substitution 'an external domain' for every implicit self-reference and note every phrase that no longer makes sense" [`01b`, Q4]. `[synth]` Four-way convergence on the watchpoint-record approach — *a finding-preservation mechanism, not a specification-revision mechanism*.

**`[synth]` Resolution direction on Q4.** Adopt the Skeptic+Outsider cross-model convergence: **no pre-use specification or kernel changes.** Record stress-test watchpoints in the decision record and in Session 008's assessment. Preserve the Generalist+Steward position that three specific gaps (Read clarification, `applications/` top-level, validation self-reference) may bite on first use; document these as the stress-test watchpoint list that Session 008 is expected to probe, not as pre-commitments to revision.

---

## Q5: Self-increment content — four-way convergence; framing divergence

**Substantive content convergence (four-way).** All four perspectives independently propose the same Session 007 work-product shape: **selection criteria + selection mechanism + a pre-commitment binding Session 008 to first external application.**

- *Generalist*: "the only defensible self-increment is producing the selection criteria from Q3 and the spec/kernel changes from Q4 as a durable package, explicitly framed as preparing for Session 008's external pivot with a named non-negotiable criterion for that pivot" [`01a`, Q5].
- *Outsider*: "a narrowly scoped first-application launch protocol... first-target criteria, the user-ratification mechanism, the minimum external brief shape, and the expected interpretation of Read and Validate for a first external session" [`01d`, Q5].
- *Skeptic*: "do the external-application re-examination itself as the session's content — as in, spend the session producing the criteria, mechanism, and pre-commitment for Session 008's external application, without actually doing the external application yet" [`01c`, Q5].
- *Steward*: "the selection-criteria spec plus a self-reference audit of the existing four active specifications... the selection mechanism from Q2 recorded as a decision" [`01b`, Q5].

`[synth]` **Four-way convergence on content. Framing divergence on label.** Generalist: "last self-increment before external." Steward: "preparatory self-work for Session 008 external." Skeptic: "external-application re-examination, not self-work." Outsider: "narrowly scoped first-application launch protocol." The same work is being named; only its classification ("self" vs "external-preparation") varies. `[synth]` The synthesizer's judgment: **the honest label is "external-application preparation," not "self-infrastructure work."** This honors the Skeptic+Outsider framing and is operationally consistent with Generalist+Steward's content.

**Four-way convergence on rejected candidates.** All four explicitly reject each of OI-001, OI-007, OI-011, OI-005, and OI-004 criterion 4 as the primary Session 007 increment.

- *OI-001 (naming).* Generalist: "risks being the comfortable choice." Outsider: "may matter eventually" but not now. Skeptic: "most ritual-adjacent option... cosmetic." Steward: "defensible but not load-bearing *now*." Four-way reject.
- *OI-004 criterion 4.* Generalist: "inward-pointing; refines the participation mechanism, which is self-infrastructure." Outsider: "orthogonal to external application." Skeptic: "weak accept" in the abstract but not as Session 007's primary work. Steward: "orthogonal to external application. Valid work but doesn't unblock anything." Four-way reject-as-primary.
- *OI-007 (open-issues scaling).* Four-way: not pressing at 9 issues.
- *OI-011 (intra-family mixing).* Four-way reject-as-primary.
- *OI-005 (sub-activities).* Four-way: explicitly blocked on external application; picking it as Session 007 work would be logically incoherent (Skeptic: "direct evidence of ritualized self-reference").

**Distinction from Session 006's deferral rationale (four-way convergence).** All four perspectives articulate the distinction: Session 006 deferred because the *selection mechanism was under-specified*; Session 007's increment *fills that under-specification*. The work is not "more time"; it is "the specific preparation that dissolves the reason for prior deferral." Generalist: "After Session 007, a Session 008 deferral cannot reuse Session 006's rationale — the mechanism will exist." Outsider: "we need one missing piece of interface definition so that the next session can no longer evade launch." Skeptic (framing it adversarially): "A deferral with an exit criterion is work. A deferral without one is drift."

**`[synth]` Resolution direction on Q5.** Session 007's work-product is: (a) selection criteria (the Q3 convergence); (b) selection mechanism (the Q2 convergence plus the explicit user-ask in the close); (c) a stress-test watchpoint list (the Q4 convergence on watchpoints-not-revisions); (d) a pre-commitment binding Session 008 to first external application with specific failure conditions. All four perspectives converge on this content; the label is "external-application preparation" per the synthesizer's judgment.

---

## Q6: OI-009 activation — three-of-four that activation is avoidable; Skeptic says activated regardless; four-way on criterion shape

**Three-of-four on avoidability.** Generalist, Outsider, Steward each propose a criterion under which Session 007's preferred outcome avoids OI-009 activation:

- *Generalist*: "activates if, and only if, it concludes with a self-increment whose justification does not terminate in a named, non-deferrable external-application commitment for Session 008" [`01a`, Q6].
- *Outsider*: "at the threshold but not yet activated. Session 007 can avoid activation only if it explicitly turns the methodology toward first external application" [`01d`, Q6].
- *Steward*: "does not activate the drift signal, conditional on the following distinguishing criterion... A self-session is load-bearing if it either (a) resolves a specific articulable obstacle that blocks a named next step... or (b) closes an open issue whose closure changes what later sessions can do" [`01b`, Q6].

**Skeptic dissent.** "The drift signal is activated, and I think activation is correct regardless of which outcome Session 007 chooses. The brief's framing — that 'load-bearing self-work' and 'ritual-tracking self-work' are distinguishable at session granularity — is wrong. OI-009 as currently formulated cannot distinguish between them without ground truth, which is precisely what external application would provide" [`01c`, Q6]. `[synth]` The Skeptic's position: record OI-009 as activated; the question is not whether Session 007 qualifies but whether the methodology treats activation seriously. "An open issue that never changes behavior is itself part of the ritual it was opened to detect."

**Four-way convergence on criterion shape.** Each perspective proposes a distinguishing criterion for load-bearing-vs-ritual:

- *Generalist* (criterion-proposal): "Self-work is load-bearing when its justification survives the following test: *can the need for this increment be stated in terms that refer to the methodology's asserted external use, or only in terms that refer to the methodology's self-description?*" [`01a`, Q6].
- *Outsider*: "Load-bearing self-work removes a concrete blocker to a named next external action and narrows the remaining decision space. Ritual-tracking self-work may still be intelligent and non-trivial, but it leaves the next external action no closer than before" [`01d`, Q6].
- *Skeptic*: "Self-work is load-bearing if the weakness it addresses would be visible to a reader outside the workspace reading the specs for the first time. Self-work is ritual if the weakness is only visible to readers who have already internalised the prior provenance" [`01c`, Q6].
- *Steward*: "A self-session is load-bearing if it either (a) resolves a specific articulable obstacle that blocks a named next step, where the obstacle was identified in provenance and the next step is concrete; or (b) closes an open issue whose closure changes what later sessions can do" [`01b`, Q6].

`[synth]` Four independent criterion-proposals. They substantively overlap: each asks some version of "does this increment unblock a named next step?" The Skeptic's criterion (external-reader visibility) is the most stringent; the Steward's (named next step) is the most operational; the Generalist's (translation-to-external-frame) is the most frame-sensitive; the Outsider's (narrows remaining external-action decision space) is the most action-centric. **These four criteria can be adopted as a package: an increment is load-bearing iff it satisfies at least one of the four forms.** No single criterion subsumes the others; their disjunction is more robust than any one.

**Session 008 constraint (three-of-four).** Outsider: "Session 008 should be limited to target ratification and first application. If even that does not happen, the methodology should downgrade its own claim from 'domain-general methodology' to 'promising but unvalidated self-hosting methodology'" [`01d`, Q6]. Generalist: "if Session 008's assessment would defer again, the deferral requires invoking a newly-surfaced, specifically-named blocker, recorded as a decision with its load-bearing claim defended, not asserted" [`01a`, Q6]. Steward: "if Session 008 does not produce first external application *or* it deliberates on another self-topic *or* it defers external application again, the drift signal activates regardless of per-session justification quality" [`01b`, Q6]. Skeptic (adversarial-form): Session 008 constraint is part of why OI-009 must be recorded as activated-with-consequence.

**The Outsider's downgrade-of-claim proposal.** Unique to the Outsider: if Session 008 fails to execute first external application, the methodology "should downgrade its own claim from 'domain-general methodology' to 'promising but unvalidated self-hosting methodology'" [`01d`, Q6]. `[synth]` This is a coverage-finding. No Claude perspective surfaced the downgrade mechanism. It is distinctive and load-bearing: it provides a hard consequence for continued deferral that would be visible in PROMPT.md or a top-level README.

**`[synth]` Resolution direction on Q6.** Adopt the three-of-four position: Session 007's outcome (external-application preparation + binding Session 008 commitment) does not activate OI-009 **on the proposed package criterion**, conditional on Session 008 actually executing. Preserve the Skeptic's "activated regardless" dissent. Record the four criterion-proposals as a disjunctive package for OI-009 assessment going forward. Adopt the Outsider's downgrade-of-claim proposal as a conditional consequence if Session 008 fails to execute.

---

## Points of Disagreement (preserved)

These are the positions not absorbed into consensus. Each is load-bearing and must survive into the decision record:

1. **Framing of Q1 itself (Skeptic-unique).** The Skeptic rejects Q1's A/B framing as incomplete and audits Session 006's close for redefining OI-009 without deliberation. This audit finding must be recorded; no other perspective flagged it. `[synth]` Adopted as an OI-009-related finding; the decisions preserve the Skeptic's substantive concern (the deferral-history-count criterion was added without deliberation) even as the session proceeds on Position A grounds.

2. **Selection mechanism — criteria-first vs. just-ask (Skeptic dissent).** Generalist/Outsider/Steward: criteria in Session 007, user-ask between sessions. Skeptic: just ask the user, criteria are circular. Adopted: the three-of-four approach. Skeptic's "criteria are circular" dissent preserved as lead rejected alternative. Skeptic's "just ask with none-of-the-above option" is operationally encoded in the user-ask itself.

3. **Software-adjacency as first-target candidate (2-2 split, cross-model).** Outsider+Steward: software-adjacent domains (software design, research-plan, curriculum) are acceptable first targets. Generalist+Skeptic: software-adjacent is "rigged game" or confirmation-biased. Adopted: Generalist+Skeptic's stricter stance as criterion, because first external's purpose is stress-testing domain-generality, and the stricter stance better serves that purpose. Outsider+Steward's permissive stance preserved as minority — specifically noting that if the user directs a software-adjacent target, the target is not disqualified by this criterion (user-direction overrides); the criterion binds the agent-selection default.

4. **Pre-use specification changes (2-2 split, cross-model).** Generalist+Steward: three minor pre-use changes. Skeptic+Outsider: no pre-use changes; pain is the signal. Adopted: Skeptic+Outsider's no-pre-use-changes position. The three Generalist/Steward-named gaps (Read clarification; `applications/` top-level; validation self-reference audit) are recorded as **stress-test watchpoints** — expected failure points that Session 008's first external application is specifically instructed to probe and record.

5. **OI-009 activation (3-1, Skeptic dissents).** Adopted: three-of-four that Session 007's outcome avoids activation conditional on the criterion-package and Session 008 execution. Skeptic's "activated regardless" preserved as lead rejected alternative.

6. **Same-voice-on-both-sides concern (Skeptic coverage-only).** The orchestrating agent who wrote the assessment (arguing external pivot) also writes the close and the decisions. The synthesis framework itself is the intended counter-weight, but the Skeptic's concern is structurally valid and is preserved as a meta-note that future sessions should be alert to.

7. **`participants_family` honest labelling.** All four perspectives treated the Outsider as a genuine non-Claude participant (no one questioned the participant's authenticity). This is not a dissent point; it is recorded here because the Skeptic specifically noted the orchestrating-agent-pre-decided-the-outcome risk, and the four-way convergence on Q5's content counts against that concern in this session's evidence.

---

## Cross-Model Observations

This was the methodology's third heterogeneous-participant deliberation. Two distinct cross-model patterns surfaced:

**Pattern 1: Skeptic+Outsider convergence against pre-use spec changes (Q4).** The adversarial Claude perspective and the non-Claude perspective independently converged on "no pre-use changes; pain is the signal; pre-emptive changes contaminate the test." The two Claude non-adversarial perspectives (Generalist, Steward) both argued for minor pre-use changes. This is the opposite of a "Claude converges, Outsider diverges" pattern — the Outsider aligns with the most sceptical Claude perspective, against the two more constructive Claude perspectives. The convergence argument has two independent sources: Skeptic's methodological-contamination concern and Outsider's pre-emptive-optimization-warning-sign concern. `[synth]` The convergence is substantive, not merely lexical.

**Pattern 2: two-two split on software-adjacency that crosses the model axis (Q3).** Outsider+Steward accept software-adjacent as candidate first-target; Generalist+Skeptic reject it. Model family does not predict the argument: non-Claude + one Claude accepted vs. two Claude rejected. This is notable because a simpler cross-model-testing hypothesis would expect the Outsider to align differently from all three Claude perspectives. The Outsider aligning *with* a Claude perspective (Steward) against two other Claude perspectives (Generalist, Skeptic) is evidence that the methodology-family axis is not the dominant axis in this question; the argumentative axis dominates.

**Outsider-unique contributions (not present in any Claude response):**

- **Downgrade-of-claim consequence** [`01d`, Q6]: if Session 008 fails to execute first external application, downgrade the methodology's claim from "domain-general" to "promising but unvalidated self-hosting." No Claude perspective surfaced this.
- **Ratification-as-third-path framing** [`01d`, Q2 and Meta-note]: explicit articulation that "user ratification" is distinct from both "user-direction" and "unilateral selection," and is the load-bearing third path the brief did not name. The Claude perspectives described variants of this but did not label it as a framing innovation.
- **Scoping warning against "deciding how to decide"** [`01d`, Meta-note]: "Session 007 could spend itself deciding how to decide, then call that prudence. At this stage, any internal work not tightly coupled to launching Session 008 risks proving OI-009 correct." The Skeptic raised a related concern (criteria-first is circular), but the Outsider's framing is distinct — it names the failure mode of *Session 007 itself* becoming meta-meta-work.

The Outsider's banner-recorded identity (OpenAI GPT-5 via Codex CLI v0.121.0, session id `019da2e3-d854-72c2-bd39-42545da77631`, `reasoning effort: xhigh`, 18,723 tokens used) is the transport-layer evidence of non-Claude participation per D-029's Q6 honest-evidence requirement.

---

## Limitations

Required content for multi-agent deliberation records (v3 spec's Limitations requirement):

- **Three of the four perspectives share the Claude Opus 4.7 model family.** The Outsider's distinct-lineage participation does not remove the Claude-majority. Convergence that includes the Outsider is stronger evidence than convergence that does not; this synthesis has flagged both categories where they apply.
- **The Outsider was invoked via a CLI wrapper (`codex exec`), not a direct API.** Transport fidelity depends on convener integrity. The raw output is committed verbatim including banner and prompt echo; no automated integrity check verifies this.
- **Brief-writing had no adversary.** The shared brief was written by the synthesizer-orchestrator (a Claude Opus 4.7 agent). The phrases "domain-generality," "load-bearing," "overdue," "drift-to-ritual," "heavy-handed" appear in the brief. Adoption of these phrases by multiple perspectives is partially lexical echo. Convergence on the *substantive framing* (Position A for external application) is genuine across four independent rationales, but the vocabulary in which the frame is expressed is brief-derived. The synthesis has tried to distinguish substantive from lexical convergence.
- **The synthesis step is a single-agent re-entry point** (Claude Opus 4.7, matching three of four deliberators' model family). The synthesizer has not played any perspective, per D-018. This limitation is preserved from v3 spec's Limitations section and applies here identically. The Skeptic's concern about "same voice on both sides" applies specifically to this session: the orchestrating agent wrote the assessment arguing external-pivot, convened the deliberation, and now synthesises the deliberation that produced external-preparation — the four-perspective structure is the methodology's only mechanism against single-agent framing capture in this session.
- **Whether the sustained-practice tally advances is indeterminate at synthesis time.** D-023's triggers are file-specific. Whether any Session 007 decision triggers D-023 depends on the decisions' content (kernel changes? spec creations? OI-004 state changes?). The synthesizer's reading is that none of the Session 007 decisions as sketched in this synthesis in fact triggers D-023.1–4 — there are no kernel modifications, no revisions to `multi-agent-deliberation.md`, no revisions to `validation-approach.md` in Tier-2-touching ways, and no OI-004 state change. If that reading holds through the Decide activity, the deliberation was non-Claude-conservative-inclusion but not D-023-required; the sustained-practice tally does not advance. This is recorded honestly as an indeterminate-at-synthesis-time outcome whose resolution is a decision-level matter.
- **The Outsider was selected by the session operator** (Claude Code orchestrating agent), not independently. `participant_selection_method: self` is the most honest classification. Same caveat as Sessions 005 and 006.
- **The deliberation's scope may itself be a drift signal.** The Outsider's Meta-note and the Skeptic's adversarial position both flag this concern: spending a multi-agent deliberation on "should we do the thing" is, under some framings, the very ritual-tracking OI-009 monitors for. The synthesis's counter: the deliberation produced genuine four-way substantive convergence on content (Q5) and genuine cross-model disagreement on two axes (Q3, Q4), neither of which is consistent with rubber-stamp drift. But the concern stands and is explicitly preserved.

## Structural honesty notes

- Every claim attributing a position to a perspective in this synthesis cites the source file and question section.
- `[synth]` marks synthesizer-original claims (direction-setting moves, convergence identifications, resolution proposals not found verbatim in any raw output).
- Dissent is preserved in the "Points of Disagreement" section at its strongest form. The Skeptic's six-point dissent is the session's largest preserved-minority set.
- Majority/minority structure is reported explicitly where the four perspectives diverged.
- Quote over paraphrase was applied for all load-bearing attributions.
- The brief-priming check on "load-bearing," "domain-generality," "overdue," and "drift-to-ritual" is documented in the Synthesis Conventions section above; the convergence claims have been adjusted to distinguish lexical echo from substantive agreement.
- The synthesizer's single-agent re-entry risk is explicit in Limitations. The Skeptic's "same voice on both sides" concern is specifically preserved as a structural finding that future sessions should track.
