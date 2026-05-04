---
session: 194
title: historical-harvest-chain-walk-reachability — deliberation
generated_by: selvedge export
---

# Deliberation

## D-4 — How to make harvested historical-context substrate-resident AND chain-walk-reachable from active deliberation surfaces, given operator-named purpose of knowledge-into-agent-context plus decisions-captured-for-future-agents

sealed_at: 2026-05-04T03:01:48.169Z

### P-1 (anthropic)

**Position.** Graph reachability via typed FK edges is load-bearing; substrate-resident context must be reachable via SQL joins from active deliberation surfaces, not string-match heuristics.

**position.**
- Ship option C as primary: engine_feedback_anchors with FK to objects.alias, extend T-32 chain_walks walker to traverse anchor edges so harvest EFs surface as anchored-reachable nodes.
- Backfill the 22 EF-S193-* in this same session because unmoored harvest rows defeat the harvest stated chain-walk-utility purpose.
- Light E (orient surfacing) acceptable as secondary read-side affordance only after the typed graph exists.
**schema_sketch.**
- engine_feedback_anchors with FK to engine_feedback.id and objects.id, anchor_role CHECK in (about, descended_from, calibrates, supersedes_context), PK on (feedback_id, anchor_object_id, anchor_role).
- Anchor target is objects.alias row (decisions, specs, issues, prior EFs, FRs) — same alias table chain_walks already traverses, so the graph composes.
- Submit-time validator: harvest-prefixed EFs (body_md starts historical-harvest:) MUST declare >=1 anchor; non-harvest EFs MAY declare 0 (back-compat).
- Extend chain_walks walker_version to surface inbound engine_feedback_anchors.feedback_id rows as anchored-reachable nodes with nodes_visited and edges_traversed increments per T-32 receipt-pattern.
**cli_surface.**
- bin/selvedge ef submit accepts --anchor <alias>[:role] repeatable; refuses harvest-prefixed body without >=1 anchor (E_REFUSAL_T-NEW).
- bin/selvedge query chain-walk <alias> extends to surface anchored EFs in walk output under a distinct [anchored-feedback] section with role label.
- bin/selvedge orient adds a relevant-history section keyed off active-issue/active-spec alias set joined against engine_feedback_anchors — fed by typed graph not FTS5.
**migration_path.**
- Migration 045: create engine_feedback_anchors with indexes on both columns plus walker_version bump.
- Same-session backfill: 22 EF-S193-* rows each get >=1 typed anchor derived from existing chain_walk_utility field via operator-supervised one-shot script resolving named aliases through objects.alias lookup.
- Refuse on unresolved names — no synthetic aliases per DV-S189-1.
- Backfill is anchor-edge declaration on rows already in current substrate post-S193 import, not backdated typed-row reconstruction; consistent with DV-S189-1 wipe-boundary posture.
**what_not.**
- Reject B (FTS5-as-primary): FTS5 is search not graph reachability — returns string-match BM25 hits not typed edges traversable by chain_walks; DV-S081-1 names substrate as canonical.
- FTS5 may ship later as read-side accelerator over the typed graph but MUST NOT be the discovery primitive.
- Reject A (free-form topic strings): pseudo-links reachable only via string-match heuristics on topic_atom values, equivalent to LIKE-grep dressed up as a table.
- Closed-enum topic variant acceptable only if enum members are themselves objects.alias rows, at which point it collapses to option C with redundant indirection.
- Reject D (mandatory precheck refusing without history-query receipt): process gate without typed graph underneath is theater — agents satisfy the receipt by running any history-query, not the right one.
- Gate without graph is DV-S190-2-pattern premature graduation. Ship the graph first; gates later if validate.sh stale-signal fires.
- Reject any shape that ships option E alone or as primary: orient-surfacing without typed anchor edges is a UI patch over the same untyped substrate — same orphan rows, prettier display.
- Reject deferring 22-row backfill to a future session: leaving 22 unmoored harvest EFs while shipping the anchor table is the worst outcome — operator-named gap persists and tech debt accumulates.
**open_question.**
- Should the walker traverse anchor edges bidirectionally (anchor-object to EF and EF to anchor-object) or only inbound (anchor-object to EF) on assumption walks always start from active deliberation surfaces?
- Inbound-only is simpler and matches operator quote: agents start from current work and walk outward to history. Bidirectional adds traversal cost without clear benefit.
**risk.**
- Anchor-resolution failure during backfill: chain_walk_utility may name an alias not in current substrate (S193 subagent generated speculatively). Mitigation: refuse on unresolved, log as EF for triage.
- Do NOT auto-create stub aliases (DV-S189-1 no-synthetic-rows binds).
- Walker performance: each chain-walk now joins through engine_feedback_anchors, bound by 22 rows today, growth-rate harvest-frequency-dependent. Mitigation: index both columns; truncation_status handles overflow.
- Anchor-role enum drift: 4-member CHECK may need extension. Mitigation: migration discipline already proven (44 migrations through S188); single migration adds an enum member.
- False-positive anchoring during backfill: subagent-generated chain_walk_utility may anchor to tangentially-related alias. Mitigation: operator-supervised one-shot, reviewable diff; calibration EF if mis-anchors surface.
**what_lost.**
- If this loses to FTS5-primary or topic-string-primary, lost is the substrate-discipline invariant that future-agent discovery is graph-reachable from current work.
- Would be shipping a search index over orphan rows and calling it surfacing — agents find harvest EFs by guessing keywords, not walking from the deliberation they are authoring.
- chain_walks T-32 infrastructure remains blind to harvest content forever; next harvest compounds the orphan population.
- DV-S081-1 substrate-canonical degrades to substrate-canonical-for-typed-rows-but-not-for-harvest-rows — exactly the pre-engine-v48 condition T-32 was built to escape.

### P-2 (openai)

**Position.** Load-bearing requirement is the operator quote: putting relevant knowledge into agent context. Fight for E and/or D as primary v1 — success is whether agents see relevant pre-S180 reasoning in-context without knowing search terms.

**schema_sketch.**
- Use whatever substrate index makes the surface reliable: C anchors, B FTS5, or both.
- If C ships, it is only acceptable as an input to orient/precheck surfacing, not as the deliverable.
- Preserve DV-S081-1 by keeping receipts substrate-native: substrate canonical, markdown is generated export.
**cli_surface.**
- Extend bin/selvedge orient to show Historical context candidates beside open issues and active specs.
- Add an optional deliberation-open precheck that automatically runs anchor/topic/FTS matching and prints human-readable harvest pointers before perspective convening.
- Include source archive path, one-line summary, why-load-bearing-now, and chain-walk utility in the packet.
**migration_path.**
- Backfill the 22 EF-S193 harvest rows with enough anchors/topics/search text to exercise the surface.
- Add a receipt following T-32 shape: markdown body, sha256, edge count, walker_version, truncation_status, nodes_visited, edges_traversed, adapted for context-surfacing evidence.
- Validate by opening a fresh S194-like deliberation and confirming the harvest rows appear without manual SQL grep.
**what_not.**
- Reject C-alone: anchor FK correctness without orient/precheck visibility still leaves agents blind.
- Reject SQL-only discovery: it requires the agent to already know what they are missing.
- Reject one-shot untriaged feedback surfacing as sufficient: disposition removes the only automatic context path.
**open_question.**
- Should D refuse deliberation-open when no history-query receipt exists, or should v1 only warn and attach the receipt?
**risk.**
- Poor matching can flood orient with irrelevant harvest rows and train agents to ignore the section.
- FTS-only matching can miss renamed concepts unless paired with anchors or curated topics.
- Mandatory D can become ceremony unless the output is short, useful, and directly attached to the deliberation packet.
**what_lost.**
- If C-alone wins, system preserves typed purity but loses operator-named purpose: relevant knowledge entering agent context window at the moment decisions are made.

### P-3 (anthropic)

**Position.** Any S194 v1 mechanism MUST honor existing substrate-schema discipline: typed atoms 8-240 chars, FK references to objects.alias only, no untyped strings, substrate-side gates via T-32 receipt-pattern.

**position.**
- Converge with P-1 on option C (engine_feedback_anchors with FK to objects.alias) but for schema-correctness reason not chain-walk-graph-integrity.
- Option C is the only shape that respects the engine typed-row contract.
- Option A (free-form topic strings) creates ungrounded categorical labels that drift and synonym-fragment, reproducing the retrieval problem harvest tried to solve.
- Option B (FTS5 on body_md) violates DV-S081-1 substrate canonical, markdown is generated export by promoting prose surface to first-class queryable knowledge.
**schema_sketch.**
- engine_feedback_anchors with FK to engine_feedback.id and objects.id, PRIMARY KEY on (feedback_id, anchor_object_id).
- Anchor target MUST resolve to a row in objects with a typed alias; existing CHECK 8-240 char atom discipline applies transitively via objects.alias.
- NO free-form topic_atom column at v1; NO nullable anchor; NO anchor_label TEXT; NO secondary string column for unmatched anchors.
- Submit-time validation: refuse insert if anchor_object_id does not resolve, with E_REFUSAL_T<NN> carrying substrate-named recovery hint listing nearest-alias candidates.
**cli_surface.**
- bin/selvedge submit engine_feedback ... --anchor <alias> [--anchor <alias>]* — each --anchor resolved to objects.id at submit.
- bin/selvedge query extension already sufficient for retrieval; no new ad-hoc traversal CLI.
- Light bin/selvedge orient extension (option E) admissible IF it queries via the FK join, not via substring match on body_md.
**migration_path.**
- Migration NN: create engine_feedback_anchors with FK plus PK plus index on anchor_object_id.
- Backfill 22 EF-S193-* rows in-session by parsing each rows chain_walk_utility for already-existing aliases (DV-S081-*, OI-S083-*, FR-S188-*, etc.) inserting one row per resolved alias.
- Rows that resolve to zero current-substrate aliases get ZERO anchor rows — acceptable, they remain reachable via orient untriaged surface and SQL until a future deliberation cites them.
- NO synthesis of fake aliases for unresolvable anchors — DV-S189-1 no backdated typed rows, pre-S180 substrate continuity broken at wipe boundary binds here.
**what_not.**
- NOT option A free-form strings — typed atoms with no FK target produce drift and synonym fragmentation; ungrounded labels are not queryable knowledge, they are noise.
- NOT option B FTS5-on-body_md — body_md is prose surface per DV-S081-1; FTS5 over freeform prose inverts the markdown-as-generated-export framing.
- FTS5 over a closed enum of typed atoms (e.g. anchor labels) would be admissible; FTS5 over freeform prose is not.
- NOT any harvest-time tagging that admits untyped atoms or string-match-only retrieval — once shipped, untyped tags are very hard to retract without a divergence-gate.
- NOT a parallel ad-hoc traversal that bypasses chain_walks proof-pattern — audit edges from anchors into chain_walks must reuse the receipt shape per T-32.
- NOT a topic table layered on top later as escape hatch — that re-introduces option A through the back door.
**open_question.**
- If a harvested EF has zero resolvable current-substrate anchors, is right disposition (a) ship empty anchor set rely on orient untriaged, (b) refuse at backfill require operator-named anchor, or (c) defer to per-row FR?
- My stance: (a), because backfill is a one-shot historical operation; option (b) over-weights anchor-completeness against pre-S180 boundary reality.
- Distinction from P-1: P-1 lands on C for chain-walk-graph-integrity (orphans-in-citation-graph framing); I land on C for schema-correctness (typed-FK-discipline framing).
- Threshold-test distinction: P-1 might accept nullable anchor or string-fallback if it preserved graph reachability via some other edge; I would not — schema-correctness requires FK-only at v1.
**risk.**
- v1 FK-only is strict; some harvested rows backfill with zero anchors and stay orphaned in citation graph until cited — acceptable per DV-S189-1 markdown-only-recovery posture for pre-S180 substrate.
- Submit-time refuse-on-unresolvable-anchor adds friction; mitigated by substrate-named recovery hint listing nearest aliases (T-33 pattern).
- Pressure will appear post-ship to add a topic_label TEXT column just for unmatched cases — must be refused at divergence-gate; record now as predicted-future-FR-to-reject.
- Schema-correctness threshold 1: FK references only, no free-form labels at v1 (covers reject-A).
- Schema-correctness threshold 2: typed atoms enforced via existing CHECK constraints transitively through objects.alias (covers reject-B and reject-A-via-back-door).
- Schema-correctness threshold 3: audit edges into chain_walks reuse the proof-pattern, not a parallel ad-hoc traversal (covers reject-D-as-sole-mechanism and substring-matching orient-extension).
**what_lost.**
- If preserved as minority against majority admitting option A or B: record as minority-pin that future drift / synonym-fragmentation / prose-as-canonical incidents are predicted-and-named.
- This perspective cited as the structural argument for a future divergence-gate to retract the untyped column.

### P-4 (anthropic)

**Position.** Ship C plus light E at v1; reject D as premature. DV-S190-2 graduation-discipline mandates substrate-receipt gates wait until calibration-EFs prove necessity across N closes.

**position.**
- Operator precluded DV-S109-1 ceremony-subtraction for S194 but did NOT preclude DV-S190-2.
- Gating deliberation-open on history-query receipt before retrieval mechanism (typed anchors plus orient surfacing) has proven its value is the exact pattern DV-S190-2 forbids.
- Refuse-hook fired before calibration evidence names a real missed-context incident violates DV-S190-2.
**what_not.**
- Do NOT ship D (mandatory deliberation-open precheck T-NN refusing without history-query receipt) in v1. Receipt-pattern gates need calibration-EF evidence first per DV-S190-2.
- Zero closes with C+E shipped means zero data on whether the surface is sufficient without a hard gate.
- Do NOT ship a precheck-CLI that emits a verbose context-pack the deliberator must paste into the open-receipt. That re-bloats orient surface and inverts the ergonomic point.
- Do NOT couple anchor-declaration enforcement at submit-time so tightly that legitimate harvest EFs without a clean current-substrate anchor get refused. Orphan-tolerance is required.
- Do NOT pre-decide the gate shape now and merely defer activation — that pre-commits the design before the surface has been observed in use.
- Per DV-S190-2 the shape of the gate is informed by the calibration-EF pattern, not pre-specified.
**risk.**
- Precheck-dispatch failure: a deliberation-open gate depending on a CLI emitting structured receipt becomes a hard blocker when CLI is broken or topic-extractor mis-classifies. Operator friction at most expensive moment.
- Topic-match heuristic miss: novel deliberations on rare topics (the very ones most likely to need historical context) are precisely where anchor-graph has thinnest coverage.
- Refusing to open a deliberation because no anchor matched penalises the cases where the agent most needs human judgement.
- Surface re-bloat: if E surfaces every harvest EF whose anchor matches any active issue, orient becomes unscannable and agent goes back to ignoring it.
- False-confidence from receipt-theatre: a gate that accepts any history-query receipt regardless of whether agent actually read result trains agent to satisfy gate without internalising lesson. Worse than no gate.
- Sunk-cost lock-in: shipping D now means later calibration-EFs that say the gate fires on wrong topics face a change-cost the v1-without-D path does not carry.
**open_question.**
- What is the watch-FR shape that triggers graduation? Propose FR-S194-watch.
- If 3 calibration-EFs across N>=5 sessions name pattern deliberation-closed-without-surfacing-relevant-pre-shipped-historical-context, graduate to T-NN deliberation-open precheck per DV-S190-2 receipt-pattern precedent.
- Until that signal fires, anchor-graph plus orient surfacing is the whole intervention.
**what_lost.**
- If synthesis ships D against this dissent, preserve as minority: gate-skeptic claim that DV-S190-2 mandates calibration-evidence-first for substrate-receipt gates and was not precluded by operator for S194.
- Operator-friction claim: deliberation-open is wrong refuse-point because it punishes novel-topic deliberations where anchor coverage is thinnest by construction.
- Ergonomic claim: ship-the-surface-first lets us observe whether the surface alone is sufficient — a finding we forfeit if we ship the gate concurrently.

### Synthesis

## Synthesis

**Adopt: option C + concurrent option E at v1; reject option D at v1; reject options A and B as primary.**

**Mechanism (option C, the typed-graph half).** Ship migration NN creating `engine_feedback_anchors(feedback_id INTEGER NOT NULL REFERENCES engine_feedback(feedback_id), anchor_object_id INTEGER NOT NULL REFERENCES objects(object_id), anchor_role TEXT NOT NULL CHECK(anchor_role IN ('about','descended_from','calibrates','supersedes_context')), PRIMARY KEY(feedback_id, anchor_object_id, anchor_role))` per P-1 schema sketch and P-3 schema-correctness threshold. FK to `objects.object_id` enforces typed reachability via the same alias graph that `chain_walks` already traverses (T-32, engine-v48). Submit-time validator: harvest-prefixed EFs (body_md starts `historical-harvest:`) MUST declare ≥1 anchor; non-harvest EFs MAY declare 0 (back-compat with existing 100+ EF rows). Refuse `E_REFUSAL_T<NEW>` on unresolvable anchor aliases with substrate-named recovery hint listing nearest-alias candidates per T-33 pattern. P-3 schema-correctness threshold binds: FK-only at v1, no free-form `topic_label TEXT` column, no nullable anchor; M-3 minority preserved that any future pressure to add a TEXT escape hatch is a predicted-future-FR-to-reject.

**Surfacing (option E, the agent-context half).** Extend `bin/selvedge orient` with a `Relevant historical context (anchored)` section keyed off the alias set of currently-surfaced open issues + active spec versions + HIGH-priority FRs, joined against `engine_feedback_anchors.anchor_object_id` via the FK. Each surfaced row prints `EF-S<wno>-<n> [<anchor_role> anchor: <alias>] <one_line_summary_first_atom>` with the source archive path inline. P-1, P-3 reflect this as "fed by typed graph not FTS5"; P-2 reflects this as "agents see relevant pre-S180 reasoning in-context". Cap at N=10 rows per orient run with `--all-anchored` flag for full enumeration to prevent surface re-bloat per P-4 risk #3.

**[synth] — concurrent ship is load-bearing, neither half alone satisfies the operator metric.** This is a synthesis-only point not made by any single perspective. P-1 framed E as "secondary read-side affordance"; P-2 framed E (or D) as "the load-bearing half"; P-3 admitted E "if it queries via FK join"; P-4 said "ship C + light E at v1." Synthesis adopts P-2's reframing of the success metric — operator quote *"It's all about putting relevant knowledge into agent's context"* — and concludes that shipping C without E at v1 would satisfy P-1's typed-graph claim while losing the operator-named purpose. Conversely, shipping E without C would re-introduce string-match heuristics. The two are co-equal at v1; sequencing is C-first (migration + handler + backfill) then E (orient extension) so that E queries an already-populated table.

**Reject D at v1 (gate-skeptic synthesis).** P-1, P-3, P-4 converge on rejecting mandatory deliberation-open precheck T-NN at v1; P-2 advocates only "optional" precheck which collapses to E (the orient surfacing serves the same purpose without refusal authority). DV-S190-2 graduation-discipline binds: substrate-receipt gates wait until calibration-EFs prove necessity. Operator precluded DV-S109-1 ceremony-subtraction for S194 but did NOT preclude DV-S190-2. M-2 minority preserved (P-4): graduation watch-FR shape — if 3 calibration-EFs across N≥5 sessions name pattern "deliberation closed without surfacing relevant pre-shipped historical context the agent should have found via anchor-graph", graduate to T-NN deliberation-open precheck per DV-S190-2 receipt-pattern precedent.

**Backfill discipline (22 EF-S193-* in same session).** All 4 perspectives admit in-session backfill per codex shape-consult motivating-failure-case framing. P-1 wants reject-on-unresolvable-alias with operator-supervised one-shot; P-3 wants zero-anchors-acceptable for rows that resolve to no current-substrate alias. Synthesis adopts P-3's zero-anchor-acceptable per DV-S189-1 markdown-only-recovery posture (pre-S180 substrate continuity broken at wipe boundary; some pre-S180 lessons anchor to concepts no longer carrying a current alias). Backfill script reads each EF-S193-N row's `chain_walk_utility` field, attempts alias resolution via SQL `objects.alias` lookup, inserts one anchor row per resolved alias, logs unresolved as `triage` flag EF for operator review. P-1's risk-mitigation preserved as runtime guard: NO synthetic alias creation per DV-S189-1.

**Walker traversal (P-1 open question).** v1 ships inbound-only (anchor-object → EF) traversal because chain-walks always start from active deliberation surfaces (decision_v2 walking outward). Bidirectional preserved as forward-direction if a future deliberation reads a harvest EF and needs to forward-walk to its sibling anchors.

**[synth] — sequencing matters.** Ship migration first, then handler, then backfill, then orient extension, then session-close. Shipping orient-extension before backfill = empty section trains agents to ignore the surface; shipping handler before migration = handler queries non-existent table. Sequencing is part of the v1 contract.

**Counterfactuals admitted (T-36 receipt-pattern).** CF-1: ship D at v1 with mandatory T-NN refuse-on-no-receipt — deferred to FR-S194-1 watch-trigger per M-2 graduation shape. CF-2: ship engine_feedback_anchors with anchor target as `TEXT` label admitting both aliases and free-form topic strings — addressed-in-synthesis via P-3 schema-correctness threshold, FK-only adopted, TEXT escape hatch explicitly excluded.

**What lost — minorities preserved.**
- M-1 (P-2): "Anchor FK without orient/precheck visibility leaves agents blind." Addressed by concurrent C+E ship per [synth] above; preserved as the watch-trigger argument that future calibration-EFs naming "anchor table populated but agent missed historical context" graduate to D per M-2.
- M-2 (P-4): DV-S190-2 watch-FR shape preserved verbatim for substrate-receipt-gate graduation.
- M-3 (P-3): Schema-correctness threshold preserved as predicted-future-FR-to-reject any topic_label TEXT escape hatch.

**Forward-references emitted by this synthesis.** FR-S194-1 (watch-trigger for D graduation per M-2). FR-S194-2 (predicted-future-FR-to-reject TEXT escape hatch per M-3). FR-S194-3 (chain-walks walker bidirectional traversal extension preserved as forward-direction per P-1 open question).


### Synthesis points

- **convergence C-1.** Option C (engine_feedback_anchors FK to objects.alias) is primary substrate mechanism per all 4 perspectives admit-set (P-1 + P-2 + P-3 + P-4).
- **convergence C-2.** Reject option A (free-form topics) + option B (FTS5-on-body_md) as primary mechanism; FTS5-on-body_md violates DV-S081-1 substrate-canonical framing.
- **convergence C-3.** Ship option E (bin/selvedge orient extension surfacing anchored harvest EFs) at v1 in addition to option C; query via FK join not substring match.
- **convergence C-4.** Backfill 22 EF-S193-* rows in same session per codex motivating-failure-case framing; unmoored harvest rows defeat the harvest stated chain-walk-utility purpose.
- **divergence D-1.** D mandatory T-NN deliberation-open precheck at v1: P-2 admits optional precheck; P-1 + P-4 reject as premature; P-3 implicit-reject. Synthesis: reject at v1.
- **divergence D-2.** E load-bearing weight: P-2 co-primary with C; P-1 secondary affordance; P-3 admits if FK-join; P-4 light E. Synthesis: co-equal at v1 per [synth] operator-metric.
- **divergence D-3.** Anchor-resolution failure: P-1 reject-on-unresolved-alias; P-3 zero-anchors-acceptable per DV-S189-1 markdown-only-recovery. Synthesis: P-3 admit + P-1 runtime guard.
- **minority M-1.** P-2: anchor-FK-without-surfacing leaves agents blind; preserved as watch-trigger-argument that calibration-EFs naming missed-context graduate to D per M-2.
- **minority M-2.** P-4: DV-S190-2 watch-FR graduation shape - 3 calibration-EFs across N>=5 sessions naming missed-context graduate to T-NN precheck per receipt-pattern.
- **minority M-3.** P-3: schema-correctness threshold - FK-only at v1 binds; predicted-future-FR-to-reject any topic_label TEXT escape hatch column pressure.
