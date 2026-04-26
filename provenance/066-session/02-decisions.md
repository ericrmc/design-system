---
session: 066
title: Decisions — Path L per operator surface; engine-manifest §7 v1-v11 archive-packed; thin per-version index + current-version entry inline retained; OI-002 minor classification; engine-v12 preserved
date: 2026-04-26
status: complete
---

# Decisions — Session 066

## D-240: Path L per operator-surfaced priority directive

**Triggers met:** [none]

**Triggers rationale:** Operator-surfaced path-determination at session-mid; not a multi-perspective deliberative decision per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required. Single-orchestrator implementation of pre-ratified forward direction (chain S063 §2 finding 17 + S064 §8 honest-limit 4 + S065 §8 honest-limit 3 all forward-recommended restructure). Per OI-002 substantive-vs-minor heuristic, the restructure is minor-class (see D-241 below); per S048 D-154 EF-001 operator-directed-resolution precedent, a single-orchestrator implementation of a pre-ratified narrow-scope direction is appropriate.

**Single-agent reason:** Single-perspective; non-load-bearing implementation of pre-ratified forward direction per chain S063+S064+S065. The substantive deliberation was the cumulative forward-recommendation across three closes; S066 is the implementation surface.

**Decision:** Path L (single-orchestrator structural restructure of `specifications/engine-manifest.md`) is the path for Session 066, ratified per operator-surfaced priority directive ("As 'Engine-manifest exceeds the read limit' this session should prioritise remediation, if nothing else is a priority, Path A Watch is not recommended.").

**Rationale:** Concrete operational evidence: at S066 open the agent attempted to Read `specifications/engine-manifest.md` and received a content-too-large error from the Read tool (file at 7,887 words ≈ 26,081 tokens; over the 25K-token Read-tool ceiling). The (z12) 5-condition test was all-clear at S066 open (recorded in 00-assessment §3a); Path A would have been (z12)-justifiable. Operator-surface explicitly inverted the recommendation per the operator-surfacing channel + §10.4-M10 written-warrant clause (c) + S036/S057/S060/S061/S063/S064 cumulative precedent chain; cumulative count advances n=6 → n=7 (S066).

**Alternatives surfaced and rejected** (D-129 standing discipline twentieth-consecutive clean exercise):

1. **Path A (Watch)** — explicitly rejected by operator-surface; (z12) all-clear notwithstanding.
2. **Path L (workspace-structure restructure)** — workspace-structure 6,606 words is over 6K soft but well under 8K hard and well under Read-tool 25K-token limit; not blocking; defer.
3. **Path T (EF-059 triage)** — activation precondition (b) WX-62-1 closure not satisfied at S066 (window stays at 2-of-3 since S066 is non-triggered per Layer 2 trigger evaluation); defer.
4. **Path PD (EF-058-claude-md-drift substantive class arc kickoff)** — triaged-deferred; no operator surfacing for this scope; defer.
5. **Path-AS Shape-1 (synthesis for restructure shape)** — forward direction has been pre-ratified across three closes (archive-pack OR separate-history-file); operator-surface also did not request synthesis; single-orchestrator implementation of pre-ratified direction is appropriate scope per S048 D-154 EF-001 precedent.
6. **Path L+R (refactor check 27 heuristic per S065 honest-limit 11)** — S065 forward-direction was "at next triggered close: refine check 27 heuristic OR codify periphrastic-form discipline as Path A close-narrative convention"; S066 is not the next triggered close and the heuristic refinement is not the operator's surfaced priority; defer.

## D-241: §7 historical entries archive-packed; thin per-version index + current-version entry inline retained; OI-002 minor; engine-v12 preserved

**Triggers met:** [none]

**Triggers rationale:** Per OI-002 substantive-vs-minor heuristic, the restructure is **minor**: content-preserving structural restructure via existing archive-pack discipline per `read-contract.md` v6 §4-§7; no new normative content in `engine-manifest.md` §1-§6; no semantic change to engine-version declarations; no new rules / required fields / triggers / severity / gating / required artefacts. Analogous classifications: S040 D-123 SESSION-LOG.md preemptive restructure (classified minor) + S022 R8c retroactive archive-pack precedent (operational, not engine-spec revision). Per `engine-manifest.md` §5 versioning discipline, no engine-version increment for "minor elaborations within an existing spec's scope." The current engine-version (the twelfth) is preserved.

**Single-agent reason:** Single-orchestrator implementation per D-240 above.

**Decision:** Adopted the following restructure of `specifications/engine-manifest.md`:

(a) Created archive-pack `provenance/066-session/archive/pre-restructure-engine-manifest-history/` per `read-contract.md` v6 §4 archive-pack structure + §5 manifest schema + §7 integrity guarantee:
  - `00-source.md`: byte-identical extract of pre-S066 `specifications/engine-manifest.md` lines 129-275 (the eleven historical engine-version §7 entries v1 through v11 inclusive); 5,816 words; 50,126 bytes; 147 lines.
  - `manifest.yaml`: per §5 schema; `chunk_boundary_rule: single-file`; `kind: other-named` (active-spec section relocated for read-tool-ceiling remediation); `source_hash_sha256: 043c00405dfe337d5e75114957d6eb84e74ca5f32810546b4ec5eb6943779e2d`; `originating_session: 17` (engine-manifest origin); `migrated_in_session: 66`; readers_note explains the migration trigger and the preservation discipline.

(b) Edited `specifications/engine-manifest.md` §7:
  - Replaced the eleven historical entries (lines 129-275 pre-S066) with: a transition paragraph + thin per-version index table (one row per historical version with Established/Decision/Class columns + archive-pack pointer per `read-contract.md` v6 §6 reference convention).
  - Preserved the current engine-version §7 entry (lines 276-304 pre-S066) inline below the thin index.
  - Preserved §Validation section unchanged.
  - Updated frontmatter: `last-updated: 2026-04-26` + `updated-by-session: 066`.
  - Post-edit file: 2,319 words / 188 lines / ~7K tokens estimated. Cleared 6K soft warning. Cleared 25K-token Read-tool ceiling.

(c) Engine-version disposition: **the twelfth engine version is preserved** at S066 close. Preservation depth advances 1 → 2. No engine-version increment per `engine-manifest.md` §5 minor-elaboration exclusion + OI-002 minor-classification per heuristic + content-preserving structural-restructure precedent chain (S040 D-123 + S022 R8c).

**Rationale:** The restructure preserves all content verbatim per archive-pack discipline (`read-contract.md` v6 §4 chunk-boundary mechanical rule + §7 integrity guarantee + check 21 hash verification). The eleven historical entries remain accessible by the standard `[archive: path]` reference convention per `read-contract.md` v6 §6; check 22 (archive-pack citation consistency) verifies the new reference resolves. Aggregate default-read surface budget recovers 5,475 words headroom from S065 close 87,310 / 90K (2,690 headroom) to S066 close ~81,000-82,000 / 90K (8,000-9,000 headroom). Per-file budget for the canonical engine-manifest path clears the 6K soft warning. The Read-tool 25K-token ceiling is cleared with substantial margin.

**Engine-v12 entry retention rationale**: keeping the current-version entry inline below the thin index preserves the engine-conventional discoverability pattern where the "current state" is immediately readable without consulting the archive-pack. Future engine-version entries will land inline as they are ratified; if/when a future session ratifies a subsequent engine-version that pushes engine-manifest past the 6K soft warning again, the next restructure should follow the same pattern (rotate the now-historical engine-v12 entry into the archive-pack at that future session).

**Alternatives surfaced and rejected**:
1. **Move §7 to a separate file** (e.g., `specifications/engine-manifest-history.md` as engine-adjacent or as new default-read file) — rejected: introduces a new file that requires either default-read inclusion (does not solve aggregate-budget pressure) OR engine-adjacent classification (changes file-class semantics + introduces ambiguity about whether the history is part of the engine definition). Archive-pack is the engine-conventional pattern for this case and does not require new file-class semantics.
2. **Compress all entries to a more concise format** — rejected: information loss; archive-pack discipline forbids summarisation per `read-contract.md` v6 §3 archive-surface preservation discipline.
3. **Multi-chunk archive-pack** — rejected: 5,816 words fits well under the per-chunk 6K word target per `read-contract.md` v6 §4; single-chunk single-file form is simpler.
4. **Archive-pack v1 through v6 only** (keeping v7-v12 inline as "recent" history) — rejected: would leave engine-manifest at ~5,500 words still over Read-tool ceiling at next engine-version increment; archiving v1-v11 (everything except current) is the cleanly defensible boundary that future restructures can follow as a pattern.

## D-242: housekeeping (S066 close)

**Triggers met:** [none]

**Triggers rationale:** Routine housekeeping per S041+ standing convention; no decision-level change to specifications, OIs, or warrants; cumulative-counter and watchpoint-status sub-sections fold into one decision per S041 D-126 + 41-session standing convention.

**Single-agent reason:** Routine non-substantive bookkeeping per standing convention; no perspectives required.

**Decision:** Housekeeping recorded for S066 close (15 sub-sections a-o; **thirty-eighth-consecutive housekeeping `[none]`-trigger pattern**):

a. **D-129 standing discipline twentieth-consecutive clean exercise** (six non-Path-L alternatives surfaced and rejected at D-240; §5.12 Path-Selection Defender reopen warrant (a) does not fire).
b. **D-138 folder-name default twentieth-consecutive clean exercise** (`provenance/066-session/`).
c. **WX-28-1 thirty-sixth close-rotation zero retention-exceptions**. S060 rotates OUT (S060 was the Path L+A reshape-mid-ratification session per S060 D-213); S066 enters. Retention window post-rotation: S061 / S062 / S063 / S064 / S065 / S066.
d. **WX-24-1 MAD v4 thirty-ninth-session no-growth streak new record** (24-session run from S042 reset; extends S065's 23-session record). MAD v4 last edited at engine-v2 S021; remains unchanged at the twelfth-engine-version boundary.
e. **WX-43-1 explicit-instruction variant cumulative tracking** unchanged at n=0-of-17 (no MAD-perspective Agent invocations at S066 single-orchestrator session).
f. **WX-44-1 + WX-44-2 + WX-47-1** codex-CLI watchpoints not exercised at S066 (no codex-CLI invocation). Cumulative counts unchanged.
g. **WX-50-1 + WX-58-1**: closed; no obligations at S066.
h. **WX-62-1 stays at 2-of-3** at S066 close per Layer 6.3 explicit clause + S063 close §7 explicit clause: third recording at next triggered close. S066 5-field block recorded in close §6 with `reviewer_invoked: no-not-triggered` per the explicit clause for non-triggered sessions during mid-window. **First-of-record second-consecutive-non-triggered-close-during-WX-62-1-mid-window event.**
i. **§5.6 GPT-family-concentration window-ii observation NOT advanced at S066** (no MAD; no cross-family reviewer; window-ii cumulative count unchanged at seven-consecutive at S064 close).
j. **§10.4-M10 written-warrant clause (c) operator-surfacing channel exercised at S066** via mid-session priority directive. Cumulative count advances n=6 → **n=7** (S036/S057/S060/S061/S063/S064/S066).
k. **§10.4-M25 P2 cadence-depth concern observation at S066**: the twelfth engine version's preservation depth advances 1 → 2 (forward-discipline observed; cadence concern not re-firing at S066).
l. **VD-001 (z5) ledger row remains `status: resolved`** with closure rationale at S064. **VD-002 (z5) ledger row remains `status: open`** with `review_by_session: S067`. No lifecycle event at S066. Layer 2 trigger (d) does not fire.
m. **engine-feedback inbox state unchanged** at S066 close: 1 new (EF-059) / 2 triaged / 9 resolved / 0 rejected. EF-059 carries `triage_scheduled` per S062 D-225 activation precondition (b) "≥3 sessions per WX-62-1 observation window"; at S066 close window is still 2-of-3 (not yet satisfied); triage continues to defer to S067+.
n. **13 active OIs unchanged** at S066 close. No OI opened, resolved, or amended at S066.
o. **50 first-class minorities preserved engine-wide** at S066 close (unchanged from S065 close; cross-references at `specifications/workspace-structure.md` v9 §10.4-M1 through M25 + cross-spec mirrors at `specifications/validation-approach.md` v7 §10 / `specifications/retrieval-contract.md` v1 §7 / `specifications/records-contract.md` v1 §7 / `specifications/reference-validation.md` v3 §10). No new minorities at S066 (no MAD; no contested deliberation per Path L scope).
