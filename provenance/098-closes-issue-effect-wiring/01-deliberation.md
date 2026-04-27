---
session: 098
title: closes-issue-effect-wiring — deliberation
generated_by: selvedge export
---

# Deliberation

## D-6 — closes_issue effect wiring: trigger vs handler-side and identity-conveyance

sealed_at: 2026-04-27T23:24:58.078Z

### P-1 (anthropic)

**Position.** Handler-side dispatch implements; refusal trigger enforces; issues become objects rows for uniform alias resolution; opens_issue stays descriptive.

**position.**
- Handler in _submit_decision_v2 walks effects and calls _submit_issue_disposition for closes_issue, mirroring how supports/effects/alternatives are walked today.
**schema_sketch.**
- Extend objects.object_kind enum to admit issue and backfill an objects row for every existing issues row so target_object_id can carry the issue alias.
**migration_path.**
- Single migration recreates objects.object_kind CHECK, backfills 25 issues into objects, and a CLI release updates _submit_issue to insert the objects row.
**schema_sketch.**
- Add an AFTER INSERT trigger on decision_effects that refuses when effect_kind is closes_issue and the resolved target issue is not in resolved/superseded after the same transaction.
**what_not.**
- Does not auto-create issues from opens_issue and does not retroactively mutate the eight historical closes_issue rows whose targets are already resolved by separate dispositions.
**risk.**
- Adding issue to object_kind requires the SQLite CHECK-recreate dance because CHECK constraints are immutable; pattern exists in prior migrations.
- T-24 may refuse the implied issues UPDATE if linked work_items are queued or leased; this is correct semantics — the orchestrator must clear work_items first.
**what_lost.**
- decision_effects gains behavior tied to effect_kind rather than being purely descriptive; precedent already exists in walking supports and alternatives.

### P-2 (openai)

**Position.** Handler-side dispatch via _submit_issue_disposition; add target_issue_id column rather than issues-in-objects; defer opens_issue pending schema growth.

**position.**
- Issue lifecycle change goes through the same Python path as explicit disposition so T-22 and T-24 stay centralized in one application surface.
**schema_sketch.**
- Add a typed target_issue_id column to decision_effects rather than coercing issues into the objects ontology.
**cli_surface.**
- Handler resolves the issue alias through _resolve_issue_alias, then calls _submit_issue_disposition in the same write transaction.
**migration_path.**
- New column plus one-time interpretation of historical target_descriptor strings; no future writes should depend on prose.
**what_not.**
- Do not invent vague reason atoms or bypass text_atom validation; reason for the disposition must come from explicit decision context.
**risk.**
- Handler-only enforcement leaves drift if any future code path inserts decision_effects directly without going through _submit_decision_v2.
- Broadening objects to admit issues changes the ontology and creates secondary questions about object lifecycle, descriptors, and aliases.
**open_question.**
- How is a valid bounded reason atom derived for the synthetic disposition; the submit path may need to require enough reason material from the decision.
**what_lost.**
- Refusing the enum values entirely would be simplest but leaves closes_issue and opens_issue as misleading dead vocabulary.

### Synthesis

**Convergence.** Both perspectives place the dispatch in the Python handler `_submit_decision_v2`, calling `_submit_issue_disposition` so the existing T-22 and T-24 contracts stay in one application surface. Both defer `opens_issue` because `decision_effects` does not carry title or priority and synthesizing them would force hidden defaults.

**Divergence.** Identity conveyance. P-1 prefers extending `objects.object_kind` to admit `issue` and backfilling, so `target_object_id` resolves uniformly through the existing T-01 surface. P-2 prefers adding a typed `target_issue_id` column to `decision_effects` and keeping issues out of the `objects` ontology to avoid broadening it.

**Minority risk noted by both.** Handler-only enforcement leaves drift if any future write path bypasses `_submit_decision_v2`. P-1 proposes a structural refusal trigger to close the gap; P-2 names the risk but does not propose a remedy.

**Resolution direction.** Take P-2 on identity (typed `target_issue_id` column; T-01-equivalent refusal of unresolved issue alias). Take P-1 on enforcement (BEFORE INSERT trigger refuses `closes_issue` rows whose target issue is not already in resolved/superseded). The handler runs the disposition first, so it always satisfies the trigger; the trigger catches anyone who tries to insert directly. `target_descriptor` is repurposed to carry the closure-reason text used to construct the disposition reason atom — it stops carrying identity. `opens_issue` deferred to a later session.

### Synthesis points

- **convergence C-1.** Handler-side dispatch in _submit_decision_v2 calling _submit_issue_disposition is preferred over a substrate-only trigger.
- **convergence C-2.** opens_issue dispatch stays out of scope because decision_effects lacks the fields (title, priority) for safe issue creation.
- **divergence D-1.** Identity conveyance: typed target_issue_id column (P-2) versus extending objects to admit issues (P-1).
- **minority M-1.** Handler-only dispatch leaves drift risk if direct decision_effects writes bypass the handler; P-1 proposes a refusal trigger to close the gap.
