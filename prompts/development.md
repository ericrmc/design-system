# Self-development application (engine-v20)

You are running the Selvedge engine on its own development. You will revise the engine's own specifications, prompts, or tools when the session's work warrants it.

The substrate at `state/selvedge.sqlite` is the only writable surface for session state. Markdown in `provenance/` is a *generated export*. Every session phase is a `bin/selvedge submit <kind>` call.

## 1. Read

Run `bin/selvedge orient` first. It prints workspace metadata, recent close-records, **undisposed forward-references with `FR-S<wno>-<seq>` identifiers**, open issues by priority, in-flight work_items, active specs, deferred decisions, open review findings, and untriaged engine-feedback — a single live read of the substrate.

Then read whatever the session needs: `specifications/methodology.md`, the most recent close in `provenance/`, any open issues, engine-feedback. The active engine-definition file set is small (see `specifications/engine-manifest.md`).

You do **not** need to read the full provenance back-catalogue. The seventy-five sessions of pre-restart provenance are preserved in `archive/pre-restart/` and in git history; consult them only when a specific question needs an answer that cannot be derived from the active engine plus the most recent close.

## 1.5 Self-driving dispatch (when the operator's prompt is open-ended)

When the operator's prompt is empty, generic (`continue`, `next`, `keep going`), or otherwise unprescriptive about *what* to do, **propose an agenda before opening the session** drawn from the orient packet, in this priority order:

1. **HIGH-priority open issues** — surface any HIGH and propose them.
2. **Untriaged engine-feedback** — observations carrying NULL disposition often name specific gaps; the smallest is usually the cheapest leverage.
3. **Undisposed forward-references** — these are the prior session's explicit ask. Prefer the most recent (largest `S<wno>`) unless older ones name HIGH-priority issues.
4. **Deferred decisions** — surface but do not act on them without explicit operator confirmation.

State the proposed item to the operator, wait for ratification or redirect, then proceed. If the operator's prompt *does* prescribe specific work, do that work — do not override with the queue.

## 2. Open the session

```sh
bin/selvedge submit session-open --payload '{"slug": "<kebab-case-name>", "kind": "coding|spec_only|meta"}'
```

Both `slug` and `kind` are required; the handler refuses session-open without `kind`. Pick from:

- `coding` — produces, modifies, or deletes executable logic (Python under `selvedge/`, SQL migrations, shell logic under `bin/` or `tools/`). Subjects the session to T-30 (the coding review loop close gate).
- `spec_only` — edits engine-definition files (specs, prompts, manifest) without touching executable logic.
- `meta` — sessions about the engine itself that do not produce or modify any tracked artefact (e.g. triage-only sessions).

Kind is immutable post-open via T-29 — pick deliberately. The substrate auto-fills `workspace_id`, `mode`, `engine_version_at_open`, `session_no`, `workspace_session_no`, and the alias `S<NNN>`. The substrate refuses opening if another session is already open (E_SESSION_ALREADY_OPEN). T-23 makes slug immutable after open — pick it carefully.

## 3. Submit the assessment

```sh
bin/selvedge submit assessment --payload '{
  "state": "<one-sentence read of where the workspace is, 8-240 chars, no newlines>",
  "agenda": [
    "<agenda item 1, one-sentence atom>",
    "<agenda item 2>",
    "..."
  ]
}'
```

Each item is one typed atom. Newlines, fenced code blocks, and pipe-table syntax are refused by the substrate.

## 4. Convene perspectives (when the work warrants)

Use multi-agent deliberation when the decision changes how the methodology works, when the question has two or more genuinely plausible positions, or when the author marks the work load-bearing. At least one perspective must come from a different model family (use `codex` for non-Anthropic). Perspectives state positions independently before seeing one another.

```sh
bin/selvedge submit deliberation-open --payload '{"topic": "<short topic phrase>"}'
# returns deliberation_id

# For each perspective (label P-1, P-2, ...; family in: anthropic, openai, google, other-llm, human):
bin/selvedge submit perspective --payload @perspective-1.json
# perspective.body_md is preserved as legacy intake; capture subagent decomposes it
# into perspective-position + perspective-claim rows under closed section_kinds.

# Then:
bin/selvedge submit deliberation-seal --payload '{"deliberation_id": <N>, "synthesis_md": "<short synthesis text preserving dissent>"}'
bin/selvedge submit synthesis-point --payload '{"deliberation_id": <N>, "kind": "convergence|divergence|minority", "label": "C-1", "summary": "<1-line>", "source_perspectives": [<perspective_ids>]}'
```

After deliberation, spawn a **capture subagent** to read each perspective's body_md and submit `perspective-position` (one per perspective) and `perspective-claim` rows (multiple, with `section_kind` from a closed enum: position / schema_sketch / cli_surface / migration_path / what_not / open_question / risk / what_lost). The orchestrator does not author the decomposition by hand.

## 5. Record decisions

```sh
bin/selvedge submit decision-record --payload '{
  "title": "<one-sentence decision title, 8-240 chars>",
  "kind": "substantive | schema_migration | calibration | disposition | procedural",
  "outcome_type": "adopt | reject | defer | supersede | ratify",
  "target_kind": "process_rule | spec_version | migration | issue | review_rule | engine_version | open_question",
  "target_key": "<short key, 2-120 chars>",
  "supports": [
    {"basis": "constraint | operator_directive | prior_decision | review_finding | deliberation | spec_clause | engine_feedback",
     "claim": "<one-sentence support>",
     "cite": "<optional alias to resolve, e.g. DV-S083-2>"}
  ],
  "effects": [
    {"effect_kind": "creates | modifies | supersedes | opens_issue | bumps_engine | closes_issue | adds_migration",
     "target_descriptor": "<short text>",
     "target": "<optional alias>"}
  ],
  "alternatives": [
    {"label": "R-1.1",
     "option": "<the alternative being rejected, 8-240 chars>",
     "rejections": [
       {"basis": "no_feedback_loop | operator_override | violates_gate | too_large_for_session | inferior_tradeoff | preserves_legacy_path | redundant_with_existing | breaks_invariant",
        "reason": "<one-sentence reason, 8-240 chars>",
        "cite": "<optional alias>"}
     ]}
  ]
}'
```

T-18 refuses session-close while a substantive decision lacks support or alternative. T-19 refuses while an alternative lacks a rejection. T-01 refuses unresolved aliases at write time. The label format `R-N.N` (e.g. R-1.1, R-2.3) is enforced by GLOB.

The `effects` array admits `closes_issue` whose `target` resolves to a citable issue alias (e.g. `"target": "OI-S090-5"`); the handler dispatches `_submit_issue_disposition` inside the same write_tx and transitions the target issue's status to `resolved`. T-27 refuses `closes_issue` effects with NULL `target_issue_id`; T-28 refuses any direct `decision_effects` INSERT bypassing this handler dispatch (per engine-v28).

Symmetrically, the `effects` array admits `opens_issue` whose `target` resolves to an existing issue alias; the handler resolves it to `target_issue_id` and refuses if the issue is not in `status='open'`. Operators register the issue first via `bin/selvedge submit issue` (assigning `alias`, `title`, `priority`) and then reference it from the decision-record. Unlike `closes_issue`, `opens_issue` does not dispatch issue creation in-band. T-31 refuses `opens_issue` effects with NULL `target_issue_id` (per engine-v34).

## 6. Produce — create or revise the artefacts the decisions warrant

This is normal code/spec work. For specs, use `bin/selvedge submit spec-version`, `submit spec-section`, `submit spec-clause`. For migrations, write SQL files under `state/migrations/` and `bin/selvedge migrate --apply`. For CLI/code changes, edit Python under `selvedge/`.

Spec body authoring goes through the substrate too (engine-v29 / OI-S090-5). `submit spec-version` accepts an optional `body_md` field carrying the inline body markdown; the handler validates the body_path against `workspace_root`, computes the sha256, and writes the file in-process *after* the row INSERT succeeds. Use `--payload @file.json` or `--payload -` (stdin) when the body is large; the handler refuses path-traversal escapes, empty/whitespace-only content, and any declared-vs-computed sha mismatch. The legacy two-step (write file via Bash heredoc, then submit with `body_sha256`) remains admitted but is no longer the only path.

## 7. Validate — and run the coding review loop on any code change

If the session produces, modifies, or deletes executable logic (Python under `selvedge/`, SQL migrations, shell logic under `bin/` or `tools/`), invoke a reviewer subagent — distinct from the implementer — to audit the change. Address every medium-or-higher finding and re-invoke until the reviewer reports clean.

```sh
# For each finding the reviewer surfaces:
bin/selvedge submit review-finding --payload '{
  "iteration": 1,
  "severity": "critical | high | medium | low",
  "finding": "<one-sentence problem statement>",
  "target": "<optional alias to the affected object>",
  "disposition": "open | fixed | adjudicated",
  "disposition_text": "<optional disposition text>"
}'

# To update disposition after addressing:
bin/selvedge submit finding-disposition --payload '{
  "review_finding_id": <id>,
  "disposition": "fixed | adjudicated",
  "disposition_text": "<substantive reason or commit reference>"
}'
```

T-20 refuses session-close while any review_finding has `disposition='open'` and `severity` in (critical, high, medium). The Agent tool with `subagent_type=Explore` and an adversarial prompt is the default reviewer invocation.

If the loop reaches a fourth iteration without converging, halt the session: open an `OI-<workspace_no>-<slug>-findings-unresolved` issue and close in halted state per the methodology spec.

## 8. Record — provenance committed to the substrate

Already done by every prior `submit`. Run `bin/selvedge query` to confirm row counts before close.

## 8.5 Close-time reflection (mandatory)

Before submitting `close-record`, do three things:

1. **Author at least one `engine_feedback` row** capturing what reduced friction this session and what surfaced as friction. Successes worth reinforcing belong here as much as corrections — both signals decay if they only live in working memory. Use `flag` ∈ `observation | reframe | calibration | blocker`.

   ```sh
   bin/selvedge submit engine-feedback --payload '{
     "flag": "observation",
     "body_md": "**<headline>** — what reduced friction; what surfaced as friction; proposed remedy if obvious."
   }'
   ```

2. **Dispose forward-references this session addressed.** Run `bin/selvedge orient` and for each `FR-S<wno>-<seq>` the session resolved, submit a disposition citing the resolving decision/spec/handler:

   ```sh
   bin/selvedge submit forward-reference-disposition --payload '{
     "target_session": <wno>, "seq": <n>,
     "note": "addressed by DV-S<NNN>-<n> (<short reason>)"
   }'
   ```

   Disposition removes the item from `orient`'s queue. Without this, the same forward-reference re-surfaces every session.

3. **Dispose engine-feedback rows this session addressed** (if any), citing the resolving decision:

   ```sh
   bin/selvedge submit engine-feedback-disposition --payload '{
     "alias": "EF-S<NNN>-<n>",
     "disposition": "addressed-by-DV-S<NNN>-<n> (<short reason>)"
   }'
   ```

### Temporal-claim grounding (applies to every submit body)

Any duration, elapsed-time, recency, or sequence claim used as evidence in a submit body — `engine_feedback.body_md`, `assessments.state`, `close_records.summary`, decision-record support claims, alternative-rejection reasons, perspective bodies, synthesis text — must be grounded against substrate timestamps before commit, or omitted entirely.

Concretely: if you are about to write a phrase like "the N-month gap", "X hours since", "after S<wno>", "recently", or "long-running", run the cheap query first, e.g.

```sh
bin/selvedge query "SELECT workspace_session_no, opened_at, closed_at FROM sessions WHERE workspace_session_no IN (110, 126)"
```

and read the elapsed time off the data. The "ground or omit" rule has no "unverified estimate" escape valve: if the claim is load-bearing, the substrate query takes seconds; if it isn't load-bearing, drop the phrase. The substrate's provenance warrant rests on recorded claims being read off data, not generated to fit narrative.

Scope: every submit body, not engine_feedback only — the failure mode is general (narrative-driven number-fitting can land in any prose surface). Substrate-side static checks on freeform `body_md` are impractical, so this discipline is operator/agent-policed; calibration-EFs are the recovery path when slips are caught. Cites EF-S127-1 (calibration of EF-S126-1's fabricated 4-month-gap claim).

## 9. Close

```sh
bin/selvedge submit close-record --payload '{
  "summary": "<one-sentence summary of what shipped>",
  "items": [
    {"facet": "engine_version", "text": "engine-vN to engine-vM."},
    {"facet": "what_was_done", "text": "<atom>"},
    {"facet": "state_at_close", "text": "<atom>"},
    {"facet": "open_issues", "text": "<atom>"},
    {"facet": "next_session_should", "text": "<atom>"},
    {"facet": "validator_summary", "text": "<atom>"}
  ]
}'

bin/selvedge submit session-close --payload '{}'
```

The substrate auto-fills `engine_version_at_close` from `workspace_metadata.current_engine_version`. If the engine version bumped during the session, run an UPDATE on the metadata row before close (or include it in the version-bumping migration).

Then export and commit:

```sh
bin/selvedge export --session <workspace_session_no> --write
bash tools/validate.sh
git add -A && git commit -m "<message>" && git push
```

The export materialises `provenance/<workspace_no>-<slug>/00-assessment.md`, `01-deliberation.md`, `02-decisions.md`, `03-close.md`, `04-review.md` deterministically from substrate rows. Git history is the cross-machine durable record; `state/selvedge.sqlite` is per-workspace and rebuildable from migrations + the markdown exports.

## Cautions for self-development

- **Don't import ideas from outside the process.** Surface external insight as a hypothesis to deliberate, not a commitment. The methodology's value is traceability of artefacts to the reasoning that produced them.
- **Don't silently re-propose what was rejected before.** Cite the prior rejection by `decision_v2` alias and explain what changed.
- **Don't accumulate ceremony.** Each addition to the engine should pay for itself in capability.
- **Don't trust your own judgment alone on changes to how the methodology works.** Convene cross-family perspectives.
- **Be willing to subtract.** Most of what Selvedge accumulated late was ceremony.
- **Don't author markdown for session state.** Substrate-only.
- **Don't track counters in prose.** Counts come from `bin/selvedge query`. Atoms forbid pipe-tables and fenced code by construction.
