---
session: 098
title: closes-issue-effect-wiring — assessment
engine_version_at_open: engine-v27
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

Engine-v27 admits decision_effects.effect_kind in (closes_issue, opens_issue) descriptively only — no trigger or handler dispatches the issue state change; existing 8 closes_issue rows all have target_object_id NULL.

## Agenda

1. Triage EF-S096-3: wire closes_issue so it atomically transitions issues.status when a decision_effect is recorded.
2. Decide between substrate-trigger and handler-side dispatch for the wiring (deliberation warranted).
3. Decide how to convey issue identity in decision_effects: add issues to objects, add target_issue_id column, or accept alias via descriptor parse.
4. Scope question: does opens_issue need the same wiring this session, or is descriptive-only acceptable for now?
5. Implement migration + any handler change; run reviewer subagent.
6. Decide whether the wiring warrants engine-v28 bump.
