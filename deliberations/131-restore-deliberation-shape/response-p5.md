**Position.** Restore a small, disciplined deliberation shape: four convened perspectives by default, at least three valid outputs, named for expected disagreement on the specific problem, with one explicit adversarial role and one cross-family role. The recurring pattern across mature deliberation traditions is not “more voices”; it is independent precommitment, differentiated responsibilities, preserved dissent, and a synthesizer/editor/judge who maps rather than becomes another advocate. External: I am importing peer-review panels, appellate panels, design crits, juries, safety review boards, and red-team exercises from outside this brief; treat as hypothesis, not warrant. Read through §4, those analogues mostly confirm what MAD v4 already disciplined and what the restart lost.

**Q1 (number).** Floor: three valid outputs. Target: four convened perspectives for methodology-changing or load-bearing decisions. Cap: five without special ceremony; more than five requires written justification at convening. Two outputs should be recorded as consultation, not multi-agent deliberation. MAD v4’s default three was defensible, but the post-restart timeseries shows that weak prompt guidance slides toward two, and S124 shows four can surface load-bearing content missed by a two-default. External: appellate courts often use odd panels to avoid ties; treat as hypothesis. Here, synthesis maps and does not decide, so tie avoidance is less important than coverage and blind-spot disruption.

**Q2 (role discipline).** Use named perspectives chosen for expected disagreement on this problem, with no permanent roster. Do not use a closed enum of substantive roles; it would accrete and invite rote filling. Do require each perspective to carry a declared axis: what it is expected to notice, defend, or attack. The substrate can require `label` and `stance_summary`; prose should require the convening note to say why this perspective is expected to disagree. External: peer review and design crits both separate reviewer identity/function from the particular paper or artifact; treat as hypothesis. The engine needs that flexibility because constraints.md property 3 says shared shape is the danger, not merely missing a checklist slot.

**Q3 (required role).** Yes: at least one adversarial perspective is required. It should be substrate-enforced at seal time: no `deliberation-seal` if no submitted valid perspective is marked adversarial. This is exactly the kind of structural friction constraints.md properties 1, 2, and 5 require. Prose-policed adversarial discipline was lost after restart; the observed drift is evidence that exhortation is insufficient. The adversary should not be a generic contrarian. Its stance brief must name what consensus or proposal it is expected to challenge.

**Q4 (stance-brief structure).** Re-codify the shared/role-specific split. Briefs may remain workspace files, but the substrate should record enough metadata to verify the shape: shared brief hash, role-specific stance hash, committed-before-launch timestamp, and perspective label. The byte-identical shared section is important because it makes framing variance inspectable; it also prevents the convening agent from quietly steering different models with different facts. External: blind peer review and jury instructions both depend on common instructions before independent judgment; treat as hypothesis. The analogue fails partly because LLMs do not remember institutional norms, so immutability and hashes matter more here than in human processes.

**Q5 (synthesis discipline).** Restore the small core: synthesizer was not a perspective; attributed claims cite source perspective and question or section; synthesizer-original claims use `[synth]`; convergence is distinguished from coverage; dissent and minority positions are preserved; synthesis maps, it does not decide. Quote-over-paraphrase should be guidance for load-bearing claims, not a universal rule. The existing `synthesis_points.kind` enum already supports convergence, divergence, and minority, but it misses coverage; add coverage or make “single-source support” structurally visible. External: appellate dissents and peer-review minority reports treat disagreement as signal rather than failure; treat as hypothesis. That maps directly to MAD v4 and to S124, where a non-majority-like creative perspective produced design content.

**Q6 (graceful degradation).** The MAD v4 floor should return: fewer than three valid outputs is not deliberation. With target four, one failed or refused perspective can be preserved without collapsing the process. A refusal should remain provenance, not be coerced into agreement or replaced silently. If fewer than three valid outputs return, the operator must either re-run, reformulate, or explicitly downgrade the artifact from deliberation to consultation. External: hung juries and failed peer-review rounds have procedures for non-decision; treat as hypothesis. The LLM-specific reason is sharper: constraints.md property 2 says retry is cheap unless the system makes degradation consequential.

**Q7 (smallest shape).** The smallest viable shape is: four convened, three valid minimum, one cross-family, one adversarial, named roles with expected-disagreement rationale, immutable shared/role brief hashes, and synthesis points that cite sources while distinguishing convergence, divergence, minority, and coverage. This is not a 482-line spec restoration. It is the load-bearing spine of MAD v4 translated into a few substrate checks and a short prompt section.

**schema_sketch.**
- Add `deliberation_roles(deliberation_id, perspective_id, role_kind, stance_hash, shared_brief_hash, expected_disagreement)`.
- `role_kind` closed only for process roles: `adversarial`, `generative`, `constraint`, `domain`, `operator`, `other`; labels remain free text.
- Add `synthesis_points.kind = coverage` or require `source_count` so single-perspective points cannot masquerade as convergence.
- Add seal checks: at least three valid perspectives, at least one adversarial, at least one cross-family when rule applies, shared brief hash consistent.

**cli_surface.**
- Extend `deliberation-open` with `--target-perspectives`, `--shared-brief-hash`, and `--rationale`.
- Extend `perspective` with `--role-kind`, `--stance-hash`, and `--expected-disagreement`.
- Extend `deliberation-seal` to refuse invalid quorum or missing adversarial role.
- Keep `synthesis-point`, but add `coverage` or require explicit source count.

**migration_path.**
- First update `prompts/development.md §4` with the restored minimum shape.
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
- Whether `coverage` deserves its own `kind` or can be derived from `source_perspectives`.
- Whether brief immutability must be git-commit enforced or whether substrate hashes are enough.
- Whether human/operator perspectives should count toward the quorum when LLM-family blind-spot risk is the reason for deliberation.

**risk.**
- Four perspectives may become ceremony if used for non-load-bearing work.
- A required adversarial role may become performative unless the stance names a real proposal to attack.
- Substrate checks may overfit today’s failure mode and create new accretion pressure.
- Role-kind enums may slowly expand unless treated as process metadata, not taxonomy.

**what_lost.**
- Faster two-perspective deliberations lose status as full MAD.
- Operator discretion narrows at seal time.
- Some lightweight questions will need to be downgraded or reformulated rather than synthesized.
- The engine gives up a little flexibility to regain the deliberation shape that made disagreement productive.
