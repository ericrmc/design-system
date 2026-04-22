entry point). |
    44	| `prompts/application.md` | Template prompt for external-problem applications (loads the engine by reference to this manifest; specifies application-context slots). |
    45	| `specifications/methodology-kernel.md` | Kernel: defines the nine-activity execution semantics. |
    46	| `specifications/multi-agent-deliberation.md` | Defines multi-perspective deliberation triggers, non-Claude participation, recording schema. |
    47	| `specifications/validation-approach.md` | Two-tier validation: structural checks and guided-assessment questions. |
    48	| `specifications/workspace-structure.md` | Defines file classes, top-level structure, provenance conventions. |
    49	| `specifications/identity.md` | Records the name Selvedge and the three-layer denotation. |
    50	| `specifications/reference-validation.md` | Defines reference-validation as the third sense of validation. |
    51	| `specifications/read-contract.md` | Defines the access discipline: default-read surface vs archive surface (v1, added engine-v3). |
    52	| `specifications/engine-manifest.md` | **This file.** |
    53	| `tools/validate.sh` | Executable: runs the Tier 1 structural checks from `validation-approach.md`. |
    54	
    55	An external-application workspace that clones the engine should copy (or reference) these files and nothing else from the source workspace.
    56	
    57	### 4. What is explicitly NOT part of the engine
    58	
    59	The following are development-provenance or application-scope; they are **not** loaded when an external application initialises:
    60	
    61	- `SESSION-LOG.md` (development-provenance)
    62	- `open-issues.md` (development-provenance)
    63	- `provenance/` (development-provenance: all session records)
    64	- `applications/NNN-*/` (application-scope: prior application outputs, not reusable as engine load)
    65	- `specifications/*-v1.md`, `*-v2.md`, `*-v3.md` (superseded spec versions: preserved in the workspace but not active engine definition)
    66	
    67	This manifest's own version history is also not part of the engine load; the current `engine-manifest.md` is what counts.
    68	
    69	### 5. Versioning discipline
    70	
    71	The engine version (`engine-v1`, `engine-v2`, ...) increments when any file in §3 changes in substance. "In substance" means:
    72	
    73	- A new engine-definition file is added to §3.
    74	- An existing engine-definition file receives a substantive revision (v-bump per the spec-revision discipline in `workspace-structure.md`).
    75	- An engine-definition file is removed or superseded.
    76	
    77	The engine version does **not** increment on:
    78	- Typo corrections or formatting adjustments.
    79	- Minor elaborations within an existing spec's scope (per the OI-002 substantive-vs-minor heuristic).
    80	- Updates to development-provenance or application-scope files.
    81	- Changes to `SESSION-LOG.md`, `open-issues.md`, or `provenance/`.
    82	
    83	Engine-version increments are declared by a decision record in the session that executes the increment. The decision names the file(s) changed and the new engine version.
    84	
    85	### 6. Loading the engine / minimal external-application initialisation contract
    86	
    87	An external application workspace is initialised by:
    88	
    89	1. **Copy the engine-definition file set** (§3) into a fresh directory (or reference them from a canonical engine repository). The copy is flat: maintain the same paths (`PROMPT.md`, `prompts/`, `specifications/`, `tools/`).
    90	2. **Create fresh development-provenance files** in the new workspace:
    91	   - Empty `SESSION-LOG.md` (header only).
    92	   - Empty `open-issues.md` (header only).
    93	   - Empty `provenance/` directory.
    94	3. **Create the first application directory** `applications/001-<slug>/` containing at minimum a `brief.md` carrying:
    95	   - The problem statement.
    96	   - Constraints (domain constraints; time constraints; stakeholder constraints).
    97	   - Stakeholders (who holds the problem; who will receive the artefact; who validates).
    98	   - Success condition (what the artefact must do for the application to be considered successful).
    99	4. **Select the execution prompt.** For an external-problem application, copy `prompts/application.md` to the workspace's `PROMPT.md` (or reference it), then fill in the template slots with the application-specific content from `brief.md`. For a self-development application (like this workspace), use `prompts/development.md`.
   100	5. **Record the engine version loaded.** The first session's provenance (e.g., `provenance/001-*/00-assessment.md`) should name the engine version (`engine-v1` or later) the workspace was initialised from.
   101	6. **Run Session 001** per the loaded execution prompt. The session Reads the application's initial state (the `brief.md` + the engine specifications), Assesses what the application's first increment should be, Convenes perspectives, Deliberates, Decides, Produces the first artefact or design fragment, Validates, Records, and Closes.
   102	
   103	The critical rule per Outsider [Session 017 01d Q6]: **external application workspaces inherit the engine, not the engine's autobiography.** The development-provenance of the Selvedge engine's own development is preserved in this source workspace; it does not travel with the engine to an external application.
   104	
   105	### 7. Engine version history
   106	
   107	- **`engine-v1`** — established Session 017 via D-074. First versioned engine definition. File set per §3. Corresponds to the post-Session-017 state of the workspace: `methodology-kernel.md` v4 + scope-clarification sentence; `multi-agent-deliberation.md` v3 + minor scope-applicability sentence; `validation-approach.md` v3 + minor scope-applicability sentence; `workspace-structure.md` v3; `identity.md` v2; `reference-validation.md` v1; `tools/validate.sh` as of Session 005/006 last substantive change; `PROMPT.md` as thin dispatcher; `prompts/development.md` and `prompts/application.md` as created by D-074. Subsequent intra-engine-v1 changes (Session 019: `reference-validation.md` v1 → v2; Session 020: `workspace-structure.md` v3 minor amendment) did not bump the engine version because v3 minor amendments do not trigger §5 bump per OI-002 heuristic.
   108	
   109	- **`engine-v2`** — established Session 021 via D-082. Substantive revisions to three engine-definition files: `multi-agent-deliberation.md` v3 → v4 (added §Criterion-4 Articulation for OI-004; §Acceptable Participant Kinds for OI-004; six new Layer 2 manifest fields; one new synthesis frontmatter field; one new session-level participants.yaml block; four-state OI-004 lifecycle with §Closure Procedure for OI-004); `validation-approach.md` v3 → v4 (added §Tier 2 Q8; documented gating conventions for new checks 16-19); `tools/validate.sh` substantive update (added checks 16, 17, 18, 19; added CRITERION4_ARTICULATION_SESSION constant; added PARTICIPANT_ORGANISATION_CLOSED_SET constant; added Tier 2 Q8 print-out). v3 of the two specs preserved as `multi-agent-deliberation-v3.md` and `validation-approach-v3.md` (both `status: superseded`). All other engine-definition files unchanged at engine-v2 boundary: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `methodology-kernel.md` v4, `workspace-structure.md` v3, `identity.md` v2, `reference-validation.md` v2, `engine-manifest.md` (this file, frontmatter `last-updated: 2026-04-22` + `updated-by-session: 021`).
   110	
   111	- **`engine-v3`** — established Session 022 via D-084. First engine-v-bump to add a new engine-definition file: `specifications/read-contract.md` v1 (new; defines default-read surface vs archive surface access discipline). Substantive revisions to multiple engine-definition files: `methodology-kernel.md` v4 → v5 (§1 Read revised to name default-read vs archive distinction); `workspace-structure.md` v3 → v4 (substantive — adds `open-issues/` directory replacing `open-issues.md` file per v3 split-authorisation clause; adds archive-pack subdirectory convention; cross-references to read-contract.md; SESSION-LOG.md text restored to thin-index form); `validation-approach.md` v4 → v5 (added §Tier 2 Q9 for read-contract adherence; documented gating conventions for new checks 20, 21, 22); `tools/validate.sh` substantive update (added checks 20, 21, 22; added READ_CONTRACT_ADOPTION_SESSION, DEFAULT_READ_HARD_WORD_CEILING, DEFAULT_READ_SOFT_WORD_CEILING constants; added Tier 2 Q9 print-out). Substantive revisions to prompts: `prompts/development.md` lines 19, 25, 43 revised for read-contract discipline; `prompts/application.md` analogous Read-section revision for external-application consistency. v4 of the two revised specs preserved as `methodology-kernel-v4.md`, `workspace-structure-v3.md`, `validation-approach-v4.md` (all `status: superseded`). All other engine-definition files unchanged at engine-v3 boundary: `PROMPT.md` (thin dispatcher unchanged), `multi-agent-deliberation.md` v4 (unchanged; cross-referenced from workspace-structure.md v4 and read-contract.md for provenance layout continuity), `identity.md` v2, `reference-validation.md` v2. Session 022 additionally performed retroactive migrations under the new read-contract: R8a SESSION-LOG.md restored to thin one-liner index; R8b `open-issues.md` split into `open-issues/` directory with per-OI files; R8c Session 014 Outsider perspective (96,651 words) archive-packed at `provenance/022-workspace-scaling-trajectory/archive/014-oi016-outsider/`; R8c' Session 022's own Outsider raw (22,611 words) archive-packed at session close. Mempalace R3 `CLAUDE.md` paragraph removed per E.1 (Session 020 §5.4 warrant trigger 1 satisfied; not engine-definition). Engine-v3 is the first engine-v-bump to introduce a new engine-definition spec file (beyond the original eleven at v1).
   112	
   113	- **`engine-v4`** — established Session 023 via D-086. Substantive revision to one engine-definition file + substantive update to `tools/validate.sh`: `read-contract.md` v1 → v2 (§2 budget values recalibrated 15,000 → 8,000 hard and 10,000 → 6,000 soft per empirical 3.0× tokens-per-word ratio correcting v1's 1.3× assumption; §2 Rationale rewritten; §2a aggregate default-read surface report added with advisory threshold ≥90,000 and activation threshold ≥100,000; §5.1/§5.2/§5.3/§5.5 minorities added; §10 versioning updated); `tools/validate.sh` constants `DEFAULT_READ_HARD_WORD_CEILING` 15000 → 8000 and `DEFAULT_READ_SOFT_WORD_CEILING` 10000 → 6000; new aggregate reporter constants `DEFAULT_READ_AGGREGATE_ADVISORY=90000` and `DEFAULT_READ_AGGREGATE_ACTIVATION=100000`; check 20 output extended with aggregate report per §2a (informational not pass/fail/warn). v1 of read-contract.md preserved as `read-contract-v1.md` with `status: superseded`. All other engine-definition files unchanged at engine-v4 boundary: `PROMPT.md`; `prompts/development.md`; `prompts/application.md`; `methodology-kernel.md` v5; `multi-agent-deliberation.md` v4; `validation-approach.md` v5; `workspace-structure.md` v4; `identity.md` v2; `reference-validation.md` v2; `engine-manifest.md` (this file, documentary update per Session 021 sub-pattern). Engine-v4 is the second engine-v-bump in adjacent sessions (engine-v3 Session 022; engine-v4 Session 023) and the third in four sessions (engine-v2 Session 021; engine-v3 Session 022; engine-v4 Session 023). **Session 022 §5.4 Skeptic engine-version-cadence minority warrant activates at engine-v4 adoption:** "three engine-v-bumps in four adjacent sessions OR external-application portability confusion." Post-activation escalation trigger per Session 023 D-086 R9: any further engine-v-bump in Sessions 024/025/026 elevates §5.4 to substantive and forces a dedicated engine-manifest §5 revision deliberation in that session. OI-018 tracks this as an open issue for Session 024+. Known consequence of v4 adoption: `specifications/multi-agent-deliberation.md` at 6,403 words exceeds new 6,000-word soft warning and fires on adoption; this is designed soft-warning function per read-contract.md v2 §2; Session 024 responds per §8 remediation options.
   114	
   115	Future engine-version increments will extend this history in this section.
   116	
   117	## Validation
   118	
   119	To validate this specification:
   120	
   121	1. Confirm the files enumerated in §3 all exist at the declared paths.
   122	2. Confirm that any file NOT enumerated in §3 but present in the workspace is either (a) in §4's explicit exclusion list, or (b) a superseded spec version, or (c) clearly out-of-scope (e.g., `.git`, `.gitignore`, `.claude`, `.serena`).
   123	3. Confirm that `identity.md` v2 references this manifest as the definition of the engine at the current version.
   124	4. Confirm that `workspace-structure.md` v3 references the same three file-class distinction this manifest implies (engine-definition / development-provenance / application-scope).
   125	5. When a session executes a substantive revision to an engine-definition file, confirm the session's decision record declares a new engine version in this manifest's §2 and §7.
   126	6. When an external application workspace is first initialised, confirm its Session 001 provenance records the engine version loaded per §6.5.
   127	7. Confirm that no engine-version increment has occurred without a decision record authorising it (guard against silent engine-version drift).

 succeeded in 0ms:
     1	---
     2	title: Read Contract
     3	version: 2
     4	status: active
     5	created: 2026-04-22
     6	last-updated: 2026-04-23
     7	updated-by-session: 023
     8	supersedes: read-contract-v1.md
     9	---
    10	
    11	# Read Contract
    12	
    13	## Purpose
    14	
    15	This specification defines the **access discipline** governing what the methodology reads in full at every session open versus what it preserves verbatim and accesses by explicit reference. It repairs a divergence observed at Session 022 between the methodology's normative read obligation (`methodology-kernel.md` §1 Read: "every file, every specification, every provenance record") and the operational read mechanism (paginated `Read --offset`, targeted `Grep`, harness-layer routing around oversized files).
    16	
    17	The access discipline is a dimension separate from — and cutting across — the existing file-class ontology in `workspace-structure.md` (engine-definition / development-provenance / application-scope). A file may be engine-definition AND default-read (an active specification); development-provenance AND archive surface (a historical raw perspective).
    18	
    19	Created Session 022 per D-084 as the resolution of the workspace-scaling trajectory. The read-contract articulates an engine-v3 repair of what Session 022 diagnosed as an OI-015 laundering pattern materialised at the harness layer.
    20	
    21	This specification applies equally to the self-development application and to external-problem applications of the Selvedge engine. Its default-read and archive enumerations are engine-definition content; external-application workspaces inherit them at engine-v3.
    22	
    23	## Specification
    24	
    25	### 1. Default-read surface
    26	
    27	The default-read surface is the bounded set of files read in full at every session open. Every session's Read activity must read every file enumerated below in full before any substantive work proceeds.
    28	
    29	**The default-read surface enumeration at engine-v3:**
    30	
    31	1. Every active-status `.md` file in `specifications/`. "Active-status" means frontmatter `status: active`. Superseded-status files (`*-v1.md`, `*-v2.md`, etc., carrying `status: superseded`) are archive surface by exclusion (§3).
    32	2. `PROMPT.md` (top-level dispatcher).
    33	3. `prompts/development.md` (self-development executable prompt).
    34	4. `prompts/application.md` (external-application executable prompt).
    35	5. `SESSION-LOG.md` (thin one-line-per-session index; full per-session detail lives in `03-close.md`).
    36	6. `open-issues/index.md` (thin overview; full per-OI detail lives in `open-issues/OI-NNN.md` files).
    37	7. Every `provenance/NNN-title/03-close.md` across all closed sessions.
    38	8. Every file in the currently-active session's provenance directory (`provenance/NNN-title/` where NNN is the current session). While the session is open, current-session provenance is default-read; on close, it becomes archive surface by exclusion (§3) unless it is a `03-close.md` (which stays default-read by §7 above).
    39	
    40	The enumeration is closed. A file not enumerated here is archive surface by §3.
    41	
    42	### 2. Default-read budget
    43	
    44	Per-file constraints:
    45	
    46	- **Hard ceiling: 8,000 words.** Any file in the §1 enumeration exceeding 8,000 words of body content (frontmatter excluded) is a validation failure at `tools/validate.sh` check 20. The session that produces such a file must either reduce it or restructure it (e.g., split into multiple files each under the ceiling; relocate detail to archive surface with reference from the default-read file).
    47	- **Soft warning: 6,000 words.** Any file in the §1 enumeration between 6,000 and 8,000 words triggers a validator warning (not a failure). The warning is signal that the file is approaching the ceiling; the next session should consider restructuring. The 6,000-word value is ~75% of the 8,000-word hard ceiling; this ratio is the design principle for future revisions (the validator constants are named integers per `tools/validate.sh`; the ratio lives here as the design guide).
    48	
    49	Measurement: word count via `wc -w` on body content after the closing YAML frontmatter delimiter. The word-count metric is chosen for stability across tokenisers (per Session 022 Outsider [01d-Q6] + Conservator [01b-Q6] convergence).
    50	
    51	**Rationale for the chosen values (revised Session 023).** The current single-Read-tool ceiling at the time of adoption is approximately 25,000 tokens. Empirical measurement of workspace prose-with-markdown files at Session 022 (SESSION-LOG 10,405 words → 33,227 tokens; open-issues 9,783 words → 27,437 tokens) shows a tokens-per-word ratio of approximately 3.0×, not the 1.3× that the v1 Rationale used. At the corrected ratio, 8,000 words is approximately 24,000 tokens — narrowly within the single-Read ceiling, aligned with the reader-contract intent that default-read means "read in full at every session open." The 6,000-word soft warning is approximately 18,000 tokens, well within single-Read, providing early signal before files approach the ceiling.
    52	
    53	The v1 Rationale's 15,000-word hard ceiling (≈ 45,000 tokens, ~1.8× the single-Read ceiling) was set under an empirically wrong calibration. The v1 values produced a ceiling that routinely required paginated reading at files near the ceiling — misaligned with default-read's own purpose. Session 022's Honest Notes flagged this error; Session 023 corrected the values per D-086.
    54	
    55	**Known consequence at v2 adoption.** `specifications/multi-agent-deliberation.md` at 6,403 words exceeds the new 6,000-word soft warning at v2 adoption. This is the designed function of the soft warning: to prompt restructure when a file approaches the ceiling. Session 024+ remediation options per §8 below.
    56	
    57	**Minority positions preserved (Session 023 D-086 R10 §5):**
    58	
    59	- **§5.1 Pacer 10K/7.5K minority** (Session 023 [01b-Q1, Q2]). Position: 10,000-word hard ceiling with 7.5K soft warning preserves calibration-corrective discipline while leaving growth headroom. Activation warrant: if the adopted 8K/6K budget produces three or more restructure-for-budget events in the next 5 sessions (restructures prompted by budget rather than by content completion), revisit upward toward 10K/7.5K. Alternatively, if 8K binds on `multi-agent-deliberation.md` or `reference-validation.md` in a way that forces content-coherence-damaging split, this position becomes preferred revision direction.
    60	
    61	- **§5.2 Skeptic no-change + warrant-literalism minority** (Session 023 [01c-Q1]). Position: the v1 Outsider-§5.3 activation warrant had not literally fired; revising values one session into a five-session grace window subverts the spec's own governance mechanism for self-revision. Vindication warrant: if within 5 sessions of Session 022 adoption (i.e., by Session 027) no default-read file exceeds 7,500 words and no restructure-for-budget event occurs, the Skeptic no-change position is vindicated retroactively — Session 023's revision was premature.
    62	
    63	- **§5.3 Pacer aggregate-hard-budget minority** (Session 023 [01b-Q3]). Position: adopt aggregate default-read surface hard budget at 90K hard / 80K soft now; naming a budget creates the forcing function that watchpoint-only reporting lacks. Activation warrant: if aggregate exceeds 100,000 words OR grows >10% in a single session without compensating restructure, this position becomes preferred revision direction.
    64	
    65	- **§5.5 tokeniser-drift watch minority** (Session 023 [01a-Honest Limits, 01d-Honest Limits]). Position: the 3.0× tokens-per-word ratio used in the revised Rationale is measured on two files only; applicability across file-types is not empirically verified. Activation warrant: if any single-Read attempt on a default-read file fails due to token-budget-exceeded despite the file being under the 8K word ceiling, re-measure the tokens-per-word ratio across a sample of default-read files and re-calibrate.
    66	
    67	### 2a. Aggregate default-read surface report (added v2)
    68	
    69	`tools/validate.sh` check 20 additionally reports the aggregate word count across all default-read surface files in every Tier 1 run. This is informational at v2 (not pass/fail/warn). Advisory and activation thresholds:
    70	
    71	- **Advisory:** aggregate ≥ 90,000 words. Validator emits an advisory note; next session should note the aggregate in close.
    72	- **Activation:** aggregate ≥ 100,000 words OR aggregate grows >10% in a single session without compensating restructure. Session N+1 should deliberate whether to add an aggregate hard budget per §5.3 minority.
    73	
    74	The aggregate report is a prophylactic against the accretion failure mode the Session 022 Outsider identified ("per-file control alone is not sufficient if the default-read set keeps growing by accretion" [archive: provenance/022-workspace-scaling-trajectory/archive/022-outsider/#chunk-04, Q6]). At engine-v4 adoption, aggregate is approximately 81,500 words across 33 default-read files; advisory threshold not reached; activation threshold not reached.
    75	
    76	### 3. Archive surface
    77	
    78	By exclusion: anything preserved in the workspace but not on the §1 enumeration. This includes:
    79	
    80	- Raw perspective files (`provenance/NNN-title/01X-perspective-<role>.md`) from closed sessions.
    81	- Superseded specification versions (`specifications/*-v1.md`, `*-v2.md`, etc., carrying `status: superseded`).
    82	- Deliberation synthesis files (`provenance/NNN-title/01-deliberation.md`) from closed sessions.
    83	- Decision files (`provenance/NNN-title/02-decisions.md`) from closed sessions.
    84	- Assessment files (`provenance/NNN-title/00-assessment.md`) from closed sessions.
    85	- Manifests (`provenance/NNN-title/manifests/`) from closed sessions.
    86	- Participant indexes (`provenance/NNN-title/participants.yaml`) from closed sessions.
    87	- Any per-OI historical annotation files that predate the Session 022 `open-issues/` directory split.
    88	
    89	Archive surface records are **preserved verbatim.** Summarisation, silent compression, content-aware truncation, or edit-in-place are forbidden. The preservation-vs-summarisation distinction is the load-bearing property that prevents this specification from becoming an on-ramp for information loss.
    90	
    91	Archive surface records are **accessed by explicit reference.** A session reading an archive record must cite it per §6 below; silent non-reads of relevant archive records are a validation concern (check 22 and Tier 2 Q9 in `validation-approach.md` v5).
    92	
    93	### 4. Archive-pack structure
    94	
    95	When an archive-surface record exceeds the default-read per-file budget (§2 hard ceiling), or when the archive record is produced within a current session that will otherwise push the current-session provenance directory over budget at close, the record must be structured as an **archive-pack**: a directory with a manifest plus numbered chunks, preserving byte-identical content via line-range splits only.
    96	
    97	Archive-pack layout:
    98	
    99	```
   100	provenance/NNN-title/archive/<slug>/
   101	  manifest.yaml        # frontmatter + chunk table + integrity fields
   102	  00-source.md         # byte-identical single file if under per-chunk budget
   103	  OR
   104	  01-chunk.md          # numbered chunks with line-range boundaries only
   105	  02-chunk.md
   106	  ...
   107	```
   108	
   109	Chunk size target: each chunk ≤ 10,000 words (matching the §2 soft warning) so that reading any individual chunk never exceeds comfortable read budget.
   110	
   111	Boundary rule: **mechanical only** — either line-range or byte-range boundaries. Content-aware boundaries (e.g., "end at a paragraph break," "split at a heading") are forbidden because they introduce chunking judgment that can silently edit content over time. Line-range and byte-range boundaries are both mechanical and auditable; the manifest declares which rule was used via `chunk_boundary_rule: line-range | byte-range | single-file`. Line-range is preferred where the file's line-length distribution is bounded; byte-range is the fallback when the file contains very long lines that would otherwise produce oversized chunks (the Session 014 Outsider file exemplifies this: a 96,651-word file with individual lines of up to 3,328 words; line-range chunking produced chunks over 36,000 words that would themselves breach the default-read budget, so byte-range splitting into 50,000-byte chunks was used).
   112	
   113	### 5. Archive-pack manifest fields
   114	
   115	The `manifest.yaml` file in every archive-pack carries the following required fields:
   116	
   117	```yaml
   118	---
   119	archive_id: <stable identifier, typically <originating-NNN>-<slug>>
   120	originating_session: <session number>
   121	originating_path: <workspace-relative path of the source file>
   122	migrated_in_session: <session number that created the archive-pack>
   123	kind: raw-perspective | over-budget-annotation | superseded-spec | other-named
   124	total_bytes: <integer; bytes of concatenated chunks in canonical order>
   125	total_words: <integer; words of concatenated chunks>
   126	chunk_count: <integer>
   127	chunk_boundary_rule: line-range | single-file
   128	source_hash_sha256: <SHA-256 hash of full concatenation of chunks in ordinal order>
   129	chunks:
   130	  - ordinal: 1
   131	    file: 01-chunk.md
   132	    line_range: "1-500"
   133	    chunk_hash_sha256: <SHA-256 hash of this chunk's contents>
   134	  - ordinal: 2
   135	    file: 02-chunk.md
   136	    line_range: "501-1000"
   137	    chunk_hash_sha256: <SHA-256 hash>
   138	  ...
   139	readers_note: <1-3 sentences; what the archive preserves; when to consult it>
   140	---
   141	```
   142	
   143	The manifest is pointer-only. Narrative content beyond the `readers_note` field is forbidden — `readers_note` is at most three sentences. The manifest exists to resolve references, not to summarise the archived content.
   144	
   145	### 6. Reference conventions
   146	
   147	Default-read surface files cite archive-surface records using a stable reference string:
   148	
   149	```
   150	[archive: provenance/NNN-title/archive/<slug>/]
   151	```
   152	
   153	With optional chunk-level precision:
   154	
   155	```
   156	[archive: provenance/NNN-title/archive/<slug>/#chunk-02]
   157	```
   158	
   159	Readers resolving the reference read `manifest.yaml` first, consult the `readers_note`, and then read specific chunks as the current work requires. A citing session that relies on archive content for a load-bearing claim must either read the cited chunk(s) in full, or declare in its honest-limits section that the claim rests on prior-session vetting of the archive content rather than fresh re-reading.
   160	
   161	The reference convention is load-bearing for validator check 22 (archive-pack citation consistency): every `[archive: path]` reference in a default-read file must resolve to an existing archive-pack path.
   162	
   163	### 7. Integrity guarantee
   164	
   165	The `source_hash_sha256` field in each archive-pack manifest is computed against the canonical concatenation of chunks in numerical order. `tools/validate.sh` check 21 verifies this hash on every run; any mismatch is a hard-fail.
   166	
   167	Per D-017 immutability (`workspace-structure.md` §provenance), once the migrating session closes, archive-pack files are immutable. Any revision to an archive-pack's content requires a new migrating session with its own decision record; the revision creates a new archive-pack and a supersession reference, not an edit of the prior pack.
   168	
   169	Archive-packs created by retroactive migration (migrating a closed session's file into archive form) use the **copy-plus-reference** discipline per Session 009 D-054 precedent: the original file at its original path is **not modified**; the archive-pack is created alongside, typically in the migrating session's own provenance directory (`provenance/<migrating-NNN>/archive/<slug>/`). The original remains at its original path as the byte-identical witness; the archive-pack provides structured access.
   170	
   171	Archive-packs created for the current session's own raws (per §9 close-time obligation) move the original content into the archive-pack structure directly (the original path becomes the archive-pack path; no duplication). Because the session is still open at the time of packing, moving is not an edit of a closed-session file.
   172	
   173	### 8. Default-read surface budget at session close
   174	
   175	At every session close, the orchestrator verifies that every file in the §1 enumeration satisfies the §2 per-file budget. `tools/validate.sh` check 20 enforces this; a hard-fail at session close blocks the session from closing cleanly.
   176	
   177	Remediation when a default-read file exceeds the budget: reduce the file in place; or split the file into multiple default-read files (each under budget) with the original split-file designated archive-surface (its content preserved as an archive-pack); or relocate detail to archive-pack form with references from a thinner default-read replacement.
   178	
   179	Remediation must not summarise or silently compress; the archive-pack discipline preserves content verbatim.
   180	
   181	### 9. Close-time obligation for current-session raws
   182	
   183	At every session close, the orchestrator measures each raw perspective file and each provenance file in the current session directory. Any file exceeding the default-read per-file hard ceiling (§2: 15,000 words) is archive-packed before session close.
   184	
   185	Mechanism for current-session raw-to-archive-pack migration:
   186	
   187	1. Create `provenance/NNN-title/archive/<slug>/` where `<slug>` is a short descriptive identifier (typically matching the perspective role and question theme).
   188	2. Split the file into line-range chunks each ≤ 10,000 words. Preserve byte-identical content.
   189	3. Write `manifest.yaml` with the required fields (§5), computing all hashes.
   190	4. **Remove the original file** from the provenance root. The original content now lives in the archive-pack chunks (byte-identical); there is no duplication. (This removal is permissible during session close because D-017 immutability binds only on closed sessions.)
   191	5. Update any in-session references (e.g., from `01-deliberation.md`) to use the `[archive: path]` convention.
   192	
   193	The SESSION-LOG entry for the session records archive-pack presence with a one-phrase note (e.g., "archive-packs: 1 (outsider)").
   194	
   195	### 10. Versioning
   196	
   197	Version 1 established Session 022 per D-084. Version 2 established Session 023 per D-086 (§2 budget-value recalibration from 15K/10K to 8K/6K; §2 Rationale corrected for empirical 3.0× tokens-per-word ratio; §2a aggregate report added; §5.1/§5.2/§5.3/§5.5 minorities added). v1 preserved as `read-contract-v1.md` with `status: superseded`.
   198	
   199	Subsequent revisions to this specification follow OI-002 substantive-vs-minor heuristic (`open-issues/OI-002.md`):
   200	- **Substantive:** any change to the §1 enumeration, §2 budget values, §2a aggregate thresholds, §4 archive-pack structure, §5 manifest fields, §6 reference convention, or §7 integrity mechanism. Engine-version bump per `engine-manifest.md` §5.
   201	- **Minor:** clarifying text edits, cross-reference updates, examples within existing scope.
   202	
   203	Watchpoint recorded Session 023 D-086 R10 §5.5: if `read-contract.md §2` budget values are revised a second time within three sessions of Session 023 v2 adoption, examine whether the spec's design frame (per-file word count as measurement primitive) is itself miscalibrated — consider token-count or hybrid metrics.
   204	
   205	## Validation
   206	
   207	To validate this specification:
   208	
   209	1. Confirm every file in the §1 enumeration exists at its declared path and carries the required frontmatter (for specifications) or is a well-formed index/close.md (for SESSION-LOG and open-issues).
   210	2. Confirm every file in the §1 enumeration satisfies the §2 per-file budget. `tools/validate.sh` check 20 automates this verification.
   211	3. Confirm that files not in the §1 enumeration but present in the workspace are either (a) explicitly archive surface (per §3), or (b) out-of-scope top-level files (e.g., `.git`, `.gitignore`, `.claude`, `.serena`, `applications/`), or (c) session-scratch files outside the read-contract scope.
   212	4. For every archive-pack in `provenance/*/archive/*/`: confirm `manifest.yaml` is well-formed with all §5 required fields; confirm `source_hash_sha256` matches the actual hash of concatenated chunks in canonical order. `tools/validate.sh` check 21 automates this.
   213	5. For every `[archive: path]` reference in a default-read surface file: confirm the reference resolves (path exists; chunk ordinals exist if specified). `tools/validate.sh` check 22 automates this.
   214	6. Confirm that `methodology-kernel.md` §1 Read references this specification as the authority on default-read vs archive distinction.
   215	7. Confirm that `prompts/development.md` and `prompts/application.md` read-activity instructions reference this specification as the authority.
   216	8. Confirm that `workspace-structure.md` v4 §SESSION-LOG.md, §open-issues, and §specifications point at this specification for the access-discipline rules.

 succeeded in 0ms:
     1	---
     2	title: Validation Approach
     3	version: 5
     4	status: active
     5	created: 2026-04-17
     6	last-updated: 2026-04-22
     7	updated-by-session: 022
     8	supersedes: validation-approach-v4.md
     9	---
    10	
    11	# Validation Approach
    12	
    13	## Purpose
    14	
    15	This specification defines how the methodology validates itself: what is checked, how checks are organized, and what the checks can and cannot assure. It serves the methodology's self-hosting principle — a methodology that cannot verify its own specifications cannot evolve reliably.
    16	
    17	**Scope note (added as a minor correction in Session 009 per D-056).** This specification covers **Workspace validation** as defined in `methodology-kernel.md` v2 §7. **Domain validation** (the second sense of §7, concerning whether an external artefact functions in its target domain) is performed by domain-actors outside this specification's Tier 1 / Tier 2 scope and is not automated by `tools/validate.sh`. Its governance lives in the kernel §7 text itself.
    18	
    19	**Scope note (added as a minor correction in Session 017 per D-074).** The Tier 1 structural checks and Tier 2 guided-assessment questions defined in this specification apply equally to the self-development application and to external-problem applications of the Selvedge engine. Validation is engine-level; the specific artefacts checked (and the appropriate domain-validation pathway) vary by application kind, but the two-tier discipline is invariant.
    20	
    21	Version 5 adds three new Tier 1 checks (20, 21, 22) operationalising the read-contract in `specifications/read-contract.md` v1 (D-084, Session 022), and one new Tier 2 question (Q9) addressing read-contract adherence. It specifies gating, severity, and sequencing rules for the new checks. It supersedes v4 (`validation-approach-v4.md`).
    22	
    23	Version 4 adds four new Tier 1 checks (16, 17, 18, 19) operationalising the OI-004 criterion-4 articulation in `multi-agent-deliberation.md` v4 (D-082, Session 021), and one new Tier 2 question (Q8) paired with check 18's honest limit. It specifies gating, severity, and sequencing rules for the new checks. It superseded v3 (`validation-approach-v3.md`).
    24	
    25	Version 3 added two new Tier 1 checks (14, 15) that operationalised v2 `multi-agent-deliberation.md` Validation items 1 and 2 (now v3+ Validation items), and one new Tier 2 question (Q7) paired with checks 14/15's honest limits. It specified gating, severity, and sequencing rules for those checks. It superseded v2 (`validation-approach-v2.md`).
    26	
    27	Version 2 added three new Tier 1 checks (11, 12, 13) that enforce the D-024 heterogeneous-participant schema introduced by `multi-agent-deliberation.md` v2, and one new Tier 2 question paired with check 13's honest limit. It superseded v1 (`validation-approach-v1.md`).
    28	
    29	## Specification
    30	
    31	### Two-Tier Model
    32	
    33	Validation has two tiers, reflecting the distinction between properties that can be checked mechanically and those that require judgment.
    34	
    35	**Tier 1: Structural Checks** are automated checks run by `tools/validate.sh`. They verify that the workspace's files conform to the formats and conventions defined in other specifications. Structural checks are necessary but not sufficient for methodology health — a workspace can pass all structural checks while its specifications are semantically wrong or its provenance is misleading.
    36	
    37	**Tier 2: Guided Assessment** is a set of questions printed by the validation tool for the agent or human conducting the session to consider. These questions address properties that cannot be checked mechanically: semantic consistency, provenance usefulness, and whether the methodology is making genuine progress.
    38	
    39	### Tier 1: Structural Checks
    40	
    41	The following checks are automated:
    42	
    43	| # | Check | Source Spec | Severity | Gate |
    44	|---|-------|-------------|----------|------|
    45	| 1 | Required top-level files exist (PROMPT.md, SESSION-LOG.md, open-issues.md) | workspace-structure | Fail | unconditional |
    46	| 2 | Required directories exist (specifications/, provenance/) | workspace-structure | Fail | unconditional |
    47	| 3 | Each specification has YAML frontmatter with required fields (title, version, status, created, last-updated, supersedes) | workspace-structure | Fail | unconditional |
    48	| 4 | Each specification has three required section headings (Purpose, Specification, Validation) | workspace-structure | Fail | unconditional |
    49	| 5 | Provenance directories follow NNN-title naming convention | workspace-structure | Fail | unconditional |
    50	| 6 | Session log has an entry for each provenance directory | workspace-structure | Fail | unconditional |
    51	| 7 | Each provenance directory contains at least one .md file | methodology-kernel | Fail | unconditional |
    52	| 8 | Provenance files have YAML frontmatter with required fields (session, title, date, status) | workspace-structure | Fail | unconditional |
    53	| 9 | Decision records include rejected alternatives sections | methodology-kernel | Warning | unconditional |
    54	| 10 | No uncommitted changes to provenance files (basic immutability heuristic) | workspace-structure | Warning | unconditional |
    55	| 11 | Multi-agent three-raw-output floor: ≥3 files matching `*-perspective-*.md` | multi-agent-deliberation (v2 Validation #3) | Fail | session has ≥1 `*-perspective-*.md` file |
    56	| 12 | Heterogeneous-participant schema well-formedness: each `manifests/*.manifest.yaml` has all D-024 required fields as literal keys | multi-agent-deliberation (v2 Validation #8) | Fail | session has `manifests/` subdirectory |
    57	| 13 | Cross-model-claim honesty: `cross_model: true` implies ≥1 manifest with `training_lineage_overlap_with_claude` other than `known-overlap` OR `participant_kind: human` | multi-agent-deliberation (v2 Validation #9) | Fail | session declares `cross_model: true` AND check 12 passed for that session |
    58	| 14 | Multi-agent trigger coverage: decision declares any `d016_*` trigger implies ≥3 raw perspective files plus synthesis OR `**Single-agent reason:**` annotation on the decision | multi-agent-deliberation (v3 Validation #1 operationalised) | Fail | session ≥ 006 AND session has ≥1 decision record with `**Triggers met:**` line |
    59	| 15 | Non-Claude trigger coverage: decision declares any `d023_*` trigger implies ≥1 manifest with `participant_kind` outside `{claude-subagent, anthropic-other}` OR `**Non-Claude participation:**` skip annotation with `reason:` and `retry_in_session:` sub-fields | multi-agent-deliberation (v3 Validation #2 operationalised) | Fail | session ≥ 006 AND check 12 passed for that session |
    60	| 16 | Independent-claim evidence-pointer presence: each manifest with `training_lineage_overlap_with_claude: independent-claim` has non-empty `training_lineage_evidence_pointer:` field | multi-agent-deliberation v4 §Heterogeneous-Participant Recording Schema | Fail | session ≥ 021 |
    61	| 17 | Claude-output-in-training disclosure: each manifest with `participant_kind` in `{non-anthropic-model, human}` has a `claude_output_in_training:` field whose value is in `{known-yes, known-no, unknown, n/a}` | multi-agent-deliberation v4 §Heterogeneous-Participant Recording Schema | Fail | session ≥ 021 |
    62	| 18 | OI-004 closure-retrospective well-formedness: any `provenance/*/oi-004-retrospective.md` artefact contains the three required sections `## Qualifying Deliberations Table`, `## Summary Tally`, `## P4 Assertion` | multi-agent-deliberation v4 §Closure Procedure for OI-004 | Fail | presence of `oi-004-retrospective.md` artefact |
    63	| 19 | Non-Anthropic participant_organisation closed-set membership: each manifest with `participant_kind: non-anthropic-model` has non-empty `participant_organisation:` field whose value is in the spec-enumerated closed set | multi-agent-deliberation v4 §Acceptable Participant Kinds for OI-004 | Fail | session ≥ 021 |
    64	| 20 | Default-read surface per-file budget: every file in `read-contract.md` §1 default-read enumeration has body-word-count ≤ `DEFAULT_READ_HARD_WORD_CEILING` (Fail) or ≤ `DEFAULT_READ_SOFT_WORD_CEILING` (Warn) | read-contract §2 | Fail/Warn | session ≥ 022 |
    65	| 21 | Archive-pack manifest integrity: every `provenance/*/archive/*/manifest.yaml` has required keys and the stored `source_hash_sha256` matches actual hash of concatenated chunks in ordinal order | read-contract §7 | Fail | presence of any `archive/` subdirectory under `provenance/*/` |
    66	| 22 | Archive-pack citation consistency: every `[archive: path]` reference in a default-read surface file resolves to an existing archive-pack path; chunk ordinals named in the reference exist in the manifest | read-contract §6 | Fail | presence of any `archive/` subdirectory under `provenance/*/` |
    67	
    68	Checks marked **Fail** cause the tool to exit with a non-zero code. Checks marked **Warning** are reported but do not cause failure.
    69	
    70	### Gating Conventions (checks 11, 12, 13)
    71	
    72	**Presence-gating.** Checks 11, 12, and 13 apply only to sessions whose provenance exhibits the relevant artefact. A session without any `*-perspective-*.md` files is not a multi-agent session and is out-of-scope for check 11. A session without a `manifests/` subdirectory has not adopted the D-024 schema and is out-of-scope for check 12 (and by extension, check 13). Out-of-scope sessions produce no output from the gated check — no warning, no failure.
    73	
    74	**Consequence for prior sessions.** Sessions 001 (Genesis) and 002 (Self-Validation) are not multi-agent; they are out-of-scope for all three new checks. Session 003 and Session 004 are multi-agent (have perspective files) but did not produce a `manifests/` subdirectory; they are in-scope for check 11 and out-of-scope for checks 12 and 13. Session 005 and later sessions that adopt the full schema are in-scope for all three.
    75	
    76	**Rationale for the gate granularity.** Gating at `manifests/` subdirectory presence — rather than at `participants.yaml` presence or at session-number — was chosen to (a) keep Session 004's bootstrap-exempt minimal `participants.yaml` naturally out-of-scope without requiring an inline exemption list, (b) avoid encoding a numeric session cutoff that must be maintained in the tool, and (c) produce the same outcome in practice as session-number gating (Session 005 is the first session to have a `manifests/` subdirectory). This decision is recorded in D-030 (Session 005) along with the genuine cross-model disagreement that preceded it.
    77	
    78	### Gating Conventions (checks 14, 15) — Session-number gating
    79	
    80	**Session-number-gating.** Checks 14 and 15 apply only to sessions numbered ≥ 006. The gate is encoded as an explicit constant `TRIGGERS_MET_ADOPTION_SESSION=6` near the top of `validate.sh` so a future reader can see the history in one line. Out-of-scope sessions (001 through 005) produce no output from these checks — no warning, no failure.
    81	
    82	**Rationale for session-number gating here (distinct from check 12's artefact-presence gating).** Session 006 deliberated (D-039) on whether to use presence-gating (as with checks 11–13) or session-number gating for checks 14 and 15. The cross-perspective result: three of four perspectives (Archivist, Skeptic, Outsider — cross-model) converged on session-number gating; one (Implementer) preferred presence-gating. The decisive arguments were (a) ambiguity of absence under presence-gating (a missing `**Triggers met:**` line cannot be distinguished from "pre-adoption" vs "author forgot"), and (b) bypass-by-omission: presence-gating invites operators who want to avoid a check to simply omit the triggering field. Session-number gating makes absence in a post-adoption session unambiguously a failure. This is the same cross-perspective divergence pattern that Session 005 faced (D-030); the resolution here is the opposite because the failure-mode calculus differs — check 12's artefact-presence gating could not be gamed-by-omission (the `manifests/` directory is a substantive artefact, not a trivially-omittable field), whereas `**Triggers met:**` can be trivially omitted.
    83	
    84	**Consequence for prior sessions.** Sessions 001 through 005 are out-of-scope for checks 14 and 15. Session 006 and later sessions must include `**Triggers met:**` on every decision record (with `[none]` if no triggers fired).
    85	
    86	### Gating Conventions (checks 16, 17, 19) — Session-number gating; Check 18 — presence-gating
    87	
    88	**Session-number-gating (checks 16, 17, 19).** Apply only to sessions numbered ≥ 021. The gate is encoded as an explicit constant `CRITERION4_ARTICULATION_SESSION=21` near the top of `validate.sh` so a future reader can see the history in one line. Out-of-scope sessions (001 through 020) produce no output from these checks — no warning, no failure.
    89	
    90	**Rationale for session-number gating.** Checks 16, 17, 19 enforce schema fields introduced by `multi-agent-deliberation.md` v4 §Heterogeneous-Participant Recording Schema (D-082, Session 021). Pre-adoption manifests do not have these fields and cannot have them retroactively per the immutability rule (D-017). Per the Session 006 D-039 precedent for checks 14/15, session-number gating is the correct mechanism for prospective-only schema adoption. Presence-gating would create the ambiguity-of-absence problem (a missing `claude_output_in_training:` field cannot be distinguished from "pre-adoption" vs "author forgot").
    91	
    92	**Presence-gating (check 18).** Check 18 fires only when an `oi-004-retrospective.md` file is present anywhere under `provenance/*/`. The artefact does not exist until a future session writes it; pre-existence sessions are out-of-scope. Once written, check 18 verifies structural well-formedness; substantive adequacy is Tier 2 Q8 (paired).
    93	
    94	**Out-of-scope behaviour for participant_kind values.** Check 17 is out-of-scope for `participant_kind` in `{claude-subagent, anthropic-other}` (no Claude-output disclosure required for Claude-fa