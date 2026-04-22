---
session: 022
title: Synthesis — Workspace Scaling Trajectory and Read-Contract Adoption
date: 2026-04-22
status: synthesized
synthesizer: claude-opus-4-7-orchestrator
participants_family: cross-model
cross_model: true
non_claude_participants: 1
oi004_qualifying_participants: [outsider]
anchor_commit_cited: 46f0baf
---

# Synthesis — Session 022

## 1. Deliberation summary

Session 022 deliberated the workspace-scaling trajectory brought to head by four observed facts: `SESSION-LOG.md` at 33,227 tokens (breaches the 25K single-read ceiling); `open-issues.md` at 27,437 tokens (also breaches); the 96,651-word `provenance/014-oi016-resolution/01d-perspective-outsider.md` extreme outlier; and Session 022's own session-open §1 Tooling note resolving the ceiling breaches via paginated `Read --offset` — a pattern the operator named as OI-015 laundering materialised at the harness layer [§3].

Four perspectives convened: Architect (constructive design advocate), Conservator (preservation-first fidelity tester), Skeptic (adversarial with operator's 3-falsifier burden on defer-positions), Outsider (OpenAI GPT-5.4 via `codex exec`, session id `019db521-775f-7872-9b38-f0c4b0094c28`, reasoning effort xhigh, stdin-pipe invocation per Session 021 lesson).

§5.4 Skeptic mempalace-non-use trigger 1 has materialised (Sessions 020, 021, 022 non-use). Operator ratified E.1 (remove CLAUDE.md R3 mempalace paragraph) and expanded scope to a broader scaling-trajectory deliberation.

This synthesis adopts a bounded-read-contract frame with specific refinements, creates a new narrow-single-purpose specification, bumps to `engine-v3`, and performs targeted retroactive migrations. Five first-class minorities are preserved with operational activation triggers.

## 2. Convergences and divergences

### 2.1 — Convergences (4-of-4 cross-family; all families, all perspectives)

**C1. E.1 — Remove CLAUDE.md R3 mempalace paragraph.** All four perspectives affirm the removal. Warrant §5.4 trigger 1 satisfied per non-use Sessions 020/021/022 [01a-Q7, 01b-Q7 §5.4, 01c-Q7 §5.4 "already ratified", 01d-Q7 §5.4 "subsumption"]. Independent concurrence.

**C2. SESSION-LOG.md restoration to thin index (§5.3 / §5.2 adoption).** All four perspectives affirm this restoration direction [01a-Q5a, 01b-Q5a, 01c-Q5a "narrowly", 01d-Q5 "yes on both"]. Warrant §5.3 (c) satisfied — file exceeds single-read ceiling within 5 sessions of R1 adoption [§5 brief]. The operator's observation that "canonical detail lives in `03-close.md`" holds per `workspace-structure.md` v3 §SESSION-LOG.md [§4.3 brief].

Variation in shape: Architect + Conservator + Outsider adopt "thin entries + full detail in 03-close.md"; Skeptic adopts narrower "banner note + go-forward discipline from Session 023, historical entries immutable." This shape-variance is below the convergence threshold — all four agree restoration direction; Skeptic's narrower shape is preserved as a bounding influence on the adopted mechanism (see R8e and §5.4).

### 2.2 — Convergences (3-of-4 cross-family; 2 Claude + 1 non-Claude)

**C3. Bounded-read-contract frame (versus operator's "canonical-vs-witness" as literally worded).** Architect [01a-Q1] "accept with refinement" (orientation-layer vs preservation-layer), Conservator [01b-Q1] "partial — accept tier distinction; reject 'witness' naming; reject 'canonical' overloading; propose 'active-layer' / 'preserved-layer'", Outsider [01d-Q1] "partially yes — deeper diagnosis is broken read contract; accept direction, reframe as bounded working-set contract." Skeptic [01c-Q1] rejects the frame categorically.

Cross-family: 2 Claude (Architect + Conservator) + 1 non-Claude (Outsider) accept with refinement. 1 Claude (Skeptic) rejects. **3-of-4 cross-family for the diagnosis; unanimous on renaming the operator's literal "canonical/witness" vocabulary** — no perspective adopts the operator's vocabulary verbatim as spec text. Operator's "canonical surfaces" creates terminology collision with existing `workspace-structure.md` v3 usage of "canonical" [01b-Q1]; "witness" connotes passive testimony rather than preserved-exact-text [01b-Q1, 01d-Q3].

**Synthesis vocabulary adopted:** "default-read surface" vs "archive surface" (Outsider's formulation) — both perspectives from Claude side offer refinements (orientation-layer/preservation-layer vs active-layer/preserved-layer); Outsider's is the most precise because it names the operational property directly (what gets read by default vs what gets read by reference). "Archive" is adopted over "witness" because it captures the preservation-with-explicit-access property without passive-testimony connotation.

**C4. Kernel §1 Read must be revised (d023_1 fires, engine-v3).** Architect, Conservator, Outsider all affirm [01a-Q2, 01b-Q2, 01d-Q2]. Skeptic rejects this session but agrees kernel revision would be appropriate at some point [01c-Q2 "if kernel §1 must be revised, it is not this session's work"]. Cross-family: same 3-of-4 composition.

Kernel text "every file, every specification, every provenance record" [§4.1 brief] is the specific contradiction. An external application inheriting engine-v2 kernel at 676K-word workspace-equivalent faces the same unexecutability. Leaving kernel unrevised while revising only `prompts/development.md` creates spec-layer contradiction forbidden by `prompts/development.md` line 39 ("Do not overwrite prior specifications silently").

**C5. `prompts/development.md` lines 19, 25, 43 revised.** Architect proposes specific text naming the orientation layer concretely [01a-Q2]; Conservator proposes text forcing explicit enumeration of preserved-layer non-reads [01b-Q2]; Outsider proposes text using "default-read surface" and "archived records" vocabulary [01d-Q2]. Skeptic rejects revision this session [01c-Q2]. Cross-family: 3-of-4.

**C6. `prompts/application.md` analogous revision.** Outsider [01d-Q2] "I would further align `prompts/application.md`, because its current Read section still says the full current state of the application workspace. If that text is left untouched, the engine exports the same contradiction to external applications." This concern raised by Outsider is not explicitly addressed by the Claude perspectives but implicit in the kernel-revision affirmation (if kernel revised, both `prompts/development.md` and `prompts/application.md` must align). **Synthesis treats this as 3-of-4 by implication** given Claude perspectives' agreement that engine-definition consistency is required.

**C7. `provenance/014-oi016-resolution/01d-perspective-outsider.md` retroactive migration this session.** Architect, Conservator, Outsider all yes [01a-Q4a, 01b-Q4a, 01d-Q4a]. Skeptic no [01c-Q4a "D-017 immutability country"]. Cross-family: 3-of-4.

Mitigation of Skeptic's immutability concern: migration via **copy-plus-reference** per Session 009 D-054 precedent [§4.5 brief] — original file stays untouched at its original path; archive-pack created alongside (location per R7 below); original remains discoverable for full-immutability readers. This meets Skeptic's load-bearing constraint (original unedited) while achieving Architect/Conservator/Outsider's migration goal (structured-access form exists).

**C8. Engine-v3 bump warranted.** Architect, Conservator, Outsider all affirm [01a-Q9, 01b-Q9, 01d-Q9]. Skeptic rejects [01c-Q9 "engine-v3 field becomes change-log timestamp rather than meaningful version artefact"]. Cross-family: 3-of-4.

Skeptic's concern preserved as §5.3 minority: versioning-frequency-as-churn watchpoint.

**C9. Trigger declaration `d016_1, d016_2, d023_1/2/3` agreed on full adoption set.** Same 3-of-4 composition with the same Skeptic opt-out contingent on "if minimal set adopted."

### 2.3 — Divergences — cross-family split

**D1. Witness-pack/archive-pack location** — session-local vs top-level.

| Perspective | Position | Rationale |
|---|---|---|
| Architect [01a-Q3] | Session-local `provenance/NNN-title/witnesses/<slug>/` | Locality; discoverability; avoids new top-level directory |
| Conservator [01b-Q3] | Session-local `<session-dir>/preserved/<basename>/` | Locality; session-reasoning stays together |
| Outsider [01d-Q3] | Top-level `witnesses/` or `archives/` directory | Respects provenance immutability; avoids adding files inside closed provenance directories |
| Skeptic [01c-Q3] | No position (rejects witness-pack) | n/a |

Cross-family: Claude 2 for session-local; non-Claude 1 for top-level; 1 Claude silent. **Not cross-family-majority either side.** The Outsider's immutability argument is load-bearing — adding subdirectories inside `provenance/014-oi016-resolution/` does modify that closed-session directory tree (git-visible change), which Session 009 D-054's `applications/` top-level precedent argues against.

Counter-argument per Architect/Conservator: `applications/` precedent introduced a top-level directory for **external artefacts**, not for preservation of session-internal material. Archive-packs are derivative-of-session-content; top-level storage severs session-affinity and introduces a new centralised-directory scaling problem (the same problem we are addressing!).

**Synthesis adopts session-local** (`provenance/NNN-title/archive/<slug>/`) per the Architect+Conservator locality argument, with two mitigations honoring Outsider:

1. **D-017 immutability preserved** via explicit rule: retroactive archive-pack creation does NOT modify any existing provenance file; new directories and files are created alongside. The working-tree change is an addition, not a modification. Git history records the addition in a new session's commit.
2. **Outsider's position preserved as first-class minority §5.1** with activation warrant: if per-session `archive/` subdirectories themselves become a scaling or discovery problem within 5 sessions of adoption, top-level `archives/` becomes the preferred revision direction.

Naming: "archive" adopted over "witnesses" (Outsider's C3 rationale) to name the property directly.

**D2. Budget value for canonical-surface hard-gate.** Architect 25K-token hard / 20K-token soft; Conservator 25K-token hard with word-count fallback; Outsider 8,000 words per file; Skeptic rejects hard-gate, accepts soft-warn at configurable word count.

Three of four accept a hard-gate in some form; one rejects. Cross-family: 3-of-4 for some hard-gate.

Metric divergence: tokens (Architect, Conservator fallback to words) vs words (Outsider, Skeptic soft-warn).

**Synthesis adopts word-count measurement** per Outsider's argument that the bash validator is word-count-based + stability across model versions [01d-Q6]; Conservator also endorses word-count fallback [01b-Q6]. **Synthesis adopts budget compromise: hard-fail at 15,000 words; soft-warn at 10,000 words.** Rationale:

- 25K tokens ≈ 19K words (Architect's effective hard ceiling at 1.3× approximation). 15K words leaves headroom below single-read-tool current ceiling.
- Outsider's 8K words is more conservative but may force witness-packing on currently-acceptable files (e.g., `reference-validation.md` at ~5K words is fine; `methodology-kernel.md` at ~1.5K words is fine; specs currently bounded). The goal is to prevent **future** drift, not force restructure of currently-acceptable files.
- 10K-word soft-warn provides early warning before canonical files approach hard-fail.

Outsider's 8K-word preference preserved as minority §5.2 (activation: if the 15K-word budget proves permissive enough that drift continues within 5 sessions, tighten to 8K).

**D3. Where the read-contract specification lives.** Architect + Conservator propose housing rules in `workspace-structure.md` v3 → v4 (add §active-layer enumeration). Outsider proposes new `specifications/read-contract.md` as a narrow-single-purpose spec. Skeptic rejects.

Cross-family: 2 Claude for workspace-structure; 1 non-Claude for new spec; 1 Claude rejects.

Outsider's argument [01d-Q3]: "This is cross-cutting enough that burying it in `workspace-structure.md` would make the rule hard to follow and easy to drift." The read-contract touches kernel §1 Read semantics (kernel-level), validation check semantics (validation-approach), prompts execution semantics (prompts/), and spec-filing semantics (workspace-structure). Housing rules in any single file buries cross-cutting concerns.

Precedent analysis: the OI-002 narrow-single-purpose-spec pattern is established at n=3 (`identity.md`, `reference-validation.md`, `engine-manifest.md`) — all three originated from cross-family deliberations where the Outsider was a significant contributor (Sessions 012, 014, 017 respectively). Adding a 4th narrow-purpose spec (`read-contract.md`) is within pattern.

**Synthesis adopts the Outsider's proposal — create new `specifications/read-contract.md` v1** — per the cross-cutting-concern argument + precedent of Session 017 engine-manifest.md (also Outsider-frame-completion). This is a frame-completion contribution kind (5th distinct kind after Session 014 structural innovation, Session 017 frame-replacement, Session 019 textual precision, Session 020 type-drift, Session 021 structural bifurcation) — the 6th instance.

Workspace-structure.md receives a minor cross-reference to `read-contract.md` (no v-bump necessary per OI-002 heuristic — a pointer is elaboration within scope).

**D4. `open-issues.md` restructure scope.** Architect: partial (long-annotation migration, keep file structure). Conservator: partial (per spec anticipation clause, split into `open-issues/` directory). Outsider: yes (via same spec anticipation clause). Skeptic: no (strict §5.1 warrant not met).

Cross-family: 2 Claude + 1 non-Claude for some restructure; 1 Claude against. Specific convergence: Conservator + Outsider both point at `workspace-structure.md` §open-issues.md's existing "unless the number of issues makes a single file unwieldy" authorization clause [§4.4 brief].

**Synthesis adopts Conservator + Outsider convergence**: exercise the existing spec anticipation clause. Split `open-issues.md` into `open-issues/` directory with `index.md` (thin index, ≤5K words) + `OI-NNN.md` files (one per issue, each well under budget). This does not require new spec language beyond a minor edit to `workspace-structure.md` §open-issues.md clarifying the directory layout.

Skeptic's "§5.1 strict warrant not met" concern honored: the split is **not** adoption of the §5.1 minority rollback direction (strict 50K-token threshold unmet); it is exercise of the already-present spec anticipation clause, which has its own independent warrant ("unwieldy" is a shape-test, not a size-test).

**D5. Superseded spec copies reclassification.** Architect, Conservator, Skeptic: No (3 Claude). Outsider: Yes (reclassify as archive-surface immediately per engine-manifest §4).

Cross-family: 3 Claude against (existing `-vN.md` convention works) vs 1 non-Claude for.

**Synthesis adopts 3-of-4 Claude position**: defer reclassification of superseded spec copies. Existing convention (`-v1.md`, `-v2.md` suffix; `supersedes:` frontmatter chain) is adequate; no current scaling pressure on superseded specs (each is ≤5K words; aggregate 9 files; all preservation-layer by type).

Outsider's position preserved as minority §5.5 with activation warrant (if a future session cites a superseded spec as active-canonical because the frontmatter `status: superseded` was not honored, the reclassification-first direction becomes preferred).

### 2.4 — 4-of-4 divergence — Epoch-index consolidation (operator candidate #4)

Conservator rejects as drafted (summarisation disguised as witness); accepts only if redefined as purely navigational [01b-Q4f]. Architect defers [01a-Q4f]. Outsider defers [01d-Q4f]. Skeptic rejects categorically [01c-Q4f].

**Synthesis rejects operator candidate #4 as drafted.** Adopted instead: **not this session.** If a future session proposes epoch-consolidation, it must be (i) navigational only (link-table, no synthetic content per Conservator's load-bearing redefinition), and (ii) its own dedicated deliberation, not combined with other scaling work.

Operator's candidate #4 was an explicit input requested for deliberation; the unanimous cross-perspective rejection is signal, not error.

## 3. Cross-family weighting check (per Session 019 close precedent)

Per the discipline established in Sessions 019/020/021, cross-family majority on a macro-question does not transfer automatically to every specific content sub-question.

**Macro-question "adopt read-contract frame":** 3-of-4 cross-family (Architect + Conservator + Outsider vs Skeptic). Both families represented on adoption side. Outsider's contribution is substantively distinct (broken-read-contract diagnosis; new-spec proposal) not derivative-vote; Claude perspectives' refinements (vocabulary; protocol-fidelity; location) are substantively distinct too. This is affirmatively cross-family, not cross-family-shaped coincidence.

**Macro-question "engine-v3 bump":** 3-of-4 cross-family. Same composition. Same cross-family honesty check applies.

**Sub-question divergence tracking:** D1, D2, D3, D4, D5 above each tracked separately. Synthesis does NOT claim cross-family warrant for sub-question resolutions that rely on Claude-majority alone (D2 budget value, D5 superseded-spec reclassification), preserving Outsider positions as first-class minorities with activation warrants.

**Sub-question D3 (new spec location) — 2 Claude + 1 non-Claude vs 1 non-Claude alone:** adopted per cross-family honesty (non-Claude in majority; Outsider's cross-cutting argument load-bearing; Claude dissent is the rejecter Skeptic who rejects the frame entirely).

## 4. Anti-laundering check on the adoption aggregate (Session 014 Skeptic Q7 test applied)

Does the adopted set **widen what counts as pass**?

**Test 1: "Laundering-as-codification" — Skeptic's Q1 objection.** Does adopting "archive surface" as legitimate spec text codify the harness-layer routing that OI-015 named as laundering?

Mitigation: the read-contract spec (R5) specifies that archive access requires explicit reference — a reader reading an archived record MUST name the record and cite the chunk; unacknowledged non-reads are validator-detected (check 22; see R9 addendum). The Skeptic's strongest objection ("witness dumping becomes satisfy-by-pointing") is blocked by the **enumeration requirement** in prompts/development.md line 25 revised text (per Conservator [01b-Q2]): "enumerate the preserved-layer records relevant to the session's subject matter; for each, either read it in full or declare in an honest-limits section why it was not read and what gap that leaves."

The laundering-as-codification risk is addressed at the enforcement level, not just the conceptual level. Non-reading becomes a declared action, not a silent action. **Mitigation holds.**

**Test 2: "Threshold-arbitrariness" — Skeptic's Q3 objection.** Does any threshold choice (15K hard; 10K soft; 8K Outsider-minority) bake in a tunable-in-favor trigger?

Mitigation: thresholds are in `tools/validate.sh` as named constants with explicit session-adoption comments (per check 16/17/18/19 precedent). Threshold changes are spec revisions requiring their own deliberation. Session 020 §5.1 warrant-drift concern (operator's 50K-token claim vs 27K actual) is honored: §5.1 warrant text **not** re-revised this session; §5.1's strict warrant preserved; the open-issues split is exercised via the existing spec anticipation clause, not by softening §5.1.

**Mitigation partial.** Skeptic's concern that future sessions might tune thresholds in favor is not fully blocked. Preserved as watchpoint WX-22-2 (threshold-adjustment discipline).

**Test 3: "Bootstrap paradox" — Skeptic's Q8 objection.** Does Session 022 witness-packing its own raws create a re-read problem for Session 023+?

Mitigation: thresholded application per Outsider [01d-Q8]. Session 022's own raw perspectives at 3,200 + 4,000 + 3,500 + 22,000 words respectively. Only the Outsider (22,428 words) exceeds the 15K hard budget. Session 022's close action: witness-pack **only** the Outsider perspective; Architect/Conservator/Skeptic perspectives remain as ordinary raw-perspective files at their original paths. Session 023 reading the deliberation record loads ordinary raws for three perspectives + archive manifest (small) + response-body chunk for Outsider (the response body is ~8K words — a single chunk under budget).

**Mitigation holds** with the thresholded-application refinement. The bootstrap paradox materialises only if everything is witness-packed; thresholded packing avoids it.

**Test 4: "Scope-in-one-session" — Skeptic's Q9 objection.** Two engine bumps (v2 in Session 021; v3 in Session 022) in consecutive sessions make engine-version a change-log timestamp.

Mitigation: partial. The sessions are consecutive, but the changes address distinct concerns (Session 021: OI-004 criterion-4 articulation — OI-specific; Session 022: read-contract frame — structural). Engine-manifest.md §5 specifies version bumps are triggered by substantive file changes; it does not specify a minimum-session-gap. Skeptic's concern is load-bearing but the spec does not prohibit the adjacent bumps.

**Mitigation partial.** Preserved as §5.3 minority (version-bump cadence watchpoint).

**Aggregate assessment:** The adoption passes anti-laundering check on tests 1 and 3 (fully) and tests 2 and 4 (partially, with specific watchpoints and minorities recorded). No test is failed outright. The adopted set does not lower any existing threshold, does not drop any existing check, does not soften any mechanism-failure criterion; it adds new checks (20, 21, 22) and new normative content (read-contract.md).

## 5. Recommendations

### R1 — Remove `CLAUDE.md` R3 mempalace paragraph (E.1)

Unanimous 4-of-4. §5.4 Skeptic mempalace-non-use trigger 1 satisfied. CLAUDE.md lines 14–29 deleted; the Session 020 D-080 text is preserved in Session 020's `03-close.md` and in this session's `02-decisions.md` for continuity.

### R2 — Adopt bounded-read-contract frame

3-of-4 cross-family. The workspace artefact set is governed by an **access discipline** distinguishing:
- **default-read surface** — the bounded set of files read in full at every session open.
- **archive surface** — immutable exact-text records preserved verbatim and accessed by explicit reference, not default-read.

The distinction cuts across the existing engine-definition / development-provenance / application-scope file classes [workspace-structure.md v3 §File classes]; it is a separate access-discipline dimension.

Outsider's "bounded working-set contract" diagnosis [01d-Q1] accepted as the frame's own rationale: the frame exists because the methodology's normative read obligation and operational read mechanism have diverged; the read-contract re-aligns them.

### R3 — Revise `prompts/development.md` lines 19, 25, 43

Substantive revision. Prior version preserved as `prompts/development.md` renamed to git-preserved previous-commit reference (prompts/ directory historically uses git-preservation rather than v-suffix per workspace-structure.md §PROMPT.md v3 "significant event" convention).

**Line 19 adopted text** (synthesis of Architect's precision + Conservator's enumeration-discipline + Outsider's vocabulary):

> "Begin by reading the workspace's default-read surface completely: the active specifications (per `specifications/engine-manifest.md` §3), the current `SESSION-LOG.md` index, the current `open-issues/index.md`, and each prior session's `03-close.md`. Then enumerate the archive-surface records relevant to this session's subject matter; for each, either read it in full via its archive manifest + chunk references, or declare in the session's honest-limits section why it was not read and what gap that leaves."

**Line 25 adopted text** (per Conservator's loophole-closing structure):

> "Before doing any substantive work, consult the workspace's record of prior decisions: `SESSION-LOG.md` entries, `open-issues/` status files, and — for any decision load-bearing to this session's work — the relevant `02-decisions.md` and any archive-surface records it references. If an idea was considered and rejected earlier, do not silently re-propose it."

**Line 43 adopted text** (per Conservator's preservation-primary + Architect's mechanism-distinction):

> "Preserve all provenance. Do not delete, silently compress, or summarise historical records. When a record exceeds the default-read budget configured in `specifications/read-contract.md`, preserve it as an immutable archive-pack with byte-identical preservation, a pointer-only manifest, integrity hashes, and stable references from the default-read surface."

### R4 — Revise `methodology-kernel.md` v4 → v5 §1 Read

Substantive revision; d023_1 fires; engine-v3 triggered. v4 preserved as `methodology-kernel-v4.md` status: superseded.

**Proposed §1 Read revision:**

> Absorb what the session will reason from before changing anything. In every session this includes **workspace reading** of the default-read surface — the active specifications, the `SESSION-LOG.md` index, `open-issues/index.md`, and prior sessions' `03-close.md` records — in full. The archive surface (raw perspective records, superseded spec versions, over-budget annotations preserved as archive-packs per `specifications/read-contract.md`) is read by explicit reference as the session's work requires; it is not default-read. Build a complete picture of the workspace's default-read surface and of any archive-surface material the session depends on.

(Rest of §1 — domain reading paragraph; receptive-activity line — unchanged.)

### R5 — Create `specifications/read-contract.md` v1

New narrow-single-purpose specification. Outsider frame-completion contribution. n=4 in the OI-002 narrow-spec pattern (after identity.md, reference-validation.md, engine-manifest.md).

Content sections (normative):

1. **Purpose.** Defines the access discipline distinguishing default-read surface from archive surface; specifies budgets, archive-pack structure, integrity mechanisms, and reference conventions.

2. **Default-read surface enumeration.** Explicit list:
   - Every active-status `.md` file in `specifications/`.
   - `SESSION-LOG.md`.
   - `open-issues/index.md` (post-R8 split).
   - Every `provenance/NNN-title/03-close.md`.
   - Every current-session provenance file (within the active session only, while it is open).
   - `PROMPT.md`, `prompts/development.md`, `prompts/application.md`.

3. **Archive surface enumeration.** By exclusion: anything preserved in the workspace but not on the default-read enumeration.

4. **Default-read budget.** Per-file hard ceiling: 15,000 words. Per-file soft-warn: 10,000 words. Measurement: word count via `wc -w` on body content (frontmatter excluded). Rationale: word count is stable across tokenisers; approximation to current 25K-token Read ceiling is conservative (15K words ≈ 19.5K tokens at 1.3× ratio). Constants encoded in `tools/validate.sh`.

5. **Archive-pack structure.** Directory located at `provenance/NNN-title/archive/<slug>/` (session-local; D-017 immutability preserved via new-files-only rule). Contents:
   - `manifest.yaml` — frontmatter + chunk table + integrity fields; no summary content.
   - `00-source.md` — byte-identical copy of the original file if under per-chunk budget; OR
   - `01-chunk.md`, `02-chunk.md`, ... — numbered chunks if multiple; line-range boundaries only (no content-aware splits).
   
6. **Archive-pack manifest fields** (YAML):
   ```yaml
   archive_id: <stable identifier>
   originating_session: <NNN>
   originating_path: <relative path>
   migrated_in_session: <NNN>
   kind: raw-perspective | over-budget-annotation | superseded-spec | other-named
   total_bytes: <integer>
   total_words: <integer>
   chunk_count: <integer>
   chunk_boundary_rule: line-range | single-file
   source_hash_sha256: <hash of full concatenation>
   chunks:
     - ordinal: 1
       file: 01-chunk.md
       line_range: "1-500"
       chunk_hash_sha256: <hash>
     - ordinal: 2
       file: 02-chunk.md
       line_range: "501-1000"
       chunk_hash_sha256: <hash>
   readers_note: <1-3 sentences; what the archive preserves; when to consult it>
   ```

7. **Reference conventions.** Default-read files cite archive records as:
   ```
   [archive: provenance/<NNN-title>/archive/<slug>/]
   ```
   With optional chunk-level:
   ```
   [archive: provenance/<NNN-title>/archive/<slug>/#chunk-02]
   ```
   Readers resolving the reference read `manifest.yaml` first, then relevant chunks. The manifest's `readers_note` guides "when to read what."

8. **Integrity guarantee.** The `source_hash_sha256` field in the manifest is computed against the canonical concatenation of chunks in numerical order. `tools/validate.sh` check 21 verifies on every run. D-017 immutability: once the migrating session closes, archive files are immutable; any revision requires a new migrating session with its own decision record.

9. **Close-time obligation for current-session raws.** At session close, the orchestrator measures each raw perspective file and each provenance file in the current session directory. Any file exceeding the per-file hard ceiling (15,000 words) is archive-packed before session close. `SESSION-LOG.md` entry for the session names the archive-pack presence.

10. **Versioning.** v1 established Session 022. Subsequent revisions per OI-002 substantive-vs-minor heuristic.

**Validation** (spec §Validation section):
1. Every file in §2 enumeration exists and is ≤ per-file hard ceiling.
2. Every file not in §2 enumeration and not covered by §3 exclusion clarifications is in violation.
3. Every archive-pack has a well-formed `manifest.yaml` with all required fields.
4. Every archive-pack's `source_hash_sha256` matches the actual hash of concatenated chunks.
5. Every default-read file citing an archive reference uses the `[archive: path]` convention.

### R6 — Revise `workspace-structure.md` v3 → v4 (minor)

Minor amendment (per OI-002 heuristic — pointer and cross-reference additions within existing scope, no new normative content).

- Add a cross-reference in §open-issues.md noting the directory layout enforced post-R8.
- Add cross-reference in §specifications noting superseded-version discipline unchanged (engine-manifest.md §4 + existing `-vN.md` convention; no archive-pack requirement).
- Add cross-reference to `specifications/read-contract.md` in the top-matter.

No v-bump would typically be required for a pointer-only amendment. However, coupling with other engine-v3 changes and the open-issues directory creation makes this **substantive in aggregate** per OI-002 precedent of Session 017 D-074 (workspace-structure v2 → v3 was substantive in that bump due to file-class distinction addition). Synthesis declares **v3 → v4 substantive** to pair with open-issues directory creation. v3 preserved as `workspace-structure-v3.md`.

### R7 — Revise `prompts/application.md` analogously

Substantive revision (parallel to R3). Line-by-line alignment with R3's default-read / archive distinction in the application-prompt context. Outsider's C6 concern addressed: external applications inherit the revised read-contract.

Prior version preserved via git (per workspace-structure.md §PROMPT.md convention).

### R8 — Canonical-surface restoration this session

**R8a — `SESSION-LOG.md` to thin one-liner index.** Per Conservator's lossless-migration protocol [01b-Q5a]:

1. For each session row (001-021) where the summary column exceeds a "brief index" target (≤200 words), verify the corresponding `03-close.md` file contains the detail.
2. Where detail is missing from `03-close.md`, copy verbatim from SESSION-LOG to a new section in that `03-close.md` before thinning.
3. Thin SESSION-LOG entries to Session-number | Date | Title | one-sentence decision-surface summary.
4. Preserve the pre-R8a version of SESSION-LOG.md as `provenance/022-workspace-scaling-trajectory/archive/pre-R8a-SESSION-LOG/` archive-pack for reference.

Target SESSION-LOG size post-R8a: ~3-5K words (22 rows × ~200 words table-header + summaries).

**R8b — `open-issues.md` → `open-issues/` directory.** Exercise existing spec anticipation clause [§4.4 brief]. Structure:

```
open-issues/
  index.md              — thin overview + list of OIs with status + one-line summary each
  OI-002.md
  OI-004.md
  OI-005.md
  OI-006.md
  OI-007.md
  OI-008.md
  OI-009.md
  OI-011.md
  OI-012.md
  OI-013.md
  OI-014.md
  OI-015.md
  resolved/
    OI-001.md
    OI-003.md
    OI-010.md
    OI-016.md
    OI-017.md
```

Each OI-NNN.md carries the current content + historical annotations verbatim (lossless migration per Conservator's protocol). `index.md` under 5K words. Per-OI files vary.

`open-issues.md` at the workspace root is deleted after migration; `open-issues/index.md` becomes the default-read target. `workspace-structure.md` v3 → v4 minor amendment (R6) names the new location.

**R8c — Session 014 Outsider archive-pack migration.**

Source: `provenance/014-oi016-resolution/01d-perspective-outsider.md` (96,651 words).

Destination: `provenance/022-workspace-scaling-trajectory/archive/014-oi016-outsider/`.

Migration: copy-plus-reference per Session 009 D-054 precedent. Original stays untouched; archive created alongside. Chunk boundaries: line-range only per Conservator [01b-Q4a]. Chunk size target: ≤10,000 words per chunk (below soft-warn to leave readers breathing room).

Expected chunk count: ~10 chunks for the 96,651-word file.

Archive lives at Session 022's provenance directory because that's the **migrating** session; Session 014's directory is unmodified.

Reference from Session 014's `03-close.md` added as minor note: "The Outsider perspective for OI-016 deliberation was archive-packed in Session 022 per read-contract R8c; see `provenance/022-workspace-scaling-trajectory/archive/014-oi016-outsider/`." This is the only cross-reference added; no other Session 014 file is modified.

**R8d — Other over-threshold raws: defer with enumeration.**

`tools/validate.sh` new check 20 (R9) produces an enumerated list of over-threshold files at session close. This list becomes the migration queue for Session 023+.

**R8e — Superseded specs: defer.** No action this session.

**R8f — Epoch-index consolidation: rejected as drafted.** See §2.4.

### R9 — `tools/validate.sh` Tier 1 new checks

**Check 20 — Default-read surface budget (per-file).**
- Iterates `read-contract.md` §2 enumeration. For each file, measures `wc -w` on body content. Fails if > 15,000 words; warns if > 10,000.
- Constants `DEFAULT_READ_HARD_WORD_CEILING=15000`, `DEFAULT_READ_SOFT_WORD_CEILING=10000`, `READ_CONTRACT_ADOPTION_SESSION=22`.
- Gated: session-number ≥22 (post-adoption).

**Check 21 — Archive-pack manifest integrity.**
- Iterates `provenance/*/archive/*/manifest.yaml`. For each: verifies required fields present; verifies `source_hash_sha256` matches actual hash of concatenated chunks.
- Presence-gated (fires only if any archive-pack exists).

**Check 22 — Archive-pack citation consistency.**
- For every archive-surface file referenced from a default-read file, verify the reference resolves (path exists, chunk ordinals exist).
- Catches broken archive references from spec text or 03-close.md.
- Presence-gated.

**Validation-approach.md v4 → v5** paired Tier 2 question Q9 (new):

> Q9. Read-contract adherence. For this session's work, verify: (a) the default-read surface enumeration in `read-contract.md` was actually followed — every enumerated file was read at session open; (b) any archive-surface records relied on for load-bearing claims are cited via the `[archive: path]` convention in default-read files; (c) any non-reads of relevant archive records were declared in the session's honest-limits section. Flag silent skips — these are the harness-layer laundering pattern `read-contract.md` exists to prevent.

### R10 — Engine-v3 declaration

`engine-manifest.md` updated:
- §2: `engine-v3` (was `engine-v2`).
- §3: add `specifications/read-contract.md` to the file table.
- §7: new history entry naming Session 022 D-084 as the bump driver; listing all revised specs + validate.sh + prompts.
- Frontmatter: `last-updated: 2026-04-22` + `updated-by-session: 022`.

Engine-manifest.md itself: documentary update only (no v-bump per Session 021 sub-pattern).

### R11 — OI housekeeping

- **OI-002:** tenth data point (R3/R4/R6/R7 substantive; R5 creation pattern continues at n=4; R9 check additions substantive; multi-spec revision batch). Heuristic holds stable.
- **OI-004:** tally advances 7-of-3 → 8-of-3 (D-084 fires d023_1 + d023_2 + d023_3 — eighth required-trigger deliberation with non-Claude participation). Criterion-3 cumulative 55 → 60 (5 new Outsider contributions this session: broken-read-contract diagnosis; bounded-working-set-contract framing; new-spec proposal for read-contract.md; aggregate-size discipline; prompts/application.md export-consistency concern). Voluntary:required ratio 7:7 → 7:8 (required overtakes voluntary; second such session after Session 017).
- **OI-007:** count 12 → 12 (no OI opened or resolved). Five new first-class minorities held in deliberation §5 rather than as new OIs per Session 015/019/020/021 precedent.
- **OI-015:** Session 022 is a **positive exercise** of the laundering-gap reconciliation — operator input surfaced verbatim in brief §3; each perspective treated it as input to be surveyed; kernel §1 Read revision (R4) is itself the response to the laundering-at-harness-layer finding the operator raised. Monitor continues.

## 5. First-class minorities preserved

### §5.1 — Skeptic "reject frame entirely" minority

**Position** [01c-Q1, Q9]: the bounded-read-contract frame codifies the OI-015 harness-layer laundering pattern rather than repairing it; engine-v3 bump in the session adjacent to engine-v2's adoption makes the engine-version field a change-log timestamp; the alternative diagnosis ("one anomalous file, growth rate, unbounded kernel clause") warrants narrower remedies (per-artefact size rule; session-close growth budget; kernel §1 clarification).

**Operational warrant.** Minority becomes preferred revision direction if any of the following:

(i) A future session cites an archive reference as satisfying kernel §1 Read without reading the archived content — the "witness dumping" laundering pattern materialises. Concrete form: a session's honest-limits section names an archive record as "sufficient to rely on via manifest alone" for a load-bearing claim.

(ii) Two consecutive engine-version bumps occur in adjacent sessions after engine-v3 (i.e., engine-v3 → engine-v4 in Session 023, engine-v4 → engine-v5 in Session 024), confirming the version-churn concern.

(iii) The 15K-word hard ceiling is tuned in any direction within 3 sessions, confirming the threshold-arbitrariness objection.

### §5.2 — Outsider minority on archive-pack location (top-level `archives/`)

**Position** [01d-Q3]: archive-packs should live at top-level `archives/` or `witnesses/` to respect provenance immutability more cleanly than adding subdirectories to session-local provenance folders.

**Operational warrant.** Minority becomes preferred revision direction if any of:

(i) Three or more sessions' per-session `archive/` subdirectories become a discovery problem — e.g., a session needs to find all archive-packs of a certain kind and has to scan every session directory.

(ii) Session-local archive discipline fails to prevent a modification of a closed session's directory (e.g., a session accidentally edits the original migrated file while creating the archive-pack alongside, breaking D-017 immutability).

(iii) External-application workspaces inheriting read-contract.md report confusion about archive location (the per-session pattern does not transfer cleanly to external-application provenance structure).

### §5.3 — Outsider minority on default-read budget (8,000 words)

**Position** [01d-Q6]: 8,000-word per-file budget is the right conservative value; 15,000 words is too permissive and may allow drift to resume.

**Operational warrant.** Minority becomes preferred revision direction if any of:

(i) Within 5 sessions of R5 adoption, any default-read file exceeds 10,000 words (the soft-warn threshold) without subsequent migration. Confirms 15,000 hard ceiling is permissive-enough that drift resumes.

(ii) A session emerges where a default-read file at 12,000-15,000 words is cited as satisfying the budget but causes a reader burden equivalent to pre-R5 33K-token SESSION-LOG friction. Confirms the budget is calibrated to file-size rather than aggregate-reading-burden.

(iii) Outsider's aggregate-development-provenance-size warning [01d-Q6] materialises: the total default-read set exceeds some reasonable aggregate budget (e.g., 100K words total) even though each individual file is under 15K.

### §5.4 — Skeptic "engine-version adjacency" minority

**Position** [01c-Q9]: two engine bumps in adjacent sessions (v1→v2 Session 021; v2→v3 Session 022) convert the engine-version field into a change-log timestamp. A minimum-session-gap discipline between engine bumps would protect the field's meaning.

**Operational warrant.** Minority becomes preferred revision direction if any of:

(i) engine-v3 is bumped to engine-v4 within Sessions 023-025. Confirms cadence concern.

(ii) An external application loading engine-v2 faces portability-loss because it does not know whether to also load engine-v3 changes, or vice versa; the version-frequency creates ambiguity.

### §5.5 — Outsider minority on superseded-spec reclassification

**Position** [01d-Q4c]: superseded specs should be reclassified to archive surface immediately per `engine-manifest.md` §4's existing exclusion; the current `-vN.md` convention is effective but the discipline is "by-suffix-naming" rather than "by-explicit-classification."

**Operational warrant.** Minority becomes preferred revision direction if any of:

(i) A future session cites a superseded spec (e.g., `multi-agent-deliberation-v3.md`) as active-canonical because the frontmatter `status: superseded` was overlooked. Confirms classification-by-suffix is insufficient.

(ii) The aggregate word count of superseded spec copies in `specifications/` becomes its own scaling surface (e.g., aggregate > 30K words).

## 6. Cross-model contributions (per v4 §Closure Criteria criterion 3)

**Five concrete Outsider-sourced contributions materially shaped adopted Session 022 content:**

1. **"Broken read contract" diagnosis** as deeper frame than operator's "two artefact kinds" [01d-Q1]. Shapes R2's framing rationale and R5's decision to house rules in a dedicated new spec. No Claude perspective produced this diagnosis — Architect accepted operator frame; Conservator refined vocabulary; Skeptic rejected frame.

2. **"Bounded working-set contract" reframing** at Q1 [01d-Q1]. Names the operational property (working-set bound) rather than the artefact-type (canonical/witness). Shapes R2's descriptive text. Claude perspectives stayed within artefact-type framing.

3. **Proposal for new `specifications/read-contract.md`** as dedicated narrow-single-purpose spec [01d-Q3]. Cross-cutting-concern argument. Adopted as R5. Architect and Conservator both placed rules in workspace-structure.md; Outsider's separate-spec proposal has Session 017 engine-manifest.md precedent (also Outsider-proposed new-spec).

4. **Aggregate-size discipline** beyond per-file budget [01d-Q6]: "Per-file control alone is not sufficient if the default-read set keeps growing by accretion." Shapes §5.3 minority warrant (iii); potential R9 check 20 extension to aggregate-set reporting.

5. **`prompts/application.md` export-consistency concern** [01d-Q2]: "If that text is left untouched, the engine exports the same contradiction to external applications." Shapes R7 (analogous revision). Claude perspectives did not surface this explicitly.

**Cross-model contribution kind**: frame-completion at the spec-architecture structural level (creating a new spec to house cross-cutting concerns). This is the 6th distinct kind across Sessions 005-022: split-resolving third-way (009/010/011); structural innovation (014); frame-replacement at concept level (017); textual precision (019); type-drift diagnosis (020); structural bifurcation (021); **spec-architecture frame-completion (022)**.

**Criterion-3 cumulative**: 55 (through Session 021) + 5 (Session 022) = **60** across Sessions 005–022. Criterion 4 remains articulated (state 3; no retrospective attempted this session).

**Novel data pattern**: Outsider performed pre-response workspace exploration (multiple `exec` tool calls reading `CLAUDE.md`, `prompts/development.md`, `prompts/application.md`, `methodology-kernel.md`, `workspace-structure.md`, `engine-manifest.md`, `validation-approach.md`, `multi-agent-deliberation.md`, `tools/validate.sh`, `provenance/014-oi016-resolution/01d-perspective-outsider.md`). This is the **second session** with this pattern (after Session 021); pattern is now n=2, stabilising toward routine. Per Outsider honest-limits [01d Honest Limits], workspace-read is not pretraining-import and does not violate §10 anti-import.

## 7. Watchpoints recorded Session 022

**WX-22-1 — Laundering-as-codification watchpoint** (Skeptic §5.1 adjacent). Track whether read-contract adoption produces a session citing an archive reference to satisfy kernel §1 Read without reading the archived content. Audit surface: Session 023+ honest-limits sections; archive-reference citation patterns.

**WX-22-2 — Threshold-adjustment discipline** (Skeptic §5.1(iii)). Track whether the 15K-word hard ceiling or 10K soft-warn is tuned in any direction within 3 sessions. Early-warning signal for ex-post-convenience budget revision.

**WX-22-3 — Engine-version cadence** (Skeptic §5.4). Track whether engine-v3 → engine-v4 occurs within Sessions 023-025. Concern is version-field becomes change-log timestamp rather than meaningful artefact.

**WX-22-4 — Archive-pack location stress test** (Outsider §5.2). Track whether session-local `archive/` subdirectories create discovery friction or D-017 violations within 5 sessions.

**WX-22-5 — Aggregate default-read surface growth** (Outsider §5.3(iii)). Track total default-read surface word count at each session open. Activates if aggregate exceeds ~100K words.

## 8. Synthesizer's limits (honest-notes to future sessions)

1. **Synthesis is single-Claude-orchestrator** per `multi-agent-deliberation.md` v4 §Limitations. Session 022 synthesis-re-entry risk is high given the scope of adoption (8 file surfaces touched; new spec created; engine-v3 bump). Session 023 audit of Session 022 synthesis fidelity is particularly important; WX-22-1 and WX-22-2 should be specifically checked.

2. **D1 archive-pack location** adopted session-local over Outsider's top-level on an argument-weight judgment (locality + new-top-level-scaling concern vs immutability-via-no-new-files concern). The cross-family composition is 2 Claude + 0 non-Claude on the adopted side. Synthesis adopted partly because D1 is a design-choice where either can work; preserved Outsider minority §5.2 ensures rollback path.

3. **D2 budget value (15K/10K words)** adopted as compromise without full cross-family warrant. Outsider's 8K preserved as §5.3. If Session 023 audit finds the 15K permissiveness problematic, early rollback is available.

4. **Session 014 Outsider archive migration (R8c)** is this session's load-bearing migration. If the chunking execution introduces any byte-level drift (accidental whitespace normalization, line-ending changes), check 21 catches it at close. Pre-commit verification: compute source hash before migration; compute concatenated chunk hash after; diff.

5. **SESSION-LOG restoration protocol (R8a)** requires per-entry verification that 03-close.md carries the full detail. For sessions where 03-close.md is thinner than SESSION-LOG (possible for older sessions), the thinned SESSION-LOG entry must be preceded by content-copy-forward. This is mechanical but load-bearing.

6. **Brief-priming awareness**: the synthesis uses operator-vocabulary sparingly but does use "archive" (Outsider variant), "default-read surface" (Outsider), "bounded" and "read contract" (Outsider). Less of the operator's original "canonical surfaces / witnesses" vocabulary is in the synthesis. This is a deliberate choice reflecting the cross-family convergence on re-naming; but it is worth flagging that the synthesis's vocabulary was shaped more by Outsider than by operator, which is the healthy shape (non-Claude reframing accepted on merit) but should not be confused with operator-frame adoption.

7. **Skeptic's defer-position** was honored where strictly-literal-warrant-text was respected (§5.1 not activated on softer ceiling-breach condition; §5.1 minority preserved). The Skeptic's broader "reject frame entirely" position was not adopted; it is preserved as §5.1 with activation warrants that honor its load-bearing concerns.

8. **Session 021 synthesis fidelity (the prior session)** was audited in Session 022's `00-assessment.md` and found clean. Session 022's synthesis applies a similar cross-family-weighting + anti-laundering check discipline. Session 023 should audit Session 022's synthesis for the same dimensions plus the new concerns raised here.

9. **Not synthesized vs rejected**: the synthesis distinguishes. "Not this session" (operator candidate #4 epoch-consolidation; retroactive bulk raw migration; superseded spec reclassification) are deferrals — the candidates remain available for future sessions. "Rejected" (Skeptic's total frame rejection) means the synthesis adopted a different position, preserving the rejected one as minority. Perspectives' positions are not erased by non-adoption.

---

(End of synthesis.)
