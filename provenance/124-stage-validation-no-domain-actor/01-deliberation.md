---
session: 124
title: stage-validation-no-domain-actor — deliberation
generated_by: selvedge export
---

# Deliberation

## D-14 — Validation when no domain-actor is available: third sense, two-tier pattern, or different mechanism — and the meta-problem of a domain-agnostic methodology scaling to solve its own problems.

sealed_at: 2026-04-29T12:16:27.899Z

### P-1 (anthropic)

**Position.** Adopt the two-tier validation pattern as a substrate-of-record mechanism with a new stage_validation kind, advisory authority, scoped initially to disaster-response with re-evaluation at arc close.

**schema_sketch.**
- New substrate kind `stage_validation` with one row per Tier-B pass per external stage, attributed to the validating self-dev session.
- Required fields: arc_id, stage_n, tier (A or B), validator_session_id, continuity_verdict, constraint_coherence_verdict, dissent_md, evidence_refs[].
- Verdicts are ternary (pass / pass-with-findings / fail) not binary, so partial signal is preserved instead of collapsed.
- Continuity is evaluated as "no contradiction with stage N-1 product," not monotonic improvement, because monotonicity is unverifiable absent a ground truth.
- Constraint-coherence is evaluated against both the stage's own imposed constraints and the brief's domain constraints (fictional physics), tagged separately.
- Each `stage_validation` row links to the external-workspace artefact hashes it validated, so post-hoc reproducibility is preserved.
- Findings that warrant kernel-level attention are emitted as engine-feedback rows with `from=stage_validation` provenance, not buried in the validation row itself.
- Tier-B rows are queryable by arc and by stage so the final phase-7 meta synthesis can aggregate them as the empirical material S106 commissioned.
- `stage_validation` rows are immutable once recorded; revisions append a new row with `supersedes` rather than mutate.
- A `confidence` field (low/med/high) captures Tier B's own honesty about how much it could actually verify without a domain actor.
**cli_surface.**
- `bin/selvedge stage-validate --arc <id> --stage <n>` runs the Tier B pass and writes one `stage_validation` row, dry-run supported.
- `bin/selvedge stage-validate --list --arc <id>` reads back all Tier-A and Tier-B rows for an arc in stage order for review.
- No new Tier-A CLI — Tier A is the external workspace's existing close activity and needs no new surface here.
**migration_path.**
- This deliberation's decision-record commissions the `stage_validation` substrate kind and the CLI verb; implementation lands in S125 or S126.
- Stage 1 (already complete) gets a retroactive Tier-B pass once the substrate kind exists, recorded with `retroactive=true` so it is not confused with live validation.
- Stages 2–7 of the disaster-response arc each receive a live Tier-B pass at the stage boundary before the next stage is commissioned.
- OI-S105-1 is closed by this deliberation citing the decision-record; the kernel's "Validation senses" subsection is amended to enumerate three senses, with the third defined as "substrate-cross-validation by an independent workspace."
- OI-016 (deferred in DV-S092-1) is reopened citing the new signal — Tier B is the new signal — and resolved alongside OI-S105-1.
- The disaster-response arc's phase-7 synthesis explicitly aggregates `stage_validation` rows as its primary input, replacing any plan to summarise from markdown EFs.
- Re-evaluation gate: at arc close, a dedicated session decides whether to generalise the pattern, scope it tighter, or retire it; the gate is calendared into the arc plan.
- Validate (kernel activity 7) gets a one-line addition: "where domain-actor is unavailable, substrate-cross-validation by an independent workspace is admitted as the third sense."
**what_not.**
- Not binding authority — Tier B finding "fail" does not force the external workspace to re-do the stage; it records dissent and may emit an OI on the external workspace's queue.
- Not a markdown artefact under `applications/` — that's exactly the decay pathway S106's commission was structured to avoid.
- Not generalised to all external arcs on first adoption — the disaster-response arc is the empirical bed, and generalisation without phase-7 evidence is premature.
- Not concurrent with the external stage's own work — Tier B reads the closed stage product, so concurrency would mean validating a moving target.
- Not a replacement for domain validation when a domain actor *is* available — the third sense is a substitute under unavailability, not a peer.
- Not adjudication between the two workspaces — Tier B reports, it does not arbitrate, and there is no escalation tribunal.
**open_question.**
- Who staffs Tier B inside the self-dev workspace — a dedicated session role, the next available session, or a scheduled cron?
- Should Tier-B validators be barred from reading prior Tier-B verdicts on earlier stages, to prevent verdict-anchoring across stages?
- Does `stage_validation` belong on the same substrate as session rows or in a sibling table, given it references external-workspace artefacts?
- Is "constraint-coherence" graded (how much of the stage's constraints were checked) or boolean (any violation = fail)?
- Should Tier B be allowed to commission a sub-deliberation when verdicts conflict internally, or must a single validator emit a single row?
**risk.**
- Tier B becomes performative — validators rubber-stamp because they lack ground truth — and the substrate fills with `pass` rows that mean nothing.
- Coupling creep — advisory Tier B drifts toward binding through social pressure, and the external workspace loses its independence.
- Substrate bloat — `stage_validation` rows accrete without ever being read back, defeating their purpose as durable evidence.
- Confirmation of the kernel by its own machinery — self-dev validating its own external-arc product risks a closed loop where Selvedge always says Selvedge worked.
- The phase-7 synthesis treats Tier-B rows as evidence of validation having occurred, not evidence of the artefact being correct, and the distinction is lost.
**what_lost.**
- The cleaner kernel reading where Validate has exactly two senses and the third is admitted only as an open issue, not a shipped mechanism.
- The option to discover that *no* substitute for domain validation is honest, and to record that finding instead of building machinery around the gap.
- Some of the design openness this deliberation deliberately preserved by holding stage-1 specifics out — once Tier B ships, future stages will be designed knowing they'll be Tier-B'd.
- The minority position that markdown EFs are sufficient and substrate-rowing the validation is over-engineering for a fictional arc.

### P-2 (openai)

**Position.** Reject the third validation sense as methodology camouflage; reviewer workspace identity is not evidence of independence, so any second pass is review, not validation.

**schema_sketch.**
- The kernel should retain exactly two validation senses: workspace validation and domain validation.
- The undefined provisional reference substitute should be removed, not elaborated into a third validation sense.
- No-domain-actor outputs should carry an explicit validation-limitation record.
- A second pass may be recorded as adversarial review, not validation.
- Reviewer workspace identity is not evidence of independence.
- Constraint-coherence is a workspace criterion unless constraints are externally tested.
- Continuity should mean contradiction detection, not monotonic improvement.
- Cross-family review should be captured as reviewer provenance, not as a new epistemic tier.
- A stage may pass workspace validation while remaining unvalidated for external use.
- Domain validation requires observed or reported function in the target domain.
**cli_surface.**
- None - this correction should change methodology semantics before it creates commands.
- Existing validation commands may add a no-domain-actor limitation flag.
- Any review command should say review, challenge, or audit rather than validate.
**migration_path.**
- Amend methodology.md line 38 to name only workspace and domain validation.
- Replace OI-S105-1 with a decision record rejecting provisional substitutes as validation.
- Add a short note defining no-domain-actor status as a validation limitation.
- Reclassify Tier B outputs as adversarial review artefacts if the operator still wants them.
- Apply the corrected language prospectively to later disaster-response stages.
- Revisit stage 1 only to label its epistemic status, not to retrofit a new validation sense.
- Preserve prior OI-016 deferral unless a real domain actor or reference case appears.
**what_not.**
- Do not create stage_validation as a new substrate kind for this case.
- Do not let self-dev review masquerade as domain validation.
- Do not make Tier B binding, because it has no domain authority to bind against.
- Do not imply that fictional-domain plausibility is evidence of real-world function.
- Do not treat more ceremony as stronger validation.
**open_question.**
- What minimum evidence would let Selvedge reopen domain validation for fictional external arcs?
- How should reviewer provenance record shared training-distribution risk?
- Should adversarial review have required dissenting frames when no domain actor exists?
- What label should appear on artefacts intended for external use but lacking domain validation?
**risk.**
- Rejecting the third sense may feel like losing operational closure for fictional arcs.
- Operators may underuse adversarial review if it is not blessed as validation.
- The methodology may look less complete because it refuses to certify what it cannot know.
- Shared model-family assumptions can still survive ordinary workspace validation.
**what_lost.**
- Selvedge loses a tidy stage gate for no-domain-actor external arcs.
- The disaster-response arc loses the comfort of calling its final pass validation.
- The method gives up a convenient fiction that independent workspaces create external evidence.

### P-3 (anthropic)

**Position.** Subtract the third sense from the kernel; no-domain-actor is just skipped Domain validation, and the two-tier pattern does not belong in methodology.md on the strength of one in-flight arc.

**schema_sketch.**
- The kernel keeps exactly two validation senses, workspace and domain, with no third sense and no provisional substitute clause.
- Workspace validation already includes "internally consistent, does not contradict active specifications, accurately describes the workspace" — coherence checks live here by definition.
- When no domain-actor is available, Domain validation is recorded as "skipped: no domain-actor" and the activity proceeds; skipping is not substituting.
- A skipped Domain validation is a first-class outcome, not a defect requiring backfill; the substrate row records the skip with reason.
- External-arc artefacts that need cross-stage coherence checks invoke Workspace validation in the host workspace where the artefacts live, not a new kernel mechanism.
- If the self-dev workspace also runs coherence checks against an external workspace's product, that is a *second* Workspace validation by a second workspace — still the same sense, applied twice.
- Two applications of one existing sense is not a new sense; the kernel's vocabulary is sufficient to describe what the two-tier pattern actually does.
- Any cross-workspace coherence check is recorded as ordinary Workspace validation substrate scoped to the validating workspace, with a pointer to the validated workspace's artefact.
- No new substrate kind (`stage_validation`) is introduced; existing `validation_record` (or whatever the current schema names) carries the rows.
- No new CLI verbs, no new artefact templates in `specifications/`, no new required fields on stage close.
**cli_surface.**
- None — the kernel change is a deletion in `specifications/methodology.md`; subtraction does not warrant new commands.
- If anything, audit existing validation-recording paths to confirm they admit `skipped: no domain-actor` cleanly without schema growth.
**migration_path.**
- Open a PR against `specifications/methodology.md` deleting "and provisional reference substitute (when no domain-actor is available)" from line 38.
- Close OI-S105-1 with disposition "kernel made coherent by deletion; two senses are canonical."
- Leave OI-016 deferred under its existing "new signal warrants reopening" status — this deliberation is not new signal, it is a design conversation.
- Add one sentence to the Validation senses subsection: "Domain validation may be recorded as skipped when no domain-actor is available; skipping is not a third sense."
- Let the disaster-response arc's stage-2..stage-7 proceed using Workspace validation in both the external and self-dev workspaces as needed, with no kernel change blocking them.
- Capture any two-tier-shaped procedure the arc actually uses as arc-local notes under `applications/<arc>/`, not as kernel.
- After the arc closes, run a retrospective: did anything observed *fail* to express as workspace-validation-plus-skipped-domain-validation?
- Only if a second independent external arc reproduces the same gap does the question of a kernel-level addition reopen.
- If promotion ever happens, the target is `prompts/application.md` or arc-plan templates, never `methodology.md`'s nine-activity kernel.
- Treat this deliberation's output itself as substrate-of-record; do not let it become a back-door kernel amendment.
**what_not.**
- Do not introduce a `stage_validation` substrate kind, a `validate-stage` CLI verb, or a "Tier B" role in the kernel.
- Do not codify the two-tier pattern in `methodology.md` on the strength of one in-flight arc; that is the import-from-outside trap the cautions name.
- Do not make Tier B binding, advisory, or "substrate-of-record only" at the kernel level — the kernel should not know Tier B exists.
- Do not invent "constraint-coherence" or "continuity" as kernel-level criteria; they are at most arc-plan acceptance criteria for one arc.
- Do not generalise to "all future external arcs lacking a domain-actor" pre-emptively; one example is not a pattern.
- Do not reopen OI-016 on the basis of a design deliberation that has not seen stage-1's specifics.
- Do not add ceremony (new templates, new required fields, new close-checklists) to compensate for an absent domain-actor.
**open_question.**
- Does the existing validation-recording schema cleanly express `skipped: no domain-actor` today, or does it need a small field addition to be honest about skips?
- Should the deletion PR also tighten the Validate activity's prose to make "skip is allowed" explicit, or is that gold-plating?
- If the disaster-response arc's stage-2 retrospectively shows a coherence check that genuinely cannot be framed as Workspace validation, what is the smallest possible kernel concession?
**risk.**
- The arc may produce empirical material that *looks* like a third sense; the discipline is to ask whether it is actually two applications of Workspace validation by two workspaces before conceding.
- Subtraction may be read as dismissiveness toward the operator's two-tier proposal, when it is in fact preserving the proposal's option-value by not prematurely freezing it as kernel.
- A future arc with different shape (e.g. domain-actor partially available) might surface a real gap; the position is "wait for that signal," not "deny it can ever exist."
- Deleting line 38's trailing clause without a replacement sentence about skipping could be misread as forbidding skips; the migration path includes a one-sentence clarification to prevent that.
**what_lost.**
- A clean kernel-level vocabulary for "we coherence-checked something we couldn't domain-validate" — the cost of using two-applications-of-Workspace-validation is slightly heavier prose in records.
- Symmetric naming for the operator's Tier A / Tier B intuition; under subtraction, both tiers are just "Workspace validation, scoped to workspace X."
- If the disaster-response arc produces a coherence check that genuinely cannot be expressed as workspace-validation plus skipped-domain-validation, the question reopens and this position is wrong.
- Recording the condition under which subtraction would be wrong is the honest minority-preservation move, not hedging.

### P-4 (openai)

**Position.** Define the third sense as a reference_harness primitive — a durable substitute that exposes whether artefacts survive declared-world claims, dissent, perturbations, and later evidence — without claiming domain-validated status.

**schema_sketch.**
- Add `reference_harness` as the substrate kind for provisional reference substitute validation.
- Each harness targets one stage product, one external arc, and one declared absence of domain-actor.
- The required fields are `target_artifacts`, `claim_set`, `world_constraints`, `assumption_basis`, `surrogate_frames`, `stress_protocols`, `results`, and `expiry`.
- `claim_set` decomposes the artefact into externally meaningful claims that could fail outside the workspace.
- `world_constraints` includes both brief constraints and constraints the stage imposed on itself.
- `assumption_basis` records load-bearing assumptions, their origin session, and their present status.
- `surrogate_frames` are constructed critics made from prior decisions, minority positions, role-stakeholder voices, and reference analogies.
- `stress_protocols` must include constraint replay, counterfactual perturbation, and adversarial dramatization.
- `results` labels each claim as survived, strained, broken, untestable, or deferred.
- `dissent_trace` records minority surrogate objections even when the final harness result passes.
- `falsification_triggers` names later facts or artefact changes that automatically reopen the harness.
- `expiry` sets a session-distance after which the harness must be replayed if the artefact remains active.
- A passing harness permits progression but never upgrades the artefact to domain-validated.
- A broken load-bearing claim opens an issue and blocks closure of the stage validation activity.
**cli_surface.**
- Add `selvedge validate harness --stage S --target PATH` to create a harness scaffold from stage artefacts.
- Add `selvedge validate replay --harness ID` to rerun constraint replay after later-stage changes.
- Add `selvedge validate stress --harness ID --perturbation SET` to append counterfactual stress results.
- Add `selvedge validate expire` to list harnesses whose session-distance has elapsed.
- Add `selvedge validate triggers --changed PATH` to identify harnesses reopened by changed evidence or assumptions.
- Add `selvedge validate summarize --arc ARC` to show survived, strained, broken, and deferred claims across stages.
**migration_path.**
- First update methodology.md so Validate has three defined senses with `reference_harness` as the third.
- Introduce `reference_harness` without replacing workspace validation or domain validation.
- Apply the new primitive retrospectively to stage 1 only after the schema lands.
- Require all future external arcs lacking a domain-actor to create one harness per stage product.
- Treat existing internal issue queues as the destination for broken load-bearing harness results.
- Preserve current markdown artefacts by linking them as targets rather than translating them into the harness.
- Run the first two disaster-response stages as calibration material before declaring CLI behavior mandatory.
- Add a short decision record explaining that substitute validation is not real domain acceptance.
- Reopen OI-016 only if the first harnesses show the absence of domain-actor still creates unresolved authority problems.
**what_not.**
- Do not define the third sense as self-dev workspace review, because workspace identity is not the primitive.
- Do not let continuity plus coherence masquerade as external adequacy.
- Do not make surrogate role-play disposable theatre without preserved dissent and claim-level outcomes.
- Do not require monotonic improvement, because external reasoning sometimes validly narrows or reverses earlier claims.
- Do not classify untestable claims as passed merely because no contradiction was found.
- Do not scope this only to fictional disaster response, because the same gap appears in future-facing and inaccessible domains.
**open_question.**
- Selvedge still needs a rule for how many surrogate frames are enough for a harness to count as convened.
- The methodology must decide whether broken non-load-bearing claims block stage close or only create ordinary issues.
- The engine needs a stable way to distinguish claim failure from artefact incompleteness.
- The expiry interval should probably vary by domain volatility, but no calibration data exists yet.
**risk.**
- The harness may create false confidence if readers forget that surviving surrogate tests is not domain proof.
- Surrogate frames can inherit the same blind spots as the original deliberation.
- Claim decomposition may become bureaucratic if every minor sentence is treated as externally meaningful.
- Adversarial dramatization can overfit to vivid imagined failure modes instead of likely ones.
**what_lost.**
- This approach loses the simplicity of a two-tier validation checklist.
- It gives up a clean pass or fail story in favor of claim-level survival, strain, and expiry.
- It cannot provide the emotional certainty of a real domain actor saying the artefact worked.
- It makes validation slower, because substitute reference becomes an artefact that must be maintained.

### Synthesis

# S124 / D-14 deliberation synthesis

Four perspectives — P-1 anthropic pragmatic-hybrid, P-2 openai cross-family adversarial (skeptic-of-necessity), P-3 anthropic adversarial-minimalist, P-4 openai creative-dreamer — converged on four points, diverged on three, and the synthesis preserves two minorities as activation-warranted.

## Convergence

**C-1.** Monotonic-improvement is rejected as the continuity criterion by all four perspectives; continuity, if defined, is contradiction-detection between stage N and stage N-1, not improvement.

**C-2.** Simulated validation must never pretend to be domain validation: P-1 ("not a peer"), P-2 ("validation-limitation"), P-3 ("skipping is not substituting"), P-4 ("never upgrades the artefact to domain-validated"); the kernel must preserve the epistemic gap honestly.

**C-3.** Cross-family finding: workspace identity is not the validation primitive. P-2 ("reviewer workspace identity is not evidence of independence") and P-4 ("workspace identity is not the primitive") independently arrived at the same critique. This is decisive against framing two-tier review as the kernel-level mechanism.

**C-4.** The trailing clause on methodology line 38 should be removed: P-2 ("amend line 38 to name only workspace and domain"), P-3 ("delete the trailing clause"). The clause as written is undefined and harmful.

## Divergence

**D-1.** Does the kernel need a third validation sense at all? P-1 yes (two-tier as third sense). P-4 yes (reference_harness as third sense). P-2 no. P-3 no.

**D-2.** Mechanism shape. P-1: two-tier review across workspaces. P-4: reference_harness with claim_set, world_constraints, surrogate_frames, stress_protocols, falsification_triggers, expiry. P-2: explicit limitation labels. P-3: deletion only.

**D-3.** Substrate machinery. P-1: new stage_validation kind. P-4: new reference_harness kind. P-2 / P-3: nothing new.

## Synthesis (S-C: subtract now, pilot harness, defer kernel-promote)

The kernel adopts the line-38 deletion (P-3) and gains a clarifying note that domain-validation may be recorded as skipped; OI-S105-1 closes on this. The kernel does NOT yet acquire a third sense.

The methodology commissions reference_harness (P-4) as a *workspace-experimental* substrate kind — not yet a kernel sense. The pilot runs on disaster-response stages 2 through arc-end. Each harness records claim-level survival/strain with the epistemic guardrails P-2 named: a passing harness never upgrades the artefact to domain-validated status. The harness is the substrate pathway by which the disaster-response arc fulfils its S106 commission to surface empirical material on validation-without-domain-actor.

The kernel-promotion question defers to arc close. Re-evaluation is tracked via OI-S124-1 (priority MEDIUM, trigger = arc close, estimated ~S140). Three outcomes are admitted at re-evaluation: promote harness to kernel third sense, retire harness as ceremony with EF capturing why, or scope-change.

## Minorities preserved

**M-1 — P-1's two-tier-as-kernel-third-sense.** Preserved as minority because the operator's starting framing has weight even when superseded by cross-family critique. Activation: if the harness pilot fails because cross-workspace independence (rather than claim-level structure) was what validation actually needed, this position reactivates as the candidate shape.

**M-2 — P-2's full rejection of harness-as-validation.** Preserved as activation-warranted minority. Activation: if the harness pilot accumulates pass rows that have no operator value at re-evaluation — rubber-stamp validators with no ground truth — this position activates and the harness retires.

## Forward direction

S125 (coding): implement reference_harness substrate kind per P-4 schema, with P-2 epistemic guardrails baked into the row shape. S126+ (operator-coordinated): operator pilots harness on disaster-response stage 2 close. Re-evaluation at arc close per OI-S124-1.


### Synthesis points

- **convergence C-1.** All four perspectives reject monotonic-improvement as continuity criterion; contradiction-detection between stage N and N-1 is the admitted reading.
- **convergence C-2.** All four insist simulated validation must not pretend to be domain validation; the epistemic gap is preserved by the kernel.
- **convergence C-3.** Cross-family finding: workspace identity is not the validation primitive; P-2 and P-4 independently arrived at this critique against the two-tier framing.
- **convergence C-4.** P-2 and P-3 converge on removing the trailing clause from methodology line 38; the clause is undefined and harmful as written.
- **divergence D-1.** Whether the kernel needs a third validation sense: P-1 yes via two-tier, P-4 yes via reference_harness, P-2 no, P-3 no.
- **divergence D-2.** Mechanism shape: P-1 two-tier review; P-4 reference_harness with claim and stress and expiry; P-2 limitation labels; P-3 deletion.
- **divergence D-3.** Substrate machinery: P-1 new stage_validation kind; P-4 new reference_harness kind; P-2 and P-3 nothing new.
- **minority M-1.** P-1 two-tier-as-kernel-third-sense preserved as minority; activates if harness pilot fails on cross-workspace independence rather than claim-level structure.
- **minority M-2.** P-2 full rejection of harness-as-validation preserved as activation-warranted minority; activates if pilot accumulates rubber-stamp pass rows at re-evaluation.
