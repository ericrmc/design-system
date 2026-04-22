---
session: 016
title: Assessment — Operator Reframing Input (Engine vs. Methodology)
date: 2026-04-22
status: draft — halt for user ratification before proceeding
---

# Assessment — Session 016

## 1. Read (workspace state)

Ran `tools/validate.sh` at session open: **363 pass, 0 fail, 0 warnings**. Seventh consecutive clean run at a session-opener (Sessions 010, 011, 012, 013, 014, 015, 016).

Active specifications (6):

- `methodology-kernel.md` v4 (last-updated Session 014, D-069; §7 Validate revised to name three senses).
- `workspace-structure.md` v2 (last-updated Session 009, D-054).
- `multi-agent-deliberation.md` v3 (last-updated Session 006, D-041).
- `validation-approach.md` v3 (last-updated Session 006, D-041).
- `identity.md` v1 (created Session 012, D-063).
- `reference-validation.md` v1 (created Session 014, D-069) — **still un-exercised**.

External artefacts (2 canonical, 1 superseded): unchanged from Session 015 snapshot.

Open issues: **12 active** (OI-002, OI-004, OI-005, OI-006, OI-007, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015). **4 resolved** (OI-001, OI-003, OI-010, OI-016).

Session 016 received a session-open operator input (preserved verbatim at `00-operator-input.md`). This input proposes a structural reframing of the workspace: the work produced across sessions may be better understood as an **engine** (defined inputs, procedures, outputs) rather than as a **methodology** in the abstract. The input offers two structural consequences as input rather than direction: (1) distinguishability of the engine's executable definition from the provenance of its development; (2) distinct execution prompts for different applications of the engine.

Session 015 D-072 precommitted Session 016 to execute Option A (first-exercise of reference-validation, Cell 1). The operator input explicitly authorises agenda re-examination: "Determine the session's agenda accordingly."

## 2. Audit of Session 015 synthesis fidelity

Per Session 015 close's next-session item 2, the audit surface for Session 015 is narrower (no deliberation): verify (a) Session 014 synthesis-fidelity findings in `015-session-assessment/00-assessment.md` §2 are consistent with cited raw-output line references, and (b) D-072's `[none]` triggers declaration is consistent with the decision's content per Q7.

### 2.1 — Session 014 citation consistency

Session 015 §2 cites four raw-output locations:

- **§2.1 cites `014-oi016-resolution/01a-perspective-architect.md` Q3 lines 67–91.** File exists; read. Architect's Q3 begins at line 67 (`## Q3 — Validation shape`) and concludes at line 91. Content: Architect argues for single-session iteration-within-session with three internal roles on the grounds that "validation signal cannot re-enter the Produce step — it can only trigger a new Produce step in Session N+2, with all the context reconstruction costs that entails." Session 015 §2.1's paraphrase is faithful; the cross-session feedback path is the named concern; Cell-2-internal-iteration addresses within-session emergent-constraint responsiveness. **Citation consistent.**

- **§2.2 cites `01c-perspective-skeptic.md` Q7 lines 146–177 and `01d-perspective-outsider.md` Q7 line 760.** Skeptic Q7: file contains Q7 with the "third kind of evidence … closer in kind to workspace-validation" framing and the "provisionally addressed by reference-validation mechanism, with the prior structural concern preserved" phrasing cited. Outsider Q7: single-line cite located. **Citations consistent.**

- **§2.3 cites `01c-perspective-skeptic.md` Q5 lines 106–122.** File contains Q5 with "provisional substitute" framing and the explicit "the language 'provisional substitute' is deliberate" line. Load-bearing-language claim is supportable. **Citation consistent.**

- **§2.4 cites `reference-validation.md` §1 line 46 "flagged tension" text.** Confirmed present as "Flagged tension (preserved per Session 014 Skeptic Q1)" paragraph in §1. **Citation consistent.**

**§2.1 substantive new-eyes finding:** the Session 014 close's phrasing "Cell-2 iteration budget mitigates Architect's continuous-loop concern" overstates; Architect's raw concern is the cross-session validation-to-Produce feedback path, not within-session emergent-constraint responsiveness. Session 015's §2.1 correctly distinguishes these and re-scopes WX-14-2. **Finding supportable and recorded correctly.**

### 2.2 — D-072 triggers declaration consistency

D-072 declares `triggers_met: [none]` with rationale: "does not modify the kernel (no d023_1), does not create or revise a specification (no d023_2, d023_3), does not change OI-004 state (no d023_4), and is not the output of a multi-perspective deliberation (no d016_1 substantive kernel, d016_2 new spec, d016_3 genuine cross-model disagreement, nor load-bearing d016_4 reasoning)."

Content of D-072: ratifies Option A as Session 015's agenda-shortlist output and applies defaults (mixed-direction shortlist; orchestrating agent as Case Steward; Stop 3b session shape); defers shortlist production. No specification file edited. No kernel file edited. OI-004 tally unchanged per D-072's own housekeeping paragraph. The decision is a planning record implementing explicit user steering.

**Verdict on consistency:** the `[none]` declaration is consistent with the decision's content. No d016_* trigger applies because the decision is not a novel design output requiring multi-perspective reasoning; no d023_* trigger applies because no kernel/spec file changed and no OI-004 state change was asserted. **Triggers declaration consistent with Q7.**

### Audit overall verdict

Session 015 is synthesis-fidelity-clean on both auditable dimensions. The one substantive new-eyes finding from Session 015 (§2.1 Cell-2-iteration-budget overstatement) is correctly scoped and has not grown or shifted under re-examination.

## 3. Surveying step — the engine-vs-methodology reframing under its explicit name

Per PROMPT.md anti-silent-import rule, the operator input must be introduced through "an explicit surveying or hypothesising step rather than committing it directly." Per OI-015 laundering-enforcement requirement, the input must be re-examined as a choice competing with alternatives at Deliberate or Decide, not absorbed as given context. This §3 performs the surveying step; §4 performs the hypothesising step; §5 maps consequences; §6 presents agenda options.

### 3.1 — What the current specifications actually say about "methodology"

A survey of the word's use in active specifications:

- **PROMPT.md** (15 occurrences of "methodology") frames the workspace as "building a design methodology" (line 3) and describes the methodology as "a structured approach for designing complex things." Uses abstract-approach language: "The methodology is not specific to any domain. … The methodology itself — the mechanic of diverse perspectives reasoning together, producing durable artefacts, preserving their reasoning, and evolving the system by running the same mechanic on its own outputs — is domain-general."
- **methodology-kernel.md** v4 titles itself "Methodology Kernel" and defines "the core process of the methodology: what happens during each application of the prompt, in what order, and to what standard." Uses operational language: "the minimum viable process — the kernel that every session follows."
- **identity.md** v1: "The methodology is referred to as Selvedge." Uses reference-handle language: "It is not a brand, a slogan, or a claim of school."
- **workspace-structure.md** v2 uses both "methodology" and "methodology-kernel" to describe what the workspace implements; uses "methodology" as a noun for the thing specified.
- **multi-agent-deliberation.md**, **validation-approach.md**, **reference-validation.md** all refer to "the methodology" as a functioning object with processes, checks, and outputs.

**Observation:** across six active specifications, "methodology" is used in two distinct ways that have not been distinguished:
1. **Methodology-as-abstract-approach** (PROMPT.md §3-§9): the domain-general mechanic of perspectives reasoning together, producing artefacts, preserving reasoning.
2. **Methodology-as-concrete-implementation** (methodology-kernel.md §Purpose; all operational-language uses): the specific kernel + multi-agent-deliberation + validation-approach + reference-validation + identity + workspace-structure that the workspace implements.

The operator's proposed reframing names these two senses: **methodology** for (1) and **engine** for (2). This is a terminological sharpening, not an invention. The two senses already exist in the specifications; they are currently labelled with the same word.

### 3.2 — What is structurally absent under the current framing

A survey of what the workspace does NOT currently contain, relative to what the operator's reframing presupposes:

- **No loadable engine-definition manifest.** There is no single artefact that says "to use this engine, load these files." Reading six active specs plus PROMPT.md plus understanding open issues is the current reconstruction path. A new user wanting to use the engine on their own problem must infer its boundaries.
- **No application-vs-self-development distinction in PROMPT.md.** PROMPT.md frames every session as advancing "the methodology's own development." It has no branch for "you are applying the engine to an external problem; load the engine and apply it."
- **No application-specific context-loading pattern.** The `applications/` directory holds external-artefact outputs but there is no pattern for "an application's own context" (its domain inputs, its stakeholders, its validation path, its session-log) distinct from the self-development workspace.
- **No versioned engine release.** The current six active specs describe the engine at its current self-development state. There is no concept of "engine v1.0 — release A," "engine v1.1 — release B," such that an application could pin to a specific engine version.
- **No documentation that treats Selvedge as an engine name rather than a methodology name.** `identity.md` treats "Selvedge" as "a reference handle" for the methodology; the engine/application distinction does not appear.

### 3.3 — Related framings (surveyed, not imported silently)

Framings from other traditions that address the engine-vs-development distinction, surveyed as alternatives:

- **Specification vs. reference implementation.** Common in standards work (ISO, IETF, W3C). A specification describes a system; a reference implementation demonstrates the specification. Under this framing, a methodology would be a specification and the engine would be a reference implementation. Fit with current workspace: partial — the workspace contains specifications and treats them as normative; there is no reference-implementation-vs-specification distinction currently.
- **Interpreter vs. interpreted program.** A self-hosting interpreter (e.g., a Lisp compiler written in Lisp) has an engine (the interpreter implementation) and programs it runs (which may include a new version of itself). The distinction between the running-interpreter and the program-being-run is structural. Fit: close to what the operator proposes — every session has so far been a program the engine runs on itself; external applications would be programs the engine runs on non-self content.
- **Build system vs. built artefact.** A build system (Make, Bazel) has rules and executes them over inputs to produce outputs. The rules are reusable across many builds. Fit: close — if the engine is the rules, any application is a build. The self-development sessions are builds where the target is the engine itself.
- **Meta-circular evaluator.** The strong form of self-hosting in Lisp literature. The evaluator defines its own semantics. Fit: tangentially related — Selvedge's self-hosting is specification-level, not implementation-level in the strict sense.
- **Framework vs. application.** In software (Rails, React), a framework defines a scaffold and hooks; applications fill in the hooks. Fit: partial — the "engine" would be the framework; applications would be specific instances.
- **Method vs. methodology vs. methodological framework.** In research-methods terminology, a *method* is a specific procedure; a *methodology* is a justified philosophy of methods; a *methodological framework* is an operationalisation. Under this tradition, the current workspace has been developing a methodological framework, not a methodology in the strict sense. The operator's "engine" maps to "methodological framework operationalised as executable."
- **Language vs. specification vs. implementation** (programming languages). Python-the-language, the CPython reference implementation, and PyPy/Jython alternative implementations are three different objects. Fit: Selvedge currently conflates all three.

**Surveyed conclusion:** the engine/application distinction has close analogues in several traditions. None of them quite fit Selvedge exactly (because Selvedge's engine is text-based specifications executed by a general-purpose LLM, not code executed by a computer), but the closest fit is the **interpreter vs. interpreted program** framing: the engine is a set of specs + a prompt that instructs an LLM to act on them; an "application" is running that engine against a specific problem context.

### 3.4 — Is the reframing accurate to what has been built?

**Partially. The reframing names a real distinction and clarifies structural ambiguity; but it does not exactly match the workspace's current shape.**

- **Accurate part:** the six active specifications + `tools/validate.sh` + PROMPT.md plus the discipline described (multi-agent, provenance-preserved, etc.) do constitute a concrete implementation — an engine in the operator's sense. Calling this "the methodology" conflates implementation with abstract approach.
- **Accurate part:** every session 001–015 has been a self-development application of this engine. The "two applications" count (008 and 010) is misleading: those were external-artefact-producing sessions within self-development, not separate applications in a separate workspace.
- **Partial-fit part:** calling the workspace "at least two applications" understates; it is fifteen applications of the engine, all of them self-development, plus two external-artefact-producing self-development sessions.
- **Partial-fit part:** PROMPT.md is not yet separable — it bundles engine-invocation (Read, Assess, Convene…) with self-development framing ("This workspace is building a design methodology…"). The "distinct execution prompt" consequence the operator names would require refactoring PROMPT.md into a loader + a development-specific context.

### 3.5 — What the reframing does NOT imply (survey of incorrect readings)

Guarding against sloppy absorption:

- Does NOT imply Selvedge's name changes. "Selvedge" names the thing. Whether that thing is called a methodology or an engine, the name still points at it.
- Does NOT imply the nine-activity kernel changes. The kernel describes the engine's execution semantics; that semantics is invariant under the reframing.
- Does NOT imply any existing external artefact is retroactively reclassified. `applications/008-morning-unfurl/` and `applications/010-household-decision-protocol/` are outputs produced by engine runs; the engine/application distinction re-describes them but does not delete or move them.
- Does NOT imply the reference-validation mechanism changes. Its Cell 1 / Cell 2 / Cell 3 structure is an engine-level definition; it is runnable under either framing.
- Does NOT imply the methodology (in the abstract-approach sense) is absent from the workspace. It exists as a latent abstraction behind the specifications. What the reframing adds is a clean named distinction so the engine can be referenced independently.

## 4. Hypothesising step — what would a reframing adoption look like?

Three structural hypotheses, each stated so subsequent deliberation can compete them.

### H1. No reframing — retain current framing; record the observation as clarifying prose

Under H1, the current specifications stay as-is. The operator's observation is accepted as a useful lens for a human reader but is not adopted into any specification text or file structure. Reasoning: the distinction is already implicit; making it explicit incurs revision cost without corresponding operational benefit. The first-exercise of reference-validation proceeds per D-072.

**Gains:** minimal revision cost; D-072 precommitment honoured without replanning; existing specifications unchanged; Selvedge's "self-hosting" identity preserved without introducing engine-vs-application vocabulary that the workspace has not yet earned through external use.

**Losses:** the latent ambiguity remains; a new reader wanting to load the engine on a separate problem still has to reconstruct its boundary; PROMPT.md continues to conflate engine-invocation with self-development framing; the workspace's claim to be usable on external problems remains under-evidenced at the artefact level (the two external-artefact-producing sessions were inside self-development, not outside).

**Strongest advocate position (hypothesised):** a Skeptic would argue H1 is the default until the engine has actually been used externally (OI-001 identity.md Reopening condition 1: "external adoption for 3mo"). Inventing vocabulary for uses that haven't happened yet is pre-mature naming; the textile-preservation discipline argues against premature structural commitments.

### H2. Full reframing — adopt engine/application distinction across all specifications

Under H2, the workspace is explicitly reorganised:
- PROMPT.md is split into two files (or refactored): `engine-prompt.md` (application-agnostic engine invocation) and `development-prompt.md` (current self-development driver; loads engine-prompt + adds development-specific framing). Or: single PROMPT.md with two branches selected by application type.
- A new `engine-definition.md` (or similar) manifest names the files that constitute the loadable engine at any version.
- `methodology-kernel.md` is renamed `engine-kernel.md` (or retitled without file rename for continuity).
- `workspace-structure.md` gains a new section distinguishing engine-definition files, development-provenance files, and application-scoped files.
- `identity.md` is updated to say Selvedge names the engine.
- A new section or specification describes how to initialise a fresh application workspace (what files to copy/link from the engine definition; what scaffolding to create for application-specific provenance).

**Gains:** full separation of concerns; engine is loadable; applications become first-class; PROMPT.md's self-development framing is no longer load-bearing for external use; structural ambiguity resolved.

**Losses:** substantial revision cost across 4–6 specifications; risk of over-specifying structure for applications that have not yet occurred (speculative design); kernel rename may trigger unnecessary version-chain work; risk that the new separation re-introduces its own ambiguities (e.g., are development sessions applications of the engine in the same sense external applications are? — the operator's note treats them as such, but this is a design choice, not a given).

**Strongest advocate position (hypothesised):** an Architect would argue H2 is the only way to make the engine honestly loadable. The current conflation is a structural debt that grows more expensive to pay off the longer it remains.

### H3. Partial reframing — name the distinction, defer full restructure

Under H3, the distinction is named at the specification level (e.g., a new `engine-manifest.md` specification that enumerates the engine-definition files without renaming or moving them; a minor update to `identity.md` acknowledging "engine" as an operational synonym; a paragraph in `PROMPT.md` acknowledging the two kinds of application — self-development and external — with pointer to the manifest). PROMPT.md is NOT split. Existing specifications are NOT restructured. The engine's executable definition is pointable-at but the executable continues to be bundled with development.

**Gains:** names the distinction without heavy refactoring; preserves existing specifications and filenames; creates a single new specification that future sessions can build on (including a possible H2 move later if external adoption materialises per identity.md Reopening condition 1); honours the operator's observation without over-committing.

**Losses:** incomplete — the second operator consequence (distinct execution prompts) is not yet addressed; PROMPT.md still bundles engine-invocation with self-development; applications still cannot be run in a fresh workspace without manual surgery on PROMPT.md.

**Strongest advocate position (hypothesised):** an Operationalist would argue H3 is the right step-size: name the distinction, ship the manifest, let the first actual external application (if and when it occurs) drive the rest of the restructure.

### Comparison of hypotheses

| Dimension | H1 (no reframing) | H2 (full reframing) | H3 (partial reframing) |
|---|---|---|---|
| Revision cost | low | high | medium |
| Names the ambiguity | no | yes | yes |
| Makes engine loadable | no | yes | partially |
| Splits PROMPT.md | no | yes | no |
| Risk of speculative over-design | low | high | medium |
| Preserves D-072 precommitment | yes | possibly — Cell 1 framing may need review | yes |
| Triggers kernel revision | no | likely yes | unlikely |
| Requires D-023 non-Claude | if adopted yes (kernel revision) | yes | likely yes (touches PROMPT.md at minimum) |
| Identity.md update | no | yes | minor |

## 5. Interaction with the D-072 precommitment

Session 015 D-072 precommitted Session 016 to Option A (Cell 1 of reference-validation) per explicit user ratification. The operator input does not revoke this precommitment but does invite agenda re-examination.

### 5.1 — Does the reframing change Cell 1's framing?

Cell 1 of reference-validation is the sourcing + sealing of a case pack for an engine test. Under the reframing:
- **H1:** Cell 1 unchanged. The Case Steward is a role within the engine's self-development application.
- **H2:** Cell 1's framing may be reconsidered. The reference-validation mechanism is an engine-level capability for validating engine outputs against documented references; under H2, this test runs as an "application of the engine" (reference-case as application context). But the test is still executed within the self-development workspace (not in a fresh application workspace), so the reframing is more descriptive than operational for Cell 1.
- **H3:** Cell 1 unchanged, but the engine-manifest can record the engine version under test; if the manifest is produced first, Cell 1 can tag its artefacts with `engine-version: v1` or similar.

**Implication:** Cell 1 execution is largely reframing-independent. The core Cell 1 work (sourcing candidates, running C3 saturation gates, L1 contamination canaries, sealing the case pack) is engine-kernel-level activity that proceeds the same way under H1, H2, or H3.

### 5.2 — Does the reframing change D-072's disposition?

Two paths preserve D-072's substance:

- **Path A: Execute D-072 (Cell 1) this session; open OI-017 for reframing deliberation in a subsequent session.** Honours precommitment; generates first-exercise data that is informative but not decisive for reframing deliberation.
- **Path B: Defer D-072 (Cell 1) to a subsequent session; use this session to record the operator input and open OI-017.** Re-disposes D-072 explicitly; does not violate continuity because the disposition is recorded.

Both paths preserve the precommitment in the sense of not abandoning it silently. The difference is session-budget allocation: Path A spends this session executing Cell 1 plus opening OI-017; Path B spends this session only on the operator-input assessment plus OI-017 opening.

### 5.3 — Session budget reasoning

Cell 1 execution requires (per `reference-validation.md` §1 and §3):
- Sourcing 3–5 candidate reference cases with C1–C8 evaluation.
- Running C3 saturation gate: two constraints-only produce tests per candidate (independent Claude + non-Claude).
- Running L1 contamination canary: thin prompts to ≥2 model families per candidate.
- Tranche-partitioning the surviving candidate with author-documented problem-shape-change evidence.
- User ratification halt for single-candidate selection.
- Sealing the case pack: tranche-0 brief, emergent-constraint schedule, reference envelope, contamination-audit plan, anti-drift witness commit hash.
- `brief-gatekeeper.md` at exercise-provenance root.

This is substantial work even on its own. Session 015 D-072 explicitly deferred exactly this work because "Cell 1 case sourcing includes C3 saturation-gate runs (two constraints-only produce tests per candidate) and L1 contamination-canary runs (thin prompts to ≥2 model families per candidate), which have non-trivial cost per candidate and are better executed in a dedicated session."

Adding the operator-input assessment to Cell 1 execution in the same session compounds scope beyond what Session 015 explicitly budgeted Cell 1 for. The assessment alone is session-appropriate; assessment plus Cell 1 risks a rushed Cell 1 or a superficial assessment.

## 6. Agenda options considered

### Option α — Assessment-only; defer Cell 1; open OI-017

Scope: this session completes the operator-input assessment (in progress); opens OI-017 with activation trigger and preferred starting point; records D-073 with `triggers_met: [none]` per single-perspective planning-record precedent (D-072). Cell 1 is deferred to Session 017 or a later session.

**Gains:** bounded scope; clean session product; honours the operator's explicit "resolution not required this session" stance; gives Session 017 (or later) room to deliberate OI-017 with full multi-agent discipline if the user chooses; does not compound scope beyond Session 015's precedent.

**Losses:** second consecutive preparation-only session (Session 015 was also preparation). Pattern-risk: OI-009 ceremony-without-advance. *Mitigation: this session is preparation responding to a fresh operator input — not self-generated ceremony. G/O/K/S criterion-package evaluation in §7 below confirms it satisfies at least (G), (O), (K), (S).*

### Option β — Execute Cell 1 per D-072; open OI-017 as carried-forward work

Scope: this session executes Cell 1 of reference-validation (candidate sourcing, C3/L1 tests, sealing) per D-072, *and* records operator input, *and* opens OI-017. Assessment of the reframing becomes a brief annotation rather than a substantive §3–§5 treatment.

**Gains:** honours D-072 precommitment; generates first-exercise data; does not defer twice in a row.

**Losses:** compounds scope substantially; risks rushed Cell 1 with weaker C3/L1 test discipline; reduces the assessment to a surface note that does not meet the PROMPT.md "explicit surveying or hypothesising step" requirement for the operator input. The latter is structurally more concerning: the operator input is a first-class reframing proposal, and absorbing it without a proper hypothesising step would replicate exactly the laundering failure mode OI-015 names.

### Option γ — Full deliberation on OI-017 this session

Scope: this session convenes a multi-agent deliberation (with non-Claude participation per D-023 requirements, since adoption of H2 or H3 would revise PROMPT.md and plausibly kernel). Three or four perspectives deliberate H1 / H2 / H3 and competing alternatives. A decision is made.

**Gains:** fastest path to resolution; engages the reframing under full discipline; avoids opening an OI only to close it later.

**Losses:** explicitly overrides the operator's "resolution not required this session" stance; high-stakes deliberation in the same session as the input's receipt without time for surveying-step content to settle; risk of reaching for a premature decision on a question the operator framed as exploratory.

### Option δ — Null-response

Scope: proceed with Cell 1 per D-072 as if no operator input had been received; record the operator input but take no other action.

**Gains:** none beyond pure D-072-honouring.

**Losses:** violates the PROMPT.md anti-silent-import rule ("If an insight arrived through reading something unrelated, a conversation with a human, or your own pretraining, introduce it as an input to an explicit surveying or hypothesising step rather than committing it directly" — the operator input, treated this way, would be silently deferred rather than properly surfaced). **Rejected on specification-compliance grounds.**

## 7. OI-009 G/O/K/S evaluation (if Option α is selected)

Per OI-009's Session 007 D-048.2 criterion-package, self-work is load-bearing iff it satisfies at least one of (G), (O), (K), (S). Option α is preparation-only self-work; the evaluation is required.

- **(G) Translation-to-external-frame.** Satisfied. The operator input is a proposal about how the engine can be loaded by external users. Responding to it is engine-external-framing work by construction.
- **(O) Narrows-external-action-decision-space.** Satisfied. Opening OI-017 specifies a concrete decision surface (H1/H2/H3 + alternatives) for the next deliberation; the downstream external action "load the engine on a new application" becomes explicit rather than implicit.
- **(K) External-reader visibility.** Satisfied. The ambiguity the reframing names is visible to an external reader who reads PROMPT.md and identity.md today and tries to figure out whether "the methodology" is a pattern or a system.
- **(S) Specific-obstacle resolution.** Satisfied. The operator has named a specific obstacle (engine not distinguishable from development provenance; no application-execution-prompt). Opening OI-017 is the next step toward resolving that obstacle.

**OI-009 evaluation: Option α passes all four criteria.** Not ritual-tracking; load-bearing self-work.

## 8. Recommendation

**Option α — assessment-only; defer Cell 1; open OI-017.**

- Rationale: the operator input is a first-class structural proposal that requires the PROMPT.md-mandated explicit surveying/hypothesising step; this session provides that step but does not (and should not, per operator's stance) force a resolution; Cell 1 is deferred on session-budget grounds and can be executed in Session 017+ under whichever framing is selected (the reference-validation mechanism is reframing-agnostic at the Cell 1 level).
- The session closes with OI-017 opened and D-072's disposition explicitly re-examined; Cell 1 execution is the default next-session work unless the user elects to deliberate OI-017 first.

## 9. Halt for user ratification

Session 016 halts here for user ratification of:

- **Assessment shape.** Whether §3's surveying and §4's hypothesising adequately introduce the operator input per the PROMPT.md anti-silent-import rule.
- **Agenda disposition.** Option α (recommended) vs Option β vs Option γ.
- **D-072 re-disposition.** If Option α is ratified: should Session 017 execute Cell 1 (per D-072 standing precommitment), or deliberate OI-017 first?
- **OI-017 scope and activation trigger.** Whether the OI-017 draft in `open-issues.md` (forthcoming in D-073) is scoped correctly.
- **Tooling input.** The operator authorised `uv tool` installations where the engine determines a tool is needed. This session identifies no tool need yet (the assessment is specification-level work). If OI-017 deliberation proceeds, `gemini` and `codex` CLIs are already available per CLAUDE.md for non-Claude participation; no additional tool installation is anticipated at this stage.

Pre-commitment: if Option α is ratified and Session 017 is elected to proceed with Cell 1 per D-072, the six OI-016 re-opening triggers remain in force; OI-017 remains open but is not a blocker for Cell 1. If Option α is ratified and Session 017 is elected to deliberate OI-017 first, Cell 1 execution is deferred until after that deliberation; D-072 remains in effect but its execution timing is pushed out.

Session 016 will not proceed to Cell 1 case sourcing, to a multi-agent OI-017 deliberation, or to any specification revision before this ratification.
