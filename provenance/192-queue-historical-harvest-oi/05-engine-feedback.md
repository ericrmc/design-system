---
session: 192
title: queue-historical-harvest-oi — engine-feedback
generated_by: selvedge export --session
---

# Engine feedback

## EF-S192-1

- **flag.** observation
- **disposition.** (none)

**codex-shape-consult:** S192 queues one-shot historical-insight harvest as HIGH-priority OI per operator ask; codex (gpt-5) shaped the arc.

**Lenses (4 parallel Explore subagents).** subtraction-lessons (removals + designs explicitly rejected + less-engine-is-better lessons); deliberation-discipline (provenance + sealed decisions + evidence standards + session hygiene + authority boundaries); abandoned-designs (interesting but unlanded mechanisms + UI/CLI/API ideas + schemas + workflows); operator-calibration (operator feedback + agent failure patterns + priority calibration + ergonomics + observability needs).

**Per-subagent prompt shape.** Each Explore prompt carries the do-not-commit + do-not-mutate-substrate boilerplate per prompt-development.md section 4 part-one + part-two. Search surface: archive/pre-restart/ (S075 problem statement + S076 restart + S078 design commitments); provenance/legacy-substrate-summary.md (pre-S180 inventory); provenance/<wno>-<slug>/*.md for S001-S179 sessions surviving in git. Output strict JSON max 12 candidates per subagent: [{source_path, one_line_summary, why_load_bearing_now, suggested_disposition: harvest-as-EF | open-as-OI | drop-already-current}]. Subagents prefer source paths over paraphrase confidence, mark weak/duplicative finds as drops, do not reconstruct typed rows.

**Codex review gate.** Orchestrator merges candidates and hands list to codex with sealed-decision context (DV-S081-1 substrate-loss-defense-v1; DV-S109-1 ceremony-subtraction; DV-S189-1 markdown-only-recovery rejecting rebuild; DV-S190-2 graduation-discipline). Codex labels each: keep | drop | conflicts-with-sealed-decision | already-in-current-substrate. Target survival rate 25-40%; over 50% means harvest too permissive; under 15% means lenses too broad or current substrate already absorbed.

**Batch import shape.** Survivors land as either (a) engine_feedback row with body_md prefixed historical-harvest: source=<archive_path> for durable lessons; or (b) fresh OI at MEDIUM default (HIGH only if protects substrate integrity / prevents repeated agent failure / unlocks near-term engine work). Every imported row cites source path in body. No backdated session_no, no synthetic perspectives, no fake provenance walks per DV-S189-1.

**Self-disposing clause.** OI body explicitly names one-shot scope: run once, import survivors, close OI. Post-ship guard EF: future historical harvests require a specific named gap (not general archive rereading) to avoid recurring harvest loop temptation.

**Session-shape verdict.** kind=meta correct (no executable behavior changes; substrate-facing engine_feedback + issue rows only).

## EF-S192-2

- **flag.** observation
- **disposition.** (none)

**audit-step:** 0 load-bearing interpretive choices — exclusions applied: choice (lens set + per-subagent shape + review-gate target rate + batch-import routing + self-disposing scope) all sourced from EF-S192-1 codex shape-consult cited in OI-S192-1 body; no implementer choices left unattached to substrate.
