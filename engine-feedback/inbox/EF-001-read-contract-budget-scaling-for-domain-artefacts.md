---
feedback_id: EF-001-read-contract-budget-scaling-for-domain-artefacts
source_workspace_id: selvedge-disaster-response
source_session: 001
created_at: 2026-04-24
reported_by: operator
target: engine
target_files:
  - specifications/read-contract.md
  - prompts/application.md
  - specifications/workspace-structure.md
severity: friction
status: inbox
---

# EF-001 — Read-contract per-file budget (6K soft / 8K hard) does not obviously scale to domain artefacts in external applications

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

## Suggested Change

This is a **substantive spec question** warranting proper deliberation (self-dev MAD), not an ad-hoc fix. Candidate framings for that deliberation:

**(a) Separate budget class for application-scope mutable artefacts.** New §2d in `read-contract.md`: application-scope artefacts have a relaxed per-file budget (candidate values: 24K hard / 18K soft, approximately 3× the engine-file default). Aggregate budget still applies. Rationale: domain artefacts have different natural size distributions than engine/methodology files.

**(b) Index-plus-detail pattern formalised for application artefacts.** Canonical artefact at `applications/NNN-<slug>/system-model.md` is an index under 6K with `[archive: applications/NNN-<slug>/system-model-detail/]` references; detail files in `system-model-detail/` each under 8K with archive-pack discipline. Preserves existing budget; introduces index-layer overhead.

**(c) Exclude applications/ from default-read per-file budget; apply only to aggregate.** `read-contract.md` §2 carves out `applications/` content from per-file measurement. Only §2b aggregate budget applies. Simple; asymmetric across file classes but matches different natural size distributions.

**(d) Defer to external-application discretion.** Each external application records a per-artefact-budget choice in its brief or arc-plan; engine provides guidance but not mandate. Preserves engine simplicity; increases per-application governance cost.

**(e) Preserve current strict budget; mandate artefact-splitting convention.** Formalise split-into-multiple-files with naming conventions (`system-model-infrastructure.md`, `system-model-population.md`, ...). Lowest spec change; highest per-artefact complexity cost.

Related: resolving the `applications/` default-read enumeration ambiguity (deferred candidate EF-047-(iv)) is **prerequisite** to any of (a)-(e). The current spec contradiction (`read-contract.md` §1 excludes `applications/`; `prompts/application.md` §Read includes it) must be settled first to know whether the budget even applies.

OI-002 classification: any of (a)-(e) is **substantive** (changes §2 budget semantics or adds new classes). Would bump `read-contract.md` v4 → v5 + engine-v7 → v8.

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

The `selvedge-disaster-response` Session 001 is operating under the current budget (per the quoted statement; compliance path being domain-content compression and/or potential file-splitting). This produces **domain-distortion of the v1 artefacts** for this specific application — a direct cost to disaster-response-artefact quality.

Per arc-plan §11 operator-is-the-transport, the operator has chosen to route this feedback direct-to-self-dev-inbox rather than waiting for external Session 001's own outbox-write + operator-mediation. This is expedient (gets the signal to self-dev immediately while the external session is still running) but means the external session's own potential outbox record about the same friction may duplicate this one. Deduplication at triage is acceptable.

**In-session resolution at Session 001**: none. The budget is a standing engine-level constraint; external sessions cannot amend it from inside their own execution (per `prompts/application.md`: "[engine-definition files] are not up for revision within this application's sessions unless a kernel-revision is explicitly authorised by the engine's source workspace"). The session must execute under the current constraint.

**Post-arc self-dev review**: this feedback joins the backlog of S047 D-150 deferred candidates. The spec contradiction at EF-047-(iv) is prerequisite; this EF-001 record is the downstream scalability consequence. Post-arc self-dev MAD (probably engine-v8 bump candidate) should address (iv) resolution first, then (a)-(e) budget-scaling framings, likely in one bundled deliberation.
