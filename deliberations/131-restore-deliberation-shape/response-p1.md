**Position.** The post-restart drift is not a drift in *intent* — the prompt still says "convene perspectives when warranted" — but a drift in *shape*, because the prompt subtracted every disciplining element except cross-family. The §4.4 timeseries shows what an undisciplined "when warranted" produces under constraints.md property 2 (failure is cheap) and property 6 (the agent cannot see its own deficiencies while executing them): a 2-default that satisfies the rule with minimum effort. EF-S124-1 documents one cost-of-absence; the timeseries shows 24 further deliberations where we cannot know what a 3rd or 4th perspective would have produced because none was convened. The MAD v4 substantive core in §4.2 was disciplined precisely at the points the post-restart prompt left soft — number floor, role-naming, adversarial requirement, stance-brief shape, three-output quorum. Restoring those five elements, in prose at the prompt level rather than as substrate machinery, is the smallest move that addresses the drift without re-importing the 482-line spec. Subtraction holds: the OI-004 closure machinery, manifest schemas, and validate.sh checks 16–19 stay archived. What returns is the discipline that produced this engine for 75 sessions, condensed.

**Q1 (number).** Floor of 3, target 3, up to 5 when the problem spans clearly different concern-domains, written justification at convening time for >5. This is MAD v4 verbatim and the §4.4 evidence supports it: the one 4-perspective deliberation (S124) is the one EF-S124-1 names as load-bearing in a way the 2-default would not have produced. The 11 × 2-perspective deliberations are the drift the operator named. A floor of 3 means "convene perspectives when warranted" stops being satisfiable by the cheapest possible compliance.

**Q2 (role discipline).** Named perspectives chosen for expected disagreement on *this* problem, no permanent roster (MAD v4 §4.2 verbatim). Free-form labels (current state) collapse to "P-1 anthropic, P-2 openai" because the prompt names no axis of disagreement. Closed enums would re-create the accretion pathway. Operator-named axes is the middle path the pre-restart engine ran for 75 sessions; the §4.4 evidence does not show it failed.

**Q3 (required role).** Yes — at least one adversarial perspective, prose-disciplined at the prompt level, not substrate-enforced. Substrate enforcement (refuse `deliberation-seal` without an adversarial flag) would re-create the manifest-schema accretion pattern that the restart specifically subtracted. The constraints.md property 3 finding — cross-family deliberation reveals shape, not just answers — generalises to adversarial role: without one, the brief-writer's framing propagates uncontested (MAD v4 limitations boilerplate, §4.2: "brief-writing has no adversary").

**Q4 (stance-brief structure).** Re-codify the shared/role-specific split in prose. Briefs remain workspace files, not substrate rows — substrate would force the 482-line accretion path. The S131 brief itself is the existence proof that the structure is implementable in workspace markdown without schema change. Brief immutability after commit (MAD v4 §4.2) is the discipline that makes deliberations reproducible; that is worth one prompt-level sentence.

**Q5 (synthesis discipline).** Recover four elements at the prompt level: (a) synthesizer-not-a-perspective, (b) citation requirement for attributions, (c) `[synth]` markers for synthesizer-original claims, (d) convergence-vs-coverage distinction. The fifth — dissent preservation as majority/minority — is partially handled by `synthesis_points.kind` (convergence/divergence/minority already admitted, §4.6). No substrate change needed for (a)–(d); they are prose disciplines on the synthesis markdown. Constraints.md property 6 ("synthesis is the highest-risk single-agent re-entry point") warrants the citation discipline specifically.

**Q6 (graceful degradation).** Yes, restore "fewer than three valid outputs is not a deliberation" verbatim from MAD v4. With Q1's floor at 3, this is the natural quorum: refusal preserved as provenance, but the deliberation must be re-run or reformulated rather than synthesised over 1–2 outputs. This is prose discipline; no substrate gate needed.

**Q7 (smallest shape).** Replace prompts/development.md §4 (currently three sentences) with roughly twelve sentences covering: floor-3-target-3-up-to-5, perspectives-named-for-this-problem, adversarial-required, shared/role-specific brief split with byte-identical shared section, brief immutability after commit, synthesizer-not-a-perspective, citation + `[synth]` + convergence-vs-coverage, three-output quorum. No new substrate. No new spec file. The prompt absorbs the discipline; the substrate stays narrow.

**schema_sketch.**
- No schema change proposed. Existing `synthesis_points.kind` enum already admits convergence/divergence/minority.

**cli_surface.**
- No new CLI verbs. Existing `deliberation-open`, `perspective`, `deliberation-seal`, `synthesis-point` carry the load.

**migration_path.**
- S132 amends prompts/development.md §4 with the twelve-sentence discipline above.
- Engine-manifest version bump.
- No archive churn; MAD v4 stays in `archive/pre-restart/` as historical record.
- First post-amendment deliberation tests the floor-of-3 rule under live conditions.

**what_not.**
- No substrate-enforced adversarial flag (re-creates manifest accretion).
- No closed role-enum (re-creates roster pathway).
- No restoration of OI-004 closure machinery, Layer 2 manifest schema, four-state lifecycle, or validate.sh checks 16–19 (stale, excluded by brief).
- No new spec file; the discipline lives in the prompt.

**open_question.**
- Whether the operator wants to retroactively re-run any of the 11 × 2-perspective post-restart deliberations under the new floor, or grandfather them.
- Whether `synthesis_points.source_perspectives` should require non-empty for `convergence` kind (would substrate-enforce the convergence-vs-coverage distinction; might be accretion).
- Whether "load-bearing" warrants a marker on `deliberations` rows so EF authoring can audit floor-compliance.

**risk.**
- Twelve sentences in the prompt may decay under context pressure (constraints.md property 4) the same way the original three did. Mitigation: review at session-close should include a "did §4 hold?" check.
- Floor of 3 may produce ceremonial third perspectives where 2 was genuinely sufficient. The §4.4 evidence does not distinguish "drift" from "appropriate minimalism" for every case.
- Adversarial-required as prose discipline relies on operator policing; constraints.md property 2 says exhortative friction underperforms structural friction.

**what_lost.**
- The operational simplicity of the current 3-sentence §4. Authors must now satisfy more shape per deliberation.
- The 2-perspective default's speed for narrow technical disposition decisions. Some of the 11 × 2-perspective post-restart deliberations may genuinely have been right-sized.
- The option of treating MAD v4 as fully archived; this position re-imports its substantive core, even at reduced length.
