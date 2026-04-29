**Position.** Restore only the load-bearing minimum, not MAD v4. The evidence establishes drift in perspective count and one strong counterexample, but it does not establish that the full old shape was necessary. The accretion risk is internal evidence too: constraints.md property 6 says additions made to correct deficiencies can consume the slack needed to see deficiencies. So the answer should be a small prompt-level rule: foundational methodology decisions convene four named perspectives, chosen for disagreement on the question, including one adversarial perspective and at least one cross-family perspective; graceful degradation requires at least three valid outputs. Everything else should remain prose discipline unless repeated failures prove substrate enforcement is needed.

**Q1 (number).** Floor: three valid outputs for anything called multi-agent deliberation. Target: four perspectives for foundational or methodology-changing decisions. Default: do not make four universal. Use two only for bounded, implementation-adjacent questions where the decision does not change methodology shape. Use three for ordinary load-bearing choices. Use four for foundational decisions, ambiguous framing decisions, and cases where operator steering is likely to dominate. More than four requires a short convening note explaining the distinct disagreement axis added. The brief’s evidence supports a four-perspective target for at least S124-like decisions; it does not support a universal five-perspective or six-perspective norm.

**Q2 (role discipline).** Use named perspectives chosen for expected disagreement on this problem, with no permanent roster and no closed enum. A closed enum would import old machinery without evidence that role taxonomy caused the post-restart failure. Free-form labels alone are too weak, because the post-restart drift lost role differentiation. The minimal discipline is: each perspective gets a short stable name and a one-sentence disagreement charge at convening time. The charge should identify what this perspective is expected to contest, protect, or imagine. The operator should name axes of disagreement, not personalities.

**Q3 (required role).** Yes: one adversarial perspective is required for foundational or methodology-changing deliberations. I would not substrate-enforce it yet. The strongest internal warrant is MAD v4’s adversarial requirement plus the present role’s own concern: restoration-by-default is exactly the kind of consensus slide an adversarial role can resist. But the brief gives no worked example where a substrate refusal would have improved an actual past decision. So record the adversarial role in the brief and synthesis, and let session close or review catch omissions before adding database constraints.

**Q4 (stance-brief structure).** Re-codify the shared/role-specific split as prompt guidance for four-perspective foundational deliberations. Do not make briefs substrate rows. The current substrate refuses prose-in-rows by construction, and stance briefs are prose. Forcing them into substrate would fight property 1 in the wrong direction: it would either weaken the substrate’s atom discipline or create awkward fragments that lose the value of a coherent brief. Keep briefs as workspace files when used. The useful part to restore is immutability and diffability: shared sections byte-identical; role-specific stance the only variation; committed or otherwise fixed before perspectives launch. Do not restore the full six-section template as mandatory for every small deliberation.

**Q5 (synthesis discipline).** Restore four synthesis disciplines in prose: source citation for attributed claims, convergence-vs-coverage distinction, dissent preservation, and synthesizer-not-a-perspective. These map directly to known risk points in the brief: correlated model-family agreement, operator framing propagation, and synthesis as the highest-risk single-agent re-entry point. `[synth]` markers are useful but should be required only for load-bearing synthesizer-original claims. Quote-over-paraphrase should be guidance, not a rule; requiring it globally invites ceremony. Synthesis should continue to map rather than decide. The existing `synthesis_points.kind` enum already supports convergence, divergence, and minority; do not expand schema until a concrete synthesis failure demands it.

**Q6 (graceful degradation).** Keep the old floor: fewer than three valid outputs is not a deliberation. This is one of the few old rules with a clear conceptual warrant. One or two outputs cannot distinguish deliberation from ordinary comparison, and the post-restart mode of two is exactly the drift under examination. For a four-perspective foundational deliberation, three valid outputs may proceed only if the missing output is preserved as provenance and the synthesis states the degradation. If the adversarial perspective is missing, the synthesis should say adversarial coverage is absent rather than pretending the quorum carried the same weight.

**Q7 (smallest shape).** The smallest shape is a prompt-level convening rule, not a restored spec: “For foundational or methodology-changing deliberations, convene four named perspectives chosen for disagreement on this problem, including one adversarial and one cross-family perspective. Use immutable shared/role-specific briefs. Synthesis must cite sources, separate convergence from coverage, preserve dissent, and mark load-bearing synthesizer-original claims. Fewer than three valid outputs is not MAD.” That is the minimum that addresses the observed two-perspective drift and S124 evidence without recreating the 482-line pathway.

**schema_sketch.**
- No schema change now.
- Use existing `perspectives.label`, `perspectives.family`, and `synthesis_points.kind`.
- If failures recur, consider adding a lightweight `role_charge` atom later, but only with a worked failure case.

**cli_surface.**
- No new CLI verbs.
- Optional future enhancement: `deliberation-open` could accept repeated `--role "Name: charge"` flags, but this is not necessary for the first restoration.

**migration_path.**
- Patch `prompts/development.md` §4 with the four-perspective foundational rule.
- Add a short synthesis checklist to the same section.
- Run the next few methodology-changing deliberations under this rule.
- Reassess only from observed misses, not from speculative completeness.

**what_not.**
- Do not restore `specifications/multi-agent-deliberation.md`.
- Do not add lifecycle machinery, manifest layers, or validation checks from MAD v4.
- Do not create a permanent perspective roster.
- Do not substrate-store prose briefs.
- Do not make four perspectives mandatory for every deliberation.

**open_question.**
- The brief does not show which of the 11 two-perspective deliberations produced worse decisions.
- The operator-steering complaint may partly be prompt-decay or framing bleed, not perspective count.
- It is unclear whether cross-family availability is operationally reliable enough for hard enforcement.

**risk.**
- A prose-only rule may drift again.
- Four perspectives may become ceremony for questions that only need two.
- The adversarial role may become performative if the stance brief is weak.
- Without substrate counters, the engine may not notice gradual noncompliance.

**what_lost.**
- This gives up the reproducibility and enforcement strength of full MAD v4 in exchange for lower context weight and lower accretion risk.
