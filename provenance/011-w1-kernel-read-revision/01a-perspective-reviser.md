---
session: 011
title: Perspective — Reviser
date: 2026-04-20
status: committed-verbatim
perspective: reviser
committed_at: 2026-04-20
---

## Q1

I propose replacing kernel §1 Read in full with the following text. I follow the §7 Validate precedent (two named senses, parallel sub-sections) because the underlying asymmetry is the same — self-hosting versus external — and because parallel structure across §1 and §7 reduces reader load.

> #### 1. Read
>
> Absorb what the session will reason from. Two senses apply.
>
> **Workspace reading** applies to every session. Absorb the full current state of the workspace: every file, every specification, every provenance record. If the workspace is under version control, understand the recent history. Build a complete picture before changing anything.
>
> **Domain reading** applies when a session produces or revises an artefact intended for use outside the workspace. Absorb the domain constraints the session operates under and the domain knowledge available to the perspectives. Domain constraints are stated by the user or operator in-session — the problem being addressed, the conditions it must meet, the person it must serve. Domain knowledge is what the orchestrating agent and the perspectives bring from pretraining or cited reference to the problem the artefact addresses. Record what domain inputs were taken, from whom, and where they entered the session; outside inputs that change a workspace decision are surfaced through Convene and Deliberate, not committed silently (PROMPT.md).
>
> This is a receptive activity. Its output is understanding, not artefacts.

**On naming.** I use "Workspace reading" and "Domain reading" — parallel to §7's "Workspace validation" and "Domain validation." Rejected alternatives:

- *Inline prose without sub-headings.* This was how §1 looked before Session 009's §7 revision; it would leave §1 and §7 structurally asymmetric despite describing the same self/external split. A reader moving between §1 and §7 would have to re-derive the distinction in §1 from prose while reading it off the sub-heads in §7. The cost is low each time and high in aggregate.
- *A single unified sense with enlarged scope* (e.g., "Read whatever the session needs"). Rejected: the whole point of W1 is that the current wording names only workspace state, which left Sessions 008 and 010's Read step under-described. A unified sense re-hides the distinction W1 identified.
- *"Internal reading" / "External reading."* Rejected: "external reading" suggests reading external documents (books, web pages), which is a narrower subset of what Sessions 008 and 010 actually did. "Domain reading" more accurately covers user-stated constraints plus pretrained knowledge plus cited reference.

**On length.** The proposed text is roughly 175 words versus the current ~40. §1 becomes longer than most peer activities but shorter than §7 post-revision. This is acceptable because §1 and §7 are the two activities where the self/external asymmetry lives; the other activities (Convene, Deliberate, Decide, Produce, Record, Close) are symmetric across the asymmetry and can stay compact.

**Confidence.** High on the sub-section split and naming ("Workspace reading"/"Domain reading"). Medium on the exact wording of "Domain reading" — a competing drafter might reasonably cut the explicit PROMPT.md parenthetical and instead pointer to it from the §1 header, or might fold "domain constraints" and "domain knowledge" into a single sentence. Low-confidence phrase: "what the orchestrating agent and the perspectives bring from pretraining or cited reference" — this edges into mechanism-describing; a tighter drafter might write "knowledge the session's participants bring to the problem."

## Q2

I prefer option (b): two parallel sub-sections under §1, mirroring §7.

**Precedent-following case.** Session 009 established a structural pattern: when an activity has both a self-hosting and an external-artefact sense, name them as parallel sub-sections with **Bold** leading phrases. The W1 finding is the same asymmetry as the W4 finding — "this activity works differently for external artefacts than for workspace artefacts." Treating equivalent asymmetries with equivalent structure is how readers build reliable intuitions about the kernel. A reader who has learned "§7 has two senses because external validation is categorially different from workspace validation" will expect the same shape in §1. Delivering it reduces surprise and preserves parallelism across the spec. Further, the pattern scales: if a future session identifies an analogous asymmetry in, say, §6 Produce, the shape is already established.

**Precedent-departing case.** The strongest arguments to depart:

1. **§1 is short.** Currently ~40 words. Sub-sections for a 40-word activity are heavy; they impose structure overhead on content that barely needs it. Parallel sub-sections work in §7 partly because §7 post-revision is around 150 words — enough to benefit from internal signposting. For §1, inline prose could carry the distinction more lightly.
2. **Sub-sections in §1 set an implicit precedent for §2–§9 to gain sub-sections.** That risk is real; kernel bloat would degrade readability. Once §1 and §7 both have sub-sections, a future session might feel the pattern is the default and add sub-sections to activities whose content doesn't warrant them.
3. **Making the external/self-hosting asymmetry visible in two places (§1 and §7) might over-emphasise it.** The methodology is one methodology, not two; heavy visual division could wrongly suggest that external-artefact work is a parallel track rather than the same track with different inputs.

**My resolution.** I accept the precedent-departing case's observations but still prefer (b). Here is why:

- The §1 length objection dissolves once domain reading is actually described. A truthful "Domain reading" sub-section with enough content to be useful will carry the activity to ~150 words — comparable to §7. The comparison "§1 is short and sub-sections are heavy" is a comparison against the current §1, which Session 011 is revising precisely because it's incomplete.
- The bloat-precedent concern is addressable by explicit note in the session's provenance (D-record): "Sub-sections are used in §1 and §7 because both activities have a self/external asymmetry; this is not an invitation to sub-section other activities." Structural precedents are only as binding as the recording session makes them.
- On visibility: the asymmetry *is* real. Sessions 008 and 010 Read differently than sessions 001–007 did, and that difference is load-bearing. Hiding it in prose is a form of under-statement that would cost future readers more than the visible asymmetry costs.

Rejected: (a) in-paragraph elaboration — retains asymmetry between §1 and §7 shapes. Rejected: (c) pointer to elaboration spec — an external-application-guidance document that the kernel points to is a reasonable long-term structure, but it's a larger move than W1's scope allows; the current session should not invent a new spec when a local revision suffices.

## Q3

Domain reading is: **the domain constraints stated to the session by the user or operator, and the domain knowledge the orchestrating agent and the perspectives bring to the problem the artefact addresses.** That's the minimal definition matching what Sessions 008 and 010 actually did.

Mapping to the brief's (a)–(f):

- **(a) user-stated constraints in opening messages** — IN. This is the most traceable form of domain input. Provenance: the session's opening-messages transcript is part of the session record; the orchestrating agent quotes or paraphrases into the shared brief at Convene.
- **(b) orchestrating-agent pretrained knowledge** — IN, conditionally. The orchestrator brings this in when composing the shared brief and when writing the session's narrative. Provenance: when the orchestrator uses pretrained knowledge in a way that shapes a workspace decision, that introduction happens explicitly in Convene (framing the brief) or Deliberate (surfacing an external analogue) — not silently in Read.
- **(c) perspective pretrained knowledge** — IN, but with a specific channel. Perspectives bring pretrained knowledge — that is what makes them useful. They bring it via the brief's framing and via their role-specific stance, and they may use it inside their independent reasoning. The `multi-agent-deliberation.md` constraint ("perspectives reason from the brief") is not a prohibition on pretraining; it's a prohibition on reading workspace files or using tools during the independent phase. A Reviser drafting kernel text uses pretrained knowledge about specification-writing; that's fine. The constraint that matters is: the perspective surfaces external analogues explicitly (e.g., "[external analogue: ...]"), not silently.
- **(d) explicit in-session research (web, document lookup)** — IN, conditionally. Where available, research is a legitimate Read input for external artefacts. Provenance: the orchestrator records what was searched, what was read, and which reference was cited, in the session record. Perspectives do not run research during the independent phase (the `multi-agent-deliberation.md` constraint is binding here); if research is needed, it runs before Convene or between Deliberate and Decide.
- **(e) external reference materials the user cites** — IN. These are closest to (a) — user-provided inputs. Provenance: cite the reference.
- **(f) all of the above** — essentially yes, with the channel constraints named above.

**Boundary.** Domain reading is not a licence to launder outside ideas into workspace decisions. It is a name for inputs that are *already* entering the session at Convene/Deliberate via the brief, the user's messages, and the perspectives' pretraining; the name exists so that future readers can see those inputs counted as part of Read rather than disguised as workspace reading or pretending not to exist.

**Provenance mechanisms.** Three, each cheap:

1. **In-brief attribution.** When the orchestrator includes domain knowledge in the shared brief, attribute ("user stated X at session open"; "decision-theory framings commonly include Y"). This is already how Session 010's brief worked.
2. **External-analogue flagging in perspective responses.** `[external analogue: ...]` — the constraint from §5 of the current brief — is a perspective-level mechanism for surfacing pretrained inputs without silent import.
3. **Session-record listing.** The session's Record activity names the domain inputs it drew on, so future readers can audit.

**Reconciling pretraining-as-domain-reading with the "perspectives reason from the brief" constraint.** Pretrained knowledge that a perspective brings to its independent reasoning is not "reading" in the sense Stance Briefs forbids (which is reading workspace files or using tools). It is pre-existing capability. The Read activity at the kernel level encompasses the session's absorption of domain knowledge, much of which is delivered to perspectives via the shared brief. When a perspective draws on pretraining inside its independent response, it flags it. That is the reconciliation.

## Q4

The tension is real but resolvable. Let me state it plainly:

- **PROMPT.md rule:** Do not import ideas from outside the process silently. External inputs must be introduced via explicit surveying/hypothesising steps.
- **`multi-agent-deliberation.md` §Stance Briefs:** Perspectives reason from the brief during the independent phase.
- **W1 revision:** Name "domain reading" as part of kernel §1, legitimising outside inputs at the first activity of every session that handles external artefacts.

The apparent contradiction: W1 says outside inputs are fine at Read; PROMPT.md says they need explicit handling. The reconciliation: **naming an input as "domain reading" IS the explicit handling.** The rule isn't "no outside inputs"; the rule is "no silent outside inputs." Giving domain reading a named kernel slot is the opposite of silent import — it makes outside inputs a first-class, auditable element of the session.

**Proposed reconciliation text, as a trailing clause in the "Domain reading" sub-section:**

> Record what domain inputs were taken, from whom, and where they entered the session; outside inputs that change a workspace decision are surfaced through Convene and Deliberate, not committed silently (PROMPT.md).

The clause does two things: (i) mandates provenance for domain inputs at Read; (ii) preserves the distinction that *workspace decisions* (kernel revisions, spec changes, D-records) still go through the surveying/hypothesising pipeline. Domain reading is for inputs into an external artefact's content, not for smuggling conclusions into workspace self-changes.

**A sharper framing:** there are two kinds of "outside idea." Domain knowledge that shapes the external artefact (how a psoas release works; how decision-making under time pressure fails) is outside in the sense that it originates outside the workspace — but it is inside the session that produces the artefact, and it has to be. Outside ideas that would change workspace self-description (a new activity in the kernel, a revised provenance convention, a structural pattern imported from somewhere else) are the ones PROMPT.md's rule primarily targets, because those silently rewrite the methodology's self-knowledge. Domain reading is explicitly about the first kind. The reconciliation text should make that visible.

**Concrete failure mode the carve-out could produce.** Session X is producing an external artefact. A perspective (or the orchestrator) wants a workspace-level revision — say, adding a new activity to the kernel. They rationalise it as emerging from "domain reading": "the user's framing implied we need a Reflect activity." But what actually happened is the perspective imported a methodology idea from pretraining (e.g., an Agile retrospective pattern) and dressed it as domain input. The D-record says "domain-read; incorporated." Silent import, laundered through Read.

**Mitigation.** The kernel's §4 Deliberate and §5 Decide are the guards. Any workspace decision requires deliberation and an explicit D-record with reasoning; that's where silent import gets caught. The reconciliation text above holds: domain reading populates the inputs, but workspace decisions still route through Deliberate/Decide with reasoning that is traceable to the brief's content, not to a diffuse "domain read suggested it" gesture. Reviewers reading the D-record should be able to point to a specific brief line or surveying step that supports the decision. If they cannot, the decision is ceremonial or smuggled.

A second mitigation that is not in-scope for this revision but worth naming: at some future point, an explicit "surveying step" artefact convention — where external analogues are logged separately from workspace-internal reasoning — would close this gap tighter. Out of scope for W1.

## Q5

**G/O/K/S check on the Q1–Q4 proposal.**

- **(G) Translation-to-external-frame.** Satisfied. The need for the revision can be stated in external terms: "When the methodology produces artefacts like the back-mobility sequence (Session 008) or the household decision guide (Session 010), a significant source of the session's reasoning is domain knowledge that the current kernel §1 does not name. A reader applying the kernel to a new external artefact — say, writing a sequence for a wrist injury — would find §1 Read silent on where they should gather domain knowledge and how they should count it. The revision fixes that silence."
- **(O) Narrows-external-action-decision-space.** Partially satisfied. The revision does not unblock a specific external action in the immediate queue. But it narrows the decision space for the next external-artefact session: domain reading will have a named place. Session 012 or 013, producing an artefact in a new domain, benefits. The narrowing is real but modest.
- **(K) External-reader visibility.** Satisfied. A reader outside the workspace reading the kernel for the first time, after seeing Sessions 008 and 010's artefacts, would notice the current §1 Read's silence — it literally says only "absorb the full current state of the workspace," which is demonstrably not all that Sessions 008 and 010 did. The gap is reader-visible. Fixing it is reader-serving.
- **(S) Specific-obstacle resolution.** Satisfied. The obstacle is W1, an open watchpoint on the register since Session 008 (D-051). Its closure changes what later sessions can do in a small but concrete way: sessions producing external artefacts can cite kernel §1's "Domain reading" sub-section when explaining their Read step, rather than re-inventing the explanation.

**Verdict:** The revision satisfies G, K, S clearly and O partially. That is a comfortable pass under the criterion-package. Honest note: the revision is not a dramatic unblock. It is a small, correct piece of drafting with durable value. If it came up against hard resourcing constraints, it is defensible as session work; if the question is "is this the highest-yield session work we could do right now," the answer is "probably yes given domain validation on Session 010 is pending."

**The refuse-the-revision case.** The strongest form:

> The kernel is the methodology's minimal description of what a session does. External-domain work is a particular application of that minimal description. Each application may have conventions specific to it (domain-knowledge handling, reference-citation styles, user-engagement patterns). Those conventions do not belong in the kernel; they belong in an `external-applications.md` or an `applications/CONVENTIONS.md` document. The kernel stays tight; applications elaborate as needed.
>
> Under this view, W1's finding is true but mis-addressed. The finding should produce an **application-layer spec**, not a kernel revision. Session 011 would then decline to revise §1 Read and would instead draft an applications-layer convention that names domain reading.

**Why I reject it.** Three reasons, in order of weight:

1. **The asymmetry is in the kernel activity itself, not in an application's elaboration.** "What does Read consume" is a first-order question about what the activity *is*. Moving that to an applications-layer document says "§1 Read means one thing, and sometimes in some applications it means a different thing that we describe elsewhere" — which is a worse read than "§1 Read has two senses, named." The §7 Validate precedent already established that kernel activities can carry two senses when the asymmetry is load-bearing. W1 is the same shape as W4.
2. **Kernel minimality is not an argument against accurate kernel text.** The current §1 is minimal but incomplete: it says Read is "absorb the full current state of the workspace," which under-describes what Sessions 008 and 010 did. Refusing the revision preserves a minimal-but-wrong kernel over a slightly-longer-but-right kernel. That is a bad trade.
3. **An applications-layer spec is a larger move than W1's scope.** Inventing `external-applications.md` in Session 011 is out of scope under D-058's single-increment discipline. It is also a bigger structural decision than the current session can carry without its own brief and its own deliberation.

**Residual concern.** The refuse case does flag a real risk: if §1 and §7 both gain sub-sections, and future sessions keep finding asymmetries, the kernel could grow. That is a bounded risk, not a reason to decline the current revision, but it is worth an open issue — "when does an accumulating self/external asymmetry trigger extracting application conventions to a separate spec." I would support recording that as an issue at Record, not as a reason to defer W1.

## Meta-note

(a) My position likely to differ from other perspectives: I commit to **both** parallel sub-sections *and* PROMPT.md reconciliation text embedded in §1 Read, rather than sub-sections alone or a pointer to a separate reconciliation section. An Adversarial perspective will likely argue the reconciliation clause over-extends §1 and belongs in PROMPT.md cross-reference; a Minimalist perspective will likely argue against sub-sections entirely. I hold both because Sessions 008 and 010's actual Read steps require both the sense-split and the provenance clause to be described truthfully.

(b) Suspect brief assumption: the brief treats the §7 Validate precedent as "adjacent but not binding." I think it is closer to binding than not-binding, given that the two activities carry the same asymmetry; calling it non-binding under-weights the parallelism argument.

(c) Framing concern: Q3's (c) sub-option ("perspective pretraining as domain reading") is ambiguous and the brief asks for reconciliation without quite defining whether pretraining is an input at Convene or at Read. My Q3 answer treats it as entering at Convene-via-brief, read at Read.
