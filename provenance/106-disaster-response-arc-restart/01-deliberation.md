---
session: 106
title: disaster-response-arc-restart — deliberation
generated_by: selvedge export
---

# Deliberation

## D-9 — Disaster-response arc-plan v2 + bootstrap rebuild + orchestration design

sealed_at: 2026-04-28T05:09:43.994Z

### P-2 (openai)

**Position.** Reject 9-phase 30-session shape as gate-fitting; use engine-surface-mapped 6 stress + meta arc, ~18-21 sessions, with explicit extend-to-30 only on non-ceremonial EF yield.

**schema_sketch.**
- Recommended v2 shape: 7 phases x 3 sessions = 21 sessions, with checkpoints after S012 and S018.
- Phase 0 S001-S003 baseline rebuild: produce system model, assumption ledger, response plan, risk register, response/recovery boundary.
- Phase 0 exists because v7 empirically needed 3 sessions just to land S001-class artefacts before any reveal.
- Phase 1 S004-S006 observability/ground-truth failure: shelter counts, medical census, flood maps, road status disagree.
- Phase 1 engine surface: assumption provenance, uncertainty accounting, refusing to launder incomplete evidence into plan certainty.
- Phase 2 S007-S009 physical interdependency cascade: bridge plus fibre plus port power plus dialysis cold-chain coupling fails.
- Phase 2 engine surface: system-model revision, dependency traceability, cross-artefact consistency.
- Phase 3 S010-S012 scarcity/triage: fuel, water, generator parts, medevac slots, satellite bandwidth cannot all be satisfied.
- Phase 3 engine surface: value conflict, rejected alternatives, stakeholder-facing rationale, non-prose decision structure.
- Phase 4 S013-S015 authority conflict combines coordination, legal/jurisdictional, and political fracture unless engine surfaces differ.
- Phase 4 reveal: port authority, provincial commissioner, central coordinator, and NGO data policy conflict.
- Phase 4 engine surface: cross-stakeholder authority conflict, dissent preservation, supersession without retroactive editing.
- Phase 5 S016-S018 secondary hazard / temporal reframing: landslide, contamination, heatwave, disease, or industrial spill.
- Phase 5 changes response into recovery while earlier artefacts still drive action.
- Phase 5 engine surface: scope boundary, assumption lifecycle, response-to-recovery transition.
- Phase 6 S019-S021 validation/meta synthesis: no domain actor, no reference case; classify validation versus mere coherence and harvest EF.
- Phase 6 engine surface: constraints section 3 cross-family blind spots and section 5 lesson non-internalisation.
- If release gate insists on 30, add S022-S030 only as adaptive extension, not nine pre-planned reveals.
- Adaptive extension shape: 3 sessions adversarial audit, 3 sessions operator-subtraction/ceremony removal, 3 sessions external replay.
**cli_surface.**
- Propose a thin monitor-external tool, not a dashboard.
- Status subcommand: takes workspace path, returns JSON with workspace id, engine version, sessions closed, latest close timestamp.
- Status JSON also includes open issues, EF outbox count, validation status, and latest git head.
- Next-input subcommand: reads arc-plan plus assumption ledger and close exports given workspace, arc, phase id, and out path.
- Next-input outputs draft session input with phase, reveal axis, candidate assumptions, and required operator fill; must not silently choose reveal.
- Harvest-ef subcommand: reads EF records given workspace, target self-dev path, since-session, and dry-run flag.
- Harvest-ef outputs substrate submit engine-feedback JSON payloads or a refusal report.
- This tool is load-bearing only if it reduces constraints section 4/5 context loss and transport errors; if it becomes status theater, delete it.
**migration_path.**
- Archive the v7 disaster workspace as evidence, not substrate.
- Keep v7 artefacts available as empirical witness: 3 sessions produced baseline artefacts and no reveals.
- Do not inherit the v7 response plan into the new workspace.
- Create a fresh v31 external workspace with a rebuilt bootstrap script.
- Bootstrap copies only active engine-definition files, CLI package, migrations, hooks/settings for PreToolUse, and validate.sh.
- Bootstrap then runs selvedge init, writes MODE.md, creates applications/001-disaster-response/brief.md and session-inputs/, leaves provenance empty.
- Place active arc v2 at applications/001-disaster-response-arc/arc-plan.md.
- In provenance/106-session/ record the decision, rejected alternatives, and a snapshot/hash/pointer.
- D-017 makes provenance bad for mutable planning, so arc-plan stays in applications, not provenance.
**what_not.**
- Do not split coordination, legal, jurisdictional, and political fracture into four reveals unless each has a distinct engine-surface hypothesis.
- Otherwise those four splits are just costumes for authority conflict.
- Do not run headless subprocess orchestration; it attacks operator workload but adds machinery before proving the work needs it.
- Headless orchestration worsens constraints section 6 violations.
- Do not treat 30 as epistemically justified; it is a release gate number, not yet an evidence-yield curve.
- Do not migrate v7 artefacts into the canonical new workspace; that imports obsolete engine assumptions and contaminates the baseline.
**open_question.**
- Is the 30-session gate operator-fixed, or can 21 plus evidence-based extension/refusal satisfy the intent?
- Does v31 have a substrate-native place for application artefact state, or will application artefacts remain markdown while session state is substrate-only?
- What EF-yield threshold ends the arc: EF count, novelty of EF class, or operator judgment?
**risk.**
- This position may under-exercise domain variety; a smaller arc could miss disaster-response-specific issues.
- Issues a separate legal or political reveal would surface might be missed by combining authority sub-types in one phase.
- The thin monitor may miss drift that a richer orchestration layer would catch.
- If the release gate is non-negotiable, arguing against 30 may create process friction even if technically correct.
**what_lost.**
- Adopting this loses the rhetorical neatness of a 30-session, 9-phase plan.
- It loses continuity with rich v7 artefacts.
- It loses the chance to test full automation early.
- The trade is deliberate: less ceremony, cleaner evidence, and fewer duplicate stressors.

### P-3 (anthropic)

**Position.** Subtract aggressively: 5-6 sessions not 30, pure operator transport (no monitor-external), hard reset of v7, bootstrap copies engine files plus init only; each new reveal axis is a hypothesis to remove.

**schema_sketch.**
- A 5-session arc, indexed against actual v7 evidence rather than an aspirational session-count.
- S001 produces system + ledger + plan v1, replicating what v7-S001/002/003 took three sessions to produce; v7 artefacts are the brief, not workspace state.
- If S001 cannot land v1 in one session under engine-v31 substrate-only writes, that slip is itself the most valuable engine-feedback the trial can produce.
- The arc extends S001 rather than absorbing slip into a 30-session budget.
- S002 is the coordination reveal (S047 §3b unchanged); S003 is infrastructure+comms reveal (S047 §3c unchanged).
- S004 is demand reveal (S047 §3d unchanged); S005 is validation-meta plus EF synthesis (S047 §3e unchanged).
- This is S047 original arc executed against engine-v31; S047 was deliberated by four perspectives across two model families with ceiling of five reveals.
- Adding four new axes inflates the design without naming what current-engine surface those reveals are hypothesised to exercise.
- Each new axis needs its own §8-style draft EF filename and surface-thesis before it earns a session; no one-sentence surface thesis means the axis is decoration.
**cli_surface.**
- None. No monitor-external, no harvest-ef, no orchestrator subcommand.
- The operator transports session-input files, reads close records, and copies engine-feedback files between workspaces by hand. Five round-trips.
- The v7 SESSION-LOG records that 3 round-trips happened; 5 is not a coordination problem the substrate needs to solve.
- Tooling is paid for in capability the operator cannot achieve manually; at five sessions, cp and a text editor suffice.
- If an arc-end retrospective reveals a specific operator-pain point that automation would relieve, the next external arc earns the tool.
- This is the constraints §6 subtraction discipline applied at a tool-acquisition decision.
**migration_path.**
- Archive /Users/ericmccowan/Development/selvedge-disaster-response/ into archive/v7-disaster-response-attempt/ in the source workspace.
- Hard reset, but not because v7 artefacts are unsalvageable; the operator-load to migrate them across the v7-to-v31 substrate boundary is real.
- The artefacts remain good source material in their archived state.
- Write a single-purpose bootstrap script at tools/bootstrap-v31-application.sh that creates target tree (engine-definition dirs only).
- Bootstrap copies PROMPT.md, prompts/application.md, prompts/development.md, four specs, tools/validate.sh, selvedge/, bin/selvedge, state/migrations/.
- Bootstrap runs bin/selvedge init, seeds workspace_metadata with mode/workspace-id/application-brief pointer, writes MODE.md.
- Bootstrap writes a one-line empty applications/001-disaster-response/brief.md for the operator to populate. Stop there.
- Operator drafts the application brief from the archived v7 artefacts; the brief carries the scenario; the arc-plan is operator-held.
- Place arc-plan at applications/001-disaster-response/arc-plan.md (mutable); operator-held only, not transported into external workspace until S005.
- Run S001 through S005; each session: operator drafts session-NNN-input.md, opens Claude Code in external workspace, reads outputs, transports EF outbox by cp.
**what_not.**
- Not an aliases.yaml seed; the v7 retrieval substrate was deprecated by engine-v20 substrate-only writes; carrying it forward replicates drift S047 was authored against.
- Not a .mcp.json; Claude Code standard tool surface plus bin/selvedge is sufficient; an MCP retrieval server is unpaid-for ceremony at 5 sessions.
- Not a tools/build_retrieval_index.py or tools/retrieval_server.py copy; substrate is canonical; bin/selvedge query is the read path.
- Not a slot-templated brief.md; the v7 bootstrap generated one with seven placeholder slots; the operator writes the brief from archived v7 artefacts.
- A template biases what gets written.
- Not an engine-feedback/outbox/README.md that re-explains the EF schema; prompts/application.md already documents the schema and an extra README is duplicate authority.
- Not a --monitor-external or --harvest-ef flag on selvedge; no monitor-external tool until two consecutive arc retrospectives independently surface operator pain.
- Not the four new reveal axes; each is a hypothesis; each needs a one-sentence surface thesis before it earns a session.
- Not a 9-phase x 3-session shape; the 30 sessions target is anchored on the engine-v20 release-gate number, itself a sticky number from S078.
- If 5 sessions of disaster-response produces all the EF the engine can productively triage, sessions 6-30 are ceremony.
**open_question.**
- Is the engine-v20 release-gate 30 sessions number itself revisable in light of empirical EF-yield-per-session, or is it a hard count the operator holds for independent reasons?
- If the 30-session count is hard, the gate is itself a methodology bug.
- After S005 EF synthesis, what is the operator actual decision-rule for another arc warranted vs the engine is now load-bearing on real problems?
- The arc can produce feedback indefinitely; the trial has to terminate on a criterion.
- If S001 fails to land v1 in one session, is the right response to extend S001, re-shape into a v7-style 3-session warm-up, or treat the slip itself as the trial primary EF?
- My position is that the slip itself is the primary EF, but the operator may have a different reading.
**risk.**
- The strongest counter is that 5 sessions produces too few reveals to differentiate engine handles disaster-response well from engine has not yet been pressed at its weak surfaces.
- My answer: that is the right risk to take first.
- If 5 sessions of pressure on coordination, infra+comms, demand, and meta-validation cannot surface engine weakness, the engine is probably well-calibrated for problems of this shape.
- If 5 sessions cannot surface weakness, the next trial should be a different domain.
- Repeating the same scenario assumes weaknesses are surface-by-axis rather than surface-by-domain; constraints §6 cuts the other way.
- Subtracting the monitor-external tool means each round-trip costs operator attention; at 5 round-trips this cost is bounded.
- If the operator reports round-trip cost as the binding constraint at S005 retrospective, build the tool then with empirical sizing.
**what_lost.**
- The richest loss is the synoptic 30-session record itself.
- A 30-session arc produces a body of work large enough to triage second-order patterns: recurring failure shapes across multiple revisions of the same artefact, not just per-session frictions.
- A 5-session arc cannot produce that synoptic record.
- Second-order pattern discovery is deferred until the engine has run against a different domain and cross-domain comparison becomes available.
- This is a real loss; my reading is that constraints §6 growth without external pressure produces internal elaboration applies more strongly than hypothetical second-order yield.
- The 75-session run already established the engine cannot cleanly self-develop past internal elaboration without external falsification.
- Repeating that pattern in an external workspace by inflating session-count is the same trap with a different label.

### P-1 (anthropic)

**Position.** Adopt 9-phase x ~3-session arc (~27 sessions in 30-session gate); hard-reset v7 workspace; keep operator-as-transport; add light hybrid arc-driver tooling for status, input-gen, EF harvest.

**schema_sketch.**
- Phase P0 baseline (sessions 001-003) has no reveal axis (T0); produces system-model v1, assumption-ledger v1 (>=12 IDs), response-plan v1, risk-register v1.
- P0 matches v7 empirical floor: 3 sessions to land S001 artefacts, not 1 as S047 estimated.
- Phase P1 coordination (004-006) reveals governance fracture (port Article X; NGO refuses share); produces response-plan v2, decision-trees v1, supersession-ledger v1.
- P1 exercises constraints section 5: forces ledger-driven re-derivation rather than narrative drift.
- Phase P2 infra+comms (007-009) reveals rail bridge unusable 21d, fibre severed, satellite rationed; produces system-model v2, response-plan v3, comms-degraded branches.
- P2 exercises constraints section 1: forces typed assumption-row updates instead of narrative.
- Phase P3 demand surge (010-012) reveals upland evac +7.5k, cold-chain low, shelter contamination; produces recovery-plan v1, response-plan v4, OI-disposition audit.
- P3 exercises constraints section 6: forces minority-lifecycle audit on early-phase dispositions.
- Phase P4 political reframe (013-015) reveals central govt curtailment, aid corridor politicised; produces governance-model v2, plan v5 constrained-authority branches.
- P4 exercises constraints section 3: cross-family perspective is load-bearing here.
- Phase P5 secondary hazard (016-018) reveals aftershock landslide, sewage outbreak, responder fatigue; produces escalation-protocol, response-plan v6.
- P5 exercises constraints section 4: tests whether mid-arc context anchors back to original brief.
- Phase P6 economic frame (019-021) reveals insurance withdraws, layoffs, funding bottleneck; produces recovery-plan v2 funding-contingent branches.
- P6 exercises constraints section 2: forces substrate to refuse mismatched effects.
- Phase P7 longitudinal closure (022-024) reveals 90-day milestone with assumptions vindicated/abandoned; produces recovery-transition artefact, vindication map.
- P7 exercises constraints section 5: tests early-phase minority disposition honesty across the arc.
- Phase P8 meta-synthesis (025-027) reveals no domain actor and no reference case; produces validation-position.md, retrospective.md, >=5 EF outbox records.
- P8 mirrors S047s S005; this is the EF synthesis the arc was built to produce.
- Total arc is 8 reveals (P1-P8) plus P0 baseline = 27 sessions, leaving 3-session spare budget before the 30-session ceiling.
**cli_surface.**
- Add a new selvedge-side subcommand group bin/selvedge arc-driver, living in self-dev workspace only; never installed in external.
- arc-driver has exactly three subcommands: status, next-input, harvest-ef. Capping at three is structural to keep it a tool, not a driver.
- status subcommand takes --workspace path; reads external SQLite read-only and prints workspace_metadata, sessions tail, open issues count.
- status also prints last close_record next_session_should, EF outbox files mtime list, and current phase derived from session count.
- next-input subcommand takes --workspace and --phase; reads external assumption-ledger via substrate query and arc-plan.md phase stub.
- next-input selects 2+ candidate assumption IDs whose load-bearing flag is set, emits JSON with phase, target_assumption_ids, stub_path, and draft_facts from arc-plan.
- next-input output is JSON-by-default to feed the operator drafting buffer; operator reviews, edits, and places the file in the external workspace.
- harvest-ef subcommand takes --workspace and --since-session; reads external engine-feedback/outbox/*.md and copies into self-dev engine-feedback/inbox/.
- harvest-ef registers each harvested file as an engine_feedback row via submit engine-feedback and records the harvest in subtraction_log.
- The CLI does NOT execute the external session; it only produces inputs and harvests outputs, keeping operator-as-transport (constraints section 6) intact.
**migration_path.**
- Step 1 Archive v7: mv selvedge-disaster-response into complex-systems-engine/archive/v7-trial-2026-04-24-disaster-response/, then commit on self-dev side.
- Step 2 Rewrite bootstrap from scratch; the existing archive/pre-restart/tools/bootstrap-external-workspace.sh is engine-v7 era and unsalvageable.
- New bootstrap copies 4 specs (methodology, constraints, workspace, engine-manifest), PROMPT.md, prompts/application.md, bin/selvedge, selvedge package.
- Bootstrap also copies state/migrations/, tools/validate.sh, tools/hooks/refuse-substrate-md.py, and .claude/settings.json.
- After copy, bootstrap runs bin/selvedge init and writes MODE.md with mode=external-problem and application_brief=applications/001-disaster-response/brief.md.
- Step 3 Place arc-plan at applications/001-disaster-response-arc/arc-plan.md on self-dev side as mutable; bootstrap does NOT copy it into external (operator-only per S047).
- Step 4 Wire arc-driver as selvedge/cli.py subcommand with status, next-input, harvest-ef; the coding review loop applies to the implementation.
- Step 5 Run external sessions: operator drafts each session-NNN-input.md from arc-driver next-input output, runs Claude Code in external; on close, self-dev calls harvest-ef.
**what_not.**
- No headless subprocess orchestration (Option C); it removes the human reviewer that constraints section 6 names as non-optional.
- The arc-driver is a tool, not a driver; it never executes the external session itself.
- No migration of v7 artefacts forward; the 645-line system-model and 116-line assumption-ledger were produced under engine-v7 markdown-as-state.
- Migrating v7 artefacts into substrate-canonical engine-v31 would either smuggle prose-state in or require translation effort larger than re-deriving them honestly.
- No 5-session arc (S047 shape); the empirical floor is 3 sessions to baseline, so a 5-session arc with 4 reveals will not clear S002.
- No arc-plan at provenance/106-session/arc-plan.md sealed-only; S047 sealed plan was wrong about cadence and a sealed plan cannot revise.
- A mutable arc-plan at applications/.../arc-plan.md lets later self-dev sessions revise the arc when reality contradicts it, while D-017 keeps each session-input carve sealed.
**open_question.**
- Should the cross-family perspective be wired in at every reveal phase or only at P4 (political reframe) and P8 (meta-synthesis)?
- Trade-off: cost of cross-family perspective at every phase vs. constraints section 3 coverage if it only fires at P4 and P8.
- External applications/001-disaster-response/ artefacts are domain artefacts, not substrate-canonical surfaces; PreToolUse hook must not refuse markdown writes there.
- Does the bootstrap need a hook variant for external workspaces, or do we trust the existing path glob to exclude applications/?
- Is the engine-v31 substrate engine_feedback row capable of representing a multi-paragraph EF record, or does the EF outbox stay markdown-in-files until a substrate kind ships?
**risk.**
- Risk: arc-driver becomes orchestration; each next-input call is one more place where self-dev context drifts toward what the tool says vs what constraints surface needs.
- Mitigation for orchestration drift: cap arc-driver subcommands at three; refuse a fourth without an OI naming the friction that motivates it.
- Risk: hard-reset wastes v7 EF candidates; three sessions of friction-against-v7 is evidence about v31 only insofar as constraints recur.
- Mitigation for v7 EF loss: pre-bootstrap triage session reads v7 close records and harvests still-applicable items as engine-feedback rows.
- Risk: 27-session arc is budget-tight; if P0 takes 4 sessions instead of 3, the arc cannot complete inside the 30-session release gate.
- Mitigation for budget tightness: P8 collapses to 1 session if prior phases produced sufficient EF substance to synthesise.
**what_lost.**
- Hard-reset loses the rich v1 artefacts (645-line system model, 801-line response-plan) that the v7 trial produced over three sessions of cross-family deliberation.
- Those artefacts represented real work: ASM-19 splits, multi-view derivation, three sessions of substantive engagement that will not be preserved forward.
- The next trial restarts from the brief, not from those artefacts; P0 baseline is re-derived rather than inherited.
- An inheriting arc would reach P1 faster but carry forward prose-state assumptions that engine-v31 explicitly refuses, ending up faithful to neither substrate.
- The honest cost of hard-reset is named here so a future session reconsidering it can read the trade rather than relitigate it blindly.

### Synthesis

# S106 Deliberation Synthesis

Three perspectives — P-1 anthropic pragmatic-hybrid, P-2 openai cross-family adversarial, P-3 anthropic adversarial-minimalist — converged on four points, diverged on three, and the synthesis preserves one minority as activation-warranted.

## Convergence

**C-1 — Hard reset of the v7 workspace.** All three perspectives reject inheritance of v7 substrate-state. P-1 names the engine-version gulf (10 specs to 4; markdown-state to substrate-only; PreToolUse hook; T-30 review loop). P-2 names contamination of the baseline. P-3 names operator-load to migrate. Convergence point: archive v7 workspace, fresh bootstrap.

**C-2 — Bootstrap minimalism.** All three argue for trimming the engine-v7 bootstrap's accumulated cargo. P-3 names specific exclusions (no `aliases.yaml` seed, no `.mcp.json`, no retrieval substrate copy, no slot-templated brief). P-2 says "engine-definition + CLI + migrations + hooks/settings + validate.sh, then init". P-1 lists same files as P-2 plus `tools/hooks/refuse-substrate-md.py` and `.claude/settings.json` (the PreToolUse hook). The intersection — engine-definition + selvedge package + migrations + hook + settings + validate.sh + init + workspace_metadata seed — is the synthesis bootstrap scope.

**C-3 — Arc-plan placement is mutable, in `applications/`.** P-1 and P-2 explicitly. P-3 too (`applications/001-disaster-response/arc-plan.md`). The S047 sealed-in-provenance placement was tried and proved wrong about cadence; mutable placement lets later self-dev sessions revise the arc when reality contradicts.

**C-4 — No headless subprocess orchestration (Option C rejected).** All three name this. P-1 says it removes the human reviewer constraints §6 names as non-optional. P-2 says it adds machinery before proving the work needs it. P-3 implicitly via "pure operator transport".

## Divergence

**D-1 — Number of sessions.** P-3: 5 (S047 unchanged). P-2: 21 (7 phases × 3 sessions, with adaptive extension to 30 only on EF-yield evidence). P-1: 27 (9 phases × 3 sessions, sized to the 30-session release gate).

**Synthesis adopts P-2's adaptive shape**: commit to 21 sessions (7 phases × 3) as the floor; admit S022-S030 as adaptive extension decided at S021 retrospective on EF-yield criteria. This honours P-1's gate-anchoring concern and P-2's evidence-yield discipline simultaneously.

**D-2 — Number/shape of reveal axes.** P-3: 4 (S047 unchanged: coordination, infra+comms, demand, validation-meta). P-2: 6 (observability/ground-truth, physical interdependency cascade, scarcity/triage, authority conflict (folds coord+legal+political), secondary hazard/temporal reframing, validation/meta). P-1: 8 (P-2's six plus political reframe and economic frame as separate axes).

**Synthesis adopts P-2's engine-surface taxonomy.** P-2's argument is decisive: distinct engine surfaces > distinct domain flavours. P-1's split of coordination/political/legal into separate axes was domain-flavoured; collapsed into authority-conflict, the engine-surface mapping is honest. P-1's economic frame is genuinely distinct (forces substrate to refuse mismatched effects per constraints §2) and is preserved as a candidate axis for the adaptive S022-S030 extension.

**D-3 — `monitor-external` CLI.** P-3: none. P-1, P-2: thin three-subcommand (`status`, `next-input`, `harvest-ef`).

**Synthesis adopts the thin three-subcommand CLI**, named `monitor-external` per operator direction (P-1's "arc-driver" and P-2's "monitor-external" both proposed; operator preferred the latter as generalisable beyond this arc). Implementation deferred to S108 coding session, after bootstrap rebuild lands at S107.

## Minority preserved (first-class)

**M-1 — P-3 minimalist arc.** P-3's case for closing at S005-S006 if S001-S003 baseline produces shape-changing EFs is preserved with this **activation warrant**: if P0 (S001-S003) produces ≥3 substantive engine-feedback records — each ≥250 words with concrete evidence pointer (substrate query, file path, atom ID), each naming engine-v31-specific friction NOT addressable as a routine OI — the S021 retrospective may close the arc early at S006 with the original S047 4-axis subset. This is not a hedge; P-3's argument that "if 5 sessions of pressure cannot surface engine weakness, the engine is probably well-calibrated for problems of this shape" is load-bearing for whether the arc continues.

## Forward direction

S107 (coding): rebuild `tools/bootstrap-external-workspace.sh` per C-2 scope. S108 (coding): implement `bin/selvedge monitor-external status/next-input/harvest-ef`. S109 (coding or external-mediated): execute bootstrap, populate `applications/001-disaster-response/brief.md` from archived v7 source, hand off to operator for first external session. The arc itself begins as external workspace S001 once bootstrap is verified.


### Synthesis points

- **convergence C-1.** All three perspectives agree on hard reset of the v7 disaster-response workspace; engine has changed too much for honest migration.
- **convergence C-2.** All three perspectives agree on bootstrap minimalism: engine-definition file set, selvedge package, migrations, hooks, settings, validate.sh, init, workspace_metadata seed; exclude retrieval substrate, aliases.yaml, .mcp.json.
- **convergence C-3.** All three perspectives agree arc-plan v2 should be mutable and live under applications/, not sealed in provenance/106-session per D-017.
- **convergence C-4.** All three perspectives reject Option C headless subprocess orchestration; operator-as-transport stays structural per constraints six.
- **divergence D-1.** Number of sessions divergent: P-3 5, P-2 21 with adaptive extension, P-1 27. Synthesis adopts P-2 adaptive shape: 21 committed plus extend-on-EF-yield evidence.
- **divergence D-2.** Reveal axis count divergent: P-3 4 unchanged, P-2 6 surface-mapped, P-1 8 domain-flavoured. Synthesis adopts P-2 surface taxonomy; P-1 economic-frame retained as candidate for adaptive extension.
- **divergence D-3.** monitor-external CLI divergent: P-3 none, P-1 and P-2 thin three-subcommand status next-input harvest-ef. Synthesis adopts thin three-subcommand; defer implementation to S108 coding session.
- **minority M-1.** P-3 minimalist arc preserved as first-class minority. Activation warrant: if P0 baseline S001-S003 produces three or more substantive engine-feedback records each at least 250 words with concrete evidence pointer naming engine-v31-specific friction not addressable as routine OI, the S021 retrospective may close arc early at S006 with original S047 four-axis subset.
