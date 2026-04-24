---
triage_id: EF-001-triage
feedback_ref: ../inbox/EF-001-read-contract-budget-scaling-for-domain-artefacts.md
triaged_in_session: 048
triaged_at: 2026-04-24
status: resolved
disposition: operator-directed-resolution adopted this session via substantive read-contract.md v4→v5 + minor prompts/application.md §Read clarification + engine-v7→v8 bump; deliberation skipped per operator_directed_resolution frontmatter field on source inbox record
opened_issue: null
spec_amendments:
  - path: specifications/read-contract.md
    from_version: 4
    to_version: 5
    classification: substantive
  - path: prompts/application.md
    classification: minor
  - path: specifications/engine-manifest.md
    classification: documentary
    note: engine-v7→v8 bump entry in §7
decision_records:
  - D-153
  - D-154
engine_version_impact: engine-v7 → engine-v8
subsumed_deferred_candidates:
  - session: 047
    decision: D-150
    candidate: (iv)
    description: read-contract.md §1 vs prompts/application.md §Read ambiguity resolution
---

# Triage — EF-001 read-contract-budget-scaling-for-domain-artefacts

## Classification

**Target**: engine. **Severity on inbox record**: friction. **Source**: `selvedge-disaster-response` Session 001, operator-relay direct-to-inbox.

**Disposition**: **resolved** this session. The source inbox record carried the `operator_directed_resolution` frontmatter field declaring resolution direction as "not open to deliberation". Deliberation is therefore structurally excluded from this triage. Adoption executed single-orchestrator this session per S048 D-152 (path ratified) + D-153 (substantive amendment) + D-154 (engine-v7→v8 bump).

## Adoption summary

Four operator-directed resolution items were each translated to concrete specification language:

1. **Exclude `applications/` from §2 per-file budget** → `read-contract.md` v5 §2d new section codifying the per-file-budget carve-out for `applications/NNN-<slug>/`; consequential non-contribution to §2b aggregate follows from `applications/` remaining outside the §1 closed enumeration.
2. **§2b aggregate budget continues to apply** → preserved unchanged (applies to §1 enumeration aggregate as before; `applications/` never was in §1 so the aggregate scope is unchanged in normative content, merely made explicit by the new §2d text).
3. **Chunked-read-on-demand via existing Read-tool offset/limit** → `read-contract.md` v5 §2d names the mechanism explicitly ("partial reads via Read tool with `offset` and `limit` parameters, with repeated partial-reads as work progresses"); no new tool built; no archive-pack machinery required for application-scope artefacts.
4. **Optional manifest/index as navigation pointer** → `read-contract.md` v5 §2d names the pattern optional; recommends thin (target under 1,000 words) for large applications; not mandatory.

Additionally, `prompts/application.md` §Read is amended minor-documentary to remove the "and `applications/`" inclusion in the Workspace-reading bullet (the source of the S047 P3 Outsider latent spec-contradiction finding) and to restructure the Domain-reading bullet to name §2d chunked-read-on-demand + the optional index pattern explicitly.

`tools/validate.sh` is unchanged: check 20 (default-read per-file budget) was already not counting `applications/` files in its default-read aggregate because §1 was already closed pre-v5; the carve-out codifies the pre-existing behaviour without requiring a new enforcement mechanism.

## Subsumed deferred candidate

S047 D-150 deferred spec-amendment candidate **(iv)** (`read-contract.md` §1 closed enumeration omits `applications/` while `prompts/application.md` §Read treats `applications/` as a read input, making hidden application-scope content ambiguous) is **resolved by direction** via this adoption. The documentary half (bring `prompts/application.md` §Read into alignment with `read-contract.md` §1 closure) is executed this session; nothing further is required for candidate (iv) at S049 or the post-arc self-dev review. The three remaining deferred candidates from S047 D-150 ((i) kernel §7 qualitative-multi-agent label; (ii) workspace-structure §provenance supersession-marker codification; (iii) OI state-machine constraint-invalidated transition) are unchanged by this triage.

## Forward observations

- **First-ever adoption via `operator_directed_resolution` frontmatter field.** The field was introduced ad-hoc on the EF-001 inbox record post-original-creation (commit 12743be per git history). Precedent established: the field carries resolution direction that is pre-declared as not-for-deliberation; adopting session implements rather than re-deliberates. Forward-convention candidate: `specifications/workspace-structure.md` v5 §engine-feedback may benefit from a minor documentary codification of the field. Deferred to a future session (not bundled with S049 MAD because its scope is §engine-feedback documentation rather than the retrieval-discipline methodology territory of the S049 scope).
- **First-ever inbox→triage→resolved lifecycle transition.** EF-001 completes the full lifecycle within a single triage session. Observed-clean execution; no structural adjustment to the inbox/triage/resolved machinery was required. Continues to validate the §engine-feedback adoption at S036.
- **External workspace inheritance.** The `selvedge-disaster-response` external workspace inherited the pre-carve-out budget language at its S001 session-open (engine-definition files copied at engine-v7 per S046 D-142 bootstrap). Operator-mediated transport of the v5/v8 update into the external workspace is a between-sessions operator action; the external workspace's next session-open may re-copy engine-definition files or receive an operator-delivered diff.

## OI impact

No OI opened. No OI resolved. OI-019 unchanged by this triage (sub-question (f) "extended-baseline visibility mechanism" is distinct from applications/-scope per-file-budget scoping).
