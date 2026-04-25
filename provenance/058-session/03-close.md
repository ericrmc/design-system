---
session: 058
title: Close — Path AS-MAD-execution per S057 D-196 pre-ratification; 4-perspective two-family MAD on EF-055 substantive-arc; Substrate-N3.5 pilot toward Direction A adopted; new engine-definition spec records-contract.md v1; SESSION-LOG.md migrated to records/sessions/ as proving slice; engine-v9→v10 second-instance MAD-adopted-new-engine-definition-spec class; D-198 through D-205 (eight decisions); four new first-class minorities §10.4-M12 through §10.4-M15 (count 36→40); §10.4-M10 written-warrant amendment (clause c operator-surfacing channel formalised); WX-58-1 records-discipline-soak observation window opens
date: 2026-04-25
status: complete
---

# Close — Session 058

## §1 Artefacts produced

### §1a Provenance (`provenance/058-session/`)

- `00-assessment.md` (~3,200 words; commit `c0fc8e0`) — pre-work commit per D-017 spirit + S048-S057 precedent chain. Reflects Path AS-MAD-execution per S057 D-196 pre-ratification + recommended composition for first-step ratification.
- `01-brief-shared.md` (~2,700 words; commit `7226ea3`) — shared brief §1 methodology-context + §2 problem-statement + §3 design questions Q1-Q8 + 8 open questions + §5 response-format + §6 anti-import-constraint byte-identical across briefs.
- `01-brief-p1.md` (~280 words; commit `7226ea3`) — P1 Substrate-Methodology Architect role-specific stance.
- `01-brief-p2.md` (~340 words; commit `7226ea3`) — P2 Incrementalist Conservator role-specific stance.
- `01-brief-p3.md` (~350 words; commit `7226ea3`) — P3 Outsider Frame-Completion role-specific stance.
- `01-brief-p4.md` (~370 words; commit `7226ea3`) — P4 Cross-Family Reviewer Laundering-Audit role-specific stance.
- `01a-perspective-substrate-methodology-architect.md` (~3,000 words; commit `a2c9805`) — P1 raw output verbatim from Claude Opus 4.7 subagent (general-purpose Agent tool).
- `01b-perspective-incrementalist-conservator.md` (~3,500 words; commit `a2c9805`) — P2 raw output verbatim from Claude Opus 4.7 subagent.
- `01c-perspective-outsider-frame-completion.md` (~2,470 words; commit `a2c9805`) — P3 raw output verbatim from codex exec / GPT-5.5 reasoning-effort xhigh.
- `01d-perspective-cross-family-reviewer.md` (~2,200 words; this close commit) — P4 raw output verbatim from codex exec / GPT-5.5 reasoning-effort xhigh; second-invocation post-canonical-perspective-files-wrapping per first-of-record P4-blocked-on-precondition refusal.
- `01-deliberation.md` (~5,000 words; this close commit) — synthesis per `multi-agent-deliberation.md` v4 §Synthesis with citation discipline + `[synth]` markers + quote-over-paraphrase for load-bearing claims + convergence-vs-coverage distinction + alphabetical perspective ordering + dissent-preservation.
- `02-decisions.md` (~5,200 words; this close commit) — **eight decisions**: D-198 Path AS-MAD-execution + perspective composition ratified `[d016_2, d016_3, d016_4]` + D-199 Substrate-N3.5 pilot toward Direction A adopted `[d016_2, d016_3, d016_4]` + D-200 engine-v9→v10 bump `[d016_2]` + D-201 records-contract.md v1 created `[d016_2, d016_4]` + D-202 workspace-structure.md v6→v7 + read-contract.md v5→v6 substantive revisions `[d016_2]` + D-203 SESSION-LOG.md migration `[d016_2]` + D-204 §10.4-M10 warrant amendment + four new minorities preserved `[d016_2]` + D-205 housekeeping `[none]` (15 sub-sections).
- `03-close.md` — this file.
- `manifests/<role>.manifest.yaml` — four per-participant manifests (P1 substrate-methodology-architect / P2 incrementalist-conservator / P3 outsider-frame-completion / P4 cross-family-reviewer) per `multi-agent-deliberation.md` v4 §Heterogeneous-Participant Recording Schema.
- `participants.yaml` — session-level participants index per Layer 3.
- `archive/pre-records-SESSION-LOG/` — archive-pack of pre-engine-v10 SESSION-LOG.md per D-203; manifest.yaml + 00-source.md (byte-identical witness 7,390 words / 62,539 bytes; sha256 17302df920...).
- `codex-p3-final.log` + `codex-p3-raw-output.log` — codex P3 final message and full transcript.
- `codex-p4-final.log` + `codex-p4-raw-output.log` — codex P4 final message (second invocation) and full transcript.

### §1b Specification changes THIS session

**One new engine-definition spec** + **two substantive engine-definition spec revisions** + **one minor engine-manifest update** + **two engine-adjacent tool updates**.

NEW:
- `specifications/records-contract.md` v1 — declares structured-record-as-source-of-truth discipline + fact-family directory pattern + bootstrap obligations per D-201. ~3,000 words.

REVISED (substantive):
- `specifications/workspace-structure.md` v6 → v7 — file-class extension (`structured-source-record` + `markdown-witness`) + `records/` directory in top-level structure + §records-substrate section + SESSION-LOG.md migrated section + §10.4-M10 written-warrant amendment + §10.4-M12 through §10.4-M15 four new minorities preserved per D-202a + D-204. v6 preserved as `workspace-structure-v6.md` with `status: superseded`. Words ~3,918 → ~5,400.
- `specifications/read-contract.md` v5 → v6 — §1 item 5 SESSION-LOG.md → records/sessions/index.md + Records-directory clarification per D-202b. v5 preserved as `read-contract-v5.md` with `status: superseded`. Words ~5,624 → ~6,000.

REVISED (documentary per §5 sub-pattern):
- `specifications/engine-manifest.md` — §2 engine-v9 → engine-v10 + §3 add records-contract.md + §7 engine-v10 entry per D-200. Words ~5,184 → ~5,800.

ENGINE-ADJACENT (NOT in §3 enumeration):
- `tools/validate.sh` — check 25 added (records-substrate integrity per `records-contract.md` v1 §3); `RECORDS_CONTRACT_ADOPTION_SESSION=58` constant; `SESSION_RECORD_STATUS_ENUM` constant; check 1 + check 6 updated to accept records/sessions/index.md OR SESSION-LOG.md (engine-v10+ vs pre-engine-v10); default-read enumeration item (3) updated.
- `tools/build_retrieval_index.py` — `classify_kind()` extended to recognise `records/<family>/` paths (returns `record-<family>` kind); `extract_session()` extended with RECORDS_SESSION_PATH_RE for records/sessions/S<NNN>.md.

WORKSPACE STRUCTURE:
- `records/sessions/` directory created at workspace root with 58 records (S001–S058) + thin `index.md`.
- `SESSION-LOG.md` REMOVED from workspace root (migrated to records/sessions/; preserved as archive-pack at `provenance/058-session/archive/pre-records-SESSION-LOG/`).
- `engine-feedback/INDEX.md` updated: status summary 0 new / 2 triaged / 6 resolved / 0 rejected → 0 new / 1 triaged / 7 resolved / 0 rejected; EF-055 row Status updated to **resolved (S058 D-199 through D-205)** with disposition narrative.
- `engine-feedback/triage/EF-055-...md` updated `resolved_by:` to `provenance/058-session/`.

### §1c Development-provenance files amended (WX-35-1 claim discipline)

Per WX-35-1 standing discipline, each claimed file amendment is verified via `git log --oneline <path>` at close.

- `provenance/058-session/00-assessment.md` — CREATED (commit `c0fc8e0`).
- `provenance/058-session/01-brief-shared.md` — CREATED (commit `7226ea3`).
- `provenance/058-session/01-brief-p1.md` — CREATED (commit `7226ea3`).
- `provenance/058-session/01-brief-p2.md` — CREATED (commit `7226ea3`).
- `provenance/058-session/01-brief-p3.md` — CREATED (commit `7226ea3`).
- `provenance/058-session/01-brief-p4.md` — CREATED (commit `7226ea3`).
- `provenance/058-session/01a-perspective-substrate-methodology-architect.md` — CREATED (commit `a2c9805`).
- `provenance/058-session/01b-perspective-incrementalist-conservator.md` — CREATED (commit `a2c9805`).
- `provenance/058-session/01c-perspective-outsider-frame-completion.md` — CREATED (commit `a2c9805`).
- `provenance/058-session/01d-perspective-cross-family-reviewer.md` — CREATED this close commit.
- `provenance/058-session/01-deliberation.md` — CREATED this close commit.
- `provenance/058-session/02-decisions.md` — CREATED this close commit.
- `provenance/058-session/03-close.md` — CREATED this close commit (this file).
- `provenance/058-session/manifests/*.manifest.yaml` — 4 files CREATED this close commit.
- `provenance/058-session/participants.yaml` — CREATED this close commit.
- `provenance/058-session/archive/pre-records-SESSION-LOG/manifest.yaml` + `00-source.md` — CREATED this close commit.
- `provenance/058-session/codex-p3-final.log` + `codex-p3-raw-output.log` — committed (renamed from .md to .log per S050 convention).
- `provenance/058-session/codex-p4-final.log` + `codex-p4-raw-output.log` — committed (final from second invocation).
- `specifications/records-contract.md` — CREATED this close commit.
- `specifications/workspace-structure.md` (v7) + `specifications/workspace-structure-v6.md` (status: superseded) — EDITED + CREATED this close commit.
- `specifications/read-contract.md` (v6) + `specifications/read-contract-v5.md` (status: superseded) — EDITED + CREATED this close commit.
- `specifications/engine-manifest.md` — EDITED this close commit (engine-v10 entry + §3 + §2).
- `tools/validate.sh` — EDITED this close commit (check 25 + constants + check 1/6 updates).
- `tools/build_retrieval_index.py` — EDITED this close commit (classify_kind + extract_session for records).
- `records/sessions/index.md` + `records/sessions/S001.md` through `records/sessions/S058.md` — 59 files CREATED this close commit.
- `SESSION-LOG.md` — DELETED from workspace root (migrated; archive-pack preserved per D-203).
- `engine-feedback/INDEX.md` — EDITED (EF-055 row + status summary).
- `engine-feedback/triage/EF-055-...md` — EDITED (resolved_by: pointer).

NOT EDITED:
- `PROMPT.md`, `MODE.md`, `prompts/development.md`, `prompts/application.md`, `CLAUDE.md` — unchanged.
- `methodology-kernel.md` v6, `multi-agent-deliberation.md` v4, `validation-approach.md` v5, `identity.md` v2, `reference-validation.md` v3, `retrieval-contract.md` v1 — all unchanged at engine-v10 boundary.
- `specifications/aliases.yaml` — unchanged at engine-v10.
- `tools/bootstrap-external-workspace.sh` — NOT edited this session (records-contract.md v1 §5 specifies the extension; actual implementation deferred to a future minor session given scope limits at S058; honest-limit recorded below).
- `open-issues/*.md` + `open-issues/index.md` — NOT edited (no OI opened/resolved/amended; 13 active OIs unchanged).
- `engine-feedback/inbox/EF-055-...md` — NOT edited per intake-files-preserved-verbatim convention.
- `.mcp.json`, `.gitignore` — NOT edited.
- `.cache/retrieval.db` — REBUILT post-spec-edits (gitignored; not committed); 549 documents / 58,198 identifiers (up from S057's 473 docs / 54,987 identifiers; +76 docs and +3,211 identifiers from records/sessions/ + briefs + perspectives + spec revisions + new spec).

### §1d Validator status at close

Validator at close: **1349 PASS / 0 FAIL / 26 WARN** (3 spec soft-warnings + 23 design-intent "no rejected alternatives" warnings).

- Aggregate default-read surface: **78,476 words across 22 files** (validator-measured at close). SESSION-LOG.md (7,390) removed; records/sessions/index.md (~1,458) added; spec revisions added ~5,600 words; net change small. Headroom to 90K soft: 11,524 words.
- Per-file: `multi-agent-deliberation.md` v4 6,637 words (soft warning); `reference-validation.md` v3 7,177 words (soft warning); `read-contract.md` v6 ~6,000 words (at soft warning boundary; possibly under).
- Check 20 per-file: 3 soft warnings preserved (MAD + RV + read-contract approaching).
- Check 20 aggregate: PASS (78,476 / 90K soft).
- Check 21 archive-pack manifest integrity: PASS (new archive-pack at provenance/058-session/archive/pre-records-SESSION-LOG/ verified hash match).
- Check 22 archive-pack citation consistency: PASS (new archive-pack reference cited from workspace-structure.md v7 + read-contract.md v6 + engine-manifest.md v10 entry).
- Check 23 MODE.md presence: PASS.
- **Check 25 records-substrate integrity**: PASS (58 session records; index rows match; status enum clean; no orphans).

WX-34-1 SESSION-LOG.md ceiling pressure: **PERMANENTLY RETIRED** at S058 by migration to records/sessions/. The file no longer exists; ceiling-pressure observation discharged-by-migration.

### §1e Engine-version status THIS session

**Engine-v9 → engine-v10 content-driven bump** at S058 close per D-200. Engine-v9 preservation window closes at **8 sessions** (S050→S057; engine-v10 ratified at S058) — **second-longest-running engine-v in workspace history** after engine-v7 11-session record (S036→S048).

Engine-v10 establishes the **second-instance MAD-adopted-new-engine-definition-spec class** (after engine-v8→v9 at S050 D-172). Bump-provenance class reified at n=2.

§5.4 cadence minority does NOT re-escalate per S028 D-096 / S033 D-107 / S036 D-114 / S048 D-154 / S050 D-172 content-driven-bump precedent chain extended to S058.

## §2 Operational warrants changed or advanced

1. **Substrate-N3.5 pilot toward Direction A adopted as substantive-arc resolution of EF-055.** 3-of-4 cross-family weighted convergence (P1 + P3 + P4 own-recommendation; P2 isolated on Direction C). P3 originated Substrate-N3.5 reframe not in design-space.md §4 inventory; P4 endorsed with narrower phase-1; synthesis adopted with phase-1 = SESSION-LOG.md only as proving slice. **First-of-record cross-family-originated-and-adopted reframe-architecture event** (Substrate-N3.5 was not in the pre-MAD design-space §4 inventory; P3 surfaced it; synthesis adopted it).

2. **Engine-v9 closes preservation depth 8 — first-of-record exceeds-engine-v4-and-v5 marks; second-place all-time after engine-v7's 11-session record.** Second-longest-running engine-v in workspace history.

3. **Engine-v10 ratified — second-instance MAD-adopted-new-engine-definition-spec class.** New engine-definition spec `records-contract.md` v1 + 2 substantive engine-definition spec revisions (workspace-structure.md v6→v7 + read-contract.md v5→v6) + 1 documentary engine-manifest.md update + 2 engine-adjacent tool updates.

4. **EF-055 inbox→triaged→resolved within session lifecycle** (post-S056 D-191/D-192 triaged → S058 D-199 through D-205 resolved). Engine-feedback state 0 new / 2 triaged / 6 resolved → 0 new / 1 triaged / 7 resolved.

5. **§10.4-M10 written-warrant amendment formalised**: new clause (c) operator-surfacing channel added alongside existing (a) maintenance-cost-2× + (b) multi-hop-dominance-5×. **First-of-record minority-warrant-amendment via operator-surfacing-channel-formalisation event.**

6. **Four new first-class minorities preserved** (§10.4-M12 P2 warrant-gated deferral / §10.4-M13 P3+P4 shallow-Direction-A warning / §10.4-M14 P1 broader-phase-1 / §10.4-M15 P2 spec-local distributed minority directories). Engine-wide minority count 36 → 40.

7. **First-of-record P4-blocked-on-precondition refusal event.** P4 first invocation correctly refused the audit because canonical perspective files (01a/01b/01c) had not yet been wrapped — codex raw log only contained the prompt. P4's refusal was methodology-correct: laundering-audit role's anti-laundering-by-process discipline. Re-launched with explicit canonical paths after Case Steward wrapping; second invocation produced clean audit. **Future MAD sessions running cross-family laundering-audit role should ensure canonical perspective files are wrapped before launching P4.**

8. **WX-58-1 records-discipline-soak observation window opens.** S058 close + S059 open + S060 open phase-2 gate per `records-contract.md` v1 §6.

9. **WX-34-1 SESSION-LOG.md ceiling-pressure permanently retired.** File migrated to records/sessions/; bounded by record count not session-content; structural-friction discharged-by-migration. Three-consecutive-soft-warning pattern (S055/S056/S057) terminates at S058 by migration.

10. **D-129 standing discipline thirteenth-consecutive clean exercise** (00-assessment §4a + D-198 inline; five non-Path-AS-MAD-execution alternatives).

11. **D-138 folder-name default thirteenth-consecutive clean exercise** (`provenance/058-session/`).

12. **WX-28-1 twenty-eighth close-rotation zero retention-exceptions.** S052 rotates OUT; S058 enters. Retention window post-rotation: S053 / S054 / S055 / S056 / S057 / S058.

13. **WX-24-1 MAD v4 thirty-first-session no-growth streak new record** (16-session run from S042 reset; extends S057's 15-session record).

14. **WX-43-1 explicit-instruction variant cumulative n=0-of-13** self-commit breaches across S047 (3) + S049 (3) + S050 (4) + S058 (3 P1+P2+self-Case-Steward; P3+P4 sandboxed not applicable).

15. **§5.6 GPT-family-concentration window-ii observation continues** (fifth-consecutive worst-case-side substantive-deliberation data point S044+S045+S047+S050+S058). Cross-family contribution at S058 was substantive and load-bearing; supports continued-preservation.

## §3 Engine-v disposition and preservation depth

**Engine-v9 → engine-v10 ratified at S058 close.**

Engine-v preservation depths for record:
- engine-v2 (S021 adopted; S022 bump 1-session)
- engine-v3 (S022 adopted; S023 bump 1-session)
- engine-v4 (S023 adopted; S028 bump 5-session)
- engine-v5 (S028 adopted; S033 bump 5-session)
- engine-v6 (S033 adopted; S036 bump 3-session)
- engine-v7 (S036 adopted; S048 bump **11-session** — longest)
- engine-v8 (S048 adopted; S050 bump 2-session)
- engine-v9 (S050 adopted; S058 bump **8-session** — second-longest after engine-v7)
- **engine-v10 (S058 adopted; current preservation window count 1)**.

Candidate triggering events for engine-v11:
- **WX-58-1 phase-2 fires at S059** — mirrored-minority migration (workspace-structure §10.4 ↔ retrieval-contract §7 to canonical records/minorities/) per `records-contract.md` v1 §6 phase-2 gate.
- Phase-3 (engine-version history + reference-validation §10 + feedback metadata) at S060+.
- EF-047-brief-slot-template resolution at arc-exercise session (pending operator transport).
- Operator-surfaced agenda for any engine-definition substantive revision.

## §4 Preserved first-class minorities at S058 close

**40 first-class minorities preserved engine-wide at S058 close** (36 at open + 4 new from S058 MAD).

Full enumeration per `specifications/workspace-structure.md` v7 §10.4 (M1–M15) + §5.1/§5.4/§5.5/§5.6/§5.7/§5.8/§5.9/§5.10/§5.11/§5.12/§5.13/§5.14 + Session 024 A.4 four minorities + Session 027 §A/§B/§C + existing preserved-minorities in `reference-validation.md` v3 §10.1/§10.2/§10.3 + `retrieval-contract.md` v1 §7.1–§7.5 (mirrored with workspace-structure §10.4-M7–M11) + new `records-contract.md` v1 §7.1–§7.4 (mirrored with workspace-structure §10.4-M12–M15).

§10.4-M10 amended with new written warrant (c) operator-surfacing channel per D-204 Part A.

§5.6 minority preserved unchanged with continued-preservation-against-future-event-horizon disposition (S058 substantive cross-family contribution P3 + P4 supports preservation).

## §5 Watchpoints status at S058 close

- **WX-24-1** — MAD v4 stable 6,637 words. **Thirty-first-session no-growth streak** (S043–S058). New record (16-session run).
- **WX-24-3** — reference-validation label discipline n=8 stable.
- **WX-27-1** — stable.
- **WX-28-1** — **twenty-eighth close-rotation** (S052 rotates OUT; S058 enters); zero retention-exceptions.
- **WX-33-2** — reference-validation.md v3 7,177 words stable.
- **WX-34-1** — **PERMANENTLY RETIRED** at S058 by SESSION-LOG.md migration to records/sessions/. Ceiling-pressure-on-strictly-linear-per-session-file structurally retired; future records-substrate growth is bounded by record count not session-content; index file is bounded by row count.
- **WX-35-1** — standing discipline applied cleanly; explicit retractions recorded in §1c.
- **WX-43-1** — cumulative baseline n=6-of-8 + explicit-instruction variant n=0-of-13 (S047+S049+S050+S051+S052+S053+S054+S055+S056+S057+S058). OI-promotion discharged-as-not-warranted per S050 D-176.
- **WX-44-1** — codex-CLI repo-wide-search independence-phase-breach watch. Not exercised this session beyond P4's intentional file-reads of canonical perspective files (which is the role's required input, not an independence-phase breach). Cumulative n=3 unchanged.
- **WX-44-2** — codex CLI model-version-drift discipline: codex CLI invocations used GPT-5.5 reasoning-effort xhigh per `~/.codex/config.toml` defaults consistent with S047/S050 invocations; no model-version-correction events.
- **WX-47-1** — codex-CLI argv `---` YAML parsing fragility: workaround applied successfully (stdin pipe `cat /tmp/s058-brief-pN.md | codex exec`).
- **WX-50-1** — observation window closed at S053; phase-1 paused; phase-1 tools available for organic use. S058 exercised substrate substantially (build_retrieval_index.py rebuild post-spec-edits; substantive index growth from records family).
- **WX-58-1 (NEW)** — records-discipline-soak observation window opens at S058 close. First observation: check_25_status pass / migrated_id_resolution 58-of-58 / fallback_index_readable yes / record_witness_drift 0 / session_record_added_without_editing_accretive_block yes.

## §6 No retrieval-substrate WX-50-1 recording obligation; WX-58-1 first recording

Per `retrieval-contract.md` v1 §6, the WX-50-1 3-field recording obligation applies to sessions S050 through S053 inclusive. S058 is post-window; no obligation.

Per `records-contract.md` v1 §6, the WX-58-1 5-field recording obligation applies to sessions S058 through S060 inclusive. S058 first recording per §1d above + §5 WX-58-1 entry.

**Substrate use at S058**:
- 1 `tools/build_retrieval_index.py` rebuild post-spec-edits: 549 documents / 58,198 identifiers (up from S057's 473 / 54,987; +76 docs +3,211 identifiers attributable to records/sessions/ + spec revisions + new spec).
- Plus implicit invocations via FastMCP `tool_manager` introspection.
- Records-substrate is now first-class indexed: classify_kind() returns `record-sessions` for `records/sessions/*.md`; resolve_id() can return canonical `S<NNN>` records.

MCP stdio transport remains unverified per S051-S057 chain.

## §7 Next-session items and forward observations

**Session 059 recommendation**: depends on operator agenda. Most likely paths:

- **Path AS-MAD-execution phase-2** if phase-2 gate fires at S058 close: WX-58-1 conditions met enable mirrored-minority migration (workspace-structure §10.4 ↔ retrieval-contract §7 to canonical records/minorities/) at S059. Single-orchestrator if pattern is clean; MAD if novel issues surface. Engine-v10→v11 candidate or engine-v10 minor amendment per OI-002.
- **Path A (Watch)** if operator does not surface AND phase-2 conditions are not yet judged sufficient (e.g., one-session soak before phase-2 commitment).
- **Path L+A** preemptive-restructure not needed (WX-34-1 retired at S058).
- **Path PD/OS** if operator surfaces alternative agenda.

**Inbox check at open**: `engine-feedback/inbox/` status at S058 close: 0 new / 1 triaged / 7 resolved / 0 rejected. EF-047-brief-slot-template remains triaged-deferred per S050 D-174.

**`forward_references('S059')` organic-use opportunity** at S059 session-open per `prompts/development.md` §How to operate paragraph. Substrate now first-class indexes records/sessions/; pattern observation will continue.

**External-application arc progression**: `selvedge-disaster-response` arc S002–S005 pending operator transport.

**Post-arc self-dev review obligation** (carrying from S047 D-150): three remaining deferred candidates (i)/(ii)/(iii) preserved.

**S059 close should evaluate**:
- Engine-v10 preservation OR engine-v11 adoption (per phase-2 progression).
- WX-58-1 second observation (S059 close 5-field recording).
- §10.4-M12 / M13 / M14 / M15 minorities first observation data points.
- D-129 fourteenth-consecutive exercise; D-138 fourteenth-consecutive folder.
- WX-28-1 twenty-ninth close-rotation (S053 rotates OUT; S059 enters).
- WX-24-1 MAD v4 thirty-second-session no-growth (if no MAD edit) OR cycle reset (if MAD substantively edits MAD spec).
- §5.6 window-ii observation if MAD convenes (sixth-consecutive worst-case-side data point would advance).

## §8 Honest limits at close

1. **Path AS-MAD-execution proceeded per S057 D-196 pre-ratification + S058 D-198 first-step composition ratification.** Operator did not surface override; default-proceed honoured.

2. **Tools/bootstrap-external-workspace.sh extension deferred.** `records-contract.md` v1 §5 specifies the bootstrap-extension; actual implementation edits to `tools/bootstrap-external-workspace.sh` deferred to a minor follow-up session given S058 scope limits. The records-contract.md v1 §5 specification is normative; future external-workspace bootstraps are blocked on the implementation. Recorded as forward observation for S059+.

3. **MCP stdio transport remains unverified in-session.** Same chain as S051 / S052 / S053 / S054 / S055 / S056 / S057.

4. **records/sessions/index.md word count uncertainty.** Index file ~1,458 words measured; well under 6K soft. As records/sessions/ accumulates additional sessions, the index will grow ~25-40 words per session (thin pointer-only row); projected to remain under 6K for ~150+ additional sessions before any pressure.

5. **Validator check 25 phase-1 scope is structural not semantic.** Verifies index-row-record consistency on `id` + presence of required fields + status enum membership + no orphans. Does NOT verify that title or summary fields match between record and index. Future phase-2 may extend to semantic-level checks.

6. **§10.4-M13 shallow-Direction-A warning is the highest-priority watchpoint.** If migrated `records/sessions/*.md` lack structured authoritative frontmatter in practice (e.g., operators edit body content rather than frontmatter; index becomes manually authoritative), the source-of-truth discipline is at risk and the minority becomes preferred revision direction.

7. **Records-contract.md v1 §5 bootstrap obligations not yet implemented.** External-workspace bootstrap script extension is specified but not yet coded; this is engine-adjacent debt.

8. **P4 first-invocation refusal added unexpected work.** Re-launching P4 with explicit canonical paths added one cycle of process. Net positive: methodology-correct refusal preserved audit integrity. Future MAD sessions should pre-wrap canonical perspective files before launching P4 to avoid this cycle (or P4 brief should explicitly reference the codex-pN-final.log files as alternative input source).

9. **Aggregate forecast accuracy improved at S058.** Forecast was 78,000-82,000 / 22+ files; actual is 78,476 / 22 files. Forecast within 3.2% of actual — significantly improved over WX-22-1 forecast-error pattern. Pattern observation: when scope is well-bounded (specific spec edits + mechanical migration), forecast is accurate; when scope is open (free-form prose growth like SESSION-LOG.md), forecast under-estimates.

10. **Read-discipline coverage at session open**: per `read-contract.md` v6 §1 enumeration: MODE.md ✓; engine-manifest ✓; read-contract ✓; workspace-structure ✓; retrieval-contract ✓; methodology-kernel ✓; multi-agent-deliberation ✓; validation-approach ✓; identity ✓; reference-validation ✓; PROMPT.md ✓; prompts/development.md ✓; prompts/application.md ✓; SESSION-LOG.md ✓ (read at session-open in two chunks; subsequently migrated this session); open-issues/index.md ✓; engine-feedback/INDEX.md ✓; S057 close in detail ✓; S057 design-space.md in full ✓; S057 02-decisions.md in full ✓; S057 00-assessment.md in full ✓; S056 close in detail ✓; EF-055 inbox + triage records in full ✓; S050 P3 + P4 + 01-deliberation in full ✓. Honest-limit deferred: S052/S053/S054/S055 closes not freshly re-read in detail at S058 open beyond their unusually-verbose SESSION-LOG.md rows; S050 P1 + P2 raw perspectives read selectively per MAD synthesis relevance (their substance digested via 01-deliberation). Recorded transparently per WX-22-1.

11. **§10.4-M12 (P2 warrant-gated deferral) preserved with explicit re-evaluation conditions.** If §10.4-M10 telemetry remains absent by S060, OR phase-1 cost exceeds projected maintenance savings, OR check 25 is noisy/expensive, OR record-witness drift is detected within two sessions, OR phase-1 reduction <7K words: deferral position vindicated; substantive arc may roll back via archive-pack restoration.

12. **Operator-stated preference treatment**: 4-of-4 cross-family convergence on durable-input-not-foreclosure. Synthesis adopted Substrate-N3.5 pilot toward Direction A — substantial-variant of operator-stated Direction A — on technical merits via cross-family deliberation, not deference. Per P4 [`01d`, Q8]: "preference should affect interpretation, not outcome selection."

13. **§5.6 window-ii observation carries forward.** Fifth-consecutive worst-case-side substantive-deliberation data point. Per S041 D-125/D-126 §5.6 minority text strict reading, window-ii closed at S047 close; spirit-level question carries forward. Cross-family contribution at S058 was substantive (P3 + P4 surfaced + drove synthesis); supports continued-preservation reading.

## §9 Aggregate default-read surface impact at close

**Pre-close aggregate** (at S058 open per validator): ~80,161 words across 21 files.

**Actual post-close**: **78,476 words across 22 files** (validator-measured).

Net delta:
- SESSION-LOG.md (7,390 words) REMOVED from default-read enumeration.
- records/sessions/index.md (~1,458 words) ADDED.
- specifications/records-contract.md v1 (~3,000 words) ADDED.
- workspace-structure.md grew 3,918 → ~5,400 (+1,482).
- read-contract.md grew 5,624 → ~6,000 (+376).
- engine-manifest.md grew 5,184 → ~5,800 (+616).
- Close-rotation: S052 close (~3,800 words) rotates OUT; S058 close (~3,500 words estimated) enters.
- Net: -1,685 words, +1 file.

Headroom to 90K soft ceiling: **11,524 words** (comfortable; no accretion concern at S058).

**WX-34-1 retirement at S058**: SESSION-LOG.md ceiling-pressure structurally retired by migration. records/sessions/index.md grows ~25-40 words/session; projected to remain under 6K for 150+ sessions of additional growth before any soft-warning concern.

## §10 S058 meta-observations

1. **Substrate-N3.5 reframe was a genuine cross-family frame-completion contribution.** P3 originated; P4 endorsed with narrower scope; synthesis adopted. Without P3+P4 (Codex/GPT-5.5), the synthesis would likely have defaulted to P1's "thin index plus per-record Markdown" pattern that P3 + P4 explicitly named as Substrate-N2-only-superficially. **n=2 Substrate-Nn-reframes originated by P3 Outsider role**: S050 P3 surfaced Substrate-N1/N2/N3; S058 P3 surfaced Substrate-N3.5. Pattern: P3 Outsider role consistently surfaces alternative-architecture reframes the Claude perspectives miss. This is a Cause-3 corroborating-evidence data point per OI-004 closed-state forward semantics.

2. **First-of-record P4-blocked-on-precondition refusal event** demonstrates the laundering-audit role's anti-laundering-by-process discipline. Recorded as engine-conventional behaviour. Future MAD sessions running cross-family laundering-audit role should pre-wrap canonical perspective files before launching P4 OR explicitly reference alternative input source paths in P4 brief.

3. **Engine-v9 closes preservation depth 8 (second-longest after engine-v7 11-session record).** Engine-v10 is the second-instance MAD-adopted-new-engine-definition-spec class; the bump-provenance class is reified at n=2.

4. **Substrate-N3.5 distinction from sharded-Markdown is the load-bearing reframe.** Records-contract.md v1 §1 explicitly rejects sharded-Markdown-as-Substrate-N2; the source-of-truth-vs-witness discipline is what makes this Substrate-N2 substantively rather than nominally. §10.4-M13 minority preserves the failure-mode warning.

5. **WX-34-1 retired at S058 — first watchpoint structurally retired by methodology evolution rather than pressure-resolution.** WX-34-1 was opened at S034 (or earlier) tracking SESSION-LOG.md ceiling pressure; periodic restructures (S022 R8a / S040 D-123 / S051 D-178) addressed pressure events; S058 migration addresses the structural cause. Pattern: when a watchpoint tracks a structurally-resolvable concern, migration retires the watchpoint; when it tracks an ongoing-monitoring concern, periodic remediation addresses it.

6. **Cross-family contribution evidence cumulative**: S050 (Substrate-N3 P3-originated, adopted as Substrate-1 implementation under Substrate-N3-architecture-as-frame; 5 minorities preserved with cross-family-load-bearing); S058 (Substrate-N3.5 P3-originated, adopted as Substrate-N3.5-pilot-toward-Direction-A; 4 minorities preserved with cross-family-load-bearing). Cumulative Cause-3 corroborating-evidence data points 79 (S041 closure) → 81+ (S058 adds n=2 cross-family-load-bearing data points).

7. **Records-substrate operates as engine-defined contract + engine-adjacent implementation pattern** (mirrors retrieval-contract.md adoption pattern at S050). The contract is in §3 enumeration; implementation is workspace-local. External workspaces inherit the contract via bootstrap; implementation copied per §5 (deferred to follow-up session).

8. **Thirtieth-consecutive housekeeping `[none]`-trigger pattern.** D-205 extends pattern since D-126 Session 041. Engine-conventional.

9. **First operator-surfaced-channel-formalisation event in workspace history** (§10.4-M10 written-warrant amendment with new clause (c) per D-204 Part A). Activates the operator-surfacing-channel as a formalised activation mechanism for §10.4-M-N minorities.

10. **Path AS-MAD-execution reified at n=2 (S050 + S058).** Path AS-class observations: S049 + S050 + S057 + S058 = 4 Path-AS-class sessions in workspace history. Path AS pure (synthesis only) reified n=2 at S057. Path AS-MAD-execution (synthesis-followed-by-MAD) reified n=2 at S058.

## §11 Commit and close

This close file is committed with the S058 artefacts:
- `provenance/058-session/00-assessment.md` (pre-work commit `c0fc8e0` already done).
- `provenance/058-session/01-brief-shared.md` + `01-brief-p[1-4].md` (briefs commit `7226ea3` already done).
- `provenance/058-session/01a/01b/01c-perspective-*.md` + codex logs (perspectives commit `a2c9805` already done).
- `provenance/058-session/01d-perspective-cross-family-reviewer.md` (this close commit).
- `provenance/058-session/01-deliberation.md` (this close commit).
- `provenance/058-session/02-decisions.md` (this close commit).
- `provenance/058-session/03-close.md` (this file; this close commit).
- `provenance/058-session/manifests/*.manifest.yaml` + `participants.yaml` (this close commit).
- `provenance/058-session/archive/pre-records-SESSION-LOG/` (manifest + source; this close commit).
- `specifications/records-contract.md` v1 (NEW; this close commit).
- `specifications/workspace-structure.md` v7 + `workspace-structure-v6.md` (this close commit).
- `specifications/read-contract.md` v6 + `read-contract-v5.md` (this close commit).
- `specifications/engine-manifest.md` (engine-v10 entry; this close commit).
- `tools/validate.sh` (check 25 + constants; this close commit).
- `tools/build_retrieval_index.py` (record-aware indexing; this close commit).
- `records/sessions/S001.md` through `records/sessions/S058.md` + `records/sessions/index.md` (59 files; this close commit).
- `engine-feedback/INDEX.md` + `engine-feedback/triage/EF-055-...md` (lifecycle update; this close commit).
- SESSION-LOG.md (DELETED from workspace root; this close commit).

Engine-v10 ratified per D-200 (preservation window count 1; second-instance MAD-adopted-new-engine-definition-spec class). 40 first-class minorities preserved (36 + 4 new from S058 MAD). 13 active OIs unchanged. Engine-feedback state 0 new / 1 triaged / 7 resolved / 0 rejected (EF-055 transitions triaged→resolved within session). Substrate-N3.5 pilot toward Direction A adopted as primary direction; phase-1 = SESSION-LOG.md only as proving slice. records-contract.md v1 created; workspace-structure.md v6→v7; read-contract.md v5→v6; engine-manifest.md engine-v10 entry; tools/validate.sh check 25; tools/build_retrieval_index.py record-aware indexing. SESSION-LOG.md migrated to records/sessions/ (58 records + thin index); pre-migration archive-pack at provenance/058-session/archive/pre-records-SESSION-LOG/. WX-34-1 SESSION-LOG.md ceiling-pressure permanently retired at S058 by migration. WX-58-1 records-discipline-soak observation window opens. Engine-v9 closes preservation depth 8 (second-longest after engine-v7 11-session record); §5.4 cadence minority does NOT re-escalate per content-driven-bump precedent chain. D-129 thirteenth-consecutive + D-138 thirteenth-consecutive clean exercises. WX-28-1 twenty-eighth close-rotation S052 OUT S058 IN zero retention-exceptions. WX-24-1 MAD v4 thirty-first-session no-growth streak new record. Thirtieth-consecutive housekeeping `[none]`-trigger pattern. §10.4-M10 written-warrant amendment formalised (operator-surfacing channel as third clause). First-of-record P4-blocked-on-precondition refusal event (methodology-correct anti-laundering-by-process). First-of-record cross-family-originated-and-adopted reframe-architecture event (Substrate-N3.5 not in pre-MAD design-space.md §4 inventory).
