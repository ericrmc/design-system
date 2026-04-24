---
feedback_id: EF-001-read-contract-budget-scaling-for-domain-artefacts
source_workspace_id: selvedge-disaster-response
source_session: 001
created_at: 2026-04-24
last_updated: 2026-04-24
reported_by: operator
target: engine
target_files:
  - specifications/read-contract.md
  - prompts/application.md
  - specifications/workspace-structure.md
severity: friction
status: inbox
operator_directed_resolution: exclude applications/ from per-file budget; aggregate budget unchanged; chunked-read-on-demand via existing Read-tool offset/limit mechanism; optional manifest/index as navigation pointer; not open to deliberation
---

# EF-001 — Read-contract per-file budget (6K soft / 8K hard) does not scale to domain artefacts; operator-directed resolution: exclude applications/ from per-file budget

## Observation

During execution of `selvedge-disaster-response` Session 001, the external Case Steward made the following statement (quoted verbatim by operator):

> Budget shape: the four v1 artefacts each need to stay under the 6K-word soft / 8K-word hard default-read ceiling. Perspective raw outputs will be archive-packed at close if they exceed 6K

The operator then raised the meta-question: **"How will this default-read limit scale with large complex artefacts?"**

The external session is applying the `read-contract.md` v4 §2 per-file budget (6,000 soft / 8,000 hard words) to its domain artefacts (`system-model.md`, `assumption-ledger.md`, `response-plan.md`, `risk-register.md`). For the Laurel Delta / Nivaro compound coastal-disaster scenario affecting ~200,000 population across three settlements with layered infrastructure dependencies, vulnerability profiles, and a 10-day response horizon, each of these artefacts is plausibly a 10,000-30,000-word document in realistic domain practice — well above the 8,000-word hard ceiling.

The session's compliance path is either (a) heavy content compression (domain-fidelity distortion), (b) splitting each artefact across multiple under-budget files, or (c) archive-packing primary working artefacts (the pattern was designed for archive-surface content, not primary artefacts). All three have costs.

This friction arises **at the very first real exercise** of the external-application pathway. Prior in-workspace "application" exercises (Morning Unfurl S008 at ~500 words; Household Decision Protocol S010/S013 at ~1,500 words) were small enough that the budget never bound. `selvedge-disaster-response` is the first test at realistic domain complexity.

## Why It Matters

The `read-contract.md` v4 §2 per-file budget was **calibrated against self-development methodology-content files**, not domain-artefact files. The S023 D-086 recalibration from v1's 15K/10K to v2's 8K/6K was motivated by: (i) empirical 3.0× tokens-per-word ratio against the 25K-token single-Read ceiling, (ii) measurement on `SESSION-LOG.md` (10,405 words) and `open-issues.md` (9,783 words) — both methodology-content files. The rationale does not reference domain-artefact scaling.

`read-contract.md` §1 enumerates the default-read surface: items 0-9 name engine-definition files, workspace-identity marker, `SESSION-LOG.md`, `open-issues/index.md`, per-close-retention-window close files, current session provenance, and conditional `engine-feedback/INDEX.md`. **Items 0-9 do NOT name `applications/`.** By §3 ("anything preserved in the workspace but not on the §1 enumeration") application-scope artefacts are archive-surface by default.

But `prompts/application.md` §Read instructs external sessions to read `applications/` as part of domain scope:

> Domain reading — this application's problem statement, constraints, stakeholders, success condition, initial state (the slots above), plus any domain materials introduced into the session.

This is the **latent spec contradiction** P3 Outsider flagged at S047 as their unique finding (recorded as deferred candidate EF-047-(iv) per S047 D-150). The external Session 001 has encountered this contradiction operationally: it is reading `applications/` files (following `prompts/application.md`) AND applying the `read-contract.md` §2 per-file budget to them (treating them as default-read because they are being read at session-open).

Three concrete scaling problems:

1. **Single-artefact bound**. A realistic 10-day response plan for 200K population easily exceeds 8K words. Splitting produces file-proliferation; compression produces domain distortion. Neither preserves the artefact's utility for its actual purpose.

2. **Cumulative across sessions**. The arc evolves artefacts across 5 sessions (S047 D-147 + arc-plan §3). Even if each individual v1 fits under 8K, v3 or v4 revisions — which accrue branch-points, invalidation annotations, decision-tree complexity, and cross-artefact references — grow naturally. An artefact that fit at S001 may not fit at S004.

3. **Aggregate pressure**. `read-contract.md` §2b aggregate budget (90K soft / 100K hard) applies across all default-read files. In the external workspace, the default-read surface at S003 includes: engine-definition files (~80K per self-dev measurement) + MODE.md + SESSION-LOG + open-issues/index + 2 prior closes + 7+ application artefacts + current session provenance. This can plausibly exceed 100K hard by S003 or S004 — forcing close-rotation AND artefact-restructure simultaneously, potentially mid-deliberation.

## Operator-directed resolution (not open to deliberation)

The operator has directed the resolution path directly, removing this record from the post-arc deliberation candidate set. **Resolution**:

1. **Exclude `applications/` from `read-contract.md` §2 per-file budget enforcement.** The 6K soft / 8K hard per-file ceilings do not apply to files at `applications/NNN-<slug>/` in any workspace.
2. **`read-contract.md` §2b aggregate budget continues to apply.** Total default-read surface remains bounded at 90K soft / 100K hard; large domain artefacts contribute to aggregate and will still force close-rotation or artefact restructure if aggregate approaches ceiling. The per-file relief does not change aggregate pressure.
3. **Chunked-read-on-demand via the existing Read-tool offset/limit mechanism.** When a session needs to read a large artefact, it reads in chunks as needed. No new archive-pack machinery required for application-scope artefacts; the existing Read-tool capability is the chunking mechanism.
4. **Optional manifest or index as navigation pointer.** An external application MAY place a thin `applications/NNN-<slug>/index.md` (or `manifest.yaml`) enumerating its artefacts + sections + chunk hints, to help sessions find content without reading everything. Not mandatory; recommended for applications whose artefacts are large enough that section-level navigation is useful.

This operator directive also **resolves** the direction of deferred candidate EF-047-(iv) (the `read-contract.md` §1 / `prompts/application.md` §Read ambiguity): `applications/` is NOT part of the §1 closed default-read enumeration and not subject to §2 per-file budget; `prompts/application.md` §Read's instruction to read `applications/` refers to session-scope read-as-needed, not default-read-at-session-open. EF-047-(iv) becomes "document this clarification" rather than "choose between two readings".

## Implementation obligation (pending future self-dev session)

The operator-directed resolution is engine-level but has not yet been adopted via self-dev session + decision record. Adoption obligation:

- **`read-contract.md`**: add a §2 carve-out clause explicitly exempting `applications/` from per-file budget (6K/6 hard, 8K soft values remain for all other enumerated classes); update §10 versioning. Classification: **substantive** per OI-002 (changes normative budget semantics for a class of files) — engine-v7 → v8 candidate.
- **`prompts/application.md`**: §Read paragraph clarifying that "domain reading" of `applications/` is session-scope read-as-needed via chunked-read-on-demand, not default-read-at-session-open; notes optional manifest/index pattern. Classification: **minor** documentary clarification (no new normative rule; consolidates operator-directed interpretation).
- **`specifications/workspace-structure.md`** §applications: may note the optional manifest/index pattern if adopted.

Bundling (iii) of S047 D-150 (kernel §7 `qualitative-multi-agent` label) and (iv) (this resolution's documentary half) plus the §2 budget carve-out into a single engine-v7→v8 bump deliberation is a likely post-arc path. Not proposed here; just noted as the natural grouping.

## Implications for the current `selvedge-disaster-response` arc

The external Session 001 Case Steward's compliance path (quoted at §Observation) is **no longer required** under the operator-directed resolution. The session may produce v1 artefacts at natural domain size without compression or artefact-splitting. The operator may communicate the directive into the external workspace via an operator-message injection at an appropriate point.

Forward observation: if Session 001 has already committed compressed or split artefacts before the operator directive reaches it, later sessions may consolidate via the normal canonical-path-revised revision pattern (S013 D-066 precedent) without violating D-017 (the sealed S001 provenance stays; the mutable application-scope artefact gets a v2 in-place).

## Evidence

- External session 001 Case Steward statement quoted above (operator relay; verbatim).
- `read-contract.md` v4 §2 per-file budget values (6,000 soft / 8,000 hard words; D-086 Session 023 recalibration rationale).
- `read-contract.md` v4 §1 enumeration items 0-9 (does not include `applications/`).
- `prompts/application.md` §Read paragraph 2: "Domain reading — this application's problem statement, constraints, stakeholders, success condition, initial state (the slots above), plus any domain materials introduced into the session."
- `prompts/application.md` §Produce: "External artefacts live in `applications/NNN-<slug>/` per `specifications/workspace-structure.md` v4 §applications."
- S047 deliberation §2f (P3 Outsider's spec-contradiction finding, adopted as Surface 6 feedback target): "`read-contract.md` §1 closed enumeration omits `applications/`; `prompts/application.md` §Read treats `applications/` as read input, making hidden application-scope content ambiguous."
- S047 D-150 deferred spec-amendment candidate (iv): `read-contract.md` §1 + `prompts/application.md` §Read ambiguity resolution.
- Self-dev aggregate measurement at engine-v7: ~80K words across engine-definition + development-provenance default-read surface. External workspace starts at ~80K at S001 open (inheriting the same engine-definition files) + ~0 domain content; can grow ~5-15K per session from artefact accumulation.

## Application-Scope Disposition

The `selvedge-disaster-response` Session 001 began under the current (pre-directive) budget interpretation, per the quoted statement. The operator subsequently directed the resolution above (exclude `applications/` from per-file budget; chunked-read-on-demand; optional manifest/index). Communication of the directive into the external workspace is an operator action; at the time of this record update the external session may or may not have received the directive.

Per arc-plan §11 operator-is-the-transport, this feedback was routed direct-to-self-dev-inbox rather than via the external workspace's outbox → operator-mediated transport, for expediency while the external session was running. The external session's potential own-outbox record about the same friction may duplicate this one; deduplication at triage is acceptable.

**In-session impact at Session 001**: the directive removes the constraint; whether Session 001's already-produced v1 artefacts need re-expansion depends on how much compression was applied before the directive reached the session. If artefacts are compressed and the domain demands more detail, later sessions revise in place via the canonical-path-revised pattern (S013 D-066 precedent).

**Post-arc self-dev review obligation**: the operator-directed resolution still requires formal spec adoption in a future self-dev session (substantive `read-contract.md` §2 carve-out + engine-v8 bump + minor `prompts/application.md` §Read clarification; see "Implementation obligation" section above). This record stays in inbox pending that triage. The S047 D-150 deferred candidate (iv) is subsumed: its direction is determined; its documentation remains to be written.
