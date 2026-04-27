Position: A — Ratify 17, enumerate all 17 tables in `specifications/engine-manifest.md`, and record the change as a calibration under 078 D-10’s existing “breachable with cause” clause.

The cleanest disposition is: schema remains unchanged, `synthesis_points` remains a first-class table, `objects` is listed explicitly, and the table budget becomes 17 for engine-v17. I would avoid introducing an “infrastructure-exempt” category during the release-gated period.

The strongest arguments for A:

1. **It uses the escape hatch D-10 already provided.**  
   Session 078 D-10 did not define the table limit as absolute; it explicitly allowed breach “with cause.” Session 079 D-2 already recorded the cause for `synthesis_points`: T-14 needs a durable structural place to enforce “convergence requires ≥2 source_perspectives,” and the omission was acknowledged as calibration. The current question is therefore not “may Selvedge exceed 16?” but “is this breach justified enough to record plainly?” I think yes.

2. **It minimizes methodology growth during the release gate.**  
   078 D-5 blocks methodology-expanding self-development before the external-problem trial closes. A table-budget calibration is specifically within the admitted class of changes. Option C may be technically accurate, but it introduces a new conceptual distinction: “domain tables” versus “substrate-infrastructure tables.” That is an attractive distinction, but it becomes another axis future sessions must maintain. Given the documented history of 75 self-development sessions and the restart’s emphasis on smallness, I would not add that category unless it solves an active operational problem.

3. **It aligns the manifest with the actual substrate.**  
   The active schema in `state/migrations/001-initial.sql` has 17 tables. The manifest currently enumerates 15, omitting both `objects` and `synthesis_points`. The manifest should not present a partial mental model of the substrate. If `objects` is required for T-01 ref resolution, it belongs in the manifest even if described as plumbing. If `synthesis_points` carries T-14 semantics, it also belongs there.

The strongest arguments against A:

1. **Counting `objects` as a normal table may blur architectural intent.**  
   `objects` is qualitatively different from `decisions`, `sessions`, `perspectives`, or `work_items`. It is indirection infrastructure for citable aliases, not a domain entity. Option C captures that distinction better. I take this seriously, but I weigh it below release discipline: accurate prose can say “`objects` is infrastructure for ref resolution” without creating a budget exemption category.

2. **Ratifying 17 may weaken the force of future budgets.**  
   If every breach becomes calibration, the budget stops constraining design. The answer is to make this ratification narrow: “17 for engine-v17 because `synthesis_points` enforces T-14 and `objects` supports T-01; no general relaxation.” The recorded cause should be concrete enough that future additions cannot cite this as generic permission.

The unstated assumption I would surface is that the table budget is a proxy for conceptual complexity, not a literal storage-object limit. If so, `objects` may be low conceptual load despite being a table, while `synthesis_points` is real methodology surface. The deliberation should decide whether budgets constrain physical tables, conceptual domain entities, or externally visible active-spec concepts.

What could change my answer: if `synthesis_points` is not actually queried, cited, or needed to enforce T-14 in practice, then subtracting it later may be sensible once the migration runner exists. Conversely, if external-trial use shows synthesis points are central to review, then 17 should become the stable budget rather than a temporary breach.
