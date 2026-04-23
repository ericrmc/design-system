---
session: 036
title: Perspective — Synthesiser (Path PD)
date: 2026-04-23
status: complete
perspective: Synthesiser
committed_at: 2026-04-23T00:00:00Z
---

## Q1. Dispatcher revision

The operator-enumerated directions 1–5 are not actually competing alternatives along a single axis — they trade off along at least three distinct axes that a minimal-revision or preservation-first lens tends to flatten. Making the axes explicit is the integrative move.

**Axis A — Locus of signal.** Direction 1 (`MODE.md`) places the signal in a *dedicated* file. Direction 2 (structural signature across `applications/NNN-<slug>/brief.md` plus self-dev negative signal) places the signal in the *workspace shape*. Direction 3 (frontmatter in `SESSION-LOG.md`) places it *inside an already-required file*. Direction 4 (separate prompt files) places it in *which prompt the operator invokes*. Direction 5 (Session-001 init discipline plus fallback-narrowing) places it in *process* rather than artefact.

**Axis B — Visibility and audit cost.** Directions 1 and 3 are human-readable at a glance. Direction 2 is invisible-to-read in the sense that no single file declares the mode — the dispatcher must reason about multi-file presence/absence. Direction 4 is maximally visible (operator selected it by invocation). Direction 5 is invisible during steady-state because the discipline happens once at workspace birth.

**Axis C — Failure mode when the invariant breaks.** Direction 1 fails closed if `MODE.md` is deleted or forgotten at init — dispatcher cannot route. Direction 2 fails ambiguously if a workspace is mid-migration (e.g., first external-application session before `applications/001-<slug>/brief.md` is written, or a self-dev workspace that happens to also carry an `applications/` directory for sample briefs). Direction 3 requires `SESSION-LOG.md` to exist with parseable frontmatter from Session 001, shifting a must-exist invariant onto an already-load-bearing artefact. Direction 4 fragments the "single entry point" abstraction that `PROMPT.md` currently provides. Direction 5 leaves steady-state unchanged but concentrates all risk at workspace birth.

The Reviser's likely minimal-revision preference narrows toward direction 5 (smallest delta) or direction 2 (no new artefact). The Skeptic-preserver's likely preference narrows toward leaving the dispatcher alone and narrowing the fallback, or toward direction 3 if preservation-of-existing-files is the preservation criterion. Both lenses can miss that the *current* fallback behaviour ("halt and seek clarification from the operator") is not a bug — it is a legitimate engine behaviour that the operator is free to declare steady-state for external-problem workspaces. Every-session halt is cheap in the single-operator single-session regime this engine currently inhabits; it becomes costly only under automation pressure that does not yet exist.

**Integrative proposal for Q1.** Hybrid direction 6, composed as follows: adopt direction 2 (structural signature) as the *primary* dispatch test, with direction 5 (Session-001 init discipline) as the *generative* discipline that guarantees the signature holds from Session 001, and direction 1 (`MODE.md`) as an *optional override* that resolves ambiguity when present. Concretely, the revised `PROMPT.md §Dispatch` would (a) check for `MODE.md` first and honour it if present; (b) otherwise test structural signature — presence of `applications/NNN-<slug>/brief.md` with NNN ≥ 001 routes external-problem, presence of `provenance/` with session directories 002+ and `SESSION-LOG.md` with prior sessions routes self-development; (c) fall back to operator clarification only on genuine ambiguity (neither signature matches, or both match). This preserves the single-entry-point abstraction, avoids a new mandatory file, handles steady-state for Sessions 002+, and keeps an escape hatch for migration/edge cases. Direction 4 is rejected as over-fragmenting; direction 3 is rejected as loading dispatch semantics onto a file that already carries session-state semantics.

**Dissent preserved.** A minimal-revision reading that chooses direction 5 alone (narrow the fallback, require init discipline, dispatcher unchanged) is defensible and should be recorded as a first-class minority if the hybrid is adopted — it avoids any dispatcher-spec change and treats §2a as a process problem, not an artefact problem. A "no revision warranted" reading is also defensible on the grounds that the operator can simply answer the halt-and-clarify prompt each session; this should also be preserved.

## Q2. Feedback pathway

The five sub-questions (Location, Shape, Intake, Retention, Discipline) interact with existing engine machinery in ways that Reviser (minimal-revision) or Skeptic-preserver (don't touch what isn't broken) lenses may under-weight.

- **Location.** Candidates: a dedicated `applications/NNN-<slug>/feedback.md`; a section inside each application's close artefact; an OI entry in the source-workspace `open-issues/` filed by the operator on return. The first is local to the application and travels with it; the third is closest to how OI-002/OI-004 already function.
- **Shape.** Either free-form observations or a structured template (observed-friction, observed-gap, proposed-engine-change, severity). Structured shape couples to OI-002 substantive-vs-minor classification.
- **Intake.** The critical coupling. Feedback re-entering the source workspace must be classifiable: does it open an OI, fire a watchpoint, or warrant immediate engine revision? Natural home: source-workspace `open-issues/` with a convention that feedback-sourced OIs are tagged.
- **Retention.** Feedback should persist in the external application's provenance (it is durable reasoning about that run) *and* in the source workspace when it triggers action (OI or watchpoint). Dual retention avoids the operator-memory dependency called out in §2b.
- **Discipline.** Return is not mandatory — most external runs may produce no engine-level feedback. Sessions 008/010 external-artefact precedent is sparse data: no feedback emerged. Two readings — (i) signal that feedback is genuinely rare; (ii) absence because no pathway existed, so operator didn't know what to return. Under reading (ii) the current sparseness is not evidence against a pathway; it is evidence for one. Under reading (i) the pathway is over-engineering for a rare event. This is a genuine empirical ambiguity that should be preserved rather than resolved prematurely.

**Integrative proposal for Q2.** Minimum viable pathway: (a) add a `feedback.md` section to the external-application close convention (location + shape), optional and empty-by-default; (b) specify that non-empty feedback at application close *may* be lifted into the source workspace as an OI by the operator, following existing OI-opening discipline (intake + retention + discipline); (c) do not mandate return. This is lifecycle-light: it names the pathway without forcing traffic through it. Watchpoint interaction: if feedback lifts to an OI, that OI participates in the existing OI-002 classification and §9-trigger machinery unchanged. First-class minority preservation pattern is unaffected — feedback-sourced reasoning that dissents from adopted engine direction preserves exactly as in-workspace dissent does.

**Dissent preserved.** A Skeptic-preserver reading that treats Sessions 008/010 sparse data as signal (reading i) and defers feedback-pathway formalisation until a second external application actually produces returnable observations is defensible and should be recorded. Building pathway ahead of demonstrated demand is a form of speculative infrastructure this engine has historically avoided.

## Q3. Q1–Q2 relationship

This is the central integrative question. The §2c framing ("both engine-application boundary") is correct but under-specifies *which* boundary: Q1 is a **load-time routing boundary** (which prompt branch runs given a workspace state), Q2 is a **post-completion return boundary** (how observations flow back from application to engine). They share a conceptual frame (engine-application interface) but operate at different lifecycle phases and touch different files.

A single-mechanism solution would be elegant but strained. For instance, using `MODE.md` as both dispatch marker *and* feedback carrier conflates state-declaration with observation-content and creates a file that must be read at dispatch time but appended to at close time — awkward concurrency semantics for a markdown artefact.

**Integrative proposal for Q3.** Treat Q1 and Q2 as distinct mechanisms with clean decomposition, but solve them in the *same session* so the §2c shared frame is honoured at the specification level. The decomposition: Q1 touches `PROMPT.md §Dispatch` and possibly a new structural convention (paths under `applications/`); Q2 touches application-close convention and possibly a new OI-opening convention. These edits do not collide. Cross-referencing between the two in the spec (e.g., the engine-manifest §6 external-application section naming both load-time dispatch and close-time feedback as components of the engine-application lifecycle) captures the shared frame without forcing a shared mechanism.

## Q4. Substantive revision scope

Under the integrative proposal, revised files are: `PROMPT.md` (dispatch logic), `specifications/engine-manifest.md` (§6 external-application description, add close-time feedback convention), and potentially `specifications/workspace-structure.md` (structural-signature definition for dispatch). Volume: low — tens of lines per file, not structural rewrites. This is substantive per OI-002 heuristic (spec semantics change, not formatting), so engine-v bumps to v7. First-class minorities: the preserved dissents from Q1 and Q2 above. No interaction with OI-004 closure procedure since this is a new substantive change, not a closure.

## Q5. First-class minority preservation

At minimum: the Q1 minimal-revision-direction-5-only dissent; the Q1 "no revision warranted" dissent; the Q2 defer-feedback-pathway dissent (sparse-data-as-signal reading). These preserve symmetrically across the minimal-revision / preservation axis and across the dispatcher / feedback axis, which matters for future retrospective evaluation of whether the hybrid was the right call.

## Q6. WX-35-1 disposition

Three-way trade-off: (a) retroactive backfill risks anti-laundering violation and rewrites session history in a way that itself becomes a laundering pattern if repeated; (b) new convention (state-history edits must be verified via git-log before close-narrative assertion) is preventative but does not address the 13-session accumulated drift; (c) incremental (fix going forward, accept past drift as observed) preserves honesty about the gap.

**Integrative proposal for Q6.** Hybrid of (b) and (c): adopt a new convention preventing recurrence (Session-036 close-discipline extension: git-log verification of any claimed file-edit before commit), accept past drift without backfill (honouring anti-laundering), and open a watchpoint extension under WX-35-1 or a successor to verify the new convention holds for a defined evaluation window (e.g., 3 sessions). This matches the engine's existing pattern of preventative-convention-plus-verification-window (WX-34-1 precedent). Backfill-as-such is rejected on anti-laundering grounds; pure-incremental is rejected because it leaves the 13-session pattern unaddressed at the convention level.

**Dissent preserved.** A Reviser-aligned reading that prefers pure (c) — incremental only, no new convention — on minimal-revision grounds is defensible and should be recorded.

## §5 External input flag

No pretrained ideas imported. All reasoning derives from the brief's enumeration of existing engine artefacts and conventions.
