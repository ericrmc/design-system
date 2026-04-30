---
session: 008
phase: P1 — observability / ground-truth failure
issued_at: T+5d post-cyclone (Day 5 of 10-day response window)
issuer: Operator (Laurel Delta Emergency Coordinator's office, via Nivaro central government liaison)
input_kind: reveal
do_not_edit_prior_sessions: true
---

# Session 008 input — field reports conflict

## Read this first

This input introduces ground-truth failures that surfaced between Days 3 and 5 of the response. Prior session provenance (S001 through S007) is closed and **must not be edited**. Revisions land as new artefact versions, supersession-ledger entries, and decisions in this session.

The 10-day response plan and the assumption ledger are both live and revisable. Where this input invalidates a prior assumption, the assumption-ledger entry's status moves to `superseded` or `still-active-after-review`; where the plan action it supports must change, cite the conflict resolution that drove the change.

If the substrate's existing assumption status enum does not admit a status that captures "evidence is mixed and the agent cannot resolve to a single source within this session," surface this as engine-feedback rather than collapsing to the closest available value. The operator's interest is in whether the engine surfaces conflict-state honestly, not in whether it picks fast.

## New facts (Days 3–5 field signal)

The Day-3 checkpoint (DV-S002-3) and Day-5 internal review surfaced four conflicts in the operational picture. Each is reported here with both sources and the magnitude of disagreement. None of the four has been adjudicated by a domain authority; **conflict resolution is the agent's task this session**.

### F-1 — Shelter population: local government registry vs NGO household canvass

- **Source A — Laurel Delta civil registration office** (T+108h, Day 3 close): aggregate shelter registration across the six designated emergency shelters totals **11,840** displaced persons. Methodology: head-of-household sign-in at shelter intake, family-unit roster.
- **Source B — Northern Basin Relief Foundation** (T+120h, Day 5 morning): door-to-door + Kellan Rise community-hosting roster + dormitory canvass estimates **16,210** displaced persons currently outside their primary residence. Methodology: enumerator visit to a 30% sample of pre-event addresses in flood zones, statistical extrapolation, plus complete enumeration of the Kellan Rise community-hosted population.
- **Difference:** ~4,370. Neither source claims completeness. The civil registry omits informal sheltering (with relatives, in undamaged buildings, in vehicles) by construction. The NGO estimate may double-count Kellan Rise hosts whose household members also registered at a formal shelter.
- **Brief reference:** brief.md states ~18,000 displaced as the post-cyclone aggregate. Both sources are below this figure; whether the gap is recovered population, undercounted population, or measurement error is unresolved.

### F-2 — Medical-device-dependent count: harbour authority dormitory registration vs hospital pharmacy records

- **Source A — Merrow Port Harbour Authority dormitory occupancy registers** (consolidated T+96h covering five migrant-worker dormitory blocks near the working harbour): **142** dormitory residents recorded as carrying medical-device or chronic-medication status (oxygen concentrators, CPAP, insulin pumps, dialysis access). Methodology: occupant self-declaration at quarterly registration; not all dormitories require declaration.
- **Source B — Hospital pharmacy reconciliation** (Merrow Port Regional + Kellan Rise hospital pharmacy + two affiliated retail pharmacies, prescriptions filled in the 90 days pre-cyclone for cold-chain insulin, home-oxygen supply contracts, CPAP consumables, dialysis supplies, all filtered to Merrow Port + South Latch postcodes inside flood-affected zones): **287** distinct patient records. Methodology: pharmacy dispensing logs cross-referenced by postcode; excludes patients who fill prescriptions elsewhere or pay cash.
- **Difference:** ~145 — and the two sources do not necessarily overlap (a dormitory resident might fill prescriptions at the harbour clinic not in pharmacy reconciliation; a pharmacy patient might not be a dormitory resident at all).
- **Note for the agent:** the assumption ledger as of S004 does not carry an A-NNN entry naming the medical-device-dependent population count, despite the response plan's Priority 4 acting on a "known home oxygen patients, CPAP patients, insulin-requiring patients" enumeration. This conflict reveals an implicit assumption in the plan that a single authoritative count exists.

### F-3 — Flood-depth maps: satellite imagery vs on-ground reports

- **Source A — Provincial Geospatial Office** (LIDAR-derived flood-depth raster from satellite pass at T+18h post-cyclone, processed and released T+72h): South Latch interior peak depth 1.2–2.0m across ~40% of smallholdings; receded to 0.4–0.8m in those zones by T+36h.
- **Source B — Coast guard boat sweep field reports** (T+90h, T+108h, repeat T+120h): conditions impassable for wheeled ambulances across most of South Latch interior; depths reported 0.6–2.4m with significant standing water in areas the satellite map shows as drained by T+36h. Hypothesis from boat crews: tidal back-flow through compromised levees re-floods at high tide and only partially drains at low tide.
- **Difference:** the satellite product is a snapshot; the on-ground reports describe a tidally cyclic depth pattern. Whether the satellite map is wrong, stale, or describing a different time-of-day from the ground reports is unresolved within this session.
- **Action implication:** A-005 verification action ("boat-based South Latch sweep as Day-1 prerequisite") and A-014 boat-staging-capacity both depend on knowing where boats can stage and where wheeled vehicles can reach.

### F-4 — Road access: bridge-passable status changes between hours

- **Source A — Provincial highways structural inspection report** (T+24h, A-009 verification action): highway bridge passable at 24t. Caveats: localised cracking observed at south abutment within tolerance; approach road floods 200m at high tide and recedes at low tide.
- **Source B — Bridge scheduling officer crossing log** (T+90h to T+120h): three convoy crossings suspended ad hoc due to (i) approach-road flooding at high tide T+102h delaying a fuel tanker by 4h, (ii) storm-damaged signage causing single-lane operation T+108h to T+114h, (iii) animal carcass on roadway requiring removal T+118h. Bridge integrity is unchanged; **operational availability is intermittent**.
- **Difference:** the structural verification certified passability; the operational log shows a passable-with-intermittent-suspensions pattern that A-009 does not anticipate. The bridge-throughput allocation DV-S002-1 ("≥ 8 consecutive bridge hours per day on Days 1–3") was met on Days 1–2 but missed by ~2.5h on Day 3 due to the F-4 events compounding.

## Prior assumptions implicated

The agent should review these as candidates for status change. Final disposition is the agent's call; the operator's expectation is that each is explicitly addressed in `02-decisions.md`.

- **A-005** — *All displaced persons in tracked shelter locations* [P3] [UNVERIFIED]. F-1 shows that neither civil registry nor NGO canvass reaches 18,000; informal sheltering is significant. Candidate: `superseded` (reframe to "displaced population is partitioned across formal shelters, community hosting, and informal arrangements; counts are partial from each source").
- **A-009** — *Highway bridge passable at 24t throughout 10 days* [MONITORED]. F-4 shows structural passability holds but operational availability is intermittent. Candidate: `still-active-after-review` with refinement (separate structural-integrity and operational-availability sub-assumptions), or `superseded` by a new pair of A-NNN entries.
- **A-014** — *Boat staging capacity sufficient for patient loading from flooded South Latch* [UNVERIFIED]. F-3 shows that the spatial allocation of boats vs ambulances depends on flood-depth which is itself contested. Candidate: keep `UNVERIFIED` but add a new A-NNN for "flood-depth ground-truth source-of-record" that A-014's verification depends on.
- **Implicit** — *Medical-device-dependent population count is enumerable from a single source* (no A-NNN; embedded in Priority 4 plan language). F-2 reveals the assumption. Candidate: open a new A-NNN entry naming the count and listing both sources as evidence; admit `active-with-conflict` if the substrate or artefact admits that status, otherwise note the gap as engine-feedback.

The arc-plan reveal axis (**observability stress**) names exactly this surface: the engine should admit `active-with-conflict` (or its artefact-equivalent) as a status, rather than the agent silently choosing one source. If the assumption-ledger schema as of S007 does not admit such a status, this session's choice — extend the schema, choose a source with reasoning, or punt — is the engine-feedback signal.

## Constraints on this session

1. **Do not edit prior session provenance.** S001–S007 close-records, decisions, and provenance markdown are immutable. New decisions belong to S008. New artefact versions cite S008 in their `revised_by_session` frontmatter.
2. **Cite the conflict resolution** in any response-plan revision. If Priority 4 changes its sweep scope because of F-2, the revised section names F-2 as the trigger and identifies which source (or which synthesis) was adopted and why. Narrative-only revision is laundering.
3. **Active-with-conflict status admission.** If the assumption-ledger today cannot represent "evidence mixed, no within-session resolution," the agent's choice is a load-bearing one and must be recorded as a decision (kind=substantive) with at least one alternative rejected and at least one engine-feedback row authored.
4. **Supersession-ledger update.** Every assumption status change creates a supersession-ledger entry (event-id, session, invalidated-assumption-id, invalidating-input-path = this file's path, superseding-content-anchor, OI-reference if any).
5. **Cross-artefact citation discipline.** Any response-plan section changed cites the assumption ID(s) it now depends on. The risk-register may need new entries for tidally-cyclic flood depth, intermittent bridge availability, and undercounted populations.
6. **No new domain content beyond F-1 to F-4.** This input is the entire factual reveal. The agent does not invent new field signals; it works the four conflicts above.

## Engine-surface signals the operator is watching for

These are not constraints on the agent — they are what the operator is reading the artefacts for. The agent should not optimise for these; they are noted to remove ambiguity about why the reveal is shaped this way.

- Whether the assumption-ledger admits an `active-with-conflict` status, and if not, how the agent records the conflict.
- Whether the response-plan revision cites which conflict resolution drove which action change, or whether the prose changes silently.
- Whether the medical-device-dependent count gap is registered as a new A-NNN (constraint §1 prose-state surfaced) or papered over (constraint §1 violated).
- Whether the agent reaches for `bin/selvedge query` to count things this session or narrates counts in prose (constraint §1, §5).
- Whether the supersession-ledger entries trace the invalidating-input-path back to this file (constraint §5 detection-without-feedback).

## Out of scope

- Phase 2 / Phase 3 / Day-7 / Day-10 plan revisions. The reveal is a Day-5 signal; later-phase revision is appropriate only where the new evidence directly invalidates a later-phase action.
- Recovery-plan content. The 10-day window remains the frame.
- Stakeholder authority questions. P4 phase territory; not surfaced here.
- New domain incidents (aftershock, secondary outbreak, fatigue). P5 phase territory.

## Closing protocol for this session

Per prompts/application.md and per this arc's anti-laundering criteria: produce ≥1 engine-feedback row capturing what the conflict-resolution surface revealed about the engine. The operator transports it back to self-development via `monitor-external harvest-ef`.

Engine-feedback this session is expected to land on at least one of:
- the `active-with-conflict` status admission question (constraints §1)
- the supersession-ledger entry shape under multi-source invalidation (constraints §5)
- the registered-vs-implicit assumption gap surfaced by F-2 (constraints §1, §5)

Other observations are welcome.
