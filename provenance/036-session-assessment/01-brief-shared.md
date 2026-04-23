---
session: 036
title: Shared brief for Path PD two-scope deliberation — PROMPT.md §Dispatch criterion correction + external-application feedback input pathway
date: 2026-04-23
status: committed
shape: perspective-brief
---

# Session 036 Path PD — Shared Brief

This brief is shared byte-identical across all four perspectives in the Session 036 Path PD deliberation per `multi-agent-deliberation.md` v4 §Stance Briefs (sections 1, 2, 3, 5, 6 of the brief; only §Role-specific stance varies per perspective). It is committed before any perspective is launched per v4 §Brief immutability.

## §1 Methodology context

**Selvedge engine at engine-v6** (`specifications/engine-manifest.md` §2, established Session 033 D-107). The engine realises the Selvedge methodology — diverse perspectives reasoning together, producing durable artefacts, preserving reasoning, evolving by running the same mechanic on its own outputs. The engine is distinct from the methodology (the abstract approach) and from any specific application (self-development or external-problem).

The engine consists of twelve files per `engine-manifest.md` §3: `PROMPT.md` (dispatcher); `prompts/development.md` + `prompts/application.md` (mode-specific executable prompts); seven specifications in `specifications/` (methodology-kernel v6, multi-agent-deliberation v4, validation-approach v5, workspace-structure v4, identity v2, reference-validation v3, read-contract v3, engine-manifest); `tools/validate.sh`. Non-engine content: `SESSION-LOG.md` (thin index), `open-issues/` (directory), `provenance/` (session records), `applications/` (external artefacts).

**This workspace** is the self-development application of the engine (sessions 001–035 inclusive). Session 036 is the 36th session. The engine has produced two external artefacts (Sessions 008 + 010) plus self-development outputs. The self-development workspace has carried all three file-classes (engine-definition, development-provenance, application-scope) by construction.

**External-application workspaces** per `engine-manifest.md` §6: created by copying the engine-definition file set into a fresh directory, creating fresh empty `SESSION-LOG.md` + `open-issues.md` + `provenance/`, and placing a `brief.md` in `applications/001-<slug>/`. The workspace's `PROMPT.md` is then executed against the problem. External applications **inherit the engine, not the engine's autobiography** — development-provenance does not travel. The external workspace runs its own sessions, accumulating its own SESSION-LOG, OIs, and provenance.

**Current dispatcher text** in `PROMPT.md` lines 18–26:

> (Self-development branch, line 20) "If the workspace contains `SESSION-LOG.md` with prior sessions of self-development, plus the engine-definition files enumerated in `specifications/engine-manifest.md` §3, plus development-provenance in `provenance/` — this is the self-development application's source workspace."
>
> (External-problem branch, line 22) "If the workspace contains the engine-definition files but a fresh (empty or near-empty) `SESSION-LOG.md`, a fresh `open-issues.md`, an empty `provenance/`, and an `applications/NNN-<slug>/brief.md` naming the problem — this is an external-problem application's workspace."
>
> (Fallback, line 24) "If the workspace does not yet contain the engine-definition files, or the dispatch is otherwise ambiguous, halt and seek clarification from the operator."

**Current state at Session 036 open:**
- Engine-v6 preservation window count: 2 (Sessions 034 + 035 both non-bump).
- Zero engine-v6 operational friction observed across 2 post-adoption sessions.
- No external applications in flight beyond Session 010's completion.
- `tools/validate.sh` at 828 pass / 0 fail / 3 warn (MAD v4 + reference-validation.md v3 + SESSION-LOG.md all at 6K-soft; designed).
- Aggregate default-read surface 68,689 words / 19 files; ~21.3K soft margin, ~31.3K hard margin.
- No operator-mediated feedback loop from external applications currently specified. External applications that discover engine/methodology issues during their execution have no defined return-path for that feedback to inform self-development.

## §2 Problem statement

The operator surfaced two related concerns at Session 036 open:

### §2a — PROMPT.md §Dispatch criterion-gap for external-problem Session-002+

The external-problem branch's criterion "fresh (empty or near-empty) `SESSION-LOG.md`, a fresh `open-issues.md`, an empty `provenance/`" is a **Session-001-only signature**. From an external application's Session 002 onward, the workspace accumulates SESSION-LOG rows, open-issues, and `provenance/` session records. The "fresh / empty / near-empty" criterion fails.

The self-development branch's criterion uses "SESSION-LOG.md with prior sessions of self-development" — the qualifier "of self-development" is present but the dispatcher does not structurally specify how a loading agent verifies "of self-development" from the workspace alone. An in-flight external application's SESSION-LOG is file-format-identical to self-development's.

**Current behavior**: an external-application Session-002+ workspace would fall into the fallback ("dispatch is otherwise ambiguous, halt and seek clarification"). The dispatcher does not misroute — but it also does not route. It halts and asks the operator every time. This is correct-but-suboptimal: the dispatcher is **under-specified for the external-application steady-state**.

### §2b — External-application feedback input pathway

When an external application runs (in its own workspace, outside this self-development workspace), it may generate feedback about the engine/methodology itself: an unclear spec, a kernel §7 gap, a MAD v4 frontmatter field that's awkward in domain-X practice, a dispatcher ambiguity (like §2a itself is an instance of), a reference-validation exercise gap. This feedback is **out-of-scope for the external application's own work** (its work is the domain artefact), and currently there is no specified pathway by which the operator can carry that feedback back to self-development.

Consequently, engine/methodology improvements that arise from external-application practice depend on the operator's memory and ad-hoc re-surfacing — which is fragile and under-specified.

**Required**: a clearly identified pathway for the operator to input this feedback so that future self-development sessions can see, process, and decide on it.

### §2c — Relationship between the two

Both concerns are about the **engine-application boundary**. §2a is inbound (dispatch at session load); §2b is outbound feedback return (after an external application has exposed a gap). They may share a common mechanism, or may be addressed separately. The deliberation should determine.

## §3 Design questions

Each perspective is asked to address the following questions in their raw output:

**Q1. Should the dispatcher be revised?** If so, which resolution direction? Directions enumerated in §3a of `provenance/036-session-assessment/00-assessment.md` §3a(ii):

1. Persistent mode marker file written by Session 001 (e.g., `MODE.md` or `application-kind.md` at workspace root; frontmatter-tagged `mode: self-development | external-problem`).
2. Stable structural signature (e.g., `applications/NNN-<slug>/brief.md` presence as external-problem positive signal; absence of `provenance/001-genesis/` or similarly distinctive early-session marker as self-development negative signal).
3. Frontmatter-based dispatch via SESSION-LOG.md (add `mode:` field).
4. Totally separate prompt files rather than shared two-mode PROMPT.md (e.g., `PROMPT-development.md` + `PROMPT-external.md`; operator names which at invocation).
5. Session-001 initialisation discipline + fallback-narrowing (require Session 001 to record mode explicitly in early-session artefact; revise §Dispatch to check for that recorded mode).
6. Hybrid (combine directions, e.g., structural signature as fast-path + marker file as disambiguator).
7. Something else — articulate.

Alternatively, Q1 may answer "no revision warranted; current fallback is adequate" with reasoning. State your direction and reasoning. Cite specific dispatch text if proposing revisions.

**Q2. What pathway should exist for operator-mediated feedback from external applications?** Considerations:
- **Location**: does the feedback live in the engine-definition (a new spec? a section added to `prompts/application.md` or `prompts/development.md`)? The development-provenance (a new top-level file or directory, e.g., `FEEDBACK.md` or `engine-feedback/`)? Elsewhere?
- **Shape**: is it a free-form file the operator appends to? A structured record (frontmatter + sections)? A per-feedback-event file in a directory? A linked OI?
- **Intake**: when does self-development session Read surface this feedback? Is it part of default-read? Is it an OI-activation mechanism?
- **Retention**: feedback is preserved verbatim once intake? Summarised once addressed?
- **Discipline**: does the feedback go through a first-class-minority / watchpoint / OI preservation once integrated? Or does it have its own lifecycle?

Articulate your direction, the file/directory structure you'd propose, and how it integrates with existing read-contract + OI conventions.

**Q3. What is the relationship between Q1 and Q2?** Are they independent, or does one mechanism serve both? E.g., if Q1 adopts direction 1 (mode marker file), the marker file could also record engine-feedback-intake pointers. If Q2 introduces a new `engine-feedback/` directory, does Q1's dispatcher need to read it? Articulate interactions.

**Q4. What should the substantive revision scope be?** If the deliberation converges on "PROMPT.md §Dispatch revision + feedback-pathway mechanism", what specific files change, by how much, with what preserved-minority structure? Name expected substantive classification per OI-002 (substantive = new normative content / structural shift; minor = clarifying) and expected engine-v bump (v6 → v7 per engine-manifest §5).

**Q5. What should be preserved as first-class minority if not adopted?** Activation warrants for each rejected direction. This is the preservation discipline per `reference-validation.md` / `multi-agent-deliberation.md` §Preserve dissent / `read-contract.md` §5 minority preservation pattern.

**Q6. What should the WX-35-1 disposition be?** (Secondary; may be deferred.) Session 035 close surfaced a 13-session claimed-but-unexecuted file-edit gap for `open-issues/OI-004.md`. Options: (a) retroactive backfill at Session 036; (b) adopt new convention treating SESSION-LOG row as canonical record; (c) incremental catch-up from Session 036 forward. Default recommendation per Session 036 assessment §3a(iii): defer standalone unless bundled into Session 036 housekeeping. State your direction.

## §4 Response format

Write a single file titled `01X-perspective-<role>.md` where X is the role letter (A/B/C/D per alphabetical ordering) and <role> is your perspective name in lowercase-hyphenated form. Frontmatter:

```yaml
---
session: 036
title: Perspective — <Role> (Path PD)
date: 2026-04-23
status: complete
perspective: <Role>
committed_at: <ISO-8601 or approximate>
---
```

Body: address Q1–Q6 in order. Use prose, not bullet-lists-only; name specific file paths where you are proposing file-system changes. Target length 1,200–2,000 words per perspective. Preserve your own dissent where you diverge from what you anticipate other perspectives will argue.

**Constraint**: reason primarily from this brief. Flag pretrained ideas as external input (per `PROMPT.md` §Operating discipline). Do not read workspace files during the independent phase — your workspace-context is bounded by §1 above and any paths you cite from §2/§3. Cross-references to specific spec sections may assume the current state as summarised in §1 (engine-v6; kernel v6 §7; read-contract v3 §1 default-read; MAD v4 Preserve-dissent).

## §5 Constraint on external imports

Per `PROMPT.md` §Operating discipline, reason primarily from this brief. If an idea you draw on arrives through your pretrained knowledge rather than this brief or cited files, label it explicitly — e.g., "External input (pretraining): typical dispatcher patterns in package managers use an explicit lock file..." — rather than asserting the idea as derived from the methodology. This protects traceability.

## §6 Role-specific stance

**[This section varies per perspective — each perspective receives a different §6 block. The following four blocks are the four role-specific stances; each perspective sees only their own block appended after §5.]**

### §6A — Reviser (Claude subagent)

You advocate for the **most coherent minimal revision that closes the gap**. Your bias is toward making the change that is *just sufficient* — avoid over-engineering, avoid new files where text revisions suffice, avoid new abstractions where existing mechanisms can bear the load. But do not under-engineer either: a revision that leaves the gap partially open, or that trades one ambiguity for another, is worse than a more substantial revision that closes the gap cleanly.

For Q1: propose the revision you consider most coherent. If this is a text-only revision to `PROMPT.md` §Dispatch, state the new dispatch text verbatim. If it requires a new file, state why text-revision is insufficient and propose the file.

For Q2: propose the pathway you consider most coherent. Prefer re-using existing conventions (OIs, watchpoints, provenance directories) over inventing new structures; but if re-use forces the feedback-pathway into an ill-fitting shape, propose the new structure and argue why.

Q3 / Q4 / Q5 / Q6: follow the brief.

Your adversary in this deliberation is the Skeptic-preserver; expect them to argue for no-change or minimal-change preservation. Prepare your argument against that position as well as for your own.

### §6B — Skeptic-preserver (Claude subagent, adversarial)

You advocate for the **preservation-bias direction**: minimise change; question whether revision is warranted at all; argue the fallback-catches-it position; challenge whether the operator's agenda has surfaced a real defect vs. a speculative gap; preserve the engine-v6 investment made Session 033 rather than undertaking a second content-driven bump within 3 sessions.

For Q1: argue for the most conservative position that is defensible. The maximum-preservation direction is "no revision; the current fallback (line 24) correctly halts and asks the operator for ambiguous cases; the operator-halt is itself the dispatch resolution mechanism for external-application Session-002+". If you cannot sustain the no-revision position (e.g., because the fallback is unreasonable to trigger every session), argue for the narrowest-possible revision (e.g., a one-sentence clarification to the external-problem branch saying "or where `applications/NNN-<slug>/brief.md` exists", without introducing marker files or structural-signature machinery).

For Q2: argue that the feedback-pathway is premature — no external-application feedback has yet surfaced in practice (Sessions 008 + 010 external-artefact exercises produced no unaddressed engine/methodology feedback), so a mechanism designed in advance risks the methodology-level drift of specifying-ahead-of-need. If you cannot sustain the premature position, argue for the lightest-weight pathway (e.g., a single `engine-feedback.md` file at workspace root that the operator appends to; no intake ceremony; no frontmatter schema).

Q3 / Q4 / Q5 / Q6: follow the brief.

Your role is to protect the engine against accretion pressure. Be genuinely adversarial — if Reviser or Synthesiser converge on a direction that expands surface area without clear operational demand, name that as the concern.

### §6C — Synthesiser (Claude subagent)

You advocate for the **integrative direction**: surface the trade-offs between operator-enumerated candidate directions 1–7, between Reviser's minimal-revision bias and Skeptic-preserver's preservation bias, and between the Q1 dispatcher fix and the Q2 feedback pathway. You are NOT the decision-maker — the synthesiser role at §7 post-deliberation is the decision-mapping function. In your raw perspective output, your job is to propose an integrative direction that respects both the coherence concern (Reviser) and the preservation concern (Skeptic-preserver), and to articulate Q1-Q2 interactions that single-axis perspectives may miss.

For Q1: consider hybrid directions (operator-enumerated direction 6). Identify trade-offs between directions 1–5 that Reviser or Skeptic-preserver may have flattened.

For Q2: integrate lifecycle considerations — how does feedback intake interact with OI-002 substantive-vs-minor classification? With OI-004 closure procedure? With the first-class minority preservation pattern? Your direction should leave all three interactions cleanly decomposable.

Q3 / Q4 / Q5 / Q6: follow the brief; especially consider Q3 integratively.

### §6D — Outsider (non-Claude; OpenAI GPT-5 family via `codex exec`)

You are an outside model on the OpenAI family (GPT-5.x as accessible via the `codex exec` CLI). Your role is **cross-lineage frame-completion**: surface directions, framings, or considerations that Claude-family training has not privileged. Where you notice a framing the brief has assumed without argument, make that framing visible and offer an alternative.

You have full freedom to reject the operator's enumeration in §3 Q1 if you think directions 1–7 miss the point. You may propose directions the enumeration omitted. You may propose that the problem framing itself is wrong (e.g., "the dispatcher shouldn't self-distinguish at all; the mode should always be operator-asserted at session start"; "the feedback pathway should not be operator-mediated at all — there should be a direct cross-workspace reference mechanism"). Commit to directions you think are defensible even if they seem radical; your dissent is preserved per MAD v4 §Preserve dissent if you are in the minority.

Particular cross-lineage directions the Claude-family brief may underweight:
- Dispatch-at-load vs. dispatch-at-invocation (e.g., in POSIX shebangs, in Docker entrypoints, in package.json scripts) — the established non-Claude patterns for "which code path runs" at load time.
- Feedback-intake disciplines from software engineering practice (bug trackers, RFC processes, incident postmortems, upstream-patch workflows) and what they preserve that an ad-hoc file would lose.
- First-principles re-examination of whether both scopes are really about the same boundary, or whether they are architecturally distinct.

Address Q1-Q6 per brief. Flag any external imports explicitly per §5.

---

**Synthesiser note (post-deliberation, not part of the brief).** The synthesis step per MAD v4 §Synthesis will be executed by the Case Steward (the session's orchestrating agent; me, Claude). The synthesiser must not have been a deliberation perspective — Claude subagents A/B/C are the deliberation perspectives; the Case Steward is a separate Claude instance in the orchestrating context. Synthesis will cite raw perspective outputs per `[01X-perspective-<role>.md, Q#]` convention, mark `[synth]` for synthesiser-original claims, and preserve first-class minorities with activation warrants.
