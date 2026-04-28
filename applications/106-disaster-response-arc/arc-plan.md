---
title: Arc-Plan v2 — selvedge-disaster-response external-application trial
authoring_session: 106
date: 2026-04-28
status: active
supersedes: provenance/047-session/arc-plan.md (S047 5-session v1)
external_workspace_pending: /Users/ericmccowan/Development/selvedge-disaster-response (to be re-bootstrapped at S107-S108)
synthesis_decisions: DV-S106-1 (arc structure) · DV-S106-2 (bootstrap scope) · DV-S106-3 (orchestration) · DV-S106-4 (hard reset) · DV-S106-5 (placement)
preserved_minority: M-1 (P-3 minimalist arc, S106 deliberation_id=9)
visibility: operator-only — do NOT copy into external workspace default-read surface
---

# Arc-Plan v2 — selvedge-disaster-response external-application

## §1 Summary

This is the authoritative arc-plan for executing the engine-v31 Selvedge engine against the **first genuine external-problem trial**. The trial runs in a freshly-bootstrapped external workspace at `/Users/ericmccowan/Development/selvedge-disaster-response/` (created at S107 / S108). The arc commits to **7 phases over 21 sessions** with adaptive extension to S022-S030 decided at the S021 retrospective on EF-yield evidence. Total upper bound: 30 sessions, satisfying the engine-v20 release gate from S078 D-5.

The previous arc-plan (S047 v1, 5 sessions / 4 reveals) was attempted and reached only 3 sessions before pause; those 3 sessions ran on engine-v7 with markdown-state and produced rich v1 baseline artefacts (system-model 645 lines, assumption-ledger 116 lines, response-plan 801 lines, risk-register 674 lines) but never reached any reveal phase. The empirical lesson: **3 sessions is the floor for landing v1 baseline artefacts**, not 1. This arc-plan v2 is sized to that empirical cadence.

### §1.1 Feedback-yield thesis

The trial is structured around **engine-surface stress**, not domain coverage. Each reveal phase exercises a distinct surface drawn from `specifications/constraints.md` §1-§6 — the six properties that drove the engine-v17 redesign. A reveal that is "different disaster-response stuff" without naming a distinct surface is decoration; the synthesis at S106 explicitly rejected the costume-of-the-same-surface arc shape (DV-S106-1 R-1.2; the cross-family P-2 critique that authority-conflict was the engine surface under the coordination/legal/political domain costumes).

### §1.2 Operator role

The operator holds this arc-plan; external sessions never see it directly. Per-session inputs are drafted from this arc-plan's per-phase stubs plus the live substrate state read from the external workspace via `bin/selvedge monitor-external next-input` (once S108 lands the tool). The operator transports each session-input into the external workspace, opens Claude Code there, and after the session closes, runs `monitor-external harvest-ef` to copy any engine-feedback records back into self-dev.

## §2 Scenario at T0 — what external S001 will see

### §2a Setting (re-used from S047 §2a; archived v7 brief.md is canonical source)

**Laurel Delta**, a low-lying island-and-estuary district in the invented country **Nivaro**. Three settlements: **Merrow Port** (~62K, working harbour + industrial fishery; one regional hospital ~450 beds), **South Latch** (~58K, agricultural plain, levee-dependent; dialysis centre serving ~1,200 patients), **Kellan Rise** (~80K, upland approach, mixed urban-residential; one secondary hospital ~280 beds). Total affected population ~200,000. Vulnerability profile per S047 §2b (~9% over 70; ~2.5% on powered medical equipment; ~1,200 dialysis-dependent in South Latch; migrant-worker dormitories near Merrow Port; dispersed estuary-islet fishing community on VHF only).

### §2b The disaster at T0

Late-season cyclone crossed Laurel Delta ~36 hours before S001 opens. Storm surge ~2.8m above mean high tide; lower Merrow Port and two-thirds of South Latch flooded; ~18,000 displaced; grid out across Merrow Port and South Latch (3-7 day partial restoration estimated); primary drinking-water plant compromised by salt-water intrusion; Merrow Port regional hospital on generator; freight rail bridge passable at reduced rating; one highway bridge intact at 24-tonne; sea and air access degraded. Local government has requested a **10-day response-and-stabilisation plan** that S001 will produce v1 of.

### §2c What external S001 must NOT see

- Any §3 phase content beyond P0.
- The reveal axes for P1-P6.
- The adaptive extension policy at S021.
- The existence of this arc-plan as a single document.

The operator drafts each `applications/001-disaster-response/session-inputs/session-NNN-input.md` per the per-phase stub in §3 and places it in the external workspace **only at that session's T0**.

## §3 Arc structure — 7 committed phases × 3 sessions

### §3a P0 — baseline (S001-S003)

**Pre-declared axis**: none (T0 is the baseline).

**Expected artefacts** (cumulative across the 3 sessions):
- `applications/001-disaster-response/system-model.md` (v1)
- `applications/001-disaster-response/assumption-ledger.md` (v1) — typed entries with stable IDs (`A-NNN`); reproduces or improves on the v7 ASM/POP/INF/SVC/DEP/EXT/SIL/CON/DEC/GIV/EXT-SURVEY taxonomy as the session warrants.
- `applications/001-disaster-response/response-plan.md` (v1) — 10-day response-and-stabilisation plan
- `applications/001-disaster-response/risk-register.md` (v1)

**Engine-surface mapping** (constraints §1, §5): does the engine-v31 substrate-canonical write path actually prevent the prose-state drift constraints §1 names, when the agent reaches for markdown tables for "structured-state" application work? Watch for whether the agent reaches for `bin/selvedge query` to count things or narrates counts in prose.

**Per-phase close criteria** (any session in the phase that closes):
1. Assumption-ledger has ≥12 numbered entries with status + originating evidence.
2. Cross-artefact citation: every load-bearing premise in response-plan.md cites an assumption ID.
3. Close-record `next_session_should` names the specific next baseline gap (or, if all four artefacts complete, transitions to P1).
4. ≥1 EF outbox file OR explicit close-note justifying non-production.

### §3b P1 — observability / ground-truth failure (S004-S006)

**Pre-declared axis**: **observability stress**. Field reports conflict: shelter counts disagree between local government and NGO census; medical-device-dependent count disagrees between harbour-authority dormitory registration and hospital pharmacy records; flood-depth maps disagree between satellite imagery and on-ground reports; road-access status changes between hours.

**Engine-surface mapping** (constraints §1 prose-state, §5 detection-without-feedback): does the assumption-ledger admit "active-with-conflict" status, or does the agent silently choose one source? Does the response-plan revision cite which conflict resolution drove which action change?

**Operator action at T0 of S004**: read external assumption-ledger v1; select ≥2 assumptions that are load-bearing for response-plan-v1 actions and could plausibly conflict. Draft session-004-input.md with new-facts (the conflict reveal), invalidated-prior-assumptions (the IDs), constraints, and a do-not-edit-prior-sessions clause. Use `bin/selvedge monitor-external next-input` to bootstrap the draft once S108 lands.

### §3c P2 — physical interdependency cascade (S007-S009)

**Pre-declared axis**: **dependency chain failure**. Freight rail bridge structurally compromised on aftershock; cannot reopen for ≥21 days. Fibre-optic trunk severed; Kellan Rise drops to microwave at ~5% prior bandwidth. Merrow Port port-side power substation flooded; dialysis centre cold-chain at 18-hour limit; satellite uplink rationed.

**Engine-surface mapping** (constraints §4 context-loss, §5 lesson-non-internalisation): does the system-model revision update v1's `INF-*` and `DEP-*` entries (or substrate-equivalent), or does the agent re-derive the dependency map from scratch losing the v1 IDs? Is the supersession traced or hidden?

### §3d P3 — scarcity / triage (S010-S012)

**Pre-declared axis**: **multi-axis allocation under scarcity**. Fuel for generators, potable water from rotation wells, generator parts (specifically transfer switches), medevac slots from Kellan Rise to provincial hospital, and satellite bandwidth ALL cannot be simultaneously satisfied. Each is enough alone; together they aren't.

**Engine-surface mapping** (constraints §2 failure-as-cheap, §3 cross-family blind spots): forces the engine to record value conflicts as first-class structure (substrate decision rows, not narrative paragraphs); cross-family perspective likely load-bearing here on whose triage frame is privileged.

### §3e P4 — authority conflict (S013-S015)

**Pre-declared axis**: **cross-stakeholder authority conflict** (folds S047's coordination + the operator's earlier-proposed legal/jurisdictional + political-fracture into a single phase). Port authority emergency declaration restricts civilian coordinator access to dock zones; provincial commissioner invokes Article X of the Nivaro Civil Protection Act claiming command precedence; central government emergency coordinator's authority contested; the Northern Basin Relief Foundation refuses to share beneficiary data citing donor-confidentiality policy.

**Engine-surface mapping** (constraints §3, methodology §When to convene multiple agents): does the deliberation actually convene cross-family on this phase, or does it default to single-family? The S047 plan named cross-family at every phase; the synthesis here recommends cross-family **at minimum at P4 and P6**, more often if budget allows.

### §3f P5 — secondary hazard / temporal reframing (S016-S018)

**Pre-declared axis**: **scope-boundary stress**. Aftershock landslide closes the Kellan Rise highway approach; sewage outbreak in two shelters; responder fatigue at 14 days. The plan was a 10-day response plan; the system is now in week three and operating against a stale frame.

**Engine-surface mapping** (constraints §4, §5): does the response-plan supersede cleanly to a recovery-plan, or do the two coexist and contradict? Does the assumption-ledger reflect that "10-day window" is now a superseded constraint?

### §3g P6 — validation-meta + EF synthesis (S019-S021)

**Pre-declared axis**: **validation-meta**. Operator reveals: no domain-actor will ever validate this scenario; no reference case exists. The arc was designed from the self-development workspace to produce engine-feedback.

**Engine-surface mapping** (constraints §3, §6): does the synthesis honestly classify what the artefacts validate vs merely cohere around? Does the retrospective name engine-v31-specific frictions, or default to safe-language self-praise?

**Expected artefacts**:
- `applications/001-disaster-response/recovery-plan.md` (v1, bounded transition only)
- `applications/001-disaster-response/validation-position.md` — declares per-artefact validation sense
- `applications/001-disaster-response/retrospective.md` — cross-session observations  
- ≥6 engine-feedback substrate rows (or files in `engine-feedback/` if the substrate kind is unavailable in external) covering the arc; ≥3 of these must be ≥250 words with concrete evidence pointers.

**Per-phase close criteria** (S021 specifically):
1. Validation-position artefact exists and explicitly states each artefact class's validation sense.
2. ≥6 EF records produced across the arc (cumulative).
3. Retrospective identifies ≥2 surfaces where the arc's validation **did not** catch a weakness a different validation shape would have.
4. **S021 retrospective decides whether to extend to S022-S030** per §3.5.

## §3.5 Adaptive extension policy (S022-S030)

The arc commits 21 sessions; sessions 22-30 are **extension-on-evidence**. At S021 close, the self-dev workspace runs a triage session reading all S006-S021 EF records and decides:

- **Extend** if EF-yield-per-session in S016-S021 averaged ≥0.5 substantive (≥250-word, evidence-pointered) records AND ≥3 distinct engine-surfaces remain unexercised. Extension activates **at most 3 candidate phases** from the deferred candidate list (§3.5.1) at 3 sessions each (max 9 → S030).
- **Close at 21** if EF-yield is below threshold, or if all candidate engine-surfaces have been exercised, or if the M-1 minority activated earlier (see §10).

### §3.5.1 Deferred candidate phases (extension only)

These phases were considered at S106 and deferred for S021 retrospective re-evaluation:

- **P-X1 economic frame**: insurance withdraws coverage; layoffs at Merrow Port industrial fishery; central government funding bottleneck. Engine surface: constraints §2 (substrate refusing mismatched effects).
- **P-X2 longitudinal closure**: 90-day milestone; assumptions vindicated/abandoned; recovery-transition formal handoff. Engine surface: constraints §5 (early-phase minority disposition honesty across long arc).
- **P-X3 operator-subtraction**: per P-2's adaptive-extension proposal — three sessions auditing accumulated arc ceremony and removing it. Engine surface: constraints §6 (subtraction role with authority to remove).

## §4 Evolution mechanic (70/30 hybrid, retained from S047 §4)

**Pre-declared (70%)**: each phase's axis is fixed in §3 of this plan. Each transition has a magnitude range defensible from the scenario.

**Emergent (30%)**: the specific assumption(s) invalidated at each transition are selected by the operator at session-open after reading the prior session's substrate state. The invalidated assumption must be one the prior session actually made load-bearing.

This hybrid prevents pre-scheduled-only (constraint change irrelevant to what the session committed to) and pure-emergent (operator may retcon at each transition).

## §5 Substrate-canonical invalidation mechanism (engine-v31 update)

D-017 is unchanged: closed provenance is immutable. The three parts S047 §5 named live in the external workspace's substrate (engine-v31) plus mutable application-scope artefacts:

- **Assumption ledger** is an application artefact (markdown under `applications/001-disaster-response/`) carrying typed rows with stable IDs (`A-NNN`); status moves from `active` → `superseded`/`invalidated`/`still-active-after-review` are tracked **in the artefact**, not in the substrate's `decisions_v2` rows (those record session decisions that drove the status change).
- **Supersession ledger** is an application artefact appending one row per supersession event (event-id, session, invalidated-assumption-id, invalidating-input-path, superseding-content-anchor, OI-reference).
- **Supersession-marker issue** uses the engine-v22+ `issues` substrate table directly; alias `OI-S<wno>-<seq>`; status `open`; `surfaced_session_id` set; body atom names the verbatim invalidated assumption text and the invalidating-input pointer.

## §6 Per-session validation approach

**Per-session deliberation cadence** (engine-v31 methodology §When to convene multiple agents):

- P0 baseline (S001-S003): convene multi-agent on at least S001 (initial system model is methodology-touching; cross-family at P0 is recommended-not-required).
- P1-P5: convene per-session at operator discretion based on the session's load-bearing claim. **Cross-family deliberation required at P4 (authority-conflict, kernel §3 single-family hides shape-of-question biases) and P6 (validation-meta synthesis)**.
- P6 (S019-S021): 4-perspective two-family minimum, mirroring S047 S005 and S106 itself.

**Validation senses** (engine-v31 methodology v4):
- **Workspace validation**: every session.
- **Domain validation**: not available (no domain-actor exists for this fictional scenario); per `prompts/application.md` §2-9, application artefacts carry `validation: reference-provisional` or equivalent.

## §7 Anti-laundering close-criteria (cumulative across all phases)

Each session's close-record must verify:

1. **Failed/strained criteria recorded**: every close lists ≥1 strained or failed validation criterion OR explicitly justifies why every criterion passed cleanly. Zero strains across the arc is laundering signal.
2. **Mutable-artefact revision traceability**: every revision after S001 cites the triggering session-input and updates the supersession-ledger.
3. **Cross-session touch**: every session after S001 names ≥1 prior assumption/artefact-section/issue/minority that was preserved/revised/superseded/invalidated.
4. **Reveal-session assumption action**: P1-P5 sessions mark ≥2 assumption IDs as `superseded`/`invalidated`/`still-active-after-review` AND name ≥1 artefact section changed.
5. **EF outbox production**: every session produces ≥1 EF outbox record OR a close-note explicitly justifying non-production.
6. **EF record substance**: each EF file ≥250 words with ≥1 concrete evidence pointer (substrate query, file path, atom ID, session-input path, or close-record claim).
7. **Minority-lifecycle audit** (P3 onward): if any prior preserved minority's factual premise is touched by current-session reveal, close explicitly records vindicated/obsoleted/preserved-unchanged disposition.

## §8 Targeted engine-feedback surfaces (mapped to constraints, not domain)

Each phase has a primary surface from constraints.md and a draft EF filename. External sessions producing EF records use these filenames or close-equivalents.

| Phase | Primary surface (constraints.md §) | Draft EF filename |
|-------|-----------------------------------|-------------------|
| P0 | §1 prose-state, §5 detection-without-feedback | `EF-P0-substrate-vs-prose-state-discipline.md` |
| P1 | §1, §5 (active-with-conflict ledger status) | `EF-P1-conflict-status-ledger-gap.md` |
| P2 | §4 context-loss, §5 ID-preservation | `EF-P2-dependency-id-preservation.md` |
| P3 | §2 failure-as-cheap, §3 cross-family value-conflict | `EF-P3-value-conflict-substrate-shape.md` |
| P4 | §3 single-family blind spot | `EF-P4-cross-family-load-bearing.md` |
| P5 | §4, §5 supersession-vs-coexistence | `EF-P5-temporal-reframe-supersession.md` |
| P6 | §3, §6 self-perception under load | `EF-P6-validation-meta-honesty.md` |

## §9 Vindication / refutation criteria (arc-end assessment)

**Vindication** (the arc exercised what it was designed to exercise):
- ≥4 non-duplicative EF records across the arc.
- No closed provenance was edited (`git log` check on `provenance/NNN-session/`).
- Every reveal changed or explicitly reaffirmed assumption IDs.
- ≥5 of the 7 §8 surfaces have a corresponding EF.
- `validation-position.md` exists and is honest.
- S021 retrospective produced an extend-vs-close decision with substrate-recorded reasoning.

**Refutation** (the arc drifted into ceremony):
- Fewer than 2 substantive EF records (pathway exercised but not meaningfully).
- Constraint updates appeared only as narrative notes; assumption statuses did not change.
- Preserved minorities were dropped without explicit disposition.
- Any closed-session provenance file was edited.
- Zero strains recorded in any close.

## §10 Preserved minority (M-1, P-3 minimalist)

P-3's case for closing the arc at S005-S006 with the original S047 4-axis subset is preserved as first-class minority. **Activation warrant**: if P0 (S001-S003) produces ≥3 substantive engine-feedback records — each ≥250 words with concrete evidence pointer (substrate query path, file path, atom ID), each naming engine-v31-specific friction NOT addressable as a routine OI — the operator may convene a S006 retrospective and close the arc early on the grounds that the engine has surfaced its weak surfaces inside the baseline alone. This is not a hedge; P-3's argument that "if 5 sessions of pressure cannot surface engine weakness, the engine is probably well-calibrated for problems of this shape" is load-bearing for whether the arc continues.

If M-1 activates, the next external arc must run against a different domain (constraints §6: external pressure as methodology requirement; repeating the same scenario assumes weaknesses are surface-by-axis rather than surface-by-domain).

## §11 Operator transport instructions

For each external session N (N≥4):

1. Read this arc-plan's per-phase stub (§3<phase-letter>) for the phase containing N.
2. Read the prior external session's substrate state via `bin/selvedge monitor-external status --workspace <external-path>` (once S108 ships).
3. Use `bin/selvedge monitor-external next-input --workspace <external-path> --phase <P-id>` to draft the session-input. Edit by hand; do not ship the tool's output verbatim.
4. Place the input file at `<external>/applications/001-disaster-response/session-inputs/session-NNN-input.md`.
5. Open Claude Code in the external workspace; PROMPT.md dispatches to `prompts/application.md` via MODE.md.
6. After the session closes, run `bin/selvedge monitor-external harvest-ef --workspace <external-path>` to copy any EF records into self-dev's `engine_feedback` substrate.

For the **first** external session (S001):
- Operator populates `applications/001-disaster-response/brief.md` from the archived v7 brief at `archive/v7-trial-2026-04-24-disaster-response/applications/001-disaster-response/brief.md`. The brief content is reusable; the v7 substantive artefacts (system-model, response-plan, etc.) are NOT inherited.
- `applications/001-disaster-response/session-inputs/session-001-input.md` carries §2a + §2b verbatim.

For the **arc end** (S021 close OR M-1 activation OR S030 final):
- Self-dev runs a post-arc triage session reading all EF records and deciding adoption of any deferred spec-amendment candidates.
- This arc-plan v2 is preserved at `applications/106-disaster-response-arc/arc-plan.md`; S106's session provenance carries the synthesis decision pointers.

---

**Arc-plan v2 ends.** This file is mutable across the arc. Revisions land as new self-dev sessions; each revision updates the frontmatter `last-revised-session` and adds an entry to a §0 revision log (created on first revision).
