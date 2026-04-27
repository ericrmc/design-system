---
session: 081
title: Cross-family deliberation on OI-079-001 disposition — synthesis
date: 2026-04-27
substrate_deliberation_id: 2
sealed_at: 2026-04-27T06:14:18.722Z
---

# 01 — Deliberation synthesis

## What was deliberated

The disposition of OI-079-001: how to record the discrepancy between the schema's 17 tables, 078 D-10's ≤16-table budget, and `engine-manifest.md`'s 15-table prose enumeration. Three named candidate dispositions (A: ratify 17, B: subtract synthesis_points, C: recategorise objects as infrastructure) were carried into the deliberation; perspectives were free to propose a fourth.

This is the first agent-on-substrate deliberator-N flow the workspace has run on a load-bearing question. The substrate carries the deliberation as `deliberation_id=2` (sealed `2026-04-27T06:14:18.722Z`) under session 2 (narrative S081); the four `synthesis_points` rows produced from this deliberation are `synthesis_point_id` 2–5; the perspectives are `perspective_id` 3–5 (aliases `P-2-claude`, `P-2-codex`, `P-2-adversarial`).

## Convening

Three perspectives, each writing blind:

- **`P-2-claude`** — Anthropic family (Claude Opus 4.7, the orchestrator). Neutrally framed; wrote first, before reading either of the others.
- **`P-2-codex`** — OpenAI family (`codex` CLI, `gpt-5.5`, `xhigh` reasoning effort). Cross-family per `methodology.md` §When to convene multiple agents and per `CLAUDE.md` §Multi-agent work. Run via `codex exec --sandbox read-only` with a self-contained prompt at `/tmp/s081-codex-prompt.txt`; the prompt embedded the question, the three named candidate dispositions, and the binding constraints, with explicit instructions not to use any tools or read any files.
- **`P-2-adversarial`** — Anthropic family (Claude general-purpose subagent, separate context). Briefed adversarially: challenge the most plausible default disposition, surface unstated assumptions, propose alternatives the workspace had not surfaced. Permitted to read selected workspace files; explicitly forbidden from reading the other two perspective files (which did not exist when it began work, and were not present at any path it would have searched).

The orchestrator did not read any other perspective before submitting `P-2-claude`; the cross-family agent had no file access; the adversarial agent had file access but was prevented by instruction (and by ordering — its work overlapped temporally with codex but it did not have access to either output). Blind condition was preserved across all three.

## Positions

| Perspective | Position | One-line summary |
|---|---|---|
| `P-2-claude` | C with one tightening | Recategorise `objects` as substrate-infrastructure exempt; name the criterion (a table is infrastructure if it has no domain semantics and exists only to make cross-cutting operations on domain rows possible). |
| `P-2-codex` | A with narrow ratification | Ratify 17 via the existing breach clause; record cause specifically; do not generalise the relaxation to future additions. |
| `P-2-adversarial` | A fourth option D | Replace D-10's budget rule itself; the count is the wrong object; the failure mode is the prose-state mechanism, not the number. |

The diversity is real. The three positions were arrived at independently (blind condition verified) and span the whole disposition surface from "minimal change, narrow record" to "category re-draw" to "rule replacement."

## Synthesis

The synthesis is recorded in the substrate as four `synthesis_points` rows (substrate `deliberation_id=2`):

### Convergence (`synthesis_point_id=2`, label `reject-B`)

**Sources: P-2-claude, P-2-codex.** Disposition B (subtract synthesis_points; absorb T-14 elsewhere) is rejected. Structurally blocked on the absent migration runner (OI-080-001 / EF-079-002), and on substantive grounds — moving T-14 from a CHECK constraint to application-layer JSON-parse is the prose-state failure mode `constraints.md` property 1 names. P-2-adversarial does not endorse B; the question is recast at a higher level.

### Convergence (`synthesis_point_id=3`, label `manifest-must-align`)

**Sources: P-2-claude, P-2-codex.** The manifest's prose enumeration (currently 15) must be brought into alignment with the actual schema. Both `objects` and `synthesis_points` are missing from the manifest and must be enumerated. P-2-adversarial agrees the omissions matter — but treats them as evidence the prose-counter mechanism is itself the bug, which strengthens rather than weakens the alignment requirement.

### Divergence (`synthesis_point_id=4`, label `A-vs-C-vs-D`)

**Sources: P-2-claude, P-2-codex, P-2-adversarial.** How to record the disposition. A and C reach the same schema and the same prose-edit set; they disagree on whether to draw an infrastructure/domain category line. D rejects the framing entirely. The release-gate analysis settles the cleavage: A is admitted unambiguously by 078 D-5; C is on the boundary; D substantively rewrites 078 D-10 and is gate-blocked.

A second observation surfaced after the seal, in the course of writing the decision: 078 D-10's enumeration of 16 tables explicitly included `objects` (verified at `provenance/078-design-commitments/02-decisions.md` line 354). This makes C not a recategorisation of D-10's listing but a substantive revision of it — moving an item out of the 16-list. The release-gate analysis hardens accordingly: C is gate-blocked on the same grounds as D, leaving A as the only admitted disposition.

P-2-claude's perspective explicitly named "I don't know" on this point ("Whether 078's D-10 author intended `objects` to count as one of the 16 or implicitly excluded it as plumbing. The 078 decision text would tell me; I haven't read it in this session.") — the deliberation answered the question and the answer reshapes which dispositions remain available.

### Minority (`synthesis_point_id=5`, label `budget-is-derived-quantity`)

**Source: P-2-adversarial.** The table-count budget is a derived quantity masquerading as a constraint. The substrate can compute its own count; the failure mode (two prose miscounts of two different tables across three sessions) is exactly what `constraints.md` property 1 says the substrate exists to eliminate, recurring one layer up. Carried forward to OI-081-001 for post-release-gate reconsideration.

## What the deliberation did not do

The deliberation did not interrogate **why** the table-count budget exists or whether the workspace measures restraint correctly. P-2-adversarial's question "what does the table-count budget protect against that the validator, the release gate, and the migration runner won't already protect against?" is the substantive challenge; under the release gate, it cannot be answered by a self-development session that has the authority to revise D-10. The question is preserved for OI-081-001.

The deliberation also did not consider whether the manifest enumeration *should be removed entirely*, with the schema and a `selvedge query` invocation as the source of truth. That option is implicit in P-2-adversarial's framing and is captured in OI-081-001 as one of the post-gate considerations.

## Methodology evidence

This deliberation is the first end-to-end exercise of the engine-v17 deliberator-N flow on a load-bearing question:

- **Three perspectives**, **at least one cross-family** (codex/openai), **at least one adversarial** (Claude subagent briefed adversarially) — kernel requirement satisfied.
- **Blind condition** preserved — verified by ordering (P-2-claude written before reading any other; codex sandboxed; adversarial agent file-permitted but barred by instruction from the other perspective files).
- **Substrate carried the deliberation** — `deliberations` row 2, `perspectives` rows 3–5, `synthesis_points` rows 2–5, plus the seal at `2026-04-27T06:14:18.722Z`. T-14 (convergence requires ≥2 sources) was satisfied by both convergence rows. T-05 (no perspective insert after seal) was not exercised this session (would have required attempting a post-seal write; deferred).
- **Citable_alias refs from decisions to perspectives** — D-1's `body_md` cited [P-2-claude], [P-2-codex], [P-2-adversarial], producing 3 substrate `refs` rows (verified at submit time: `"refs": 3`).
- **Disagreement preserved** — the minority position (P-2-adversarial / synthesis_point 5) is in the substrate as a typed row, in the deliberation synthesis above, and in OI-081-001 as a forward-pointing record.
