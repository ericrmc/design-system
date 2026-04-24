---
session: 047
title: "Cross-family reviewer / realist: Feedback yield depends on anti-laundering gates, not scenario cleverness"
date: 2026-04-24
status: raw
perspective: cross-family-reviewer-realist
committed_at: "<will be filled in by committer>"
---

## Position summary

My position is that the arc-plan should be accepted only if it makes anti-laundering criteria first-class work, not after-the-fact audit prose. The external sessions will otherwise take predictable shortcuts: accept fictional facts as givens, mark constraint changes as “noted,” revise artefacts in place without naming what was invalidated, and close with useful disaster-response content but weak engine feedback. The plan should use a plain compound-disaster scenario because narrative novelty is not the yield source. The yield source is disciplined partial-view execution: hidden future constraints, explicit assumption IDs, forced retroactive invalidation records, and per-session engine-feedback outbox files.

I recommend a five-session arc. The full arc-plan should live in the self-development workspace only, with the operator transporting per-session reveal briefs into the external workspace at each session open. This is a hybrid of §2.5.3(a) and §2.5.3(c): complete orchestrator view in self-dev; accumulating partial view in the external application. The external workspace should not receive the full plan until after arc completion. The main measurable guard is this: every session after Session 001 must name at least one prior assumption, artefact section, OI, minority, or validation claim that was preserved, revised, superseded, or invalidated. If no such object is touched, the session did not exercise the intended engine surface.

## Q1 — Scenario at T0 + arc structure

Scenario: the fictional Greywater Basin is a low-lying coastal river district with one inland town, three smaller settlements, an industrial port, and dispersed rural communities. Present-day population is about 165,000. Vulnerabilities include an aging levee system, one regional hospital, two aged-care clusters, high seasonal-worker housing density near the port, limited private vehicle ownership in the south flats, and a single freight rail bridge that also carries a major fibre trunk. At external Session 001 T0, a severe rain-and-surge event has flooded the lower basin, damaged two bridges, displaced about 18,000 people, interrupted grid power in four zones, and created uncertainty about drinking-water safety.

Placement: the authoritative full arc-plan belongs in the self-development workspace, not the external workspace. The external workspace receives only `applications/001-disaster-response/session-inputs/session-00N-input.md` at each session T0. This follows `engine-manifest.md` §6’s separation between engine/application workspaces and the source workspace’s development-provenance, and avoids exposing future constraints through `prompts/application.md` §Read, which treats application scope as session input.

Arc:

Session 001: build the initial system model, assumption ledger, initial risks, and validation baseline under partial information.

Session 002: produce a response plan and decision tree after an infrastructure reveal invalidates a key mobility/logistics assumption.

Session 003: revise under a demand surge and coordination reveal that invalidates the prior command model.

Session 004: revise under communications degradation and misinformation constraints; explicitly audit minority positions and deferred OIs from Sessions 001-003.

Session 005: transition to recovery, close the scenario arc, produce a final supersession map, and write engine-feedback synthesis.

Laundering risk: the executing session may treat the fictional scenario as if it were a neutral domain brief and optimise for plausible emergency management rather than engine feedback.

Measurable guard: Session 001 close must include a table named `engine-surface-targets-exercised`, with at least three rows mapping scenario features to engine surfaces. If absent, the close is incomplete.

## Q2 — Constraint-evolution mechanic + D-017-compliant retroactive-invalidation handling

Delivery should be operator-injected constraint-update briefs. The arc-plan may pre-schedule the stress pattern, but each reveal should be written as a session-open input file and withheld until that session begins. Use a mixed mechanic: 70% pre-planned reveal, 30% emergent selection from prior outputs. The operator should choose which prior assumption to invalidate based on what the previous session actually made load-bearing.

Session 002 infrastructure reveal: the east bridge is unusable for ten days, not two; the fibre trunk on it is severed. This invalidates assumptions about rapid mutual-aid inflow and stable data links.

Session 003 demand and coordination reveal: a norovirus outbreak appears in two shelters, while the regional coordination authority is split between basin civil administration and a port-security emergency order. This invalidates shelter-density assumptions and single-command assumptions.

Session 004 communications reveal: mobile service becomes intermittent, radio channels are congested, and a false evacuation notice has moved people toward a closed road. This invalidates public-information assumptions and tests decision trees under degraded observability.

Session 005 recovery reveal: the flood recedes unevenly; water quality remains uncertain; political pressure shifts from life safety to reopening port operations. This invalidates the response/recovery boundary and tests session-level done-ness.

D-017 handling: do not edit closed provenance. `workspace-structure.md` §provenance says errors or retractions are recorded in subsequent sessions, not by editing past records. The external workspace should maintain a mutable `applications/001-disaster-response/assumption-ledger.md` with stable IDs like `A-001`, `A-002`, status values `active | superseded | invalidated | unresolved`, and fields `invalidated_by_session`, `invalidating_input`, `affected_artefacts`, and `prior_provenance_witness`. Each current session’s decisions record the invalidation, and prior session files remain untouched.

Spec-amendment classification: adding an official OI state transition `constraint-invalidated` would be substantive under OI-002, because it changes lifecycle semantics rather than clarifying wording. The external arc should not amend the engine in place; it should emit feedback.

Laundering risk: a session may say “constraints changed” and continue with a lightly revised plan.

Measurable guard: any session with a constraint reveal must mark at least two assumption IDs as `superseded`, `invalidated`, or explicitly `still-active-after-review`, and must name at least one artefact section changed because of that classification.

## Q3 — Artefact progression

External visible artefacts:

`applications/001-disaster-response/brief.md`: initial visible scenario only. Sealed after Session 001 except for a frontmatter pointer to later session inputs if local convention permits.

`applications/001-disaster-response/session-inputs/session-001-input.md` through `session-005-input.md`: operator-injected, sealed once delivered. Future files do not exist in the external workspace until their session opens.

`applications/001-disaster-response/system-model.md`: created Session 001, mutable. Fields: `originating_session`, `last-revised-session`, `supersedes`, `active_assumption_ids`.

`applications/001-disaster-response/assumption-ledger.md`: created Session 001, mutable and central. This is the main anti-laundering artefact.

`applications/001-disaster-response/response-plan.md`: created Session 002, mutable through Session 005.

`applications/001-disaster-response/risk-register.md`: created Session 001, mutable. Must carry `risk_status` and `triggering_constraint_update`.

`applications/001-disaster-response/decision-trees.md`: created Session 002, mutable. Session 004 must revise it under communications degradation.

`applications/001-disaster-response/validation-ledger.md`: created Session 001, mutable. Records validation criteria and which criteria failed or changed under reveals.

`engine-feedback/EF-00N-<slug>.md`: external outbox records under `workspace-structure.md` §engine-feedback. These are visible in the external workspace and operator-transported to self-dev inbox later.

Self-dev-only artefact: full arc-plan and reveal schedule. It may be preserved in S047 provenance or a self-dev application artefact, but it must not be copied into the external workspace before Session 005 close.

File-edit claim: executing sessions are expected to edit the mutable files above; this should be verifiable with `git log -- applications/001-disaster-response/assumption-ledger.md` and equivalent paths. Prior provenance copies are not edited.

Laundering risk: in-place mutable artefacts can erase why a change occurred.

Measurable guard: every mutable artefact revision after Session 001 must update `last-revised-session` and include a `supersedes` or `change_reason` entry naming the session input file. If an artefact changes without such a pointer, the revision is suspect.

## Q4 — Validation approach per session

Use four perspectives per external session when feasible: Operations Planner, Infrastructure/Logistics Critic, Affected-Population Advocate, and Laundering Auditor. The fourth role is mandatory because `multi-agent-deliberation.md` §Perspectives requires adversarial coverage, and this arc’s main failure mode is ceremonial compliance.

Validation cannot be Domain validation because there is no domain actor. It also cannot honestly be Provisional reference substitute because the fictional scenario has no sealed proven solution; `methodology-kernel.md` §7 makes that substitute dependent on a staged constraint tranche and comparison reference. The replacement should be labelled `validation: qualitative-internal` or similar, while also producing engine feedback that this label is not codified in kernel §7.

Criteria:

Internal coherence: no response action relies on an invalidated assumption.

Cross-artefact consistency: system model, plan, risks, and decision trees use the same assumption IDs.

Traceability: every major recommendation traces to a visible session input or explicit hypothesis.

Constraint-impact accounting: each reveal names affected assumptions and artefact sections.

Adversarial sufficiency: the Laundering Auditor must state whether the session produced real engine-feedback evidence or only domain-work output.

The Case Steward synthesiser sits after raw perspectives and before Decide. The synthesiser may map convergence and dissent but should not invent validation evidence. Per `multi-agent-deliberation.md` §Synthesis, synthesis maps rather than decides.

Laundering risk: validation becomes self-certification by the same agent that wants to close.

Measurable guard: each session’s `03-close.md` must list failed or strained validation criteria, not only passed criteria. A close with zero strains across five sessions is evidence of laundering, not success.

## Q5 — Feedback-yield optimisation (primary target)

Targeted surfaces:

1. Hidden-scenario handling and partial-view done-ness. Exercised by Q1 placement and per-session reveal files. Expected feedback: `EF-001-hidden-scope-doneness` — the application prompt lacks a clean way to distinguish “session done under current reveal” from “arc done.” Property surfaced: load-bearing gap in session-close semantics under non-visible future scope.

2. Kernel §7 validation void. Exercised by Q4’s qualitative validation fallback. Expected feedback: `EF-001-qualitative-validation-gap` — fictional, no-domain, no-reference applications need a named validation label and criteria. Property surfaced: unclear spec / missing affordance.

3. D-017 retroactive invalidation. Exercised by Q2 assumption ledger and current-session-only invalidation records. Expected feedback: `EF-002-retroactive-invalidation-d017` — closed provenance remains immutable, but mutable application artefacts need explicit supersession markers. Property surfaced: wrong abstraction boundary between provenance immutability and artefact mutability.

4. OI lifecycle pressure. Exercised by OIs opened on assumptions that later become irrelevant. Expected feedback: `EF-003-oi-constraint-invalidated-state` — open/resolved/deferred is insufficient when an issue is made obsolete by a later constraint reveal. Property surfaced: missing state transition.

5. MAD minority preservation under invalidation. Exercised by Session 004’s audit of earlier minority positions. Expected feedback: `EF-004-minority-after-invalidated-premise` — the engine preserves dissent, but does not say how to classify preserved dissent whose factual premise is later invalidated. Property surfaced: load-bearing gap in cross-session dissent lifecycle.

6. Engine-feedback outbox first-use friction. Exercised every session. Expected feedback: `EF-005-feedback-outbox-operability` — the outbox path works only if sessions are forced to write specific feedback rather than deferring methodology observations. Property surfaced: rigid or under-instrumented convention.

Deliberately not targeted: actual disaster-response domain validity. No practitioner, jurisdiction, or real emergency standard is being consulted. That is acceptable because this arc is for self-development feedback, not field readiness.

Laundering risk: sessions may create the named EF files with thin prose to satisfy the plan.

Measurable guard: each EF file must contain at least one concrete evidence pointer to a session input, artefact diff, OI, or close-section claim, plus a statement of application-scope disposition. Minimum useful body length should be 250 words; shorter records need a close-note justification.

Feasibility: five sessions is executable if artefact count is capped and each session has one primary reveal. The over-specification risk is a plan that dictates all invalidations regardless of what prior sessions actually made important. The under-specification risk is leaving the operator to improvise all reveals. The 70/30 mechanic above is the workable middle.

Vindication criteria at arc end: at least four non-duplicative EF records exist; no future reveal was visible before its session; every reveal changed or explicitly reaffirmed assumption IDs; no closed provenance was edited; and Session 005 can produce a supersession map from Session 001 assumptions to final artefacts.

Refutation criteria: fewer than two substantive EF records; constraint updates only appear as narrative notes; no assumption statuses change; minority positions are dropped without disposition; or the operator has to explain arc coherence outside the workspace because the artefacts do not show it.

## Confidence and limits

Confidence is moderate. I am confident about the laundering risks because they follow directly from the engine surfaces named in the brief and from the spec boundaries in `methodology-kernel.md` §7, `workspace-structure.md` §provenance and §engine-feedback, and `multi-agent-deliberation.md` §Synthesis. I am less confident about exact file placement because the prompt/application read language and read-contract enumeration appear to create pressure around whether `applications/` is default-read in all contexts. The hidden-scenario constraint makes that ambiguity useful feedback rather than a blocker.

I did not read other perspectives’ raw outputs. During file discovery, I observed that other perspective filenames existed in the session directory, but I did not open or inspect their contents. I treat that as no substantive WX-44-1 independence breach, with the caveat that filename visibility occurred.

Per §5.6, both non-Claude seats are Codex/GPT-family in this session. That continues the GPT-family-concentration worst-case-side data point and should not be laundered as broad non-Claude diversity.

## Independent-claim evidence pointer

Independence basis should be recorded through the Session 047 Layer 2 participant manifest required by `specifications/multi-agent-deliberation.md` §Heterogeneous-Participant Recording Schema, expected path `provenance/047-session/manifests/cross-family-reviewer-realist.manifest.yaml`. Relevant fields: `participant_kind: non-anthropic-model`, `provider: openai`, `participant_organisation: openai`, `model_family: gpt`, `invocation_method: cli-wrapper`, `independence_basis: organization-distinct`, and `raw_response_file` pointing to this output. Per the brief’s WX-44-2 instruction, `model_id` should be verified from the Codex CLI startup metadata in the raw-output log, not copied from prior sessions.
