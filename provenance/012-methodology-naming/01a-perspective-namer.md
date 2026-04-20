---
session: 012
title: Perspective — Namer
date: 2026-04-20
status: committed-verbatim
perspective: namer
committed_at: 2026-04-20
---

## Q1

Identity threshold: **conditional-yes**, with the condition being that naming be load-bearing rather than ceremonial (it must satisfy at least one G/O/K/S criterion, and the chosen name must be argued from identity rather than imported).

The three strongest identity markers:

1. **The nine-activity kernel (Read → Close) as a stable frame.** Eleven sessions have exercised this same sequence. Kernel sections have been revised (§7 in Session 009, §1 in Session 011) but the nine-activity shape has not. This is a recognisable silhouette — not a collection of practices, a specific frame. Recognisability is the substrate of a name: you can only name something whose outline is stable enough that the name points to the same thing next year.

2. **Preservation-by-versioning as a distinctive pattern.** v1 → v2 → v3 with explicit `supersedes`/`superseded-by` pointers, rather than overwriting. This is rare. Most methodologies either freeze (treating v1 as sacred) or churn (treating old versions as garbage). This workspace treats superseded specs as durable provenance. A name can honour this without having to name it explicitly.

3. **Provenance as a first-class output.** 62 decisions with rationale and rejected alternatives; four parallel perspective outputs committed verbatim from prior sessions. The methodology doesn't just produce specs — it produces the reasoning trail that led to those specs, and treats that trail as a durable artefact equal in weight to the spec itself. Two external artefacts shipped (one validated) demonstrate this isn't only self-referential.

**Under-developed markers — things a name should *not* commit to:**

- **External adoption.** Two external artefacts, one validated, one pending. This is a track record but not a proven general-purpose methodology. A name that implies "framework for X" risks overclaiming. The name should not presume a particular external domain.
- **Tooling/automation.** Trigger-coverage annotations are machine-readable in principle but no tooling enforces them. A name evoking software infrastructure ("engine," "kernel-as-platform," "OS") overcommits to automation that doesn't exist.
- **Community/practice-of.** One practitioner, one workspace. A name carrying "school," "practice," or "tradition" connotations is premature.

So: identity is sufficient to name *what the methodology has become* — a deliberation-and-provenance discipline with a nine-activity spine and a preservation convention. It is not sufficient to name *what the methodology aspires to be.* The candidates in Q2 are constrained accordingly: they must point at what exists, not at ambition.

## Q2

Five candidates. Each emerges from an identity marker the methodology already exhibits; none is borrowed wholesale from an existing framework.

### Candidate 1: **Ninefold**

(a) **Ninefold.**
(b) Derivation: the kernel has nine activities (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close). "Ninefold" is an English compound meaning "of nine parts" or "nine-layered." It is a shape-word, not a content-word. [external analogue: Buddhist *Noble Eightfold Path* — flagged because "N-fold" as a methodology label is a recognisable pattern; it applies here because the methodology's most stable marker genuinely is the count and order of its activities, not because "-fold" is a trendy suffix.]
(c) Emphasises: the nine activities as the spine. The claim the methodology most strongly supports.
(d) Hides: provenance, the preservation convention, multi-perspective deliberation. Someone hearing "Ninefold" does not learn that perspectives disagree on record or that superseded specs are preserved.
(e) Collision: "Ninefold" is in use as a cloud-services company name and as a general English word. No major methodology collision I am aware of. Moderate risk: the company is small enough that confusion is local rather than global, but searchability is degraded.

### Candidate 2: **Kernel Method**

(a) **Kernel Method.**
(b) Derivation: `methodology-kernel.md` is the central specification. "Kernel" is already the workspace's term-of-art for the nine-activity core. "Method" follows the plain English pattern ("the X method") without overclaiming.
(c) Emphasises: the kernel as irreducible core — the small, stable centre around which specifications accrete.
(d) Hides: everything orbital. Nothing in the name indicates provenance, versioning, or deliberation.
(e) Collision: **severe.** "Kernel method" is a well-established term in machine learning (support vector machines, kernel PCA, Gaussian processes). Any search returns ML literature. This is almost certainly disqualifying — a practitioner saying "we used the Kernel Method" in 2029 will be misheard immediately. Including it mainly so the ranking has a clear reject.

### Candidate 3: **Strata**

(a) **Strata.**
(b) Derivation: the preservation convention produces layers — v1, v2, v3 of specs co-exist with supersession pointers. The workspace's history is legible by reading down the layers. "Strata" (geological) captures this.
(c) Emphasises: preservation, time-depth, the legibility of superseded reasoning. The methodology's most distinctive structural commitment.
(d) Hides: the nine-activity sequence, deliberation, the kernel. A name focused on vertical accumulation rather than horizontal process.
(e) Collision: "Strata" is widely used — a social-tech company, multiple software products, a font. As a methodology name specifically, I am not aware of a direct collision, but the word is crowded. Searchability poor. Recognisability as a concept good.

### Candidate 4: **Session Kernel**

(a) **Session Kernel.**
(b) Derivation: two of the methodology's most load-bearing nouns. The workspace organises work into *sessions*; each session exercises the *kernel*. "Session Kernel" points at the unit (one session = one kernel-execution = one increment). Already implicit in `SESSION-LOG.md` plus `methodology-kernel.md`.
(c) Emphasises: the increment discipline — the fact that this methodology produces one increment per session and treats sessions as the unit of account. Memorable, internal vocabulary, honest to current practice.
(d) Hides: nothing that isn't present. But: "Session Kernel" sounds like software infrastructure (Jupyter kernels; OS kernels), which risks overclaiming as a computational system.
(e) Collision: "session kernel" appears in Jupyter/computing contexts as a common noun — a Jupyter session has a kernel. This is moderate collision: different enough that a sentence "the Session Kernel methodology" reads cleanly, but searchability is mixed.

### Candidate 5: **Record Kernel**

(a) **Record Kernel.**
(b) Derivation: pulls together two of the methodology's most distinctive commitments. The kernel (nine-activity spine) and the Record activity (which, combined with preservation-by-versioning, yields the provenance artefact). "Record Kernel" names the pairing that distinguishes this methodology from methodologies that have a spine but no preservation, or preservation but no spine.
(c) Emphasises: the binding of increment-shape to provenance. That is, it names the methodology's actual thesis — that decisions and their reasoning trail are inseparable outputs of a single disciplined process.
(d) Hides: deliberation and multi-perspective participation. Someone hearing "Record Kernel" might expect a single-agent workflow.
(e) Collision: none I am aware of. "Record" and "kernel" are both common, but the phrase "record kernel" is not in use for any methodology, software, or book I can recall. Searchability likely clean initially.

## Q3

**Criteria, weighted.**

1. **Honesty to identity** (weight: highest). Does the name point at something the methodology actually is, or at something it merely aspires to? A name that overclaims fails Constraint A. This is the gating criterion — a name failing here is rejected regardless of other virtues.

2. **Collision-avoidance / searchability** (weight: high). Can a practitioner in 2029 say the name and be understood without caveat? Can an external reader search the name and find this methodology first, or at least find it without confusion? A name that loses to dominant existing usages is permanently handicapped.

3. **Resistance to ossification** (weight: high). Does the name pre-commit the methodology to a specific content it might outgrow? A name anchored to the nine-activity count ossifies more than a name anchored to a broader shape.

4. **Non-pretentiousness** (weight: medium-high). Does the name claim more grandeur than the methodology's scope? "The [X] Method" is dry and honest; "The [X] Tradition" is pretentious given one practitioner and one workspace.

5. **Memorability** (weight: medium). A name that fits in a sentence and sticks. Short names with concrete referents tend to win; abstract compounds less so.

6. **External-legibility** (weight: medium). A first-time reader encountering the name in an external artefact's frontmatter should be able to form a rough hypothesis about what the methodology is. Names requiring a glossary lookup to make sense fail this.

7. **Translatability** (weight: low-medium). Does the name embarrass in any language I can check? Short English nouns usually travel; puns and idioms don't.

**Explicit tradeoffs.**

- Honesty-to-identity competes with resistance-to-ossification. A name that points at the nine-activity spine is honest *now* but ossifies if the spine ever changes. A name that points at a broader shape is more future-proof but less distinctive.
- Memorability competes with collision-avoidance. Short concrete names are memorable but more likely colliding with existing usages; distinctive compounds are less collision-prone but less memorable.
- Non-pretentiousness competes with external-legibility. "The Kernel" is non-pretentious but so generic that a first-time reader learns nothing; "The Nine-Activity Provenance Discipline" is legible but pompous.

**Ranked evaluation of Q2 candidates:**

| Criterion (weight) | Ninefold | Kernel Method | Strata | Session Kernel | Record Kernel |
|---|---|---|---|---|---|
| Honesty (highest) | strong | strong but narrow | strong | strong | strongest |
| Collision (high) | moderate | **fails** | weak | moderate | strong |
| Ossification (high) | weak (tied to count) | moderate | moderate | moderate | strong |
| Non-pretentious (med-high) | strong | strong | moderate | strong | strong |
| Memorability (med) | strong | strong | strong | moderate | moderate |
| External-legibility (med) | weak | weak (ML confusion) | moderate | moderate | moderate |
| Translatability (low-med) | moderate | strong | strong | strong | strong |

**Ranking:**

1. **Record Kernel** — strongest overall. Honest to the methodology's actual thesis (preservation-bound increment discipline), low collision, resists ossification because neither "record" nor "kernel" pre-commits to the exact nine activities.
2. **Ninefold** — memorable and shape-pointing but ossifies to "nine"; if a tenth activity were ever added the name becomes a liability.
3. **Session Kernel** — honest, memorable internally, but software-infrastructure connotations risk overclaiming.
4. **Strata** — beautiful but hides the kernel.
5. **Kernel Method** — rejected on collision grounds alone.

## Q4

**Preferred placement:** kernel frontmatter only, v-bump the kernel.

Concretely, add one line to `methodology-kernel.md`'s frontmatter: `name: Record Kernel` (or whichever name is chosen), and bump the kernel's version (e.g., v3 → v4 on §0 or wherever frontmatter sits). The kernel's title becomes "The Record Kernel" or similar in the document heading. This is the minimum placement that makes the name canonical — the kernel is the one specification every external reader will read first, and naming it is equivalent to naming the methodology whose spine it is.

**Why kernel-only, not broader:**

The name becomes load-bearing (satisfies K — external-reader visibility — because anyone reading `methodology-kernel.md` encounters the name immediately) without requiring revisions to PROMPT.md, SESSION-LOG.md, multi-agent-deliberation specs, workspace-structure specs, or validation-approach specs. Each of those additional placements would require its own v-bump under D-016 trigger coverage, and would invoke D-023 multi-agent requirements on some (multi-agent-deliberation and validation-approach are D-023 spec-families). A kernel-only placement keeps Session 012 single-increment (Constraint D).

**Trigger coverage for kernel-only placement:** the kernel is itself a D-023 specification (it was revised under required-trigger deliberation in Sessions 009 and 011). Session 012 *is* a required-trigger deliberation — four perspectives, non-Claude participation — so this placement is covered by the session's existing deliberation rather than requiring additional work.

**Alternatives rejected:**

- **PROMPT.md first-paragraph self-reference.** Rejected. PROMPT.md is the prompt applied each session; adding the name to its first paragraph commits every future session-kickoff to invoking the name. This over-burdens the workspace — it makes the name feel compulsory rather than referential. Also risks circular reading: PROMPT.md's own constraint is that vocabulary emerge from process; prominent self-reference in PROMPT.md confuses prompt-text with emergent identity.
- **New `specifications/identity.md` file.** Rejected. A dedicated file for the name overstates the name's weight — a name is a single string, not a specification. A file invites expansion (mission statements, values) that Session 012 is not scoped to produce.
- **No canonical placement, external-references only.** Rejected for the opposite reason. If the name isn't in any workspace artefact, it isn't canonical, and the methodology can't claim to have named itself — it's only claiming that agents refer to it by a name externally, which doesn't resolve the open issue.
- **SESSION-LOG.md header.** Rejected as primary placement (the log is a record, not a specification), but a passing mention in the Session 012 log entry is natural and uncontroversial.

## Q5

The refuse-to-name case at its strongest:

**The Session 001 dissent is not falsified by identity accumulation; it anticipated exactly this.** The Skeptic said names create attachment — once named, the methodology becomes an identity to defend. Eleven sessions of accumulation make *defending the current shape* more tempting, not less. A name arriving now crystallises whatever state the methodology happens to be in at Session 012 — which is substantially self-infrastructure, with only two external artefacts. Naming now risks locking in a self-focus that the methodology should grow out of.

The Minimalist said naming is premature. Two external artefacts, one validated, one pending, is still a small track record. A methodology's name should come from what it has done, and what it has done is mostly exist. The G/O/K/S criterion-package exists precisely because self-work tempts self-ceremony; naming the methodology is paradigmatically self-ceremony unless rigorously justified.

**What evidence would make naming clearly right?** Three candidates:

1. *External adoption by a second practitioner* — if someone outside this workspace used the methodology (kernel, provenance conventions, versioning) to produce their own external artefact, the methodology would have demonstrably become a thing distinct from its originator, and naming would be descriptive rather than constructive.
2. *A third external artefact, domain-validated* — the sample is too small at n=2 (one validated). n=3 with validation begins to look like a track record rather than a handful of attempts.
3. *A failure mode the name-absence created* — if "the methodology" proves actually confusing in real external-reader contexts (not hypothetically awkward), the name addresses a concrete obstacle (criterion S).

None of these conditions is met.

**Form of the decline if Session 012 refuses:** OI-001 remains open; add a note that Session 012 engaged the question, reaffirmed the threshold is not met, and specified the three conditions above as triggers for re-opening. The question is not retired, not deferred indefinitely, but held with explicit conditions that make re-opening principled rather than arbitrary.

**My honest assessment.** The refuse-to-name case is stronger than I want it to be. My Q1 answer was conditional-yes, but the condition — that naming be load-bearing — is genuinely hard to satisfy. Does naming resolve a specific obstacle (S)? No obstacle has been named that name-absence blocks. Does it narrow external-action decision-space (O)? Only if a named third external artefact's frontmatter benefits from a methodology name — possible but speculative. Does it translate to external frame (G)? Only weakly: "the methodology" is awkward, not broken.

I will still argue for Record Kernel if the session decides to name, because it is my role to do so and because if the session names now, Record Kernel is the best candidate. But I record here that the refuse-to-name case, seriously engaged, is approximately as strong as the name-now case, and a Session 012 decision to hold OI-001 open with the three conditions above would be defensible — possibly more defensible than naming.

This is the tension my role-specific stance asked me to record rather than soften. It is recorded.

## Q6

**What naming changes — concrete steering from "Record Kernel":**

1. **Future self-presentation will accentuate the Record activity and preservation-by-versioning.** A methodology whose name literally contains "Record" will — whenever its practitioners introduce it — begin by explaining that record-keeping is first-class. This *does* align with the methodology's actual distinctive commitment, so the steering is honest, but it will lead to sessions framing new work through the provenance lens by default. For example: a future session producing a new external artefact will more naturally emphasise the artefact's provenance directory than the artefact itself, because "Record Kernel" has primed that emphasis.

2. **Tension with Decide.** "Record Kernel" subtly demotes the Decide activity in the nine. A casual reader might infer that this methodology is primarily a record-keeping discipline. It is not — decisions (D-001 through D-062) are load-bearing outputs, and the Decide activity is structurally equal to Record. The name's framing effect *understates* Decide. This is a cost of the name, and should be acknowledged in any placement.

**What naming does NOT privilege — a property left available to future sessions:**

"Record Kernel" says nothing about **deliberation** or **multi-perspective participation**. The Deliberate activity and the multi-agent-deliberation specification (perspective shapes, non-Claude participation, closure criteria) are some of the methodology's most elaborate work. A future session could, without tension with the name, foreground deliberation as the central practice — write a mission-statement-style artefact arguing that disciplined multi-perspective deliberation is the methodology's core contribution. "Record Kernel" does not block this framing; it leaves deliberation available as a future emphasis-target.

Similarly, the name does not privilege any external domain. A session producing a third external artefact (in a domain quite different from back-pain sequences or household decisions) would not be name-constrained; "Record Kernel" is domain-neutral.

**If refusing to name (per Q5's strongest form):** staying unnamed steers the methodology toward *description-by-listing* rather than *description-by-label*. External readers must be told "it's a deliberation-and-provenance discipline with a nine-activity kernel and a preservation-by-versioning convention" rather than "it's [Name]." This is awkward in prose but it keeps the methodology provisional and legible — every description is an invitation to examine what the description actually refers to, rather than a shortcut that conceals the referent. Staying unnamed steers away from any version of "once named, defended as identity" — the concern Session 001's Skeptic raised.

## Meta-note

(a) **Position likely to differ from other perspectives.** I expect at least one perspective (Historian-flavoured) to argue identity is clearly sufficient and naming is overdue; another (Skeptic-flavoured) to argue strongly for refusing. My Q1 conditional-yes plus Q5 honest engagement with the refuse-case will likely sit between those poles. I am also likely to be more conservative about placement (kernel-only) than perspectives who will want the name in PROMPT.md. My salient differentiator: I weight collision-avoidance and resistance-to-ossification higher than memorability, which should show in my Q3 table and ranking.

(b) **Suspect assumption in the brief.** The framing that a name lives on a scale "no name ↔ provisional name ↔ permanent name" is partly a false trichotomy. A name can live in kernel frontmatter only and be treated as revisable under normal v-bump discipline — that's a real fourth option the brief underweights.

(c) **Framing concern.** The brief leans implicitly toward "name or not." The actually-hard question is *whose reader is the name for* — internal agents or external adopters. I answered assuming external readers; another perspective might reasonably answer assuming internal coherence, and the synthesis should surface that split.
