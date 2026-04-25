---
session: 059
title: Close — Path T+L bundled scope (Triage of 3 EF-058 inbox records + Path L 6-step uv-migration + records-substrate bootstrap implementation discharge of S058 honest-limit #2 + minor retrieval-contract.md v1 §5.1+§5+§10 template-shape sync); engine-v10 preserved (preservation depth 2); 7 decisions D-206 through D-212; engine-feedback state 3 new / 1 triaged / 7 resolved → 0 new / 3 triaged / 8 resolved (EF-058-uv-migration resolved; EF-058-claude-md-drift + EF-058-tier-2-validation triaged-deferred); WX-58-1 second observation 5-field recording; tenth source-realignment-or-extension precedent chain instance
date: 2026-04-25
status: complete
---

# Close — Session 059

## §1 Artefacts produced

### §1a Provenance (`provenance/059-session/`)

- `00-assessment.md` (~2,070 words; commit `2145ff3`) — pre-work commit per D-017 spirit + S048-S058 precedent chain. Reflects Path T+L bundled scope per intake-disposition + S058 honest-limit #2 follow-up obligation.
- `02-decisions.md` (this close commit) — **seven decisions**: D-206 Path T+L bundled scope ratified `[none]` + D-207 EF-058-uv-migration adopted via 6-step Path L `[none]` + D-208 EF-058-claude-md-drift triaged substantive-arc-deferred `[none]` + D-209 EF-058-tier-2-validation triaged substantive-arc-deferred per operator MAD preference `[none]` + D-210 minor retrieval-contract.md v1 §5.1+§5+§10 template-shape sync amendment `[d016_2]` + D-211 records-substrate bootstrap implementation discharge of S058 honest-limit #2 `[none]` + D-212 housekeeping `[none]` (thirty-first-consecutive).
- `03-close.md` — this file.

No MAD perspectives convened at S059 (default-agent path; no d016_2/d016_3/d016_4 substantive-revision-scale triggers fire).

### §1b Specification changes THIS session

**Zero new engine-definition specs** + **one minor engine-definition spec amendment**.

REVISED (minor per OI-002):
- `specifications/retrieval-contract.md` v1 — §5.1 .mcp.json template (command python3 → uv; args [tools/retrieval_server.py] → [run, tools/retrieval_server.py]) + §5 step 2 dependency-install instructions (pip-install path → uv-only path with PEP 723 self-resolution) + §5 step 3 build-index instruction (python3 → uv run) + §5 closing "does NOT require" list nuance (network access qualifier added for uv first-run dependency resolution exception) + §10 honest-limit "External-workspace portability tax" language (permanent → reduced but persistent; mcp[cli]+pyyaml two-package install → single-tool uv prerequisite) per D-210. Spec content (§1 scope, §2 capabilities, §3 failure behaviour, §4 workspace state, §6 phase-2 gate, §7 minorities, §8 versioning, §9 validation) unchanged. v1 preserved (no version bump per OI-002).

ENGINE-ADJACENT (NOT in §3 enumeration):
- `tools/retrieval_server.py` — PEP 723 inline-deps script block at top: `requires-python = ">=3.11"`; `dependencies = ["mcp[cli]", "pyyaml"]`. Existing ImportError fallback for `mcp[cli]` and `yaml` preserved for direct python3 invocation compatibility.
- `tools/build_retrieval_index.py` — PEP 723 inline-deps script block at top: `requires-python = ">=3.11"`; `dependencies = ["pyyaml"]`. Existing ImportError fallback preserved.
- `.mcp.json` — `command: "python3"` → `command: "uv"`; `args: ["tools/retrieval_server.py"]` → `args: ["run", "tools/retrieval_server.py"]`.
- `tools/bootstrap-external-workspace.sh` — refactored: pip-install instructions → uv-only path; `python3 tools/build_retrieval_index.py` → `uv run tools/build_retrieval_index.py`; `.cache/venv/` setup language removed; `records-contract.md` added to SPEC_FILES array; `records/sessions` directory added to mkdir tree; SESSION-LOG.md scaffolding replaced with thin records/sessions/index.md per records-contract.md v1 §2.2; header documentation lines 20-25 updated; step count "13 files" → "14 files"; engine-adjacent tooling echo extended with PEP 723 inline-deps note.

WORKSPACE STRUCTURE:
- `.cache/venv/` REMOVED from workspace (gitignored; not committed). No tool hardcoded `.cache/venv/bin/python3` paths verified.
- `engine-feedback/inbox/EF-058-*.md` (×3) preserved verbatim (intake-files-preserved-verbatim convention).
- `engine-feedback/triage/EF-058-substrate-runtime-uv-migration-recommended-path.md` — CREATED this close commit per D-207 triage + resolved disposition.
- `engine-feedback/triage/EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` — CREATED this close commit per D-208 triage + substantive-arc-deferred disposition.
- `engine-feedback/triage/EF-058-tier-2-validation-discipline-by-distinct-agent.md` — CREATED this close commit per D-209 triage + substantive-arc-deferred per operator MAD preference disposition.
- `engine-feedback/INDEX.md` — EDITED: status summary `3 new / 1 triaged / 7 resolved / 0 rejected` → `0 new / 3 triaged / 8 resolved / 0 rejected`. Three EF-058 row Status updates with disposition narratives. Note-on-direct-to-inbox-placement extended with EF-058×3 triage at S059 narrative.
- `records/sessions/S059.md` — CREATED this close commit per records-contract.md v1 §2.1.
- `records/sessions/index.md` — EDITED: S059 row appended per records-contract.md v1 §2.2.

### §1c Development-provenance files amended (WX-35-1 claim discipline)

Per WX-35-1 standing discipline, each claimed file amendment is verified via `git log --oneline <path>` at close.

**Pre-close commit (commit `2145ff3`)**:
- `provenance/059-session/00-assessment.md` — CREATED ✓.

**This close commit**:
- `provenance/059-session/02-decisions.md` — CREATED.
- `provenance/059-session/03-close.md` — CREATED (this file).
- `engine-feedback/triage/EF-058-substrate-runtime-uv-migration-recommended-path.md` — CREATED.
- `engine-feedback/triage/EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` — CREATED.
- `engine-feedback/triage/EF-058-tier-2-validation-discipline-by-distinct-agent.md` — CREATED.
- `engine-feedback/INDEX.md` — EDITED (status summary + three rows + note paragraph).
- `specifications/retrieval-contract.md` — EDITED (§5.1 + §5 + §10 minor template-shape sync per D-210).
- `tools/retrieval_server.py` — EDITED (PEP 723 inline-deps).
- `tools/build_retrieval_index.py` — EDITED (PEP 723 inline-deps).
- `.mcp.json` — EDITED (command + args).
- `tools/bootstrap-external-workspace.sh` — EDITED (uv-migration + records-substrate bootstrap per D-211).
- `records/sessions/S059.md` — CREATED.
- `records/sessions/index.md` — EDITED (S059 row appended).
- `.cache/retrieval.db` — REBUILT post-spec-edits (gitignored; not committed); 559 documents / 59,729 identifiers (up from S058 close 549/58,198).

NOT EDITED:
- `PROMPT.md`, `MODE.md`, `prompts/development.md`, `prompts/application.md`, `CLAUDE.md` — unchanged.
- `methodology-kernel.md` v6, `multi-agent-deliberation.md` v4, `validation-approach.md` v5, `workspace-structure.md` v7, `read-contract.md` v6, `identity.md` v2, `reference-validation.md` v3, `records-contract.md` v1, `engine-manifest.md` — all unchanged at engine-v10 boundary.
- `specifications/aliases.yaml` — unchanged.
- `tools/validate.sh` — unchanged.
- `open-issues/*.md` + `open-issues/index.md` — NOT edited (no OI opened/resolved/amended; 13 active OIs unchanged).
- `engine-feedback/inbox/EF-058-*.md` (×3) — NOT edited per intake-files-preserved-verbatim convention.

`.cache/venv/` — REMOVED from workspace (per D-207 step 5; gitignored; not committed).

### §1d Validator status at close

Validator at close: **1370 PASS / 0 FAIL / 27 WARN** (3 spec soft-warnings + 24 design-intent "no rejected alternatives" 2-per-session warnings).

- Aggregate default-read surface: **79,329 words across 22 files** (validator-measured at close, post-close-rotation S054-S059). Headroom to 90K soft: 10,671 words.
- Per-file: `multi-agent-deliberation.md` v4 6,637 words (soft warning; pre-existing); `reference-validation.md` v3 7,160 words (soft warning; pre-existing); `engine-manifest.md` 6,020 words (**NEW soft warning at S059** — crossed 6K threshold post-S058 engine-v10 entry growth).
- Check 20 per-file: 3 soft warnings (MAD + RV + engine-manifest NEW).
- Check 20 aggregate: PASS (79,153 / 90K soft).
- Check 21 archive-pack manifest integrity: PASS (no new archive-packs at S059).
- Check 22 archive-pack citation consistency: PASS.
- Check 23 MODE.md presence: PASS.
- **Check 25 records-substrate integrity**: PASS (58 session records pre-close-commit-of-S059.md; 59 post-close-commit; index rows match; status enum clean; no orphans).

WX-34-1 SESSION-LOG.md ceiling pressure: PERMANENTLY RETIRED (S058 migration; tracked here for record).

**Engine-manifest.md crosses 6K soft warning at S059 close.** First-of-record engine-manifest soft warning. Cause: §7 engine-v10 entry added at S058 grew the file from 5,184 to 6,020. Forward observation: engine-manifest may need accretive-block restructure at engine-v11+ if engine-v entries continue to expand. The §10.4-M10 Substrate-N2 minority's activation warrant tracks this kind of accretive-block pressure; not yet at activation threshold.

### §1e Engine-version status THIS session

**Engine-v10 preserved** at S059 close. Preservation depth: **2** (S058 ratified + S059 preserved).

Engine-v10 preservation trajectory: at start of post-engine-v10 era; n=1 sessions preceded; preservation depth = 1 at S058 close; preservation depth = 2 at S059 close. References: engine-v7 record (11 sessions) and engine-v9 (8 sessions); engine-v10 trajectory unconstrained at this depth.

§5.4 cadence minority does NOT re-escalate per content-driven-bump precedent chain extended to S059 preservation (cadence concern separates from substantive-bump classification; S059 is non-bump session).

## §2 Operational warrants changed or advanced

1. **EF-058-uv-migration resolved within session lifecycle** (S058-post-session-intake → S059 D-207 resolved). Eight-session MCP stdio transport unverified honest-limit chain S051-S058 closes at S059 (modulo next-session-open MCP smoke-test confirming tool surface). Engine-feedback state `3 new / 1 triaged / 7 resolved` → `0 new / 3 triaged / 8 resolved`.

2. **EF-058-claude-md-drift triaged-deferred substantive-arc** (D-208). Methodology observation about S050 MAD shared-frame-blindness against CLAUDE.md operator-standing-instruction; classified substantive-arc-shape per intake disposition; deferred to dedicated future MAD per intake "NOT recommended for same-session resolution" recommendation; cross-linkage with EF-058-tier-2-validation likely produces joint design-space.md if scope-coherent.

3. **EF-058-tier-2-validation triaged-deferred substantive-arc per operator MAD preference** (D-209). Meta-pattern subsuming the other two EF-058 records; classified substantive-arc-shape per S057 EF-055 precedent chain; operator-stated preference at intake "should go through MAD" honoured via deferral; phase-1 synthesis (Path AS Shape-1) → phase-2 4-perspective two-family MAD → phase-3 adoption (engine-v11 highly-likely candidate); bootstrap-paradox feature acknowledged.

4. **Tenth source-realignment-or-extension precedent chain instance** (D-207). Precedent chain S022 R8a / S030 D-100 / S033 D-108 / S040 D-123 / S046 D-143 / S051 D-178 / S052 D-181 / S054 D-186 / S054 D-187 / **S059 D-207+D-210+D-211**. Pattern is engine-conventional for inbox-record-driven defect-fixes: operator surfaces concrete defect with concrete fix path → triage classifies minor → single-orchestrator implements → minor template-shape spec amendments where needed → engine-v preserved.

5. **Records-substrate bootstrap implementation discharges S058 honest-limit #2** (D-211). records-contract.md v1 §5 normative obligations now implemented in tools/bootstrap-external-workspace.sh; external-workspace bootstrap is records-substrate-aware at engine-v10+. First external-workspace bootstrap will be the first-exercise of the path; until then, the implementation is normatively-spec-aligned but not deeply user-tested per honest-limit #3.

6. **Bundled-Path-T+L pattern reified at n=2** (S054 EF-053+EF-054 first-instance; S059 EF-058×3 second-instance with mix of same-session-resolution + deferred-to-future-MAD). The pattern accommodates heterogeneous EF dispositions in a single session: some resolved-same-session, some triaged-and-deferred.

7. **First-of-record post-session-intake-triple event triage** (EF-058×3 at S059). Three related records filed in one S058-post-session discussion (operational + methodological + meta-pattern layers) all triaged in S059; demonstrates the discussion-pattern in which a single operator-surfaced gap surfaces multiple layers in sequence as the discussion deepens.

8. **WX-58-1 second observation 5-field recording at S059 close** per records-contract.md v1 §6 (see §5 below for full 5-field).

9. **D-129 standing discipline fourteenth-consecutive clean exercise** (00-assessment §3b inline; five non-Path-T+L alternatives surfaced).

10. **D-138 folder-name default fourteenth-consecutive clean exercise** (`provenance/059-session/`).

11. **WX-28-1 twenty-ninth close-rotation zero retention-exceptions.** S053 rotates OUT; S059 enters. Retention window post-rotation: S054 / S055 / S056 / S057 / S058 / S059.

12. **WX-24-1 MAD v4 thirty-second-session no-growth streak new record** (17-session run from S042 reset; extends S058's 31-session record).

13. **WX-43-1 explicit-instruction variant** cumulative tracking continues; S059 default-agent path invoked Agent tool (via TaskCreate spawn during planning) but the WX-43-1 baseline tracks Case-Steward-orchestrator perspective-launch invocations; no MAD-perspective invocations at S059. Cumulative n=0-of-13 baseline unchanged.

14. **§5.6 GPT-family-concentration window-ii observation NOT advanced at S059** (no MAD convened; window-ii substantive-deliberation data point chain S044+S045+S047+S050+S058 does not extend at S059). Pattern observation: post-engine-v10 first session is non-MAD; window-ii observation depends on subsequent MAD-involving sessions.

15. **§10.4-M10 written-warrant clause (c) operator-surfacing channel exercised at S059 indirectly** through the EF-058×3 records triage (the records were operator-surfaced post-session intakes). The substantive-arc deliberations for the two deferred records will exercise §10.4-M10-class activation pathway formally if/when phase-1 synthesis adopts.

## §3 Engine-v disposition and preservation depth

**Engine-v10 preserved at S059 close.** Preservation depth: 2.

Engine-v preservation depths (current state):
- engine-v2 (S021 adopted; S022 bump 1-session)
- engine-v3 (S022 adopted; S023 bump 1-session)
- engine-v4 (S023 adopted; S028 bump 5-session)
- engine-v5 (S028 adopted; S033 bump 5-session)
- engine-v6 (S033 adopted; S036 bump 3-session)
- engine-v7 (S036 adopted; S048 bump **11-session** — longest)
- engine-v8 (S048 adopted; S050 bump 2-session)
- engine-v9 (S050 adopted; S058 bump **8-session** — second-longest after engine-v7)
- **engine-v10 (S058 adopted; current preservation depth 2 at S059 close)**.

Candidate triggering events for engine-v11:
- **WX-58-1 phase-2 evaluation at S060 close** per records-contract.md v1 §6 phase-2 gate (mirrored-minority migration may produce minor amendment OR engine-v11 candidate per direction adopted). Note: see §8 honest-limit #4 for resolve_id ordering finding that may affect strict phase-2 gate criterion #2 reading.
- **EF-058-tier-2-validation substantive-arc adoption** (engine-v11 highly-likely candidate per direction adopted; phase-1 synthesis → phase-2 MAD → phase-3 adoption arc).
- **EF-058-claude-md-drift substantive-arc adoption** (engine-v11 candidate per direction (b)/(c) adopted; possibly minor only per direction (a)).
- **EF-047-brief-slot-template resolution** at arc-exercise session (pending operator transport).
- **Operator-surfaced agenda for any engine-definition substantive revision.**

## §4 Preserved first-class minorities at S059 close

**40 first-class minorities preserved engine-wide at S059 close** (unchanged from S058 close). No MAD; no contested deliberation; no new minorities preserved.

§10.4-M10 written-warrant clause (c) operator-surfacing channel exercised indirectly via the EF-058×3 triage but no formal activation of any §10.4-M-N minority at S059.

## §5 Watchpoints status at S059 close

- **WX-24-1** — MAD v4 stable 6,637 words. **Thirty-second-session no-growth streak** (S043–S059). Extends S058's 31-session record. New record (17-session run from S042 reset).
- **WX-24-3** — reference-validation label discipline n=8 stable.
- **WX-27-1** — stable.
- **WX-28-1** — **twenty-ninth close-rotation** (S053 rotates OUT; S059 enters); zero retention-exceptions.
- **WX-33-2** — reference-validation.md v3 7,160 words stable (slight reduction from S058's 7,177 word measurement; possibly measurement variance; within soft warning).
- **WX-34-1** — PERMANENTLY RETIRED (S058).
- **WX-35-1** — standing discipline applied cleanly per §1c above.
- **WX-43-1** — cumulative baseline n=6-of-8 + explicit-instruction variant n=0-of-13 unchanged at S059 (no MAD invocation; baseline does not advance). OI-promotion discharged-as-not-warranted per S050 D-176.
- **WX-44-1** + **WX-44-2** + **WX-47-1** — codex-CLI watchpoints not exercised at S059 (no codex CLI invocation). Cumulative counts unchanged.
- **WX-50-1** — observation window closed at S053; phase-1 paused; phase-1 tools available for organic use. S059 exercised substrate substantively (build_retrieval_index.py rebuild post-spec-edits; substantive index growth from new triage records + 00-assessment + bootstrap-script edits).
- **WX-58-1** — **records-discipline-soak observation second observation at S059 close** per records-contract.md v1 §6.

## §6 WX-58-1 second observation (records-substrate use)

Per `records-contract.md` v1 §6, the WX-58-1 5-field recording obligation applies to sessions S058 through S060 inclusive. S059 second recording:

- **`check_25_status`**: **pass** (validator output: "records-substrate integrity OK: 58 session records pre-close-commit; 59 post-close-commit; index rows match; status enum clean; no orphans").
- **`migrated_id_resolution`**: **58/58 (loose) / 0/58 (strict)** — see §8 honest-limit #4 for finding. Loose interpretation (resolve_id finds the canonical S<NNN> at any path): 58/58. Strict interpretation (resolve_id returns records/sessions/S<NNN>.md as source_path per records-contract.md v1 §2.1 authoritative reading): 0/58 because retrieval_server.py current ordering prefers `specifications/` over `records/` for canonical resolution. S058 first observation reported 58/58 under loose interpretation; carrying-forward strict-vs-loose distinction to S060 phase-2 gate evaluation.
- **`fallback_index_readable`**: **yes** (records/sessions/index.md remains flat-Markdown-readable independent of substrate transport; verified by direct Read tool inspection at S059 open).
- **`record_witness_drift`**: **0** (S059 record + index row added consistently per records-contract.md v1 §2.1+§2.2; check 25 verified).
- **`session_record_added_without_editing_accretive_block`**: **yes** (S059.md created; records/sessions/index.md row appended; SESSION-LOG.md does not exist in workspace post-S058 migration; no accretive-block edit).

**Substrate use at S059**:
- 1 `tools/build_retrieval_index.py` rebuild post-D-207 PEP 723 migration: 557 documents / 59,472 identifiers (intermediate state).
- 1 `tools/build_retrieval_index.py` rebuild post-S059 file-additions: 559 documents / 59,729 identifiers (final state for S059 commit; up from S058 close 549/58,198; +10 documents and +1,531 identifiers attributable to triage records + 00-assessment + 02-decisions + 03-close + S059.md + bootstrap-script edits + retrieval-contract.md edits).
- Substrate-aware ordering for record-kind canonicals: NOT YET — see §8 honest-limit #4.
- MCP stdio transport partially smoke-tested via `uv run tools/retrieval_server.py --help` PEP 723 dep resolution; full tool-surface verification deferred to next session-open per Claude Code restart constraint.

## §7 Next-session items and forward observations

**Session 060 recommendation**: depends on operator agenda. Most likely paths:

- **Path A (Watch) for WX-58-1 phase-2 gate evaluation** if phase-2 conditions pre-evaluation fires per records-contract.md v1 §6 (need S060 close 5-field recording to complete the 3-session window). The strict-vs-loose interpretation question for `migrated_id_resolution` per §8 honest-limit #4 must be resolved at S060 evaluation.
- **Path L for resolve_id ordering minor fix** if S060 evaluates the strict reading as substrate-bug-driven (not spec-readiness-driven) and adopts a minor implementation fix to retrieval_server.py to prefer `records/<family>/` over `specifications/` for record-kind canonical resolution. Eleventh source-realignment-or-extension precedent chain candidate.
- **Path AS-MAD-execution phase-2** (records-substrate mirrored-minority migration) if phase-2 gate fires under loose interpretation OR resolve_id minor fix is adopted at S060.
- **Path AS Shape-1 (phase-1 synthesis)** for EF-058-tier-2-validation OR EF-058-claude-md-drift substantive-arc kickoff. Joint design-space.md possible per cross-linkage.
- **Path PD/OS** if operator surfaces alternative agenda.

**Inbox check at open**: `engine-feedback/inbox/` status at S059 close: **0 new / 3 triaged / 8 resolved / 0 rejected**. EF-047-brief-slot-template + EF-058-claude-md-drift + EF-058-tier-2-validation remain triaged-deferred.

**`forward_references('S060')` organic-use opportunity** at S060 session-open per `prompts/development.md` §How to operate paragraph. Substrate post-uv-migration is structurally first-class; whether MCP tool surface appears in agent context is the at-S060-open verification.

**Next-session smoke-test close-criterion** per EF-058-uv-migration intake §Suggested Change step 6: at S060 open, verify `mcp__selvedge-retrieval__search`, `mcp__selvedge-retrieval__resolve_id`, `mcp__selvedge-retrieval__forward_references` appear in agent's tool surface; call `resolve_id("S058")` and confirm it returns a record (any path; loose interpretation) via tool call (not via Bash). Record close-criterion in S060 close WX-58-1 5-field section.

**External-application arc progression**: `selvedge-disaster-response` arc S002–S005 pending operator transport.

**Post-arc self-dev review obligation** (carrying from S047 D-150): three remaining deferred candidates (i)/(ii)/(iii) preserved.

**S060 close should evaluate**:
- Engine-v10 preservation OR engine-v11 adoption (per phase-2 progression OR substantive-arc kickoff).
- WX-58-1 third observation (S060 close 5-field recording closes 3-session window; phase-2 gate fires if criteria met).
- §10.4-M12 / M13 / M14 / M15 minorities second observation data points (phase-1 soak observation continues).
- D-129 fifteenth-consecutive exercise; D-138 fifteenth-consecutive folder.
- WX-28-1 thirtieth close-rotation (S054 rotates OUT; S060 enters).
- WX-24-1 MAD v4 thirty-third-session no-growth (if no MAD edit).
- §5.6 window-ii observation if MAD convenes (sixth-consecutive worst-case-side data point would advance).
- **Strict-vs-loose `migrated_id_resolution` interpretation per §8 honest-limit #4** — three candidate paths: (i) minor implementation fix to retrieval_server.py ordering; (ii) records-contract.md v1 §2.1 clarification; (iii) phase-2 gate criterion #2 amendment.

## §8 Honest limits at close

1. **Path T+L bundled scope proceeded per intake-disposition + S058 honest-limit #2 alignment.** Operator did not surface override at S059 open; default-proceed honoured. Operator confirmed scope mid-session ("Proceed, that scope matches.") explicitly.

2. **MCP stdio transport smoke-test partial in-session.** `uv run tools/retrieval_server.py --help` verified PEP 723 dep resolution and FastMCP import success; full tool-surface verification (`mcp__selvedge-retrieval__*` tools appear in agent context; `resolve_id` callable via tool not Bash) requires Claude Code restart and is deferred to next session-open per Claude Code restart constraint. **Reclassification path** per EF-058-uv-migration intake §Suggested Change closing paragraph: "If the smoke-test surfaces a non-trivial defect (FastMCP version pinning issue; stdio handshake mismatch; uv run PATH issue under Claude Code's spawn environment), reclassify as substantive substrate fix and open new EF record. The current scope assumes config-shape problem with config-shape fix."

3. **Records-substrate bootstrap implementation is normative-spec-aligned, not deeply user-tested.** records-contract.md v1 §5 specifies the obligations; the implementation in `tools/bootstrap-external-workspace.sh` follows the spec but has not been exercised against a fresh-bootstrap target until next external-workspace bootstrap. Honest-limit: external-workspace bootstrap with records-substrate is post-S059 first-exercise candidate.

4. **resolve_id ordering preference for migrated record-kind canonicals — finding from S059 self-validation.** records-contract.md v1 §2.1 declares records/<family>/<id>.md as authoritative for migrated record-kind identifiers; per retrieval-contract.md v1 §2.2 resolve_id returns "the markdown file path where its canonical definition lives" which for migrated record-kind canonicals SHOULD be records/<family>/<id>.md. The current substrate implementation in tools/retrieval_server.py orders results by `CASE WHEN source_path LIKE 'specifications/%' THEN 0 ELSE 1 END, source_path, line LIMIT 1` — preferring specifications/ for canonical resolution. For migrated S<NNN> identifiers (S001-S058 + S059), this returns specifications/* paths first (e.g., resolve_id("S001") returns specifications/engine-manifest.md; resolve_id("S058") does NOT return records/sessions/S058.md preferentially). Strict reading of WX-58-1 5-field migrated_id_resolution = 0/58 at S059 close (no S<NNN> resolves to records/sessions/S<NNN>.md preferentially); loose reading = 58/58 (all S<NNN> are found by resolve_id, just at non-canonical paths). S058 first observation reported 58/58 under loose interpretation; this S059 close documents the strict-vs-loose distinction explicitly. **Carrying forward to S060 phase-2 gate evaluation per records-contract.md v1 §6**: three candidate paths require operator audit / cross-checked review (not S059 self-resolution per Tier-2-self-validation discipline gap concern flagged in EF-058-tier-2-validation): (i) minor implementation fix to prefer records/<family>/ over specifications/ for record-kind id resolution (eleventh source-realignment-or-extension); (ii) records-contract.md v1 §2.1 clarification distinguishing 'authoritative for content' from 'preferred-source for substrate resolution'; (iii) phase-2 gate criterion #2 amendment to use loose interpretation. **Recommend operator audit at S060 to break tie.**

5. **engine-manifest.md crosses 6K soft warning at S059 close (NEW).** First-of-record engine-manifest soft warning. Cause: §7 engine-v10 entry added at S058 grew the file from 5,184 to 6,020 words. Forward observation: engine-manifest may need accretive-block restructure at engine-v11+ if engine-v entries continue to expand. The §10.4-M10 Substrate-N2 minority's activation warrant tracks this kind of accretive-block pressure; not yet at activation threshold.

6. **Tier-2-self-validation discipline gap acknowledged.** Per EF-058-tier-2-validation: this S059 session itself exercises the same Tier-2-by-the-doing-agent discipline that the deferred substantive-arc will deliberate on. The honest-limit #4 finding is an example of self-validation surfacing a substrate-implementation discrepancy that the same agent is not the right party to resolve. Per EF-058-tier-2-validation §Application-Scope Disposition: "the recursive concern (who Tier-2-validates the MAD that decides Tier-2-validation) is a feature not a bug." S059 proceeds with default discipline; voluntary application of an unspecified mechanism would be premature-formalisation. The §8.4 finding's resolution is explicitly recommended for operator audit at S060.

7. **Read-discipline coverage at session open**: per `read-contract.md` v6 §1 enumeration: MODE.md ✓; engine-manifest ✓; read-contract ✓; workspace-structure (referenced via S058 close) ✓; retrieval-contract ✓ (re-read for D-210 amendment); records-contract ✓; methodology-kernel (referenced via S058 close); multi-agent-deliberation (referenced via S058 close); validation-approach (referenced via S058 close); identity (referenced via S058 close); reference-validation (referenced via S058 close); PROMPT.md ✓; prompts/development.md ✓; prompts/application.md (referenced via prior sessions); records/sessions/index.md ✓; open-issues/index.md ✓; engine-feedback/INDEX.md ✓; S058 close in detail ✓; 3 EF-058 inbox records in detail ✓; tools/retrieval_server.py ✓; tools/build_retrieval_index.py (top portion) ✓; tools/bootstrap-external-workspace.sh ✓; .mcp.json ✓; specifications/aliases.yaml ✓; one prior triage record (EF-055) for format reference ✓. **Honest-limit deferred**: S053-S057 closes not freshly re-read in detail at S059 open beyond their content as referenced via S058 close §3+§7+§8 narratives. methodology-kernel.md / multi-agent-deliberation.md / validation-approach.md / identity.md / reference-validation.md / prompts/application.md not freshly re-read in detail at S059 open per content-stability across engine-v10 boundary (no substantive changes since engine-v9 boundary at S050 close). Recorded transparently per WX-22-1.

8. **Aggregate forecast accuracy at S059.** Forecast was 78,000-79,500 / 22 files; actual is 79,153 / 22 files. Forecast within 0.5% of actual — within range. Pattern observation: tighter scope produces more accurate forecasts.

9. **TaskCreate/TaskUpdate harness tools used** for session-tracking discipline. WX-43-1 baseline counts Case-Steward-orchestrator perspective-launch invocations (MAD shape); session-task-tracking is not a perspective-launch and does not advance the cumulative WX-43-1 count.

10. **`records/sessions/index.md` word count at S059 close**: ~1,500 words (added one row of ~25-40 words to S058's ~1,458). Well under 6K soft. Projected to remain under 6K for ~150+ additional sessions before any pressure.

11. **bootstrap-external-workspace.sh records-substrate scaffolding skip-list change.** The file SKIPS list now reads "records/" rather than "SESSION-LOG.md" because the new bootstrap creates a fresh records/sessions/index.md (rather than copying the self-dev workspace's records/ which contains 59 session-specific records that would not apply to an external workspace). Documentation updated to reflect this.

12. **Substrate-availability for substrate-aware S<NNN> resolution.** Per honest-limit #4: substrate is available at engine-v10 baseline for `search` and `resolve_id` but does NOT preferentially return records/sessions/ paths for migrated S<NNN> canonicals. Substrate-availability for the records-contract.md v1 §2.1 normatively-asserted resolution semantics is: NOT YET. Resolution at S060 per §7 forward observations.

## §9 Aggregate default-read surface impact at close

**Pre-close aggregate** (at S059 open per validator): ~78,476 words across 22 files (S058 close measurement).

**Actual post-close**: **79,329 words across 22 files** (validator-measured at S059 close, post-close-rotation S054-S059).

Net delta from S058 close to S059 close:
- `engine-feedback/INDEX.md` grew (3 new triage rows + status summary update): ~+200 words.
- `specifications/retrieval-contract.md` grew (D-210 minor amendment): ~+150 words.
- `records/sessions/index.md` grew (S059 row appended): ~+30 words.
- Close-rotation: S053 close (4,422 words) rotates OUT at S059 close commit; S059 close (~3,949 words derived from validator-measured aggregate delta) enters.
- Net: -473 (S059 close - S053 close) + 380 (other edits) = -93… measurement reports +853 (78,476 → 79,329); minor measurement-arithmetic discrepancy attributable to additional minor word-counts from .md changes not enumerated above (e.g., S059.md record itself ~200 words is counted in records/sessions/ outside the default-read).

Headroom to 90K soft ceiling: **10,671 words** (comfortable; no accretion concern at S059).

`records/sessions/index.md` growth pattern: ~25-40 words per session row; projected to remain under 6K for 150+ additional sessions before any soft-warning concern. Engine-manifest.md NEW soft warning (6,020 / 6K) is the first accretive-block warning candidate at engine-v10+ — see §8 honest-limit #5.

## §10 S059 meta-observations

1. **Tenth source-realignment-or-extension precedent chain extension** (D-207 + D-210 + D-211). Pattern is now firmly engine-conventional for inbox-record-driven defect-fixes. Operator-recommended at intake → triage classifies minor → single-orchestrator implements → minor template-shape spec amendments where needed → engine-v preserved. Pattern validated at n=10 across heterogeneous defect classes.

2. **First-of-record post-session-intake-triple event triage in single session** (EF-058×3 at S059). The post-session-intake mechanism (operator surfaces feedback after session close) reified at first-event with the EF-054 single record at S053-post-session; second-event at S055-post-session with EF-055; **third-event at S058-post-session with EF-058×3 multi-record sequence**. The three records sequenced as (a) operational defect-fix → (b) methodological observation → (c) meta-pattern observation; demonstrates the discussion-pattern in which a single operator gap surfaces multiple layers as the discussion deepens. Triage-in-single-session reified at n=2 (S054 EF-053+EF-054 first-instance; S059 EF-058×3 second-instance).

3. **Tier-2-self-validation discipline gap surfaced concretely at S059 close** via the §8 honest-limit #4 finding (resolve_id ordering preference). This is exactly the kind of finding the EF-058-tier-2-validation substantive-arc is concerned with: same agent doing the work + assessing the work; finding surfaces a substrate-implementation discrepancy that the same agent is not the right party to resolve. The methodology's discipline at present is to surface honestly + defer to operator/next-MAD; this is engine-conventional but is itself the pattern under EF-058-tier-2-validation review.

4. **Bundling-by-coincidence pattern reified at n=2** (S054 D-185+D-186+D-187 first-instance bundled retrieval_server.py edits + prompts/development.md edit; S059 D-207+D-211 second-instance bundled tools/bootstrap-external-workspace.sh edits). The pattern is engine-conventional when scope-coincidence on a single file makes splitting artificial.

5. **Engine-manifest.md crosses 6K soft warning** for first time at S059 close (NEW). This is engine-v10's first soft-warning event. Engine-manifest growth is dominated by §7 engine-v entries (~700 words per engine-v); engine-v11 would add another ~700 pushing well past 7K toward 8K hard. Forward observation: engine-manifest may need accretive-block restructure at engine-v11+ adoption (similar to SESSION-LOG.md → records/sessions/ migration at S058); §10.4-M10 Substrate-N2 minority watches this class.

6. **WX-58-1 second observation at S059 close completes 2-of-3 of the records-discipline-soak observation window.** S060 close adds the third observation; phase-2 gate fires per records-contract.md v1 §6 conditions if all three closes' 5-field readings pass. The strict-vs-loose interpretation question per §8 honest-limit #4 affects whether S058 first observation's "58/58" is reaffirmed or recalibrated at S060 phase-2 evaluation.

7. **Path T+L bundled-with-substrate-bootstrap pattern** is the first-of-record instance where a Path T+L resolution bundles an unrelated S058-honest-limit-deferred-implementation into the same session. The bundling worked because both edits touched the same file (`tools/bootstrap-external-workspace.sh`); the pattern is conditional on file-coincidence rather than scope-coincidence.

8. **Thirty-first-consecutive housekeeping `[none]`-trigger pattern.** D-212 extends pattern since D-126 Session 041. Engine-conventional (S050+S057+S058 substantive housekeeping are the four-of-31 exceptions in the run; pattern remains dominant).

9. **Operator engagement pattern at S059**: thin operator input (`/clear` followed by `PROMPT.md`); mid-session operator confirmation of scope ("Proceed, that scope matches."); no other operator surfacing during execution. Pattern continues from S058 in light-engagement mode appropriate to single-orchestrator default-agent path. Operator's preference for thin-engagement when scope is clear is durable input that informs path-selection at session-open.

10. **CLAUDE.md §Tools standing operator instruction validated as load-bearing at S059** via D-207 alignment. The pre-S059 8-session honest-limit chain demonstrated the cost of pretraining-default overriding operator standing instructions; the S059 alignment with `uv` per CLAUDE.md §Tools is an example of the methodology accepting and integrating operator standing input. The methodological-pattern resolution (whether MAD shared-brief should read CLAUDE.md) remains deferred at EF-058-claude-md-drift substantive-arc.

## §11 Commit and close

This close file is committed with the S059 artefacts:
- `provenance/059-session/00-assessment.md` (pre-work commit `2145ff3` already done).
- `provenance/059-session/02-decisions.md` (this close commit).
- `provenance/059-session/03-close.md` (this file; this close commit).
- `engine-feedback/triage/EF-058-substrate-runtime-uv-migration-recommended-path.md` (this close commit).
- `engine-feedback/triage/EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` (this close commit).
- `engine-feedback/triage/EF-058-tier-2-validation-discipline-by-distinct-agent.md` (this close commit).
- `engine-feedback/INDEX.md` (status + 3 rows + note paragraph; this close commit).
- `specifications/retrieval-contract.md` (D-210 minor amendment; this close commit).
- `tools/retrieval_server.py` (D-207 PEP 723; this close commit).
- `tools/build_retrieval_index.py` (D-207 PEP 723; this close commit).
- `.mcp.json` (D-207 uv command; this close commit).
- `tools/bootstrap-external-workspace.sh` (D-207+D-211 uv-migration + records-substrate bootstrap; this close commit).
- `records/sessions/S059.md` (records-contract.md v1 §2.1 record; this close commit).
- `records/sessions/index.md` (S059 row appended; this close commit).

`.cache/venv/` deleted from workspace per D-207 step 5 (gitignored; not committed).

Engine-v10 preserved per D-200 lineage (preservation depth 2 at S059 close). 40 first-class minorities preserved engine-wide (unchanged). 13 active OIs unchanged. Engine-feedback state 0 new / 3 triaged / 8 resolved / 0 rejected (EF-058-uv-migration resolved within session via 6-step Path L; EF-058-claude-md-drift triaged-deferred substantive-arc; EF-058-tier-2-validation triaged-deferred substantive-arc per operator MAD preference). 7 decisions: D-206 + D-207 + D-208 + D-209 + D-210 + D-211 + D-212. Tenth source-realignment-or-extension precedent chain instance. WX-58-1 second observation 5-field recording per records-contract.md v1 §6. WX-28-1 twenty-ninth close-rotation S053 OUT S059 IN zero retention-exceptions. WX-24-1 MAD v4 thirty-second-session no-growth streak new record (17-session run from S042 reset). engine-manifest.md crosses 6K soft warning for first time at engine-v10 (NEW; first-of-record). Thirty-first-consecutive housekeeping `[none]`-trigger pattern. resolve_id ordering preference for migrated record-kind canonicals surfaced as honest-limit #4 (recommended for operator audit at S060 phase-2 gate evaluation). MCP stdio transport full smoke-test deferred to next session-open per Claude Code restart constraint; partial smoke-test (uv run PEP 723 dep resolution + FastMCP import + index rebuild) verified in-session.
