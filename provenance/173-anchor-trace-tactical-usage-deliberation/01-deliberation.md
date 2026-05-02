---
session: 173
title: anchor-trace-tactical-usage-deliberation — deliberation
generated_by: selvedge export
---

# Deliberation

## D-26 — Anchor-trace tactical-usage shape: invocation points, depth defaults, clause strength, ergonomic gaps, spec home.

sealed_at: 2026-05-02T03:12:53.924Z

### P-1 (anthropic)

**Position.** Ship a recommended §5 clause naming anchor-trace invocation points at decision-record draft time, plus a --print stdout mode FR; defer T-NN gate until calibration-EF recurrence per DV-S152-1.

**cli_surface.**
- Before drafting decision-record alternatives at depth 2; anchor on the target spec_version / OI / parent decision the new record will affect.
- Before drafting spec-version supersede at depth 3; supersession needs the version-chain plus source-decisions in view.
- Before closing/disposing an OI at depth 2; surfaces origin decision plus downstream FRs to verify closure actually discharges the issue.
- When operator surfaces a calibration-EF naming a missed counterfactual, depth 2 anchored on the sealed deliberation grounds the claim in observable trace.
- NOT at session-open queue triage; orient already provides the read at lower context cost.
- Depth 1 quick-cite only when the agent is verifying a single known parent reference is still load-bearing.
**migration_path.**
- Recommended (operator/agent-policed) at engine-v47; calibration-EFs are the recovery path when a slip is caught.
- Promotion trigger: if a future calibration-EF names a decision that re-proposed a rejected alternative AND anchor-trace would have caught it, ship gate-promotion OI.
- The promotion-trigger structure mirrors §8.5 audit-step and §4 seal-grade clauses; this is the third instance of the typed-observation→gate pattern.
**cli_surface.**
- --print mode emitting markdown body to stdout is the highest-leverage gap; without it tactical use is twice as expensive as archival use.
- --json for structured consumption is a later-facing affordance once linting use cases emerge.
- --summary compact node-count + edge-stats is appealing but the markdown body is already small at depth 2.
- Per-anchor caching is unnecessary at current scale; the BFS is fast.
**migration_path.**
- Primary clause in §5 decision-record discipline as a sub-step before drafting supports / alternatives arrays.
- Brief cross-reference in §8.5 close-time list under item 2 (FR disposition) and item 3 (EF disposition).
- No new dedicated section; one-tool patterns do not warrant their own §X header.
- Phrase as a recommendation that names invocation triggers and depth defaults, not as a forced step.
**what_not.**
- Do not run anchor-trace on every decision; ceremony cost outweighs leverage when the decision is local.
- Do not use --write for tactical agent use; reserve --write for archival traces operator may consult later.
- Do not promote to T-NN gate from one operator-surfaced miss; require calibration-EF evidence first.
- Do not assume the trace is a substitute for reading the cited spec or close record; it surfaces structure, not content.
- Do not require trace citation in every decision-record body; the trace is a check, not a deliverable.
**risk.**
- Recommended clause may be ignored same as the tool itself was ignored across 56 sessions; mitigation requires surface placement, not just clause text.
- §5 placement risks burying the clause under the existing decision-record schema; needs a clear sub-step prefix.
- Stdout --print may quietly displace --write archival use, weakening the durable audit trail per P-2 risk reading.
- Depth 2 default may miss older supersession chains for long-lived specs (methodology v1→v9); operator escalation to depth 3-5 is the recovery path.
**open_question.**
- Should the §5 clause be phrased as a checklist sub-step or as a separate paragraph after the schema description?
- Should --print be the new default with --write opt-in, or --write the default with --print opt-in?
- How much should the §5 clause name about invocation depth versus delegating to operator/agent judgment?

### P-2 (openai)

**Position.** Use anchor-trace as targeted chain-walk before irreversible/precedent-sensitive moves, not session ritual; make it cheap, visible, state-transition-bound: decisions, supersedes, OI/FR closure, calibration claims.

**cli_surface.**
- Decision supports/alternatives: depth 2; catches rejected options, missing supports, and peer decisions before prose hardens.
- Spec-version supersede: depth 3; supersession needs source clauses, parent decisions, and nearby effects in view.
- OI close/dispose: depth 2; verifies origin, downstream FRs, and whether closure actually discharges the issue.
- FR rot disposal: depth 2; reconstructs what was deferred, not what the current agent vaguely remembers.
- Session-open queue triage: depth 2 only for OIs naming 3+ sessions or showing high fan-in.
- Calibration-EF counterfactual: depth 2; required when the claim is we missed applying X before.
- Depth 1: only for quick citation lookup on a single known parent.
- Depth 4-5: operator-requested or suspected long supersession chain; never default.
**migration_path.**
- Recommended now; mandatory later only after calibration EFs name missed anchor-trace use.
- Hard gate only for spec supersede and OI/FR closure with stale or multi-session provenance.
- No universal T-NN close gate; that converts a useful probe into budget tax.
- Require note of alias + depth in the decision/closure artifact when used.
- Treat absence of trace as acceptable if the artifact names why provenance is local and fresh.
**cli_surface.**
- Add --print; agent consumption should not require write-read ceremony.
- Add --summary; emit nodes, edges, sessions, rejected alternatives, open FRs, supersession links.
- Add --json; enables future linting without scraping markdown.
- Add --limit-open; prioritize undisposed OIs/FRs and rejected alternatives.
- Add suggested anchors from an OI/FR alias; reduce alias-choice friction.
- Keep --write for archival traces, but make stdout the tactical default.
**migration_path.**
- Put the main clause in §5 decision-record discipline.
- Add close-time cross-reference in §8.5 for OI/FR disposition.
- Avoid a new chain-walk section unless more tools join the pattern.
- Phrase as precedent-sensitive artifacts require provenance check, not run anchor-trace.
**what_not.**
- Do not run it at every session-open.
- Do not make depth 3 the default for all decisions.
- Do not require archival markdown for every tactical trace.
- Do not promote to substrate gate from one operator-surfaced miss.
- Do not use traces as proof of correctness; they surface context, not judgment.
- Do not let recursive methodology calibration become the main consumer.
**risk.**
- Recommended clauses may be ignored again without a lightweight reminder path.
- Mandatory gates may suppress small useful decisions under ceremony pressure.
- Depth 2 can miss older supersession causality in long-lived specs.
- --print may increase use but reduce durable audit artifacts.
- Agents may anchor on surfaced nodes and miss relevant non-closed-family context.
**open_question.**
- What exact recurrence threshold promotes recommended use to mandatory gate?
- Should stale mean session age, edge count, open-FR count, or human-marked risk?
- Should the trace report rank rejected alternatives above supports by default?
- Should calibration EFs cite the trace output or only the recovered aliases?

### P-3 (anthropic)

**Position.** Ship only the --print FR and watch; the tools 56-session non-use is a natural experiment with no calibration-EF pressure, so a clause now is anecdote-driven design. Defer spec edit until recurrence.

**cli_surface.**
- Defer all clause-recommended invocation points; agent discretion is the current state and has not produced calibration-EF pressure.
- If the agent already has the discretion and the tool, naming additional invocation points without enforcement is just clause-text bloat.
- The empirical question is whether the agent fails to invoke when invocation would help; that data does not exist in calibration-EF form yet.
**migration_path.**
- No clause now; emit only the ergonomic FR and a watch-FR for calibration-EF surface.
- Clause recommended later only if calibration-EF evidence accumulates; at the rate of one per ~5 sessions to match prior promotion-trigger thresholds.
- T-NN substrate gate never; the closed edge family is engine-internal and a forced gate would create a new self-referential ceremony cycle.
**cli_surface.**
- --print is the only clearly justified ergonomic ask; the disk-write-then-Read pattern doubles tactical-use cost.
- Multiple ergonomic adds (--summary, --json, --limit-open, suggested-anchors) inflate the coding follow-up beyond what the value-add can defend at one-data-point evidence.
- Reserve broader ergonomic batch for after a clause is justified by recurrence; do not pre-build affordances for use shapes that have not been observed.
**migration_path.**
- No spec edit now. If a clause lands later, §5 sub-step is the right home; agree with P-1 and P-2 on placement once justified.
- Adding a §X new section would be premature optimisation under ceremony-subtraction discipline.
- The promotion-trigger structure should be encoded as an FR watch row and an EF calibration-watch row, not as spec text yet.
**what_not.**
- Do not ship a recommended clause from one operator-surfaced gap; that is anecdote-driven design.
- Do not pre-build ergonomic affordances (--json, --summary) without an observed use case demanding them.
- Do not name specific depths in spec text without empirical depth-yield data per invocation point.
- Do not assume the agents 56-session non-use is a discipline gap; the failure modes the tool catches may not occur at the rate that justifies trace cost.
**risk.**
- Without a clause, the same 56-session non-use pattern continues; ergonomic --print alone may not change agent discipline if the discipline gap is real.
- Deferring the clause has opportunity cost: each session risks a re-proposal slip the trace would have caught and the slip will not be cheaply observable post-hoc.
- The minimalist path bets calibration-EFs would surface a real problem; if the agent silently re-proposes without naming the slip, recurrence-pressure cannot fire.
**open_question.**
- Is the 56-session non-use evidence that the agent does not need the trace, or evidence that the agent does not think to use it?
- Should the FR watch row carry an explicit alias-pattern (e.g. calibration-EF naming a re-proposed rejected alternative) or stay open-ended?
- If --print ships and the non-use pattern continues for another 20 sessions, is that the trigger for the clause?

### Synthesis

Three perspectives convened on tactical-usage shape for the anchor-trace chain-walk feature shipped 56 sessions ago at S117 / OI-S114-1 v1 and not invoked tactically by the agent in any subsequent self-development session. P-1 anthropic primary advocates a recommended clause in prompts/development.md §5 plus a coding FR shipping --print stdout mode (highest-leverage ergonomic), with mandatory T-NN substrate gate deferred to calibration-EF recurrence pressure per DV-S152-1 typed-observation-to-gate progression. P-2 openai-codex cross-family converges on the recommended-clause shape but expands the ergonomic ask to a coherent batch (--print plus --summary plus --json plus --limit-open plus suggested-anchors) and contributes the framing precedent-sensitive artifacts require provenance check rather than run anchor-trace. P-3 anthropic adversarial-minimalist dissents on shipping any clause now; reads the 56-session non-use as a natural experiment whose result is that the named failure modes have not surfaced as calibration-EFs at the rate that would warrant intervention; recommends shipping only --print plus a calibration-watch FR. Convergence majority C-1 adopts --print stdout mode as the highest-leverage ergonomic affordance shipped via dedicated coding FR; C-2 rejects mandatory T-NN substrate gate at engine-v47 with promotion-trigger via calibration-EF recurrence per DV-S152-1; C-3 defers broader ergonomic batch (--summary --json --limit-open suggested-anchors) to observed-need basis under DV-S109-1 ceremony-subtraction discipline; C-4 names §5 decision-record discipline as spec home with §8.5 brief cross-reference, no new dedicated section. Divergence D-1 records the clause-strength split: P-1 plus P-2 majority adopt a recommended clause via spec-edit FR; P-3 dissents arguing for FR-watch-only with calibration-EF accumulation as the trigger. Minority M-1 preserves P-3 dissent: 56-session non-use as substantive empirical evidence; folded into synthesis as a calibration-watch FR pairing with the spec-edit FR; if next 5 sessions pass without tactical anchor-trace invocation despite --print landing, that becomes the second data point escalating the discipline-gap reading. The synthesis ships FR-driven not clause-driven this session per operator-named mandate; spec edit and coding work are emitted as forward-references for follow-up sessions, not executed in S173. P-2 cross-family contribution on phrasing (precedent-sensitive provenance check vs run anchor-trace) folds into the spec-edit FR scope. P-2 broader ergonomic batch is preserved as a separate deferred FR scope conditional on observed need post --print landing, honouring P-3 minimalist concern about premature affordance-building. Cites DV-S109-1 ceremony-subtraction, DV-S152-1 typed-observation-to-gate progression, DV-S171-1 self-referential-EF disqualification clause, OI-S114-1 v1 anchor-trace, DV-S116-1 chain-walk scope, DV-S117-1 v1 implementation.

### Synthesis points

- **convergence C-1.** All three perspectives converge: --print stdout mode is the highest-leverage ergonomic affordance; ship via dedicated coding FR.
- **convergence C-2.** All three reject mandatory T-NN substrate gate at engine-v47; promotion only after calibration-EF recurrence per DV-S152-1.
- **convergence C-3.** Defer broader ergonomic batch (--summary --json --limit-open suggested-anchors) to observed-need basis under DV-S109-1 ceremony-subtraction.
- **convergence C-4.** Spec home is §5 decision-record discipline with §8.5 cross-reference; no new dedicated chain-walk section warranted.
- **divergence D-1.** Clause-strength split: P-1 + P-2 majority adopt recommended clause via spec-edit FR; P-3 dissents in favour of FR-watch-only.
- **minority M-1.** P-3 minimalist preserves: 56-session non-use as natural experiment; folded into calibration-watch FR pairing with spec-edit FR.
