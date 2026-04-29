**Position.** The post-restart drift to a 2-perspective default is not primarily a number problem — it is a self-steering problem. The pre-restart engine's MAD kept the operator as a participant rather than a steering wheel by building structural mechanisms that made operator nudging structurally costly. Those mechanisms were subtracted at the restart, and what remained — three sentences in §4 of the prompt — is insufficient to hold deliberation shape under context pressure. Restoring self-steering requires identifying the two or three highest-leverage mechanisms from MAD v4 and re-encoding them at the right layer, not re-importing the full 482-line spec.

**Q1 (number).** Floor: three. Default: four for decisions that change how the methodology works; three for contained mechanical decisions. The evidence is direct: S124 at four perspectives produced design the operator identifies as load-bearing; the eleven 2-perspective deliberations in the post-restart timeseries produced no equivalent finding. The floor of three is warranted by the MAD v4 graceful-degradation rule — fewer than three valid outputs is not a deliberation. The target of four is not a restoration of the five-default but a correction of the drift below the minimum. Justification-to-deviate is required for any deliberation that drops below the default; the justification is recorded at convening time, not retroactively.

**Q2 (role discipline).** Perspectives are selected for expected disagreement on *this* problem. No permanent roster. The convening agent names the axes-of-disagreement before launching any perspective — this is the load-bearing discipline. Naming the axes forces the operator to make the disagreement-structure legible before the deliberation begins, which is the mechanism that makes the operator a participant in framing rather than a retroactive narrower. Free-form labels are acceptable; a closed enum is not necessary. The requirement is that each perspective has a short name used consistently throughout brief, raw output, synthesis, and decision record.

**Q3 (required role).** Yes: at least one perspective must be adversarial. The requirement is prose-disciplined, not substrate-enforced. The rationale is property 3 from constraints.md: perspectives from the same model family share training-distribution blind spots that look like disagreement but are actually shared priors. The adversarial requirement is the cheapest available structural insurance against consensus-as-shared-prior. It does not require a different model family, but it pairs with the existing cross-family rule. Together: cross-family provides different-prior coverage; adversarial-required provides within-brief pushback.

**Q4 (stance-brief structure).** The shared/role-specific split must be re-codified. The mechanism that made it self-steering: brief immutability commits the framing before any perspective launches, making mid-flight operator nudge impossible. The constraint on external imports in every brief (§6 of the current shared brief) is a direct descendent of this — it asks each perspective to flag pretrained framings, which is the cheapest check against operator vocabulary propagating through all perspectives identically. Both constraints — immutability and external-import flagging — belong in the brief structure, not only in the shared brief of one deliberation. Stance briefs are workspace files; they do not need to be substrate-recorded. The substrate already captures perspective bodies; the brief is the input that produced the perspective, and the commit timestamp on the brief file is sufficient provenance.

**Q5 (synthesis discipline).** Four of the five MAD v4 synthesis rules are load-bearing for the self-steering property: synthesizer-not-a-perspective, citation requirement, `[synth]` markers, and convergence-vs-coverage distinction. The fifth — synthesis-order anchoring — is process tidiness without self-steering value and can be dropped. The synthesizer-not-a-perspective rule is the highest-priority: it closes the re-entry point where the operator (or orchestrator) could otherwise deliberate and decide in the same role. Citation requirement and `[synth]` markers together make post-deliberation audit of operator-influence on synthesis tractable. Convergence-vs-coverage protects against over-reading consensus. Dissent preservation is implied by the minority kind in the existing synthesis_points substrate schema.

**Q6 (graceful degradation).** The MAD v4 floor applies: fewer than three valid outputs is not a deliberation and must be re-run or reformulated. Stance refusal is provenance, not error. The substrate already records perspective bodies; a refused or empty perspective body is meaningful signal. No new schema change is needed. The floor should be prose-disciplined in the prompt, not substrate-enforced.

**Q7 (smallest shape).** The smallest shape that addresses the post-restart drift is three prose additions to `prompts/development.md` §4, currently three sentences. Addition 1: perspective floor (three minimum, four default for methodology-changing decisions), with deviation requiring justification recorded at convening time. Addition 2: adversarial requirement (at least one perspective's named job is to challenge emerging consensus). Addition 3: brief immutability requirement (briefs committed before any perspective launches; not edited during deliberation). These three, together with the existing cross-family rule, restore the self-steering property without re-importing the 482-line spec. Role-specific stance structure (the shared/role-specific split) is already embodied in this deliberation's brief files and serves as the living template; it does not need additional prose encoding beyond noting the structure in §4.

**schema_sketch.**
- No schema changes required. The existing `perspectives` table, `synthesis_points` table, and closed `section_kind` enum are sufficient.
- If substrate enforcement of the adversarial requirement is desired later, `perspectives` could admit a `role_kind` column with a closed enum including `adversarial` — but this is not the minimum viable shape.

**cli_surface.**
- No new CLI verbs required. The existing `deliberation-open`, `perspective`, `deliberation-seal`, and `synthesis-point` verbs are sufficient.
- The deviation-justification for dropping below the default perspective count can be recorded as a `synthesis-point` with kind `minority` at convening time, or as a note in the deliberation topic.

**migration_path.**
- Edit `prompts/development.md` §4 to add the three prose additions (perspective floor, adversarial requirement, brief immutability). This is a single file edit, no substrate migration, no archive recovery.
- The living template for the shared/role-specific brief structure is this deliberation's files; reference them from §4 or archive a canonical template in `specifications/` as a single short file (not 482 lines).
- Future deliberations adopt the new §4 immediately; past deliberations are not retroactively affected.

**what_not.**
- Do not re-import the 482-line MAD v4 spec. The stale machinery (OI-004 closure, Layer 2 manifest schema, validate.sh checks) is dead weight.
- Do not substrate-enforce the perspective floor or adversarial requirement. Prose discipline at the prompt layer is sufficient; substrate enforcement adds friction without adding the self-steering property.
- Do not add a permanent perspective roster. Selection by expected disagreement on *this* problem is the mechanism; a roster would flatten it.
- Do not require cross-family enforcement beyond the existing rule. The adversarial requirement is the complementary mechanism; they are not equivalent.

**open_question.**
- The brief-immutability requirement assumes the convening agent is not also a perspective. In practice, is the orchestrator sometimes also P-1? If so, the synthesizer-not-a-perspective rule needs to extend to cover this.
- Is the deviation-justification for dropping below the default recorded in the substrate, in the brief, or only in the prompt? The current schema has no field for convening-time justification; a lightweight convention should be named.

**risk.**
- Prose-only additions to §4 are vulnerable to the same context-pressure decay that eroded the original three sentences. Property 4 (models lose foundational instructions under context pressure) applies here. The three additions are more specific and therefore slightly more resistant, but not immune.
- Naming axes-of-disagreement before launching perspectives requires the operator to have already partially analysed the problem — if the operator has not, the pressure to skip the step is high and prose discipline will not hold.

**what_lost.**
- If the adversarial requirement is prose-only, it will be dropped under time pressure without consequence the engine can perceive. This is the cost of not substrate-enforcing it.
- Keeping brief files as workspace files (not substrate-recorded) means the input that produced each perspective is not queryable alongside the perspective body. Provenance is weaker than it could be.
- Dropping synthesis-order anchoring loses one deterrent against synthesis-order anchoring bias — the first perspective presented tends to frame the synthesis. The cost is small but real.
