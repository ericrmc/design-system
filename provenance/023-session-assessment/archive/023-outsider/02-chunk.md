lit file or relocate detail to archive-pack)."
tools/validate.sh:803:    elif [[ $word_count -gt $DEFAULT_READ_SOFT_WORD_CEILING ]]; then
tools/validate.sh:804:      warn "$rel — $word_count words exceeds soft warning threshold ($DEFAULT_READ_SOFT_WORD_CEILING). Approaching hard ceiling ($DEFAULT_READ_HARD_WORD_CEILING)."

codex
I’ve confirmed the mechanics the brief cites: `read-contract.md §2` and §10 really do make value changes substantive, and `engine-manifest.md §5` really does tie substantive engine-definition changes to an engine bump. I’m checking the OI-002 / workspace-structure revision heuristic next, because Q4 turns on whether there is any legitimate “minor-within-scope” escape hatch.
exec
/bin/zsh -lc "sed -n '90,150p' specifications/validation-approach.md" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "sed -n '1,220p' open-issues/OI-002.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
**Rationale for session-number gating.** Checks 16, 17, 19 enforce schema fields introduced by `multi-agent-deliberation.md` v4 §Heterogeneous-Participant Recording Schema (D-082, Session 021). Pre-adoption manifests do not have these fields and cannot have them retroactively per the immutability rule (D-017). Per the Session 006 D-039 precedent for checks 14/15, session-number gating is the correct mechanism for prospective-only schema adoption. Presence-gating would create the ambiguity-of-absence problem (a missing `claude_output_in_training:` field cannot be distinguished from "pre-adoption" vs "author forgot").

**Presence-gating (check 18).** Check 18 fires only when an `oi-004-retrospective.md` file is present anywhere under `provenance/*/`. The artefact does not exist until a future session writes it; pre-existence sessions are out-of-scope. Once written, check 18 verifies structural well-formedness; substantive adequacy is Tier 2 Q8 (paired).

**Out-of-scope behaviour for participant_kind values.** Check 17 is out-of-scope for `participant_kind` in `{claude-subagent, anthropic-other}` (no Claude-output disclosure required for Claude-family participants). Check 19 is out-of-scope for `participant_kind` other than `non-anthropic-model` (organisational origin closed-set membership is required only for non-Anthropic LLM participants). These are recorded inline in the validate.sh check implementation and in the honest-limit comments.

**Closed-set extension discipline.** The PARTICIPANT_ORGANISATION_CLOSED_SET in `validate.sh` is initialised at engine-v2 with values `{anthropic, openai, google, meta, xai, mistral, deepseek, cohere, local, human-individual, other-named}`. Extending this set requires a named decision in a session's `02-decisions.md` and a same-session update to the constant. Adding a new provider is **not** a substantive revision to `multi-agent-deliberation.md` per OI-002 heuristic (the spec already permits the closed set to extend); it is a substantive update to `tools/validate.sh` per `engine-manifest.md` §5 only when the addition substantively changes what counts as criterion-4-eligible. Routine provider additions (e.g., adding `cohere` after first operational use) are treated as minor validator-data updates not triggering an engine-version bump. This convention is established Session 021 and may be revisited if it produces silent failures.

**Consequence for prior sessions.** Sessions 001 through 020 are out-of-scope for checks 16, 17, 19. Session 021 and later sessions whose manifests claim OI-004 narrowing must include the new fields per the schema in `multi-agent-deliberation.md` v4. Pre-adoption sessions retain their original manifests unchanged.

### Gating Conventions (checks 20, 21, 22) — Session-number and presence-gating

**Session-number-gating (check 20).** Check 20 applies only to sessions numbered ≥ 022 (the session that adopted `specifications/read-contract.md` v1). The gate is encoded as an explicit constant `READ_CONTRACT_ADOPTION_SESSION=22` near the top of `validate.sh`. Out-of-scope sessions (001 through 021) produce no output from check 20 — pre-adoption SESSION-LOG.md / open-issues.md sizes are preserved as-is until the R8a / R8b migrations complete in Session 022.

**Presence-gating (checks 21, 22).** Checks 21 and 22 fire only when at least one `provenance/*/archive/*/` directory exists. The archive-pack infrastructure does not exist until Session 022 creates the first archive-pack (Session 014 Outsider retroactive migration per R8c); pre-existence sessions are out-of-scope.

**Rationale for mixed gating.** Check 20 measures default-read surface files that exist prospectively from the adoption session onward. Checks 21 and 22 measure archive-packs that exist only when created; presence-gating is the correct mechanism per Session 005 D-030 precedent.

**Budget constants.** Encoded near the top of `validate.sh`:

```
DEFAULT_READ_HARD_WORD_CEILING=15000
DEFAULT_READ_SOFT_WORD_CEILING=10000
READ_CONTRACT_ADOPTION_SESSION=22
```

Any revision to these constants is a substantive revision to `tools/validate.sh` per `engine-manifest.md` §5 and requires an engine-version bump.

**Measurement.** Check 20 measures word count via `wc -w` on body content after the closing YAML frontmatter delimiter. Frontmatter and the three-dash delimiters themselves are excluded.

**Default-read surface detection.** The validator maintains a canonical default-read file-set derived from `read-contract.md` §1. The implementation uses a glob-based helper (not filename heuristics) reading the §1 enumeration patterns:
- `specifications/*.md` where frontmatter `status: active` (not `superseded`, `draft`, or `deprecated`).
- `PROMPT.md`, `prompts/development.md`, `prompts/application.md`.
- `SESSION-LOG.md`.
- `open-issues/index.md`.
- `provenance/*/03-close.md`.
- Files in the currently-active session's provenance directory (only the most recent NNN- directory containing an un-closed `03-close.md` or no `03-close.md` at all).

Archive-pack files and superseded-status specifications are excluded from check 20 scope.

### Sequencing (check 13 after check 12; check 14 after check 11; check 15 after check 12)

Check 13 depends on well-formed manifests. If check 12 fails for a given session, check 13 reports `BLOCKED: check 12 failed for this session; cannot evaluate check 13` for that session and does not itself fail or warn. This prevents double-reporting of a single underlying problem and keeps the tool honest about what it actually evaluated.

Check 14 depends on the three-raw-output floor established by check 11. If check 11 fails for a given session (fewer than three perspective files when multi-agent artefacts are asserted), check 14 reports `BLOCKED: check 11 failed for this session; cannot evaluate check 14`. Check 14 does **not** depend on check 12: it inspects perspective-file presence, not manifest content (per D-040, the Outsider's precision argument).

Check 15 depends on well-formed manifests. If check 12 fails for a given session, check 15 reports `BLOCKED: check 12 failed for this session; cannot evaluate check 15`. Check 15 is independent of check 14 (a decision can fail 15 while passing 14 or vice versa).

### Check 13's Honest Limit (mandatory inline documentation)

Check 13 enforces **consistency of self-report**, not **truthfulness of self-report**. This limit is mandatory content in three locations:

1. A comment block in `tools/validate.sh` directly above check 13's implementation.
2. Check 13's failure message (as an inline NOTE).
3. This specification (above).

The language to preserve verbatim:

> This check verifies the session's claim is internally consistent with its manifests. It does not and cannot verify that the manifests' lineage claims are themselves true. Manifest truth relies on operator integrity and the `participant_selected_by` field's accountability.

**Known gaming modes** (recorded in D-029 and preserved for future maintainers):

 succeeded in 0ms:
---
id: OI-002
status: see-body
surfaced-in-session: see-body
---

### OI-002: Threshold for substantive revision vs. minor correction
**Surfaced:** Session 001
**Status:** Open (data points added Sessions 002, 003, 004, 005, 006, 009, 011, 017, 019; Session 012, Session 013, Session 014, and Session 017 added observations on the narrow-single-purpose-spec-creation pattern without formal heuristic updates)
Decision D-004 established that substantive revisions trigger file-level version preservation while minor corrections do not. No formal criteria for distinguishing the two have been defined. Session 002 (D-014): adding `tools/` to workspace-structure was minor — change *anticipated by* the specification's own language. Session 003 (D-020): adding a pointer to `multi-agent-deliberation.md` in methodology-kernel.md was minor — kernel's Convene/Deliberate language was already mechanism-neutral. Session 004 (D-026): revising `multi-agent-deliberation.md` v1 → v2 was **substantive** — adds new normative content (new trigger rules, new required fields, new mechanism shapes) not anticipated structurally in v1. Session 005 (D-034): a pair of simultaneous revisions resolved differently — revising `validation-approach.md` v1 → v2 was **substantive** (added three new Tier 1 checks with gating, severity, sequencing, and a new Tier 2 question; new normative content); annotating each Open Extensions entry in `multi-agent-deliberation.md` v2 with an activation precondition was **minor** (elaboration within the section's explicit purpose of naming future candidates; no rules, required fields, triggers, or required artefacts changed). Session 006 (D-041): first session where **both** active revisions were substantive — `multi-agent-deliberation.md` v2 → v3 (adds `triggers_met:` required schema, new Trigger-Coverage Annotation Schema section, updates Validation section operationalisation status) and `validation-approach.md` v2 → v3 (adds two new Tier 1 checks with gating/severity/sequencing/honest-limits and a new Tier 2 question). D-042's revision of an Open Extensions activation precondition was minor per the Session 005 pattern (bundled into v3, not separately preserved). Session 009 (D-053, D-054): `methodology-kernel.md` v1 → v2 was **substantive** (named two senses for §7 Validate with domain-actor phrasing, new normative content); `workspace-structure.md` v1 → v2 was **substantive** (created `applications/` top-level directory with mutability rules and copy-plus-reference regularization). Session 011 (D-060): `methodology-kernel.md` v2 → v3 is **substantive** — added two named senses for §1 Read (workspace reading, domain reading), first-sentence reorder removing self-hosting-first framing, PROMPT.md reconciliation clause localising §1's scope, perspective-pretraining routing-note; new normative content not anticipated in v2's §1 text. The five-point heuristic holds stable: **minor** if the change makes explicit what the specification's existing language already contains or explicitly anticipates as a category of extension, OR annotates existing candidate entries with descriptive metadata within the section's stated purpose; **substantive** if the change adds new normative content (rules, required fields, severity decisions, gating rules, triggers, required artefacts) beyond what the existing language contains. Session 012 (D-063): created `specifications/identity.md` as a new v1 specification (`supersedes: none`). This is a **creation**, not a revision — outside OI-002's existing binary of substantive-vs-minor-revision. Observation recorded for future heuristic development: the heuristic's scope is revisions; creations of narrow single-purpose specs (like identity.md) may warrant a third category. No formal OI-002 update; monitor. Session 013 (D-066): revised the Session 010 external artefact (`applications/010-household-decision-protocol/house-decision-five-moves.md`) v1 → v2 per user Validate receipt. The pattern used operationally — preserve prior version with `-v1` suffix in place, mark `status: superseded`, update canonical path's frontmatter with `version:`, `supersedes:`, `last-revised-session:` — is analogous to the specification-revision pattern but applies to an **external artefact in `applications/`**, not a specification in `specifications/`. Like Session 012's creation case, this is **outside OI-002's existing scope** (which covers specification revisions only). Observation recorded: external-artefact revisions may warrant their own pattern formalisation (see WX-13-6); a future session may deliberate whether `workspace-structure.md` §applications should formalise the `-v1` preservation pattern. No formal OI-002 update; monitor. Session 014 (D-069, D-071): revised `methodology-kernel.md` v3 → v4 (**substantive** per heuristic — new normative content: Reference validation named as third sense, anti-substitution clause, label discipline, scope-statement). File-level versioning applied per precedent; v3 preserved as `methodology-kernel-v3.md`. Session 014 also **created** `specifications/reference-validation.md` v1 as a new narrow single-purpose specification (`supersedes: none`). This is the **second creation** of a narrow single-purpose spec after Session 012's `identity.md`. Per Session 012 D-063 precedent, creation of a narrow single-purpose spec is outside OI-002's existing substantive-vs-minor-revision binary. Observation recorded: the pattern of narrow-single-purpose-spec creation is now n=2 (identity.md + reference-validation.md); a future heuristic update could formalise creation as a third category distinct from substantive revision and minor revision. No formal OI-002 update this session; monitor. Session 017 (D-074): revised `identity.md` v1 → v2 (**substantive** — adds three-layer denotation; new normative content) and `workspace-structure.md` v2 → v3 (**substantive** — adds file-class distinction; documents `prompts/` directory; new normative content). File-level versioning applied; v1/v2 preserved. Session 017 also **created** `specifications/engine-manifest.md` v1 as the **third** narrow single-purpose specification (`supersedes: none`) — pattern is now n=3 (identity.md + reference-validation.md + engine-manifest.md). Additionally executed **three minor edits without v-bump**: `methodology-kernel.md` v4 (one-sentence §Purpose scope clarification referencing engine-manifest and identity); `multi-agent-deliberation.md` v3 (one-sentence §Purpose scope-applicability); `validation-approach.md` v3 (one-sentence §Purpose scope-applicability). All three minor edits are elaborations within existing scope (no new rules, required fields, severity decisions, gating rules, triggers, or required artefacts); the five-point heuristic continues to hold stable. **The n=3 narrow-single-purpose-spec-creation pattern is now increasingly warranted for formalisation as a third OI-002 category** (distinct from substantive revision and minor revision); a future session may execute the formalisation as a minor update to the heuristic. No formal OI-002 update this session; monitor. Session 019 (D-078): revised `reference-validation.md` v1 → v2 (**substantive** per heuristic — adds new normative rejection conditions at §1 C3 (verbatim-phrase zero-tolerance; cross-family retrieval asymmetry), new §9 re-opening trigger 7, new L1 two-stage structure with preserved-record obligation at L1b; extended §9 trigger 6; sharpened §9 trigger 5). File-level versioning applied; v1 preserved as `reference-validation-v1.md` with `status: superseded`, `superseded-by: reference-validation.md (v2)`. The five-point heuristic continues to hold stable. No formal OI-002 update this session; monitor.



exec
/bin/zsh -lc 'rg -n "substantive|minor|v-bump|spec-revision" specifications/workspace-structure.md' in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
78:Both files are revisable under the methodology's spec-revision discipline (significant revisions recorded in provenance; v-suffix preservation if substantive changes accumulate).
122:When a specification undergoes substantive revision, the prior version is preserved with a version suffix (e.g., `workspace-structure-v1.md`) and the new version takes the canonical filename. Minor corrections are committed through git without file-level versioning.

codex
The versioning question is tighter than it first looks. `validation-approach.md` also explicitly says revising the budget constants in `validate.sh` is substantive and bump-worthy, so avoiding `engine-v4` would require overruling multiple live specs, not just soft-reading one sentence in `read-contract.md §10`.
exec
/bin/zsh -lc "sed -n '1,220p' provenance/022-workspace-scaling-trajectory/archive/022-outsider/manifest.yaml" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "sed -n '1,260p' provenance/022-workspace-scaling-trajectory/03-close.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
archive_id: 022-outsider
originating_session: 022
originating_path: provenance/022-workspace-scaling-trajectory/01d-perspective-outsider.md (original moved into this archive-pack at session close per read-contract.md §9)
migrated_in_session: 022
kind: raw-perspective
total_bytes: 168247
total_words: 22611
chunk_count: 4
chunk_boundary_rule: byte-range
source_hash_sha256: a6f8734f792c1dfb9d3387247eb9d1c70c72cf28531ae1c6db7efc7555d740b8
chunks:
  - ordinal: 1
    file: 01-chunk.md
    byte_range: "0-49999"
    chunk_hash_sha256: af5dd03325e87f7347e9594a3a0daf2ef8bb4bd68d90b3649ce8228033005c14
  - ordinal: 2
    file: 02-chunk.md
    byte_range: "50000-99999"
    chunk_hash_sha256: 26de4e2b1087a29dad60659a7c284e6effb34100274133b02b0aadba2c8e1d8f
  - ordinal: 3
    file: 03-chunk.md
    byte_range: "100000-149999"
    chunk_hash_sha256: fb94e6894d4bd2e3195575fc71c16982119956bb2d6b1b1c39296f08d50f644d
  - ordinal: 4
    file: 04-chunk.md
    byte_range: "150000-168246"
    chunk_hash_sha256: e968de21a740b5dd0e6822ef306948f8d5abcb2335a1a4c3eb9af201249aed7f
readers_note: Session 022 OpenAI GPT-5.4 Outsider perspective via codex exec (session_id 019db521-775f-7872-9b38-f0c4b0094c28; tokens_used 46,382; reasoning effort xhigh). Full CLI banner + echoed brief + four codex markers with pre-response workspace-exploration tool calls + reasoning summary + response body (opening + Q1-Q9 + Honest Limits) + end-of-stream duplicate response body preserved verbatim per Session 014 precedent. Read chunk 04 for the response body tail (Q7-Q9 + Honest Limits); chunks 01-03 for brief echo + reasoning traces + response body. Per read-contract.md §9, the original file at 01d-perspective-outsider.md was moved into this archive-pack at session close; there is no duplication.

 succeeded in 0ms:
---
session: 022
title: Close — Read-Contract Adoption; engine-v2 → engine-v3; SESSION-LOG thinned; open-issues/ directory; Session 014 Outsider archive-packed
date: 2026-04-22
status: complete
---

# Close — Session 022

## Artefacts produced

### Provenance (`provenance/022-workspace-scaling-trajectory/`)

- `00-assessment.md` — session-open assessment: Session 021 audit across five close-directed dimensions; minor findings on close.md validation count and d016_1 over-declaration; five paths presented; halt for operator direction.
- `01-brief-shared.md` — shared deliberation brief (§1 methodology context; §2 problem statement + scale facts; §3 operator direction verbatim; §4 current spec text excerpts; §5 Session 020 minority warrant assessment; §6 survey of adjacent traditions; §7 perspective placement; §8 design questions Q1–Q9; §9 response format; §10 anti-import constraint; §11 closure). Committed at anchor commit `46f0baf`.
- `01a-stance-architect.md`, `01b-stance-conservator.md`, `01c-stance-skeptic.md`, `01d-stance-outsider.md` — role-specific stances, 150–300 words each per v4 §Stance Briefs.
- `01a-perspective-architect.md` — Claude Opus 4.7 subagent output (verbatim). Position: accept frame with refinement (orientation/preservation rename); propose specific prompts text; session-local archive-pack location; retroactive migration limited to Session 014 Outsider; engine-v3 warranted.
- `01b-perspective-conservator.md` — Claude Opus 4.7 subagent output (verbatim). Position: partial frame acceptance; rename to "active-layer" / "preserved-layer"; kernel §1 Read revision required; SHA-256 integrity; session-local location; epoch-indexing rejected as forbidden summarisation; engine-v3.
- `01c-perspective-skeptic.md` — Claude Opus 4.7 subagent output (verbatim). Position: REJECT frame as codifying OI-015 harness-layer routing; adopt only E.1 + SESSION-LOG thin-index (§5.3); reject engine bump; reject no-grandfather; adversarial burden on falsifiers met.
- `01d-perspective-outsider.md` → **archive-packed at close per read-contract.md §9** (22,611 words exceeded 15,000-word hard ceiling). Archive-pack at `archive/022-outsider/` (4 chunks, 50KB each; byte-range boundaries; SHA-256 verified). Original file removed from provenance root; content preserved byte-identical in archive. Outsider position (OpenAI GPT-5.4 via `codex exec`, session id `019db521-775f-7872-9b38-f0c4b0094c28`, tokens_used 46,382, reasoning effort xhigh): partial frame acceptance; diagnoses "broken read contract" as deeper frame than canonical-vs-witness; proposes access-discipline layer cutting across existing file-class ontology; new `specifications/read-contract.md` spec (adopted); bounded working-set contract framing; aggregate-size discipline; prompts/application.md export-consistency concern (all five Outsider contributions shaped adopted content per D-084 synthesis §6).
- `01-deliberation.md` — synthesis. Maps 4-of-4 convergences (C1 E.1; C2 SESSION-LOG restoration) and 3-of-4 cross-family convergences (C3 frame acceptance; C4 kernel revision; C5 prompts revisions; C6 application.md alignment; C7 014 Outsider migration; C8 engine-v3; C9 triggers). Divergences D1–D5 explicitly tracked and resolved with cross-family honesty (D3 new-spec location adopted Outsider's side per cross-family composition; D1 archive-pack location adopted 2-Claude locality with Outsider minority preserved; D2 budget value adopted compromise with Outsider minority preserved). Anti-laundering check passes tests 1 and 3 fully, tests 2 and 4 partially with watchpoints WX-22-1 through WX-22-5.
- `02-decisions.md` — two decisions. D-084 adopts R1–R11 with `triggers_met: [d016_1, d016_2, d016_3, d023_1, d023_2, d023_3]`. D-085 OI housekeeping with `triggers_met: [none]`.
- `03-close.md` — this file.
- `manifests/architect.manifest.yaml`, `conservator.manifest.yaml`, `skeptic.manifest.yaml`, `outsider.manifest.yaml` — per-participant D-024 manifests with v4 schema fields.
- `participants.yaml` — session-level index with `oi004_qualifying_participants: [outsider]`.
- `archive/pre-R8a-SESSION-LOG/` — archive-pack witness of pre-thin SESSION-LOG.md (10,405 words; single-file chunk; SHA-256 verified).
- `archive/pre-R8b-open-issues/` — archive-pack witness of pre-split `open-issues.md` (9,783 words; single-file chunk; SHA-256 verified).
- `archive/014-oi016-outsider/` — archive-pack of Session 014 Outsider perspective file (96,651 words → 18 chunks; byte-range boundaries; SHA-256 source hash matches concatenation). Copy-plus-reference discipline: **original `provenance/014-oi016-resolution/01d-perspective-outsider.md` unchanged** at its original path per D-017 immutability.
- `archive/022-outsider/` — archive-pack of Session 022's own Outsider perspective file (22,611 words → 4 chunks; byte-range boundaries; SHA-256 verified). **Move-not-copy discipline per read-contract §9**: original `01d-perspective-outsider.md` removed from provenance root; content preserved byte-identical in archive chunks. No grandfather clause honored.

### Specifications created

- **`specifications/read-contract.md` v1** — new narrow-single-purpose specification. n=5 in the OI-002 narrow-spec pattern (after identity.md, reference-validation.md, engine-manifest.md, and read-contract.md — wait, this is read-contract.md itself being the 5th; actually n=4 including read-contract.md per D-084 synthesis §2 D3 analysis).

Correction: OI-002 narrow-single-purpose-spec pattern is now n=4 (identity.md + reference-validation.md + engine-manifest.md + read-contract.md). The Session 022 D-084 creates the 4th.

### Specifications revised substantively

- **`methodology-kernel.md` v4 → v5** — §1 Read revised to articulate default-read surface vs archive surface distinction with explicit cross-reference to `read-contract.md`. v4 preserved as `methodology-kernel-v4.md` with `status: superseded` and `superseded-by: methodology-kernel.md (v5)`.
- **`workspace-structure.md` v3 → v4** — adds `open-issues/` directory structure replacing single `open-issues.md` file; adds archive-pack subdirectory convention under `provenance/NNN-title/archive/`; updates §SESSION-LOG.md to reflect thin-index-only form; adds cross-references to `read-contract.md`; documents archive-surface status of superseded specs. v3 preserved as `workspace-structure-v3.md` with `status: superseded`.
- **`validation-approach.md` v4 → v5** — adds Tier 1 checks 20 (default-read budget), 21 (archive-pack manifest integrity), 22 (archive-pack citation consistency); adds Tier 2 Q9 (read-contract adherence); adds §Gating Conventions (checks 20, 21, 22); adds honest-limit notes for new checks. v4 preserved as `validation-approach-v4.md` with `status: superseded`.
- **`engine-manifest.md`** — §2 declares `engine-v3` (was `engine-v2`); §3 adds `specifications/read-contract.md` to engine-definition file table; §7 history extended with new engine-v3 entry citing D-084 and listing spec changes. Frontmatter `last-updated: 2026-04-22` + `updated-by-session: 022`. engine-manifest.md's own version unchanged at v1 per Session 021 sub-pattern (documentary updates to a tracking spec do not bump the tracking spec).

### Prompts revised substantively

- **`prompts/development.md`** — lines 19, 25, 43 revised for default-read / archive distinction; cross-references `read-contract.md`. Prior version preserved via git history per `workspace-structure.md` §PROMPT.md convention.
- **`prompts/application.md`** — Read section revised analogously to preserve external-application portability of the read-contract; updates references to workspace-structure.md v4 and multi-agent-deliberation.md v4.

### Tooling

- **`tools/validate.sh`** substantive update:
  - New constants `READ_CONTRACT_ADOPTION_SESSION=22`, `DEFAULT_READ_HARD_WORD_CEILING=15000`, `DEFAULT_READ_SOFT_WORD_CEILING=10000`.
  - New check 20 (default-read surface per-file budget) with session-number gating and word-count measurement (frontmatter-excluded).
  - New check 21 (archive-pack manifest integrity) with SHA-256 hash verification; presence-gated on `provenance/*/archive/` existence.
  - New check 22 (archive-pack citation consistency) resolving `[archive: path]` references; skips placeholder references with angle-bracket tokens.
  - Check 1 updated to accept either `open-issues.md` (pre-R8b) or `open-issues/index.md` (post-R8b).
  - Tier 2 Q9 added to the printed guidance.

### Development-provenance files amended

- **`open-issues.md` → `open-issues/` directory** per R8b:
  - `open-issues/index.md` — thin default-read index (one line per OI, status summary, links to per-OI files).
  - `open-issues/OI-002.md` through `open-issues/OI-016.md` — per-OI files with lossless migration of original annotations.
  - `open-issues/resolved/OI-001.md`, `OI-003.md`, `OI-010.md`, `OI-017.md` — resolved OI files.
  - Pre-R8b `open-issues.md` archive-packed at `provenance/022-workspace-scaling-trajectory/archive/pre-R8b-open-issues/` (witness-preserved verbatim).
- **`SESSION-LOG.md`** restored to thin one-liner index per R8a:
  - Pre-session: 10,405 words (1 soft-warn breach of new 10,000-word check 20 soft threshold).
  - Post-restoration: ~2,000 words. Each session summary reduced to one-sentence decision-surface line.
  - Pre-R8a SESSION-LOG archive-packed at `provenance/022-workspace-scaling-trajectory/archive/pre-R8a-SESSION-LOG/` (witness-preserved verbatim).
  - Session 022's entry appended as thin one-liner naming D-084/D-085 and engine-v3.
- **`CLAUDE.md`** per R1 / E.1:
  - Mempalace R3 orchestrator-convenience paragraph removed (lines 14–29 of the previous text).
  - `### Multi-agent work` section retained with unchanged text (non-mempalace tool guidance).

### No external artefact this session

Session 022 is a self-development deliberation session producing engine-definition revisions. No external artefact produced; no `applications/` directory changes.

### Engine-version transition — engine-v2 → engine-v3

This is the methodology's **second engine-version increment** (after engine-v1 → engine-v2 at Session 021). First engine-v-bump to **add a new engine-definition file** to §3 (previous engine versions revised existing files only; engine-v3 adds `specifications/read-contract.md` v1).

Substantive changes at engine-v3 boundary per `engine-manifest.md` §5:
- New spec: `specifications/read-contract.md` v1.
- Revised specs: `methodology-kernel.md` v4→v5; `workspace-structure.md` v3→v4; `validation-approach.md` v4→v5.
- Revised prompts: `prompts/development.md`, `prompts/application.md` (both in-place revision; git-preserved history).
- Revised tool: `tools/validate.sh` (new checks 20/21/22 + new constants + Tier 2 Q9).
- engine-manifest.md itself: §2 + §3 + §7 updated; no own version bump (documentary update per Session 021 sub-pattern).

Unchanged at engine-v3 boundary: `PROMPT.md` dispatcher, `multi-agent-deliberation.md` v4, `identity.md` v2, `reference-validation.md` v2.

**Skeptic §5.4 engine-version cadence minority** (two engine-v-bumps in adjacent sessions) preserved as first-class minority with activation warrant at 3-consecutive-bump pattern or external-application portability confusion.

### Externally-loadable engine portability

Per `engine-manifest.md` §6 initialisation contract, an external-application workspace initialising from engine-v3 inherits:
- `PROMPT.md` (unchanged).
- `prompts/development.md` + `prompts/application.md` (both revised — Read instructions articulate default-read/archive distinction).
- `specifications/methodology-kernel.md` v5 (§1 Read revised).
- `specifications/multi-agent-deliberation.md` v4 (unchanged).
- `specifications/validation-approach.md` v5 (new checks + Q9).
- `specifications/workspace-structure.md` v4 (`open-issues/` directory; archive-pack subdirectory convention).
- `specifications/identity.md` v2 (unchanged).
- `specifications/reference-validation.md` v2 (unchanged).
- `specifications/read-contract.md` v1 (NEW).
- `specifications/engine-manifest.md` (declares engine-v3).
- `tools/validate.sh` (substantively updated).

External applications at engine-v3 get the read-contract from Session 001 of their workspace; they do not inherit this workspace's development-provenance archive-packs or per-OI files per the critical rule in engine-manifest.md §6 ("external application workspaces inherit the engine, not the engine's autobiography").

## Decisions made

- **D-084** — Adopt R1 through R11 read-contract minimum-coherent set; engine-v2 → engine-v3. Triggers: `[d016_1, d016_2, d016_3, d023_1, d023_2, d023_3]`. Non-Claude participation: Outsider OpenAI GPT-5.4 via `codex exec` as Shape A perspective (qualifies for OI-004 narrowing per v4 §Acceptable Participant Kinds).
- **D-085** — OI state housekeeping. OI-002 10th data point. OI-004 tally advances 7-of-3 → 8-of-3; voluntary:required rebalances 7:7 → 7:8; criterion-3 cumulative 55 → 60. OI-007 count unchanged at 12. Five first-class minorities §5.1–§5.5 preserved in `01-deliberation.md` with operational activation warrants. OI-015 positive exercise (4th). Triggers: `[none]`.

## Validation

`tools/validate.sh` at close: **PASS** — 571 pass, 0 fail, 1 warn (uncommitted changes in provenance/; expected — this session's work-in-progress). Pre-Session-022 baseline was 498 pass; Session 022 added +73 pass items from: existing checks 1–19 firing on Session 022's four-manifest deliberation + D-084 + D-085 + new spec + revised specs + new prompts + archive-packs; new check 20 firing on 33 default-read-surface files (all within budget; SESSION-LOG ~2K, open-issues/index.md ~500, specs and 03-close.md files all well under); new check 21 firing on 4 archive-pack manifests (pre-R8a-SESSION-LOG, pre-R8b-open-issues, 014-oi016-outsider, 022-outsider) all PASS SHA-256 match; new check 22 firing on archive-pack citation references (placeholder references correctly skipped).

### Tier 1 Structural Checks (notable post-Session-022 firings)

- Check 1: `open-issues/index.md exists (post-R8b directory form)` — PASS.
- Check 18: `(no oi-004-retrospective.md present; out-of-scope)` — correctly out-of-scope until a future session writes the artefact.
- Check 20: 33 default-read-surface files measured; all within 15,000-word hard ceiling; none exceed 10,000-word soft warning.
- Check 21: 4 archive-pack manifests; all hashes match (SHA-256 of concatenated chunks equals stored source_hash_sha256).
- Check 22: Archive references in default-read files resolve; placeholder references in spec text (angle-bracket tokens, literal "path") correctly skipped.

### Tier 2 Guided Assessment

1. **Provenance continuity (Q1).** Yes. Session 022's Read drew on Session 020 close (§5 minorities assessment); Session 021 close (audit dimensions + path presentation); kernel §1 Read v4 text; prompts/development.md lines 17-45 text; workspace-structure.md v3 §SESSION-LOG / §open-issues / §provenance text. Prior rejections re-cited with context (Session 020 Skeptic defer-entirely warrant satisfied; Session 019 Minimalist defer-revision posture inherited by Skeptic). No silent re-proposing of past rejections.

2. **Specification consistency (Q2).** Yes. `read-contract.md` v1's §1 enumeration is consistent with kernel v5 §1 Read cross-reference; workspace-structure.md v4 §SESSION-LOG / §open-issues / §provenance cross-reference read-contract.md; validation-approach.md v5 checks 20/21/22 reference read-contract.md §1/§5/§6/§7 respectively. prompts/development.md and prompts/application.md cross-reference read-contract.md consistently. Archive-pack manifests carry the required fields per read-contract.md §5. One consistency consideration: read-contract.md §4 originally specified "line-range only" boundary rule but Session 014 Outsider migration required byte-range due to very long single lines — spec text amended during execution to allow "mechanical-only" (line-range or byte-range) boundaries with manifest declaring which; this in-session amendment is recorded here for future audit.

3. **Adversarial quality (Q3).** Yes. Skeptic was genuinely adversarial: rejected frame entirely at Q1; rejected prompts revisions at Q2; rejected witness-pack spec at Q3; rejected all retroactive migration at Q4; narrowed SESSION-LOG restoration to prospective-only at Q5; rejected hard-gate at Q6; rejected §5.1 warrant drift at Q7; rejected no-grandfather at Q8; rejected engine bump at Q9. All four Skeptic objections (frame-as-laundering, threshold-arbitrariness, bootstrap-paradox, scope-in-one-session) engaged in the synthesis with mitigations recorded in §4. Skeptic's positions preserved as §5.1 and §5.4 minorities with operational activation warrants. Skeptic's defer-position addressed all three operator falsifiers (96K-word outlier via forward rule; kernel §1 unexecutability via return-to-spec; external-application inheritance via engine-version restraint).

4. **Meaningful progress (Q4).** Yes, substantively. The session addressed the scaling trajectory with specific changes: SESSION-LOG thinned from 10,405 to ~2,000 words (net-negative canonical-surface delta); open-issues directory split (per-OI reachability without full-file read); Session 014 extreme outlier archive-packed (fidelity preserved via copy-plus-reference); new read-contract.md specification defining the access discipline; validate.sh check 20 prevents future drift; kernel §1 Read no longer operationally unexecutable. Five first-class minorities preserved enable rollback on specific observable triggers.

5. **Specification-reality alignment (Q5).** Yes — strengthened. Pre-session: kernel §1 Read said "every file" but operators in practice used paginated reads (OI-015 laundering at harness layer per operator §3). Post-session: kernel §1 Read v5 names default-read surface + archive surface; what operators actually do matches what the spec says. `prompts/development.md` and `prompts/application.md` similarly aligned. Session 022's own §1 Tooling note ("paginated Read --offset... yields cleanly") is now spec-compliant because the read-contract explicitly authorises access-by-reference for over-budget material.

6. **Cross-model-honesty evidence (Q6).** Yes. Synthesis declares `cross_model: true`. Concrete evidence: Outsider manifest declares `participant_kind: non-anthropic-model`, `model_family: gpt`, `model_id: gpt-5.4`, `provider: openai`, `training_lineage_overlap_with_claude: independent-claim`, `participant_organisation: openai`, `independence_basis: organization-distinct`, `training_lineage_evidence_pointer: "unknown-but-asserted"`, `claude_output_in_training: unknown`. Transport notes record the `codex exec -c model_reasoning_effort=xhigh < /tmp/022-outsider-prompt.txt > /tmp/022-outsider-response.txt 2>&1` invocation; background task id `bmk9rdi27`; session id `019db521-775f-7872-9b38-f0c4b0094c28`; 46,382 tokens used; CLI banner preserved verbatim in archive-pack chunk 01. Outsider's bifurcation contribution ("broken read contract" as deeper frame; new-spec proposal for read-contract.md; aggregate-size discipline) qualitatively distinct from any Claude perspective.

7. **Trigger-coverage plausibility (Q7).** 
   - D-084 declares `[d016_1, d016_2, d016_3, d023_1, d023_2, d023_3]`. Reading D-084's Decision text: R4 modifies `methodology-kernel.md` (d016_1 + d023_1); R5 creates `read-contract.md` + R6 revises `workspace-structure.md` (both substantive, d016_2); R9 revises `validation-approach.md` substantively + revises `tools/validate.sh` substantively (d016_3 + d023_3). d023_2 (multi-agent-deliberation.md revision) is a borderline over-declaration — multi-agent-deliberation.md v4 itself unchanged at engine-v3, but read-contract.md §9 introduces close-time-obligation rules that affect how multi-agent-deliberation.md §Provenance Layout's raw perspective files are handled (the Session 022 Outsider archive-pack at close is the first exercise). Per Session 021 d016_1 over-declaration precedent, cautious over-declaration per honest-limit preference. Future sessions may re-examine if d023_2 should not have fired here.
   - D-085 declares `[none]`. Reading D-085's Decision text: records OI consequences without adding new normative content. OI-004 state unchanged at state 3 (no closure-retrospective attempted). `[none]` consistent per housekeeping precedent.
   - No `**Non-Claude participation:** skipped` annotations required (Outsider participated).

8. **OI-004 closure-retrospective substantive adequacy (Q8).** N/A this session — no `oi-004-retrospective.md` present. Session 022 does not attempt OI-004 state advance.

9. **Read-contract adherence (Q9; new in v5).**
   - (a) Default-read surface read at session open: orientation files read via paginated `Read --offset` per session-open §1 Tooling note in `00-assessment.md`; this is now spec-compliant at the post-session state because read-contract §1 enumeration includes files at any size and §4 authorises archive-pack access for over-budget material (even though at session open, SESSION-LOG and open-issues.md were pre-restoration sizes).
   - (b) Archive-surface records cited via `[archive: path]` convention: yes — Session 014 Outsider and Session 022 Outsider both cited in synthesis as archive references; pre-R8a SESSION-LOG and pre-R8b open-issues archive-packs cited in workspace-structure.md v4 and SESSION-LOG.md restoration note. Check 22 confirms references resolve.
   - (c) Non-reads declared in honest-limits: Session 022's synthesis honest-limits (§8 of 01-deliberation.md) names 9 specific items including session-open state numbers not independently verified and operator claim that §5.1 warrant satisfied (flagged as literal-text mismatch). No silent skips observed.

## Honest notes from the session

- **Workspace total word delta is POSITIVE** (676,879 → 840,956 = +164K words), driven primarily by Session 014 Outsider archive-pack (96K words of line-preservation duplication under copy-plus-reference discipline per D-017 immutability) + Session 022 provenance (~50K words) + other additions. **Default-read surface word delta is NEGATIVE** (~83K → 81,510 = -1.5K words). The operator's stated "net-negative workspace word delta" constraint is achieved at the default-read surface (the canonical orientation layer) but not at the total workspace level. This tension is fundamental: preserving immutable originals via copy-plus-reference (Conservator's load-bearing fidelity constraint) is additive by construction; the only way to achieve net-negative total is to delete originals, which violates D-017. Future sessions may consider a named exception for retroactive-migration-plus-archive cases if the aggregate tension becomes operationally binding. For Session 022, the spirit of the constraint (default-read burden reduced) is honored; the letter (total workspace reduction) is not.

- **Read-contract §4 boundary rule amended in-session** from "line-range only" to "mechanical only (line-range or byte-range; content-aware forbidden)." The Session 014 Outsider file exposed the need: line-range chunking of a 96K-word file produced chunks over 36K words because individual lines were up to 3,328 words long (codex exec reasoning-trace paragraphs). Byte-range chunking at 50KB produced 18 chunks each under 7,200 words. The spec was amended during R8c execution to reflect this; the amendment is a minor elaboration per OI-002 heuristic (clarification within existing scope of mechanical-only boundaries) and does not re-trigger engine-version bump beyond the already-declared engine-v3.

- **Word-count-vs-token-count discrepancy noted for future calibration**. My brief §2.2 and operator §3 cite token counts (SESSION-LOG 33,227 tokens; open-issues 27,437 tokens). The new check 20 measures words not tokens. Word counts for the same files: SESSION-LOG 10,405 words; open-issues 9,783 words. Ratio ~3.0× tokens-per-word for these prose-with-markdown files, not the 1.3× my synthesis §2.3 D2 calculation assumed. The 15,000-word hard ceiling therefore translates to ~45,000 tokens in Read-tool terms (far above the 25,000-token single-Read ceiling), not the ~19,500 tokens I stated. This is the Outsider's §5.3 minority concern materialised — the 15K-word budget is more permissive than my synthesis assumed. Session 023 audit should consider whether to tighten to 8,000-word hard ceiling per Outsider §5.3 on calibration grounds.

- **WX-22-1 through WX-22-5 watchpoints recorded** per synthesis §7 (laundering-as-codification; threshold-adjustment discipline; engine-version cadence; archive-pack location stress test; aggregate default-read surface growth). Session 023+ audits monitor these.

- **Session 022's own raws: three Claude perspectives remained as ordinary files; Outsider archive-packed**. Architect 01a (5,139 words per Session 022 post-commit count), Conservator 01b (3,712 words), Skeptic 01c (3,057 words) all under 15K-word ceiling; no archive-pack. Outsider 01d (22,611 words, dominated by CLI banner + echoed brief + reasoning traces + duplicate end-of-stream) exceeded ceiling; archive-packed per read-contract §9 with original file removed from provenance root. Skeptic's bootstrap-paradox concern (§5.1) does not materialise at this threshold: Session 023 reading Session 022's synthesis loads three ordinary raw files + archive manifest (small) + chunks for Outsider (4 chunks, largest 6,827 words — well under budget).

- **First codex invocation succeeded on first attempt this session.** Session 021 close noted the stdin-wait hang from argument-substitution form; Session 022 used stdin-pipe form (`codex exec ... < /tmp/prompt.txt > /tmp/response.txt 2>&1`) and succeeded on first launch. Background task id `bfutmoq27`; exit code 0. Session 021 transport lesson confirmed.

- **Outsider performed pre-response workspace exploration** (second session with this pattern after Session 021). Multiple `exec` tool calls reading CLAUDE.md, prompts/development.md, prompts/application.md, methodology-kernel.md, workspace-structure.md, engine-manifest.md, validation-approach.md, multi-agent-deliberation.md §Provenance Layout, tools/validate.sh, and provenance/014-oi016-resolution/01d-perspective-outsider.md structure. Per Outsider honest-limits this did not violate §10 anti-import. Pattern now n=2; stabilising toward routine behavior for codex exec with access to workspace files.

- **Cross-model contribution kind: spec-architecture frame-completion** (6th distinct kind across Sessions 005-022 per synthesis §6). The Outsider's proposal to house the read-contract in a dedicated new narrow-purpose specification (rather than in workspace-structure.md) is a frame-completion at the spec-architecture level — similar to Session 017 H4 (new engine-manifest.md spec) but applied to a different cross-cutting concern.

- **Brief-priming observation**: synthesis vocabulary was shaped by Outsider ("broken read contract", "default-read surface", "archive surface", "bounded working-set contract") rather than by operator ("canonical surfaces", "witnesses"). This reflects cross-family re-naming convergence. Less of the operator's original vocabulary is in the adopted spec text. Synthesizer's limit §6 flagged this; Session 023 audit should check whether the rename was substantively justified or was coordination-cost compromise.

- **OI-004 criterion-3 cumulative 60** across Sessions 005-022 (55 through Session 021 + 5 added Session 022 per synthesis §6). Criterion 4 remains articulated (state 3; no retrospective attempted).

## Next session

Session 023 should:

1. Run `tools/validate.sh` at start. Expected baseline: **571 pass, 0 fail, 0 warn**. Verify: checks 1-22 all pass; check 20 measures all default-read surface files under budget (SESSION-LOG.md, open-issues/index.md, specs, 03-close.md files); check 21 verifies SHA-256 integrity on 4 archive-packs (pre-R8a-SESSION-LOG, pre-R8b-open-issues, 014-oi016-outsider, 022-outsider) all match; check 22 resolves archive references (placeholder references in spec text correctly skipped).

2. Audit Session 022 synthesis fidelity. Particular attention to:
   - **WX-22-1 laundering-as-codification**: Session 023 is the first session after read-contract adoption. Check for any silent non-reads of archive-surface records relied on for load-bearing claims in Session 022's synthesis. Specifically, the synthesis cites `[01d-Q1]` etc. for Outsider positions — are those references verifiable against archive chunks 01-04 of `archive/022-outsider/`? If Session 023 cannot verify via archive read, the laundering pattern materialises.
   - **WX-22-2 threshold-adjustment discipline**: 15,000-word hard ceiling was adopted as compromise with Outsider's 8K minority preserved. Session 023 audit should note the word-count-vs-token-count discrepancy per honest-notes above — 15K words ≈ 45K tokens in Read-tool terms, which is ~1.8x the single-Read ceiling. Consider whether to tighten to 8K words or whether to reinterpret the ceiling. If tightening is proposed, it must be a separate deliberation (not a same-session adjustment) per §5.1 operational warrant (iii).
   - **Boundary-rule amendment**: the in-session amendment from "line-range only" to "mechanical only" in read-contract §4 was driven by the Session 014 Outsider execution necessity. Audit whether this amendment is coherent with the spec's surrounding logic, or whether it opens a different loophole.
   - **Session 014 archive-pack correctness**: verify chunk 4-6 (the large response-body chunks) contain the substantive Outsider response; verify chunk concatenation hash matches source.
   - **`d023_2` trigger declaration borderline case**: the synthesis declared d023_2 over-inclusively per honest-limit preference; audit whether it should have fired.

3. Open under no default pre-commitment. Present paths to operator (indicative; operator may steer differently):
   - **(A) Closure-retrospective draft for OI-004.** State 3 → state 4 attempt. D-023-triggering. WX-21-2 cross-model contradiction-prevailing data point verification can now rely on the expanded criterion-3 record (60 data points). D-023 cross-family required.
   - **(B) Cell 1 re-attempt of Session 019 R1-R5 (unexercised across four sessions: 020, 021, 022, and now 023-pending).** Minimalist defer-revision warrant has accumulated more session-count evidence.
   - **(C) Tighten read-contract §2 budget to 8,000 words per Outsider §5.3 minority.** Calibration-grounded per Session 022 close honest-notes (word-vs-token discrepancy). If adopted, engine-v4 warranted. §5.4 Skeptic cadence minority would activate if adopted at Session 023 (three engine-v-bumps in four sessions).
   - **(D) H4 first-exercise of external-application initialisation.** Now particularly relevant given engine-v3 introduced `read-contract.md` as a new inherited spec; fi