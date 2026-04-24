---
feedback_id: EF-047-retrieval-discipline-and-text-system-scaling-ceiling
source_workspace_id: selvedge-self-development
source_session: 047
created_at: 2026-04-24
reported_by: operator
target: methodology
target_files:
  - specifications/methodology-kernel.md
  - specifications/read-contract.md
  - specifications/workspace-structure.md
  - specifications/multi-agent-deliberation.md
  - tools/validate.sh
severity: friction
status: inbox
---

# EF-047 — Retrieval-side discipline is absent and the text-only substrate is approaching its scaling ceiling

## Observation

The Selvedge engine preserves a growing accumulation of structured content — preserved minorities, activation warrants, watchpoints, open issues, forward observations, deferred spec-amendment candidates, archive-packs, manifests, per-session decisions, per-session deliberations — across specifications, provenance, open-issues, engine-feedback, and application artefacts. The **write-side discipline** for these is strong and enforced: validator checks on frontmatter, close-rotation rules, archive-pack manifest integrity (check 21), citation consistency (check 22), MAD v4 §Preserve Dissent, workspace-structure §applications revision discipline.

The **retrieval-side discipline is absent**. There is no kernel activity "at session-open, evaluate whether any preserved-minority activation warrant has fired". There is no validator check "every preserved minority in provenance has a living pointer in an active specification". There is no tool for "surface every archive-pack fragment relevant to this decision". There is no declaration of which specs must stay in sync when one changes. Retrieval happens when someone — a Case Steward, a subagent, a human operator — remembers to look, reads broadly, and notices a connection. The whole apparatus works by memory and vigilance.

The operator (in the post-S047 conversation leading to this record) identified the concrete failure mode: **dissent and suggestions preserved in a provenance file that rotates out of the default-read window after 6 sessions effectively disappear from retrieval unless an active-surface file carries a pointer and the reader is told to follow it.** The §2c close-rotation, which solves aggregate-budget pressure, simultaneously hides old sessions from default view. Archive-pack content is preserved byte-identical but is invisible unless explicitly cited. Activation warrants are prose statements in specs that "fire" only when someone notices they apply.

The operator also observed a second, related phenomenon: the engine has accumulated **a substantial layer of manifest / index / pointer infrastructure** — `SESSION-LOG.md` (thin index), `open-issues/index.md` (thin index) + 13 per-OI files, `engine-feedback/INDEX.md` (thin index) + inbox/triage records, `specifications/engine-manifest.md` (file enumeration), `read-contract.md` §1 default-read enumeration, archive-pack `manifest.yaml` with chunk hashes, every spec's §5 / §10 minority block with archive citations, `participants.yaml` per session, per-participant `manifest.yaml`, application-scope `assumption-ledger.md` / `supersession-ledger.md` (just proposed for the external arc), `MODE.md`, frontmatter with cross-file pointers (`supersedes:`, `originating_session:`, `last-revised-session:`). Each addition was locally justified. The aggregate is substantial: **the engine is, de facto, building its own ad-hoc database on top of markdown and YAML files.**

## Why It Matters

This record deliberately pushes back against the pattern the operator has observed repeatedly when raising scale concerns: **the Skeptic / Minimalist / Pragmatist perspective responds "it's not a problem right now; don't overengineer."** That response has been correct session-by-session. It has produced the engine's restraint-discipline, which is load-bearing (§5.2 vindication across multiple epochs). But its correctness is local and time-bounded, and applying it uncritically to this concern misreads the trajectory.

**The writing is on the wall.** Three converging pressures:

1. **Retrieval asymmetry compounds with time.** In a 46-session self-dev trajectory, the aggregate default-read surface has crossed 100K+ words once (Session 027) and been structurally remediated via close-rotation + minority-into-active-spec-consolidation discipline. The remediation works because **the load is dominated by methodology text and provenance** (bounded vocabulary, converging structure). When the engine is applied to a multi-year software-engineering project with 100+ sessions, evolving API specs, implementation plans, test suites, deployment decisions, and their cross-referenced dissent, the load is no longer dominated by methodology. It is dominated by domain content that grows unboundedly. The close-rotation's 6-session window is designed against self-dev-methodology growth rates; it is not designed against engineering-project growth rates. Applying it naively would rotate out load-bearing engineering context after 6 sessions — exactly the failure mode the operator is naming.

2. **The index-of-indices is approaching its own ceiling.** Four default-read index files (SESSION-LOG, open-issues/index, engine-feedback/INDEX, engine-manifest §3), each under-specified-against-scale, each growing linearly in the content they index. The close-rotation discipline handles one of them (SESSION-LOG close-files); the others have no analogous rotation. `open-issues/index.md` will cross the 6K soft warning when OI count reaches ~40-50 with current per-OI annotation density; at 100+ OIs it crosses the 8K hard ceiling. Similar for engine-feedback. The current count (13 active OIs, 3 inbox records) is far below; at engineering scale these thresholds are reachable within one project cycle.

3. **Agents cannot be told to look where indices don't point.** A preserved minority from Session 014 that isn't carried into an active spec's §10 block is, in practical terms, invisible at Session 047. The engine's "preserve all provenance" discipline is a **bit-level guarantee** (files aren't deleted; archive-packs are byte-identical) but it is **not an operational-retrievability guarantee**. The gap between the two is the failure mode the operator is flagging. And crucially, **an agent evaluating a new proposal cannot check "has this idea been rejected before?" against all preserved dissent** because there is no index across all preserved dissent — there are per-spec §10 blocks, but no unified surface listing every minority the engine has ever preserved. If the current proposal's rejected-before status is recorded only in a rotated-out 02-decisions.md, the agent will re-propose it in good faith and the engine will treat it as new.

**The "don't overengineer" response fails on this concern specifically.** That response is valid when the proposed mechanism is heavier than the problem it solves. Here the problem is already heavy and growing: the engine has quietly built substantial retrieval infrastructure in markdown/YAML while insisting it isn't building retrieval infrastructure. Each piece — open-issues/ split, SESSION-LOG thin-index restoration, engine-feedback INDEX, archive-pack manifests, §10 minority blocks, per-session participants.yaml — is a half-step toward structured retrieval. The accumulated weight of those half-steps already exceeds what a purpose-designed structured-retrieval layer would cost. The sunk cost fallacy now pushes toward continued accretion.

**If you are designing a complex methodology that has triggers, watchpoints, decisions, minorities, warrants, cross-session dependencies, and evolving specifications, you need a retrieval mechanism that (a) is fast, (b) is reliable, (c) minimises context usage.** Text-only optimises for (b) reliability (git-versioned; human-readable; diffable) but is increasingly poor on (a) speed and (c) context-economy. A 47-session self-dev trajectory is approximately at the limit of what a human-readable markdown-only substrate can support without structured retrieval tooling. Beyond that limit, the engine either (i) builds ad-hoc retrieval-proxies that grow messier and heavier than a database, (ii) accepts operational retrieval failures as normal and rationalises them ("it's not a problem right now"), or (iii) addresses the scaling ceiling deliberately.

The operator's framing is load-bearing: **this is a methodology question, not a spec question.** The specifications can be amended at engine-v8 or later to address pieces (retrieval discipline in kernel §1 Read; validator check that preserved minorities have active-spec pointers; spec-sync declaration field). But the underlying question — is text-only the right substrate for this methodology at engineering scale? — is more fundamental.

## Suggested Change

Three levels, forcefully ordered from minimum-viable to direction-correct:

**(A) Minimum: formalise retrieval discipline in the kernel.** Kernel §1 Read currently describes default-read + archive-by-reference. Add an explicit sub-activity: "Warrant evaluation — at session-open, after Read, scan every active specification's §5 / §10 / preserved-minority / activation-warrant section against the current session's context and record whether any warrant's condition has fired." Validator check that preserved minorities in any provenance 01-deliberation.md or 02-decisions.md have a living pointer in an active-spec minority-block (close-step obligation). This closes the write-to-retrieve gap at the policy layer. **Substantive kernel §1 amendment; engine-v7 → v8 candidate.**

**(B) Medium: make cross-spec synchronisation first-class.** Spec frontmatter gains a `syncs_with:` field naming specs whose coherence depends on this one. Validator check cross-checks named values (e.g., `read-contract.md` §2 budget values vs. `validate.sh` constants). This addresses the engineering-use-case requirement of keeping related specifications in sync. **Substantive workspace-structure + validation-approach amendment; engine-v7 → v8 candidate.**

**(C) Direction-correct: commit to a structured retrieval substrate.** The engine has accumulated enough pointer / manifest / index infrastructure that the next principled addition is a query layer on top. Options, ordered by how much they violate the text-primary preference: a dedicated query tool (`tools/query.sh`) that reads frontmatter + markdown headings and returns structured results; a SQLite-style index file (committed to git; regenerable from source) that indexes every preserved minority, warrant, OI, EF-record, archive-pack, and cross-reference; a full database-backed retrieval layer with the text files as the canonical source-of-truth. Each of these looks like overengineering against the current self-dev trajectory and like underengineering against the engineering trajectory. The choice is about which trajectory the engine is designed for. **Substantial methodology-level decision; properly routed via MAD v4 deliberation; likely multi-session design process.**

**A pre-emptive note on the expected Skeptic / Minimalist / Pragmatist response:** the argument "not a problem right now; don't overengineer" is correct for (C) today and loses force session-by-session. It is **already wrong for (A)** — kernel-level retrieval discipline has zero implementation cost beyond the amendment itself and addresses a gap that has been silent because we haven't noticed its consequences yet. The validator check "preserved minorities must have active-spec pointers" would have caught any drift minority that decayed into archive-only invisibility; I cannot prove drift minorities exist because the failure mode by definition makes them invisible, which is precisely the point. The correct restraint-discipline response to (A) is "yes, with care about what counts as preserved-minority vs. forward-observation"; not "not a problem."

## Evidence

- The engine currently carries four default-read index files (SESSION-LOG.md, open-issues/index.md, engine-feedback/INDEX.md, specifications/engine-manifest.md §3); three of them accumulate monotonically; one has an explicit rotation discipline (SESSION-LOG via §2c).
- Every active specification that has produced minorities has a §5 or §10 block: `read-contract.md` §5.1-§5.11; `workspace-structure.md` §10.4; `reference-validation.md` §10 (verified via grep at multiple prior sessions). The consolidation convention works at current scale.
- `open-issues/` directory split happened at Session 022 (D-084 R8b) when the single-file form became unwieldy; the split was a retrieval affordance, not a content change. The pattern will repeat: at some OI count, per-OI files will themselves need sub-indexing.
- OI-019 sub-question (f) "extended-baseline visibility mechanism periodic-vs-triggered-vs-narrow" (opened S043) is explicitly this territory; the current record contributes a direction (procedural retrieval; structured substrate) distinct from S046's contribution (external-workspace separation).
- Archive-pack discipline: 3 archive-packs in self-dev to date (Session 014 Outsider at 96,651 words; Session 022 Outsider at 22,611 words; Session 040 pre-L SESSION-LOG). `manifest.yaml` + `readers_note` (capped at 3 sentences) is pointer-only; retrieval requires reading the chunks directly. The `readers_note` constraint is intentional (prevents the manifest from becoming a summary that drifts from the content) but the consequence is that archive-pack content is functionally invisible without an external reader remembering to consult it.
- Session 043 Long-Baseline Auditor quantified a Path-A concentration at 47% post-engine-v4 because a Case Steward asked them to look cross-session. No standing mechanism would have surfaced that finding; it was visible only because of an explicit ad-hoc query.
- `validate.sh` has grown to 23 structural checks + 1110 assertions at S047. Much of this check logic is itself retrieval (iterate provenance directories; read frontmatter; cross-check SESSION-LOG rows against provenance directories). The validator is already a structured-retrieval tool; it is not called "a database" but it performs database-like operations. Extending it to serve the retrieval discipline gap is a natural next step.
- Operator-raised framing: the accumulation of manifests, pointers, indices, ledgers, frontmatter cross-references has reached the point where designing a dedicated structured-retrieval layer is no longer obviously more complex than continuing to add text-file retrieval-proxies.

## Application-Scope Disposition

The current 5-session `selvedge-disaster-response` arc **will not trigger this concern**. Five sessions is inside the close-rotation window; the accumulated application-scope content is small relative to self-dev; minority preservation will be limited (maybe 2-5 per arc); the assumption-ledger and supersession-ledger are single files manageable without structured retrieval. The arc proceeds under the current regime.

The concern is **forward-looking**. It becomes load-bearing when:

- An external application runs longer than ~10 sessions (rotates content out of the default-read window; active-spec consolidation becomes mandatory or content is lost).
- The engine is applied to software / engineering / research domains where specs evolve across many sessions and cross-spec coherence matters.
- The preserved-minority / watchpoint / warrant accumulation exceeds what any single Case Steward can hold in working memory at session-open.

Given operator intent to use the engine for software development in future, the concern is not theoretical; it is on the trajectory and will bind before that first software project completes. The post-arc self-dev review (per S047 D-150 obligation) should bundle this record with the three prior EF records and address at minimum the (A) minimum-viable response; (B) and (C) are harder decisions that properly warrant dedicated deliberation.

**Not open to the "not a problem right now" response at the (A) level.** The retrieval-discipline gap exists now; its invisibility is its diagnostic property. The record is filed to make the invisibility visible.
