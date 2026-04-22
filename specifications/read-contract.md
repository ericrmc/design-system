---
title: Read Contract
version: 1
status: active
created: 2026-04-22
last-updated: 2026-04-22
updated-by-session: 022
supersedes: none
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

**The default-read surface enumeration at engine-v3:**

1. Every active-status `.md` file in `specifications/`. "Active-status" means frontmatter `status: active`. Superseded-status files (`*-v1.md`, `*-v2.md`, etc., carrying `status: superseded`) are archive surface by exclusion (§3).
2. `PROMPT.md` (top-level dispatcher).
3. `prompts/development.md` (self-development executable prompt).
4. `prompts/application.md` (external-application executable prompt).
5. `SESSION-LOG.md` (thin one-line-per-session index; full per-session detail lives in `03-close.md`).
6. `open-issues/index.md` (thin overview; full per-OI detail lives in `open-issues/OI-NNN.md` files).
7. Every `provenance/NNN-title/03-close.md` across all closed sessions.
8. Every file in the currently-active session's provenance directory (`provenance/NNN-title/` where NNN is the current session). While the session is open, current-session provenance is default-read; on close, it becomes archive surface by exclusion (§3) unless it is a `03-close.md` (which stays default-read by §7 above).

The enumeration is closed. A file not enumerated here is archive surface by §3.

### 2. Default-read budget

Per-file constraints:

- **Hard ceiling: 15,000 words.** Any file in the §1 enumeration exceeding 15,000 words of body content (frontmatter excluded) is a validation failure at `tools/validate.sh` check 20. The session that produces such a file must either reduce it or restructure it (e.g., split into multiple files each under the ceiling; relocate detail to archive surface with reference from the default-read file).
- **Soft warning: 10,000 words.** Any file in the §1 enumeration between 10,000 and 15,000 words triggers a validator warning (not a failure). The warning is signal that the file is approaching the ceiling; the next session should consider restructuring.

Measurement: word count via `wc -w` on body content after the closing YAML frontmatter delimiter. The word-count metric is chosen for stability across tokenisers (per Session 022 Outsider [01d-Q6] + Conservator [01b-Q6] convergence).

**Rationale for the chosen values.** The current single-Read-tool ceiling at the time of adoption is approximately 25,000 tokens (≈ 19,250 words at a 1.3× words-to-tokens approximation). A 15,000-word hard ceiling leaves headroom below the single-read ceiling. The 10,000-word soft warning provides early signal before files approach the hard ceiling.

**Outsider minority position** (§5.3 of `provenance/022-workspace-scaling-trajectory/01-deliberation.md`): 8,000-word per-file budget is the conservative-preferable value; 15,000 may be permissive. Activation warrant: if any default-read file exceeds 10,000 words (soft warning) within 5 sessions of adoption without subsequent restructure, the 8,000-word ceiling becomes the preferred revision direction.

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

Chunk size target: each chunk ≤ 10,000 words (matching the §2 soft warning) so that reading any individual chunk never exceeds comfortable read budget.

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

At every session close, the orchestrator measures each raw perspective file and each provenance file in the current session directory. Any file exceeding the default-read per-file hard ceiling (§2: 15,000 words) is archive-packed before session close.

Mechanism for current-session raw-to-archive-pack migration:

1. Create `provenance/NNN-title/archive/<slug>/` where `<slug>` is a short descriptive identifier (typically matching the perspective role and question theme).
2. Split the file into line-range chunks each ≤ 10,000 words. Preserve byte-identical content.
3. Write `manifest.yaml` with the required fields (§5), computing all hashes.
4. **Remove the original file** from the provenance root. The original content now lives in the archive-pack chunks (byte-identical); there is no duplication. (This removal is permissible during session close because D-017 immutability binds only on closed sessions.)
5. Update any in-session references (e.g., from `01-deliberation.md`) to use the `[archive: path]` convention.

The SESSION-LOG entry for the session records archive-pack presence with a one-phrase note (e.g., "archive-packs: 1 (outsider)").

### 10. Versioning

Version 1 established Session 022 per D-084. Subsequent revisions to this specification follow OI-002 substantive-vs-minor heuristic (`open-issues/OI-002.md`):
- **Substantive:** any change to the §1 enumeration, §2 budget values, §4 archive-pack structure, §5 manifest fields, §6 reference convention, or §7 integrity mechanism. Engine-version bump per `engine-manifest.md` §5.
- **Minor:** clarifying text edits, cross-reference updates, examples within existing scope.

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
