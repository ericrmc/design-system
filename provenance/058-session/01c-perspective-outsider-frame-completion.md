---
session: 058
title: Perspective — P3 Outsider / Frame-Completion (Session 058)
perspective: outsider-frame-completion
perspective_family: codex-gpt-5.5
perspective_role: outsider-frame-completion
date: 2026-04-25
status: immutable-at-commit
provenance_note: verbatim from codex exec --sandbox read-only -o output; raw log at codex-p3-raw-output.log; final message at codex-p3-final.md; model gpt-5.5 reasoning-effort xhigh per ~/.codex/config.toml; Case Steward wrapped with frontmatter only (no body edits)
---

# P3 Outsider / Frame-Completion Perspective

## Frame Critique

The §2 frame is directionally right but too file-shaped. "Accretive default-read files impose read-to-edit cost" describes the symptom, not the deeper design choice. The deeper question is whether Selvedge still treats Markdown prose files as the operational memory of the engine, with retrieval as a helper, or whether the engine's durable memory should become explicit facts with Markdown as one witness format.

The current frame risks collapsing two different moves into one: archiving long Markdown blocks into smaller Markdown blocks, and changing the substrate of truth. Direction A sounds like Substrate-N2, but its concrete examples can become "thin index plus per-record Markdown files," which is still Markdown-as-source-of-truth, only sharded. That reduces local read cost but may not change the linear-growth shape at the system level. The operator's stated preference names the stronger move: "structured records as source-of-truth; markdown as witness." The deliberation should not accidentally ratify a weaker pattern while claiming to activate §10.4-M10.

The real question is therefore: should Session 058 commit engine-v10 to a source-of-truth migration, or should it first install a registry discipline that makes such a migration reversible and testable?

My frame-completion answer is that the missing option is not exactly A or Alt 3. It is a staged "Substrate-N3.5": write-time structured records become authoritative for selected accretive facts, while existing Markdown remains the human witness during a proving interval. Once validators and generated witnesses demonstrate stability, engine-v10 can complete the N2 move. This dissolves part of the A/B/C conflict: the engine does not have to choose between a disruptive source-of-truth flip and another Markdown reshuffle.

[external]: This resembles event-sourcing and append-only ledger patterns: durable facts are appended as small records; projections are generated for humans or tools. The relevance is direct because Selvedge already has IDs, decisions, minorities, sessions, and cross-reference edges. The missing step is not search; it is disciplined fact emission.

## Q1 — Primary Direction

Recommendation, despite the above reframes: adopt an alternative architecture, **Substrate-N3.5 as the phase-1 commitment toward Direction A**, rather than Direction A as currently framed.

I would not choose Direction B. It addresses the most urgent file-pressure symptom, `SESSION-LOG.md`, but leaves the more important shape unchanged. It is tactical, cheap, and defensible only if the engine believes EF-055 is a ceiling-management problem. The brief's measurements argue otherwise: accretive sections are already about 19% of the default-read aggregate, `reference-validation.md` is already over the 6K soft threshold, and multiple engine-definition files grow by precedent, minority, or version history. Direction B would buy time while preserving the exact pathology.

I would not choose Direction C. The warrant thresholds are too late for a system that already knows the shape of the problem. Waiting until maintenance time exceeds projection 2x across three sessions or multi-hop query classes dominate prose search by 5x treats operator-visible structural drag as if it needs more empirical proof. The engine already has enough signal: Phase-1 retrieval is operational, the archive-surface citations have validated substrate utility, and the default-read surface is near the 90K soft ceiling.

I also would not adopt full Direction A immediately if "A" means migrating accretive Markdown blocks into per-record Markdown files and thin indexes. That is a useful archive-rotation pattern, but it is not necessarily Substrate-N2. It can reduce default-read cost while increasing total corpus fragmentation and validator complexity. Worse, it may let the engine claim the §10.4-M10 reframe without actually making structured records the durable substrate.

The best answer is: **ratify the substantive arc now, but make phase 1 registry-first.** The engine should define a small structured-record contract for the highest-friction accretive facts: sessions, engine versions, preserved minorities, feedback records, and validation/retrieval minority mirrors. Human Markdown indexes should become generated or validator-checked witnesses as soon as feasible. Per-record Markdown files may exist, but they should not be mistaken for the source-of-truth layer unless each file has structured frontmatter that validators treat as the record.

This option scores differently from the §2.4 matrix. It has higher substrate fit than Direction B, lower migration risk than full Direction A, better reversibility than A+Alt3, and better long-term read-to-edit cost reduction than Alt3 alone. It also honors the operator-stated preference as a durable input without laundering it into immediate maximal adoption.

## Q2 — Adoption Scope

Phase 1 should migrate facts, not prose blocks. The initial scope should be:

1. `SESSION-LOG.md` rows into `records/sessions/*.yaml` or JSONL.
2. Preserved minorities from `workspace-structure.md`, `reference-validation.md`, and `retrieval-contract.md` into one shared minority-record family.
3. `engine-manifest.md` §7 engine-version history into per-version records.
4. `engine-feedback/INDEX.md` entries into feedback-record metadata, if the inbox/resolved files already provide stable anchors.

Phase 1 should leave full narrative bodies in existing files or archive packs, with thin indexes checked against records. Phase 2 should regenerate the thin indexes from records. Phase 3 should make Markdown witnesses non-authoritative render targets where practical.

`SESSION-LOG.md` should migrate early because it is the imminent ceiling breach, but not as an isolated Direction B patch. It should be the proving case for the structured-record pattern.

## Q3 — Per-Record Directory Structure

I would avoid `specifications/minorities/` as the primary structure because it centralizes records by one current use case rather than by fact family. Prefer:

```text
records/
  sessions/
  engine-versions/
  minorities/
  feedback/
  edges/
```

If Markdown witness files are needed:

```text
witnesses/
  minorities/
  engine-versions/
```

Naming should use stable IDs, not local sequence-only names. For minorities, use the canonical existing ID where possible, for example `M10.md` only if globally unambiguous, otherwise `workspace-structure-M10.md` or a normalized ID like `minority-010.md` with source-spec metadata. Mirrored minorities should not create duplicate source records.

File-class classification should distinguish **structured source records**, **generated or checked witnesses**, and **human narrative provenance**. That classification matters more than directory placement.

## Q4 — Index Format

Use the `open-issues/index.md` thin-table pattern as the human-facing exemplar, but make it explicitly a projection of records, not a manually maintained second source of truth.

A useful thin row should contain:

```text
ID | Status | Short title | Source record | Witness/path | Last touched
```

Status should be constrained by record family. For minorities, statuses might include `preserved`, `activated`, `discharged`, `vindicated`, and `superseded`. For sessions, statuses might include `closed`, `archived`, and `superseded-by-restructure`.

Path pointers should point first to structured records and second to human witnesses. If the engine cannot yet generate the index, validators should at least compare row IDs, statuses, and paths against the structured records.

The open-issues model is right because it proves the engine can maintain bounded default-read discoverability. The needed change is authority: indexes should stop being the fact source.

## Q5 — Validator And Tool Updates

Yes, add a new integrity check, plausibly check 25, but keep it narrow at first. Phase-1 validation should prove:

1. Every record has a unique stable ID.
2. Every thin-index row points to an existing record.
3. Every required record field is present.
4. Mirrored references resolve to the same canonical record where intended.
5. Generated or checked witness paths exist.
6. No default-read accretive block silently adds an unrecorded new entry.

`build_retrieval_index.py` should index structured records as first-class retrieval objects, not merely parse Markdown witnesses. Retrieval results should be able to resolve an ID to the structured record, then expose witness/provenance paths.

Testing should use fixture records with valid, missing, duplicate, stale-index, and mirrored-minority cases. The important test is not only "validator catches bad records," but "validator catches divergence between record and witness."

## Q6 — Cross-Spec Interactions

Essential phase-1 scope:

- `workspace-structure.md`: define the new file classes and record/witness distinction.
- `read-contract.md`: update default-read expectations so thin indexes are acceptable only with substrate and fallback discoverability.
- `tools/validate.sh`: add the integrity check entry point.
- `tools/build_retrieval_index.py`: teach retrieval to include structured records.
- `engine-manifest.md`: record engine-v10 trigger criteria if the substantive arc is ratified.

Also essential: `reference-validation.md` and `retrieval-contract.md` need minimal revisions if their preserved-minority blocks move to shared records, because mirrored minority discipline is directly implicated.

Deferrable:

- Full rewrite of archive-pack structure.
- Complete generated Markdown pipeline.
- Full bootstrap external-workspace contract.
- Complete replacement of `engine-manifest.md` §7 with per-version witnesses.

Phase 1 should define the pattern and migrate the first record families. It should not require all rendering and archive machinery to be perfect before any source-of-truth progress is made.

## Q7 — Multi-Session Arc Shape

Use a 3-session arc, not a 2-session arc.

Session 058 should decide the architecture and migrate one narrow proving slice, ideally `SESSION-LOG.md` plus the record schema needed to support it. Session 059 should migrate minorities and mirrored minority references, because that tests cross-spec canonicalization. Session 060 should migrate engine-version history and feedback/index records, then decide whether Markdown witnesses are generated, checked, or still manually maintained.

A clean phase boundary is: validators pass, retrieval resolves records, thin indexes remain usable without reading archives, and a future session can add one new record without editing a long accretive block.

A 2-session arc risks either doing only Direction B in practice or rushing a source-of-truth migration before the validators have earned trust.

## Q8 — Operator-Stated Preference Treatment

Treat Direction A as durable input, not foreclosure. The S048 short-circuit precedent explicitly does not apply per the brief, so the operator preference should raise the burden on dismissing Direction A but should not determine the result.

For my Q1, the operator preference matters because it identifies the true reframe: structured records as source-of-truth, Markdown as witness. But it also makes me more suspicious of a shallow Direction A adoption. If the engine says "we adopted A" while only moving Markdown entries into smaller Markdown files, it has honored the label and missed the substance.

So my answer is influenced by the preference, but not by deference alone. The preference is best satisfied by staging toward actual Substrate-N2, not by immediate maximal migration.

## Open Question — Substrate Availability

Direction A should not depend on the retrieval substrate being available for basic operation. The fallback should be aggregate thin indexes committed as Markdown witnesses. A human should be able to discover every active record family from default-read files, even if search and `resolve_id` are unavailable.

The reframe is: substrate tools accelerate navigation, but structured records provide discipline. Those are separable. If the records are small, named, indexed, and validator-checked, the engine remains inspectable without the retrieval layer.

## Open Question — Per-Record Immutability

Use append-only chronological status events inside the structured record, or companion event records. Do not mutate historical claims in place except for explicitly correctable metadata fields.

The index may show the current status, but the record should preserve the status history. If a minority is discharged in Session 060 and vindicated in Session 064, both events matter. The thin index should display the current state; the record should explain how that state was reached.

## Open Question — Mirrored Minorities

Mirrored minorities should share one canonical minority record. Specs may have local witness references or local index rows, but not separate source records.

Separate files for mirrored instances would recreate the synchronization problem that EF-055 is trying to expose. The canonical record should include `applies_to` or `mirrored_in` fields listing the relevant specs and sections. Local specs can render a thin row pointing to the same ID.

## Open Question — Engine-Version Files

Per-version files should replace the long §7 history block as source material. `engine-manifest.md` §7 should become a thin index pointing to `records/engine-versions/` and any human witness files.

The manifest should retain enough summary for orientation: version, session range, headline change, status, and path. The full rationale belongs in the per-version record and session provenance.

## Open Question — Migration Ordering

Migrate `SESSION-LOG.md` first, but only as the first use of the general record architecture. This avoids Direction B's trap.

The second migration should be preserved minorities because they test the harder question: canonical records, mirrored spec references, status history, and dissent preservation. If the pattern works for minorities, it can work for engine-version history and feedback records.

## Open Question — External Portability

The bootstrap contract likely needs extension. External workspaces should not inherit an implicit dependency on local retrieval tooling without also inheriting record schemas, validation fixtures, and fallback indexes.

A portable engine-v10 should define the record contract as part of the workspace structure: required directories, schemas, validator checks, and generated/checkable witness behavior. Bootstrap should create empty valid record families, not merely copy Markdown templates.

## Open Question — S047 D-150 Candidate (i)

Defer the qualitative-multi-agent label issue unless the schema work directly needs a `deliberation_type` or `agent_label` field. EF-055 is already broad enough.

However, the record schema should leave room for future deliberation metadata. Do not hard-code current MAD role labels into filenames or directory shapes. Make labels data, not structure.

## Anti-Laundering Self-Check

I am straining against two criteria. First, I am trying to honor the operator's Direction A preference without simply endorsing A. Second, I am trying to avoid making "N3.5" a verbal compromise that delays the hard source-of-truth decision.

What would falsify my position: if validators cannot reliably prevent record/witness drift within one session; if adding structured records creates more close-time burden than editing accretive Markdown; or if retrieval cannot resolve structured records as well as Markdown anchors. In those cases, the engine should fall back to a narrower archive-rotation pattern and preserve Substrate-N2 as a minority.

The strongest risk in my answer is schema drag. A fact discipline only helps if the records are small, stable, and cheap to write. If the schema becomes a second specification language, the cure becomes another default-read cost.

## Counter-Frames For The Dominant Claude Position

If P1 and P2 converge on Direction A versus Direction B/C, I expect them to share one assumption: that the named Direction A is already the Substrate-N2 reframe. That may be wrong. Per-record Markdown plus thin indexes can be a better archive layout while still preserving Markdown as the actual source of truth. The engine could then spend an engine-v bump and still face the same future migration when it finally wants structured facts.

If they converge on conservative staging, I expect another shared assumption: that reversibility means keeping the source-of-truth model unchanged. That may also be wrong. A small append-only record layer can be more reversible than a prose migration, because records can regenerate indexes, be validated mechanically, and be ignored by older practices if necessary.

If they converge on "migrate the largest accretive files first," the hidden assumption is that word count is the main priority signal. I think semantic duplication is at least as important. Mirrored minorities across `workspace-structure.md`, `reference-validation.md`, and `retrieval-contract.md` are smaller than `SESSION-LOG.md`, but they expose the harder substrate problem: one fact appearing in multiple prose homes.

The frame I would push into synthesis is: do not ask only "which Markdown blocks move where?" Ask "which facts does the engine promise not to rediscover from prose again?" That is the actual §10.4-M10 activation test.
