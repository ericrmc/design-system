---
session: 131
title: restore-deliberation-shape — deliberation
generated_by: selvedge export
---

# Deliberation

## D-17 — Multi-agent deliberation: what shape should it take in this engine going forward — perspective number, role discipline, required adversarial role, stance-brief structure, synthesis discipline, graceful-degradation floor, smallest shape against post-restart drift?

sealed_at: 2026-04-29T22:56:51.713Z

### P-1 (anthropic)

**Position.** Restore the five MAD v4 disciplines (number floor, role-naming, adversarial requirement, stance-brief shape, three-output quorum) as prompt-level prose rather than substrate machinery.

**schema_sketch.**
- No schema change proposed; existing synthesis_points.kind enum already admits convergence/divergence/minority.
**cli_surface.**
- No new CLI verbs; existing deliberation-open, perspective, deliberation-seal, synthesis-point carry the load.
**migration_path.**
- S132 amends prompts/development.md section 4 with the twelve-sentence discipline.
- Engine-manifest version bump.
- No archive churn; MAD v4 stays in archive/pre-restart/ as historical record.
- First post-amendment deliberation tests the floor-of-3 rule under live conditions.
**what_not.**
- No substrate-enforced adversarial flag (re-creates manifest accretion).
- No closed role-enum (re-creates roster pathway).
- No restoration of OI-004 closure machinery, Layer 2 manifest schema, four-state lifecycle, or validate.sh checks 16-19 (stale, excluded by brief).
- No new spec file; the discipline lives in the prompt.
**open_question.**
- Whether the operator wants to retroactively re-run any of the eleven 2-perspective post-restart deliberations under the new floor, or grandfather them.
- Whether synthesis_points.source_perspectives should require non-empty for convergence kind, substrate-enforcing the convergence-vs-coverage distinction.
- Whether load-bearing warrants a marker on deliberations rows so EF authoring can audit floor-compliance.
**risk.**
- Twelve sentences in the prompt may decay under context pressure the same way the original three did; mitigation is a session-close did-section-4-hold check.
- Floor of 3 may produce ceremonial third perspectives where 2 was genuinely sufficient; evidence does not distinguish drift from appropriate minimalism for every case.
- Adversarial-required as prose discipline relies on operator policing; exhortative friction underperforms structural friction.
**what_lost.**
- The operational simplicity of the current 3-sentence section 4; authors must now satisfy more shape per deliberation.
- The 2-perspective default speed for narrow technical disposition decisions; some post-restart 2-perspective deliberations may have been right-sized.
- The option of treating MAD v4 as fully archived; this position re-imports its substantive core, even at reduced length.

### P-2 (openai)

**Position.** Restore only the load-bearing minimum as a small prompt-level rule for foundational deliberations, not full MAD v4; keep substrate enforcement out unless repeated failures demand it.

**schema_sketch.**
- No schema change now.
- Use existing perspectives.label, perspectives.family, and synthesis_points.kind.
- If failures recur, consider adding a lightweight role_charge atom later, but only with a worked failure case.
**cli_surface.**
- No new CLI verbs.
- Optional future enhancement: deliberation-open could accept repeated --role Name:charge flags, but not necessary for first restoration.
**migration_path.**
- Patch prompts/development.md section 4 with the four-perspective foundational rule.
- Add a short synthesis checklist to the same section.
- Run the next few methodology-changing deliberations under this rule.
- Reassess only from observed misses, not from speculative completeness.
**what_not.**
- Do not restore specifications/multi-agent-deliberation.md.
- Do not add lifecycle machinery, manifest layers, or validation checks from MAD v4.
- Do not create a permanent perspective roster.
- Do not substrate-store prose briefs.
- Do not make four perspectives mandatory for every deliberation.
**open_question.**
- The brief does not show which of the eleven two-perspective deliberations produced worse decisions.
- The operator-steering complaint may partly be prompt-decay or framing bleed, not perspective count.
- Unclear whether cross-family availability is operationally reliable enough for hard enforcement.
**risk.**
- A prose-only rule may drift again.
- Four perspectives may become ceremony for questions that only need two.
- The adversarial role may become performative if the stance brief is weak.
- Without substrate counters, the engine may not notice gradual noncompliance.
**what_lost.**
- Gives up the reproducibility and enforcement strength of full MAD v4 in exchange for lower context weight and lower accretion risk.

### P-3 (anthropic)

**Position.** Restore deliberation discipline via three additions: a 3-perspective floor in prompt v9, a deliberation substrate record to prevent re-defaults, and CLI gating that enforces cross-family.

**schema_sketch.**
- Extend deliberations table with minimum_perspectives INT default 3, expected_families TEXT, adversarial_perspective_label TEXT.
- Add deliberation-brief table with deliberation_id, role_label, family, stance_md_hash content-addressable reference to immutable brief text committed to git before launch.
**cli_surface.**
- deliberation-open --perspectives 3 --families anthropic,openai --adversarial skeptic gates convene at CLI level and refuses if requirements not met.
- Add brief-lock verb to commit briefs and prevent mutation until deliberation-seal.
**migration_path.**
- Add gating to existing deliberation-open verb at S132: enforce minimum-perspectives rule before briefing phase launches.
- Brief immutability enforced by existing git workflow: briefs committed before perspective-launch, commit history is the provenance record.
- No retroactive changes needed to S076-S131; the 2-perspective default is historical record, not a system error.
**what_not.**
- Not re-importing MAD v4 prose verbatim; not creating a 482-line spec; not mandating substrate-recorded role names.
- Not changing synthesis mechanics beyond re-adopting citation and convergence-vs-coverage discipline (prose-enforced).
- Not creating a rotating-quorum or past-self perspective; treating as hypothesis not warrant.
- Not mandating 5+ perspectives even for methodology changes; 4 is target, 5 requires justification.
**open_question.**
- When operator-named axes do not cleanly map to model families, how is the free-form role slot assigned: operator pre-declares, or consensus rule?
- If a deliberation starts with 3 and one perspective returns a refusal, is re-run required or is replacement perspective acceptable?
- Should stance-brief generation be formalized as a verb with a template, or remain operator-written-and-reviewed?
**risk.**
- If the 3-perspective floor is enforced at CLI level, an operator can bypass it only by hand-editing the database, creating a silent failure mode.
- Adversarial requirement can be satisfied formally (a role named skeptic) without being substantive; prose discipline is necessary but not sufficient.
- Brief immutability via git-review-before-launch works only if review step is not skipped; no code-level enforcement without a pre-commit hook, out-of-scope.
**what_lost.**
- The full MAD v4 spec schema-lifecycle machinery (4-state lifecycle, Layer 2 manifest, validate.sh checks 16-19) is not restored; these were optimizations for a larger engine.
- Rotating-quorum perspectives are not adopted; speculative and could be revisited if future deliberations show the same lessons-loss pattern.
- The constraints.md properties (now archived) are not restored as working documents; remain in the brief as historical warrant, not engine-loadable spec.

### P-4 (openai)

**Position.** Restore a small substrate-enforced kernel: minimum three valid perspectives, one cross-family, one adversarial, named per problem, with synthesis rows distinguishing convergence, divergence, minority.

**schema_sketch.**
- perspectives.role_kind TEXT NOT NULL DEFAULT generative CHECK in (generative, implementation, adversarial, historical, operator, external).
- perspectives.status TEXT NOT NULL DEFAULT valid CHECK in (valid, refusal, invalid, missing).
- deliberations.min_valid_perspectives INTEGER NOT NULL DEFAULT 3 CHECK >= 3.
- deliberations.target_perspectives INTEGER NOT NULL DEFAULT 4 CHECK >= min_valid_perspectives.
- deliberations.brief_path TEXT NULL and deliberations.brief_sha256 TEXT NULL.
- Seal check: valid perspective count must be >= min_valid_perspectives.
- Seal check: at least one valid perspective must have role_kind=adversarial.
- Seal check: at least one valid perspective must have family != convening default family, preserving cross-family commitment.
- Seal check: if any synthesis_points.kind=divergence, require at least one minority row or non-empty source_perspectives on each divergence.
**cli_surface.**
- bin/selvedge submit deliberation-open --topic ... --target-perspectives 4 --brief-path ...
- bin/selvedge submit perspective --label ... --family openai --role-kind adversarial --body-md ...
- bin/selvedge submit perspective with --status refusal preserves a refusal as provenance without counting toward quorum.
- deliberation-seal refuses with explicit missing conditions: quorum, adversarial role, cross-family perspective, or synthesis coverage.
**migration_path.**
- Add nullable columns first, backfill existing perspectives with role_kind=generative and status=valid.
- Backfill deliberations with min_valid_perspectives=3 and target_perspectives=4.
- Update CLI to require --role-kind for new perspectives after migration.
- Add seal-time validation after historical rows are migrated, so old deliberations remain readable without pretending they met new standard.
- Export generated markdown with role kind and status visible beside label/family.
**what_not.**
- Do not restore the full MAD v4 spec.
- Do not substrate-validate byte-identical brief sections yet.
- Do not create a permanent role roster.
- Do not parse citations or enforce [synth] syntax in SQLite.
- Do not add lifecycle machinery beyond valid/refusal/invalid/missing status.
**open_question.**
- Whether operator should be a role_kind or only a family=human perspective.
- Whether target four should be a hard requirement for foundation-touching decisions, requiring a decision-kind enum.
- Whether external is too vague as a role kind and should remain a label-level convention.
**risk.**
- The enum may become ceremonial if operators pick role kinds mechanically.
- A required adversarial role can produce performative objection rather than real disagreement.
- Seal checks may encourage minimal compliance unless synthesis review remains substantive.
- Brief discipline could decay next, because this proposal leaves it mostly prose-policed.
**what_lost.**
- Some flexibility lost: two-perspective deliberations can no longer seal as MAD.
- Some simplicity lost: every perspective now needs a role kind and status.
- Some nuance lost by reducing role function to a small enum.
- Some reproducibility from MAD v4 is left outside substrate, especially stance-brief immutability and citation syntax.

### P-5 (openai)

**Position.** Restore a small disciplined deliberation shape: four convened, three valid minimum, one cross-family, one adversarial, named for disagreement, with brief hashes and source-citing synthesis.

**schema_sketch.**
- Add deliberation_roles(deliberation_id, perspective_id, role_kind, stance_hash, shared_brief_hash, expected_disagreement).
- role_kind closed only for process roles: adversarial, generative, constraint, domain, operator, other; labels remain free text.
- Add synthesis_points.kind=coverage or require source_count so single-perspective points cannot masquerade as convergence.
- Add seal checks: at least three valid perspectives, at least one adversarial, at least one cross-family when rule applies, shared brief hash consistent.
**cli_surface.**
- Extend deliberation-open with --target-perspectives, --shared-brief-hash, and --rationale.
- Extend perspective with --role-kind, --stance-hash, and --expected-disagreement.
- Extend deliberation-seal to refuse invalid quorum or missing adversarial role.
- Keep synthesis-point but add coverage or require explicit source count.
**migration_path.**
- First update prompts/development.md section 4 with the restored minimum shape.
- Then add substrate seal validation for quorum, adversarial role, and cross-family presence.
- Then add brief hashes and coverage support.
- Do not backfill old deliberations except by recording the S076-S130 count series as evidence.
**what_not.**
- Do not restore the full 482-line MAD v4 spec.
- Do not create a permanent roster of named perspectives.
- Do not make five or six perspectives the default.
- Do not require closed substantive role enums.
- Do not turn synthesis into decision-making.
**open_question.**
- Whether coverage deserves its own kind or can be derived from source_perspectives.
- Whether brief immutability must be git-commit enforced or whether substrate hashes are enough.
- Whether human/operator perspectives should count toward quorum when LLM-family blind-spot risk is the reason for deliberation.
**risk.**
- Four perspectives may become ceremony if used for non-load-bearing work.
- A required adversarial role may become performative unless the stance names a real proposal to attack.
- Substrate checks may overfit todays failure mode and create new accretion pressure.
- Role-kind enums may slowly expand unless treated as process metadata, not taxonomy.
**what_lost.**
- Faster two-perspective deliberations lose status as full MAD.
- Operator discretion narrows at seal time.
- Some lightweight questions will need to be downgraded or reformulated rather than synthesized.
- The engine gives up a little flexibility to regain the deliberation shape that made disagreement productive.

### P-6 (anthropic)

**Position.** The drift is a self-steering problem; restore deliberation by re-encoding the two or three highest-leverage MAD v4 mechanisms at the right layer, not re-importing the full 482-line spec.

**schema_sketch.**
- No schema changes required; existing perspectives table, synthesis_points table, and closed section_kind enum are sufficient.
- If substrate enforcement of adversarial requirement is desired later, perspectives could admit a role_kind column with a closed enum, but not minimum viable shape.
**cli_surface.**
- No new CLI verbs required; existing deliberation-open, perspective, deliberation-seal, synthesis-point are sufficient.
- Deviation-justification for dropping below default perspective count can be recorded as a synthesis-point with kind minority at convening time, or as a note in the deliberation topic.
**migration_path.**
- Edit prompts/development.md section 4 to add three prose additions (perspective floor, adversarial requirement, brief immutability); single file edit, no substrate migration.
- The living template for shared/role-specific brief structure is this deliberations files; reference them or archive a canonical short template in specifications/.
- Future deliberations adopt the new section 4 immediately; past deliberations are not retroactively affected.
**what_not.**
- Do not re-import the 482-line MAD v4 spec; the stale machinery (OI-004 closure, Layer 2 manifest, validate.sh checks) is dead weight.
- Do not substrate-enforce the perspective floor or adversarial requirement; prose discipline at the prompt layer is sufficient.
- Do not add a permanent perspective roster; selection by expected disagreement on this problem is the mechanism.
- Do not require cross-family enforcement beyond the existing rule; the adversarial requirement is the complementary mechanism.
**open_question.**
- Brief-immutability assumes the convening agent is not also a perspective; if orchestrator is sometimes P-1, the synthesizer-not-a-perspective rule needs to extend.
- Is deviation-justification for dropping below the default recorded in substrate, brief, or only the prompt? Schema has no field; a lightweight convention should be named.
**risk.**
- Prose-only additions to section 4 are vulnerable to the same context-pressure decay that eroded the original three sentences; more specific but not immune.
- Naming axes-of-disagreement before launching requires operator partial analysis; if absent, pressure to skip is high and prose discipline will not hold.
**what_lost.**
- If adversarial requirement is prose-only, it will be dropped under time pressure without consequence the engine can perceive.
- Keeping brief files as workspace files (not substrate-recorded) means the input that produced each perspective is not queryable alongside the body; provenance is weaker.
- Dropping synthesis-order anchoring loses one deterrent against synthesis-order anchoring bias; the first perspective tends to frame the synthesis.

### Synthesis

# Synthesis — S131 deliberation on multi-agent deliberation shape

Synthesizer: orchestrator (Claude Opus 4.7, 1M context); not a perspective in this deliberation. Six perspectives reasoned in parallel, isolated, from byte-identical shared brief plus role-specific stance. Perspectives presented in alphabetical order by role: Archivist (P-1, anthropic), Dreamer (P-3, anthropic), Operator-decentering (P-6, anthropic), Outsider (P-5, openai), Skeptic (P-2, openai), Substrate-engineer (P-4, openai).

## Convergence (all six perspectives independently agreed)

**C-1. Floor of three valid perspectives.** All six restore the MAD v4 graceful-degradation rule: fewer than three valid outputs is not deliberation. The 11×2-perspective post-restart pattern in §4.4 of the brief is convergently named as the failure mode addressed. [P-1, Q1; P-2, Q6; P-3, Q1; P-4, Q1; P-5, Q6; P-6, Q1; P-6, Q6]

**C-2. At least one adversarial role is required.** All six. [P-1, Q3; P-2, Q3; P-3, Q3; P-4, Q3; P-5, Q3; P-6, Q3]

**C-3. Named perspectives chosen for expected disagreement on *this* problem; no permanent roster.** All six. Closed-enum *substantive* role taxonomy is rejected by all (P-3's enum proposal is for *process function*, not substantive role; see Minority M-1 for the residual divergence). [P-1, Q2; P-2, Q2; P-3, Q2; P-4, Q2; P-5, Q2; P-6, Q2]

**C-4. Re-codify the shared/role-specific brief split with immutability after commit.** All six. [P-1, Q4; P-2, Q4; P-3, Q4; P-4, Q4; P-5, Q4; P-6, Q4]

**C-5. Restore four synthesis disciplines: synthesizer-not-a-perspective, citation requirement, `[synth]` markers for synthesizer-original claims, convergence-vs-coverage distinction.** All six restore most or all. P-6 explicitly proposes dropping synthesis-order anchoring as "process tidiness without self-steering value"; others are silent or convergent on its retention. [P-1, Q5; P-2, Q5; P-3, Q5; P-4, Q5; P-5, Q5; P-6, Q5]

**C-6. Do NOT re-import the 482-line MAD v4 spec.** All six. [P-1, what_not; P-2, what_not; P-3, what_not; P-4, what_not; P-5, what_not; P-6, what_not]

**C-7. Do NOT restore OI-004 closure machinery, Layer 2 manifest schemas, or validate.sh checks 16–19.** All six. The brief excluded these and no perspective contested the exclusion. [synth]

## Divergence (genuine disagreement, preserved)

**D-1. Enforcement layer: prose discipline vs substrate enforcement.** Six perspectives split 3–3, cross-family balanced.

- *Prose-only* (P-1 Archivist anthropic; P-2 Skeptic openai; P-6 Operator-decentering anthropic): the discipline lives in `prompts/development.md` §4. P-1: "Substrate enforcement... would re-create the manifest-schema accretion pattern that the restart specifically subtracted" [P-1, Q3]. P-2: "the brief gives no worked example where a substrate refusal would have improved an actual past decision" [P-2, Q3]. P-6: "substrate enforcement adds friction without adding the self-steering property" [P-6, what_not].
- *Substrate-enforced minimum kernel* (P-3 Dreamer anthropic; P-4 Substrate-engineer openai; P-5 Outsider openai): seal-time checks for quorum, adversarial-role-present, cross-family-present. P-3: "Prose discipline alone fails; property 5 shows it is forgotten across sessions" [P-3, Q3]. P-4: "Property 2 says failure is cheap, and property 5 says lessons do not survive across sessions; an adversarial prose reminder will decay exactly as the perspective count did" [P-4, Q3]. P-5: "the observed drift is evidence that exhortation is insufficient" [P-5, Q3].

The split is not family-correlated. Both clusters cite constraints.md properties as warrants — opposing readings of which property is decisive (property 6 ceremony-accretion vs property 2 failure-is-cheap and property 5 lessons-don't-survive). [synth]

**D-2. Number target above the floor.** Convergence on floor=3; divergence on target.

- P-1: target 3, up to 5 with justification [P-1, Q1].
- P-2: target 4 for foundational only; 2 acceptable for "bounded, implementation-adjacent questions where the decision does not change methodology shape" [P-2, Q1] — see Minority M-2.
- P-3, P-5, P-6: target 4 for methodology-changing decisions, 3 for narrower [P-3, Q1; P-5, Q1; P-6, Q1].
- P-4: floor 3, target 4 for foundational [P-4, Q1].

Cluster: four perspectives (P-3, P-4, P-5, P-6) converge on "3 floor, 4 target for methodology-changing decisions." P-1 holds at default-3, P-2 allows 2 for narrow.

**D-3. Brief metadata in substrate vs workspace-only.** Same 3–3 split as D-1. P-3 proposes `deliberation-brief` table with content-addressed `stance_md_hash` [P-3, schema_sketch]. P-4 proposes optional `deliberations.brief_path` / `brief_sha256` [P-4, schema_sketch]. P-5 proposes `deliberation_roles(deliberation_id, perspective_id, role_kind, stance_hash, shared_brief_hash, expected_disagreement)` [P-5, schema_sketch]. P-1, P-2, P-6 say workspace-files-only with git-commit timestamp as provenance [P-1, Q4; P-2, Q4; P-6, Q4].

## Minority positions (single-source, preserved)

**M-1. Closed-enum role roster (P-3 Dreamer alone).** P-3 proposes "five role kinds: Anthropic-Pragmatist, Anthropic-Skeptic, OpenAI-Skeptic, OpenAI-Dreamer, and one free-form role named for the deliberation's actual disagreement axis" [P-3, Q2]. All five other perspectives explicitly reject permanent rosters as a return to the accretion pathway. Preserved because the operator has, in S124 and again in S131, observed that named-role variety produced novel substantive design; the closed-enum proposal is one mechanism for guaranteeing that variety. Reopen warrant: a future session where free-form role naming collapses back to "P-1 anthropic, P-2 openai" despite §4 prose discipline.

**M-2. Two-perspective acceptable for narrow technical decisions (P-2 Skeptic alone).** P-2: "Use two only for bounded, implementation-adjacent questions where the decision does not change methodology shape" [P-2, Q1]. Five other perspectives say 3 is the floor, not the default. Preserved because if substrate enforcement (D-1's other branch) prevails and refuses 2-perspective deliberations, the engine loses a low-ceremony surface that may be appropriate for some genuinely narrow decisions. Reopen warrant: post-decision deliberations that produce ceremonial third perspectives.

**M-3. `perspectives.status` enum to explicitly classify refused/invalid/missing perspectives (P-4 Substrate-engineer alone).** P-4: "valid/refusal/invalid/missing... only `status='valid'` counts toward quorum" [P-4, Q6, schema_sketch]. Others let refusal manifest implicitly via empty body. Preserved as a follow-up if implicit refusal-handling proves ambiguous. Reopen warrant: a deliberation that produces a refusal whose handling is contested.

**M-4. `coverage` as a fourth synthesis_points kind (P-5 Outsider alone).** P-5: "the existing `synthesis_points.kind` enum already supports convergence, divergence, and minority, but it misses coverage" [P-5, Q5]. Existing convergence-vs-coverage distinction is currently prose-disciplined within the synthesis body. Preserved as a follow-up. Reopen warrant: a synthesis that conflates single-perspective coverage with multi-perspective convergence in a load-bearing way.

## Coverage (single-perspective points without dissent)

- **Cov-1.** P-2 alone reframed the operator-steering complaint as potentially "prompt-decay or framing bleed, not perspective count" [P-2, open_question]. The other five accept the perspective-shape framing without challenge. [synth]
- **Cov-2.** P-5 alone systematically imported cross-domain analogues (peer review, juries, design crits, appellate panels) flagged as hypotheses per the brief's external-imports rule. The other five reasoned only from the brief's evidence base. P-5's analogues mostly *confirmed* MAD v4's substantive disciplines rather than introducing new ones [P-5, position]. [synth]
- **Cov-3.** P-6 alone framed the load-bearing target as the *self-steering property* rather than perspective count [P-6, position]. Other perspectives addressed perspective count and disciplines as ends; P-6 addressed them as means.
- **Cov-4.** P-1 alone explicitly noted that the §4.4 timeseries cannot tell us "what a 3rd or 4th perspective would have produced" in the 24 deliberations beyond S124 — an acknowledgement of evidentiary limitation that no other perspective made [P-1, Position]. [synth]

## What the deliberation decides; what it leaves to the decision

The synthesis converges decisively on the **content** to restore: floor 3, adversarial required, named-not-rostered, shared/role-specific brief with immutability, four synthesis disciplines, no spec restoration. The genuine divergence is on the **enforcement layer** (D-1) — and the cluster on each side is evenly cross-family, citing opposing readings of constraints.md as warrant. This is exactly the kind of split where synthesis must map and not decide. [synth]

The decision-record is therefore the right surface to settle D-1, D-2, D-3 — supported by the convergent content (C-1 through C-7) and the genuinely divergent enforcement question. The minority positions M-1 through M-4 are preserved as named follow-ups with reopen warrants.

## Limitations

- All six perspectives reasoned from the same shared brief authored by the orchestrator. Brief-writing has no adversary in this deliberation; framing choices propagated identically. (MAD v4 limitation, §4.2 of brief.) [synth]
- Three of six perspectives are anthropic; three are openai. Cross-family is two-family, not three; google/gemini was available but unused. (Operator may consider whether to add a third family in a follow-up deliberation if D-1 substrate enforcement prevails and substrate role-kind / brief-hash machinery is being newly introduced.) [synth]
- The orchestrator both authored the brief and synthesised the perspectives. The synthesizer-not-a-perspective rule (C-5) is honored, but the brief-writer-not-the-synthesizer separation is not. The brief committed at `deliberations/131-restore-deliberation-shape/shared-brief.md` is auditable for framing influence. [synth]
- The synthesis is not a decision. The Decide activity (decision-record) operates on this synthesis, not on raw perspectives. [P-1, Q5 reaffirm; MAD v4 §4.2]


### Synthesis points

- **convergence C-1.** Floor of three valid perspectives; fewer is not a deliberation.
- **convergence C-2.** At least one adversarial role is required.
- **convergence C-3.** Named perspectives chosen for expected disagreement on this problem; no permanent roster.
- **convergence C-4.** Re-codify shared/role-specific brief split with immutability after commit.
- **convergence C-5.** Restore four synthesis disciplines: synthesizer-not-a-perspective, citation, [synth] markers, convergence-vs-coverage.
- **convergence C-6.** Do NOT re-import the 482-line MAD v4 spec.
- **convergence C-7.** Do NOT restore OI-004 closure machinery, manifest schemas, or validate.sh checks 16-19.
- **divergence D-1.** Enforcement layer: prose-only (P-1, P-2, P-6) vs substrate-enforced minimum kernel (P-3, P-4, P-5); 3-3 split, cross-family balanced.
- **divergence D-2.** Number target above floor: P-1 holds 3, P-2 allows 2 for narrow, P-3/P-4/P-5/P-6 cluster on 4 for methodology.
- **divergence D-3.** Brief metadata in substrate (P-3, P-4, P-5) vs workspace-files-only (P-1, P-2, P-6); same 3-3 split as D-1.
- **minority M-1.** P-3 Dreamer alone proposed closed-enum role roster; five others reject permanent rosters as accretion pathway.
- **minority M-2.** P-2 Skeptic alone allowed 2-perspective deliberation for narrow technical decisions.
- **minority M-3.** P-4 Substrate-engineer alone proposed perspectives.status enum (valid/refusal/invalid/missing).
- **minority M-4.** P-5 Outsider alone proposed adding coverage as fourth synthesis_points kind.
