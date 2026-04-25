---
session: 060
title: Decisions — D-213 Path L+A ratified mid-ratification per operator surface; D-214 (i)+(b)+(β) records-substrate-authority alignment adopted (eleventh source-realignment-or-extension); D-215 housekeeping (15 sub-sections; thirty-second-consecutive [none]-trigger pattern)
date: 2026-04-25
status: complete
---

# Decisions — Session 060

## D-213: Path L+A ratified mid-ratification per operator surface

**Triggers met:** [none]

**Triggers rationale:** Path-selection decision; operator-ratified single-orchestrator path. No methodology-kernel edit; no specification edit; no reasonable-disagreement-with-MAD-warranted (operator-audit halt pattern is the engine-conventional surface for path-selection per S048 D-152 / S054 D-185 / S055 D-189 / S056 D-191 / S057 D-194 / S059 D-206 precedent chain).

**Single-agent reason:** Path-selection by Case Steward absent operator override is the engine-conventional default-agent behavior per `prompts/development.md` §How to operate + `00-assessment.md` §3-§4 D-129 standing-discipline. Mid-ratification reshape per operator surface ("Do Path L+A and implement i") is engine-conventional per S057 D-194 precedent (Path A → Path AS Shape-1 reshape via operator surface). No deliberation surface beyond the operator-audit halts; no MAD warranted.

**Decision.** Adopt **Path L+A** (minor implementation fix paired with Watch). Reshape narrative:
1. Initial Case Steward determination (this assessment, draft phase): Path A (Watch) pure — record WX-58-1 third observation; defer resolve_id ordering question per S059 close §8 honest-limit #4 explicit "operator audit at S060" recommendation.
2. Operator surface mid-ratification: "Do Path L+A and implement i" — direction (i) per S059 close §8 honest-limit #4 enumeration. Reshape adopted via explicit-operator-ratification.
3. Within Path L+A: three sub-scope choices ratified through three operator-audit halts: (i) base SQL ordering fix → (b) per-record-vs-index extension → (β) frontmatter-id indexer extension.

**Alternatives considered (per D-129 standing discipline):**
1. Path A (Watch) pure — initial Case Steward draft; rejected via operator surface before commit.
2. Path L for direction (ii) spec clarification — rejected: relabels discrepancy without fixing operational substrate behavior.
3. Path L for direction (iii) phase-2 gate amendment — rejected: weakens gate's discriminatory value.
4. Path AS-MAD-execution phase-2 — rejected: WX-58-1 phase-2 gate cannot fire until S060 close completes 3-session window AND interpretive-disposition is settled.
5. Path AS Shape-1 for EF-058-tier-2-validation or EF-058-claude-md-drift substantive-arc kickoff — rejected: triage-deferred-substantive-arc dispositions name "dedicated future MAD"; operator agenda not surfaced for S060.

**Reversibility.** Path-selection is the one reversible element. If operator at any subsequent session prefers different path-shape for S060 reconstruction, the artefacts (assessment + decisions + close + records/sessions/S060.md row) are preserved for reference.

**Pattern observation.** Path L+A reified at n=3 in workspace history (Path L+A as bundled label first instantiated at S051 D-178 SESSION-LOG forced-restructure + Watch; next at S054 D-185 Path T+L bundled scope; next at S059 D-206 Path T+L bundled scope; **S060 D-213 = Path L+A pure, third-instance bundled-Path-L-with-Watch family**). The Path L family scope-coincidence pattern (multiple coherent edits to same file or related-scope files within single session) reified again.

---

## D-214: (i)+(b)+(β) records-substrate-authority alignment adopted

**Triggers met:** [none]

**Triggers rationale:** Engine-adjacent implementation only (`tools/retrieval_server.py` + `tools/build_retrieval_index.py`). No file in `engine-manifest.md` §3 enumeration is modified. No methodology-kernel edit. No specification edit (records-contract.md / retrieval-contract.md / read-contract.md / workspace-structure.md / engine-manifest.md all unchanged). Engine-v10 preserved. Per OI-002 substantive-vs-minor heuristic + S022 R8a / S030 D-100 / S033 D-108 / S040 D-123 / S046 D-143 / S051 D-178 / S052 D-181 / S054 D-186 / S054 D-187 / S059 D-207+D-210+D-211 source-realignment-or-extension precedent chain, this is **eleventh-instance** minor implementation realigning substrate behavior with normative spec semantics; no engine-v bump.

**Single-agent reason:** Source-realignment per spec normative semantics; operator-ratified scope at three sequential halts; single-orchestrator implementation per S054 D-186/D-187 / S059 D-207 precedent for engine-adjacent fixes. Multi-position surface (sub-options (i)/(ii)/(iii); within (i): (a)/(b); further extension (α)/(β)/(γ)) was at the operator-audit halt level, not at multi-perspective MAD level. No MAD warranted per the source-realignment-or-extension precedent chain.

**Decision.** Adopt three coordinated implementation changes within Path L+A:

### §a (i) Base SQL ordering: prefer records/<family>/ over specifications/

Modified four `ORDER BY CASE` clauses in `tools/retrieval_server.py` `resolve_id` function (Strategy 1 direct canonical lookup; Strategy 1.5 alias-resolution path; Strategy 2 id_text raw-alias lookup; Strategy 3 ID-pattern prefix match). Pre-fix:

```sql
ORDER BY CASE WHEN source_path LIKE 'specifications/%' THEN 0 ELSE 1 END, source_path, line LIMIT 1
```

Post-fix (4-tier with (b) extension below):

```sql
ORDER BY CASE
           WHEN source_path LIKE 'records/%'
                AND source_path NOT LIKE '%/index.md' THEN 0
           WHEN source_path LIKE 'records/%' THEN 1
           WHEN source_path LIKE 'specifications/%' THEN 2
           ELSE 3 END,
         source_path, line LIMIT 1
```

**Rationale.** records-contract.md v1 §2.1 declares the frontmatter `id` field "Authoritative; substrate `resolve_id` returns this canonical." Pre-fix, `resolve_id("S058")` returned `specifications/engine-manifest.md` line 23 (the engine-v10 entry mention) rather than `records/sessions/S058.md`. Post-fix, substrate behavior aligns with records-contract authority discipline.

### §b Per-record-vs-index ordering within records/

Records-contract.md v1 §2.1 explicit authority discipline: **"source record (frontmatter) > index row"**. Per-record `records/<family>/<id>.md` files are source-of-truth; per-family `records/<family>/index.md` is witness/projection. The 4-tier ORDER BY (above) reflects this:
- Rank 0: `records/<family>/` files NOT ending in `/index.md` (per-record source-of-truth).
- Rank 1: `records/<family>/index.md` (witness/projection).
- Rank 2: `specifications/`.
- Rank 3: everything else.

### §β Frontmatter-id indexer extension

`records/sessions/S001-S058.md` migrated at S058 D-203 are frontmatter-only (the SESSION-LOG row content moved into `summary:` field; body empty). `tools/build_retrieval_index.py` `extract_identifiers` line 123 only scans body — not frontmatter — so the migrated S<NNN> frontmatter `id:` fields produced zero rows in the `identifiers` table. (Only `S059.md` had body-text mentions, hence the asymmetry surfaced in initial smoke-test.)

Added `extract_record_frontmatter_canonical(text, frontmatter, rel_path, kind)` helper to `tools/build_retrieval_index.py` (after `extract_identifiers`); emits one row per `records/<family>/<id>.md` file with:
- `id_text`: frontmatter `id` field value (e.g., "S001").
- `id_kind`: derived from family via `RECORD_FAMILY_KIND_MAP` ({sessions: session, minorities: minority, engine-versions: engine-version, feedback: feedback}; unknown families fall back to `family.rstrip("s")`).
- `canonical`: same as `id_text`.
- `source_path`: relative path of records file.
- `line`: file-line of `id:` field (typically 2 per records-contract.md v1 §2.1 schema; precisely scanned).
- `context`: `f"id: {fm_id}"[:120]`.

`build_index` loop modified to call the helper after `extract_identifiers(body, rel)` and append the result if non-None.

**Rationale.** Without (β), the (i)+(b) ORDER BY changes are inert for migrated S001–S058 records (no rows in identifiers table to be ordered; resolution falls through to `records/sessions/index.md` rank 1, which beats specifications/ rank 2 — net improvement, but not the source-of-truth ranking that records-contract.md v1 §2.1 declares). With (β), all 59 migrated S<NNN> resolve to `records/sessions/S<NNN>.md:2` (the frontmatter `id:` line). End-to-end records-substrate-authority alignment achieved.

**Smoke-test verification (direct Python; full MCP-transport verification at S061 open per S054 D-186/D-187 precedent):**

Migrated S<NNN> identifiers (59-of-59 resolve to per-record source-of-truth):
```
S001 -> records/sessions/S001.md:2 (session)
S017 -> records/sessions/S017.md:2 (session)
S041 -> records/sessions/S041.md:2 (session)
S058 -> records/sessions/S058.md:2 (session)
S059 -> records/sessions/S059.md:2 (session)
[full S001-S059 spot-check: 59/59 resolve to records/sessions/S<NNN>.md]
```

Non-record-kind aliases (no regression):
```
D-198      -> specifications/workspace-structure.md:327 (decision)
D-001      -> specifications/multi-agent-deliberation.md:60 (decision)
OI-002     -> specifications/engine-manifest.md:88 (open-issue)
WX-58-1    -> records/sessions/S059.md:4 (watchpoint)  [unchanged; S059 body-text mention]
EF-055     -> records/sessions/index.md:69 (feedback)  [unchanged; not yet migrated to records/feedback/]
engine-v10 -> records/sessions/index.md:9 (engine-version)  [unchanged; not yet migrated]
```

Validator check 25 (records-substrate integrity per records-contract.md v1 §3): **PASS** (59 session records; index rows match; status enum clean; no orphans). The (β) extension does not break check 25 because check 25 inspects records/<family>/index.md vs records/<family>/<id>.md schema, not the identifiers table directly.

Index rebuilt: 560 documents (S060 directory + assessment + this decisions file pre-commit) / 60,252 identifiers (up from S059 close 559 / 59,729; +1 doc + ~523 new identifier rows including 59 new frontmatter-id rows from records/sessions/S001-S059.md).

**Alternatives considered (per D-129 standing discipline):**

At sub-option level (resolve_id ordering question per S059 close §8 honest-limit #4):
1. **(i) Minor implementation fix** — adopted (operator-ratified).
2. **(ii) Spec clarification** to records-contract.md v1 §2.1 — rejected: relabels discrepancy; doesn't fix operational behavior.
3. **(iii) Phase-2 gate amendment** to records-contract.md v1 §6 criterion #2 — rejected: weakens gate.

At scope-extension level (within (i)):
4. **(a) Stop after base (i)** — rejected after first smoke-test surfaced records/-vs-index.md violation of §2.1 authority discipline; operator ratified (b).
5. **(α) Stop after (i)+(b)** — rejected after second smoke-test surfaced indexer-side gap (frontmatter-only S001-S058 not indexed); operator ratified (β).
6. **(γ) Open new EF record for (β)** — rejected as more-disciplined-but-slower path; operator chose (β) within same Path L+A.

**Eleventh source-realignment-or-extension precedent chain instance** (S060 D-214 extends the chain S022 R8a / S030 D-100 / S033 D-108 / S040 D-123 / S046 D-143 / S051 D-178 / S052 D-181 / S054 D-186 / S054 D-187 / S059 D-207+D-210+D-211).

**Reversibility.** Both files are engine-adjacent (not engine-definition); revert via single git revert if a phase-2 case surfaces edge that the 4-tier ORDER BY OR `RECORD_FAMILY_KIND_MAP` doesn't anticipate. The frontmatter-id row insertion is additive — preserving the pre-fix records/-vs-specifications/ outcome would require additional changes beyond simple revert.

---

## D-215: Housekeeping consolidation

**Triggers met:** [none]

**Triggers rationale:** Consolidation of session-end status updates: minority-warrant observation-window advances; watchpoint cumulative state; engine-v preservation depth advance; close-rotation; D-129 / D-138 standing discipline; thirty-second-consecutive [none]-trigger pattern. No methodology-kernel edit; no specification edit; no MAD-required scope.

**Decision.** Record the following 15 sub-sections of routine status updates at S060 close:

### §a Engine-v10 preserved at S060 close

Preservation depth: **3** (S058 ratified + S059 preserved + S060 preserved). Engine-v10 trajectory at depth 3 is well within the engine-v7 11-session record (longest) and approaching engine-v9 8-session second-place mark. §5.4 cadence minority does NOT re-escalate per content-driven-bump precedent chain extended to S060 preservation (cadence concern separates from substantive-bump classification; S060 is non-bump session per engine-adjacent-only edits).

### §b Engine-feedback state preserved

`0 new / 3 triaged / 8 resolved / 0 rejected` unchanged from S059 close. Three triaged-deferred records remain (EF-047-brief-slot-template + EF-058-claude-md-drift + EF-058-tier-2-validation). No inbox transitions at S060.

### §c First-class minorities preserved unchanged

**40 first-class minorities preserved engine-wide** at S060 close — unchanged from S059. No new minority preserved; no minority discharged; no minority activated this session. Single-orchestrator Path L+A; no MAD; no dissent surface.

§10.4-M10 written-warrant clause (c) operator-surfacing channel exercised indirectly via the operator-audit halt pattern at three scope decisions; no formal activation of any §10.4-M-N minority at S060.

### §d Active OIs unchanged

**13 active OIs** at S060 close — unchanged from S059. No OI opened / resolved / amended this session.

### §e D-129 standing discipline fourteenth-consecutive clean exercise

Five considered-and-rejected non-Path-L+A alternatives in `00-assessment.md` §4 + D-213 above. §5.12 Path-Selection Defender reopen warrant (a) does NOT fire. Convention scales across fourteen heterogeneous session classes (S046–S060 inclusive default-agent + operator-surfaced + Path-AS-class).

### §f D-138 folder-name default fourteenth-consecutive clean exercise

`provenance/060-session/` no suffix, no slug. Convention stable.

### §g WX-28-1 thirtieth close-rotation zero retention-exceptions

S054 rotates OUT at S060 close (S054 was the Path T+L bundled-scope two-record-resolution session — EF-053 + EF-054 fixes; rotates to archive-surface-by-exclusion); S060 enters. Retention window post-rotation: **S055 / S056 / S057 / S058 / S059 / S060**.

### §h WX-24-1 MAD v4 thirty-third-session no-growth streak new record

`multi-agent-deliberation.md` v4 stable at 6,637 words. **18-session run from S042 reset** (S043–S060 all no-growth). Extends S059's 17-session record.

### §i WX-58-1 third observation 5-field recording at S060 close

Per `records-contract.md` v1 §6 phase-2 gate, the WX-58-1 5-field recording obligation applies to sessions S058 through S060 inclusive. **S060 third recording — see close §6 for full 5-field block**.

Phase-2 gate firing-disposition: interpretively settled by operator's selection of (i) at S060 (loose reading endorsed; substrate-fix retroactively aligns strict reading from S060 forward); literally unsettled at the strict-reading-at-S059-close anchor language. Carrying as honest-limit for S061+ adjudication. Recorded in close §3 + §8 below.

### §j WX-50-1 observation window remains closed

Per `retrieval-contract.md` v1 §6, the WX-50-1 3-field recording obligation applied to sessions S050 through S053 inclusive. S060 is post-window; no obligation. S060 exercised substrate substantively (3 forward_references + 1 resolve_id + 1 search via MCP tool transport at session-open + multiple invocations via direct Python during smoke-tests + 1 ensure_index rebuild post-spec-edits).

### §k WX-43-1 cumulative baseline unchanged

Cumulative baseline n=6-of-8 + explicit-instruction variant n=0-of-13 unchanged at S060 (no MAD invocation; baseline does not advance). OI-promotion discharged-as-not-warranted per S050 D-176.

### §l WX-44-1, WX-44-2, WX-47-1 codex-CLI watchpoints not exercised

Not exercised at S060 (no codex CLI invocation). Cumulative counts unchanged.

### §m Tenth source-realignment-or-extension precedent chain becomes eleventh

D-214 extends the precedent chain to **eleventh-instance**. Pattern is engine-conventional for spec-implementation alignment via single-orchestrator Path L (with optional +A Watch). The pattern accommodates heterogeneous defect classes: query-parser fixes (S054 D-186); tool extensions (S054 D-187); migration mechanics (S022/S030/S033/S040/S046/S051/S052); template-shape syncs (S059 D-210); records-substrate-authority alignment (**S060 D-214**).

### §n Tier-2-self-validation discipline observation

Per EF-058-tier-2-validation triage-deferred substantive-arc concern: this session honored the discipline at the path-selection level (operator-audit halt pattern at three scope decisions), but exercised single-orchestrator decision-making at the implementation level (specific SQL pattern; helper function shape; family-name mapping; line-number scan algorithm). The discipline-gap meta-pattern remains the substantive-arc concern for the future MAD; S060 is one data point.

### §o Aggregate default-read surface impact recorded in close §9

Forecast 22 files / ~78,500–79,500 words; actual to be recorded post-commit in close §9. Validator at close to be recorded.

### §p Thirty-second-consecutive housekeeping [none]-trigger pattern

D-215 extends pattern since D-126 Session 041. **Thirty-second-consecutive instance.** Engine-conventional. No action warranted.

---

## Decisions summary

- **D-213** Path L+A ratified mid-ratification per operator surface `[none]`.
- **D-214** (i)+(b)+(β) records-substrate-authority alignment adopted `[none]` (eleventh source-realignment-or-extension precedent chain instance; engine-v10 preserved).
- **D-215** Housekeeping consolidation `[none]` (15 sub-sections; thirty-second-consecutive [none]-trigger pattern).

Three decisions; all `[none]` triggers; single-orchestrator default-agent path; no MAD; engine-v10 preserved.
