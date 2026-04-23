---
session: 043
title: Decisions — D-129 minor forward convention on non-Path-A alternative surfacing (3-session verification window S044-S046); D-130 open OI-019 path-selection work-channel and warrant-surface diversity; D-131 preserve Path-Selection Defender as §5.12 first-class minority (#29); D-132 housekeeping
date: 2026-04-24
status: decisions-complete
---

# Session 043 Decisions

Four decisions ratifying the §3b synthesis of `01-deliberation.md`.

## D-129: Adopt minor forward convention — default-agent session-open assessments MUST surface at least one non-Path-A alternative considered

**Triggers met:** [d008_2_convention_forward_discipline]

### Decision text

Starting Session 044, the default-agent session-open assessment MUST include a subsection surfacing at least one considered-and-rejected non-Path-A shape with a brief one-sentence rationale. The required shape is:

> **§Xn: Non-Path-A alternatives considered** (where Xn is a stable subsection identifier in the assessment's §Path-recommendation section)
>
> Minimum content: one bullet of the form `- Path <label>: <one-sentence what it would do>. Rejected because: <one-sentence why not this session>.`
>
> Additional bullets permitted and encouraged when operationally warranted.

This convention is **standing** (not windowed) but is **minor** per OI-002 (convention adopted in session decision record; no specification file amended this session; analog of WX-35-1 forward convention adopted at Session 036 before Session 039 vindication into standing discipline).

### Why minor

No specification file is amended this session. The convention lives in session decision records until such time as a formal spec-level codification is warranted. Precedent: WX-35-1 forward convention was adopted in D-116 at Session 036 as a convention; Session 039 vindicated the 3-session verification window; spec-level codification was never separately enacted — the convention graduated to standing discipline. The same pattern applies here.

### 3-session verification window

Sessions 044 / 045 / 046 will each exercise the convention. Evaluation at Session 046 close:

- **Vindication conditions**: (i) at least one of S044/S045/S046 surfaces an alternative that is subsequently adopted (i.e., the session executes a path other than Path A); OR (ii) all three sessions surface substantive alternatives with non-vacuous evidence even when Path A is ratified (i.e., the convention adds information to the reasoning trail).
- **Non-vindication conditions**: (i) all three sessions surface vacuous template alternatives ("no alternative warranted") — fires §5.12 minority reopen warrant (a); OR (ii) the convention is used to manufacture deliberative work where no warrant existed — fires §5.12 minority reopen warrant (a) and anti-laundering review.

If vindicated, the convention continues as standing discipline (possible spec codification at a future engine-v bump, via the standard cascade pattern).

If non-vindicated, the convention is withdrawn and the Path-Selection Defender position adopted as prevailing.

### Rejected alternatives

1. **Make it MUST at spec level in this session** (amend `prompts/development.md` or `methodology-kernel.md` §Assess or `multi-agent-deliberation.md`). Rejected: anti-laundering — retrofitting spec content in the same session that surfaced the motivating pattern is exactly what MAD v4 warns against. No 3-of-5 convergence exists on the exact shape (P1 says ≥2; P5 says ≥1; P3 says "Path-A justification section"). Spec amendment requires tighter convergence than was reached.

2. **Make it SHOULD (not MUST) at convention level.** Rejected: wishy-washy middle ground produces nothing operational. If adopted, it becomes a practice that is praised in sessions that use it and forgotten in sessions that don't — the worst of both worlds. MUST-at-convention-level is honest: we are asserting a discipline; if it degrades, the §5.12 minority tests will reveal it.

3. **Require ≥2 alternatives per P1's preferred shape.** Rejected: P5 said ≥1, P3 said "plural" but did not specify. 3-of-5 floor is ≥1; P1's ≥2 deferred to OI-019 as a verification-window question (does ≥1 prove sufficient or does drift toward template-filling appear?).

4. **Adopt P3's "Path-A justification section" with three one-line items** (warrant check, alternatives considered, metrics that would have triggered). Rejected: over-specifies in first adoption; anti-laundering concern about forcing a template surface. The three-item schema may be revisited at S046 evaluation if the minimal convention proves insufficient.

5. **Apply only when Path A is recommended** (not to other path recommendations). Rejected as narrow: when a substantive path is recommended (e.g., Path L, Path OI-N), its justification already lives in the assessment body. The minimal shape applies in any session where the default-agent recommendation could have been different; operationally this is almost always Path-A-recommendation sessions, but the convention is agnostic.

6. **Defer all convention adoption to OI-019 deliberation outcome.** Rejected: the Q4 convergence is the tightest in this deliberation (4-of-5 with non-Claude on majority side); leaving it unratified until OI-019 resolves would be under-responding to convergence. The verification-window mechanism allows this convention to be reversed if OI-019 concludes it was a mistake.

## D-130: Open OI-019 — Path-selection work-channel and warrant-surface diversity

**Triggers met:** [d009_1]

### Decision text

Open new open issue **OI-019: Path-selection work-channel and warrant-surface diversity** at `open-issues/OI-019.md`. State: Open. Opened Session 043.

Contents per `open-issues/OI-019.md` file (full text in that file, not duplicated here):

- **Problem statement**: The engine's path-selection mechanism is warrant-gated and sparse-by-design; 4-of-5 perspectives at Session 043 (including non-Claude) identify this as producing asymmetric behavior (dense against engine-internal trajectories; sparse against operator-frame observations) and absent work-shapes (refactoring; investigative; diagnostic/machinery-exercise; baseline-shift). No 3-of-5 convergence on the exact mechanism to address this was reached in S043.

- **Unresolved sub-questions** (from S043 deliberation):
  (a) Is "work-channel diversity" (P1) or "warrant-surface closure against operator-frame observations" (P4) the better reframe? Both are operationally coherent; neither falsifies the other.
  (b) Should preserved-minority activation warrants themselves have expiration windows (P3)?
  (c) Should the engine have state-decay or pressure triggers on closable/articulated OI state after X sessions (P5)?
  (d) Should the warrant surface be enlarged at spec level with a new "operator-frame observation" input class (P4)?
  (e) Should the default-agent convention (D-129) be codified at spec level with a specific shape (≥1 vs ≥2 vs Path-A-justification-section)?
  (f) What extended-baseline visibility mechanism, if any, is warranted — periodic (P3, P5) vs distribution-property-triggered (P4) vs narrow-targeted (P2 concession)?

- **Closure criteria** (provisional; may be refined during OI lifetime):
  - Operational evidence from the engine's continued running that one of the proposed mechanisms is load-bearing (i.e., absence of it demonstrably caused a surface-missed observation or drift).
  - Cross-family deliberation with ≥3 perspectives converging on a specific mechanism shape.
  - Anti-laundering adjudication showing the adopted shape is not retrofit to rationalise past Path-A concentration.

- **Seed perspectives**: The five Session 043 perspective files at `provenance/043-session-assessment/01{a,b,c,d,e}-perspective-*.md` are the seed material. Future deliberations should cite them.

- **§5.12 minority linkage**: The Path-Selection Defender position preserves the reasoned alternative that OI-019's resolution is "no change; the machinery works as designed." Any OI-019 deliberation MUST address the §5.12 operational reopen warrants; failure to do so is itself a laundering signal.

- **§5.6 linkage**: This session's Gemini participation is the first operational data point on the vindication side of §5.6 reopen-warrant (ii). Future OI-019 deliberations SHOULD include non-Claude non-GPT participation to avoid re-concentrating the record.

### Why now (not deferred)

An OI is the standard forward mechanism for substantive questions that have deliberation heat but lack convergence on mechanism. Deferring the OI to a later session would lose the convergence data already produced. The OI is a container for the unresolved question, not a decision about it.

### Rejected alternatives

1. **Do nothing this session on the unresolved questions.** Rejected: five perspectives have produced deliberation content that would be lost without an explicit issue pointer. Anti-discontinuity: if the deliberation is not captured in an OI, the next session would have to re-derive it from archive surface, which is exactly the "indefinitely deferrable" pattern §5.3 warned against.

2. **Bundle into existing OI-018** (cadence revisit minority). Rejected: OI-018 is specifically about engine-v bump cadence under §5.4 minority; the path-selection work-channel question is a distinct phenomenon. Conflating would dilute both.

3. **Open one OI per unresolved sub-question.** Rejected: the sub-questions are interlinked (work-channel diversity relates to warrant-surface closure relates to state-decay relates to extended-baseline visibility — they all concern the same mechanism surface). Opening five OIs would fragment what is coherently one problem space.

4. **Frame the OI narrowly around D-129 spec-codification only.** Rejected: the larger reframes (P1 channel diversity; P4 warrant surface; P5 state decay) would be lost. OI-019 captures the full surface.

## D-131: Preserve Path-Selection Defender position as §5.12 first-class minority

**Triggers met:** [d004_3_minority_preservation]

### Decision text

Preserve the Path-Selection Defender position (Perspective 2 of S043) as **§5.12** in this session's provenance (at `01-deliberation.md` §5), advancing the engine-wide first-class minority count from 28 to 29.

This is per the operator's explicit instruction in `00-assessment.md` §2:

> The reasoned conclusion that the current discipline is correct and my framing is wrong — preserve that as a first-class minority if the deliberation lands there.

Full minority text is in `01-deliberation.md` §5, including operational reopen warrants (a/b/c).

**Placement**: In S043 provenance (not in a spec file), following the S041 precedent that preserved §5.6–§5.8 in the OI-004 closure retrospective rather than a spec file. Minority preservation in provenance is a recognised pattern for minorities that do not correspond to a specific spec file's content.

### Rejected alternatives

1. **Do not preserve; treat P2's position as engaged-and-addressed via the §3b decision.** Rejected: operator explicitly requested preservation. This is a load-bearing operator instruction.

2. **Preserve in a spec file** (e.g., add §5.12 to `methodology-kernel.md` or `multi-agent-deliberation.md`). Rejected: no spec file is amended this session; preservation-in-provenance follows S041 precedent and respects anti-laundering (not retrofitting specs in same session that surfaced the pattern).

3. **Preserve with ceremonial reopen warrants only** (e.g., "revisit at Session 052"). Rejected: operator explicitly asked for operational reopen warrants. Ceremonial warrants drift into ritual; operational warrants tie reactivation to observable outcomes.

4. **Preserve but mark as "minority" rather than "first-class minority."** Rejected: the P2 position contains distinctive operational content (pre-registration argument; laundering-surface critique of all four operator seed shapes; operator-surfaced-agenda as the specified import pathway). Distinctive operational content is the definition of first-class per prior minority preservation practice.

## D-132: Housekeeping

**Triggers met:** [none]

### Decision text

At session close, the Case Steward performs the following non-specification housekeeping:

1. **SESSION-LOG.md update**: add Session 043 thin-index row reflecting the Path PSD execution, D-129/D-130/D-131/D-132, engine-v7 preservation window count 6→7 (continues new-longest run), §5.6 literal discharge + spirit forward observation, fifteenth close-rotation steady-state (Session 037 close rotates out; Session 043 close enters), first-class minority count 28→29, active OI count 12→13.

2. **open-issues/index.md update**: add OI-019 row (Open; Session 043 opened); advance active OI count 12→13; note seed perspectives at S043 provenance.

3. **open-issues/OI-019.md authoring**: create the new OI file with content per D-130.

4. **Participants manifest + individual manifests**: author `participants.yaml` + `manifests/work-shape-proposer.manifest.yaml` + `manifests/path-selection-defender.manifest.yaml` + `manifests/long-baseline-auditor.manifest.yaml` + `manifests/outsider.manifest.yaml` + `manifests/non-claude.manifest.yaml` per MAD v4 §16 schema (independent_claim; claude_output_in_training field; participant_organisation; mechanical invocation recording for gemini).

5. **WX observations recorded as forward observations** (not OI-promoting per anti-laundering single-session rule):
   - **WX-43-1** (candidate; not opened): subagent self-commit inconsistency (P1 + P4 committed individually during run; P2/P3/P5 did not). Bundling candidate for future Path-L subagent-instruction-clarification if recurs.
   - **§5.6 literal-vs-spirit observation**: literal discharge at S043 close (reopen-warrant (ii) cannot fire at S047 since non-GPT non-Claude participation now exists); spirit-level question (one data point vs sustained exercise) re-examined at Session 046 close §10.4-M1/M2/M5 tenth-of-10 evaluation.

6. **WX continuing forward observations**:
   - WX-24-1 MAD stable (continues no-growth baseline against post-D-126 6,637 threshold; S043 is second-of-N post-S042 reset)
   - WX-28-1 close-rotation zero-retention-exceptions (fifteenth rotation continues vindicated pattern)
   - WX-34-1 standing discipline (S043 row substantive-detail justified by substantive content session; precedent S041)
   - WX-35-1 standing discipline applied at substantive-session close (file-edit claim verification via git log)
   - WX-22-1, WX-24-2, WX-24-3, WX-27-1, WX-33-2 unchanged

7. **Engine-v7 preservation window count advances 6→7**, continuing new-longest run established at S042. First substantive-content session at preservation depth ≥7 since engine-v4 (which never reached 7; max was 5).

8. **§9 trigger counters**: trigger 5 at 2-of-3 unchanged (no reference-validation Cell 1 exercise this session); trigger 7 re-fire counter at 0-of-3 unchanged (same reason).

9. **§5.4 cadence minority** does not re-escalate (non-bump non-substantive-spec-change session; §5.4 concerns bump frequency, which is not exercised here).

10. **OI-004 state** unchanged (Closed). Per D-126 forward clause d023_4 narrowed semantics, d023_4 does not fire at S043.

11. **Validator run at close**: expected PASS on all provenance checks (new 043-session-assessment folder + SESSION-LOG row + new OI file + OI index update). Two designed soft-warns expected to persist (MAD 6,637; reference-validation.md v3 7,160). New potential soft-warn candidate: this session's accumulated provenance (6 perspective files + deliberation + decisions + close + manifests) may approach per-file budgets for any individual file — monitored but not expected to breach.

### Rejected alternatives

1. **Skip participants.yaml + manifests.** Rejected: MAD v4 §16 requires them for substantive cross-family deliberation. Checks 16/17/19 test them. Failing to author would be a procedural defect that §10.4-M5 (records-count feedback minority) specifically watches against.

2. **Open WX-43-1 as formal watchpoint now.** Rejected: single-session observation; anti-laundering bar for OI promotion requires recurrence. Forward-observation status is the correct disposition.

3. **Flag §5.6 literal-vs-spirit disposition as an OI.** Rejected: the disposition is recorded as a forward observation; it does not need a dedicated OI. Re-examination at S046 close is the correct disposition (analog of §10.4-M evaluation pattern).

4. **Bump engine-v7 → engine-v8 at this session close** (on grounds this is a substantive deliberation with three decision records touching engine mechanics). Rejected: no specification file is amended this session. Engine-v bumps per `engine-manifest.md` §5 require spec changes, not convention changes. Preservation window advances legitimately.

5. **Defer D-132 housekeeping to Session 044 open.** Rejected: housekeeping at close is the standard pattern (S027, S029, S036, S041 all executed housekeeping at close of substantive sessions). Deferring would leave S043 in incoherent state with decisions adopted but index/log un-updated.

6. **Bundle D-131 §5.12 minority preservation into D-130 OI-019 opening** (treat §5.12 as an OI attachment rather than engine-wide minority). Rejected: minorities and OIs are distinct constructs with distinct lifecycles. §5.12 is an engine-wide first-class minority (counted in aggregate 29); OI-019 is an open issue (counted in active-OI 13). The two mechanisms handle different kinds of preservation. Conflation would blur both.
