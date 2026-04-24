---
session: 050
title: Close — Path AS (Adoption-Scheduled) reified at n=2 via pre-scheduled 4-perspective two-family MAD on EF-047-retrieval-discipline; 14 decisions D-163–D-176 including new engine-definition spec specifications/retrieval-contract.md v1 + engine-adjacent tooling (tools/build_retrieval_index.py + tools/retrieval_server.py + specifications/aliases.yaml + .mcp.json) + bootstrap-script substrate-install extension + workspace-structure.md v5→v6 (+ §10.4-M7 through §10.4-M11 preserving 5 first-class minorities from the MAD) + engine-v8→v9 substantive bump + WX-50-1 phase-2 gate (retrieval-substrate-use recording across S050–S053); D-133 M2 third-of-3 verification window vindicated; §5.6 GPT-family-concentration fourth-consecutive-worst-case-side continues forward observation; WX-43-1 OI-promotion discharged-as-not-warranted; 31→36 preserved first-class minorities; 0 new / 1 triaged / 3 resolved / 0 rejected engine-feedback state (EF-047-retrieval-discipline + EF-047-session-inputs transitioned to resolved at S050; EF-047-brief-slot-template deferred to next arc-exercise session per D-174); Path AS reified; D-129 sixth-consecutive exercise clean; D-138 fifth-consecutive folder-name default exercise clean; WX-28-1 twenty-first close-rotation zero retention-exceptions; WX-24-1 23rd-session MAD-v4-no-growth new record; SESSION-LOG Q5=(a) thin-row discipline applied (≤180 words); first-ever engine-v-bump driven by MAD-adopted new engine-definition spec (new bump-provenance class)
date: 2026-04-24
status: complete
---

# Close — Session 050

## §1 Artefacts produced

### §1a Provenance (`provenance/050-session/`)

- `00-assessment.md` (2,965 words; commit `e5e69fd`) — pre-operator-ratification per D-017 spirit. Proposed Path AS 2nd-instance execution of S049 D-159 pre-scheduled MAD; routed operator §2a corrections + Q6 scope expansion through Halt 1 rather than silent incorporation; six Halt-1 questions with recommended defaults.
- `01-brief-shared.md` (3,492 words; commit `014e733`) — MAD shared brief, immutable-at-commit per MAD v4 §Brief immutability. §0 operator ratifications verbatim (S048/S049/S050 Halt-1 + Q6 scope expansion); §0b §5.6 worst-case-side disclosure; §0c WX-43-1 do-not-self-commit standing instruction; §0d WX-44-1 codex-CLI no-repo-wide-search; §1 deliberation context; §2a correction-overlay; §2b Halt-1 Q6 external-application-portability load-bearing; §4 eight Q1–Q8 neutrally labelled; §5 four-perspective stance briefs; §6 deliberation rules; §7 output format; §8 honest limits.
- `01a-perspective-substrate-architect.md` (6,329 words) — P1 Claude neutral surveyor (per Halt-1 Q4 amendment). Top-line: Substrate-1 SQLite FTS5 primary; phased adoption with phase-1 = 3 tools; engine-definition classification for Q7.
- `01b-perspective-incrementalist-skeptic.md` (5,142 words) — P2 Claude. Top-line: Substrate-1 SQLite FTS5 phase-1-minimum with 2 tools only; engine-adjacent (not engine-definition); lazy mtime rebuild; 6 things deliberately-not-in-phase-1; phase-2 go/no-go gates.
- `01c-perspective-outsider-frame-completion.md` (2,069 words; verbatim from codex exec) — P3 Codex/GPT-5.5 xhigh. Top-line: reframes substrate-as-fact-discipline; surfaces Substrate-N1 retrieval-ledger + Substrate-N2 structured-artefacts-as-source-of-truth + Substrate-N3 write-time-registries-plus-generated-read-model; middle-path portability (engine-defined contract + engine-adjacent implementation). Named three Claude shared-frame blind spots.
- `01d-perspective-cross-family-reviewer.md` (1,990 words; verbatim from codex exec) — P4 Codex/GPT-5.5 xhigh. Top-line: forensic audit of P1 (highest laundering risk: full-kit surface preserved under phased labelling) + P2 (operator-framing-closes-defer launders; resolve_id smuggles identifiers table); 5 first-class minorities recommended for preservation.
- `01-deliberation.md` (2,819 words) — synthesis. D-133 M2 Convene-time matrix populated; §5.6 GPT-family-concentration observation; WX-43-1 4-of-4 clean + cumulative n=0-of-9 window; Q1–Q8 convergence/divergence map; phase-1 architecture; phase-2 WX-50-1 gate; 5 preserved first-class minorities; shared-frame-blindness assessment.
- `02-decisions.md` (~5,200 words) — 14 decisions D-163–D-176. D-163 operator Halt-1 ratifications + Q6 verbatim. D-164–D-171 Q1–Q8 resolutions. D-172 new engine-definition spec `specifications/retrieval-contract.md` v1 + engine-v8→v9. D-173 WX-50-1 phase-2 gate + 5 first-class minorities. D-174 bundled-minor dispositions. D-175 D-133 M2 third-of-3 vindication. D-176 housekeeping 14-item.
- `participants.yaml` + `manifests/{substrate-architect,incrementalist-skeptic,outsider-frame-completion,cross-family-reviewer}.manifest.yaml` — MAD provenance per MAD v4 §Record.
- `codex-outsider-prompt.txt` + `codex-outsider-raw-output.log` — codex-call provenance for P3.
- `codex-cross-family-reviewer-prompt.txt` + `codex-cross-family-reviewer-raw-output.log` — codex-call provenance for P4.
- `03-close.md` — this file.

No archive subdirectories; no external-artefact in self-dev; no `STATUS.md` (not a long-running session).

### §1b Specification changes THIS session

**Substantive (engine-definition)**:
- `specifications/retrieval-contract.md` **v1 NEW** (~3,500 words) — declares phase-1 retrieval contract + WX-50-1 phase-2 gate + 5 preserved first-class minorities §7.1–§7.5 mirrored with workspace-structure.md v6 §10.4-M7–M11.
- `specifications/workspace-structure.md` v5 → **v6** substantive (+5 §10.4 minorities). `workspace-structure-v5.md` preserved as superseded witness.
- `specifications/engine-manifest.md` (documentary; §2 engine-v8→v9; §3 adds retrieval-contract.md entry; §7 new engine-v9 entry). Frontmatter `updated-by-session: 050`.

**Engine-adjacent tooling (NOT in `engine-manifest.md` §3)**:
- `tools/build_retrieval_index.py` — new (~290 LOC SQLite FTS5 indexer with ID regex registry + alias remap + integrity check).
- `tools/retrieval_server.py` — new (~270 LOC FastMCP stdio server with session-open mtime rebuild + freshness reporting + structured failure-mode response).
- `specifications/aliases.yaml` — new (schema_version 1 + 8 seed entries).
- `.mcp.json` — new (project-scoped `selvedge-retrieval` server registration).
- `.gitignore` — amended (added `.cache/` exclusion).
- `tools/bootstrap-external-workspace.sh` — amended (§3e copies engine-adjacent tooling; next-steps block prints pip-install + index-build instructions).

**Unchanged engine-definition files**: `PROMPT.md`; `MODE.md`; `prompts/development.md`; `prompts/application.md`; `methodology-kernel.md` v6; `multi-agent-deliberation.md` v4; `validation-approach.md` v5; `identity.md` v2; `reference-validation.md` v3; `read-contract.md` v5; `tools/validate.sh`.

### §1c Development-provenance files amended (WX-35-1 claim discipline)

Per WX-35-1 standing discipline, each claimed file amendment is verified via `git log --oneline <path>` at close and explicitly retracted if not committed.

- **`SESSION-LOG.md`** — **WILL BE EDITED at close commit** (thin-row per Q5=(a) ≤180 words).
- **`engine-feedback/INDEX.md`** — **EDITED** (status summary 0 new / 3 triaged / 1 resolved → 0 new / 1 triaged / 3 resolved; three rows amended to reflect S050 D-174 dispositions).
- **`engine-feedback/triage/EF-047-retrieval-discipline-and-text-system-scaling-ceiling.md`** — **EDITED** (status triaged → resolved; disposition body rewritten; `resolved_at/resolved_in_session/resolution_decisions/engine_version_impact` added).
- **`engine-feedback/triage/EF-047-session-input-files-redundant-with-verbatim-capture.md`** — **EDITED** (status triaged → resolved; resolution-fields added per D-174).
- **`engine-feedback/triage/EF-047-brief-slot-template-hidden-arc-leakage.md`** — **EDITED** (disposition revised to defer-to-next-arc-exercise; `scheduled_mad_session: null` + `deferred_*` fields added per D-174).
- **`specifications/retrieval-contract.md`** — **CREATED** (this close commit).
- **`specifications/workspace-structure.md`** — **EDITED** (v5→v6; §10.4 extension).
- **`specifications/workspace-structure-v5.md`** — **CREATED** (superseded witness).
- **`specifications/engine-manifest.md`** — **EDITED** (engine-v8→v9 documentary; frontmatter + §2 + §3 + §7 new entry).
- **`specifications/aliases.yaml`** — **CREATED**.
- **`tools/build_retrieval_index.py`** — **CREATED**.
- **`tools/retrieval_server.py`** — **CREATED**.
- **`.mcp.json`** — **CREATED**.
- **`.gitignore`** — **EDITED** (added `.cache/`).
- **`tools/bootstrap-external-workspace.sh`** — **EDITED** (§3e added; SPEC_FILES includes retrieval-contract.md; next-steps updated).
- **`tools/validate.sh`** — **NOT edited** (check 24 deferred per D-171).
- **`open-issues/*`** — **NOT edited** per WX-35-1 explicit retraction discipline. No OI opened/resolved/amended this session. OI-019 cross-referenced in retrieval-contract.md §1 but OI body unchanged.
- **`open-issues/index.md`** — **NOT edited**. Active OI count 13 unchanged.
- **`PROMPT.md`, `MODE.md`, `prompts/development.md`, `prompts/application.md`, `CLAUDE.md`** — **NOT edited**.
- `provenance/050-session/*.md` + `participants.yaml` + `manifests/*.yaml` + codex-prompt/log files — **CREATED** across three commits (`e5e69fd` 00-assessment; `014e733` MAD preparation; this close commit the remainder).

### §1d Validator status at close

Pre-SESSION-LOG-row: PASS with one expected fail (Session 050 SESSION-LOG row not yet written). Warnings: 9 (6 × decisions-no-rejected-alternatives S046/S047/S048 design + 3 × word-count soft-warnings MAD 6637 / reference-validation 7160 / SESSION-LOG pre-row 7951). Aggregate default-read surface: pre-row post-adoption forecast ~72,000 words across 20 files (added `retrieval-contract.md` ~3,500; workspace-structure.md gained ~850; SESSION-LOG row adds ~180 at close). Well under §2b 90K soft ceiling (~18K headroom).

Post-SESSION-LOG-row: expected PASS, 0 fails, 9 warnings (SESSION-LOG post-row forecast ~8,130 — breaching 8K hard ceiling by ~130 per D-176 §9 flagging; S051 forced-restructure candidate).

### §1e Engine-version status THIS session

**Engine-v9 established** at S050 close per D-172 (first engine-v-bump driven by MAD-adopted new engine-definition spec). Engine-v8 preservation window closed at depth 2 (S049 + S050-pre-adoption-state). Engine-v9's own preservation window starts post-S050-close at depth 0.

## §2 Operational warrants changed or advanced

1. **Path AS (Adoption-Scheduled) reified at n=2.** S049 first-instance + S050 second-instance (pre-scheduled at S048 D-155 + S049 D-159; ran as pre-scheduled MAD without mid-ratification reshape). Path AS is now a reified default-agent path-label.
2. **D-133 M2 third-of-3 verification window vindicated per D-175.** S045 + S047 + S050 all exercised Convene-time 7-column matrix + Outsider-non-Claude lineage-constraint + synonym-drift guard + departure-discipline. M2 graduates to vindicated-as-routine-practice.
3. **§5.6 GPT-family-concentration fourth-consecutive-worst-case-side data point.** 2 Codex + 2 Claude + 0 non-GPT-non-Claude. Per `01-deliberation.md §5` synthesis: P3+P4 non-Claude contribution was substantive and load-bearing (no shared-frame collapse). Spirit-level observation carries forward without discharge/vindication this session; deserves future MAD with non-GPT non-Claude participation.
4. **WX-43-1 cumulative explicit-instruction-variant n=0-of-9** (S047 + S049 + S050). All 4 S050 perspectives honoured the do-not-self-commit instruction. Baseline-window n=6-of-8 closed at S045 (OI-promotion threshold was met but not promoted per pattern-consistency). Per D-176 item 8: **WX-43-1 OI-promotion discharged-as-not-warranted** at S050 close.
5. **WX-28-1 twenty-first close-rotation zero retention-exceptions.** S044 rotates OUT; S050 close enters. Streak continues vindicated.
6. **WX-24-1 MAD v4 no-growth twenty-third-session streak.** `multi-agent-deliberation.md` v4 unchanged at S050. New record from the S042 reset point.
7. **WX-34-1 SESSION-LOG word-count pressure: Q5=(a) thin-row discipline applied.** Pre-row 7,951 → post-row forecast ~8,131, breaching 8K hard ceiling by ~131. S051 forced-restructure candidate (WX-34-1 forward observation: if S051 opens above 8K hard, the restructure is forced).
8. **D-129 standing discipline sixth-consecutive clean exercise.** S046/S047/S048/S049/S050/this-session 00-assessment §5b surfaced five considered-and-rejected session-shape alternatives with non-vacuous rationales. Convention remains operational.
9. **D-138 folder-name default fifth-consecutive exercise clean** (S046/S047/S048/S049/S050). `050-session` no suffix, no slug.
10. **First-ever engine-v-bump driven by MAD-adopted new engine-definition spec** (new bump-provenance class). Prior classes: preserved-minority activation (v2–v6); operator-surfaced mid-session deliberation (v7); operator-directed-resolution of inbox record (v8); MAD-adopted new engine-definition spec from inbox record (v9).
11. **§10.4-M2 (Skeptic-preserver premature-feedback-pathway) continued preservation.** Pathway exercised at adoption edge: three EF-047 records transition triaged→resolved (or triaged→deferred) without structural retrofit. Continued preservation consistent.
12. **§10.4-M5 (Reviser OI-tag-only discharged-as-vindicated) unchanged.** No re-activation trigger.
13. **Session-inputs practice-adoption observation preserved in retrieval-contract.md §5** rather than as separate spec amendment (per D-174). This preserves the discipline without adding a new file or bumping a second spec.
14. **5 new first-class minorities preserved (§10.4-M7 through §10.4-M11).** Count 31→36. Each carries specific activation warrant with reopen conditions — see `workspace-structure.md` v6 §10.4 and `retrieval-contract.md` v1 §7 (mirrored).

## §3 Engine-v disposition and preservation depth

**Engine-v9 established at S050 close; preservation window count = 0.**

Engine-v8 preservation window closed at depth 2 (S049 + S050-pre-adoption-state). Engine-v9 is the eighth engine-v-bump overall and the fifth post-cadence-maturation content-driven bump. §5.4 Session 022 engine-v-cadence minority does NOT re-escalate per the content-driven-bump precedent chain (v5/v6/v7/v8/v9).

Forward observation: engine-v9 preservation window will close at depth TBD. Phase-2 substrate extensions (edges/frontmatter_kv/warrants_currently_met/validator check 24/kernel §1a soft amendment) if triggered by WX-50-1 would produce engine-v10 at that phase-2 adoption session.

## §4 Preserved first-class minorities at S050 close

**36 first-class minorities preserved engine-wide at S050 close** (31 at open + 5 new from this MAD). Full enumeration in `specifications/workspace-structure.md` v6 §10.4 (with §10.4-M7 through §10.4-M11 mirrored in `retrieval-contract.md` v1 §7.1–§7.5).

The 5 new minorities:
- **§10.4-M7** P2 minimum-adoption / defer-with-instrumentation.
- **§10.4-M8** DuckDB structured-first substrate.
- **§10.4-M9** P1 engine-definition-at-adoption.
- **§10.4-M10** Substrate-N2 structured-artefacts-as-source-of-truth reframe.
- **§10.4-M11** `syncs_with:` declaration-of-intent distinction.

No minority discharged this session. Pre-S050 31-count preserved unchanged.

## §5 Watchpoints status at S050 close

- **WX-24-1** — MAD v4 stable 6,637 words. **Twenty-third-session no-growth streak** (S043–S050). New record.
- **WX-24-3** — reference-validation label discipline n=8 stable.
- **WX-27-1** — stable.
- **WX-28-1** — **21-of-21** close-rotation zero retention-exceptions. Streak continues.
- **WX-33-2** — reference-validation.md v3 7,160 words stable.
- **WX-34-1** — **SESSION-LOG soft-warning + hard-ceiling breach forecast**; Q5=(a) thin-row discipline applied. S051 forced-restructure candidate.
- **WX-35-1** — standing discipline applied cleanly; explicit retractions recorded in §1c.
- **WX-43-1** — cumulative explicit-instruction variant n=0-of-9 (S047+S049+S050). **OI-promotion discharged-as-not-warranted** per D-176 item 8.
- **WX-44-1** — codex-CLI independence-phase breach n=3 across S044+S045+S047. Not re-exercised at S050 (no codex search; §0d standing instruction). Forward-convention candidate (no repo-wide search from inside codex) held cleanly at S050 per P3 + P4 manifest transport_notes.
- **WX-44-2** — codex CLI model-version-drift discipline: exercised at S050 per P3 + P4 manifests (model_id verified from `~/.codex/config.toml` default rather than pattern-copied). Clean.
- **WX-47-1** — codex-CLI argv `---` YAML parsing fragility. Stdin-pipe workaround applied at S050 per P3 + P4 manifests. Clean.
- **WX-50-1 NEW (per D-173)** — retrieval-substrate-use recording through S053; phase-2 gate. See `retrieval-contract.md` v1 §6.

## §6 Retrieval substrate use (WX-50-1)

Per D-173, every session close through S053 records substrate use in 3 fields:

- **tool_calls_by_type**: `{search: 0, resolve_id: 0}` — substrate was built and committed in this session's adoption arc; no session-work queries were issued against it.
- **results_used_with_artefact_id**: `[]` — none.
- **fallbacks_due_to_missing_capability**: `[]` — none recorded this session.

**Note on S050 zero-use**: S050 is the adoption session; tool use begins at S051. This zero-value entry is a baseline anchor, not a phase-1-failing signal. WX-50-1 gate evaluation at S053 close considers S051/S052/S053 usage primarily; S050 counts as the adoption anchor.

## §7 Next-session items and forward observations

**Session 051 recommendation**: default-agent session. Priorities:
- **WX-34-1 forced-restructure trigger**: if S051 opens above 8K SESSION-LOG hard ceiling (forecast ~8,130 post-S050 close), S051 MUST restructure the SESSION-LOG at open per WX-34-1 forward observation. Approach similar to S040 D-123 compression (bundle older rows as archive-pack; thin-row the recent surface).
- **Substrate first actual use**: any read operation S051 needs to perform on the corpus should consider whether `mcp__selvedge_retrieval__search(...)` or `mcp__selvedge_retrieval__resolve_id(...)` would answer it. Record use in the WX-50-1 3-field section at S051 close.
- **External-application arc progression**: `selvedge-disaster-response` arc S002–S005 pending operator transport; substrate is now available to external-application workspaces via bootstrap-refresh (operator-discretionary).
- **Post-arc self-dev review obligation** (carrying from S047 D-150): three remaining deferred spec-amendment candidates (i)+(ii)+(iii) preserved for post-arc review. Candidate (iv) subsumed at S048 by D-153.

**S051 close should evaluate**:
- WX-34-1 disposition (restructured or breach-persists).
- WX-50-1 phase-2-gate accumulated signal (0-or-more results-used entries).
- Engine-v9 preservation (window count starts at S051).
- D-129 seventh-consecutive exercise (if default-agent session shape).
- D-138 sixth-consecutive folder-name default.
- §5.6 fifth-consecutive data point (if MAD convenes; else N/A).

## §8 Honest limits at close

- **Substrate smoke-test not run in-session.** The indexer and MCP server were written but not executed at session close (the `python3 tools/build_retrieval_index.py` and MCP-server validation steps were not performed). Code review only; no runtime verification. S051 open should exercise the substrate as its first substantive read operation and record any defects as engine-feedback.
- **Validator passes with 9 warnings + the expected Session 050 SESSION-LOG row fail until post-close-commit.** Warnings are the same three word-count soft-warnings (MAD 6637 / reference-validation 7160 / SESSION-LOG 7951→forecast 8131 hard-ceiling breach) plus six decisions-no-rejected-alternatives design-intent entries for S046/S047/S048.
- **P1 Substrate Architect's internal inconsistency** (P4 audit §1 laundering flag): the Architecture §3 proposed full-kit surface while Q2 answer was phased. Synthesis adopted P2/P4's narrower phase-1 scope (2 tools, not P1's 3); P1's list_identifiers proposal deferred to phase-2 per D-165. This is not a P1 failure; P4's audit-flag was load-bearing and resolved correctly in synthesis.
- **P2 Incrementalist Skeptic's technical under-specification** (P4 audit §2): resolve_id requires an identifiers table which P2's pure-FTS phase-1 rejected. Synthesis resolved by keeping identifiers table in phase-1 (D-165).
- **Substrate implementation is engine-adjacent, not engine-definition.** The §10.4-M9 minority preserves the engine-definition-at-adoption alternative; re-evaluation gated on stability evidence + inconsistent-inheritance signal.
- **Phase-2 gate is operator-authoritative.** The WX-50-1 recording convention is specified but the trigger-firing interpretation at S053 close will be a Case Steward call with operator oversight; it is not an automatic decision rule.
- **Bootstrap script extension not smoke-tested on a new workspace.** I modified `tools/bootstrap-external-workspace.sh` to install the substrate but did not run the bootstrap against a fresh target directory. The edits are additive and low-risk (cp commands + a heredoc) but a first-user may surface edge cases.
- **Aliases file seed entries are illustrative, not authoritative.** The 8 seed entries in `specifications/aliases.yaml` demonstrate the schema and give `resolve_id` something to find at S050; they are not a comprehensive alias vocabulary. Population is incremental per convention.

## §9 Aggregate default-read surface impact at close

Pre-close aggregate (post-substantive-edits, pre-SESSION-LOG row + this close file):
- `specifications/retrieval-contract.md` NEW (~3,500 words) — added to default-read.
- `specifications/workspace-structure.md` v5→v6 (+5 minorities ~850 words).
- `specifications/engine-manifest.md` (+1 engine-v9 entry ~650 words).
- `specifications/aliases.yaml` — default-read-eligible per retrieval-contract.md §2.3 but very small (~40 words); does not substantially move aggregate.
- `engine-feedback/INDEX.md` — ~40 words edited (status-summary + 3 row rewrites).
- Three triage files edited — NOT in §1 default-read enumeration per INDEX-only convention.
- Currently-active-session provenance (per read-contract v5 §1 item 8): `00-assessment.md 2,965` + `01-brief-shared.md 3,492` + perspective files (`01a` 6,329 + `01b` 5,142 + `01c` 2,069 + `01d` 1,990) + `01-deliberation.md 2,819` + `02-decisions.md ~5,200` + `03-close.md ~3,600` ≈ 33,606 words.
- On close: session-scope provenance rotates to archive-surface per read-contract v5 §1 item 8. Net default-read gain: +4,950 words (retrieval-contract.md + workspace-structure.md + engine-manifest.md + INDEX.md delta) minus close-rotation of S044 03-close.md (~2,900) = +2,050.
- Validator at open recorded aggregate 67,805 / 19 files. Post-S050-close forecast: **~69,855–70,500 words across 20 files** (SESSION-LOG grows to ~8,131 breaching 8K hard; close-rotation swaps S044 for S050; aliases.yaml enters — default-read-eligible per retrieval-contract.md §2.3). Well under §2b 90K soft ceiling (~19–20K headroom).

Actual aggregate to be reported in validator output post-commit.

## §10 S050 meta-observations

1. **First-ever engine-v-bump driven by MAD-adopted new engine-definition spec** (new bump-provenance class distinct from v2–v8's classes). Provenance pattern: inbox engine-feedback → operator scope revision (S049 D-157) → synthesis session producing design-space → pre-scheduled MAD (S050) → MAD synthesis → adoption with new engine-definition spec.
2. **P3 Outsider frame-completion load-bearing in synthesis.** P3's Substrate-N3 (write-time registries + generated read model) + middle-path portability (engine-defined contract + engine-adjacent implementation) are adopted directly in §2 architecture and D-170 Q7 resolution. Non-Claude contribution was substantive, not ceremonial.
3. **P4 Cross-Family Reviewer laundering audit resolved 2 real issues**: (a) P1 full-kit-vs-phased-labelling inconsistency → P1's `list_identifiers` in phase-1 deferred to phase-2; (b) P2 smuggled-identifiers-table → identifiers table explicitly kept in phase-1. Both fixes visible in D-165.
4. **Synthesis preserves 5 first-class minorities per P4 dissent-preservation recommendation**. Each carries a distinct activation warrant; none is a redundancy or consolation.
5. **Shared-frame-blindness observation**: P4 named the Claude-shared frame (markdown canonical + Python-built index + MCP + bootstrap-copied files + workspace-isolated). P3's Substrate-N1/N2 + middle-path were genuine frame-completion outside this frame. Session 050 is a data point on whether 4-of-4 shared-frame convergence fires or is avoided — **avoided at S050**, per the non-Claude contributions being load-bearing in synthesis. Counts toward EF-047-session-inputs forward observation.
6. **Adoption-scheduling pattern vindicated at n=2.** S048 D-155 → S049 D-159 → S050 MAD-and-adoption is a successful two-step (synthesis + adoption) pattern. Path AS reified.

## §11 Commit and close

This close file is committed with the S050 MAD artefacts (perspective files, deliberation, decisions, retrieval-contract.md, engine-manifest.md v9, workspace-structure.md v6, aliases.yaml, .mcp.json, indexer + server code, bootstrap-script extension, gitignore amendment, engine-feedback INDEX + triage amendments) and the SESSION-LOG thin-row (≤180 words per Q5=(a)).

Engine-v9 stands. 36 first-class minorities preserved. WX-50-1 phase-2 gate active through S053. Path AS reified at n=2.
