---
session: 199
title: prospective-scoping-discipline-gate — deliberation
generated_by: selvedge export
---

# Deliberation

## D-7 — OI-S196-5 prospective-scoping discipline v1: methodology-spec plus close-record gate

sealed_at: 2026-05-04T11:53:52.005Z

### P-1 (anthropic)

**Position.** Ship typed scoping_passes plus scoping_implications tables at v1 with closed-enum pattern_kind and FK to artefact objects; reject prose-prefix engine_feedback reuse as repeating S194 graduation cycle.

**schema_sketch.**
- scoping_passes parent table: pass_id PK, session_id FK, target_object_id FK to objects, pass_kind CHECK in (substantive, nil-attestation), summary_atom_id FK, UNIQUE(session_id,target_object_id).
- scoping_implications child: implication_id PK, pass_id FK, pattern_kind CHECK closed-five, claim_atom_id FK, lifted_to_object_id FK nullable, disposition CHECK in (lifted, deferred-FR, accepted-implicit).
- Five pattern_kind values from disaster-recovery §6.1 plus A-024 composite-safety: downstream-of-named, allocation-constraint-of-action, authority-chain-of-delegation, temporal-cycle-of-resource, composite-safety-of-aggregate.
- nil-attestation is the typed primitive form of pass-ran-no-implications: a row with zero children, not the absence of a row. Operator-curated arc is the warrant per M-3 S194 schema-correctness threshold.
**cli_surface.**
- bin/selvedge submit scoping-pass --payload {...} emits one scoping_passes row plus zero-to-many child scoping_implications rows in a single write_tx.
- T-NN at close-record-submit refuses when session shipped a substantive decision_v2/spec_versions/external-application artefact and no scoping_passes row covers it; refusal names target alias and prints exact CLI.
- Second handler bin/selvedge query scoping-coverage --session <wno> returns gap inventory for the agent at close and for an auditor afterwards.
**migration_path.**
- Migration NN creates both tables, registers objects.object_kind=scoping_pass, inserts role_write_capabilities for the new submit kind inline (lesson from S194 045+046 split-out reaffirmed at S195).
- Per DV-S189-1 markdown-only-recovery posture, no backdated rows for S001–S199; the typed gate begins from the session migration NN lands in.
- Existing engine_feedback audit-step rows continue discharging §8.5 close-time interpretive-choice audit; sibling clause covering different failure mode (prospective implications vs retrospective audit).
**what_not.**
- Reject prose-prefix detection in engine_feedback.body_md as the gate mechanism.
- Reject the disjunctive AR-row OR EF-prefix gate; the disjunction is the implicitness, and the AR-row option pre-supposes OI-S196-1 closure which has not happened.
- Reject single-flat ≥1 row requirement; implication patterns are multi-valued; substantive decision touching authority chain plus allocation constraint must record both (A-022 + A-020 joint exemplar).
- Reject closure-by-prose nil-attestation; nil is a typed pass_kind value not a prose convention.
- Reject deferring scoping_implications child to v2; the patterns ARE the discipline; without them scoping pass ran is ungroundable.
- Reject any TEXT escape-hatch on pattern_kind, matching the DV-S197-1 R-1.6 schema-correctness bar.
**open_question.**
- Should target_object_id accept a decision_v2 whose kind is not substantive (schema_migration, meta)? P-1 leans no for v1; watch-FR if migration-only session shows implication blow-up.
- Should scoping_implications.lifted_to_object_id admit assumption_register rows once OI-S196-1 lands? Yes; FK is to objects(object_id) under the polymorphic alias scheme S197 established.
- Should pattern_kind admit operator extension at v1 or stay closed-five? P-1 says closed-five with watch-FR for sixth-pattern recurrence, same posture as supersession_ledger relation_kind at S197.
- Should the close-time gate fire on spec_only sessions? P-1 says yes when a spec_version is produced; the methodology-spec amendment itself is an artefact whose implications can be unregistered.
**risk.**
- Cost of typing is one migration, one handler, one close-time T-NN, one query CLI; same shape S197 paid for supersession_ledger and S195 for assessment_prechecks.
- Real cost is table-count cognitive load; that load is paid for by chain-walk reachability the typed table earns.
- Codex reuse-engine_feedback proposal saves zero migrations now but pays in perpetuity routing chain-walk queries through prose prefix-match — exactly the S194 typed engine_feedback_anchors failure mode.
- Compound cost of paying for the same lesson twice (graduation cycle plus retyping pass) is the bigger risk than typing now.
**what_lost.**
- If P-1 loses to codex reuse: engine ships v1 gate satisfying OI-S196-5 by file-presence but cannot answer did this DV attest to its allocation-constraint pattern without grepping prose.
- Next disaster-recovery-style arc surfaces 11-of-25 again, close-time audit catches it, S(N+M) ships migration NN+k typing the table after a graduation cycle plus retyping pass over prose-prefix rows.
- P-1 prefers paying the cost once now over paying it twice.

### P-2 (anthropic)

**Position.** Ship prospective-scoping at v1 as prose-only methodology clause inside §6 (Produce), not §8.5 close-time, not T-NN substrate-gate; reserve typed substrate-gate for v2 graduation only on calibration-EF evidence.

**schema_sketch.**
- No new table at v1. Re-use engine_feedback.flag=observation with headline prefix implication-walk: so discipline lives on same surface as audit-step: and temporal-claim:.
- Promotion path: if v2 graduates, ship typed implication_walks table FK to objects.object_id and FK to assumptions.object_id (one row per implication surfaced or accepted-implicit).
- At v2, T-NN refuses close-record on absent implication_walks rows when session shipped a creates/modifies decision_effect targeting a spec/system-model/plan-shaped artefact.
- No new closed enum at v1. The retrospective §6.1 names three patterns; they go in §6 prose as examples, not as a CHECK enum, because failure mode was failure-to-ask not failure-to-pick-right-value.
- Closing the enum prematurely guarantees future arcs hit a fourth pattern that does not fit, producing the substrate-grammar violation P-3 of D-29 named at S180.
- Codex P-3 substrate-gate plus two formulaic-compliance guards do not pay for themselves at v1; CHECK constraints verify literal string presence not actual applicability — the M-1 of D-23/D-29 receipt-vs-adequacy failure mode.
**cli_surface.**
- Use bin/selvedge submit engine-feedback with body_md prefix implication-walk: <artefact-class>: <N> implications surfaced; <K> lifted to AR-S<wno>-<seq>; <M> accepted-implicit per <exclusion>. Same shape as audit-step:.
- For substantive-content lift path use existing bin/selvedge submit assumption from DV-S198-1; implication-walk: rows cite resulting AR-S<wno>-<seq> aliases. No new payload field.
- No new flag, no new prefix-CHECK, no new gate. The discipline rides on §6 prose plus the existing assumption-ledger primitive.
**migration_path.**
- v1 bumps prompts/development.md v4 to v5 adding §6 prose paragraph Produce-time implication walk citing OI-S196-5, EF-S008-2 arc-level, retrospective §6.1. No SQL migration.
- Clause directs: when session ships any decision_effect creates/modifies on plan-spec-system-model artefact, run pre-submit one-pass implication walk asking which adjacent nodes/allocations/authorities artefact assumes.
- Lift each load-bearing implication via bin/selvedge submit assumption. Record walk as one engine_feedback row with implication-walk: prefix; cite AR-S<wno>-<seq> aliases. Zero-implication walk states 0 — exclusions applied: <which>.
- Optional engine bump v54→v55 if methodology kernel revision is judged load-bearing per S180 precedent.
- v2 (only if calibration-EF triggers per §8.5 promotion-trigger pattern mapped onto this clause): ship typed implication_walks table plus T-NN.
**what_not.**
- Do not ship a §8.5 close-time clause at v1. §8.5 is recovery, §6 is prevention. Retrospective §6.1 says applied at first-artefact-production; close-time is too late to influence artefact text.
- Putting discipline at close pre-bakes a cheap-exit: artefact already authored, synthesizer names implications already addressed and skips ones not addressed, satisfying the gate formulaically.
- Do not ship codex P-3 substrate-gate at v1. It reproduces DV-S159-1 → DV-S180-1 trajectory just superseded: ship typed gate, observe formulaic compliance, subtract or graduate based on calibration evidence.
- Do not close the implication-pattern set as a CHECK enum. Retrospective named three; an arc could plausibly produce a fourth (timing-window→sequencing-gap; capability-deferral→latency-cost).
- Closed enums fit substrate-grammar invariants where the substrate dispatches on value; inappropriate for synthesizer-prompts where the value selects a cognitive frame.
- Audit-step clause ran 15 sessions at 100% rate including 2 zero-counts; D-29 M-1 question (100% measures discipline or compliance theater) unresolved. Second §8.5-shaped clause doubles the problem.
**open_question.**
- Whether implication-walk should be split per-artefact (one row per creates/modifies effect target) or per-session (one row enumerating all). Per-session at v1 cheaper; per-artefact only if v2 graduates.
- Whether kind=meta sessions (triage-only, this S199 shape) are in scope. They author closes_issue/opens_issue but not plan-shaped artefacts in §6.1 sense. Probably out-of-scope at v1; verify at next meta close.
**risk.**
- False-negative honest residual: session-author runs walk superficially and lifts zero genuine load-bearing implications when 1-2 existed. Recovery: calibration-EF in downstream session, same shape as audit-step recovery.
- Compliance-theater specific: implication-walk: 0 — exclusions applied: kind=meta authored every session would be exact cheap-exit audit-step: 0 already pioneered. §8.5 nil_attestation precedent admits this.
- Honest cost: 0-count rows accumulate diluting signal-bearing rows; recoverable by v2 typed table or retrospective query patterns.
**open_question.**
- Whether codex P-3 two formulaic guards should fold into §8.5 audit-step clause retroactively (tighter than current exclusions applied: prose) rather than into a new clause. If yes, separate session not bundled with OI-S196-5.
**risk.**
- Latency cost real but exactly the cost current engine carries with no clause; prose-only at v1 reduces from no-discipline to operator-policed; substrate-gate does not measurably reduce further while carrying formulaic-compliance hazard.
- Substrate-grammar collapse risk: piggybacking on engine_feedback flag=observation with another prefix continues prefix-substring-match P-3 of D-29 named brittle. Mitigation: v2 moves discipline off prefix-substring channel.
**what_lost.**
- Lost vs codex P-3 typed-gate: seal-time prevention of assumption-implicit failure mode, the same prevention DV-S159-1 promised at S159 and DV-S180-1 demonstrated had not actually fired across 8 rows.
- Honest inheritance from D-29: prevention through receipt-presence is theatrical at this evidence level; substrate cannot reach into synthesizer epistemic completeness check. v1 prose-only accepts this and waits for calibration-EF.
- Lost vs OI-S196-5 literal title (session-close substrate-gate analogous to T-38): literal reading promises gate at v1. P-2 reads OI title as one shape proposed not the only shape admissible; deliberation is the place to surface the axis.
- EF-S196-2 binds against citing DV-S190-2 as defer basis, not against choosing prose-at-v1 when prose is the load-bearing remediation per the failure-mode shape.
- Lost vs P-3 two formulaic guards: stricter prose-shape check at moment gate fires. P-2 holds guards do not address underlying problem (gates measure receipt not adequacy); admissible as v2 strengthening if v1 insufficient.

### P-3 (openai)

**Position.** VERDICT SHIP-WITH-NAMED-EDITS. Make it a close-record submit gate not raw session-close gate. Reuse engine_feedback.body_md prefix scoping-pass: rather than create scoping_passes table at v1.

**schema_sketch.**
- No new table at v1. Reuse engine_feedback rows with body_md prefix scoping-pass: as receipt mechanism.
- T-NN gate at close-record submit handler: refuse close-record INSERT unless session has either ≥1 assumption_ledger row whose origin_decision_object_id points to a DV from this session OR ≥1 EF beginning scoping-pass:.
- Patterns prose-only with required label list: schema-adjacency, caller-implications, migration-implications. No CHECK enum on a sub_kind column (pattern set young; expansion expected).
- Cheap-exit nil_attestation: scoping-pass: 0 — exclusions applied: <which artefact-classes reviewed or absent> admits as a single row.
**cli_surface.**
- No new submit kind. Use existing bin/selvedge submit engine-feedback with body_md prefix.
- Refusal at close-record E_REFUSAL_T<NN> naming the recovery: submit AR-row with origin_decision OR EF with prefix scoping-pass:.
- Refusal text includes the cheap-exit recipe so an agent who hits the refusal can recover with one submit.
**migration_path.**
- Migration 050 bumps engine version, adds index for engine_feedback prefix lookup (performance), INSERT schema_migrations row, role_write_capabilities inline per S194 lesson.
- v3 may add CHECK enum on pattern_kind sub_column once arc evidence demonstrates a stable pattern set.
- v2 promotion-trigger: typed scoping_passes table if (a) prefix parsing brittle, (b) reviewers need queryable counts, (c) nil attestations common low-signal, OR (d) audits need review-performed distinction.
**what_not.**
- No new table at v1; engine_feedback prefix is sufficient receipt mechanism.
- No CHECK enum on sub_kind; patterns prose-only.
- No proportional count requirement (e.g. ≥N AR rows per substantive DV); flat single-row-or-nil incentivizes quality over quantity (proportional counts incentivize low-quality row multiplication).
- No raw session-close gate; close-record is the right transaction boundary alignment with T-39.
- No bare scoping-pass: 0 admit; cheap-exit must name exclusions.
**open_question.**
- Should the gate apply to all kinds (coding + spec_only + meta) or only kinds producing artefacts? Codex view: artefact-gated applicability — apply when session produced ≥1 substantive DV/spec_version/migration; skip pure-meta sessions.
**risk.**
- Formulaic compliance: cheap-exit can become a templated bypass. Mitigation: two guards (nil must name artefact classes; substantive-DV nil must name ≥1 of three implication patterns).
- Even with guards, M-1 minority concern from DV-S180-1 lineage applies — the gate proves receipt-presence not epistemic-adequacy.
- Prefix brittleness: prose-prefix detection may fail on unicode normalization, leading whitespace, etc. Mitigation: handler trims and lowercases prefix detection; v2 typed table if recurrent.
- Engine-self bootstrap: S199 ships the gate; S199 close-record itself triggers the gate. Discipline applies to S199 ship.
**what_lost.**
- P-1 schema-correctness threshold dissent: engine primitives that alter schema/API behaviour deserve typed substrate from day one. Reusing engine_feedback risks hiding a kernel-safety obligation inside prose-prefix convention.
- Codex acknowledges this is the strongest M-1 minority dissent; v2 promotion-trigger preserved.
- Strongest M-1 minority preserved: typed-substrate-from-day-one (P-1 stance). v1 prefix-pattern is acknowledged as ceremony-subtraction compromise.
- If calibration EFs name prefix brittleness OR queryable-count-need OR review-distinguishing failure across 2+ sessions, v2 ships scoping_passes typed table.

### Synthesis

**Synthesis: ship prospective-scoping discipline v1 via close-record gate (T-41) using engine_feedback prefix scoping-pass: detection plus methodology-spec §8.6 plus two formulaic-compliance guards plus artefact-gated applicability plus cheap-exit nil_attestation closing OI-S196-5 by-mechanism in-session.**

**Convergence (multi-of-3).** C-1 close-record submit is the gate transaction boundary (P-1 + P-3 explicit; P-2 no-gate dissent preserved). C-2 methodology-spec defines 3 engine-self implication patterns: schema-adjacency, caller-implications, migration-implications. C-3 artefact-gated applicability: pure-meta sessions admit close-record without scoping-pass receipt (codex P-3 + P-1 acknowledgement). C-4 cheap-exit nil_attestation pattern (codex; T-36 lineage). C-5 atom 8-480 support_claim tier. C-6 EF-S196-2 bounded-scope binding admits this primitive as engine-evidenced-by-completed-arc.

**Divergence.** D-1 receipt mechanism. P-1 typed scoping_passes parent + scoping_implications child table from day one with closed pattern_kind enum. P-2 prose-only-no-gate at §6 Produce. P-3 close-record gate via engine_feedback prefix. Synthesis adopts P-3 prefix detection: ceremony-subtraction (DV-S109-1) + §8.5 audit-step prefix precedent + bias-toward-build-now bounded by EF-S196-2. P-1 typed-from-day-one preserved as M-1 minority + v2 promotion-trigger. P-2 no-gate stance preserved as M-2 minority watch-trigger if formulaic compliance surfaces.

D-2 gate strength. P-1 mandatory-with-child-rows; P-3 flat single-row-or-nil; P-2 no-gate. Synthesis adopts P-3 flat: proportional counts incentivize low-quality multiplication; flat invariant is "session cannot close without performing the implied-assumption review."

D-3 pattern enum vs prose. P-1 typed CHECK enum; P-3+P-2 prose-only with required labels. Synthesis adopts P-3 prose: pattern set young; v3 promotion if stable.

**Minorities.** M-1 P-1 typed-substrate-from-day-one: v2 promotion if prefix brittleness OR queryable-count-need OR review-distinguishing measurable. M-2 P-2 no-gate-prose-only-§6-Produce: watch-trigger if formulaic compliance surfaces in 2+ calibration EFs. M-3 P-2 receipt-presence-not-epistemic-adequacy: all gate designs (including this one) prove receipt presence not epistemic adequacy; v2 stronger guards (item-count proportional or domain-specific pattern checks) if M-2 fires.

**Counterfactuals.** CF-1 typed scoping_passes at v1 addressed-in-synthesis. CF-2 prose-only-no-gate addressed-in-synthesis. CF-3 proportional count requirement nilled-by-exclusion barred-by-constraint per codex incentivize-multiplication concern. CF-4 CHECK enum on pattern_kind nilled-by-exclusion out-of-scope per pattern-set-young.

**Bias-toward-build-now per EF-S196-2.** Ship v1 in S199. Codex EF-S199-1 6-edit verdict: 6 of 6 named edits adopted. P-2 no-gate dissent preserved as M-2 minority watch-trigger; gate ships under operator-named-mandate per §1.5 admissibility (operator-named at S196 OI mandate "session-close substrate-gate refusing close without assumptions-implied-by-artefacts review" — operator override of any wait-for-evidence position).

**Spec amendment in-session per DV-S197-1 + DV-S198-1 precedent.** prompts/development.md gets new §8.6 prospective-scoping clause + §8.7 surfaces T-41 gate semantics + cheap-exit recipe + watch-triggers.


### Synthesis points

- **convergence C-1.** Close-record submit is the gate transaction boundary; T-41 attaches before close-record becomes binding (P-1 + P-3).
- **convergence C-2.** Methodology-spec §8.6 defines 3 engine-self implication patterns: schema-adjacency, caller-implications, migration-implications.
- **convergence C-3.** Artefact-gated applicability: pure-meta sessions admit close-record without scoping-pass receipt; gate fires only on substantive-DV/spec_version sessions.
- **convergence C-4.** Cheap-exit nil_attestation pattern (T-36 lineage): scoping-pass: 0 — exclusions applied: <which> admits as a single row.
- **convergence C-5.** Atom 8-480 support_claim tier per OI-S177-1 widening; matches §8.5 audit-step body length budget.
- **convergence C-6.** EF-S196-2 bounded-scope binding admits this primitive as engine-evidenced-by-completed-multi-session-arc; bias-toward-build-now per operator-named-mandate.
- **divergence D-1.** Receipt mechanism: P-1 typed scoping_passes table; P-2 prose-only-no-gate at §6 Produce; P-3 close-record gate via engine_feedback prefix. Adopts P-3.
- **divergence D-2.** Gate strength: P-1 mandatory-with-child-rows; P-3 flat single-row-or-nil; P-2 no-gate. Adopts P-3 flat (proportional counts incentivize multiplication).
- **divergence D-3.** Pattern enum vs prose: P-1 typed CHECK enum; P-3+P-2 prose-only with required labels. Adopts P-3 prose (pattern set young).
- **minority M-1.** P-1 typed-substrate-from-day-one: preserved as v2 promotion-trigger if prefix brittleness OR queryable-count-need OR review-distinguishing measurable.
- **minority M-2.** P-2 no-gate prose-only-§6-Produce: preserved as watch-trigger if formulaic compliance surfaces in 2+ calibration EFs.
- **minority M-3.** P-2 receipt-presence-not-epistemic-adequacy: all gate designs prove receipt presence not adequacy; v2 stronger guards if M-2 fires.
