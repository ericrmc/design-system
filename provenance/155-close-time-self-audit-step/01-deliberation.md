---
session: 155
title: close-time-self-audit-step — deliberation
generated_by: selvedge export
---

# Deliberation

## D-21 — Shape of close-time self-audit step for OI-S154-2 + OI-S154-3 (assumption surfacing + interpretive-choice inventory)

sealed_at: 2026-05-01T19:07:05.389Z

### P-1 (anthropic)

**Position.** Substrate-enforce close audit via new interpretive_choice table + T-NN trigger refusing close until implicit assumptions are linked to A-NNN or FR; scope S154-2/3 only, not S154-5.

**schema_sketch.**
- New table interpretive_choice: cols audit_id PK, session_id FK, kind enum (implicit_assumption / interpretive_choice / counterfactual_dependency), atom_id, linked_a_nnn_id, linked_fr_id, created_at.
- New trigger T-NN at session.before_close: refuse close if no interpretive_choice row for session, or any kind=implicit_assumption row has both linked_a_nnn_id and linked_fr_id NULL.
- No changes to existing assumption_register, forward_references, or engine_feedback schemas.
- Column interpretive_choice.kind is closed enum enforced by check constraint.
**cli_surface.**
- bin/selvedge submit close-audit --session <id> --kind implicit_assumption --atom <text> creates row, optionally with --link-a-nnn or --link-fr.
- If unlinked implicit_assumption rows exist at submit-time, command rejects with error listing them and instructions to create matching A-NNN or FR.
- Alternatively single --interpretive-choices JSON payload [{kind,atom,linked_a_nnn_id?,linked_fr_id?}]; empty list requires explicit --empty-acknowledged flag.
- Submit produces perspective_claim rows in engine_feedback (metadata: session, timestamp, author); audit rows go to interpretive_choice table.
**migration_path.**
- Bump engine-manifest to include T-NN definition (no version change needed; manifest evolves in place).
- Prompt-development §8.5 revised to mandate close-audit step: enumerate implicit assumptions, decision-forks, counterfactual dependencies; lift to A-NNN or defer via FR; engine refuses close until linked.
- Methodology v9 extended: close phase explicitly includes audit sub-step with required payloads.
- One-time migration on existing sessions inserts stub interpretive_choice rows with kind=audit_backfill and null links; non-blocking but distinguishes pre/post-enforcement.
- Testing: verify T-NN blocks close on unlinked implicit_assumption rows; verify submit rejects empty audit unless flagged; verify audit rows link to A-NNN and FR.
**what_not.**
- Does NOT modify the assumption_register schema or affect existing A-NNN rows; only adds link-from metadata.
- Does NOT enforce that assumptions be correct or complete; only that implicit ones be surfaced and accounted for (linked or deferred).
- Does NOT apply to sessions opened before this version lands; backfill stub rows allow opt-in or bulk compliance via operator tooling.
- Does NOT fold S154-5 (deliberation-grading / seal-time counterfactual naming) into this seam; that remains a separate decision at a different phase.
- Does NOT create a new session-close verb; the gate fires on the existing session-close call.
**open_question.**
- Should counterfactual_dependency enum value in interpretive_choice.kind be scoped to this audit, or left open for future use? Propose: keep it; forward-compatibility is cheap.
- Should atom_id column be FK to a text_atom table for full provenance, or free text? Propose: free text now (lighter migration) but design column to allow upgrade to FK later.
- What happens when operator closes session with trivial/no interpretive choices (e.g., pure housekeeping)? Propose: require explicit --empty-acknowledged flag at submit to bypass empty check.
- If a forward_reference is later resolved, should interpretive_choice.linked_fr_id be nullable again or row remain immutable? Propose: immutable; resolved assumption gets its own A-NNN and new FR.
**risk.**
- Migration cost: all existing sessions require backfill rows or explicit acknowledgement. Operator burden if sessions cannot be bulk-processed.
- Noise risk: trivial sessions forced to articulate 'no interpretive choices' explicitly may feel bureaucratic. Mitigation: lightweight --empty-acknowledged flag.
- False negatives: operator listing 'no interpretive choices' without genuine audit passes the gate. Surfacing is mandatory; judgment of completeness remains human-owned.
- Bind risk: interpretive_choice rows in downstream queries (impact analysis, dependency graphs) may produce artifact data; mark backfill rows and exclude unless requested.
- Coupling risk: T-NN trigger on session-close becomes a hard coupling point. Future session lifecycle changes (draft vs committed) may need T-NN revision.
**what_lost.**
- The simplicity of the analogy to temporal-claim grounding: this proposal costs more than clause + calibration-EF recovery.
- The ability to close sessions without explicit audit overhead; under this proposal, every session closure demands at least a 'no interpretive choices' declaration.
- The flexibility to defer this mechanism to operator discipline: if enforcement proves over-rigid, moving to substrate enforcement makes backtracking harder.
- Potential adoption by adjacent teams who prefer lighter-weight audit surfaces (pure prose, no schema); this schema locks in a specific data model.

### P-2 (anthropic)

**Position.** Add a single §8.5 prose clause mandating close-time interpretive-choice inventory, operator-policed like temporal-claim grounding; OI-S154-2/3 only. No new tables, submit-kind, or trigger; existing composition + calibration-EFs suffice.

**schema_sketch.**
- No new tables. assumption_register, forward_references, engine_feedback, open_issues already compose to carry every artefact this clause needs to produce.
- No new columns on existing tables. At-close vs in-session lifts derivable from created_at against close-record timestamp if needed.
- No new T-NN trigger. T-18, T-19, T-20, T-22, T-23, T-29, T-30, T-39, T-40 are existing close-gate set; adding a tenth is mass without evidence.
- No new submit_kind enum value. Audit observation goes through existing engine_feedback submit kind with flag=observation and structured headline prefix audit-step:.
- The flag=observation row IS the audit artefact; body_md enumerates load-bearing interpretive choices and resolutions (lifted to A-NNN, deferred to FR, accepted-as-implicit with reason).
**cli_surface.**
- bin/selvedge submit engine-feedback with flag=observation, headline starting audit-step:, body lists each load-bearing interpretive choice and disposition (A-NNN lift, FR open, accept-implicit-with-reason).
- For each interpretive choice that needs lifting: existing bin/selvedge submit assumption call writing an A-NNN row — the call operators already make.
- For each interpretive choice that needs future revisit: existing bin/selvedge submit forward-reference call producing FR-S<wno>-<seq> — the call operators already make.
- No new flags on bin/selvedge submit close-record. Clause says 'before submitting close-record'; ordering is operator-policed prose, identical to temporal-claim grounding clause.
- One concrete row, three existing submit kinds composed — zero new CLI surface.
**migration_path.**
- prompt-development v11 to v12: insert close-time interpretive-choice inventory clause into §8.5 under temporal-claim grounding; mirror its phrasing so operator-policed pattern is visibly the same.
- methodology v9 to v10: mention §8.5 addition in Close phase narrative; one paragraph, no structural change.
- prompts/application.md: add inventory question to Close-phase checklist already there.
- No engine-manifest bump; engine-v44 stays engine-v44 because no kernel mechanism, trigger, table, column, or submit-kind changes.
- No SQL migration. The next migration (030+) is reserved for whatever genuinely needs schema.
- OI-S154-5 closed as separate-clause-deferred or moved to its own session; not folded.
**what_not.**
- Does NOT introduce a kernel-mechanism trigger refusing close until audit row exists; OI-S154-2's 'kernel mechanism' framing reinterpreted as 'kernel-spec clause', not substrate gate.
- Does NOT add an interpretive_choice table. Text atoms in an engine_feedback body carry the same information without committing to a schema before the shape is proven.
- Does NOT extend assumption_register with audit-derived columns. Provenance via created_at and the linking observation row is enough.
- Does NOT add a close-time-audit submit kind; another enum value is debt that has to be retired or maintained.
- Does NOT fold OI-S154-5 into this clause; seal-time and close-time are distinct triggers and conflating them muddies both.
- Does NOT prescribe an exhaustive taxonomy of 'load-bearing interpretive choice'; operator judgement, with calibration-EF recovery, is the precedent.
**open_question.**
- Does the prose clause achieve a meaningfully better gap-closure rate than 11/25 baseline, or does prose-only enforcement plateau at the same rate? Only the next external-problem arc tells us.
- If gap-closure stays poor after one full arc under the clause, does that argue for a substrate gate then — or for tightening the prose, as temporal-claim grounding has been tightened in place?
- Should the inventory be a free-prose enumeration in the body, or a lightly-structured headline schema (audit-step: N choices, M lifted, K FRs)? Either fits; pick the lighter.
- Is there a measurable signal (count of A-NNN lifted in close-window vs in-session) we should start tracking now so the next deliberation has data?
**risk.**
- Prose clauses get skimmed; a Close-phase that already enumerates many obligations may absorb the new clause without compliance change. Mitigation: calibration-EF recovery, same as temporal-claim grounding.
- Operator/agent judgement of 'load-bearing' varies; under-inventory hides exactly the failures OI-S154-2 names. Mitigation: peer review at next arc, calibration-EF when caught.
- Without a typed surface, querying 'which sessions ran the audit' requires substring-matching headlines in engine_feedback — fine at current scale, friction later.
- If next arc shows same 44% gap-closure under clause, we will have spent a session validating prose-only and another adding a gate; total cost exceeds gate-now if gate was inevitable.
- Sibling OI-S154-5 stays open; if it doesn't get its own session quickly it drifts.
**what_lost.**
- Lost: the strong invariant a substrate gate provides — 'no session closes without an audit row' becomes 'no session SHOULD close without an audit row', and SHOULD has a known compliance discount.
- Lost: structured queryability over interpretive choices. A typed table would let future sessions query unlifted load-bearing choices in S140–S155; under prose-only that is grep.
- Lost: the option to fold OI-S154-5 into one coherent self-audit surface; deliberation-grading and close-audit stay separately spec'd.
- Lost: a chance to mark assumption_register rows with their lifting context (in-session vs at-close), which would let next gap-closure measurement be exact rather than estimated.
- Gained-by-losing: spec parsimony, reviewability of §8.5, no migration, no new enum, no new trigger to maintain — clean A/B against temporal-claim precedent for evidence-based next deliberation.

### P-3 (openai)

**Position.** S154-2/3 describe failed use of plan-time surfaces, not need for new close-time mechanism. Add only one §8.5 reminder to lift load-bearing assumptions as A-NNN at authoring; use calibration-EFs on miss. Exclude S154-5; no new substrate.

**schema_sketch.**
- No schema change: assumption_register remains the sole register for load-bearing assumptions.
- No new interpretive_choice table; would duplicate A-NNN semantics and invite late paraphrase instead of timely lifting.
- No new close-time audit table, submit kind, or trigger; close should not certify reconstructed intent as if it were contemporaneous evidence.
- No changes to forward_references; FRs remain for future work, not a substitute for registering assumptions already used in prose.
- No changes to perspective_claim; open_question, risk, and what_lost already hold deliberative uncertainty when the session is a deliberation.
- Optional spec text only: one §8.5 bullet reminding that plan-prose must not depend on unregistered load-bearing assumptions.
- Calibration-EFs use existing engine_feedback rows with flag=calibration and a structured headline citing the missed assumption.
- No T-NN gate: the kernel should not block close merely because an audit-shaped row exists or does not exist.
**cli_surface.**
- Normal plan authoring remains unchanged: when prose relies on an interpretive choice, submit or cite the relevant A-NNN before or with that prose.
- No bin/selvedge submit close-time-audit; adding it would move attention from plan-time discipline to close-time reconstruction.
- At close, the operator reads §8.5 and confirms there is no known unregistered load-bearing assumption in submitted plan-prose.
- If a miss is noticed, use bin/selvedge submit engine-feedback --flag calibration with body naming prose, missing A-NNN, and correction path.
- Calibration payload shape: headline, quoted prose locator, missing assumption stated as an A-candidate, why it was load-bearing, and recommended next-session triage.
- If missing assumption still needed before close, register it as A-NNN then cite the calibration-EF as evidence of the slip.
- If the miss is found after close, leave the substrate history intact and let the next session triage the calibration-EF.
**migration_path.**
- Bump prompt-development v11 to v12 only if a version bump is required for the single §8.5 reminder.
- Bump methodology v9 to v10 only if methodology owns the close checklist text; otherwise leave methodology unchanged.
- Do not bump engine-manifest for schema or CLI changes, because there are none.
- Add the §8.5 reminder: load-bearing assumptions in plan-prose are lifted at authoring time, not reconstructed at close.
- Add one example calibration-EF pattern for unlifted assumption slips, reusing the established temporal-claim calibration style.
- Triage OI-S154-2 as practice-remediated without new kernel machinery, while keeping evidence open to future recurrence.
- Triage OI-S154-3 as narrowed: no close-time inventory step, only the authoring-time reminder and calibration recovery.
- Leave OI-S154-5 out of this migration; handle deliberation-seal grading separately if it still needs action.
**what_not.**
- Do not create a second assumption register under a softer name.
- Do not make close-time audit rows a proxy for actual A-NNN registration.
- Do not add a close gate that can be satisfied by formulaic prose while leaving plan authoring habits unchanged.
- Do not fold S154-5 into close, because seal-time counterfactual naming has a different trigger and actor.
- Do not require every interpretive choice to become an FR; FRs are for future review, not cleanup for missing present assumptions.
- Do not mine plan prose automatically for assumed claims; false positives create review theater and false negatives are trusted too much.
- Do not treat retrospective inventory as reliable evidence of what governed earlier reasoning.
**open_question.**
- What exact threshold makes an assumption load-bearing enough to require A-NNN lifting at authoring time?
- Who is accountable for catching a missed A-NNN before close: author, reviewer, closer, or next-session triage?
- Should repeated calibration-EFs for the same failure later reopen the question of substrate enforcement?
- How should a session distinguish an ordinary omitted detail from an implicit assumption that changed the plan's validity?
- Does S154-5 need a separate seal-time checklist, or is it also just missed use of existing deliberation fields?
**risk.**
- The same non-use pattern can recur because this proposal deliberately rejects a hard gate.
- Operators may read the §8.5 reminder as closing paperwork rather than as plan-time discipline.
- Calibration-EFs depend on readers noticing failures; silent failures remain silent.
- Partially closing the issue without mechanism may look like minimizing the 44% gap-closure evidence.
- Without a new typed surface, later analysis must inspect A-NNN rows and calibration-EFs rather than query a dedicated audit table.
- A weak culture may convert calibration-EFs into blame records instead of improving authoring practice.
**what_lost.**
- Lost relative to a trigger: no mechanical refusal of session close when no audit artifact exists.
- Lost relative to a new table: no clean query for all close-discovered interpretive choices.
- Lost relative to close-time inventory: no ritual forcing function that makes the closer reread all plan-prose for hidden assumptions.
- Lost relative to self-review FRs: fewer automatic future-session hooks for choices discovered late.
- Lost relative to folding S154-5: no unified self-audit surface across close and deliberation seal.
- Lost relative to automation: no substrate-generated candidate list of implicit assumptions for operator review.

### P-4 (openai)

**Position.** Graduated mechanism for OI-S154-2/3 only (S154-5 sibling). v1: operator-policed close-audit writing to light typed close_audit_items table; v2 T-NN gate promotion conditional on calibration-EF naming an unlifted miss.

**schema_sketch.**
- Add close_audit_items as the minimal typed surface, separate from engine_feedback so audit inventory does not blur with free-prose feedback.
- Columns: id, session_id, item_seq, kind text, atom_id, body_md, linked_object_id nullable, created_at, created_by.
- kind is text with no CHECK in v1; it is a typed-observation field, not an enum pretending the category system is already known.
- atom_id binds each row to the close submit text atom or equivalent substrate atom, keeping the item inspectable instead of buried in a paragraph.
- linked_object_id resolves aliases to A-NNN, FR-SNNN-N, OI-SNNN-N, or null; v1 permits null because some interpretive choices are newly discovered.
- Add an index on (session_id, item_seq) and a lookup index on linked_object_id; do not add a close-blocking trigger in v1.
- Store audit-derived assumptions as normal assumption_register rows, but add source=close_audit only if register already has a source field or cheap nullable extension.
- Add a spec-level trigger condition, not a substrate trigger: close-without-audit plus later calibration EF naming an unlifted assumption promotes design to a T-NN gate.
**cli_surface.**
- Operators submit one row per load-bearing interpretive choice: bin/selvedge submit close-audit-item --session S155 --kind interpretive-choice --text "..."
- If audit discovers a missing assumption, first register the assumption, then link the audit item with --link A-NNN so the inventory proves the lift occurred.
- If choice needs future review, submit the FR and link the audit item with --link FR-S155-N; item text states the choice and reason review is needed.
- The payload is one concise atom: choice made, why it mattered, whether it became an A row, whether it became an FR, and what evidence was checked.
- Session close remains bin/selvedge submit session-close ...; v1 prompt text says close is invalid by discipline if no audit item or explicit no-items item exists.
- A clean close may submit --kind no-load-bearing-choice --text "No unregistered load-bearing interpretive choices found at close."
- Do not use engine_feedback for normal audit items; reserve EF for calibration when the audit discipline failed or needs repair.
**migration_path.**
- Bump prompt-development v11 to v12 with a close-time inventory clause requiring audit items before session-close or an explicit no-items row.
- Bump methodology v9 to v10 to define close-audit actor, timing, payload, and relation to assumption registration and self-review FRs.
- Add a migration creating close_audit_items, indexes, and the new close-audit-item submit kind; bump engine-manifest from engine-v44 to engine-v45.
- Add prompt language for OI-S154-5 as a sibling seal-time clause: deliberation seal names its counterfactual, but it is not folded into the close gate.
- Add a monitoring rule: if calibration EF names a prior close as missing an audit row for an unlifted assumption, open the v2 gate-promotion issue automatically.
- After several sessions, review observed kind values and graduate stable ones to an enum only if they improve validation or query value.
- If gate promotion fires, add T-NN requiring at least one close_audit_items row for session_id before accepting session-close.
**what_not.**
- Do not fold OI-S154-5 into the same close trigger; deliberation seal is a different lifecycle event with different responsibility.
- Do not create a full interpretive-choice ontology in v1; the engine needs evidence from use before it names permanent categories.
- Do not make kind a CHECK enum yet; early enum certainty would encode guesses and force churn.
- Do not use prose-only §8.5 text as the whole fix; OI-S154-2 asks for a kernel mechanism, and typed rows are the minimum credible substrate foothold.
- Do not make an immediate T-NN gate; a brittle first gate can reward empty compliance and block closes before the payload standard is calibrated.
- Do not replace assumption_register; audit items point to lifted assumptions but do not become the assumption system.
- Do not treat a self-review FR as optional when the audit identifies a real unresolved interpretive choice.
**open_question.**
- What exact alias grammar should linked_object_id accept so it is useful without creating a polymorphic foreign-key trap?
- How many sessions of observed kind values are enough before enum graduation is justified?
- Should a no-items audit row require a distinct kind, or should absence plus close prose be acceptable for trivial sessions?
- Who decides that a downstream calibration EF names the trigger condition strongly enough to force gate promotion?
- Should audit-derived assumptions receive an explicit source column, or is linkage from close_audit_items enough provenance?
- Can deliberation-seal counterfactuals reuse this table later, or should they get a separate seal-audit table if volume grows?
**risk.**
- v1 operator-policing can fail like temporal-claim grounding slipped: recovery may be a post-hoc calibration EF, not prevention.
- A text kind field can fragment into near-duplicates, making queries noisy until a graduation pass normalises the observed categories.
- Operators may satisfy the row requirement with vague no-items entries, producing substrate presence without real assumption surfacing.
- Polymorphic linked_object_id can become loose unless alias resolution is deterministic and failed links are visible.
- Deferring the gate may leave one more external-problem arc exposed if discipline does not improve immediately.
- Separating audit rows from engine_feedback adds a new surface that must be maintained, documented, and exported.
**what_lost.**
- Relative to an immediate gate, v1 loses guaranteed prevention of closes without audit rows.
- Relative to a full new interpretive-choice table with enums, v1 loses strong category validation and mature reporting on day one.
- Relative to prose-only §8.5, this loses zero-migration simplicity and asks operators to make explicit CLI submissions.
- Relative to folding OI-S154-5, this loses a single unified self-audit banner across close and seal events.
- Relative to extending engine_feedback, this loses reuse of a familiar free-prose path, but preserves separation between audit inventory and feedback.
- Relative to marking every A row directly, this loses a pure assumption-register view of close-derived choices, but keeps unresolved choices and FR needs visible.

### P-5 (openai)

**Position.** Cover only OI-S154-2/3 (S154-5 is seal-time). Start as operator-policed §8.5 clause with promotion path to presence-only gating after calibration evidence. Use a narrow close-time-audit submit kind writing structured engine_feedback rows.

**schema_sketch.**
- No new interpretive_choice table initially; a new noun invites every adjacent decision to become audit inventory.
- Add submit kind close-time-audit that writes engine_feedback with flag=observation and a structured headline naming session, counts, and whether new A/FR rows were created.
- Add an optional source_phase or equivalent metadata on assumption_register only if the substrate already has a local pattern for provenance columns.
- If adding A provenance is too invasive, encode source=close-time-audit in the A body using the existing structured-headline pattern.
- forward_references stays unchanged; self-review FRs are ordinary FR rows whose body cites the audit EF and any A rows created at close.
- Do not add a trigger in the first landing; document a future presence-only T-NN that checks for one audit EF before session-close.
- Define 'load-bearing interpretive choice' in spec text as a choice needed to justify plan/prose/spec meaning and not already carried by substrate rows.
- Explicit exclusions: micro-decisions reflected in committed spec rows, choices resolved by citing an existing A row, and choices covered by closed FR/OI rows.
**cli_surface.**
- At close, run bin/selvedge submit close-time-audit --session S155 with markdown body following fixed headings: inventory, registered_now, self_review_frs, exclusions, nil_reason.
- If no qualifying choice exists, submit the same kind with inventory: none and a short nil_reason tied to the exclusion criteria.
- When the audit finds an unregistered load-bearing choice, first submit the needed A row, then cite it in registered_now.
- When a choice needs future validation, submit an FR that cites the audit EF and the relevant A row, then list the FR id in self_review_frs.
- The audit payload must name exclusions applied; this prevents 'nothing was load-bearing' from becoming an unargued escape hatch.
- The CLI should not ask the operator to classify seal-time counterfactuals here; that is outside close-time audit.
**migration_path.**
- Bump prompt-development v11 to v12 with the close-time audit clause and the definition/exclusion list for load-bearing interpretive choice.
- Bump methodology v9 to v10 to describe close ordering: audit inventory, register missing A rows, create self-review FRs, then close.
- Add the close-time-audit submit kind and route it to engine_feedback using existing structured-headline conventions.
- Land an engine-manifest update only if submit-kind registration is manifest-owned in engine-v44.
- Do not add a gating trigger until at least one calibration arc shows whether the structured audit row is consistently produced and useful.
- If later promoted, add a T-NN trigger that checks audit-row presence before close, not content quality or completeness.
- Close OI-S154-2 and OI-S154-3 only after the spec text, submit surface, and first live audit row exist.
- Leave OI-S154-5 open or move it through a separate deliberation-seal mechanism with its own trigger point.
**what_not.**
- This does not fold deliberation-grading into close-time reflection; S154-5 has a different actor, moment, and evidence shape.
- This does not define load-bearing as every judgement, wording choice, ordering choice, or local implementation preference.
- This does not require self-review FRs for choices already resolved by an existing A row, closed FR, closed OI, or explicit spec row.
- This does not make the substrate decide whether an interpretive choice is important enough; that remains an authored judgement.
- This does not block session-close on subjective audit quality in the initial version.
- This does not turn engine_feedback into a general registry for all decisions; it is only the audit artifact and citation hub.
- This does not replace the assumption_register; unregistered assumptions discovered at close must still become A rows.
**open_question.**
- What exact metadata field, if any, should mark A rows as audit-derived without causing a schema migration larger than this issue needs?
- How should a later presence-only trigger identify the correct audit EF if multiple close-time audit rows are submitted?
- What minimum citation standard should an audit item meet when it claims a choice is already covered by an existing substrate row?
- Should nil audits require a second reviewer after repeated arcs, or is calibration evidence enough to detect abuse?
- Which session phase owns the final audit command if close preparation and formal close are separate engine phases?
**risk.**
- Operator-policed adoption may underperform if agents treat the audit as a closing ritual rather than a search for missing A rows.
- A nil_reason path can become a loophole unless exclusions are concrete and cited.
- Adding A provenance may distract from the core fix if the migration becomes larger than the close-time audit itself.
- A later presence-only trigger could create false confidence; presence of an audit row is not evidence of audit quality.
- The definition may still be gamed by classifying broad assumptions as ordinary prose choices.
- Keeping S154-5 separate may leave a visible adjacent gap until a seal-time mechanism is designed.
**what_lost.**
- Excluding S154-5 loses the appeal of one unified self-audit surface across sessions and deliberations.
- Avoiding a new interpretive_choice table loses first-class queryability over every audited choice.
- Starting without a trigger loses immediate hard enforcement against close without an audit row.
- Presence-only future gating loses any fantasy of the substrate proving completeness or importance.
- Strict exclusions lose broad reflective coverage of small design judgements that might later look important.
- Reusing engine_feedback loses some schema purity compared with a dedicated close-audit table.

### Synthesis

# Synthesis — D-21 close-time self-audit step

The five perspectives split sharply on D-2 (authority) and D-3 (substrate shape) but converged on D-1 (scope). Synthesis adopts a graduated mechanism: substrate-conservative at v1, with named promotion triggers preserving the stronger positions as forward paths.

**D-1 SCOPE (convergence across all 5).** The close-time audit covers OI-S154-2 + OI-S154-3 only. OI-S154-5 (deliberation-grading at seal time) is mechanically distinct — different trigger, different actor, different evidence — and is explicitly excluded from this clause. P-5's scope-bounding argument carries: folding S154-5 would create a self-audit blob that does many things badly. P-4 names the same boundary; P-1 and P-2 affirm; P-3 implicitly agrees. S154-5 remains open and gets its own decision elsewhere.

**D-2 AUTHORITY (hybrid graduated).** The audit is operator/agent-policed at v1, with a named trigger condition for promotion to a substrate gate. Adopts P-4's hybrid pragmatist position with P-5's presence-only-future-gate refinement. The promotion trigger is concrete: if a future calibration-EF names a prior session-close as missing an audit row that would have caught an unlifted A-NNN, the next session opens a gate-promotion issue and ships T-NN refusing session-close on audit-row absence. P-1's gate-now position is preserved as the explicit promotion target — if the v1 clause produces the same 44% miss rate observed at peer arc S017 across the next external-problem arc, the gate ships without further deliberation. P-3's plan-time-discipline warning is preserved as a co-equal clause: the close-time audit complements but does not replace lift-A-NNN-while-prose-is-authored discipline; close-time is recovery, plan-time is prevention.

**D-3 SUBSTRATE SHAPE (substrate-conservative; reuse existing surfaces).** No new table at v1; no new submit kind at v1. The audit artefact is one `engine_feedback` row with `flag='observation'` and a structured headline prefix `audit-step:` whose body enumerates load-bearing interpretive choices and their dispositions (lifted to A-NNN X, deferred to FR-Y, accepted-implicit-with-reason Z). Lifts use existing `bin/selvedge submit assumption`; deferrals use existing `bin/selvedge submit forward-reference`. P-2's argument carries the substrate-shape decision because (a) reuse compounds, (b) the structured-headline pattern is already well-rehearsed (see audit-step parallels in EF-S127-1 calibrations), and (c) the spec_only session boundary forbids new submit kinds. P-4's separation-of-concerns argument is acknowledged: if the engine_feedback body proves insufficient over arc evidence, the table-graduation pathway is open as a follow-up coding session. P-1's typed-table position is preserved as the maximal-promotion target.

**Definition rigour (P-5 carried).** The §8.5 clause must include explicit definition of "load-bearing interpretive choice" with concrete exclusion criteria. Drawing P-5's exclusions: micro-decisions reflected in committed spec rows do not count; choices resolved by citing an existing A-NNN do not count; choices already covered by a closed FR or closed OI do not count. Without these exclusions, the audit either degenerates into noise (every micro-choice listed) or empty compliance ("no load-bearing choices, all done"). Both fail the OI-S154-2 success condition.

**Authority of the audit row vs its content (P-5).** The substrate cannot adjudicate whether a choice was truly load-bearing; it can only enforce presence. The v1 clause says: write the row, name what was load-bearing per the exclusion criteria, dispose each via lift or FR. Quality of judgement remains operator-owned, with calibration-EF as the recovery path when readers later notice misses (mirrors the temporal-claim grounding precedent).

**What ships in S155 (spec_only):**

- prompt-development v11 → v12: extend §8.5 with the close-time interpretive-choice inventory clause, mirroring the temporal-claim grounding clause structure; include the definition + exclusion criteria; cite the named promotion-trigger condition.
- methodology v9 → v10: extend Close phase narrative to mention the §8.5 audit; explicitly note S154-5 is sibling-not-folded.
- engine-manifest engine-v44 → engine-v45: bump current_engine_version because the methodology Close phase is load-bearing.
- OI-S154-2 closed by this decision (close-by-mechanism with promotion path); OI-S154-3 closed; OI-S154-5 explicitly remains open.

**What does NOT ship in S155 (deferred to follow-up):**

- New `close_audit_items` or `interpretive_choice` table.
- New `close-time-audit` or `close-audit-item` submit kind.
- T-NN session-close gate.
- Schema migration of any kind.

**Dissent preserved.** P-1's "structural completeness needs kernel ownership now" is on record; if v1 fails the next arc's gap-closure measurement, P-1's full position is the next decision. P-3's "fix is plan-time, not close-time" warning is on record and shapes the §8.5 wording: the audit is recovery, not the primary discipline. P-2's "ceremony compounds" caution shapes the no-new-submit-kind decision.


### Synthesis points

- **convergence C-1.** All 5 perspectives exclude OI-S154-5 from the close-time audit; S154-5 stays open at deliberation-seal phase.
- **convergence C-2.** Audit covers OI-S154-2 plus OI-S154-3 jointly via §8.5 close-time clause extending the temporal-claim-grounding pattern.
- **convergence C-3.** Authority is operator-policed at v1 with explicit promotion-trigger to substrate gate (P-4 hybrid plus P-5 presence-only-future-gate).
- **convergence C-4.** Substrate-conservative v1: reuse engine_feedback row with flag observation and structured headline audit-step; no new table no new submit kind.
- **minority M-1.** P-1 substrate-gate-now position preserved as explicit promotion target if v1 fails next-arc gap-closure measurement.
- **minority M-2.** P-3 plan-time-discipline warning preserved: close-time audit is recovery not prevention; lift A-NNN while authoring prose.
- **minority M-3.** P-5 definition-rigour requirement carried: spec text must define load-bearing interpretive choice with explicit exclusion criteria.
- **divergence D-1.** Authority axis split: P-1 gate-now vs P-3 no-new-clause; synthesis adopts hybrid graduated middle (P-4 plus P-5).
- **divergence D-2.** Substrate-shape axis split: P-1 new typed table vs P-2/P-3 no-new-substrate; synthesis adopts middle (no table no new submit kind v1).
