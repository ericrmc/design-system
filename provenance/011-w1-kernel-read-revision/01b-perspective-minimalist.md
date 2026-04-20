---
session: 011
title: Perspective — Minimalist
date: 2026-04-20
status: committed-verbatim
perspective: minimalist
committed_at: 2026-04-20
---

## Q1

**Proposed revision to kernel §1 Read:**

> #### 1. Read
>
> Absorb the full current state of the workspace. Every file, every specification, every provenance record. If the workspace is under version control, understand the recent history. Build a complete picture before changing anything. When a session's work concerns a domain outside this workspace's self-hosting scope, Read additionally includes absorbing the domain constraints the session operates under and the domain knowledge available to the orchestrating agent and perspectives; such domain inputs must be surfaced in the session record, not silently applied.
>
> This is a receptive activity. Its output is understanding, not artifacts.

This is the Session 008 candidate text (34 words), tightened and extended by one clause ("such domain inputs must be surfaced...") that hooks the PROMPT.md anti-silent-import rule directly into §1. Total addition: ~58 words. §1 grows from ~40 to ~98 words, becoming mid-length rather than shortest. Existing sentences are not reordered. No sub-headings.

**The senses are named only implicitly** — the text distinguishes the self-hosting default from the external extension by "additionally includes" rather than by giving each a named sub-section. I considered and reject two alternatives:

**Rejected: parallel sub-sections "Workspace reading" and "Domain reading"** (mirroring §7). This would roughly double §1's length and, more importantly, misreads the §7 precedent. §7 was forced to split because Workspace validation and Domain validation are *genuinely incompatible* activities: one is internal-consistency checking against specs already in the workspace; the other is obtaining an external evidentiary receipt from a domain-actor. They happen at different times (workspace in-session; domain may complete out-of-session), produce different artefacts, and answer different questions. §1 Read does not have that forcing property. "Read the workspace" and "absorb domain knowledge" are the *same kind of activity* — both are receptive absorption of context before acting — just pointed at different sources. The sub-section structure would be ceremonial symmetry, not load-bearing distinction.

**Rejected: pointer to a separate external-application-guidance specification.** This is tempting and I address it more fully in Q2 and Q5. Short version: a pointer-plus-external-doc is the right long-term shape once external-application methodology accretes enough surface area to justify its own spec. Today it does not. Two external artefacts (Sessions 008, 010) is too thin an evidence base to carve out a new spec. A single sentence in the kernel acknowledges the gap and lets the external-application methodology accrete as a tracked open issue until there is enough of it to warrant extraction.

**On naming:** the proposed text avoids coining "domain reading" as a term-of-art. Introducing a named concept creates an obligation for future sessions to use the name consistently, and for external readers to learn it. "Domain reading" as a phrase does not pull weight that "absorbing... domain knowledge" doesn't already pull. If a later session finds it has to refer to this sense repeatedly, that session can extract a name then, with evidence that the name is needed. Coining now is premature.

## Q2

**Preferred: (a) in-paragraph elaboration.** One additional sentence inside the existing §1 paragraph, as drafted in Q1.

**The precedent-following case (for sub-sections, option b):** Session 009's §7 Validate revision established a pattern where external vs self-hosting concerns are exposed via parallel sub-sections with explicit sense-names. Following the same structure in §1 Read produces kernel-internal coherence: a reader encountering §1 and §7 sees the same shape for the same kind of distinction. Coherence of form aids comprehension; divergent shapes for parallel concerns are a small cognitive tax on every reader forever. The §7 precedent is adjacent and fresh (one session old); departing from it within two sessions of its establishment signals either that the precedent was wrong or that this case differs, and either signal wants an explicit defence.

**The precedent-departing case (which I endorse):** the §7 precedent was load-bearing because Workspace validation and Domain validation are genuinely distinct activities — different timing, different actors, different evidence, different outputs. The sub-section structure reflected a real bifurcation. §1 Read does not bifurcate that way. Reading the workspace and reading domain knowledge are the same receptive activity targeting different sources. Imposing sub-section structure on a non-bifurcation creates false parallelism and trains readers to expect that every §N has two senses. Several activities (§2 Assess, §3 Convene, §4 Deliberate, §5 Decide, §6 Produce, §8 Record, §9 Close) do not obviously bifurcate into workspace/domain senses, and the kernel would be worse if each acquired sub-sections to match §1 and §7. The cost of setting that precedent is larger than the cost of one asymmetry between §1 and §7.

**On §1's length:** §1 is currently ~40 words, the shortest activity. My proposal brings it to ~98 words, still within the range of the other activities (§2–§9 appear to run 60–250 words on my recollection of the kernel's shape). This is not a material length problem. Adding sub-sections would push §1 to ~180+ words and make it conspicuously long for what it does.

**On the external/self-hosting asymmetry:** the kernel should **acknowledge** the asymmetry but **not structure itself around** it. The methodology is self-hosting first; external-application capability is an extension. Structuring the kernel with parallel workspace/domain sub-sections at every activity would invert that priority, making external-application look co-equal to self-hosting within the kernel. It is not — yet. Two external artefacts is a trickle of evidence, not a mandate to re-architect.

**Rejected: (c) pointer to an elaboration specification.** Premature, per Q1. A pointer from §1 to a not-yet-written spec creates a broken-link situation. A pointer to a stub spec creates ceremonial overhead. Better: one sentence in §1 plus a tracked open issue for "external-application methodology specification" to be written when enough external artefacts accumulate to justify it (my rough threshold: four or five external artefacts across at least two domain types).

**Rejected: (d) footnote or appendix.** The kernel has no footnote convention. Introducing one for a single use is disproportionate.

## Q3

**Domain reading includes (a), (b), (c), (e). Excludes (d) as out-of-scope for the Read activity specifically.**

Concretely:

**(a) User-stated constraints passed in-session.** Includes. These are direct inputs from the domain-holder and arrive through the session's opening messages. Provenance: the session's opening messages are already captured in the session record (SESSION-LOG, provenance files). No new mechanism required; the constraint surfaces in the record by being quoted or paraphrased when it informs Assess/Deliberate/Decide.

**(b) Pretrained knowledge the orchestrating agent brings.** Includes. The orchestrating agent synthesises the brief and shapes Deliberate; what it brings from pretraining is already de facto in the process. Making this explicit as *domain reading* rather than leaving it implicit is an honesty gain. Provenance: the orchestrating agent should name, in the session record, which bodies of pretrained knowledge it drew on (e.g., "yoga/mobility conventions for Session 008; decision-theory conventions for Session 010"). A single sentence in Record suffices; no new artefact needed.

**(c) Pretrained knowledge the deliberation perspectives bring, delivered via the brief.** Includes, with a nuance. The brief itself is the channel — perspectives do not read during the independent phase. So "domain reading" as performed by perspectives is: the brief author curated domain knowledge into the brief, and perspectives absorb it as brief content. Reconciliation with `multi-agent-deliberation.md` v3's "perspectives reason from the brief" constraint: the constraint is preserved. Perspectives still only read the brief during independent phase; the brief is now acknowledged to legitimately contain curated domain content rather than being fiction-ed as purely workspace-derived. Provenance: briefs are committed verbatim (D-044 or similar), so curated domain content is already preserved in the session record.

**(d) Explicit research during the session (web searches, document lookup).** Exclude from domain reading as named in §1. Research is not receptive absorption — it is a *produced* survey, and it already belongs under a surveying/hypothesising step per PROMPT.md. Folding it into Read muddles the distinction between "what we came in knowing" and "what we went out and fetched." Keep research as an explicit mid-session activity with its own provenance.

**(e) External reference materials the user or operator cites.** Includes, treated like (a). If the user says "follow this style guide" or "here is a paper I want you to consider," the citation arrives in-session and is captured in the session record. Provenance: the citation and what was taken from it are recorded alongside the user-stated constraints.

**Boundary:** domain reading covers *inputs present at or before session open* — what the orchestrating agent, the user, and (via the brief) the perspectives bring into the session. Inputs fetched mid-session are not domain reading; they are research and belong to a surveying step. This boundary keeps §1 Read receptive-only (preserving its current character: "Its output is understanding, not artifacts") and prevents Read from becoming a catchall.

**Reconciliation with PROMPT.md:** domain reading inputs are legitimate, but they must be *surfaced* in the session record. The sentence I proposed in Q1 ("such domain inputs must be surfaced in the session record, not silently applied") makes this explicit inside §1. See Q4 for the detailed failure-mode analysis.

## Q4

The revision creates **manageable tension, not contradiction.** The reconciliation is already embedded in my Q1 proposal, but it deserves direct statement.

**PROMPT.md's rule:** outside ideas must enter via an explicit surveying/hypothesising step, not be silently committed. **Stance Briefs constraint:** perspectives reason from the brief during the independent phase. **W1 revision:** domain knowledge is legitimately absorbed in Read, which is step §1 — *before* any surveying step could occur.

The tension is real but structural, not logical. PROMPT.md's rule targets **silent commitment** — importing an idea into a workspace decision without flagging its provenance. It does not forbid outside knowledge from entering the process at all; that would be incoherent, because every session inherently draws on the orchestrating agent's and perspectives' pretraining. What the rule forbids is *unflagged* import. The W1 revision is consistent with PROMPT.md as long as domain reading is **surfaced** (recorded, made visible) rather than **silently applied**.

**Proposed reconciliation text (already in Q1's §1 revision):**

> "...such domain inputs must be surfaced in the session record, not silently applied."

This clause is the hook. It does not duplicate PROMPT.md's rule; it localises the rule's application to §1 Read's new scope. A reader of the kernel sees that domain reading is legitimate but accountable. A reader of PROMPT.md sees the general rule unchanged. No carve-out is needed — the revision is *consistent with* PROMPT.md, not *exempt from* it.

**Concrete failure mode #1 — the laundering case.** A future session confronts an external domain question. The orchestrating agent has, from pretraining, a strong intuition about the answer. Rather than running an explicit surveying step that would force the intuition to compete with alternatives, the agent labels the intuition "domain reading" and absorbs it as Read-activity context. By §5 Decide, the intuition has been treated as *given context* rather than *proposed option*, and it shapes the decision without ever being subject to the brief-deliberation-decide discipline. The provenance record says "domain reading included X," but X was never surveyed. PROMPT.md's substantive protection — that outside ideas compete — has been bypassed while the surface rule (surfacing) has been honoured.

**Mitigation, which I recommend as a companion open issue, not as a §1 revision:** require that domain reading inputs which bear on a contested or novel decision be named in Assess (§2) as candidates for surveying, not just listed in Read. This keeps the §1 revision minimal while closing the laundering path. I do not propose to write this into §1 itself because it belongs to §2's or §5's semantics, not §1's.

**Concrete failure mode #2 — the scope creep case.** "Domain knowledge available to perspectives" is broad. A session could argue that an entire body of pretrained knowledge (e.g., "decision theory") counts as domain reading and therefore does not require surveying. The cure is the same as #1: domain reading inputs that are load-bearing for a decision must be named specifically, not gestured at generically.

**I do not propose to address either failure mode inside §1.** §1's job is to name the receptive activity. The disciplines that prevent abuse belong elsewhere (§2, §5, or a companion spec). Adding them to §1 would bloat it and mis-place the discipline.

## Q5

**G/O/K/S application to the Session 011 revision as I propose it:**

- **(G) Translation-to-external-frame.** Satisfied. The need for the revision is straightforwardly statable in external-use terms: "when the methodology produces an artefact for a domain outside itself, the orchestrating agent and perspectives are drawing on knowledge not in the workspace; the kernel should acknowledge this." Sessions 008 and 010 both surfaced this gap.
- **(O) Narrows-external-action-decision-space.** Weakly satisfied. It is not clear that any *specific* next external action is currently blocked by §1's current wording. Sessions 008 and 010 proceeded without the revision by reinterpreting §1. The revision removes a latent interpretive burden on future external-artefact sessions but does not unblock a named next action.
- **(K) External-reader visibility.** Satisfied. An external reader encountering the kernel today would see §1 Read describing absorption of *workspace* state and would reasonably ask "what about the domain?" when learning that the methodology has produced external artefacts. The gap is visible to first-read.
- **(S) Specific-obstacle resolution.** Satisfied. W1 is an open watchpoint from Session 008. Closing it has concrete effect: the watchpoint list shrinks by one; the kernel documents its own extension path; the precedent for how external-application concerns enter the kernel is established with minimal surface area.

**Honest reading: the revision satisfies G, K, and S cleanly and O weakly.** Three of four is comfortably load-bearing. My minimal proposal is justified by the criterion-package.

**The refuse-the-revision case (which I take seriously and partially endorse):**

> *The kernel should remain minimal. Two external artefacts is a trickle of evidence. The right move is to open an issue — "external-application methodology is underspecified" — and let it accrete evidence through more external artefacts before committing the kernel to any extension. Premature specification calcifies patterns before they are validated.*

This is a strong argument. The methodology has committed itself to external use via two artefacts but has not built enough external-application experience to know what the kernel should say about external domains. Every kernel word is a tax, and taxing the kernel with text that may turn out to be wrong-shaped after five more external artefacts is a real cost. The Reviser's instinct to draft cleanly can lead to premature crystallisation.

**Why I reject the refuse-case — but narrowly.** The refuse-case is right in principle about premature crystallisation, but wrong in the specific here for three reasons. First, W1 is an *already-open* watchpoint from Session 008, deferred once, deferred again by Session 010's scope. Carrying an open issue across sessions without resolution is itself a cost; methodologies that never close their open questions rot. Second, my proposed revision is 58 words, not a re-architecture; if it turns out wrong-shaped after further external artefacts, revising 58 words is cheap. The calcification risk scales with revision mass, and my revision is small enough that the risk is low. Third, the G/O/K/S check comes out three-of-four; a four-of-four refusal-to-revise argument would be stronger.

**Partial endorsement:** I do *not* endorse the fuller revision (sub-sections, new terminology, pointer to external-application spec) that other perspectives may advocate. Those proposals carry meaningfully higher calcification risk, and the refuse-case applies to them more forcefully than it applies to my minimal proposal. If synthesis gravitates toward the fuller revision, my position is: the refuse-case **wins against the fuller revision** even while it loses against the minimal one. "No revision, track W1 as a continuing open issue" is a better outcome than "sub-sections and new terminology."

## Meta-note

(a) **Positions I expect to differ from other perspectives.** I expect the Reviser or a structural-coherence-oriented perspective to propose parallel "Workspace reading" / "Domain reading" sub-sections mirroring §7 Validate. I reject this as ceremonial symmetry; the §7 precedent was forced by genuine activity-bifurcation that §1 lacks. I also expect some perspective to propose coining "domain reading" as a named term-of-art; I reject this as premature naming. On Q5 I will likely be the perspective most willing to say "consider no revision" as a real option.

(b) **Suspect assumption in the brief.** The brief treats W1 as ripe for closure because it was deferred once. Deferral is not ripeness. The genuine question is whether two external artefacts is enough evidence to specify external-application methodology; the brief does not ask this directly.

(c) **Framing concern.** Q1–Q4 assume the revision will happen and ask about shape. Q5 opens the refuse-case only at the end. The framing tilts toward revision.
