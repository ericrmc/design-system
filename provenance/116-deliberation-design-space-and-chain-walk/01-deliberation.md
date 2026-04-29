---
session: 116
title: deliberation-design-space-and-chain-walk — deliberation
generated_by: selvedge export
---

# Deliberation

## D-12 — Chain-walk scope for OI-S114-1 and EF-S115-1 design-space-audit reframe

sealed_at: 2026-04-29T05:54:13.388Z

### P-1 (anthropic)

**Position.** Chain-walk: ship as v1.5 follow-up to OI-S114-1 with bounded depth, not in v1 and not refused. EF-S115-1: reject sub-activities and multi-session threads; add a post-close option-surfacing convention to workspace.md as lightest remedy.

**position.**
- Anchor-only at depth-1 already includes FR-disposition traversal per S114 D-11; the disagreement is where the depth knob lives, not whether to traverse forward.
- Chain-walk follows typed FK edges: decision_supports.cited_object_id, decision_effects.target_object_id, FR-disposition disposing_decision_id, spec_versions.superseded_by.
- These are lineage edges, not transitive closure of the workspace.
- The original EF-S110-7 framing (DV-S001-5 to DV-S002-1 to S003) requires multi-hop walk; anchor-only at fixed depth-1 underspecifies the original gap.
- EF-S115-1 observation is real but the three proposed remedies are over-fitted to one data point.
- Recovery path worked: post-close operator dialogue surfaced chain-walk; S115 queued the FR; S116 deliberates it.
- That is exactly how late-surfaced options should be handled.
- Sub-activities and multi-session threads add ceremony every session for benefit only when framing is incomplete.
- FR queues plus supersession plus decision_v2 chains already admit recovery without new machinery.
**migration_path.**
- v1: anchor-only as S114 decided, walking supports/effects/alternatives/deliberations/handoffs at depth 1 along each edge type rooted at one alias.
- v1.5: add --depth N flag (default 1, hard cap 5). Cycles bounded by visited-set on object_id. Edge types unchanged from v1.
- The depth knob lives in the CLI flag, not in substrate; no schema change.
- v1 lands first as its own session; v1.5 follows after v1 has been used in anger to inform whether default depth should remain 1.
**schema_sketch.**
- No new substrate. Chain-walk is purely a query/render extension over the same FK edges v1 uses.
- Edge selection per node-kind (decision/spec_version/issue/FR-disposition/deliberation) is fixed by S114 P-2 spec; depth is the only new dimension.
- Visited-set keyed on object_id breaks cycles; deterministic order keyed on (depth, kind, alias).
**cli_surface.**
- v1: bin/selvedge export --provenance --anchor <alias> writes provenance/cross-session/<alias>.md.
- v1.5: same surface plus --depth <N> (default 1, cap 5); --depth 0 admitted as a debug surface that emits the anchor object only.
- Hyperlinks back to per-session markdown; omission surfaced as omission.
**what_not.**
- Refuse --depth unbounded. The cap of 5 is a value judgement but unbounded walks are how appetite grows.
- Refuse including objects reachable only via shared text_atoms; that is transitive closure of prose, not lineage.
- Refuse synthesised prose connecting nodes; substrate refuses prose-in-rows and the export must honour that.
- Refuse a new pre-deliberation sub-activity in methodology; cost-per-session is paid every session for benefit only when framing is incomplete.
- Refuse multi-session threading as default; doubles ceremony for cases where design-space mapping does not yield new shapes (most cases).
- Refuse re-opening S114 D-11; that decision was made in good faith on the design space available. v1.5 layers on v1 without overturning it.
**open_question.**
- Workspace.md wording: how to phrase the convention so it admits load-bearing post-close surfacing without becoming licence to reopen on weaker signals.
- Whether the synthesis step should explicitly include a sanity-check of the proposed shape against the original triggering case (would shape X answer the EF).
- Whether chain-walk default depth should remain 1 after v1.5 ships or shift to 2; defer until v1 lands and is used.
**risk.**
- Chain-walk default depth could grow under appetite if not constrained; the hard cap of 5 plus depth-1 default mitigates but is a value judgement.
- The workspace.md addition could be read as licence to reopen sealed deliberations on weaker signal than the EF named; wording must be tight.
- Treating the EF as sufficient signal to add machinery would itself be the under-exploration pattern in reverse: latching on the first plausible remedy.
**what_lost.**
- Refusing chain-walk in v1 keeps the v1 deliverable smaller but means the next two-session anchor-trace question still needs raw SQL until v1.5 lands.
- Refusing the design-space-audit sub-activity loses the case where perspectives genuinely miss a shape; the three remedies remain queued as FRs if a second instance accumulates.
- Refusing multi-session threads loses explicit pre-mapping discipline; mitigated by trusting operator-driven post-close recovery as already demonstrated.
- Adopting only the lightest remedy means EF reframe pressure is honoured but not maximally; if pattern recurs, this restraint becomes the prior rejection a stronger remedy must cite.

### P-2 (openai)

**Position.** Fold bounded anchor-rooted chain-walk into v1, and adopt reopen-on-new-reading plus a lightweight design-space audit trigger, not a standing multi-session ceremony.

**position.**
- Chain-walk is not workspace mode; it is anchor-rooted traversal over explicit substrate FK edge families.
- Depth-1 anchor-only under-delivers on the original DV-S001-5 to DV-S002-1 to S003 provenance need.
- Shipping anchor-only first risks normalizing an export that cannot answer the trace question it was created for.
- Recursive traversal is acceptable only with an explicit edge whitelist, cycle handling, deterministic ordering, and a depth bound.
- The right boundary is not 'one hop'; it is 'no unrooted workspace closure and no inferred semantic edges.'
- EF-S115-1 is real: S114 explored the offered opposition, not the design space.
- Reopen-on-new-reading would have caught chain-walk with the least ceremony.
- A lightweight design-space audit would likely have surfaced chain-walk before positions were sealed.
- Multi-session threads are too heavy as a default remedy for this failure mode.
**migration_path.**
- Implement chain-walk in OI-S114-1 v1 behind the existing --provenance --anchor <alias> surface.
- Treat one-hop export as an implementation subset, not a released semantic contract.
- Add tests for direct, two-hop, cycle, supersession, and mixed FR-disposition paths.
- If implementation exceeds the current slice, reduce edge families before reducing recursion.
**schema_sketch.**
- Traversal root is exactly one resolved alias.
- Traversal follows only declared provenance edge families: FR dispositions, supersessions, supports, effects, alternatives, deliberations.
- Each visited row carries path metadata: root alias, edge family, hop depth, predecessor row, and cycle-truncation marker.
- Ordering should be deterministic: root first, then hop depth, edge family, stable substrate key.
- Default max depth should exist even if generous; unbounded recursive export is not a v1 requirement.
**cli_surface.**
- Keep bin/selvedge export --provenance --anchor <alias> as the main command.
- Add --max-depth <n> only if needed for operator control and testability.
- Do not add --workspace or any synonym that implies unrooted roll-up.
- The default should be recursive chain-walk, not depth-1.
- Consider --one-hop only as a diagnostic escape hatch, not as the product shape.
**what_not.**
- Do not implement workspace-wide transitive closure.
- Do not traverse arbitrary SQLite FKs just because they exist.
- Do not infer provenance from markdown links or alias text.
- Do not make every deliberation multi-session by default.
- Do not add a mandatory design-space audit to every session.
- Do not protect sealed decisions from cheap reopening when a load-bearing option appears.
- Do not frame reopening as failure; it is normal substrate supersession.
- Do not let 'middle ground' count as coverage of the design space.
**open_question.**
- Which edge families are in v1 if implementation pressure forces a smaller whitelist?
- Should recursive export default depth be finite, and if so what value is operationally sane?
- How should the markdown render repeated rows reached through multiple paths?
- What threshold triggers design-space audit: reframe flag, high-impact OI, or operator request?
**risk.**
- Chain-walk can become workspace closure by drift if edge admission is loose.
- Markdown output can become noisy if every path is rendered with equal weight.
- A depth cap can hide relevant provenance unless truncation is visible.
- Design-space audit can become ritual if triggered too broadly.
- Reopen discipline can become churn if no 'load-bearing new option' threshold exists.
**what_lost.**
- The v1 implementation is larger than depth-1 anchor-only.
- Some simplicity in the original sealed S114 decision is sacrificed.
- Operators lose the false comfort of finality immediately after close.
- The engine accepts a small amount of explicit design-space cost for high-impact framings.

### Synthesis

P-1 (anthropic) and P-2 (openai) converge on the substantive frame for chain-walk: anchor-rooted traversal over an explicit closed edge family (supports, effects, alternatives, deliberations, FR-dispositions, supersessions); refuse workspace-wide transitive closure; refuse synthesised prose; refuse inferred edges. Both refuse multi-session threads as default. Both refuse a mandatory pre-deliberation design-space audit on every session.

They diverge on Q1 release scope and on the EF-S115-1 remedy weight.

On Q1, P-2 argues chain-walk folds into v1 because depth-1 anchor-only does not answer the original EF-S110-7 framing (DV-S001-5 to DV-S002-1 to S003 spans multiple hops); shipping a v1 that does not answer the question its OI was created for normalises a partial deliverable. P-1 argues v1.5: anchor-only is a useful subset, S114's decision was made in good faith on the design space available to it, staged release admits learning from use. The synthesis takes P-2 on Q1: the load-bearing argument is that the OI names cross-session trace and one hop is barely cross-session; learning from a v1 that does not answer the originating question is unhelpful learning. v1 ships bounded chain-walk with default depth 3, hard cap 5, --max-depth flag, cycle handling via visited-set on object_id, deterministic ordering by (depth, edge family, alias). This does not overturn S114 D-11; S114 chose anchor-rooted (not workspace) which both perspectives still affirm; the depth dimension was outside S114's stated frame.

On Q2, P-2 adopts both reopen-on-new-reading and a lightweight triggered design-space audit; P-1 adopts only the reopen convention as workspace.md documentation and rejects the audit sub-activity as over-correction on one data point. The synthesis takes P-1 on Q2: adopt the reopen-on-new-reading convention as a workspace.md addition (post-close operator dialogue surfacing a load-bearing option neither perspective named is a legitimate trigger for a follow-up session); defer the triggered design-space audit until a second instance of the under-exploration pattern accumulates. Both perspectives flag the same risk that triggered audit becomes ritual or that reopen becomes churn without a high bar; the high bar is built into the convention wording (load-bearing option neither perspective named).

Minority preserved: P-2's claim that adopting only the reopen convention without the triggered audit may leave the under-exploration pattern under-addressed; reopen criterion is a second instance of the pattern.

### Synthesis points

- **convergence C-1.** Both treat chain-walk as anchor-rooted over a closed edge family; refuse workspace-wide transitive closure and inferred edges.
- **convergence C-2.** Both refuse multi-session threads and a mandatory pre-deliberation design-space audit on every session.
- **convergence C-3.** Both require cycle handling, deterministic ordering, depth bound, and refuse synthesised prose in the export.
- **divergence D-1.** P-2 ships chain-walk in v1; P-1 ships anchor-only as v1 and chain-walk as v1.5. Synthesis takes P-2.
- **divergence D-2.** P-2 adopts triggered design-space audit plus reopen discipline; P-1 adopts only reopen convention. Synthesis takes P-1.
- **minority M-1.** P-2 minority: adopting only the reopen convention without triggered audit may leave the under-exploration pattern under-addressed.
