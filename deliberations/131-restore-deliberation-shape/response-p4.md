**Position.** The engine should restore a small substrate-enforced deliberation kernel: minimum three valid perspectives, at least one cross-family perspective, at least one adversarial role, named perspectives selected for this problem, and synthesis rows that preserve convergence, divergence, and minority claims distinctly. The post-restart drift is exactly the kind of erosion constraints.md predicts: prose discipline decayed into the cheapest workable pattern. I would not re-import MAD v4 as a spec. I would encode only the disciplines whose absence changes behavior: quorum, role function, adversarial presence, and synthesis coverage. Brief structure and limitations boilerplate should stay prose/workspace discipline unless repeated failures show they need substrate.

**Q1 (number).** Fixed floor: three valid perspectives before `deliberation-seal` succeeds. Target: four for methodology-shaping or foundation-touching decisions; three for narrower but still deliberation-worthy questions. More than five should require an explicit convening note, but I would not enforce the upper bound initially. The critical substrate rule is the floor, because “two perspectives” has become the attractor.

**Q2 (role discipline).** Keep free-form `label`, add closed `role_kind`. Labels remain problem-specific names; `role_kind` records structural function. I propose: `generative`, `implementation`, `adversarial`, `historical`, `operator`, `external`. This is not a permanent roster. It lets the substrate check that the deliberation has functional diversity without pretending the enum captures the actual axis of disagreement.

**Q3 (required role).** Yes: require at least one `role_kind='adversarial'` before seal. This belongs in substrate. Property 2 says failure is cheap, and property 5 says lessons do not survive across sessions; an adversarial prose reminder will decay exactly as the perspective count did.

**Q4 (stance-brief structure).** Re-codify shared/role-specific split in prompt prose and workspace convention, not substrate yet. The byte-identical brief discipline is valuable, but hard to express without turning the substrate into a document-management system. Substrate should store optional brief metadata: `brief_path`, `brief_committed_at`, maybe `brief_sha256`. It should not store the full brief body or validate section diffs unless a future failure pattern demands it.

**Q5 (synthesis discipline).** Preserve existing `synthesis_points.kind` values but strengthen seal checks: if any perspective exists with `role_kind='adversarial'`, seal should require at least one `divergence` or `minority` synthesis point, or an explicit `no_adversarial_dissent` row. I would add a `synth_origin` or `source_perspectives` non-empty requirement for non-synth claims rather than encode citation syntax. Citation format, `[synth]` markers, quote-over-paraphrase, and synthesis ordering are prose-only for now. The substrate should enforce the existence of coverage categories, not parse literary quality.

**Q6 (graceful degradation).** Restore MAD v4’s rule: fewer than three valid outputs is not a deliberation. Refusals should be preservable as perspective rows with a `status`, but only `status='valid'` counts toward quorum. A synthesis over one or two perspectives may be useful analysis, but it should not seal as multi-agent deliberation.

**Q7 (smallest shape).** Add `role_kind` and `status` to `perspectives`; add quorum/adversarial checks to `deliberation-seal`; add minimal synthesis integrity checks. Everything else remains prose. This directly addresses the observed drift without reviving the 482-line spec.

**schema_sketch.**
- `perspectives.role_kind TEXT NOT NULL DEFAULT 'generative' CHECK role_kind IN ('generative','implementation','adversarial','historical','operator','external')`
- `perspectives.status TEXT NOT NULL DEFAULT 'valid' CHECK status IN ('valid','refusal','invalid','missing')`
- `deliberations.min_valid_perspectives INTEGER NOT NULL DEFAULT 3 CHECK min_valid_perspectives >= 3`
- `deliberations.target_perspectives INTEGER NOT NULL DEFAULT 4 CHECK target_perspectives >= min_valid_perspectives`
- `deliberations.brief_path TEXT NULL`
- `deliberations.brief_sha256 TEXT NULL`
- Seal check: valid perspective count must be `>= min_valid_perspectives`.
- Seal check: at least one valid perspective must have `role_kind='adversarial'`.
- Seal check: at least one valid perspective must have `family != convening/default family`, preserving the current cross-family commitment.
- Seal check: if any `synthesis_points.kind='divergence'`, require at least one `minority` row or require each divergence row to carry non-empty `source_perspectives`.

**cli_surface.**
- `bin/selvedge submit deliberation-open --topic ... --target-perspectives 4 --brief-path ...`
- `bin/selvedge submit perspective --label ... --family openai --role-kind adversarial --body-md ...`
- `bin/selvedge submit perspective --label ... --family anthropic --role-kind adversarial --status refusal --body-md ...`
- `bin/selvedge submit deliberation-seal ...` refuses with explicit missing conditions: quorum, adversarial role, cross-family perspective, or synthesis coverage.

**migration_path.**
- Add nullable columns first, backfill existing perspectives with `role_kind='generative'` and `status='valid'`.
- Backfill deliberations with `min_valid_perspectives=3` and `target_perspectives=4`.
- Update CLI to require `--role-kind` for new perspectives after migration.
- Add seal-time validation after historical rows are migrated, so old deliberations remain readable without pretending they met the new standard.
- Export generated markdown with role kind and status visible beside label/family.

**what_not.**
- Do not restore the full MAD v4 spec.
- Do not substrate-validate byte-identical brief sections yet.
- Do not create a permanent role roster.
- Do not parse citations or enforce `[synth]` syntax in SQLite.
- Do not add lifecycle machinery beyond valid/refusal/invalid/missing status.

**open_question.**
- Whether `operator` should be a `role_kind` or only a `family='human'` perspective.
- Whether target four should be a hard requirement for foundation-touching decisions, which would require adding a decision-kind enum.
- Whether `external` is too vague as a role kind and should instead remain a label-level convention.

**risk.**
- The enum may become ceremonial if operators pick role kinds mechanically.
- A required adversarial role can produce performative objection rather than real disagreement.
- Seal checks may encourage minimal compliance unless synthesis review remains substantive.
- Brief discipline could decay next, because this proposal leaves it mostly prose-policed.

**what_lost.**
- Some flexibility is lost: two-perspective deliberations can no longer seal as MAD.
- Some simplicity is lost: every perspective now needs a role kind and status.
- Some nuance is lost by reducing role function to a small enum.
- Some reproducibility from MAD v4 is left outside substrate, especially stance-brief immutability and citation syntax.
