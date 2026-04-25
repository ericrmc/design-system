---
session: 059
title: Decisions — Path T+L bundled scope ratified (D-206); EF-058-uv-migration adopted via 6-step Path L (D-207); EF-058-claude-md-drift triaged-deferred substantive-arc (D-208); EF-058-tier-2-validation triaged-deferred substantive-arc per operator MAD preference (D-209); minor retrieval-contract.md v1 §5.1+§5+§10 template-shape sync amendment (D-210); records-substrate bootstrap implementation in tools/bootstrap-external-workspace.sh discharges S058 honest-limit #2 (D-211); housekeeping (D-212)
date: 2026-04-25
status: complete
---

# Decisions — Session 059

Seven decisions: D-206 Path T+L bundled scope ratified [default-agent]; D-207 EF-058-uv-migration adopted via 6-step Path L [default-agent + operator-recommended at intake]; D-208 EF-058-claude-md-drift triaged substantive-arc-deferred; D-209 EF-058-tier-2-validation triaged substantive-arc-deferred per operator MAD preference; D-210 minor retrieval-contract.md v1 §5.1+§5+§10 template-shape sync amendment; D-211 records-substrate bootstrap implementation discharges S058 honest-limit #2; D-212 housekeeping `[none]`-trigger pattern (thirty-first-consecutive).

## D-206: Path T+L bundled scope ratified for S059

**Context**: S058 close §7 enumerated next-session candidates (Path AS-MAD-execution phase-2 / Path A / Path L+A / Path PD/OS). Three operator-surfaced post-session intake records (EF-058-uv-migration / EF-058-claude-md-drift / EF-058-tier-2-validation) plus one S058 honest-limit-deferred work item (records-substrate bootstrap implementation per records-contract.md v1 §5) present S059 with non-trivial agenda. Per intake dispositions:
- EF-058-uv-migration recommends Path T+L same-session resolution.
- EF-058-claude-md-drift recommends defer-to-substantive-arc.
- EF-058-tier-2-validation recommends defer-to-substantive-arc per operator "should go through MAD" preference.

**Decision**: Path T+L bundled scope adopted for S059. Triage all 3 EF-058 inbox records + Path L implementation of EF-058-uv-migration's 6-step recommended path + records-substrate bootstrap implementation discharging S058 honest-limit #2 + minor amendment to retrieval-contract.md v1 §5.1+§5+§10 for template-shape sync.

**Triggers met:** `[none]`.

**Single-agent reason:** Path-ratification decision; this decision does not itself adopt any spec edit (subordinate decisions D-207/D-210/D-211 carry their own trigger declarations where applicable). Path-selection per S058 close §7 default + operator intake-disposition convergence. No MAD-triggers fire at the path-ratification level: the EF-058-uv-migration intake's concrete defect-fix path is single-orchestrator-tractable per OI-002 minor classification; the two substantive-arc-deferred records (EF-058-claude-md-drift + EF-058-tier-2-validation) are properly classified at triage and explicitly deferred to dedicated future MAD per their intake dispositions; engine-v10 is preserved across all S059 work. WX-58-1 phase-2 gate cannot fire at S059 anyway (per records-contract.md v1 §6 conditions: needs S059 close 5-field recording + ≥95% migrated-ID resolution at S059 + zero record-witness drift; cannot phase-2 at S059).

**Alternatives considered + rejected**: Per 00-assessment.md §3b D-129 standing discipline:
1. Path A (Watch) pure — rejected: three operator-surfaced intake records present non-trivial agenda; default Path A would defer all three without triage and leave eight-session MCP-transport-unverified chain unresolved.
2. Path AS-MAD-execution (substantive-arc adoption for EF-058-tier-2-validation) — rejected: requires phase-1 synthesis BEFORE phase-2 MAD per S057 EF-055 precedent; cannot skip phase-1.
3. Path AS-MAD-execution phase-2 (records-substrate mirrored-minority migration) — rejected: WX-58-1 phase-2 gate cannot fire until S060 close evaluation.
4. Compressed single-session resolution-of-all-three EF records via single-orchestrator — rejected: cannot single-orchestrate substantive arcs per d016_2 + d016_3 triggers.
5. Defer EF-058-uv-migration to substantive-arc-with-tier-2-validation — rejected: substrate-transport resolution is prerequisite for the highest-leverage Tier-2-reviewer mechanism candidate (α) per EF-058-tier-2-validation §Suggested Change.

§5.12 Path-Selection Defender reopen warrant (a) "D-129 convention degradation" does NOT fire.

**Status**: ratified.

## D-207: EF-058-substrate-runtime-uv-migration-recommended-path adopted via 6-step Path L

**Context**: S051-S058 8-session MCP stdio transport unverified honest-limit chain. Root cause: `.mcp.json` declared `command: "python3"` (system Python without `mcp[cli]` or `pyyaml`); when Claude Code spawns the server at startup, the import fails, the server crashes silently, Claude Code marks it unavailable. CLAUDE.md §Tools (added by D-144 Session 046) specifies `uv tool` install path. Operator-surfaced post-session at S058 with concrete 6-step fix recommendation.

**Decision**: 6-step Path L per EF-058-uv-migration intake §Suggested Change adopted:

1. `tools/retrieval_server.py` — added PEP 723 inline-deps (requires-python >=3.11; dependencies [mcp[cli], pyyaml]) at top after shebang.
2. `tools/build_retrieval_index.py` — added PEP 723 inline-deps (requires-python >=3.11; dependencies [pyyaml]) at top after shebang.
3. `.mcp.json` — `command: "python3"` → `command: "uv"`; `args: ["tools/retrieval_server.py"]` → `args: ["run", "tools/retrieval_server.py"]`.
4. `tools/bootstrap-external-workspace.sh` — refactored: replaced pip-install instructions with uv-only path (Next-steps step 2: "Ensure uv is installed; substrate scripts use PEP 723 inline metadata; uv resolves deps automatically per `uv run`"); replaced `python3 tools/build_retrieval_index.py` with `uv run tools/build_retrieval_index.py` (Next-steps step 3); removed `.cache/venv/` setup language; bundled records-substrate bootstrap per D-211.
5. `.cache/venv/` removal — deleted (gitignored; not committed).
6. Smoke-test — partial in-session: `uv run tools/build_retrieval_index.py` rebuild verified (557 documents / 59,472 identifiers; up from S058 close 549/58,198); `uv run tools/retrieval_server.py --help` PEP 723 dep resolution verified. Full MCP stdio smoke-test deferred to next session-open per Claude Code restart constraint (close-criterion at S060 open: verify `mcp__selvedge-retrieval__search`/`resolve_id`/`forward_references` appear; call `resolve_id("S058")` returns records/sessions/S058.md via tool call).

**Triggers met:** `[none]`.

**Single-agent reason:** Defect-fix-shape Path L on engine-adjacent files (`tools/retrieval_server.py`, `tools/build_retrieval_index.py`, `.mcp.json`, `tools/bootstrap-external-workspace.sh`); no engine-definition-spec edit in this decision (the paired retrieval-contract.md v1 minor amendment is a separate decision D-210 with its own trigger declaration). Direction-clear minor per OI-002 — operator-recommended at intake explicitly: "Single-session Path L (minor implementation fix per OI-002) per S046 D-143 / S052 D-181 / S054 D-186 source-realignment precedent chain." Tenth source-realignment-or-extension precedent chain instance per S048 D-152 + S052 D-181 + S054 D-185 + D-186 + D-187 chain. Single-orchestrator Case Steward implementation is the appropriate shape; deliberation not warranted for a fix that addresses 8-session laundered operational debt with concrete config-shape changes aligned with operator standing instruction in CLAUDE.md §Tools.

**Alternatives considered + rejected**: None at the direction level (intake recommended single concrete path; no Direction B/C alternatives to consider). At the implementation-detail level, the choice between PEP 723 inline-metadata (adopted) vs alternative `uv tool install` (rejected — `uv tool install` is for CLI-tools exposing entry-points; library-imports use PEP 723 + `uv run`) was discussed in EF-058-uv-migration §Evidence and resolved in favour of PEP 723 per uv documentation.

**Status**: resolved (full smoke-test deferred per honest-limit; reclassification path per intake §Suggested Change closing paragraph if non-trivial defect surfaces at next-session smoke-test).

## D-208: EF-058-claude-md-tools-clause-not-cross-checked-by-mad triaged substantive-arc-deferred

**Context**: S050 4-perspective MAD on EF-047-retrieval-discipline landed on pip+venv runtime; CLAUDE.md §Tools standing operator instruction specifies `uv tool` install path; the deliberation surface did not consider `uv` as alternative; P4 cross-family laundering-audit did not include CLAUDE.md cross-check in audit scope. Methodological observation about MAD shared-frame-blindness against operator-standing-instructions; concrete instance of pretraining-default-pattern overriding operator-specified direction unaudited.

**Decision**: Triaged substantive-arc-shape; deferred to dedicated future MAD session per intake disposition. Triage record at `engine-feedback/triage/EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` carries `status: triaged`, `classification: substantive-arc`, `direction_selected: deferred`, plus enumeration of five candidate directions (a)-(e) per intake §Suggested Change.

**Triggers met:** `[none]`.

**Single-agent reason:** Triage classification is single-orchestrator-tractable per S048 D-153 + S054 D-185 precedent. This decision triages-and-defers; it does not adopt any substantive direction. Substantive resolution (which would invoke MAD-required triggers per the candidate directions enumerated in the triage record) is explicitly deferred to a dedicated future MAD per intake recommendation "NOT recommended for same-session resolution." The triage classification itself names the candidate directions but does not select among them; selection requires the deferred deliberation. Engine-v10 preserved at this triage; future substantive-arc resolution may produce engine-v11 candidate per direction adopted.

**Alternatives considered + rejected**: Same-session resolution (rejected: intake explicitly recommends NOT same-session); operator-directed-resolution short-circuit (rejected: no `operator_directed_resolution` frontmatter field on inbox record; operator's preference is for substantive-arc).

**Cross-linkage**: Per intake §Why It Matters point 3 + EF-058-tier-2-validation §Suggested Change open-question 6: cross-linkage with EF-058-tier-2-validation likely. Joint design-space.md possible if scope-coherent at phase-1 synthesis.

**Status**: triaged-deferred; resolution path is dedicated future MAD per S057 EF-055 substantive-arc precedent chain. Engine-v11 candidate per direction adopted (substantive if (b)/(c); minor if (a) alone).

## D-209: EF-058-tier-2-validation-discipline-by-distinct-agent triaged substantive-arc-deferred per operator MAD preference

**Context**: Eight-session honest-limit chain S051-S058 ("MCP stdio transport remains unverified") demonstrates Tier 2 self-validation by the same agent that performed the work cannot detect the patterns it is supposed to catch. validation-approach.md v5 §Limitations names the conflict-of-interest but treats naming as mitigation; multi-agent-deliberation.md v4 §Synthesis forbids self-synthesis at MAD level but tolerates self-validation at session-close-Tier-2 level (architectural asymmetry). Operator-stated preference at intake: "should go through MAD." Meta-pattern subsuming the other two EF-058 records as concrete instances (operational + methodological).

**Decision**: Triaged substantive-arc-shape per S057 EF-055 precedent chain; deferred to dedicated future MAD session per intake disposition + operator preference. Triage record at `engine-feedback/triage/EF-058-tier-2-validation-discipline-by-distinct-agent.md` carries `status: triaged`, `classification: substantive-arc`, `direction_selected: deferred`, plus enumeration of five candidate mechanisms (α)-(ε) per intake §Suggested Change.

**Triggers met:** `[none]`.

**Single-agent reason:** Triage classification is single-orchestrator-tractable. This decision triages-and-defers; it does not adopt any substantive direction. Operator-stated preference at intake "should go through MAD" is explicitly honoured via deferral. Substantive resolution requires three-phase arc per intake §Suggested Change: phase-1 synthesis/design-space (Path AS Shape-1) → phase-2 4-perspective two-family MAD (Path AS-MAD-execution) → phase-3 adoption (engine-v11 highly-likely candidate). Cross-family deliberation is essential because the question itself is "what cross-family discipline should apply at session close" — a Claude-only deliberation has the same conflict-of-interest the question investigates. Bootstrap-paradox is a recognised feature: resolving session(s) exercise discipline they formalise; observable evidence is the meta-cross-check on the deliberation. Engine-v10 preserved at this triage.

**Alternatives considered + rejected**: Same-session resolution (rejected: intake explicitly recommends NOT same-session per operator MAD preference); single-orchestrator triage of mechanism (α) "tools/validate.sh new check" alone (rejected: would foreclose deliberation between (α)/(β)/(γ)/(δ)/(ε); operator preference is substantive arc); voluntary application of an unspecified Tier 2 mechanism at S059 close itself (rejected: premature-formalisation; the methodology's resolution path is the dedicated MAD that will define the discipline).

**Cross-linkage**: Per intake §Why It Matters point 3 + EF-058-claude-md-drift cross-reference: this record subsumes EF-058-uv-migration (operational instance) + EF-058-claude-md-drift (methodological instance) as concrete instances of the structural cause (Tier 2 self-validation conflict-of-interest). Joint design-space.md possible at phase-1 synthesis if scope-coherent with EF-058-claude-md-drift.

**Operator audit recommendation**: per intake §Application-Scope Disposition closing paragraph, when the substantive-arc reaches phase-3 adoption, the resolving session's close should explicitly request operator audit as one-time cross-check on the bootstrap-paradox concern (the resolving MAD exercising the discipline it formalises is observable evidence; operator audit is the meta-cross-check on that evidence).

**Status**: triaged-deferred; resolution path is dedicated future MAD per S057 EF-055 substantive-arc precedent chain. Engine-v11 highly-likely candidate.

## D-210: Minor amendment to retrieval-contract.md v1 §5.1 + §5 + §10 for template-shape sync

**Context**: D-207 changes runtime from pip+venv to uv+PEP 723; the retrieval-contract.md v1 §5.1 `.mcp.json` template currently shows `command: "python3"`, §5 step 2 prints pip-install instructions, §10 honest-limit references "mcp[cli] + pyyaml Python dependency install at bootstrap." Template-shape and operator-instruction text drift from implementation post-D-207.

**Decision**: Three minor amendments executed:

- **§5.1 `.mcp.json` template**: `command: "python3"` → `command: "uv"`; `args: ["tools/retrieval_server.py"]` → `args: ["run", "tools/retrieval_server.py"]`. Added explanatory paragraph naming PEP 723 + `uv run` deps resolution. Template-shape sync with implementation per D-207.
- **§5 step 2 dependency-install instructions**: pip-install path → uv-only path (PEP 723 self-resolves; no install step beyond `uv` itself).
- **§5 step 3 build-index instruction**: `python3 tools/build_retrieval_index.py` → `uv run tools/build_retrieval_index.py`.
- **§5 closing "does NOT require" list**: added qualifier on "no network access" to acknowledge uv first-run dependency resolution exception (subsequent runs use cached deps).
- **§10 honest-limit "External-workspace portability tax" language**: nuance from "permanent" to "reduced but persistent"; "mcp[cli] + pyyaml two-package install" → "single-tool uv prerequisite + PEP 723 self-resolution"; broader §7.4 Substrate-N2 reframe minority preserved.

**Triggers met:** `[d016_2]`.

**Single-agent reason:** Direction-clear minor template-shape sync to retrieval-contract.md v1 §5.1+§5+§10. Spec content (§1 scope, §2 capabilities, §3 failure behaviour, §4 workspace state, §6 phase-2 gate, §7 minorities, §8 versioning, §9 validation) is unchanged; only template shape + operator-instruction text + honest-limit language sync with the new uv-based implementation. v1 preserved (no version bump per OI-002). Minor per OI-002 + S048 D-153 sub-pattern + S054 D-186 minor-template-shape-sync precedent. Tenth source-realignment-or-extension precedent chain instance (paired with D-207 implementation). Operator default-ratified the direction by surfacing no Halt and no scope override at S059 open. Deliberation is not appropriate for a 6-line YAML config sync + a paragraph of dependency-install-instruction text update.

**Alternatives considered + rejected**: Substantive v1→v2 bump bundled with the uv migration (rejected: spec content unchanged; v1→v2 would be over-bumping per OI-002; engine-v10 preserved); skip the amendment and let template drift (rejected: WX-35-1 file-edit-claim discipline + spec-as-source-of-truth requires template-shape sync at the same session as implementation change).

**Status**: resolved.

## D-211: Records-substrate bootstrap implementation in tools/bootstrap-external-workspace.sh discharges S058 honest-limit #2

**Context**: S058 close §8 honest-limit #2: "Tools/bootstrap-external-workspace.sh extension deferred. records-contract.md v1 §5 specifies the bootstrap-extension; actual implementation edits to tools/bootstrap-external-workspace.sh deferred to a minor follow-up session given S058 scope limits." S059 IS that follow-up session per S058 §7 next-session-items. Bundling with D-207 Path L because both edits touch the same file (bundling-by-coincidence per S054 D-185+D-186 precedent).

**Decision**: tools/bootstrap-external-workspace.sh extended per records-contract.md v1 §5 obligations:

- Added `records-contract.md` to `SPEC_FILES` array (engine-definition specs copied to new workspace).
- Added `records/sessions` to `mkdir -p` directory tree creation.
- Replaced SESSION-LOG.md scaffolding with thin `records/sessions/index.md` header per records-contract.md v1 §2.2 pattern (header text + table-header columns; no rows).
- Updated header documentation (lines 20-25): SKIPS list + step 5 description.
- Updated step count: "13 files per engine-manifest §3" → "14 files per engine-manifest §3".
- Updated §1c step description: "development-provenance + records-substrate scaffolding."

**Triggers met:** `[none]`.

**Single-agent reason:** Implementation-of-existing-normative-spec on engine-adjacent file (`tools/bootstrap-external-workspace.sh`); no engine-definition-spec edit in this decision (records-contract.md v1 §5 was already adopted at S058 D-201; this decision implements what the spec normatively requires). Per OI-002 minor (implementation-of-existing-normative-spec; bug-fix-style-or-additive-extension-without-semantic-change heuristic). Engine-v10 preserved. Bundled with D-207 because both edits touch the same file (bundling-by-coincidence per S054 D-185+D-186 precedent); avoids artificial split into two sessions editing the same file.

**Alternatives considered + rejected**: Defer implementation to S060+ as separate minor session (rejected: bundling-with-D-207 is efficient since both edits touch the same file; bundling-by-coincidence per S054 D-185+D-186 precedent; second separate session would be artificial split); also implement Markdown-witness auto-generation pipeline (rejected: deferred to phase-3+ per records-contract.md v1 §6).

**First-exercise**: Records-substrate bootstrap is post-S059 spec-aligned but not yet exercised against a fresh-bootstrap target. First external-workspace exercise will be the test of the bootstrap path; until then, the implementation is normatively-spec-aligned but not deeply user-tested per S059 honest-limit #3.

**Status**: resolved.

## D-212: Housekeeping `[none]`-trigger pattern (thirty-first-consecutive)

**Context**: Per S050 D-176 / S041 D-126 / S028 D-097 housekeeping discipline: at session close, surface any in-flight artefacts, audit-pending items, or maintenance work not covered by primary decisions.

**Decision**: No housekeeping items surfaced at S059. Pattern continues from D-126 Session 041 forward.

**Triggers met:** `[none]`.

**Single-agent reason:** Housekeeping records standing-discipline outcomes + watchpoint counter advances + engine-version preservation across one decision record per multi-agent-deliberation.md v4 convention. No deliberation required. All session work covered by D-206 through D-211. No in-flight artefacts requiring close-narrative housekeeping disposition. WX-22-1 forecast-error pattern unchanged (S059 forecast is well-bounded; aggregate close to forecast). WX-44-1 + WX-44-2 + WX-47-1 codex-CLI discipline NOT exercised (no codex CLI invocation at S059). §5.6 GPT-family-concentration window-ii observation NOT advanced at S059 (no MAD convened; window-ii substantive-deliberation data point chain S044+S045+S047+S050+S058 does not extend at S059).

**Status**: thirty-first-consecutive `[none]`-trigger pattern (S041→S059; S050 + S057 + S058 four-of-31 housekeeping-substantive sessions are the only exceptions in the run; pattern remains dominant). Engine-conventional.

## Decisions count + cross-references

7 decisions: D-206 + D-207 + D-208 + D-209 + D-210 + D-211 + D-212.

- **D-206 (path ratification)**: ratifies S058 §7 default + intake-disposition convergence + S058 honest-limit #2 follow-up obligation.
- **D-207 (uv-migration adoption)**: resolves EF-058-uv-migration; closes 8-session MCP-transport-unverified honest-limit chain (modulo next-session smoke-test).
- **D-208 (claude-md-drift triage)**: defers substantive-arc to dedicated future MAD.
- **D-209 (tier-2-validation triage)**: defers substantive-arc to dedicated future MAD per operator MAD preference.
- **D-210 (retrieval-contract.md v1 amendment)**: minor template-shape sync; v1 preserved.
- **D-211 (records-substrate bootstrap)**: discharges S058 honest-limit #2.
- **D-212 (housekeeping `[none]`)**: thirty-first-consecutive pattern.

Cross-session references: D-129 fourteenth-consecutive standing-discipline exercise; D-138 fourteenth-consecutive folder-name default exercise; WX-28-1 twenty-ninth close-rotation (S053 OUT, S059 IN); WX-24-1 MAD v4 thirty-second-session no-growth (extends S058's 31-session record); WX-43-1 cumulative tracking (no MAD at S059; explicit-instruction variant unchanged from S058 baseline n=0-of-13).

Engine-v10 preserved across all seven decisions (no engine-v bump). New first-class minorities preserved at S059: 0 (no MAD; no contested deliberation). Engine-wide minority count remains 40 at S059 close.
