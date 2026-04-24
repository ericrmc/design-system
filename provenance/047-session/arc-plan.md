---
title: Arc-Plan — selvedge-disaster-response external-application Sessions 001-005
session: 047
date: 2026-04-24
status: authoritative-self-dev-copy
created: 2026-04-24
placement: self-dev (per D-147 §3 placement option (a))
external_workspace: /Users/ericmccowan/Development/selvedge-disaster-response/
application_id: 001-disaster-response
produced_by: Session 047 four-perspective two-family MAD (2 Claude + 2 Codex/GPT-5.5)
synthesizer: claude-opus-4-7-case-steward
visibility: operator-only — do NOT copy into external workspace default-read surface until arc completion (Session 005 close or later)
---

# Arc-Plan — selvedge-disaster-response external-application

## §1 Summary + feedback-yield thesis

This is the authoritative plan for executing the Selvedge engine against its **first genuine external-problem application** across **five sessions** in the workspace at `/Users/ericmccowan/Development/selvedge-disaster-response/` (bootstrapped at Session 046 D-142).

The application is a **fictional self-contained compound coastal-disaster response scenario** in the invented geography "Laurel Delta" in the invented country "Nivaro". The scenario is deliberately a vehicle: its purpose is NOT to produce a realistic disaster-response plan but to produce **the most valuable engine-feedback to self-development** per the operator's S047 optimisation target.

The arc is designed around **seven engine surfaces** (§8) chosen because the engine currently under-specifies or under-exercises them. Each session is structured to exercise at least one surface via **deliberate design**, not emergent accident.

**Feedback-yield thesis**: a clean disaster-response narrative would produce little feedback — the engine chugs through competently. An arc with pre-declared invalidation axes, hidden future constraints, measurable anti-laundering close-criteria, and a final retrospective session focused explicitly on engine-feedback synthesis will force the engine into its under-specified corners at known boundaries. Where executing sessions feel friction, that friction becomes a feedback record. Where they proceed smoothly when friction was expected, that smoothness is itself informative.

**Operator role**: the operator holds the full arc-plan (this file); external sessions see only what the operator transports to them at each session's T0. **The external application does not have the full view of the scenario until all sessions are completed** (operator constraint recorded in §2.5 of the session 047 shared brief).

## §2 Scenario at T0 — what Session 001 sees

### §2a Setting

**Laurel Delta**, a low-lying island-and-estuary district in the invented country **Nivaro**. The setting is fictional; no real geography or public disaster case is imported, so the executing sessions must reason from the brief rather than leaning on memorised domain knowledge (anti-laundering per PROMPT.md external-imports rule).

Laurel Delta has three main settlements:
- **Merrow Port** (coastal, ~62K, working harbour + industrial fishery; dense waterfront tenements; one regional hospital with ~450 beds including a neonatal unit).
- **South Latch** (low-lying agricultural plain, ~58K, dispersed smallholdings + two aged-care clusters; levee-dependent; one primary-care clinic + one dialysis centre serving ~1,200 patients).
- **Kellan Rise** (upland approach, ~80K, mixed urban-residential; one secondary hospital ~280 beds; principal road-access to the highlands).

Total affected population: approximately **200,000**.

### §2b Vulnerability profile

- ~9% over age 70 (~18K).
- ~2.5% dependent on powered medical equipment (~5K) — CPAP, home oxygen, refrigerated medications (insulin, biologics).
- ~1,200 dialysis-dependent in South Latch; regional hospital handles ~220 more.
- Migrant-worker seasonal housing near Merrow Port industrial fishery (~9K) — low-quality dormitories; two languages other than the majority.
- Dispersed fishing community on outer estuary islets — informal VHF-radio networks; no reliable cellular coverage even pre-disaster.
- One freight rail bridge connecting Merrow Port to the interior; this bridge also carries a major fibre-optic trunk serving Kellan Rise.

### §2c The disaster at T0

A late-season cyclone has crossed Laurel Delta approximately 36 hours before Session 001 opens. Current observable state:

- Storm surge peaked ~2.8m above mean high tide; lower Merrow Port and two thirds of South Latch are flooded; water is receding unevenly.
- Approximately 18,000 people are displaced; shelter capacity strained.
- Grid power is out across Merrow Port and South Latch; two of four coastal substations degraded; partial restoration estimated 3-7 days by local utility.
- The primary drinking-water treatment plant in Merrow Port has salt-water intrusion; decontamination assessment underway; backup wells serve ~35K on rotation.
- Hospital continuity risk: Merrow Port regional hospital on generator; Kellan Rise secondary hospital unaffected; dialysis centre in South Latch inaccessible.
- Road access: the freight rail bridge damaged but passable; one highway bridge into Merrow Port intact at 24-tonne rating; sea access degraded (salvage required); air access degraded (runway debris).
- Local government in Laurel Delta has requested from central government a **10-day response-and-stabilisation plan** that Session 001 will produce v1 of.

### §2d What Session 001 DOES NOT yet see (operator retains)

- The future invalidation axes at S002/S003/S004 reveals (coordination / infrastructure+comms / demand).
- The specific assumption-IDs that will be targeted for invalidation (emergent per operator selection at each T0).
- The S005 retrospective design — that Session 005 is an engine-feedback-synthesis session rather than further response-planning.
- The existence of this arc-plan as a single document. Session 001 sees only `brief.md` (already populated by the bootstrap slot-template fill) plus `session-inputs/session-001-input.md` which operator delivers at S001 T0.

## §3 Arc structure — per-session stubs

### §3a Session 001 — system model + initial response plan

**Broad objective**: establish the system model, explicit assumption ledger, and a first-pass 10-day response-and-stabilisation plan under the information available at T0.

**Pre-declared axis for T0**: n/a (T0 is the baseline; no prior-session assumptions to invalidate).

**Operator-facing stub** (what operator drafts as `session-inputs/session-001-input.md`): Transfer §2a, §2b, §2c of this arc-plan verbatim into the external workspace's `applications/001-disaster-response/session-inputs/session-001-input.md`. Do NOT include §2d or any part of §3b-§3e / §4 / §5 / §8 / §9 of this arc-plan. The `brief.md` slot-template in the external workspace should be populated with §2a + §2b + §2c + a statement that subsequent session inputs will be delivered at each T0.

**Expected artefacts produced in S001**:
- `applications/001-disaster-response/system-model.md` (v1) — external/environmental/infrastructural system model
- `applications/001-disaster-response/assumption-ledger.md` (v1) — central; stable assumption IDs A-001, A-002, ...
- `applications/001-disaster-response/response-plan.md` (v1) — 10-day response-and-stabilisation plan
- `applications/001-disaster-response/risk-register.md` (v1)
- Per-session provenance: `00-assessment.md`, `01-brief-shared.md`, four perspective files, `01-deliberation.md`, `02-decisions.md`, `03-close.md`
- Optional: initial `engine-feedback/outbox/EF-001-*.md` if any methodology friction observed

**Per-session measurable close criteria** (close is blocked if any absent):
- Assumption-ledger contains ≥12 numbered assumptions each with ID, status, and originating evidence.
- System-model names at least three infrastructure dependencies that are load-bearing for the response plan.
- Response plan cites assumption IDs directly (not paraphrased).
- Close lists ≥1 strained or failed validation criterion OR explicitly justifies why every criterion passed cleanly (laundering-audit).
- ≥1 EF outbox candidate written OR close-note justifying non-production.

### §3b Session 002 — coordination-axis shift

**Broad objective**: revise response plan + governance under a reveal that invalidates one or more S001 coordination assumptions. Produce a decision-tree for key branch-points (water-rationing triggers; medical-evac priorities; shelter-expansion thresholds).

**Pre-declared axis for T0**: **coordination** — the assumed-at-S001 unified local command is false. Central government / provincial government / port-security emergency authority structure is contested; at least one relief NGO (fictional: "Northern Basin Relief Foundation") refuses to share beneficiary data.

**Operator action at T0** (emergent-specific-assumption selection):
1. Read `selvedge-disaster-response/applications/001-disaster-response/assumption-ledger.md` (v1 produced by S001).
2. Select at least TWO coordination-class assumptions from S001's ledger that were load-bearing for the S001 response plan. Examples of what to target if present: "central government emergency coordinator has operational authority", "local NGOs will share beneficiary data", "Merrow Port harbour authority retains civilian command during emergency", "one emergency operations centre coordinates across all three settlements".
3. Draft `session-inputs/session-002-input.md` with four sections: **New Facts** (the coordination-split reveal); **Invalidated Prior Assumptions** (list the 2+ assumption IDs from step 2); **Constraints for This Session** (the invalidation implies plan revision + assumption-ledger updates + OI opening for any unresolved coordination work); **Do Not Resolve By Editing Prior Sessions** (restates D-017).
4. Place `session-002-input.md` into external workspace; external Session 002 opens reading this file as its scope-update.

**Operator-facing stub — template content for `session-inputs/session-002-input.md`**:

> ## New Facts at Session 002 T0
>
> Three days after the initial response, the governance structure that Session 001 assumed has fractured. [Flesh out: Merrow Port's harbour-authority emergency declaration remains in force, restricting civilian coordinator access to the dock zones. The provincial emergency commissioner for South Latch has invoked Article [X] of the Nivaro Civil Protection Act, claiming command precedence over the central government's coordinator. The Northern Basin Relief Foundation, coordinating ~40% of shelter intake, has refused to share beneficiary registration data citing donor-confidentiality policy.]
>
> ## Invalidated Prior Assumptions
>
> [Operator fills: list assumption IDs A-NNN from S001 ledger; e.g., "A-003 (central-government coordinator has operational authority across all three settlements) — invalidated by port-authority Article [X] invocation"]
>
> ## Constraints for This Session
>
> Revise the response plan under the coordination-fractured state. Update the assumption-ledger with statuses and new assumptions. Open OIs in the external workspace's `open-issues/` for any unresolved coordination questions. Build a decision-tree for at least three load-bearing branch-points (water rationing, medical evacuation priority, shelter data-sharing under NGO refusal).
>
> ## Do Not Resolve By Editing Prior Sessions
>
> S001's provenance is immutable per D-017. Do not edit any file in `provenance/001-*/`. Do not edit S001's response-plan.md in place — create response-plan.md v2 in the mutable canonical location with `-v1.md` preservation per the workspace-structure.md v5 §applications revision pattern; cross-reference S001's sealed copy in supersession-ledger.md.

**Expected artefacts produced in S002**:
- `response-plan.md` v2 (revised)
- `decision-trees.md` (new)
- `assumption-ledger.md` updated (statuses modified; 2+ IDs now `superseded` or `invalidated`; new A-IDs added)
- `supersession-ledger.md` (new; first rows recording S001→S002 supersession events)
- `risk-register.md` v2 (revised)
- ≥1 new OI in external `open-issues/` for invalidated-assumption unresolved work; OI frontmatter `supersedes-assumption-in:` pointer

**Per-session measurable close criteria**:
- ≥2 assumption IDs marked `superseded`/`invalidated`/`still-active-after-review`.
- ≥1 artefact section changed citing `session-002-input.md` as triggering change.
- `supersession-ledger.md` exists with ≥2 rows.
- ≥1 decision-tree branch includes an "under coordination-fracture" alternative path.
- Close lists ≥1 strained or failed validation criterion OR justifies zero-strains.
- ≥1 EF outbox record OR justified non-production.

### §3c Session 003 — infrastructure + communications shift

**Broad objective**: revise under a compound infrastructure+comms degradation reveal; adapt logistics under extended access constraints.

**Pre-declared axis for T0**: **infrastructure + communications coupled** — the freight rail bridge (load-bearing per S001 assumption) is unusable for ~3 weeks (not passable as S001 assumed); the fibre-optic trunk carried by that bridge is severed, dropping Kellan Rise's high-bandwidth data link; cellular restoration in Merrow Port delayed beyond S001 estimate; satellite bandwidth exists but is rationed.

**Operator action at T0**: select ≥2 infrastructure/comms assumptions from S001-or-S002 ledger state; draft `session-inputs/session-003-input.md`.

**Operator-facing stub**:

> ## New Facts at Session 003 T0
>
> [Flesh out: structural engineers have found the east approach of the freight rail bridge unstable after the storm's aftermath shock; the bridge cannot be re-opened for ≥21 days. The fibre-optic trunk suspended from its deck is severed; Kellan Rise's data link drops to microwave backup at ~5% of prior capacity. Cellular restoration in Merrow Port is revised: zones 2 and 4 will not be restored within 14 days due to flooded switchgear. Satellite bandwidth is rationed to emergency-services priority.]
>
> ## Invalidated Prior Assumptions
>
> [Operator fills: IDs from S001-or-S002 ledger; e.g., "A-007 (freight rail bridge passable within 3-5 days) — invalidated by structural assessment"]
>
> ## Constraints for This Session
>
> Revise logistics under extended-access constraints. Re-plan communications for 10+ day degraded-data-link state. Update decision-trees for comms-degraded branches. Explicitly audit whether any S002-preserved minority position is vindicated or obsoleted by this reveal.
>
> ## Do Not Resolve By Editing Prior Sessions

**Expected artefacts** — as §3b pattern with additions: system-model.md revised (v2) to reflect degraded connectivity; decision-trees.md revised (v2) with comms-degraded branches.

**Per-session measurable close criteria** (cumulative with §3b + one new):
- Standard set.
- **Minority-lifecycle audit**: if any S002 preserved minority's factual premise is touched by the S003 reveal, the close must explicitly record (a) vindicated, (b) obsoleted, or (c) preserved-unchanged disposition with forward-reference. Zero-audit-action across sessions is evidence of laundering.

### §3d Session 004 — demand-axis shift

**Broad objective**: revise response plan under demand-surge reveal; explicit audit of accumulated minority positions and deferred OIs from S001-S003.

**Pre-declared axis for T0**: **demand** — shelter demand doubles because upland temporary camps evacuate into the Delta; cold-chain medical demand is higher than estimated; water contamination appears in two shelters; medical-equipment-dependent census revised upward ~+40% over S001 estimate.

**Operator action at T0**: select ≥2 demand-class assumptions; draft `session-inputs/session-004-input.md`.

**Operator-facing stub**:

> ## New Facts at Session 004 T0
>
> [Flesh out: two upland temporary camps (Valdier Ridge, Oakshade) are evacuating into Laurel Delta due to secondary landslide risk — ~7,500 additional displaced arriving over 72 hours. Cold-chain medical supplies running below threshold for 3-5 day horizon. Water contamination (E.coli + low-level hydrocarbon) confirmed in the Tarsal East shelter and the Municipal Hall shelter. Census review: medical-equipment-dependent count revised to ~7,100 from S001 estimate of ~5,100 — previously uncounted migrant-housing residents surface through harbour-authority dormitory registration.]
>
> ## Invalidated Prior Assumptions
>
> [Operator fills]
>
> ## Constraints for This Session
>
> Revise response plan under demand surge. Produce a recovery-plan.md (v1) covering weeks 1-4 transition. Explicitly audit accumulated minority positions and deferred OIs from Sessions 001-003: which remain active, which are obsoleted, which are vindicated? Record dispositions in the supersession-ledger with OI-cross-references.
>
> ## Do Not Resolve By Editing Prior Sessions

**Expected artefacts** — standard + `recovery-plan.md` (new v1) + explicit disposition-audit entry in `supersession-ledger.md`.

**Per-session measurable close criteria** (cumulative + one new):
- Standard set.
- **Accumulated OI + minority audit disposition**: every active OI from S001-S003 is dispositioned (still-active / closed / obsoleted); every preserved minority is dispositioned.

### §3e Session 005 — recovery transition + engine-feedback synthesis

**Broad objective**: transition from response to recovery; produce a **recovery-transition artefact**; classify what the application's artefacts are validated-by vs merely internally-coherent; produce an engine-feedback synthesis and ≥3 EF outbox records addressing the seven targeted surfaces (§8).

**Pre-declared axis for T0**: **validation-meta** — the operator reveals that no domain-actor will ever be available for this scenario; no reference-validation case exists; the arc's qualitative-multi-agent validation must be honestly scoped. This is not a scenario-axis change but an engine-internal reveal: the arc is intentionally a self-development feedback exercise, and S005's job is to produce that feedback.

**Operator action at T0**: draft `session-inputs/session-005-input.md` naming the meta-reveal + charging S005 with engine-feedback-primary work.

**Operator-facing stub**:

> ## New Facts at Session 005 T0 (meta-reveal)
>
> This session is the retrospective and engine-feedback synthesis. There is no domain actor available. There is no reference case against which this application's artefacts can be validated. The arc was designed from the Selvedge engine's self-development workspace to produce engine-feedback. Your task for this session is to produce: (a) a recovery-transition artefact bounding what the application supports going forward; (b) a validation-position statement declaring exactly what claims the artefacts support and do not support; (c) ≥3 engine-feedback outbox records addressing methodology-level friction observed across Sessions 001-004.
>
> ## Constraints for This Session
>
> Adopt a meta-reflective MAD shape (4-perspective two-family if feasible; at least one non-Claude). The synthesis question for this session is: "What did the arc's qualitative-multi-agent validation not see from within itself?" Produce a supersession map from Session 001 assumptions to Session 005 state. Emit engine-feedback records.
>
> ## Do Not Resolve By Editing Prior Sessions

**Expected artefacts**:
- `recovery-plan.md` v2 (bounded; transition-only)
- `validation-position.md` (new; declares what is and is not validated)
- `retrospective.md` (new; cross-session observations)
- `engine-feedback-synthesis.md` (new; application-scope companion that enumerates EF records with reasoning)
- **≥3 `engine-feedback/outbox/EF-005-*.md` records** (outbox — to be operator-transported to self-dev inbox)
- Supersession map (as a new file or section in `supersession-ledger.md`)

**Per-session measurable close criteria** (S005-specific):
- ≥3 EF outbox records written, each ≥250 words with ≥1 concrete evidence pointer.
- `validation-position.md` exists and explicitly states which kernel §7 sense (or fallback) each artefact class is validated under.
- Supersession map traces Session 001 assumptions to final dispositions.
- Retrospective identifies ≥2 surfaces where the arc's validation *did not* catch a weakness that a different validation shape would have.
- ≥3 of the seven targeted feedback surfaces from §8 have been exercised and produced an EF record across the arc (not necessarily all in S005).

## §4 Evolution mechanic (70/30 hybrid)

**Pre-declared** (70% of mechanism):
- Each transition's **axis** is fixed in this arc-plan: S001→S002 coordination, S002→S003 infrastructure+comms, S003→S004 demand, S004→S005 validation-meta.
- Each transition has a **magnitude range** defensible from the scenario (storm aftermath; infrastructure fragility; secondary hazards).

**Emergent** (30% of mechanism):
- The **specific assumption** invalidated at each transition is selected by the operator at session-open after reading the prior session's committed assumption-ledger. The invalidated assumption must be one the prior session actually made load-bearing.
- The operator may add ancillary facts to the reveal to make the scenario coherent under the invalidation.

This hybrid prevents:
- Pre-scheduled-only → constraint change irrelevant to what the session actually committed to.
- Pure-emergent-only → operator may retcon whatever at each transition.

## §5 D-017-compliant invalidation mechanism (three parts)

No closed-session provenance file is ever edited. The three parts live in the external workspace as application-scope mutable content.

### §5a Assumption ledger

`applications/001-disaster-response/assumption-ledger.md` — created S001; mutable through S005.

Each assumption row:

```yaml
assumption_id: A-NNN
originating_session: NNN
status: active | superseded | invalidated | unresolved | still-active-after-review
invalidated_by_session: NNN | null
invalidating_input: session-inputs/session-NNN-input.md | null
affected_artefacts:
  - applications/001-disaster-response/response-plan.md#<section>
prior_provenance_witness: provenance/NNN-session/03-close.md (sealed reference)
text: "<verbatim assumption statement>"
```

### §5b Supersession ledger

`applications/001-disaster-response/supersession-ledger.md` — append-only chronological ledger.

Schema (markdown table):

| event-id | session | invalidated-assumption-id | invalidating-input | superseding-content | OI-reference |
|----------|---------|---------------------------|---------------------|---------------------|---------------|
| SL-001 | 002 | A-003 | session-inputs/session-002-input.md | response-plan.md#coordination | open-issues/OI-001.md |

### §5c Supersession-marker OI

When an invalidated assumption creates unresolved application work, a new OI-NNN.md is opened in the external workspace's `open-issues/` directory:

```yaml
---
id: OI-NNN
status: open-invalidated-assumption  # new value — feedback candidate per D-150(iii)
surfaced-in-session: NNN
supersedes-assumption-in:
  - path: applications/001-disaster-response/<artefact>.md
    section: <heading or line-range>
    session-of-origin: NNN
supersession-reason: <one sentence>
---
```

Body: verbatim superseded assumption quote + invalidating-input content + proposed-replacement-or-open-question + explicit note that prior-session file remains unchanged per D-017.

## §6 Per-session validation approach

**4-perspective per-session MAD** (S001-S004). The four roles:

1. **Operations Planner** (Claude subagent) — forward-looking plan content.
2. **Constraint Skeptic** (Claude subagent, adversarial) — challenges assumptions; red-teams plan; surfaces hidden premises.
3. **Stakeholder Simulator** (Claude subagent OR non-Claude; stakeholder identity varies per session) — reasons from a specific affected-group perspective named in that session's input. Suggested: S001 Merrow Port regional-hospital continuity-manager; S002 provincial emergency commissioner (coordination); S003 Kellan Rise secondary-hospital IT director (infrastructure/comms); S004 logistics officer coordinating camp influx (demand); S005 external-audit equivalent (meta).
4. **Engine Friction Recorder / Laundering Auditor** (non-Claude preferred; Codex/GPT-5.5 when feasible) — watches for methodology breakdowns; drafts candidate engine-feedback records; explicitly states whether the session produced real engine-feedback evidence vs. domain-work-only output.

**S005** uses 4-perspective two-family (2 Claude + 2 Codex/GPT-5.5) mirroring S047's shape for the meta-reflective synthesis.

**Convergence threshold**: 3-of-4 for substantive decisions within the external application. Minority preservation per MAD v4 §Preserve Dissent.

**Fallback validation criteria (kernel §7 void — no domain-actor, no reference case):**
1. **Internal coherence**: session artefacts don't contradict each other.
2. **Cross-artefact consistency**: assumption IDs cross-linked; `assumptions.md` lists every load-bearing premise used in `response-plan.md` and `decision-trees.md`; reverse-check passes.
3. **Adversarial-probe sufficiency**: Constraint Skeptic surfaces ≥1 hidden premise not explicit; resolved by adding to ledger or revising plan.
4. **Stakeholder-simulation plausibility**: Simulator surfaces ≥1 operational constraint; resolved by model adjustment or explicit mismatch flag.
5. **Constraint-impact accounting** (reveal sessions only): every reveal names affected assumption IDs and artefact sections.
6. **Engine-feedback candidate check**: close either ≥1 EF outbox record OR justified non-production note.
7. **Laundering-auditor statement**: Auditor declares whether session produced engine-feedback evidence or domain-work-only output.

Frontmatter label: `validation: qualitative-multi-agent` (new value, proposed; feedback candidate per D-150(i)).

## §7 Measurable anti-laundering guards (close-criteria)

Each session's `03-close.md` must verify all applicable guards. Absence of any applicable guard blocks clean close.

1. **Failed/strained criteria**: every close lists ≥1 FAILED or STRAINED validation criterion, not only passed. Zero strains across 5 sessions is evidence of laundering not success.
2. **Mutable artefact revision traceability**: every revision after S001 updates `last-revised-session` and includes a `supersedes` OR `change_reason` entry naming the triggering `session-input.md`. Revisions without pointers are suspect.
3. **Cross-session touch**: every session after S001 names ≥1 prior assumption/artefact-section/OI/minority/validation-claim that was preserved/revised/superseded/invalidated. If none, the session did not exercise the intended surface.
4. **Reveal-session assumption action**: sessions S002-S004 mark ≥2 assumption IDs as `superseded`/`invalidated`/`still-active-after-review` AND name ≥1 artefact section changed.
5. **EF outbox production**: every session produces ≥1 EF outbox record OR a close-note explicitly justifying non-production.
6. **EF record substance**: each EF file ≥250 words with ≥1 concrete evidence pointer (session-input path, artefact diff, OI reference, close-section claim) + application-scope disposition statement.
7. **Minority-lifecycle audit** (S003-S005): if any prior preserved minority's factual premise is touched by current-session reveal, close explicitly records vindicated/obsoleted/preserved-unchanged disposition.

## §8 Targeted engine-feedback surfaces

Seven surfaces the arc is designed to exercise. Each has a draft EF filename + one-sentence thesis. External sessions producing EF records should use these filenames (or equivalent) when the surface is exercised.

1. **Hidden-scenario / partial-view session-done-ness** (kernel §1 Read + §9 Close + §2.5 constraint).
   - Draft: `EF-001-partial-view-session-doneness.md`
   - Thesis: "Kernel §1 Read and §9 Close assume scope is fully readable at session-open; under partial-view the session cannot distinguish 'local scope complete' from 'next session's reveal will include shape-changing content'; close criteria became ambiguous at Session 001."

2. **Kernel §7 validation-label vocabulary void** (fictional + no domain-actor case).
   - Draft: `EF-005-qualitative-validation-label-gap.md`
   - Thesis: "Fictional external artefacts had neither domain actor nor reference substitute; fallback label `validation: qualitative-multi-agent` was necessary but is not codified in kernel §7's enumeration."

3. **D-017 retroactive-invalidation recording mechanism** (workspace-structure §provenance).
   - Draft: `EF-003-retroactive-invalidation-mechanism.md`
   - Thesis: "D-017 is clear that closed provenance is immutable, but the forward-recording affordance is under-specified; arc had to compose assumption-ledger + supersession-ledger + supersession-marker OIs without spec guidance."

4. **OI state-machine under constraint invalidation**.
   - Draft: `EF-004-oi-constraint-invalidated-state.md`
   - Thesis: "Existing OI states {open, resolved, deferred} have no state for 'surfaced by later-session constraint invalidation, premise moot'; sessions opened OIs with ad-hoc `status: open-invalidated-assumption`."

5. **MAD v4 minority preservation under invalidated premises** (cross-session dissent lifecycle).
   - Draft: `EF-004-minority-after-invalidated-premise.md`
   - Thesis: "MAD v4 §Preserve Dissent does not specify how a preserved minority's warrant reads when its scenario-grounding is invalidated by a subsequent session's constraint-update."

6. **Read-contract applications/ closed-enumeration ambiguity** (direct spec contradiction).
   - Draft: `EF-001-application-scope-read-contract-ambiguity.md`
   - Thesis: "`read-contract.md` v4 §1 enumeration items 0-9 do not include `applications/`; `prompts/application.md` §Read instructs external sessions to read `applications/` as domain scope; hidden-arc constraint turns latent drift into operational question."

7. **Engine-feedback outbox first-use operability** (workspace-structure §engine-feedback).
   - Draft: `EF-05X-feedback-outbox-operability.md`
   - Thesis: "First live exercise of the outbox pathway bootstrapped at S046 D-142; [report ergonomics, timing, schema adequacy, operator-transport workflow]."

**Not targeted**: real disaster-response domain competence; OI-018 engine-v bump-trigger calibration.

## §9 Vindication / refutation criteria for the arc (arc-end assessment)

Observable at S005 close or immediately after (operator assessment).

**Vindication** — the arc exercised the engine surfaces it was designed to exercise:
- ≥4 non-duplicative EF outbox records exist across the arc.
- No future reveal was visible in the external workspace before its session opened.
- Every reveal changed or explicitly reaffirmed assumption IDs.
- No closed provenance was edited (`git log` check on `provenance/NNN-*/` paths).
- Session 005 produced a supersession map from S001 assumptions to final artefacts.
- ≥5 of the 7 targeted surfaces from §8 have a corresponding EF record.
- `validation-position.md` exists declaring what the application validates and does not validate.

**Refutation** — the arc drifted into ceremony:
- Fewer than 2 substantive EF records (the pathway was exercised but not meaningfully).
- Constraint updates appeared only as narrative notes in artefacts; assumption statuses did not change.
- Preserved minorities were dropped without explicit disposition.
- The operator had to explain arc coherence outside the workspace because the artefacts did not show it.
- Any closed-session provenance file was edited.
- Zero strains recorded in any session's close (laundering signal).

## §10 Deferred spec-amendment candidates (per D-150)

These are NOT adopted in this session. Arc-execution generates feedback; post-arc self-dev review decides adoption.

1. **(i) Kernel §7 validation-label vocabulary extension with `qualitative-multi-agent`** — substantive; kernel v6→v7; engine-v7→v8.
2. **(ii) `workspace-structure.md` §provenance D-017 supersession-marker codification** — minor.
3. **(iii) OI state-machine extension with `constraint-invalidated` / `open-invalidated-assumption` transition** — substantive.
4. **(iv) `read-contract.md` §1 + `prompts/application.md` §Read ambiguity resolution** (P3 unique finding) — minor on whichever path is chosen.

## §11 Operator transport instructions

For each external session:

1. **Before external Session N opens**: read the arc-plan §3N (this file's per-session stub for Session N).
2. **Read the prior external session's assumption-ledger** (`selvedge-disaster-response/applications/001-disaster-response/assumption-ledger.md`) to select the specific assumption(s) to target at N's T0.
3. **Draft `session-inputs/session-00N-input.md`** using the stub template in §3N as a starting point; populate with concrete new-facts + specific invalidated assumption IDs.
4. **Place the input file** into the external workspace at `/Users/ericmccowan/Development/selvedge-disaster-response/applications/001-disaster-response/session-inputs/session-00N-input.md` BEFORE opening Claude Code in that workspace.
5. **Open Claude Code** in `/Users/ericmccowan/Development/selvedge-disaster-response/`. The engine's `PROMPT.md` dispatcher loads `prompts/application.md` via `MODE.md`.
6. **Session N executes** per `prompts/application.md` with the T0 input visible.
7. **At close**: verify the session's close-criteria (§7 guards applicable to N); if any EF outbox record was written, mediate it into self-dev's `engine-feedback/inbox/` before the next self-dev session opens.

For the **first** external session:
- `applications/001-disaster-response/brief.md` slot-template should be populated with §2a + §2b + §2c of this arc-plan (the T0-visible scenario), with a statement that subsequent session inputs will arrive at each T0.
- `session-inputs/session-001-input.md` should contain §2a + §2b + §2c verbatim (duplication with brief.md acceptable — the session-input file carries T0 scope authoritatively).

For the **arc-end** (S005 close or later):
- Optionally copy this arc-plan (`provenance/047-session/arc-plan.md`) into the external workspace at `applications/001-disaster-response/arc-plan.md` for post-arc review by operators or future external-audit readers.
- Self-dev should run a post-arc triage session reading all S005 EF records and deciding adoption of the four deferred spec-amendment candidates from §10.

---

**Arc-plan ends.** This file is sealed at Session 047 close per D-017. Revisions to this plan happen in future self-dev sessions as new artefacts, not as edits to this file.
