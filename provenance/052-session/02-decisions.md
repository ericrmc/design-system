---
session: 052
title: Decisions — Path T+L ratification (D-180) + Direction B adoption for EF-051 resolution (D-181) + housekeeping (D-182)
date: 2026-04-25
status: complete
---

# Decisions — Session 052

Three decisions this session. All classified `[none]` triggers per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required (no substantive-revision-scale question; narrow-implementation direction-clear; single-orchestrator Case Steward appropriate).

## D-180: Path T+L ratified; single-orchestrator default-agent session resolving EF-051 in same session as triage

**Triggers met:** `[none]`.

**Single-agent reason**: Operator input "Proceed with default agent path and do not halt." treats Halt-1 as default-ratified at recommended-option positions per `00-assessment.md` §7. Scope is narrow: triage + same-session implementation fix for a directionally-clear engine-adjacent defect (EF-051). Per S048 D-152 Path T precedent (EF-001 resolved in-session because direction was clear via `operator_directed_resolution` frontmatter), S052 applies the same shape: triage-record + implementation fix + INDEX.md state transition in the same session. No substantive-revision-scale question; no 3-of-4-or-higher convergence claim; no new first-class minority to preserve. Single-orchestrator Case Steward is the appropriate shape. This is the **seventh consecutive minor bug-fix-style implementation-realignment** per OI-002 heuristic (precedent chain: S022 R8a / S030 D-100 / S033 D-108 / S040 D-123 / S046 D-143 / S051 D-177 / S052 D-181).

**Decision**: Adopt Path T+L (Triage-classify + minor Path L implementation fix) as the default-agent session shape for S052. Subordinate decisions D-181 (implementation) + D-182 (housekeeping) execute under this path.

**Rationale**:

1. Per `prompts/development.md` §How to operate: "If `engine-feedback/INDEX.md` shows feedback records with `status: new`, the session's Assess activity should consider whether triage of one or more inbox items is the right increment for this session." EF-051 was `status: new` at S052 open. Triage is the canonical response.

2. Per S051 close §7 recommendation: "EF-051 awaits triage; status `new` at S052 open. Recommended: triage at S052 (Path T — per S048 precedent — if inbox becomes primary session agenda) OR bundled with other work if operator surfaces different agenda." Operator surfaced no different agenda.

3. Per EF-051 §Triage disposition recommendation: "S052 or later — single-orchestrator minor-amendment Path L. Not MAD-required (no kernel amendment; no spec revision beyond a possible §Honest-limit clarification in `retrieval-contract.md` if the contract is narrowed instead of the implementation fixed). Engine-v impact: minor per OI-002 if implementation fix only; no engine-v bump."

4. D-129 standing discipline seventh-consecutive exercise: five considered-and-rejected non-Path-T+L alternatives per `00-assessment.md` §4a (Path A pure rejected contradicts §How to operate / Path T pure triage-only rejected direction clear + operator recommends same-session / Path L pure skip-triage rejected breaks §engine-feedback lifecycle / Path MAD rejected no substantive-revision-scale question / Path L+A again rejected no WX-34-1 pressure).

**Path-label convention**: "T+L" is a bundled label at first-instance this session; reification deferred until n=2. "T" alone reifies at n=2 this session (S048 first instance + S052 second instance of Path T triage-shape); "L" already reified at n=2 (S040 + S051 Path L+A). T+L as a bundled label is new.

**Alternatives considered**: five non-Path-T+L alternatives surfaced in `00-assessment.md` §4a with non-vacuous rationales. Not re-enumerated here to avoid cross-file duplication; Case Steward cross-references the assessment per S022 R8a citation convention.

**Non-Claude participation**: skipped (single-orchestrator; no participant composition). `retry_in_session: null` — no deferred deliberation.

## D-181: Direction B adopted for EF-051 resolution; tools/retrieval_server.py minor implementation edit; no engine-v bump

**Triggers met:** `[none]`. No `multi-agent-deliberation.md` v4 §When MAD Is Required trigger fires: no substantive engine-definition file revision; narrow implementation fix within a single engine-adjacent file; operator "do not halt" default-ratified direction selection at `00-assessment.md` §4b.

**Decision**: Adopt Direction B (query-time aliases consultation) for EF-051 resolution. Edit `tools/retrieval_server.py` to:

1. Add `import yaml` with ImportError-tolerant fallback (`yaml = None` if absent; aliases.yaml support becomes degraded).
2. Add `load_aliases_map(workspace: Path) -> dict` module-level function returning `{alias: canonical}` dict from `specifications/aliases.yaml`.
3. In `build_server()`, load `aliases_map = load_aliases_map(workspace)` once at server startup (closure-scope); track `aliases_available` + `aliases_present` + `missing` for degraded-mode disclosure per retrieval-contract v1 §3 clause 3.
4. Insert **Strategy 1.5** between Strategy 1 (direct canonical) and Strategy 2 (id_text) in `resolve_id()`: if `aliases_map.get(alias)` returns a non-None canonical distinct from `alias`, re-run Strategy 1 against the resolved canonical.
5. Extend `_match_payload` signature with `degraded: bool` + `missing: list | None` defaults for backward-compatibility; all three match-return paths now report accurate degraded-mode state.
6. Update Strategy 2 inline comment to describe current behaviour accurately (removes false promise about alias remapping at index-time for non-regex aliases).
7. Update no-match return's `reason` string to `"no match in identifiers table or aliases.yaml"`.

**Classification — minor per OI-002**: The contract `specifications/retrieval-contract.md` v1 §2.2 is unchanged (and is correct as written). The implementation previously did not fulfill the contract for non-ID-pattern aliases; Direction B brings the implementation into fulfillment. Per the 7-precedent chain of minor bug-fix-style source-realignments (S022 R8a / S030 D-100 / S033 D-108 / S040 D-123 / S046 D-143 / S051 D-177 / **S052 D-181**), this is the **seventh minor bug-fix-style edit**. No engine-v bump.

**Engine-v9 preserved**; preservation window count advances from 1 (S051) to 2 (S052 close).

**Smoke-test evidence** (captured in `engine-feedback/triage/EF-051-aliases-yaml-not-consulted-at-query-time.md` §Smoke-test evidence and in this session's `03-close.md` §6 WX-50-1 3-field recording): 8 test cases exercised against `.cache/retrieval.db` (S051-built; unchanged this session — Direction B is query-time fix not requiring rebuild). All 8 PASS:
- 5 alias-indirection resolutions via new Strategy 1.5: `"M5"` → `§10.4-M5`; `"Reviser OI-tag-only"` → `§10.4-M5`; `"Decision 172"` → `D-172`; `"phase-2 gate"` → `WX-50-1`; `"OI 19"` → `OI-019`.
- 2 direct-canonical resolutions via unchanged Strategy 1: `"D-172"` → `D-172`; `"§10.4-M5"` → `§10.4-M5`.
- 1 None-case via no-match return: `"NONEXISTENT-999"` → None (per retrieval-contract v1 §2.2 "Never raises on unknown alias").

Aliases map observed size: **20 alias→canonical mappings** across 8 canonical entries in `specifications/aliases.yaml`.

**Direction A deferred**: Index-time reverse-remap (synthetic `identifiers` rows for each alias pointing to the canonical's declared location) is not adopted this session. Direction B is sufficient for §2.2 compliance; Direction A's distinctive benefit (alias text searchable via BM25 `search()`) is not on current requirements surface; Direction A remains additive-compatible if FTS-search-over-alias-text becomes desired later (no foreclosure). See triage record §Direction A deferred for full rationale.

**EF-051 lifecycle transition**:
- Inbox state `status: inbox` unchanged per intake-preserved convention (`workspace-structure.md` v6 §engine-feedback "intake files preserved verbatim"; triage file + INDEX.md carry the lifecycle state).
- Triage file `engine-feedback/triage/EF-051-aliases-yaml-not-consulted-at-query-time.md` created this session with `status: resolved`.
- INDEX.md status summary: 1 new / 1 triaged / 3 resolved / 0 rejected → **0 new / 1 triaged / 4 resolved / 0 rejected**.
- Inbox→triaged→resolved lifecycle complete within a single session for a self-dev-originated defect.

**Alternatives considered** (single-agent reason; direction selection only):
- Direction A (index-time reverse-remap): rejected as primary because Direction B has smaller surface, no schema change, and consistent with "aliases.yaml authoritative" framing per retrieval-contract v1 §2.3. Additive-compatible for future adoption.
- "Both Direction A and B": rejected because Direction B alone is sufficient and minimal surface change principle applies. No current evidence alias-text-FTS-search is needed.
- "Narrow §2.2 spec instead of fix implementation": rejected because §2.2 is correct as written (operator intent at S050 adoption was that aliases.yaml be authoritative at query time); narrowing the contract would silently accept the defect rather than fix it.

**Non-Claude participation**: skipped (single-orchestrator; narrow implementation fix). `retry_in_session: null`.

## D-182: Housekeeping consolidation

**Triggers met:** `[none]`.

**Single-agent reason**: Housekeeping records standing-discipline outcomes + watchpoint counter advances + engine-version preservation + minority dispositions across one decision record per `multi-agent-deliberation.md` v4 convention. No deliberation required.

### §D-182a — D-129 standing discipline seventh-consecutive clean exercise

S046/S047/S048/S049/S050/S051/S052 all applied D-129 cleanly. §5.12 Path-Selection Defender reopen warrant (a) "D-129 convention degradation" does not fire. Convention continues operational as standing discipline.

### §D-182b — D-138 folder-name default seventh-consecutive clean exercise

`052-session` no suffix, no slug. S046/S047/S048/S049/S050/S051/S052 all clean. `workspace-structure.md` v6 §provenance folder-name discipline continues operational.

### §D-182c — Path T reified at n=2

S048 first instance (EF-001 + EF-047 triage) + S052 second instance (EF-051 triage). Path T is now a reified default-agent path-label for inbox-triage default-agent path. Forward-naming convention: path-labels reify at n=2 per S051 Path L+A precedent.

### §D-182d — Path T+L as a bundled label at first instance

S052 is first instance of "T+L" as a bundled label (combining Path T triage-classify + Path L minor implementation fix in a single session). Reification of the bundled label deferred until n=2. Forward observation: if a future session bundles triage + same-session implementation fix with a recognisable T+L shape, the bundled label reifies.

### §D-182e — WX-28-1 twenty-second close-rotation zero retention-exceptions

S046 close rotates OUT at S052 close; S052 close enters. Retention window post-rotation: S047/S048/S049/S050/S051/S052. Zero retention-exceptions recorded. Streak continues well past S038 10-of-10 vindication threshold.

### §D-182f — WX-24-1 MAD v4 twenty-fifth-session no-growth streak new record

`multi-agent-deliberation.md` v4 unchanged at 6637 words. Twenty-fifth consecutive session with no MAD amendment (S043–S052). New record from the S042 reset point.

### §D-182g — WX-34-1 remediated at S051 preserved

SESSION-LOG.md at S052 close (post-thin-row append): approximately 5,000 words (4,846 pre-row + ≤180 row). Well under 6K soft warning; well under 8K hard ceiling. WX-34-1 remediation holds; forward observation unchanged.

### §D-182h — WX-50-1 phase-2 gate second-session 3-field recording

S050 baseline 0 / S051 first non-zero recording / S052 second non-zero recording. See `03-close.md` §6 for full WX-50-1 payload. Phase-2 gate status at S052 close:

- **Condition 1** (≥2 sessions in S050–S053 record ≥1 `results_used_with_artefact_id` entry): S050 = 0; S051 = 2; S052 = 7 (all via smoke-test verifying EF-051 fix; no "normal session work" retrieval calls this session since I used the Read tool directly rather than the MCP substrate for default-read surface acquisition). **Ambiguous**: if smoke-test `results_used` entries count as qualifying, S051 + S052 are the ≥2 sessions and Condition 1 is satisfied. If operator requires "normal session work" rather than verification-scoped invocations, S052 does not yet qualify and evaluation must continue at S053. **Decision deferred to operator at phase-2 MAD time** per retrieval-contract v1 §6 closing paragraph ("Phase-2 gate is operator-authoritative. The WX-50-1 recording convention is specified but the trigger-firing interpretation at S053 close will be a Case Steward call with operator oversight; it is not an automatic decision rule").
- **Condition 2** (≥1 session records ≥1 fallback where missing capability is structured-filter OR graph-traversal): S051 = 1 fallback but category was alias-indirection (not structured-filter/graph-traversal). S052 = 0 new fallbacks (EF-051 resolves the alias-indirection fallback; no new fallback category surfaces). **NOT satisfied**.
- **Condition 3** (≥1 external-workspace adoption records ≥1 useful domain-context query): not yet. selvedge-disaster-response has not been re-bootstrapped with substrate.

**Gate status at S052 close**: **Condition 1 arguable-satisfied-pending-operator-interpretation**; Conditions 2 + 3 not satisfied. Per retrieval-contract.md v1 §6 Case Steward framing, S053 close is the formal evaluation point. If operator at S053 close or phase-2 MAD time accepts smoke-test invocations as qualifying, phase-2 fires at S052 retroactively; if not, evaluation continues through S053.

**S053 recommendation**: if S053 substantive work does NOT use substrate via MCP transport in normal-session-work flow, the operator-interpretation question becomes load-bearing at the S053 close Case-Steward call. If S053 does use substrate in normal flow (regardless of smoke-test status), Condition 1 satisfies unambiguously via S051 + S053 and the S052 ambiguity is moot.

**Phase-2 adoption trigger forward observation** (if/when gate fires): per retrieval-contract.md v1 §6, "If phase-2 fires, a dedicated MAD session adopts (selectively, not automatically all): `edges` table + `traverse` MCP tool; `frontmatter_kv` table + `list_identifiers` MCP tool; `warrants_currently_met` MCP tool; `verify_archive_path` MCP tool; Soft kernel §1a Warrant-evaluation sub-activity amendment to `methodology-kernel.md`; Validator check 24; Re-examination of Q6 `syncs_with:` field question with §7.5 distinction preserved." S053+ is the candidate adoption session. S052 does not execute phase-2 adoption itself.

**Honest-limit note**: the count of 7 `results_used` entries at S052 is artefact of smoke-testing a specific fix rather than organic session-work retrieval. A more conservative counting rule would be "≥2 sessions in S050–S053 record ≥1 entry used to produce decision content that could not have been produced without the substrate". Under that rule, S051 = 2 (the canonical citations it recorded per §10.4-M5 + D-172 — both verified via MCP `resolve_id` though the operator could have used Read directly); S052 = 0 (the smoke-test calls verify the fix but produce no unique decision content — the fix itself is the decision content, verified by any mechanism). This conservative rule would leave Condition 1 unsatisfied at S052 close and continue evaluation at S053. Recorded transparently; operator chooses.

### §D-182i — Engine-v9 preservation window count 1 → 2

Engine-v9 preserved; preservation window count advances to 2 (S051 first post-v9 + S052 second post-v9). Modest depth; engine-v7 window reached 11 (the prior record). §5.4 cadence minority does not re-escalate (non-bump session; precedent chain v5–v9 intact).

### §D-182j — 36 first-class minorities preserved unchanged

No new minority preserved (single-orchestrator; no dissent surface); no minority discharged through vindication or rejection. §10.4-M1–M11 + §5.1/§5.4/§5.5/§5.6/§5.7/§5.8/§5.9/§5.10/§5.11/§5.12/§5.13/§5.14 + S024 A.4 four + S027 §A/§B/§C + `reference-validation.md` v3 §10.1/§10.2/§10.3 all preserved. Count 36 unchanged.

### §D-182k — Active OI count 13 unchanged

No OI opened, resolved, or amended. EF-051 triage did not promote to OI (classification minor per OI-002; implementation-level fix self-contained).

### §D-182l — WX-35-1 claim discipline applied cleanly

Explicit retractions recorded in `03-close.md` §1c. `SESSION-LOG.md` edited at close; `tools/retrieval_server.py` edited this session; `engine-feedback/INDEX.md` edited; `engine-feedback/triage/EF-051-*.md` created. All other listed targets (specifications, OI files, PROMPT.md, prompts/, MODE.md, CLAUDE.md, `tools/validate.sh`, `tools/build_retrieval_index.py`, `tools/bootstrap-external-workspace.sh`, `.mcp.json`, `.gitignore`, `specifications/aliases.yaml`) NOT edited per explicit retraction.

### §D-182m — Substrate-smoke-test pattern repeatable

S050 §8 forward-commitment (code-review-only at adoption + first-real-use at next-session + defect-surfaces-as-engine-feedback-intake) vindicated a second time at S052: S051 exercised substrate → EF-051 defect surfaced → S052 resolves. Pattern repeatable for future substrate adoptions that defer smoke-testing to the next session.

### §D-182n — S047 D-150 three deferred candidates unchanged

Candidates (i) kernel §7 qualitative-multi-agent label / (ii) workspace-structure §provenance supersession-marker codification / (iii) OI state-machine constraint-invalidated transition remain preserved for post-arc `selvedge-disaster-response` self-dev review. Candidate (iv) subsumed at S048 D-153. Unchanged at S052.

## Decision summary

| ID | Label | Triggers | Classification |
|----|-------|----------|----------------|
| D-180 | Path T+L ratified; single-orchestrator default-agent | `[none]` | ratification |
| D-181 | Direction B adopted for EF-051; `tools/retrieval_server.py` minor edit | `[none]` | minor per OI-002 |
| D-182 | Housekeeping consolidation (14 sub-sections a–n) | `[none]` | housekeeping |

No MAD convened. 36 first-class minorities preserved unchanged. Engine-v9 preserved (window count 1 → 2). Inbox state 1 new / 1 triaged / 3 resolved / 0 rejected → 0 new / 1 triaged / 4 resolved / 0 rejected. 13 active OIs unchanged.
