---
session: 047
title: Outsider / Feedback-Yield Reviewer: optimise the arc around hidden-state, invalidation, and validation-void failure surfaces
date: 2026-04-24
status: raw
perspective: outsider-feedback-yield
committed_at: <will be filled in by committer>
---

## Position summary

My position is that the external application should be designed less like a plausible disaster-response exercise and more like a controlled engine-instrumentation rig. The scenario only needs enough fictional coherence to let sessions make decisions; its real job is to expose what the engine assumes about visibility, validation, state continuity, and artefact authority. The highest-yield design is therefore a five-session partial-information arc where each session sees only its local brief, commits assumptions and plans, and then the next session receives an operator-injected constraint update that invalidates a load-bearing prior assumption without editing closed provenance.

The full arc-plan should **not** live in the external workspace default-read surface. I recommend approach **(a) plus (c)** from brief §2.5: the authoritative complete plan lives in the self-development workspace as the orchestrator record; the external workspace receives only per-session reveal files at T0. This directly tests the engine's under-specified handling of non-visible scope. It also exposes a specification ambiguity I do not see named strongly enough in §2: `read-contract.md` §1 defines a closed default-read surface that does not enumerate `applications/`, while `prompts/application.md` §Read instructs external sessions to read `applications/`. The hidden-arc constraint turns that ambiguity from harmless prose drift into an operational question.

The frame-level property the disaster scenario makes visible is: **Selvedge does not yet model epistemic partitions**. It has workspace state, archive state, and application state; it does not clearly model "operator-known but session-hidden scenario truth" as a first-class state.

## Q1 — Scenario at T0 + arc structure

**Placement approach:** use **self-dev authoritative plan + operator-transported per-session reveals**. The full plan should live only in the self-development workspace, preferably as a Session 047 design artefact such as `applications/001-disaster-response/arc-plan.md` in the self-dev workspace or as a preserved provenance attachment in `provenance/047-session/`. The external workspace receives `applications/001-disaster-response/session-00N-input.md` only when Session N opens. Those input files become visible thereafter and should never contain future reveals.

**T0 scenario:** The fictional setting is the **Laurel Delta**, a low-lying island-and-estuary district in the invented country of **Nivaro**. A late-season cyclone has crossed the delta and pushed brackish floodwater into three settlements: **Merrow Port**, **South Latch**, and **Kellan Rise**. Population affected: approximately 180,000-230,000 people. The population profile is deliberately mixed for planning stress: an older coastal population, a seasonal migrant workforce housed in low-quality dormitories, two hospitals, several dialysis and refrigerated-medication dependencies, and a dispersed fishing community with informal radio networks. No real geography or public disaster case is imported.

At Session 001 T0, the external team knows only: cyclone damage, flooding, partial road outage, uncertain power restoration, hospital continuity risk, shelter demand, and local government request for a 10-day response-and-stabilisation plan.

**Arc structure: five sessions.**

Session 001: build initial system model, assumption register, response objectives, and first-pass 72-hour plan. The point is to force the engine to record assumptions explicitly before it knows future constraints.

Session 002: coordination shock. A new operator brief reveals that the assumed unified local command is false: Merrow Port and South Latch answer to different emergency authorities, and a major relief NGO will not share beneficiary data. Objective: revise governance, decision rights, and coordination plan.

Session 003: infrastructure and communications shock. The main bridge is not merely damaged but unusable for three weeks; cellular restoration is delayed; satellite bandwidth exists but is rationed. Objective: re-plan logistics and communications under invalidated access assumptions.

Session 004: demand shock. Shelter demand doubles because upland temporary camps evacuate into the delta; cold-chain medical demand is higher than estimated; water contamination appears in two shelters. Objective: revise prioritisation and risk controls, including decision trees for scarcity.

Session 005: recovery and validation shock. The operator reveals that no domain actor and no reference case will be available; the final application must produce a bounded recovery-transition artefact and engine-feedback pack. Objective: close the arc, classify what is validated versus merely internally coherent, and produce feedback records.

## Q2 — Constraint-evolution mechanic + D-017-compliant retroactive-invalidation handling

Use a **pre-scheduled axis / emergent target** mechanic. The full self-dev arc-plan pre-schedules the axis for each transition: coordination, infrastructure/communications, demand, then validation/recovery. The exact assumption to invalidate should be selected by the operator from the prior session's committed assumption register. This matters: if the invalidated assumption is not one the session actually relied on, the exercise becomes theatre.

Delivery is by operator-injected `session-00N-input.md` at T0. Each reveal file should contain four short sections: `New Facts`, `Invalidated Prior Assumptions`, `Constraints for This Session`, and `Do Not Resolve By Editing Prior Sessions`.

D-017 compliance is straightforward if the arc is disciplined. Closed provenance is never edited; `workspace-structure.md` §provenance says errors or retractions are recorded in subsequent sessions. Current-session records point forward and backward. I recommend three visible external artefacts for this:

- `applications/001-disaster-response/assumption-register.md`
- `applications/001-disaster-response/supersession-ledger.md`
- `open-issues/OI-NNN.md` files when an invalidated assumption creates unresolved application work

The assumption register is a mutable application artefact per `workspace-structure.md` §applications. Each assumption gets an ID, source session, status, and, when applicable, `invalidated_by_session`. The supersession ledger records the narrative: "A-014 from Session 001 was invalidated by Session 003 reveal R-003 because..." The prior Session 001 provenance remains a historical witness.

If synthesis wants a spec amendment out of this, classify it carefully. Adding an **application-local assumption status** is minor/no engine change. Adding a new engine-level OI state such as `constraint-invalidated` is **substantive** under OI-002 because it adds normative state-machine content and likely required fields or lifecycle semantics.

## Q3 — Artefact progression

**Self-dev only:**

`applications/001-disaster-response/arc-plan.md` or equivalent Session 047 provenance attachment: complete orchestrator view, never copied into the external default-read surface until the arc is complete.

**External, visible from Session 001:**

`applications/001-disaster-response/brief.md`: T0-only application brief. Sealed after Session 001 except for explicitly recorded corrections.

`applications/001-disaster-response/session-001-input.md`: T0 reveal. Sealed once delivered.

`applications/001-disaster-response/system-model.md`: mutable. Frontmatter: `originating_session`, `last_revised_session`, `visible_from_session`, `validation_label`.

`applications/001-disaster-response/assumption-register.md`: mutable. Fields per assumption: `assumption_id`, `originating_session`, `status`, `depends_on`, `invalidated_by_session`, `current_disposition`.

`applications/001-disaster-response/response-plan.md`: mutable, with `supersedes` and `last_revised_session`.

`applications/001-disaster-response/risk-register.md`: mutable.

`applications/001-disaster-response/decision-trees.md`: mutable; each tree carries originating session and current applicability.

**External, added at later T0:**

`session-002-input.md` through `session-005-input.md`: sealed reveal files, visible only from their delivery session onward.

`supersession-ledger.md`: created Session 002, mutable through Session 005.

`validation-position.md`: created Session 005, sealed at close. It states exactly what claims the fictional exercise supports and does not support.

`engine-feedback/EF-00N-<slug>.md`: created when methodology friction is observed, using `workspace-structure.md` §engine-feedback schema.

Provenance remains sealed per session. Application artefacts are mutable in place because `workspace-structure.md` §applications explicitly permits later revision while provenance witnesses remain untouched.

## Q4 — Validation approach per session

Workspace validation always runs through `tools/validate.sh`, per `methodology-kernel.md` §7 and `validation-approach.md` §Two-Tier Model.

Domain validation is unavailable because there is no domain actor. Provisional reference substitute is also unavailable: the scenario is fictional and self-contained, and using a real reference case would change the exercise into a reference-validation exercise under `reference-validation.md`, which is outside scope.

The fallback should be named honestly as **qualitative scenario validation**, not as "validated" in the kernel §7 sense. Each session should use four perspectives:

- Response Planner: makes the best plan from visible facts.
- Constraint Skeptic: attacks assumptions, especially hidden dependency and brittle coordination.
- Stakeholder Simulator: reasons from one affected-group standpoint named in that session's brief.
- Engine Friction Recorder: watches for methodology breakdowns and drafts candidate feedback records.

The Case Steward synthesiser sits after raw outputs and before decisions, per `multi-agent-deliberation.md` §Synthesis. In the external sessions, the Case Steward must only see the external workspace state and the current reveal. The operator may know the full self-dev arc-plan, but the executing session should not.

Validation criteria should be concrete: internal coherence; cross-artefact consistency; every major decision tied to an explicit assumption; no future reveal leakage; every invalidated assumption dispositioned; risk register updated after each constraint update; local session objective complete without requiring future knowledge. This is not domain validation. It is a disciplined substitute that should probably generate engine feedback because kernel §7 does not currently name it.

## Q5 — Feedback-yield optimisation (primary target)

**Surface 1 — Hidden scenario / epistemic partition.** Exercised by Q1 placement and Q4 Case Steward scope. Expected feedback: `EF-001-hidden-scope-doneness.md` — "External sessions needed a local done criterion because the true arc scope was operator-known but intentionally not session-visible." Property surfaced: missing affordance in the kernel for non-visible scope and session completion under partial information.

**Surface 2 — Application-scope read ambiguity.** Exercised by placing full arc outside the external workspace and delivering per-session files into `applications/`. Expected feedback: `EF-001-application-scope-read-contract-ambiguity.md` — "`prompts/application.md` §Read treats `applications/` as read input while `read-contract.md` §1 closed enumeration omits it, making hidden application-scope content ambiguous." Property surfaced: unclear spec / contradictory authority boundary.

**Surface 3 — Retroactive invalidation without provenance edits.** Exercised by Q2 invalidating prior committed assumptions through current-session reveal files. Expected feedback: `EF-003-retroactive-invalidation-ledger.md` — "The arc needed an assumption supersession ledger and application-local invalidated status to avoid editing closed provenance." Property surfaced: missing standard pattern; D-017 is clear, but the forward-recording affordance is under-specified.

**Surface 4 — Kernel §7 validation void.** Exercised most strongly in Session 005. Expected feedback: `EF-005-qualitative-validation-label-gap.md` — "Fictional external artefacts had neither domain actor nor reference substitute; qualitative multi-agent checks were necessary but had no kernel validation label." Property surfaced: load-bearing gap / wrong abstraction around validation senses.

**Surface 5 — MAD minority lifecycle under invalidated premises.** Exercised by preserving dissent in Sessions 002-004 and then invalidating the premise for at least one dissent. Expected feedback: `EF-004-minority-under-invalidated-premise.md` — "MAD v4 preserves dissent but does not say how to classify a minority whose warrant depended on a later-invalidated scenario assumption." Property surfaced: missing lifecycle affordance across evolving external state.

**Surface deliberately not targeted:** real disaster-response domain adequacy. No practitioner, public standard, or real case is used. That is intentional: importing real domain validation would blur the engine-feedback experiment and expand scope into reference/domain validation design. The arc should surface engine behaviour, not claim emergency-management competence.

## Confidence and limits

I am highly confident that hidden-state handling, validation void, and retroactive invalidation are the best feedback-yield surfaces. I am less confident about exact file placement in self-dev because the brief's original default path and §2.5 amendment pull in opposite directions; synthesis should choose the concrete self-dev path. I assumed the operator can reliably prevent the external Case Steward from reading the full self-dev arc-plan.

Independence discipline note: I did not intentionally open other perspective raw outputs. However, while searching repository-wide for OI-002/specification material, tool output surfaced snippets from `provenance/047-session/01b-perspective-scenario-evolver.md`. That is an independence-phase contamination event under WX-44-1 discipline. I have not relied on that file as evidence, but the breach should be recorded.

§5.6 transparency: this P3 seat is Codex/GPT-family, and the brief states both non-Claude seats are Codex/GPT-5.5. The no-non-GPT-non-Claude concentration data point continues.

## Independent-claim evidence pointer

Participant manifest pointer to be recorded by the committer: `provenance/047-session/manifests/outsider-feedback-yield.manifest.yaml`.

Recommended manifest fields: `participant_kind: non-anthropic-model`; `participant_organisation: openai`; `provider: openai`; `model_family: gpt`; `model_id: <from Codex CLI startup metadata>`; `independence_basis: organization-distinct`; `training_lineage_overlap_with_claude: independent-claim` if the operator can support it, otherwise `unknown`; `training_lineage_evidence_pointer: unknown-but-asserted` unless the operator supplies a provider-public policy URL or workspace-internal note per `multi-agent-deliberation.md` §Layer 2.
