---
session: 005
title: substrate-only-write-path — deliberation
generated_by: selvedge export
---

# Deliberation

## D-3 — Substrate data model for prose-free session state and specifications: triples vs typed link tables vs hybrid; how to make prose-in-rows structurally impossible; CLI shape and migration path for engine-v20

sealed_at: 2026-04-27T08:41:45.525Z

### P-1 (openai)

**Position.** Use a typed relational graph: typed nodes, typed link tables per predicate, and bounded text atoms only where human language is intrinsically required. Do not use a generic triples table as the core.

**schema_sketch.**
- No semantic table has body_md, reason_md, summary_md, or nullable notes; semantic rows hold IDs, enums, ordinals, booleans, hashes, and FKs.
- Human language lives only in text_atoms with hard shape limits: length 8-320, no newlines, no fenced code, no pipe-tables.
- text_atoms.atom_type is a closed enum: title, claim, spec_clause, finding, alternative, next_step, operator_quote, legacy_import.
- decisions has decision_no, kind enum (substantive/schema_migration/calibration/disposition), title_atom_id FK, outcome_type enum, target_kind enum, target_key.
- decision_supports links a decision to a claim atom with basis enum: constraint, operator_directive, prior_decision, review_finding, deliberation.
- decision_effects records effect_kind (creates/modifies/supersedes/opens_issue/bumps_engine) against a target object_id.
- alternatives table holds label glob R-N.N and option_atom_id FK; alternative_rejections carry a basis enum and a non-null cited_object_id.
- Trigger: every substantive decision needs >=1 decision_supports row and >=1 alternatives row before close.
- Trigger: every alternative must have at least one alternative_rejections row.
- Trigger: every support and rejection must cite an existing object.
- Trigger: no session close if required assessment, decision, review, or close records are absent; no update or delete after session close.
- Trigger: no legacy decision/perspective/deliberation body writes after engine-v20.
- specs decomposed at clause granularity: specs, spec_versions, spec_sections, spec_clauses with clause_type and normative_level enums.
- spec_clauses.source_decision_id is NOT NULL: every clause is sourced from a decision.
- spec_clause_links uses relation enum supersedes/depends_on/implements to a target object_id.
**cli_surface.**
- selvedge submit kinds: session-open, read, assessment-item, deliberation-open, perspective-position, perspective-claim, deliberation-seal.
- selvedge submit kinds continued: decision-record, spec-version-open, spec-section, spec-clause, spec-version-seal.
- selvedge submit kinds continued: review-run, review-finding, finding-disposition, work-output, open-issue, next-step, session-close.
- selvedge export produces generated markdown only: specifications/*.md, prompts/development.md, prompts/application.md.
- selvedge export emits per-session views: 00-assessment.md, 01-deliberation.md, 02-decisions.md, 03-close.md, 04-review.md, manifest views.
- Standard session flow ends with: selvedge export --session NNN --write then selvedge validate --precommit.
**migration_path.**
- Ship engine-v20 as one additive migration under T-15: migration 003 creates new tables, indexes, close triggers, legacy-freeze triggers.
- Migration 003 does not drop old tables or columns; existing decisions.body_md, perspectives.body_md, deliberations.synthesis_md remain as read-only legacy sources.
- Backfill copies each old prose field into text_atoms(atom_type=legacy_import) and links it via legacy_imports(old_table, old_pk, atom_id, decomposition_status=unratified).
- Run explicit selvedge submit legacy-decompose payloads for the 11 decisions, 21 alternatives, 5 perspectives to create strict v20 facts.
- Engine-v20 lands when future writes use only v20 submit kinds and exports prefer v20 facts, falling back to legacy imports only for un-decomposed history.
**what_not.**
- Would not use a generic triples table as the main model: it makes structure look elegant while moving validation into application code and vocabulary discipline.
- Would not keep body_md plus a better parser: agents will satisfy the parser while hiding content in prose.
- Would not atomize all specification prose into triples: design intent needs readable clauses; strictness should be clause boundaries, source decisions, supersession, normative type.
- Would not use an LLM semantic validator as the refusal gate: it can review, but it must not be the substrate.
**open_question.**
- Ratify maximum text atom length: proposed 320 chars for session atoms and 700 for spec clauses.
- Ratify whether legacy rows may appear in exports with a legacy-import marker before ratification.
- Ratify the controlled enums for rejection bases and support bases.
- Ratify whether direct SQL is forbidden operationally, or only selvedge submit is blessed by convention.
- Ratify whether prompts are spec_ids with clause structure, or a separate prompt_versions table generated from the same clause machinery.

### P-2 (anthropic)

**Position.** Operator is right that prose-in-rows is a defect mode and wrong about the remedy: friction at the prose-cell boundary, not schema redesign that drives methodology toward atomized facts it cannot reassemble.

**what_lost.**
- Constraints.md §6 chain (addition consumes bandwidth; bandwidth was the diagnostic substrate; scaffolding compounds; trap is structural) loses its because-therefore tissue when atomized.
- Bandwidth being load-bearing in two senses simultaneously (work capacity and diagnostic capacity) is one inferential move; no triple captures the simultaneity.
- A reader reconstructing the §6 argument from triples would have to re-derive what the prose already contained.
- S082 03-close.md Honest-limit-3 is a handoff to a future reader: it anticipates a specific objection and supplies evidence to evaluate it.
- Triples cannot anticipate; they can only assert. Conditional rhetorical structures (if a future session disagrees) have no schema slot.
- Constraints.md §1: markdown is the right substrate for design intent; it is the wrong substrate for state. Forcing one to do the others job is the diagnosed failure mode.
**schema_sketch.**
- Add a derived body_md_word_count column on decisions, decision_alternatives, synthesis_points, engine_feedback to drive prose-density gates.
- Word-count gate at submit: <400 silent, 400-1200 requires --acknowledge-prose-density flag recorded on agent_runs, >1200 refused unless linked to a deliberation.
- For every substantive decisions row, T-17 requires body_md to parse for citable_alias references and at least one corresponding refs row in the same transaction.
- Same structural co-row rule applies to rejection_reason_md: structure lives alongside prose; prose carries reasoning, rows carry topology.
- Spec storage as whole-document blob: spec_versions.body_md TEXT NOT NULL with body_sha256 integrity check and body_path as export target.
- Required-section template enforced by writer not schema: substantive decisions need Position, Reasoning, What is rejected and why, What remains open.
**cli_surface.**
- selvedge submit --validate-prose: extract D-SNNN-N, OI-NNN-NNN, SPEC-*-vN refs and resolve against objects.citable_alias; refuse on unresolvable.
- selvedge submit --validate-prose: assert numeric claims (N tests pass, N tables, N decisions) against substrate counts; refuse on mismatch.
- selvedge submit --validate-prose: extract as established in / per N D-N patterns; cited decision must exist with compatible kind.
- selvedge submit decision --kind substantive --session NNN --title ... --body-file decision.md with --acknowledge-prose-density, --rejects, --cites flags.
- selvedge submit spec --spec-id methodology --version N --body-file path; selvedge validate --prose-claims as a separate gate.
- selvedge submit decision --interactive refuses to write until required template sections (Position, Reasoning, Rejected, Open) are present and non-empty.
**migration_path.**
- Ship the friction package as one migrations worth of additive change; do not redesign schema before the next external-problem trial.
- Specs land in substrate as whole-document body_md with FTS5 for queryability; not as decomposed atoms.
- Defer triples-table redesign until a future session, mid-trial, finds the friction package insufficient with prose-defects still occurring at the rate motivating S084.
**what_not.**
- Would not introduce a triples table as primary store for spec content: known cost (predicate-vocabulary debate), unknown benefit at one operator and ~5 sessions/week.
- Would not forbid prose in decisions.body_md, rejection_reason_md, synthesis_points.body_md, engine_feedback.body_md, deliberations.synthesis_md.
- Would not make the schema the gate for valid reasoning: schema gates facts and topology; the writer and reviewer gate reasoning.
- Would not ship spec decomposition before the first external-problem trial: the 078 D-5 release gate is load-bearing.
- Would not accept the operator framing nothing you are saying is being validated at face value: T-02, T-08, T-13, T-14 already constrain reasoning structure.
**risk.**
- Ceremony reincarnation: triples-table redesign produces ceremony around schema-migrations, predicate vocabularies, and inverse-relation conventions.
- Sessions that should be doing work would instead debate whether responds-to and addresses are the same predicate.
- Methodology-engine recursion: a session decomposing methodology.md into triples is a session not applying the engine to an external problem.
- Author-under-load failure mode A: author abandons the row and writes prose elsewhere, defeating the substrate.
- Author-under-load failure mode B: author produces technically-valid-but-meaningless triples to satisfy the schema.
- Substrate cannot distinguish meaningful from ceremonial triples; validator rubber-stamps both. LLMs are very good at producing structurally-valid output carrying no information.
- A schema rewarding structural validity creates the gradient the LLM optimizes against.
- Methodology becomes about its own data model: a redesign of magnitude prose-forbidden would consume S084-S087 minimum; at what point does the engine ship?
**open_question.**
- Q1: what specific defect in decisions.body_md content would the prose-density gate and prose-claims validator not catch? If preempting, the release gate applies.
- Q2: is the ask specs are queryable from substrate or specs are decomposed into atoms? First is solved by whole-document body_md with FTS5; second is what P-2 argues against.
- Q3: run the next external-problem trial against engine-v19 + friction package, or defer the trial until a triples-table redesign ships? Two are not compatible under the release gate.
- Q4: would you accept friction first, decompose later if a mid-trial finding proves the friction package insufficient?
- Q5: who authors the spec-content schema if specs become atoms? An LLM agent producing predicate vocabularies under load is the §6 failure mode in pure form.

### P-3 (anthropic)

**Position.** Keep body_md as a non-canonical human gloss column; force load-bearing content into typed-facet tables plus spec_section/spec_claim. No generic triples; do not drop body_md; migrate legacy rows lazily.

**schema_sketch.**
- Migration 003 is additive only (T-15 compliant). All new tables STRICT. Facet rows are small (label + value), agent-author cheap, export-cheap.
- facet_kinds(facet_kind, applies_to, cardinality) is a closed-vocabulary lookup table (same shape as role_write_capabilities) so vocab evolves via INSERT not ALTER.
- facet_kinds.applies_to enum: decision, alternative, spec_section, spec_claim, review_finding.
- facet_kinds.cardinality enum: required-1, required-1+, optional-*.
- Decision facets seeded: problem-statement (required-1), chosen-option (required-1), reason-carried (required-1+), open-question, precedent-cite (optional-*).
- Alternative facets seeded: why-rejected (required-1), cost-of-acceptance (required-1), precedent-cite (optional-*) -- the prose hole the operator named.
- Spec facets seeded: claim (required-1+ on spec_section), applies-to (optional-* on spec_claim).
- Review facets seeded: severity (required-1), what-breaks (required-1), suggested-fix (optional-*).
- decision_facets row: (decision_id, facet_kind, ord) UNIQUE; value_text length 8-400 forces tight prose, not essays.
- alternative_facets row: (alternative_id, facet_kind, ord) UNIQUE; value_text length 8-400; same trigger pattern as decision_facets.
- Trigger T-17 BEFORE INSERT on decision_facets aborts with E_REFUSAL_T17 if facet_kind not in facet_kinds with applies_to=decision.
- Trigger T-18 BEFORE INSERT on alternative_facets aborts with E_REFUSAL_T18 if facet_kind unknown for alternative.
- ALTER TABLE spec_versions ADD COLUMN body_canonical_in_substrate INTEGER NOT NULL DEFAULT 0 CHECK (0 or 1).
- spec_sections: ord, heading (length 2-120), intent_md (length 16-600), object_id FK; UNIQUE (spec_version_id, ord).
- spec_claims: ord, claim_text (length 16-400), object_id FK; UNIQUE (spec_section_id, ord).
- review_findings table: session_id, iteration (1-4), target_object_id, severity enum (critical/high/medium/low), disposition enum (fixed/adjudicated/open).
- review_finding_facets follows the same facet pattern; trigger T-19 enforces closed vocabulary.
- Trigger T-20 BEFORE UPDATE OF status on sessions blocks open->closed if any alternative is missing a required facet_kind row.
- Trigger T-21 mirrors T-20 for decision_facets; T-22 mirrors for spec_claims when body_canonical_in_substrate=1.
- rejection_reason_md NOT NULL stays (T-15 forbids drop). Treat it as denormalised summary equal to why-rejected facet ord=1; CLI checks agreement at insert.
**cli_surface.**
- New submit kinds: decision-facet, alternative-facet, spec-section, spec-claim, assessment, review-finding, review-finding-disposition.
- Revised decision payload: back-compat shape with optional facets[] and alternatives[].facets[] blocks lifted into the same JSON.
- CLI handler extends _submit_decision in cli.py:578 to write decisions, decision_alternatives, and alternative_facets in one transaction; missing required facet -> E_VALIDATION.
- selvedge export specs --to specifications/ regenerates spec markdown from spec_sections + spec_claims.
- selvedge export provenance --session 83 regenerates 02-decisions.md and other per-session views.
- Export uses Jinja-style templates in selvedge/templates/; output is byte-stable given identical inputs (sort by ord, fixed line endings).
- Validator gains a round-trip check: selvedge export specs --diff exits non-zero on drift between substrate facts and on-disk markdown.
**schema_sketch.**
- Spec granularity: H2 section + claim (paragraph-level), not sentence-level. Sentence-level cost dominates; section-level hides facets.
- Spec decomposition target: methodology.md ~9 sections x ~3 claims = ~27 spec_claims; workspace.md ~18; constraints.md ~15.
- engine-manifest.md stays file-canonical (body_canonical_in_substrate=0): it is enumeration plus version history; round-trip cost is high.
- refs.relation widening proposed: cites, supersedes, responds-to, depends-on, closes, applies-to, derived-from, restates.
- T-15 blocks the refs CHECK widening; workaround is a refs_relation_extra table (additive, joined at read). Ugly but T-15-clean.
**migration_path.**
- 13 decisions + 21 alternatives + 5 perspectives currently carry body_md / rejection_reason_md prose; backfill via VIEW v_legacy_rows that computes legacy at read.
- VIEW v_legacy_rows preferred over a column: zero writes, no T-06 conflict on closed sessions.
- T-20 and T-21 close-gate triggers exempt legacy=1 rows via NOT IN (SELECT FROM v_legacy_rows). New rows from S084 onwards must carry full facets.
- Re-authoring legacy rows is opportunistic: a future session that touches a legacy decision MAY back-decompose it; not required.
- Most of the 21 alternatives are S078-S082 methodology work with tight rejection_reason_md (>=16 char floor binding); they are not the prose hole.
- Spec versions methodology.md v3, workspace.md, constraints.md need a one-time decomposition by an S084 specifier-agent (~60 INSERTs total, one focused session).
**what_not.**
- Would not introduce a generic triples table: predicates become a free-text vocab drift sink within two sessions. Closed facet_kinds is the same shape with vocab pinned.
- Triples-with-checked-predicates IS facet_kinds; calling it triples invites generality we do not need.
- Would not drop body_md: T-15 blocks it anyway; even allowed, keep it as render hint. Forcing all prose through facets makes author write 5+ rows per paragraph.
- Would not do per-claim git-tracking (one file per claim): round-trip cost explodes; review diffs become unreadable.
- Would not use sentence-level granularity: author cost greater than prose-discipline gain.
- Would not strict NOT NULL body_md drop (T-15 blocks). Keep NOT NULL; accept body_md as one-line gloss with ~5 sec author cost.
- Would not live-rewrite the 13 closed-session decisions: T-06 protects them; legacy=1 + view is the clean path.
**open_question.**
- Q1: objects.object_kind CHECK widening for spec_section, spec_claim, review_finding kinds. Options: objects_v2 sibling + UNION view, or interpret T-15 as forbidding only destructive widening.
- Q1 preference: option (ii) with explicit ratification recorded as a calibration in S084, because objects_v2 poisons every JOIN against objects.
- Q2: body_canonical_in_substrate=1 for engine-manifest.md? Argued no. If yes, ~40 version-history claims become INSERT lines.
- Q3: facet length ceiling 400 chars. Constraints §2 has paragraphs longer than that; may need a claim_long column or relax to 800.
- Q4: spec round-trip byte-identity. OK with normalised output (CRLF->LF, trailing-newline-required, two-blank-lines-between-H2)? If yes, current spec files need a one-shot reformat at S084 open.
- Q5: legacy_prose via VIEW vs column. View avoids T-06; column is more query-friendly. Lean view.
- Q6: lifting S083 04-review.md into substrate at S084 means S083 close itself will not be decomposed (legacy). Acceptable?

### Synthesis

# Deliberation 3 — Synthesis (preserves dissent)

Three perspectives on: substrate data model for prose-free session state and specifications. Synthesis is not a decision; it feeds operator ratification per `methodology.md` §When to convene multiple agents.

## Convergences (>=2 perspectives agree)

- **C-1. Reject a generic triples table.** P-1 and P-3 explicit; P-2 implicit (rejects RDF-with-sqlite). Reasons differ: P-1 says triples push validation into application code and predicate-vocabulary discipline; P-3 says a closed `facet_kinds` lookup is the same data shape with the vocab pinned, so don't dress it up as triples; P-2 says triples-as-primary-store has known cost and unknown benefit at this scale.
- **C-2. Single additive migration under T-15.** All three would ship as one migration that adds tables/columns and triggers, never drops. P-1 and P-3 give concrete migration shape; P-2 limits the migration to friction additions, not decomposition.
- **C-3. If decomposing specs, paragraph/claim is the right granularity.** P-1 lands at clause-level with `clause_type` and `normative_level`; P-3 at H2-section + paragraph-claim. Both reject sentence-level (author cost > gain). P-2 disputes that decomposition should happen at all.
- **C-4. `engine-manifest.md` is special.** P-3 says: file-canonical, no decomposition, round-trip cost > strictness gain. P-2 agrees by extension (whole-document for everything). P-1 doesn't single it out but its clause schema would handle it.

## Divergences

- **D-1. Fate of `body_md` columns.** P-1: drop entirely; semantic tables have no `body_md`/`reason_md`/`summary_md`/nullable notes; the only writable language slot is a typed `text_atoms` row, length 8-320, no newlines, no fenced code, no pipe tables. P-3: keep `body_md` as non-canonical render hint; load-bearing content moves into `decision_facets` and `alternative_facets` with closed vocabulary; T-15 blocks dropping it anyway. P-2: keep `body_md` as the *primary* surface for connected reasoning; add friction (word-count gates, required co-rows, defect-pattern validators) but do not force prose into atoms.
- **D-2. Whether strict-decomposition is the right direction at all.** P-1, P-3: yes — the operator's challenge stands and the substrate must refuse what it currently admits. P-2: no — the operator is right that prose-in-rows is a defect mode and wrong about the remedy. Strict decomposition amputates the connected-reasoning asset 75 sessions have demonstrated value in producing.
- **D-3. Whether to ship at S084 or after the external trial.** P-1, P-3 imply S084 (give concrete migration 003 SQL). P-2 explicitly: 078 D-5 release gate forbids; ship friction-only at S084 and reconsider after the external trial.
- **D-4. Spec content shape.** P-1: spec_clauses with clause_type, normative_level, source_decision_id; spec_clause_links for supersedes/depends_on/implements. P-3: spec_sections + spec_claims with body_canonical_in_substrate flag, manifest stays file-canonical. P-2: `spec_versions.body_md TEXT NOT NULL` whole-document with sha256 integrity-check + FTS5 indexing; markdown is canonical inside the row.

## Minority positions (preserved, not erased)

- **M-1 (P-2). Technically-valid-but-meaningless triples.** "A pedantic schema produces two failure modes: author abandons the row and writes prose elsewhere, defeating the substrate; or author produces technically-valid-but-meaningless triples — `(D-S084-1, addresses, D-S083-2)` with no body — to satisfy the schema. The substrate cannot distinguish meaningful from ceremonial triples." Worth preserving because it names the LLM-author failure mode in its sharpest form: models are very good at producing structurally-valid output carrying no information, and a schema rewarding structural validity creates the gradient the LLM optimizes against. This is constraints §6 (recursive trap) in a different costume.

- **M-2 (P-2). "Ceremony reincarnated in a different form" risk.** P-2 quotes `constraints.md` §"Risks the successor must hold" verbatim: *"A database introduces schema-evolution overhead and the possibility of state-substrate-substrate-protection ceremony reincarnated in a different form. The substrate must be load-bearing — counters derived, references checked — or the same prose-state failure mode will reappear in queries-as-prose form."* P-2 argues strict decomposition is the canonical instance of that warning. Worth preserving because the warning is in the engine's own active spec; ignoring it requires a stated reason, not silence.

## Shared concerns surfaced by >=2 perspectives

- **Widening `objects.object_kind` CHECK / `refs.relation` CHECK is blocked by T-15.** P-3 names this as Q1 (sibling table vs. operator-ratified reading of T-15). P-1 doesn't address but its schema would face the same issue. Operator must rule.
- **Legacy rows (13 decisions, 21 alternatives, 5 perspectives) cannot be live-rewritten.** T-06 protects them. P-1 proposes `legacy_imports` table + opt-in decompose. P-3 proposes a `v_legacy_rows` view + close-gate exemption + opportunistic re-authoring. Both converge on opportunistic, not forced.
- **Round-trip byte-identity for spec exports.** P-1 implies template determinism; P-3 makes it an explicit Q4 (CRLF→LF, trailing-newline, two-blank-lines-between-H2 normalisation; one-shot reformat at S084 open). P-2 sidesteps because it stores whole-document.

## What synthesis is NOT

This synthesis does not pick a winner. The methodology forbids that: synthesis feeds Decide; the operator decides. The three positions are coherent and load-bearing in different ways. Picking among them requires answering questions the deliberation cannot answer:

1. What is the operator's tolerance for ceremony before the external trial? (P-2's release-gate concern.)
2. What is the actual defect rate of prose-in-rows that justifies the redesign? (P-2's Q1.)
3. Is the ask "specs queryable from substrate" or "specs decomposed into atoms"? (P-2's Q2 — the two have very different cost.)
4. Is the operator willing to author closed vocabularies under load, or should P-2's friction-package run as a trial and re-deliberate if it fails?

These are operator decisions. The session halts here.


### Synthesis points

- **convergence C-1.** Reject a generic triples table.
- **convergence C-2.** Migration must be additive only under T-15.
- **convergence C-3.** If decomposing specs, paragraph/claim is the right granularity (not sentence).
- **divergence D-1.** Fate of body_md columns: drop entirely (P-1) vs keep as render hint (P-3) vs keep as primary surface (P-2).
- **divergence D-2.** Whether strict-decomposition is the right direction at all.
- **divergence D-3.** Ship at S084 vs after the external trial.
- **divergence D-4.** Spec content shape: clauses vs facets vs whole-document blob.
- **minority M-1.** LLM-author failure mode: technically-valid-but-meaningless triples.
- **minority M-2.** Ceremony reincarnated risk; constraints.md Risks-the-successor-must-hold quoted verbatim.
