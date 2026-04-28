---
title: Read Contract
version: 4
status: active
created: 2026-04-22
last-updated: 2026-04-23
updated-by-session: 036
supersedes: read-contract-v3.md
---

# Read Contract

## Purpose

This specification defines the **access discipline** governing what the methodology reads in full at every session open versus what it preserves verbatim and accesses by explicit reference. It repairs a divergence observed at Session 022 between the methodology's normative read obligation (`methodology-kernel.md` §1 Read: "every file, every specification, every provenance record") and the operational read mechanism (paginated `Read --offset`, targeted `Grep`, harness-layer routing around oversized files).

The access discipline is a dimension separate from — and cutting across — the existing file-class ontology in `workspace-structure.md` (engine-definition / development-provenance / application-scope). A file may be engine-definition AND default-read (an active specification); development-provenance AND archive surface (a historical raw perspective).

Created Session 022 per D-084 as the resolution of the workspace-scaling trajectory. The read-contract articulates an engine-v3 repair of what Session 022 diagnosed as an OI-015 laundering pattern materialised at the harness layer.

This specification applies equally to the self-development application and to external-problem applications of the Selvedge engine. Its default-read and archive enumerations are engine-definition content; external-application workspaces inherit them at engine-v3.

## Specification

### 1. Default-read surface

The default-read surface is the bounded set of files read in full at every session open. Every session's Read activity must read every file enumerated below in full before any substantive work proceeds.

**The default-read surface enumeration at engine-v4 (of this spec; engine-v7 of the manifest):**

0. (Added v4) `MODE.md` at workspace root — the workspace-identity marker declaring `mode: self-development | external-problem`. See `specifications/workspace-structure.md` §MODE.md for schema. Required in workspace-identity file class per `workspace-structure.md` v5.
1. Every active-status `.md` file in `specifications/`. "Active-status" means frontmatter `status: active`. Superseded-status files (`*-v1.md`, `*-v2.md`, etc., carrying `status: superseded`) are archive surface by exclusion (§3).
2. `PROMPT.md` (top-level dispatcher).
3. `prompts/development.md` (self-development executable prompt).
4. `prompts/application.md` (external-application executable prompt).
5. `SESSION-LOG.md` (thin one-line-per-session index; full per-session detail lives in `03-close.md`).
6. `open-issues/index.md` (thin overview; full per-OI detail lives in `open-issues/OI-NNN.md` files).
7. The `03-close.md` file of each of the **most recent 6 session closes** (where "session" is determined by the numeric prefix on `provenance/NNN-title/` directories, sorted descending, top 6). Older closes are archive surface by exclusion (§3); they remain at their original `provenance/NNN-title/03-close.md` paths preserved verbatim but are not loaded by default. The 6-session retention window was adopted Session 028 per D-096 (supersedes v2's "every `03-close.md`" rule). See §2c close-rotation rule for mechanics.
8. Every file in the currently-active session's provenance directory (`provenance/NNN-title/` where NNN is the current session). While the session is open, current-session provenance is default-read; on close, it becomes archive surface by exclusion (§3) unless it is a `03-close.md` that falls within the §7 retention window (which stays default-read by §7 above).
9. (Added v4, conditional) `engine-feedback/INDEX.md` when the file exists AND the workspace is in self-development mode per `MODE.md`. In external-problem mode, `engine-feedback/` is outbox-role and `INDEX.md` (if present) is not default-read by this rule. In the absence of the file, this item does not contribute to the default-read surface.

The enumeration is closed. A file not enumerated here is archive surface by §3.

**Retention-exception (added v3, Session 028).** A session may record a **retention-exception decision** to keep a specific close older than the 6-session window in default-read, when that close carries load-bearing content for currently-active governance (e.g., a minority activation warrant text, a cross-referenced decision rationale). The retention-exception is recorded in the session's `02-decisions.md` with the explicit close path and the load-bearing-purpose rationale. Retention-exceptions are cumulative and lifted when the load-bearing purpose ends; the lifting is also recorded in a decision record.

### 2. Default-read budget

Per-file constraints:

- **Hard ceiling: 8,000 words.** Any file in the §1 enumeration exceeding 8,000 words of body content (frontmatter excluded) is a validation failure at `tools/validate.sh` check 20. The session that produces such a file must either reduce it or restructure it (e.g., split into multiple files each under the ceiling; relocate detail to archive surface with reference from the default-read file).
- **Soft warning: 6,000 words.** Any file in the §1 enumeration between 6,000 and 8,000 words triggers a validator warning (not a failure). The warning is signal that the file is approaching the ceiling; the next session should consider restructuring. The 6,000-word value is ~75% of the 8,000-word hard ceiling; this ratio is the design principle for future revisions (the validator constants are named integers per `tools/validate.sh`; the ratio lives here as the design guide).

Measurement: word count via `wc -w` on body content after the closing YAML frontmatter delimiter. The word-count metric is chosen for stability across tokenisers (per Session 022 Outsider [01d-Q6] + Conservator [01b-Q6] convergence).

**Rationale for the chosen values (revised Session 023).** The current single-Read-tool ceiling at the time of adoption is approximately 25,000 tokens. Empirical measurement of workspace prose-with-markdown files at Session 022 (SESSION-LOG 10,405 words → 33,227 tokens; open-issues 9,783 words → 27,437 tokens) shows a tokens-per-word ratio of approximately 3.0×, not the 1.3× that the v1 Rationale used. At the corrected ratio, 8,000 words is approximately 24,000 tokens — narrowly within the single-Read ceiling, aligned with the reader-contract intent that default-read means "read in full at every session open." The 6,000-word soft warning is approximately 18,000 tokens, well within single-Read, providing early signal before files approach the ceiling.

The v1 Rationale's 15,000-word hard ceiling (≈ 45,000 tokens, ~1.8× the single-Read ceiling) was set under an empirically wrong calibration. The v1 values produced a ceiling that routinely required paginated reading at files near the ceiling — misaligned with default-read's own purpose. Session 022's Honest Notes flagged this error; Session 023 corrected the values per D-086.

**Known consequence at v2 adoption.** `specifications/multi-agent-deliberation.md` at 6,403 words exceeds the new 6,000-word soft warning at v2 adoption. This is the designed function of the soft warning: to prompt restructure when a file approaches the ceiling. Session 024+ remediation options per §8 below.

**Minority positions preserved (Session 023 D-086 R10 §5):**

- **§5.1 Pacer 10K/7.5K minority** (Session 023 [01b-Q1, Q2]). Position: 10,000-word hard ceiling with 7.5K soft warning preserves calibration-corrective discipline while leaving growth headroom. Activation warrant: if the adopted 8K/6K budget produces three or more restructure-for-budget events in the next 5 sessions (restructures prompted by budget rather than by content completion), revisit upward toward 10K/7.5K. Alternatively, if 8K binds on `multi-agent-deliberation.md` or `reference-validation.md` in a way that forces content-coherence-damaging split, this position becomes preferred revision direction.

- **§5.2 Skeptic no-change + warrant-literalism minority** (Session 023 [01c-Q1]). Position: the v1 Outsider-§5.3 activation warrant had not literally fired; revising values one session into a five-session grace window subverts the spec's own governance mechanism for self-revision. Vindication warrant: if within 5 sessions of Session 022 adoption (i.e., by Session 027) no default-read file exceeds 7,500 words and no restructure-for-budget event occurs, the Skeptic no-change position is vindicated retroactively — Session 023's revision was premature.

- **§5.3 Pacer aggregate-hard-budget minority** (Session 023 [01b-Q3]). Position: adopt aggregate default-read surface hard budget at 90K hard / 80K soft now; naming a budget creates the forcing function that watchpoint-only reporting lacks. Activation warrant: if aggregate exceeds 100,000 words OR grows >10% in a single session without compensating restructure, this position becomes preferred revision direction.

- **§5.5 tokeniser-drift watch minority** (Session 023 [01a-Honest Limits, 01d-Honest Limits]). Position: the 3.0× tokens-per-word ratio used in the revised Rationale is measured on two files only; applicability across file-types is not empirically verified. Activation warrant: if any single-Read attempt on a default-read file fails due to token-budget-exceeded despite the file being under the 8K word ceiling, re-measure the tokens-per-word ratio across a sample of default-read files and re-calibrate.

### 2a. Aggregate default-read surface sensor layer (v2; revised v3)

`tools/validate.sh` check 20 reports the aggregate word count across all default-read surface files in every Tier 1 run. At engine-v5 (Session 028 adoption of v3), this sensor layer is **supplemented by the §2b aggregate hard budget** (enforcement layer). The sensor layer is informational; the budget layer is pass/fail/warn. Both use the same numerical thresholds by design per D-096 Session 028 (avoids "moving the trigger after it fired" per Outsider `[01d, Q2]`).

Sensor-layer thresholds (advisory / activation — informational emission):

- **Advisory:** aggregate ≥ 90,000 words. Validator emits an advisory note.
- **Activation:** aggregate ≥ 100,000 words OR aggregate grows >10% in a single session without compensating restructure. Historically (v2) this activated the §5.3 minority per its preservation warrant. At v3 adoption §5.3 is converted to active spec and the activation-emission concept is subsumed by the §2b budget tier's hard-ceiling failure mode.

The aggregate report remains a prophylactic against the accretion failure mode the Session 022 Outsider identified ("per-file control alone is not sufficient if the default-read set keeps growing by accretion" [archive: provenance/022-workspace-scaling-trajectory/archive/022-outsider/#chunk-04, Q6]). At engine-v4 adoption the aggregate was approximately 81,500 words across 33 default-read files; activation crossed at Session 027 close (105,399 words across 39 files). Session 028 adopted §2b budget tier in response.

### 2b. Aggregate hard budget (added v3, Session 028 per D-096)

Adopted Session 028 per D-096 in response to §5.3 activation warrant firing at Session 027 close. Replaces "§5.3 preserved minority" with active specification at revised values per Session 028 deliberation.

Per-aggregate constraints:

- **Hard ceiling: 100,000 words.** Any validator run where aggregate default-read surface exceeds 100,000 words is a validation failure at `tools/validate.sh` check 20 (aggregate-budget assertion). A session whose close produces aggregate above the hard ceiling cannot close cleanly: it must execute structural remediation (see §2c close-rotation rule; §8 per-file remediation options) sufficient to return aggregate below 100,000 before close finalises.
- **Soft warning: 90,000 words.** Any validator run where aggregate default-read surface exceeds 90,000 words triggers a validator warning (not a failure). The warning is signal that the aggregate is approaching the ceiling; the next substantive-deliberation session must include at least one aggregate-reducing action (close-rotation execution, spec-archive-migration, or enumeration restructure).

Measurement: sum of per-file body word counts (`wc -w` on body content after closing YAML frontmatter delimiter) across all files in §1 default-read enumeration. The same per-file measurement methodology as §2.

**Rationale for the chosen values (Session 028 D-096).** The hard ceiling matches the §2a activation threshold that fired at Session 027 close (100K). The soft warning matches the §2a advisory threshold (90K). Matching the sensor-layer thresholds preserves semantic layering: advisory emission at 90K is also soft-warning fire; activation emission at 100K is also hard-ceiling failure. The Outsider `[01d, Q2]` critique against placing the new hard ceiling above current state ("moving the trigger after it fired") was load-bearing in the values choice; see `provenance/028-session-assessment/01-deliberation.md` §3 for the cross-family synthesis.

**Adoption-time state.** At Session 028 close adoption, aggregate is reduced from 105,399 (pre-session state per validator) to approximately 56,000 words via the §2c close-rotation rule's initial exercise: Sessions 002–022 `03-close.md` files (20 files totalling ~56,180 words) rotate to archive-surface by exclusion per §1 item 7 revision. Post-rotation aggregate sits comfortably below both hard and soft thresholds.

**Minority positions preserved Session 028 per D-096 (see `provenance/028-session-assessment/01-deliberation.md` §6 for full text and activation warrants):**

- **§5.1 Pacer 10K/7.5K per-file minority** (Session 023 preserved, unactivated) — unchanged.
- **§5.2 Skeptic no-change + warrant-literalism minority** (Session 023 preserved) — retroactively vindicated Session 027; tracking complete.
- **§5.3 Pacer aggregate-hard-budget minority** (Session 023 originated, activated Session 027) — **converted to active spec at revised values per D-096 Session 028**. Historical minority text preserved in §5.3 archive block below for provenance.
- **§5.5 tokeniser-drift watch minority** (Session 023 preserved, unactivated) — unchanged.
- **§5.6 Skeptic-preserver defer-to-softer-intervention minority** (NEW Session 028). Position: continue preservation of §5.3 rather than converting; softer-intervention bundle (close-rotation alone + prompt-guidance) first; conversion reserved if soft mechanisms fail. Activation warrant: if within 3 sessions (029–031) new budget fires only through accretion-growth with no observable operational friction and softer interventions alone would have achieved equivalent aggregate reduction, Skeptic-preserver position is retroactively vindicated; Session 031+ should revisit whether hard-budget formalism was operationally necessary.
- **§5.7 Pacer-advocate 85K/95K tighter-values minority** (NEW Session 028). Position: if adopting, use 85K soft / 95K hard (between §2a advisory and activation) to exert stronger forcing. Activation warrant: if within 5 sessions (029–033) new 100K/90K budget fires twice or more without compensating restructure forcing actual remediation, Pacer-advocate tighter-values position becomes preferred revision direction.
- **§5.8 Synthesiser-integrator 110K/120K headroom-values minority** (NEW Session 028). Position: if adopting, use 110K soft / 120K hard (above current-state aggregate) to avoid specification-in-violation. Activation warrant: if within 3 sessions remediation-chaos materialises (forced restructure mid-deliberation; deliberation distortion from emergency compliance), Synthesiser-integrator headroom-values position becomes preferred revision direction.
- **§5.9 Synthesiser-integrator 10-session retention-window minority** (NEW Session 028). Position: if adopting close-rotation, use 10-session window. Activation warrant: if within 6 sessions 6-session window + citation-exception produces a pattern where 7–10-session-back closes are consulted via retention-exception decisions more than twice per session on average, 10-session window becomes preferred revision direction.
- **§5.10 Pacer-advocate 3-session retention-window minority** (NEW Session 028). Position: if adopting close-rotation, use 3-session window (more aggressive). Activation warrant: if within 6 sessions 6-session window proves insufficient for aggregate control (sessions consistently approach the new soft 90K), 3-session window becomes preferred revision direction.
- **§5.11 Skeptic-preserver pressure-signal-audit minority (methodology-level)** (NEW Session 028). Position: numerically-specified watchpoints with no pressure-signal pairing can fire mechanistically without corresponding to the engineering state they were meant to indicate; engine should audit existing watchpoints for pressure-signal pairing. Activation warrant: if any Session 029+ budget-firing surfaces a case where firing triggers remediation that later proves operationally unnecessary (no observable friction from non-remediation), preferred revision direction is adding pressure-signal audit procedures to `read-contract.md` §8 and `validate.sh` checks 20/21/22.

**§5.3 original-minority archive block (preserved verbatim for provenance).**

Original Session 023 Pacer §5.3 minority text (preserved):

> **§5.3 Pacer aggregate-hard-budget minority** (Session 023 [01b-Q3]). Position: adopt aggregate default-read surface hard budget at 90K hard / 80K soft now; naming a budget creates the forcing function that watchpoint-only reporting lacks. Activation warrant: if aggregate exceeds 100,000 words OR grows >10% in a single session without compensating restructure, this position becomes preferred revision direction.

Session 028 adopts the §5.3 direction (aggregate hard budget) at revised values (100K/90K rather than original 90K/80K) for reasons articulated in `01-deliberation.md` §3. The original values (80K/90K) were set when aggregate was 81K; against current aggregate of 105K, adoption at 80K/90K would require immediate ~25K trim, which the Outsider characterised as "demolition order" rather than forcing function `[01d, Q2]`. Revised values 100K/90K match the §2a thresholds that empirically fired, preserving clean semantic layering without moving the trigger after it fired.

### 2c. Close-rotation rule (added v3, Session 028 per D-096)

Adopted Session 028 per D-096 as the primary remediation mechanism paired with §2b aggregate hard budget. Addresses the close-file-accretion growth pattern identified as dominant across Sessions 022–027 (per Session 028 deliberation §3a).

**The rule:** At any point in time, the default-read surface includes only the `03-close.md` files of the most recent 6 sessions (per §1 item 7). Older close files are archive-surface by exclusion per §3. Files remain at their original `provenance/NNN-title/03-close.md` paths; they are preserved verbatim per §3; they are simply not loaded by default.

**Rotation mechanics:** The rotation is automatic and implicit in the §1 item 7 enumeration. The validator's default-read detection (per `validation-approach.md` v5 §Default-read surface detection) computes the 6-session window from the sorted list of provenance directories (by NNN prefix). Closes outside the window are not counted in aggregate (check 20) and not subject to per-file budget (check 20 per-file measurement).

**No physical file movement.** Unlike archive-pack migration (§4–§9 for large files), close-rotation does not move or copy files. The rotated closes remain at `provenance/NNN-title/03-close.md` unchanged. Their access-discipline category changes from default-read to archive-surface; their physical location does not.

**Citation convention for rotated closes (v3 addition).** Default-read files may cite a rotated close using the reference form `[archive: provenance/<NNN-title>/03-close.md]` per §6 (below). Check 22 (archive-pack citation consistency) is extended at engine-v5 to recognise rotated-close references of this shape in addition to archive-pack directory references of the form `[archive: provenance/<NNN-title>/archive/<slug>/]`.

**Retention-exception mechanism (v3 addition).** A session may record a retention-exception decision to keep a specific rotated close in default-read when its content is load-bearing for currently-active governance. Retention-exceptions are cumulative; lifting also requires a decision record. The exception is recorded in the session's `02-decisions.md` as:

```
**Retention-exception:** provenance/<NNN-title>/03-close.md — <load-bearing-purpose>. Lifted when: <condition>.
```

The validator's default-read detection treats retention-exception paths as included-by-override regardless of window position. If a retention-exception decision is recorded, the session must also update the default-read enumeration effectively (e.g., via a session-close note that the list of currently-excepted closes is maintained in this file's §6 history or equivalent). **Session 028 records no retention-exceptions.** (If future sessions accumulate many exceptions, WX-28-1 observational watchpoint fires and Synthesiser-integrator §5.9 10-session window minority may become preferred direction.)

**Session 028 close initial exercise.** The first application of the rule at Session 028 close rotates Sessions 002–022 `03-close.md` files (20 files totalling ~56,180 body words) out of default-read. Retained: Sessions 023, 024, 025, 026, 027, 028 closes (6 files). No retention-exceptions recorded. Post-rotation aggregate projected at ~56,000 words / 19 files — comfortably under 100K hard and 90K soft.

**Why 6 sessions specifically.** The 6-session window is the Outsider's cross-family recommendation `[01d, Q3]` from Session 028 deliberation: "Every `03-close.md` stays default-read. That is a rule, not an accident. ... I recommend the most recent 6 session closes, plus any older close that is explicitly cited by an active specification or open issue for currently load-bearing governance." The window balances the recent-history minority-review band (§5.2 vindicated at 5-session runway; §5.4 aged out at 9-session; cross-session patterns typically operate at 3–7 session horizons) against aggregate-control forcing function. See deliberation §4 for the retention-window alternatives considered (3 Pacer, 10 Synthesiser) and their preservation as first-class minorities §6.4 and §6.5.

**Relationship to §2a sensor layer.** §2a's advisory and activation thresholds (90K / 100K) remain. The close-rotation rule is the primary remediation mechanism when aggregate approaches those thresholds. Other remediation mechanisms (spec-archive-migration, per-file restructure) remain available per §8 and §9.

### 3. Archive surface

By exclusion: anything preserved in the workspace but not on the §1 enumeration. This includes:

- Raw perspective files (`provenance/NNN-title/01X-perspective-<role>.md`) from closed sessions.
- Superseded specification versions (`specifications/*-v1.md`, `*-v2.md`, etc., carrying `status: superseded`).
- Deliberation synthesis files (`provenance/NNN-title/01-deliberation.md`) from closed sessions.
- Decision files (`provenance/NNN-title/02-decisions.md`) from closed sessions.
- Assessment files (`provenance/NNN-title/00-assessment.md`) from closed sessions.
- Manifests (`provenance/NNN-title/manifests/`) from closed sessions.
- Participant indexes (`provenance/NNN-title/participants.yaml`) from closed sessions.
- Any per-OI historical annotation files that predate the Session 022 `open-issues/` directory split.

Archive surface records are **preserved verbatim.** Summarisation, silent compression, content-aware truncation, or edit-in-place are forbidden. The preservation-vs-summarisation distinction is the load-bearing property that prevents this specification from becoming an on-ramp for information loss.

Archive surface records are **accessed by explicit reference.** A session reading an archive record must cite it per §6 below; silent non-reads of relevant archive records are a validation concern (check 22 and Tier 2 Q9 in `validation-approach.md` v5).

### 4. Archive-pack structure

When an archive-surface record exceeds the default-read per-file budget (§2 hard ceiling), or when the archive record is produced within a current session that will otherwise push the current-session provenance directory over budget at close, the record must be structured as an **archive-pack**: a directory with a manifest plus numbered chunks, preserving byte-identical content via line-range splits only.

Archive-pack layout:

```
provenance/NNN-title/archive/<slug>/
  manifest.yaml        # frontmatter + chunk table + integrity fields
  00-source.md         # byte-identical single file if under per-chunk budget
  OR
  01-chunk.md          # numbered chunks with line-range boundaries only
  02-chunk.md
  ...
```

Chunk size target: each chunk ≤ 6,000 words (matching the §2 soft warning) so that reading any individual chunk never exceeds comfortable read budget. In practice, byte-range chunking at ~50,000 bytes yields chunks of approximately 5,000-7,000 words for typical workspace prose (Session 022/023/024 precedent); the word-count target is a design guide, not a hard per-chunk constraint.

Boundary rule: **mechanical only** — either line-range or byte-range boundaries. Content-aware boundaries (e.g., "end at a paragraph break," "split at a heading") are forbidden because they introduce chunking judgment that can silently edit content over time. Line-range and byte-range boundaries are both mechanical and auditable; the manifest declares which rule was used via `chunk_boundary_rule: line-range | byte-range | single-file`. Line-range is preferred where the file's line-length distribution is bounded; byte-range is the fallback when the file contains very long lines that would otherwise produce oversized chunks (the Session 014 Outsider file exemplifies this: a 96,651-word file with individual lines of up to 3,328 words; line-range chunking produced chunks over 36,000 words that would themselves breach the default-read budget, so byte-range splitting into 50,000-byte chunks was used).

### 5. Archive-pack manifest fields

The `manifest.yaml` file in every archive-pack carries the following required fields:

```yaml
---
archive_id: <stable identifier, typically <originating-NNN>-<slug>>
originating_session: <session number>
originating_path: <workspace-relative path of the source file>
migrated_in_session: <session number that created the archive-pack>
kind: raw-perspective | over-budget-annotation | superseded-spec | other-named
total_bytes: <integer; bytes of concatenated chunks in canonical order>
total_words: <integer; words of concatenated chunks>
chunk_count: <integer>
chunk_boundary_rule: line-range | single-file
source_hash_sha256: <SHA-256 hash of full concatenation of chunks in ordinal order>
chunks:
  - ordinal: 1
    file: 01-chunk.md
    line_range: "1-500"
    chunk_hash_sha256: <SHA-256 hash of this chunk's contents>
  - ordinal: 2
    file: 02-chunk.md
    line_range: "501-1000"
    chunk_hash_sha256: <SHA-256 hash>
  ...
readers_note: <1-3 sentences; what the archive preserves; when to consult it>
---
```

The manifest is pointer-only. Narrative content beyond the `readers_note` field is forbidden — `readers_note` is at most three sentences. The manifest exists to resolve references, not to summarise the archived content.

### 6. Reference conventions

Default-read surface files cite archive-surface records using a stable reference string:

```
[archive: provenance/NNN-title/archive/<slug>/]
```

With optional chunk-level precision:

```
[archive: provenance/NNN-title/archive/<slug>/#chunk-02]
```

Readers resolving the reference read `manifest.yaml` first, consult the `readers_note`, and then read specific chunks as the current work requires. A citing session that relies on archive content for a load-bearing claim must either read the cited chunk(s) in full, or declare in its honest-limits section that the claim rests on prior-session vetting of the archive content rather than fresh re-reading.

The reference convention is load-bearing for validator check 22 (archive-pack citation consistency): every `[archive: path]` reference in a default-read file must resolve to an existing archive-pack path.

### 7. Integrity guarantee

The `source_hash_sha256` field in each archive-pack manifest is computed against the canonical concatenation of chunks in numerical order. `tools/validate.sh` check 21 verifies this hash on every run; any mismatch is a hard-fail.

Per D-017 immutability (`workspace-structure.md` §provenance), once the migrating session closes, archive-pack files are immutable. Any revision to an archive-pack's content requires a new migrating session with its own decision record; the revision creates a new archive-pack and a supersession reference, not an edit of the prior pack.

Archive-packs created by retroactive migration (migrating a closed session's file into archive form) use the **copy-plus-reference** discipline per Session 009 D-054 precedent: the original file at its original path is **not modified**; the archive-pack is created alongside, typically in the migrating session's own provenance directory (`provenance/<migrating-NNN>/archive/<slug>/`). The original remains at its original path as the byte-identical witness; the archive-pack provides structured access.

Archive-packs created for the current session's own raws (per §9 close-time obligation) move the original content into the archive-pack structure directly (the original path becomes the archive-pack path; no duplication). Because the session is still open at the time of packing, moving is not an edit of a closed-session file.

### 8. Default-read surface budget at session close

At every session close, the orchestrator verifies that every file in the §1 enumeration satisfies the §2 per-file budget. `tools/validate.sh` check 20 enforces this; a hard-fail at session close blocks the session from closing cleanly.

Remediation when a default-read file exceeds the budget: reduce the file in place; or split the file into multiple default-read files (each under budget) with the original split-file designated archive-surface (its content preserved as an archive-pack); or relocate detail to archive-pack form with references from a thinner default-read replacement.

Remediation must not summarise or silently compress; the archive-pack discipline preserves content verbatim.

### 9. Close-time obligation for current-session raws

At every session close, the orchestrator measures each raw perspective file and each provenance file in the current session directory. Any file exceeding the default-read per-file hard ceiling (§2: 8,000 words) is archive-packed before session close.

Mechanism for current-session raw-to-archive-pack migration:

1. Create `provenance/NNN-title/archive/<slug>/` where `<slug>` is a short descriptive identifier (typically matching the perspective role and question theme).
2. Split the file into line-range or byte-range chunks each ≤ 6,000 words (or ~50,000 bytes, which yields comparable chunk sizes per §4). Preserve byte-identical content.
3. Write `manifest.yaml` with the required fields (§5), computing all hashes.
4. **Remove the original file** from the provenance root. The original content now lives in the archive-pack chunks (byte-identical); there is no duplication. (This removal is permissible during session close because D-017 immutability binds only on closed sessions.)
5. Update any in-session references (e.g., from `01-deliberation.md`) to use the `[archive: path]` convention.

The SESSION-LOG entry for the session records archive-pack presence with a one-phrase note (e.g., "archive-packs: 1 (outsider)").

### 10. Versioning

Version 1 established Session 022 per D-084. Version 2 established Session 023 per D-086 (§2 budget-value recalibration from 15K/10K to 8K/6K; §2 Rationale corrected for empirical 3.0× tokens-per-word ratio; §2a aggregate report added; §5.1/§5.2/§5.3/§5.5 minorities added). v1 preserved as `read-contract-v1.md` with `status: superseded`.

Version 3 established Session 028 per D-096 in response to §5.3 minority activation warrant firing at Session 027 close (aggregate crossed 100,000 words). Substantive additions: §2b aggregate hard budget (100K hard / 90K soft, pass/fail/warn); §2c close-rotation rule (most recent 6 sessions' closes retained in default-read; older closes archive-surface by exclusion; retention-exception mechanism); §1 item 7 revised from "every close" to "6 most recent closes"; §2a role clarified as informational sensor layer supplementing §2b budget enforcement; six new first-class minorities §5.6–§5.11 preserved with activation warrants. v2 preserved as `read-contract-v2.md` with `status: superseded`.

Version 4 established Session 036 per D-113 + D-116. Substantive additions: §1 item 0 adds `MODE.md` at workspace root as default-read (workspace-identity marker per `workspace-structure.md` v5 §MODE.md); §1 item 9 adds conditional `engine-feedback/INDEX.md` default-read clause in self-development mode. No change to §2 per-file budget values, §2b aggregate budget, §2c close-rotation mechanics, §4 archive-pack structure, §5 manifest fields, §6 reference convention, or §7 integrity mechanism. Aggregate budget headroom impact: `MODE.md` is approximately 200 words at adoption (negligible against 68,689 aggregate); `engine-feedback/INDEX.md` at adoption is thin-index header-only (under 100 words). v3 preserved as `read-contract-v3.md` with `status: superseded`.

Subsequent revisions to this specification follow OI-002 substantive-vs-minor heuristic (`open-issues/OI-002.md`):
- **Substantive:** any change to the §1 enumeration, §2 budget values, §2a aggregate thresholds, §2b budget values, §2c retention-window values, §4 archive-pack structure, §5 manifest fields, §6 reference convention, or §7 integrity mechanism. Engine-version bump per `engine-manifest.md` §5.
- **Minor:** clarifying text edits, cross-reference updates, examples within existing scope.

Watchpoint recorded Session 023 D-086 R10 §5.5: if `read-contract.md §2` budget values are revised a second time within three sessions of Session 023 v2 adoption, examine whether the spec's design frame (per-file word count as measurement primitive) is itself miscalibrated — consider token-count or hybrid metrics. (Status at Session 028: §2 budget values unchanged this session; the v2 → v3 revision adds §2b aggregate budget but does not re-revise §2 per-file values. Watchpoint status: preserved; no re-revision within three sessions occurred.)

Watchpoint recorded Session 028 D-096 **WX-28-1**: close-rotation-exception-frequency. If within 10 sessions of Session 028 adoption retention-exception decisions are recorded in 3 or more sessions, the 6-session retention window may be too narrow; Synthesiser-integrator §5.9 10-session window minority becomes preferred revision direction.

## Validation

To validate this specification:

1. Confirm every file in the §1 enumeration exists at its declared path and carries the required frontmatter (for specifications) or is a well-formed index/close.md (for SESSION-LOG and open-issues).
2. Confirm every file in the §1 enumeration satisfies the §2 per-file budget. `tools/validate.sh` check 20 automates this verification.
3. Confirm that files not in the §1 enumeration but present in the workspace are either (a) explicitly archive surface (per §3), or (b) out-of-scope top-level files (e.g., `.git`, `.gitignore`, `.claude`, `.serena`, `applications/`), or (c) session-scratch files outside the read-contract scope.
4. For every archive-pack in `provenance/*/archive/*/`: confirm `manifest.yaml` is well-formed with all §5 required fields; confirm `source_hash_sha256` matches the actual hash of concatenated chunks in canonical order. `tools/validate.sh` check 21 automates this.
5. For every `[archive: path]` reference in a default-read surface file: confirm the reference resolves (path exists; chunk ordinals exist if specified). `tools/validate.sh` check 22 automates this.
6. Confirm that `methodology-kernel.md` §1 Read references this specification as the authority on default-read vs archive distinction.
7. Confirm that `prompts/development.md` and `prompts/application.md` read-activity instructions reference this specification as the authority.
8. Confirm that `workspace-structure.md` v4 §SESSION-LOG.md, §open-issues, and §specifications point at this specification for the access-discipline rules.
