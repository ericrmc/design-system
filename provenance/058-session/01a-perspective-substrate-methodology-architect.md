---
session: 058
title: Perspective — P1 Substrate-Methodology Architect (Session 058)
perspective: substrate-methodology-architect
perspective_family: claude
perspective_role: substrate-methodology-architect
date: 2026-04-25
status: immutable-at-commit
provenance_note: verbatim from Agent tool subagent (claude-opus-4-7); reasoned from briefs at 01-brief-shared.md + 01-brief-p1.md; Case Steward wrapped with frontmatter only (no body edits)
---

# P1 Substrate-Methodology Architect — Independent Response on EF-055

**Session 058 multi-agent deliberation, EF-055 substrate-aware format and archive rethink (substantive-arc)**

---

## 1. Frame Critique

The §2 frame names the right problem but, I think, names it one click too narrowly. EF-055 as written is about the *read-to-edit cost of accretive default-read files*. That is the symptom that surfaced. The deeper problem, which the design-space.md cost/benefit matrix reveals indirectly, is that **Selvedge's durable artefacts and Selvedge's reading surface are the same files**. We use markdown for two distinct functions — long-term provenance retention and per-session orientation/edit work — and the linear-growth cost is the price we pay for that conflation. The Substrate-N2 reframe and the engine-v9 retrieval substrate, taken together, suggest that those two functions can now be decoupled: structured records can be the durable thing; markdown projections can be the reading thing. EF-055 is the first session where that decoupling becomes a live design move rather than a future possibility.

A second reframe worth surfacing: the §2 framing implicitly treats SESSION-LOG.md as just another accretive block, but it isn't. SESSION-LOG.md is **the only strictly-linear-per-session file** in the default-read; the four spec §10 / §7 minority blocks grow only when minorities or engine-versions are produced, which is bursty and can plateau. SESSION-LOG.md grows every session, deterministically. That makes it the *driver* of the ceiling-pressure timeline (8K hard breach forecast at S059), and any direction that doesn't address it does not address the actual scheduling crisis. Direction B intuited this — it limits scope to SESSION-LOG.md alone — but mis-prices it as merely "tactical" when it's actually the highest-leverage intervention per word migrated.

A third reframe: the design-space.md matrix presents A vs. B vs. C as a single-axis trade between disruption and ambition. It under-represents **sequencing** as a free dimension. "Migrate SESSION-LOG.md first under the Substrate-N2 pattern, then expand if patterns hold" is a real design point that doesn't fit cleanly under A or B. The matrix's row "Forecloses other directions" already hints at this — Direction B does not foreclose A — but the matrix doesn't reward staged commitment. I will lean on this reframe in Q1 and Q7.

The question the deliberation is really answering: **"Is engine-v10 the right vehicle to convert Selvedge's accretive markdown surface into a structured-record substrate, and if so, what is the smallest credible phase-1 that proves the pattern without burning the workspace?"**

---

## 2. Q1 — Primary direction

**Recommendation: A+Alt3 (Substrate-N2 reframe combined with Substrate-N3 explicit-registries bridge), staged, with phase-1 scope = SESSION-LOG.md + workspace-structure.md §10.4 (the two highest-leverage migrations) and phase-2 = remaining accretive blocks. Engine-v10 candidate at phase-1 ratification.**

Cross-axis reasoning per §2.4:

- **Read-to-edit cost reduction (high for A, A+Alt3)**: Migrating SESSION-LOG.md and §10.4 alone removes ~8,640 words from per-session edit surface (SESSION-LOG.md 7,390 + §10.4 ~1,248). That recovers headroom faster than any other intervention. Direction B captures only the SESSION-LOG portion.
- **Substrate-fit (high for A+Alt3)**: The engine-v9 substrate is now operationally exercised across 7 sessions; S055/S056/S057 organic-use empirically demonstrated `forward_references` + `resolve_id` provide cross-reference navigation that previously required prose-scan reading. This is exactly the maturity precondition that S050 P3 named as missing ("too disruptive for S050 adoption"). It is no longer missing.
- **Engineering load (high for pure A; very high for full A+Alt3)**: This is the axis I strain most. Pure Direction A across all six accretive blocks plus full Substrate-N3 registries is genuinely a 3-6 session arc with non-trivial validator/tool work. **My recommendation only stays viable under aggressive phase-1 scope discipline** (two blocks, not six). I will be explicit in Q2 that I am buying ambition by buying staging.
- **Reversibility (low for A; medium under staged A+Alt3)**: Per-record-file directories cannot be cleanly rolled back if we discover the pattern is wrong, but if we stage and only migrate SESSION-LOG.md + §10.4 in phase-1, the rollback surface is bounded. We learn whether the pattern works before committing the larger spec-§10 blocks.
- **Substrate-availability assumption**: I take the open-issue-1 risk seriously. A+Alt3 specifically addresses it: explicit registries (`identifiers.jsonl`, `edges.jsonl`, etc. per S050 P3 Substrate-N3) give us a substrate-independent fallback. Pure Direction A relies on Phase-1 retrieval substrate; combining with Alt3 hedges that dependency.
- **Operator-stated-preference fit (yes)**: Direction A is operator-preferred at intake. Per Q8, this is durable input not foreclosure. My recommendation lands on a substantial variant (A+Alt3 staged) — it preserves the operator's substantive thrust (Substrate-N2 reframe + engine-v10 candidate) while taking the structural-fact-corpus point seriously.
- **§10.4-M10 activation (yes substantive)**: This activates §10.4-M10's maintenance-cost or multi-hop-dominance written warrants implicitly, since SESSION-LOG soft-warning third-consecutive close is the empirical maintenance-cost signal even without formal counter to projection. We are not waiting for warrant-fire because *we are now within the warrant fire timeline* (S058-S059).

**Why not Direction B alone**: B captures SESSION-LOG only, but the §10 minority blocks together are already 3,561 words across four specs and continue to grow per-minority. Doing B alone defers the §10 question to a future MAD that will face the same engineering load *plus another year of accretion*.

**Why not Direction C**: C accepts the structural-friction compounding for another 2-5 sessions. SESSION-LOG.md hard-ceiling breach is forecast at S059. C's "wait for written warrants" gate is being met by the warrants themselves; deferring is now a more expensive option than acting.

**Why not Alt1 / Alt2 alone**: Alt1 (per-block archive rotation) is a periodic-restructure escalation — it just buys more periods, not a different shape. Alt2 (hybrid partial) under-commits to the substrate point.

**Why not pure Substrate-N3 (Alt3 alone)**: It is "low" on read-to-edit cost reduction in the matrix because registries don't change the markdown surface. It builds substrate but doesn't harvest the savings.

**Why A+Alt3 over pure A**: Pure A bets the workspace on substrate availability. A+Alt3 produces the same read-surface savings while also producing the structured-fact corpus that is substrate-independent and gives engine-v11+ a different evolution path.

---

## 3. Q2-Q8 — Secondary questions

### Q2 — Adoption scope

**Phase-1 (S058 MAD adoption + first migration)**: SESSION-LOG.md migration to `provenance/sessions/S<NNN>.md` per-session files, plus workspace-structure.md §10.4 migration to `specifications/minorities/M-NNN.md` per-record files. Both get thin index-row replacements in their original files. Engine-v10 ratified. **Phase-2 (next dedicated MAD or single-orchestrator session)**: remaining three spec-§10/§7 blocks (`reference-validation.md` §10, `retrieval-contract.md` §7, `engine-manifest.md` §7) migrate using the proven phase-1 pattern. **Phase-3 (opportunistic)**: `engine-feedback/INDEX.md` migration if pattern holds; explicit registries (`identifiers.jsonl`, `edges.jsonl`, etc.) added if S050 P3 Substrate-N3 still seems valuable.

**Migration sequence rationale**: SESSION-LOG.md first because it is the ceiling-pressure driver and the per-session pattern is structurally simpler than per-minority (sessions have a single canonical key; minorities have spec-and-number composite keys). §10.4 second because it is the smallest spec-block and proves the cross-spec pattern. The remaining spec-§10 blocks share the §10.4 pattern, so their phase-2 migration becomes mechanical. Engine-manifest.md §7 last because per-version files (open question 4) interact with versioning discipline and deserve dedicated attention.

### Q3 — Per-record-file directory structure

**Directory placement**: `specifications/minorities/` for cross-spec minorities (M7-M11 currently mirrored across workspace-structure.md §10.4 and retrieval-contract.md §7); spec-local for spec-internal minorities (e.g., reference-validation.md-only minorities go in `specifications/reference-validation/minorities/`). **Naming**: `M-NNN.md` for cross-spec, `<spec>-M-NNN.md` for spec-local. The cross-spec naming means M-007 through M-011 get one canonical file each, dissolving the §10.4-vs-§7 mirroring problem (open question 3).

**File-class classification**: New file-class needed in `workspace-structure.md` §file-class enumeration: "engine-definition-record" — derives from engine-definition spec (governing definition unchanged), but is itself an immutable per-record artefact post-creation. D-017 immutability applies: once a session closes a minority, that minority's file is closed. Re-discharge or re-vindication appends a status entry rather than rewrites prior status (per open question 2 — append, not overwrite).

### Q4 — Index format

**Pattern**: open-issues/index.md is the model exemplar. Index file = thin table with columns `[ID | Title | Status | Path | Anchor session]`. Status column convention: `preserved | discharged | re-vindicated | superseded`. Path-pointer convention: relative path from index file to record file (`./minorities/M-008.md` from workspace-structure.md, `../specifications/minorities/M-008.md` from retrieval-contract.md). One-line status per row, no embedded prose.

**Difference from open-issues exemplar**: open-issues/index.md has no `Anchor session` column; minorities need one because the session-of-creation is identity-defining for §10.4-M-NNN provenance. Otherwise structurally identical.

### Q5 — Validator + tool updates

**New check 25**: per-record-file integrity — for each row in an index file, verify the path resolves to an existing file; verify the file's frontmatter `id` matches the row ID; verify status field consistency. **Build-retrieval-index.py rule changes**: index ingestion needs to follow path pointers and ingest record-file content as well as index rows; this is a one-line change to the index walker if record files live under `specifications/minorities/` (already inside the indexed tree) but a more substantive change if some live in spec-local subdirectories.

**Testing strategy**: phase-1 migration of SESSION-LOG.md + §10.4 produces ~57 record files (56 sessions + ~11 minorities). Validator check 25 must pass on this corpus before phase-1 ratification closes. Add a synthetic broken-row fixture to `tools/test_validate.sh` to confirm check 25 detects path-mismatch and frontmatter-mismatch failures.

### Q6 — Cross-spec interactions

**Phase-1 essential** (4 specs touched at minimum): `workspace-structure.md` v6→v7 (file-class extension; §10.4 reshape; per-record-file immutability discipline addition); `read-contract.md` v5→v6 (§1 default-read enumeration explicitly excludes per-record files unless invoked; §2c retention-window value updated since substrate makes "older closes" still queryable through resolve_id); `engine-manifest.md` (§5 versioning trigger updated; engine-v10 entry added; §7 reshape *deferred* to phase-2 to keep phase-1 scope bounded); `retrieval-contract.md` v1→v2 (§7 thin-index-row pattern adopted for the M-NNN cross-references it mirrors).

**Phase-2 deferrable**: `reference-validation.md` v3→v4 §10 reshape; `retrieval-contract.md` §10.4 mirroring discipline question full resolution (phase-1 takes the simplest interpretation: M-NNN cross-spec files exist once; both index files point to the same file); `tools/validate.sh` check 25 (added phase-1, but its scope expands phase-2 to cover the additional migrated blocks); `tools/build_retrieval_index.py` rule changes are *minimal* phase-1 (record files already inside indexed tree) and may need rule additions phase-2 if spec-local subdirectories are introduced.

### Q7 — Multi-session arc shape

**3 sessions**: S058 = MAD adoption + phase-1 spec edits + first migration (engine-v10 ratified at S058). S059 = phase-2 migration of remaining §10/§7 blocks (single-orchestrator if pattern is clean; MAD if novel issues surface). S060 = phase-3 opportunistic registries + engine-feedback INDEX migration + soak observation. **Clean phase-boundaries**: Phase-1 → Phase-2 boundary is "phase-1 migration committed; validator green; one session of soak with no regressions; pattern judged transferable to remaining blocks." Phase-2 → Phase-3 is "all spec §10/§7 blocks migrated; aggregate default-read word count reduced ≥40%." Phase-3 has no fixed boundary — it is opportunistic and may not happen if pattern proves unnecessary.

**Why not 2 sessions**: phase-3 in the same session as phase-1 risks under-soaking the pattern; the workspace would commit to engine-v10 plus all migrations before any organic use exposes pattern problems. **Why not 4+ sessions**: opportunity cost; ceiling pressure on SESSION-LOG.md is real and the longer phase-1 takes to land, the more migration cost we pay.

### Q8 — Operator-stated preference treatment

**Durable input, not foreclosure** — the S048 D-153 `operator_directed_resolution` short-circuit explicitly does not apply (no such frontmatter field on EF-055 intake; S056 D-192 confirmed this). The S048 D-155 / S049 D-159 / S050 D-172 substantive-arc deliberation pattern does apply: triage authorises deliberation; deliberation evaluates on merits; operator preference enters as one position among others but with weight as a signal of operator-perceived workspace state.

**How it shapes my evaluation**: I take operator preference as evidence that the operator is seeing the structural-friction signal directly, which raises my prior on the ceiling-pressure timeline being real. I do not score Direction A higher on any matrix axis because of operator preference — Direction A's high read-to-edit cost reduction is an axis-evaluation, not a deference move. The recommendation A+Alt3 staged is the position I reach on technical merits; it happens to align substantially with operator preference because the operator's structural-friction read is correct.

**Resistance check**: if operator preference were for Direction C (defer), I would still recommend A+Alt3 staged based on the §59 ceiling-pressure forecast and §10.4-M10 written-warrant approach. The recommendation is invariant under operator-preference flip.

---

## 4. Open questions I address

### Open question 1 — Substrate-availability fallback

**Address**: yes, fallback discoverability is essential and is exactly what A+Alt3 buys. Phase-1 must produce a `provenance/sessions/index.md` and `specifications/minorities/index.md` aggregate-index file readable without substrate. The thin-row pattern already provides this: the index file *is* the substrate-independent fallback. If `tools/build_retrieval_index.py` fails or substrate is unavailable, the operator can `cat index.md` and follow path pointers. This must be made explicit in `read-contract.md` v6 §2c retention-window discussion.

### Open question 2 — Per-record-file immutability

**Address**: append, not overwrite. D-017 immutability applies to provenance once a session closes. If minority M-008 is preserved at S050, re-tested at S054, and re-vindicated at S058, the file `M-008.md` accumulates three frontmatter status entries chronologically: `[preserved S050; tested S054; re-vindicated S058]`. Index-file status column reflects the latest entry. Per-record file becomes a thin provenance trail. This is consistent with how the engine treats other immutable artefacts (session-close decision records, deliberation provenance) and avoids losing dissent across re-discharge cycles.

### Open question 3 — Multi-spec mirrored minorities

**Address**: one canonical file per minority. M-007 through M-011 are cross-spec minorities that currently exist as duplicated content in workspace-structure.md §10.4 *and* retrieval-contract.md §7. Under per-record-file pattern, they collapse to one canonical `specifications/minorities/M-NNN.md` file; both spec index rows point to it. This dissolves the mirroring discipline question entirely (it stops being a question). Spec-local minorities (none cross-spec) get spec-local subdirectories. This is one of the phase-1 wins and should be called out in the engine-v10 manifest as a uniformity-discipline gain.

### Open question 5 — Migration ordering

**Address**: SESSION-LOG.md first per Q2 reasoning. The per-session pattern is the structurally simplest of the migration classes (one canonical key per record), so it surfaces validator/tool issues earliest while being the highest-leverage migration per word. §10.4 second, in same phase, because it proves the cross-spec pattern needed for phase-2.

### Open question 6 — Archive-pack discipline

**Address**: each phase produces one aggregate archive-pack, not one per migrated block. Phase-1 archive-pack contains the pre-migration state of SESSION-LOG.md and workspace-structure.md §10.4 in their original form, plus a manifest mapping rows-in-original-file to record-files-after-migration. Aggregate retention rule: archive-packs from substantive migrations are retained per S022 R8a / S040 D-123 / S051 D-178 precedent (no automatic expiry). This is ~one archive-pack per multi-session arc, not one per session, which keeps archive-pack count bounded.

---

## 5. Anti-laundering self-check

**Criteria I strained to make this work**:

The biggest strain is **engineering load**. Pure Direction A's matrix entry is "high"; A+Alt3 is "very high." My recommendation only becomes credible by aggressively trimming phase-1 scope to two blocks (SESSION-LOG.md + §10.4). If I had included all six accretive blocks in phase-1, the engineering-load axis would dominate and the recommendation would not survive. **I am buying ambition by buying staging**, and that staging discipline is fragile — if the deliberation expands phase-1 scope to "do all blocks now," the recommendation breaks.

The second strain is **reversibility**. I marked it "medium under staged A+Alt3" but the matrix shows it as "low" for full A. If phase-1 lands and the per-record-file pattern proves wrong (e.g., per-record file frontmatter discipline is too costly to maintain), unwinding is non-trivial. I have no concrete unwinding plan beyond "archive-pack restoration" — that is genuinely a weakness.

The third strain is **the substrate-availability assumption**. A+Alt3 is specifically intended to hedge this, but Substrate-N3 explicit registries are themselves engineering load — the hedge has its own cost.

**What would falsify my position**:
- If S058 close measures phase-1 migration cost at >2× the Path AS Shape-1 design-space.md projection (which is the §10.4-M10 written warrant (a) trigger inverted), the staged-A+Alt3 recommendation is wrong and Direction B (SESSION-LOG only, no engine-v bump) becomes the right answer in retrospect.
- If post-phase-1 organic use shows operators reading per-record files directly more often than aggregate-index files (inverse of substrate-fit assumption), the pattern is wrong.
- If validator check 25 proves expensive to maintain across the per-record-file corpus (high false-positive rate), the immutability discipline I propose for open question 2 is too costly and a different file-class is needed.
- If the operator-stated preference for Direction A turns out to be reading a different signal than ceiling pressure (e.g., aesthetic preference for structured records absent the structural-friction concern), my matrix-evaluation premise that "operator preference is structural-friction signal" is mis-grounded.

**What I did NOT strain**: I did not score Direction A's substrate-fit lower to make B more competitive. The substrate maturity is genuinely high after 7 sessions of engine-v9 and 3 sessions of organic substrate use. I did not inflate Direction C's opportunity cost; ceiling pressure is forecast-grade not assertion-grade.

End of P1 response.
