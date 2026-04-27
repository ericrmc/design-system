---
session: 078
perspective: substrate-architect
family: Anthropic
date: 2026-04-27
---

# substrate-architect — blind position

## Frame

077 produced the design space; 078 picks. My job is to make one substrate-shape concrete enough that 079 can build it and that the adversary's prose-in-cells prediction `[077-adv]` becomes either falsified or measurable. The deliberation is not "S1 vs S2 vs S3" as three abstract regions — it is "what set of refusals does the methodology actually require, and what shape stores body content such that those refusals are mechanically possible?" `[077-D-1]` already commits the substrate to be a refusal contract; my work is enumerating that contract at a level a SQLite trigger can execute, then choosing the body-storage shape that lets the most refusals stay structural rather than prose-inspectional. I commit below to a hybrid I will call **S1+** — `[077-arch]`'s body-in-cells shape with two specific structurings borrowed from S3 (rejected-alternatives and supersession edges as constrained tuples, never free-text concatenated into a parent body) and one specific borrowing from S2 (perspective bodies stored as files referenced by SHA-256, not as `body_md` cells). Not "S1 with elements of S2" — three named artefact-kinds get S2-or-S3 treatment for stated reasons; everything else is S1.

## Position

### 1. Substrate-shape commitment: S1+

**S1+** = body-in-cells default, with three structural exceptions.

| Artefact | Body storage | Reason |
|---|---|---|
| `decisions` | `body_md TEXT NOT NULL` (S1) | The decision narrative is design intent; structuring it into tuples (S3) loses the reasoning the methodology values (`methodology.md` §Preservation: "the reasoning that led to a rejection is the input to a future decision"). The risk the adversary names is real but lives mostly in the *envelope* (which decisions reference which), not in the body prose. |
| `rejected_alternatives` | **Tuple (S3-style):** `(decision_id, alt_no, alternative_md, rejection_reason_md)` separate row per alternative; **not** concatenated into `decisions.body_md` | This is the single most-prone-to-prose-drift element in the prior engine: rejection reasons drifted into narrative bullets that referenced superseded options. Forcing one row per alternative makes them queryable, addressable (`D-S078-003.alt-2`), and refusable. `[077-dev]` had this as `decision_alternatives`; I promote it to load-bearing. |
| `specifications` body | `body_path TEXT NOT NULL`, `body_sha256 TEXT NOT NULL`, file at `specifications/<slug>-v<NNN>.md` (S2) | Specifications are the durable design intent the methodology says lives in Markdown (`workspace.md` §Specifications). Storing them as files preserves diffability across versions, which is the property `methodology.md` §Preservation calls out ("when a spec is revised, the prior version is preserved"). The substrate refuses inserts where the file at `body_path` does not hash to `body_sha256`. |
| `perspectives` body | `body_path TEXT NOT NULL`, `body_sha256 TEXT NOT NULL`, file at `provenance/NNN-<slug>/perspectives/NN-<role>.md` (S2) | Perspectives are sealed at the file-system level today and the close's note 5 (`077/03-close.md`) records that blind-discipline was procedural-only. Files-with-hashes lets the substrate refuse a perspective insert when `deliberation.sealed_at IS NOT NULL` *and* refuse silent body-rewrites of sealed perspectives via the hash check. Perspective bodies are large (the five 077 perspectives total ~5,800 lines) and rarely re-queried — file-shape suits the access pattern. |
| `supersedes` edges | **Tuple (S3-style):** explicit row in `refs(source_object_id, relation='supersedes', target_object_id, target_version_id)`; **never** narrated in body prose | The seventy-five-session record's most-cited drift was references pointing at superseded versions (`constraints.md` §1). Making supersession a typed edge lets the substrate refuse `cites` against a `superseded` target unless `allow_superseded=1` with `reason_md`, per `[077-dev]`. |
| `engine_feedback` | `body_md TEXT NOT NULL` (S1) | Operator-mediated, low-volume, primarily prose. S1 is fine. |
| `commitments` | **Tuple (S3-style):** `(commitment_id, source_decision_id, summary_md, status, opened_session, closed_session, disposition)` — `summary_md` is one paragraph capped at 1 KiB; full reasoning lives in the parent decision's body | `[077-arch]` had commitments as state-machine rows. I keep the state machine and refuse `summary_md > 1024 bytes`, forcing the agent to write the reasoning where reasoning belongs (the decision body) and the commitment to be a tracking handle, not a second narrative. |

**This addresses `[077-adv]` Divergence-3 directly.** The adversary's prediction is that S1 produces queries returning tables of identifiers whose `body_md` columns contradict each other and no validator can detect this without reading prose. S1+ rebuts the prediction by removing the three places contradiction-via-prose was empirically most likely in the prior engine: rejected alternatives, supersession statements, and commitment summaries. The remaining `body_md` cells (decisions, engine_feedback) carry *reasoning*, which by methodology design is allowed to be opinionated and contradictable — that is what deliberation produces. What the substrate refuses is contradictions in the *envelope* (cross-references, lifecycle, supersession), which S1+ structurally enforces.

I do not adopt full S2 because per-spec-file storage with a database index, applied to *every* artefact-kind, reproduces the workspace-as-directories shape the prior engine ran on, with the database as a second narration layer. The adversary's S2 is right for specifications and perspectives (large, durable, diff-valued); it is wrong for decisions (small, queryable, the unit of cross-reference). I do not adopt full S3 because nobody has produced a tuple-decomposition for decision *reasoning* that preserves what makes decisions readable, and `[077-D-3]` rejected R-3.3 for exactly that reason.

I adopt `[077-arch]`'s schema sketch and `[077-dev]`'s object registry as the working substrate; I revise both at the points above.

### 2. The refusal contract (T-1 through T-14)

The substrate refuses the following writes. Each refusal cites the `constraints.md` failure property it makes structural. The list is intended to be exhaustive at the level 079 implements; refusals discovered later become migrations (see §4).

| # | Refusal | Implementation | Addresses |
|---|---|---|---|
| **T-1** | INSERT `decisions` WHERE any reference embedded in `body_md` (or declared in `decision_refs`) does not resolve to an existing `objects.object_id` | Trigger: parse `body_md` for `[D-S\d+-\d+]`, `[SPEC-...]`, `[OI-...]`, `[EF-...]` patterns; verify each in `objects`; refuse with structured reason | Property 1 (prose-default), Property 2 (failure-as-cheap) |
| **T-2** | INSERT `decisions` WHERE no `decision_alternatives` row exists for that `decision_id` AND the decision's `kind` is `substantive` (vs `procedural`) | Trigger on `sessions.close_at` write: refuse close if any substantive decision lacks at least one alternative row | Property 1, `methodology.md` §Preservation (rejected alternatives are first-class) |
| **T-3** | INSERT/UPDATE `spec_versions` WHERE another row exists with same `spec_id` AND `status='active'` | UNIQUE partial index `(spec_id) WHERE status='active'` | Property 1 (identifier drift) |
| **T-4** | INSERT/UPDATE `spec_versions` WHERE `body_path` file's actual SHA-256 ≠ `body_sha256` column | Pre-commit hook: `selvedge validate --hashes` before allowing transaction commit | Property 2 (silent edits) |
| **T-5** | INSERT `perspectives` WHERE `deliberation.sealed_at IS NOT NULL` | Trigger on insert: lookup parent deliberation; refuse if sealed | Property 5 (lessons not surviving sessions); also addresses 077 close note 5 |
| **T-6** | UPDATE on any row where `owning_session.status='closed'` | Triggers per `[077-dev]` on `decisions`, `decision_alternatives`, `refs`, `spec_versions`, `read_log`, `reviews`, `perspectives` | `methodology.md` §Preservation (provenance immutable after close) |
| **T-7** | INSERT `refs` WHERE `relation='cites'` AND target `spec_versions.status='superseded'` AND `allow_superseded=0` | CHECK + trigger; if `allow_superseded=1` then `reason_md IS NOT NULL` required | Property 1 (references to superseded versions) |
| **T-8** | INSERT `decision_alternatives` WHERE `rejection_reason_md IS NULL OR length(rejection_reason_md) < 16` | CHECK | Property 2 (failure-as-cheap, applied to deliberation discipline) |
| **T-9** | INSERT `commitments` WHERE `length(summary_md) > 1024` | CHECK | Property 1 (forces reasoning into the decision body where it belongs) |
| **T-10** | UPDATE `commitments` SET `status` violating state machine `open → met|abandoned|superseded` (no skips, no reverses) | Trigger | Property 5 (silent commitment drift) |
| **T-11** | INSERT `sessions` WHERE prior session with same `session_no` exists OR `session_no ≠ MAX(session_no)+1` | UNIQUE + CHECK against derived counter | Property 1 (counter drift) |
| **T-12** | UPDATE `sessions` SET `status='closed'` WHERE any `work_items.status` for that session ∈ {`queued`,`leased`,`failed`} | Trigger | Property 5 (sessions closed with hidden incomplete work) |
| **T-13** | UPDATE `sessions` SET `status='closed'` WHERE no `read_log` row exists for that session AND any `decisions` row exists | Trigger | Property 6 (decisions without recorded reads are decisions made from working memory only) |
| **T-14** | INSERT any row WHERE the writer's role (from `agent_runs.role`) is not in the allowed-writers list for that table | Trigger lookup against `role_write_capabilities` table | Property 2 (capability scoping = friction); also addresses orchestrator-centralisation risk `[077-adv]` |

Refusals T-1 through T-14 are the closure of: identifier integrity, lifecycle integrity, deliberation integrity (sealed perspectives, required alternatives), supersession integrity, commitment integrity, immutability, and write-authority scoping. This is the contract `[077-D-1]` asked for, made enumerable.

I do **not** include refusals on prose *content quality* (e.g., "decision body must contain a 'why' paragraph"). Those are the reviewer's job, not the substrate's; conflating them is the prose-default failure in another costume. The substrate refuses on envelope and structure; the reviewer audits prose; the deliberation pattern produces the prose. Three roles, three jurisdictions.

### 3. Worked example (deliverable 3)

Three artefacts the methodology already produces, run through S1+:

#### 3.1 A decision record with rejected alternatives — taking 077-D-3 as the example

**Rows that would be written:**

```sql
-- Object registry entry (substrate-allocated ID)
INSERT INTO objects (object_id, object_type, lifecycle_state, created_session_id)
  VALUES ('D-S077-003', 'decision', 'draft', 'S077');

-- Decision row
INSERT INTO decisions (
  decision_id, session_id, local_no, title, body_md, status, kind
) VALUES (
  'D-S077-003', 'S077', 3,
  'Three substrate-shape candidates carried to session 078; commitment deferred',
  '## What...## Why...## Open...',  -- the prose body, free-text
  'accepted', 'substantive'
);

-- Three rejected alternative rows (the structural commitment)
INSERT INTO decision_alternatives (decision_id, alt_no, alternative_md, rejection_reason_md)
  VALUES ('D-S077-003', 1, 'Commit to S1 in 077.',
          'Prose-in-cells risk named explicitly by adversary; resolving requires worked example or prototype, neither produced.');
INSERT INTO decision_alternatives (decision_id, alt_no, alternative_md, rejection_reason_md)
  VALUES ('D-S077-003', 2, 'Commit to S2 in 077.',
          'No concrete schema for index-only shape was produced.');
INSERT INTO decision_alternatives (decision_id, alt_no, alternative_md, rejection_reason_md)
  VALUES ('D-S077-003', 3, 'Commit to S3 in 077.',
          'No perspective produced tuple-decomposition for decisions; readability cost undefined.');

-- Reference: this decision cites Divergence-3 from the deliberation
INSERT INTO refs (source_object_id, relation, target_object_id, created_session_id)
  VALUES ('D-S077-003', 'cites', 'DEL-S077-001', 'S077');
```

**Refusals exercised:**

- **T-2 fires** if the decision is inserted with `kind='substantive'` and no `decision_alternatives` rows. The agent cannot close session S077 until alternatives are written. *This is the structural enforcement of the methodology's "rejected alternatives" preservation rule, which the prior engine carried in prose and consequently lost.*
- **T-1 fires** if `body_md` contains a reference like `[077-arch]` that does not resolve. The agent must register `PERSPECTIVE-S077-arch` (or equivalent object_id) in `objects` first, or rewrite the citation.
- **T-8 fires** if `rejection_reason_md` is empty or trivially short — refuses "rejected; see synthesis."

**Assembler output (rendered Markdown for the close file):**

The assembler queries:

```sql
SELECT d.local_no, d.title, d.body_md,
       json_group_array(json_object('alt_no', da.alt_no,
                                    'alternative', da.alternative_md,
                                    'reason', da.rejection_reason_md)) AS alternatives
FROM decisions d
LEFT JOIN decision_alternatives da ON da.decision_id = d.decision_id
WHERE d.session_id = 'S077'
GROUP BY d.decision_id ORDER BY d.local_no;
```

…and renders to the existing `02-decisions.md` shape. The Markdown output is byte-identical (modulo whitespace) to what 077 produced by hand. The `## Rejected alternatives.` section is generated from the `alternatives` JSON array, not authored.

**Failure mode if the agent writes malformed input:** the agent attempts `INSERT INTO decisions ... body_md='... rejected: S2 was unworkable, S3 was too costly ...'` with no alternative rows. T-2 refuses at session close. The agent receives a structured error: `REFUSED T-2: decision D-S077-003 (substantive) requires ≥1 row in decision_alternatives`. The agent cannot retry-around: there is no way to close the session without writing the alternatives as rows. The prose-default is structurally impossible.

#### 3.2 A specification with supersession edge — methodology.md v1 → v2

Suppose session 080 substantively revises `methodology.md` (e.g., adds the human-review/subtraction-role disposition).

**Rows written:**

```sql
-- New version registered
INSERT INTO objects (object_id, object_type, lifecycle_state, created_session_id)
  VALUES ('SPEC-methodology-v2', 'spec_version', 'draft', 'S080');

INSERT INTO spec_versions (
  spec_version_id, spec_id, version_no, body_path, body_sha256,
  status, created_session_id, supersedes_version_id
) VALUES (
  'SPEC-methodology-v2', 'SPEC-methodology', 2,
  'specifications/methodology-v2.md',
  '<sha256 of file at write time>',
  'active', 'S080', 'SPEC-methodology-v1'
);

-- v1 transitioned to superseded
UPDATE spec_versions SET status='superseded' WHERE spec_version_id='SPEC-methodology-v1';

-- Update the spec head pointer
UPDATE specs SET current_version_id='SPEC-methodology-v2' WHERE spec_id='SPEC-methodology';

-- Supersession edge as a typed ref (NEVER as prose in body)
INSERT INTO refs (source_object_id, relation, target_object_id, target_version_id, created_session_id, reason_md)
  VALUES ('SPEC-methodology-v2', 'supersedes', 'SPEC-methodology', 'SPEC-methodology-v1',
          'S080', 'Adds human-review/subtraction-role disposition per S078:D-4.b.');

-- The deciding decision cites both versions
INSERT INTO refs (source_object_id, relation, target_object_id, target_version_id, created_session_id, allow_superseded, reason_md)
  VALUES ('D-S080-001', 'cites', 'SPEC-methodology', 'SPEC-methodology-v1',
          'S080', 1, 'Citing the version this decision supersedes is the supersession act.');
```

**Refusals exercised:**

- **T-3 fires** if the agent forgets to update v1's status: a UNIQUE partial index `(spec_id) WHERE status='active'` refuses two active rows. *No silent edits.*
- **T-4 fires** if `methodology-v2.md` is rewritten on disk after the row insert: the next `selvedge validate --hashes` refuses commit because the file's SHA does not match the row's `body_sha256`. *Bodies cannot drift from rows.*
- **T-7 fires** if a later session's decision tries to `cites` v1 without `allow_superseded=1`. The cite-superseded path requires explicit acknowledgement. *References cannot silently point at superseded versions.*

**Assembler output:** the active engine's `specifications/methodology.md` is a symlink (or copy) to whichever file is `current_version_id`'s `body_path`; the prior version remains at `methodology-v1.md`. `archive/specifications/` becomes empty — the substrate is the supersession record, not a directory convention.

**Failure mode:** agent writes `body_md='# Methodology\n\nThis supersedes v1 because...\n'` directly into a `spec_versions` row instead of writing the file plus hash. T-4 refuses on commit (`body_path NOT NULL` check fires first if the column is null; if path is given but file does not exist, hash check refuses). The supersession statement embedded in the body becomes a *narrative* about the supersession; the supersession *act* must be the `refs` row. The substrate forces the agent to make the structural commitment, not narrate it.

#### 3.3 A deliberation synthesis with preserved dissent — taking 077's `01-deliberation.md` as the example

**Rows written:**

```sql
-- The deliberation
INSERT INTO objects (object_id, object_type, lifecycle_state, created_session_id)
  VALUES ('DEL-S077-001', 'deliberation', 'open', 'S077');
INSERT INTO deliberations (
  deliberation_id, session_id, question_md, sealed_at, synthesis_object_id
) VALUES (
  'DEL-S077-001', 'S077', 'Design space for next-generation engine', NULL, NULL
);

-- Five perspectives (bodies as files, not cells)
INSERT INTO perspectives (
  perspective_id, deliberation_id, role, family, body_path, body_sha256, written_at
) VALUES
  ('PERS-S077-arch', 'DEL-S077-001', 'architect', 'Anthropic',
   'provenance/077-design-space/perspectives/01-architect.md', '<sha>', '...'),
  ('PERS-S077-adv',  'DEL-S077-001', 'adversary', 'Anthropic',
   'provenance/077-design-space/perspectives/02-adversary.md',  '<sha>', '...'),
  -- ... three more
;

-- Seal the deliberation (no more perspectives can be added)
UPDATE deliberations SET sealed_at = CURRENT_TIMESTAMP WHERE deliberation_id='DEL-S077-001';

-- Synthesis: convergences and divergences as typed rows, not free-text bullets
INSERT INTO objects (object_id, object_type, ...) VALUES ('SYN-S077-001', 'synthesis', ...);
INSERT INTO syntheses (synthesis_id, deliberation_id, body_md) VALUES
  ('SYN-S077-001', 'DEL-S077-001', '## Frame ...');  -- prose body OK here

-- Each convergence and divergence as a row referencing source perspectives
INSERT INTO synthesis_points (
  point_id, synthesis_id, kind, ordinal, claim_md, source_perspectives
) VALUES
  ('SP-S077-C1', 'SYN-S077-001', 'convergence', 1,
   'The substrate is a refusal contract, not a storage choice.',
   '["PERS-S077-arch","PERS-S077-adv","PERS-S077-sub","PERS-S077-gen","PERS-S077-dev"]'),
  ('SP-S077-D3', 'SYN-S077-001', 'divergence', 3,
   'Whether body content lives in database cells or in files.',
   '["PERS-S077-adv"]'),  -- minority on this point
  -- ...
;

-- Preserved dissent: a divergence with single-source attribution is a first-class minority
-- The substrate refuses synthesis_points with kind='divergence' that claim multi-source convergence
```

**Refusals exercised:**

- **T-5 fires** if any agent attempts to insert a `perspectives` row after `sealed_at` is set. *This makes 077-close-note-5's "blind discipline was procedural-only" structurally enforced going forward.*
- **A new refusal T-15** (which I add to the list, addressing `[077-arch]`'s explicit point about `sealed_until`): UPDATE `deliberations` SET `sealed_at=NULL` is refused unconditionally — once sealed, always sealed.
- A refusal on `synthesis_points` (T-16): if `kind='convergence'`, `json_array_length(source_perspectives) >= 2` required. *A convergence cannot be claimed by one perspective alone; this is the structural form of the methodology's "synthesis preserves dissent" rule.*

**Assembler output:** the rendered `01-deliberation.md` produces "## What converged" and "## What diverged" sections by querying `synthesis_points` ordered by `kind, ordinal`, with each point's claim and source-perspective tags rendered. The output is the same shape 077 produced by hand; the `[arch] [adv] [sub] [gen] [dev]` traceability tags are generated from `source_perspectives` rather than typed by an agent. *Tag drift becomes structurally impossible.*

**Failure mode:** agent attempts to write a synthesis claiming `[arch][gen]` converged on a point but only the architect perspective row supports the claim. The substrate cannot detect this from the body prose alone — but the structured `synthesis_points.source_perspectives` array is the load-bearing surface, and a future query (or human auditor) can compare each point's source-perspective list against the actual content of those perspectives' bodies. This is *less* than full structural prevention, and it is the load-bearing edge of S1+'s coverage: the synthesis body itself remains prose, and prose can mis-summarise. I accept this. The reviewer (kept in A-mid; see §5) audits this surface; the substrate prevents the most-mechanical failures, the reviewer catches the rest. This is `[077-D-1]`'s framing kept honest: the substrate refuses what the substrate can refuse, not what it cannot.

### 4. Schema-evolution protocol (the substrate-shape-specific view of Divergence-7)

The cross-family engineer owns the full protocol; my contribution is the substrate-shape-specific commitment.

**Schema changes are themselves session-shaped.** A schema migration is a `decisions` row of `kind='schema-migration'`, plus a `state/migrations/NNN-<slug>.sql` file. The decision body explains why; the SQL file is the executable change. The substrate refuses a migration whose decision row has no `body_md`, no rejected alternatives (T-2 applies — schema changes are substantive by definition), and no test-trace-row showing the migration ran clean against a copy of the live database before commit.

**Backward-compatibility for body-in-cells columns:** adding a column to `decisions` is `ALTER TABLE decisions ADD COLUMN x TEXT NULL`. Historical rows have `NULL`; new rows may have values. Refusals on the new column apply only to rows with `created_session >= migration_session`. The substrate carries `column_introduced_session` metadata so refusal triggers know not to fire on legacy rows.

**Backward-compatibility for the file-shaped artefacts (specs, perspectives):** the body files at `body_path` never change after their `body_sha256` is committed — that is T-4's whole point. A schema change that wants to *add* fields to a spec_version row (e.g., a new `domain` column) does not touch the file. A schema change that wants to *re-shape* what a spec body is (e.g., split into multiple files) creates a new `spec_versions` row with `supersedes_version_id` pointing at the old, a new file at a new path, and leaves the old row's `body_path` and hash alone. *No migration ever rewrites a closed session's bytes.*

**Schema-evolution refusal:** T-17: a migration cannot DROP a column or DROP a table. It can only ADD columns (with NULL default), ADD tables, ADD indexes, and ADD triggers. Removal happens by deprecation (a column marked deprecated stops being written by new sessions; the column remains in the schema until a separate "archive-old-schema" migration archives it to a `legacy/` schema). This is the structural form of `[077-arch]`'s "evolvable without breaking historical rows."

**This addresses `constraints.md` §"Risks the successor must hold"'s "schema-evolution overhead and the possibility of state-substrate-protection ceremony reincarnated in a different form"** by making the protocol two rules (no destructive migrations; migrations are decisions) rather than a ceremony.

### 5. Handoff to 079 (deliverable 7 contribution from this perspective)

What 079 implements first, in order:

1. `state/migrations/001-initial.sql` — the schema described above, with all tables from `[077-dev]`'s sketch plus my revisions: `decision_alternatives` as load-bearing, `spec_versions.body_path` + `body_sha256`, `perspectives.body_path` + `body_sha256`, `synthesis_points` table, `commitments.summary_md` capped, `column_introduced_session` metadata.
2. Triggers T-1 through T-17.
3. ID allocator (`selvedge id-allocate --type decision --session S079`).
4. `selvedge validate --precommit` runs PRAGMA integrity_check, FK check, T-4 hash verification, and cross-checks all `synthesis_points.source_perspectives` references resolve.
5. The round-trip test from `[077-D-5]`: open S079 → write a decision with one alternative → close → reopen → verify T-6 refuses any update.

**What 079 does not do:** does not build any LLM agent. The first session test runs with a single human writing rows via CLI to verify refusals fire. Agents come in 080+. This matches `[077-D-5]`'s amendment.

### 6. Engagements with the divergences not directly mine

**D-4.a (diagnosis-partial).** S1+ is robust to all three of `[077-adv]`'s readings: under Reading A (single-agent overload), the substrate distributes state correctly; under Reading B (accretion-without-subtraction), the substrate provides the structural surface the subtraction role acts on (the retention-test from `[077-sub]` reads `decisions`, `specs`, `engine_feedback` rows and proposes deletions); under Reading C (self-hosting as disease), the substrate is value-neutral on whether the engine runs against itself or an external problem — the schema is identical. The diagnosis-partial concern is real but does not bear on substrate-shape choice.

**D-4.b (subtractor=human?).** Substrate-shape-neutral; agents-architect's territory. My only substrate-relevant contribution: T-14's role-write-capabilities table can encode either model (one combined `human-subtractor-reviewer` role, or two distinct roles). I implement whichever 078 commits to; the schema admits both. I do note that the rule from `[077-sub]` ("Adding requires a normal session; subtraction can be operator-direct") maps naturally onto T-14: the operator's role has DELETE-via-subtraction-log capability that no LLM role has.

**D-4.c (further-cut engine-v16).** Substrate-shape-neutral. I lean toward `[077-sub]`'s cuts but defer to subtractor-perspective on which.

**Divergence-6 (SQLite).** I adopt SQLite for v1 with `[077-dev]`'s reasoning. The concurrency answer: agents run sequentially through the orchestrator's work-item queue, so there is exactly one writer at a time. Codex calls (read-only sandbox, per 077 close note 4) do not write directly; the orchestrator submits their output to SQLite. If 080+ requires concurrent writers across machines, that triggers a Postgres migration (which T-17 admits as ADD-only, since SQLite→Postgres is not a column change but a substrate substitution; the migration protocol applies at a higher level).

## Where you would not commit

1. **The decision-`body_md`-as-prose carve-out.** I argued S3 is wrong for decision bodies because the reasoning is design intent. I cannot prove this. If the empirical record from sessions 080–095 shows that decision bodies drift, contradict each other, and need reviewer-prose-reading to catch — the same failure mode `[077-adv]` predicted, just in fewer cells than full S1 — then S1+ is insufficient and S3 (decisions as `(claim, justification, alternatives_considered, conditions_for_revisit)` tuples, with body prose demoted to optional `notes_md`) becomes the next move. Evidence that would change my mind: a reviewer audit across 10 sessions finding ≥2 cases where two decision `body_md` cells contradict each other and the substrate did not refuse. I would prefer this be measured than re-argued.

2. **The file-shape for perspectives.** Storing perspective bodies as files plus SHA referenced from the database is more complex than `body_md` cells. The reason — large bodies, sealed-discipline via hash check, file diff valued for human review — is plausible but not validated. If the operational pain of "two stores to keep in sync" exceeds the value, perspectives could collapse to `body_md` cells with a separate "sealed_body_sha256" check. Evidence that would change my mind: any case where a perspective's file and row diverged unintentionally during normal session work in 079–085.

3. **T-2's "kind=substantive vs procedural" line.** I introduced this distinction to avoid forcing alternatives on procedural decisions like "use SQLite as the working substrate" where there are no genuine alternatives. But the line between substantive and procedural is itself a judgment call, and an agent under pressure will mark substantive decisions as procedural to skip alternative-writing. Evidence that would change my mind: any session where T-2 was bypassed by `kind='procedural'` mis-classification, caught at review. The fix would be promoting all decisions to `substantive` and accepting alternative-writing-overhead as the cost.

4. **The synthesis_points coverage.** §3.3 admits that body prose can mis-summarise the structured rows; the substrate cannot fully refuse this. If the reviewer cannot reliably catch this either, the deliberation pattern's "preserve dissent" rule has a structural hole. The fix would be the synthesis body itself becoming a generated artefact (assembled from `synthesis_points` rows with frame and meta-prose authored, but the substantive convergence/divergence content rendered from rows). I do not commit to that yet because it loses authorial latitude in synthesis-writing that may itself be load-bearing.

5. **No prototype.** Everything above is paper schema. The seventy-five-session record is full of paper schemas that worked until they met real workload (see `constraints.md` §1.6). 079's first deliverable is the round-trip test; if that test surfaces a refusal that does not fire when it should, or fires when it should not, the contract revises.

## What you think the other perspectives will miss

- **The adversary** will press hardest on the decision-`body_md` carve-out and the synthesis-prose hole in §3.3. They are right that these are where prose-in-cells could re-emerge. They may miss that the *envelope* refusals (T-1 through T-7, T-11 through T-14) prevent the most-empirically-observed failure classes from the prior engine, even if some prose-drift remains in residual cells. The question is not "is prose-in-cells eliminated?" — it is not — but "is the prose-in-cells residue smaller than the prose-in-files state of the prior engine, and is what remains catchable by review?" S1+ improves on both axes; the adversary may treat any residue as falsifying.

- **The agents-architect** will likely focus on which agents write which rows and miss that T-14 (capability-scoped writes) is the structural enforcement of agent role-confinement that `[077-arch]` and `[077-adv]` both worried about (orchestrator-as-bottleneck). The schema position on agents is: each `agent_runs.role` has an explicit allowed-writes list, and the orchestrator's role itself is *not* in the allowed-writes for `decisions`, `specs`, or `perspectives` — it can only write to `work_items`, `agent_runs`, and `read_log`. This forces orchestrator-as-router rather than orchestrator-as-author.

- **The cross-family engineer** will likely strengthen the Postgres migration story and the concurrent-writer story but may miss that S1+'s file-shaped artefacts (specs, perspectives) interact with git differently from cell-shaped artefacts. The git history of `state/selvedge.db` is a binary blob diff; the git history of `specifications/methodology-v2.md` is a text diff. Choosing file-shape for the artefact-kinds humans actually read in git is a deliberate concession to the methodology's "git history is the workspace's tamper-evident substrate" rule (`methodology.md` §Preservation). The engineer may want to push everything into the database; I have argued for the asymmetry.

- **The cross-family methodologist** will most plausibly challenge the addition of substrate at all (per `[077-sub]`'s frame). My S1+ reply: the schema described above is ~16 tables, ~17 refusals, and one migration protocol. That is a *smaller* surface than the eight engine-v16 spec files plus the seventy-five-session pre-restart provenance the prior engine carried. The substrate is not addition; it is *relocation* of state from prose to schema, with the schema strictly smaller than the prose it replaces. If the methodologist counts schema lines as additions and ignores prose lines removed, the accounting is wrong; if the accounting is fair, S1+ is a net subtraction.
