---
session: 114
title: triage-cross-session-provenance-export — deliberation
generated_by: selvedge export
---

# Deliberation

## D-11 — Cross-session provenance export: shape and scope (EF-S110-7)

sealed_at: 2026-04-29T04:53:28.629Z

### P-1 (anthropic)

**Position.** Ship cross-session provenance as markdown-only projection in anchor and workspace modes; defer --graph HTML until markdown is used in anger.

**position.**
- The reframe is correct on the gap even if maximalist on the remedy; substrate joins exist post S113 but are reachable only via raw SQL.
- Per-session export fragments engine reasoning across folders; cross-session export is what makes substrate-canonical-rows pay off in readable provenance.
**cli_surface.**
- Ship `bin/selvedge export --provenance` producing deterministic markdown with two modes sharing one generator.
- Anchor mode `--provenance --anchor <alias>` renders the causal chain rooted at one object walking supports/effects/FR-dispositions/supersessions.
- Workspace mode `--provenance` (no anchor) is a chronological roll-up across sessions with cross-references to FRs and supersessions.
**schema_sketch.**
- Both modes write to `provenance/cross-session/`; anchor mode is one file per alias, workspace mode a single regenerated file. No new substrate tables or inferred edges.
**migration_path.**
- First release: markdown projection of decisions, alternatives, deliberations, handoffs/FR dispositions keyed by `target_object_id` with deterministic ordering.
**what_not.**
- Reject `--graph` HTML for first release; reopen criterion is a recurring stakeholder question that markdown cannot answer.
- Refuse synthesised prose connecting decisions; substrate refuses prose-in-rows and the export must honour that constraint.
- Refuse new substrate columns or tables to support presentation; if a relation is not already reachable, omission is itself signal.
**risk.**
- Ceremony creep: framing export as deliverable pulls toward synthesised prose and presentation-only substrate writes, re-importing ceremony Selvedge has been subtracting.
- False completeness: a coherent-looking workspace export will be trusted more than its weakest join warrants; the export must surface omission, not paper over it.
**what_lost.**
- Deferring `--graph` costs ergonomic navigation for non-technical reviewers without a markdown reader; rejecting prose makes the export denser and harder to skim.

### P-2 (openai)

**Position.** Ship cross-session provenance as a deterministic anchor-based markdown trace via `bin/selvedge trace <alias>`; defer broad narrative export and HTML graph.

**position.**
- Per-session export, `query`, and `orient` do not directly answer the recurring question: how did this object get here across sessions?
- A unified cross-session narrative risks becoming a second deliberation product: broad, interpretive, and expensive to keep meaningful.
**cli_surface.**
- First release surface: `bin/selvedge trace <alias>` or `bin/selvedge export --provenance --anchor <alias>` producing markdown.
**schema_sketch.**
- Trace renders supports/effects via `decision_supports` and `decision_effects` using the newly backfilled `target_object_id`.
- Trace includes alternatives, deliberation perspectives/synthesis points only when linked to the traced object, and `close_state_items.next_session_should` plus `forward_reference_dispositions` for handoff continuity.
**migration_path.**
- First release is markdown-only with deterministic ordering, stable IDs, hyperlinks back to per-session markdown, and tests around DV-S001-5 to DV-S002-1 to S003.
- A later `--graph` should emit machine-readable graph data first, then HTML once evidence shows people need visual navigation; derived from the same trace model.
**what_not.**
- Refuse `--graph` HTML as a first-release requirement and refuse a default global `cross-session.md` that narrates the whole workspace.
- Refuse inferred edges unless clearly marked as inferred and excluded from the core deterministic trace.
- Refuse any export that rewards writing more substrate text merely to make the provenance report look richer.
**risk.**
- Documentation gravity well: authors may write substrate rows for graph aesthetics instead of decision clarity, pushing Selvedge toward ceremony.
- False authority: a unified narrative can look complete while omitting weak links; a graph can make adjacency look like causality.
- Boundary discipline is the hard part: deciding what counts as relevant without turning every export into a transitive closure of the workspace.
**open_question.**
- Open question: what counts as relevant context for a trace before it becomes a transitive closure of the whole workspace?
**what_lost.**
- Anchor-based markdown forfeits the satisfying single-report answer and HTML graph appeal; broad reviews may need multiple traces, which is acceptable.

### Synthesis

P-1 (anthropic) and P-2 (openai) converge on the substantive frame: ship cross-session provenance as deterministic markdown, defer `--graph` HTML, refuse synthesised prose, refuse new substrate columns added solely for presentation, refuse inferred edges, and treat the export as a projection of substrate rows rather than an authoritative narrative. Both surface the same risks (ceremony creep / documentation gravity well; false completeness / false authority).

They diverge on default scope. P-1 proposes shipping anchor mode and workspace mode together as a single generator unioned across sessions. P-2 refuses workspace mode by default and would ship only `bin/selvedge trace <alias>` (or `--provenance --anchor <alias>`), warning that any global default risks a transitive closure of the whole workspace and incentivises substrate writing for graph aesthetics rather than decision clarity.

The synthesis takes P-2's narrower scope as the safer first release because P-2's boundary-discipline concern is load-bearing: the engine has spent two versions subtracting ceremony, and a workspace-wide export is the kind of surface whose appetite grows with use. Shipping anchor-only first preserves the option to add workspace mode if a recurring stakeholder question genuinely cannot be answered by composing several anchor traces. P-1's workspace mode is recorded as an explicit deferral with a reopen criterion, not a refusal.

### Synthesis points

- **convergence C-1.** Both perspectives ship markdown-only first release, defer --graph HTML, treat export as projection not narrative.
- **convergence C-2.** Both refuse synthesised prose, refuse new substrate columns added solely for presentation, refuse inferred edges.
- **convergence C-3.** Both name the same two failure modes: ceremony creep / documentation gravity well, false completeness / false authority.
- **divergence D-1.** P-1 ships anchor and workspace modes together; P-2 ships anchor only and refuses default global scope.
- **minority M-1.** P-2 minority concern: a workspace-wide export risks a transitive closure of the whole workspace.
