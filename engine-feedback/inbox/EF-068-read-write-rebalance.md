---
feedback_id: EF-068-read-write-rebalance
source_workspace_id: selvedge-self-development
source_session: 068
created_at: 2026-04-26T13:35:00Z
reported_by: operator
target: methodology
target_files:
  - specifications/read-contract.md
  - specifications/records-contract.md
  - specifications/workspace-structure.md
  - prompts/development.md
  - engine-feedback/inbox/EF-068-substrate-load-bearing-and-harness-telemetry.md
severity: friction
status: new
---

## Observation

The engine's read/write discipline is structurally asymmetric in a way that compounds across sessions:

- **Forced-write discipline is highly active.** Every session produces decisions (with required `triggers_met:` + `triggers_rationale:` + `Single-agent reason:` if applicable + `Non-Claude participation:` if applicable), close-narrative §1-§11 (with required §1a-§1e + §2-§10 substantive content), records-substrate row, INDEX updates, and (when triggered) MAD artefacts + Tier 2.5 audit + manifests + participants.yaml + codex/Gemini logs. Engine-conventional "[none]"-trigger housekeeping decision pattern produces 15 sub-sections (a-o) per session × 40 consecutive sessions = ~600 housekeeping sub-sections, most of which are stable across sessions. Cumulative: ~5K words written per session minimum + multi-K extra at MAD/triggered closes.

- **Read discipline is empirically static across multi-session windows.** The default-read surface (per `read-contract.md` v6 §1) is 22 files at session-open; the orchestrator reads them via the Read tool but engagement-with vs orientation-from is unmeasured. Off-default-read content (50 first-class minorities; 4 active watchpoints; (z5) lifecycle ledger; 13 OIs; 12 EF records — historical and current) is referenced in close-narratives but rarely consulted in depth. The substrate exists for cross-session queries but has empirically near-zero adoption (per EF-068-substrate-load-bearing-and-harness-telemetry sibling EF).

- **The write side outpaces the read side because writes are mechanically forced and reads are mechanically encouraged.** Validate.sh checks (1-28) enforce write structure (frontmatter + sections + decision shape + manifest schema + records-substrate integrity). No equivalent mechanism enforces read engagement. The "read at session-open" obligation in `prompts/development.md` is a prompt-side instruction; whether the agent actually engaged or skim-read is unobservable. The asymmetry is structural.

- **Aggregate budget pressure is constant**, addressed via close-rotation (S<N-6> rotates out at S<N>). But close-rotation is a write-side coping mechanism — it bounds aggregate by removing-from-default-read; it does not address whether the next session reader engages with the artefacts that remain.

- **Every session produces a 15-sub-section housekeeping decision** (§D-NNN-final per S048+ pattern). The sub-sections (a)-(o) cover: validator state, aggregate measurement, engine version, first-class minorities, active OIs, engine-feedback state, validation-debt ledger, WX-28-1 close-rotation, WX-24-1 MAD v4 streak, WX-43-1 cumulative tracking, WX-44/47 codex-CLI, WX-50-1/58-1/62-1 closure status, Layer 2 trigger evaluation, D-129/138 standing discipline, and pattern continuation. Most of these are stable session-to-session and update by single increment (close-rotation +1; streak +1; preservation depth +1). The full-prose housekeeping carries forward without substantive change but consumes write budget + read attention every close.

The fundamental observation: **forced-write discipline produces an artefact-rich workspace; read discipline does not keep up because the artefacts can be referenced cheaply (in-line cross-references) without being engaged**. The substrate was the engine's tool to make engagement cheap-and-mechanical; in practice the substrate's non-use makes non-engagement cheap-and-invisible.

## Why It Matters

The cumulative impact:

1. **Read-engagement quality degrades over time.** Cross-references become richer (every close-narrative cross-references prior decisions, prior minorities, prior watchpoints, prior EF records); but the references are cheap. The reader-side check that "the reference is actually load-bearing" depends on the reader engaging with the cited content, which is unobservable. The engine accumulates pseudo-evidence — claims that look substantive (citation-rich) but are not mechanically verified.

2. **Forced-write rate amplifies the asymmetry.** Each new session adds another ~5K words of cross-referenced content. Six-session retention window means the next session reader has ~30K words of recent close-narrative + 4-5 EF records + lifecycle ledger to engage with. At skim-read rate, this is feasible; at engage-with rate, it is not. The system passively trades engagement-depth for citation-breadth.

3. **Housekeeping content propagates by inertia.** The 15-sub-section housekeeping pattern produces stable scaffolding across sessions. Useful for orientation; resistant to substantive revision. When a structural change is needed (e.g., the §10.4-M10 written-warrant clause (c) operator-surfacing channel cumulative count tracking) it gets added as a new sub-section without removing now-stable old sub-sections. Cumulative housekeeping grows monotonically.

4. **Substrate non-adoption is partially explained by write/read asymmetry.** When write is forced and read is encouraged, agents optimize for write completeness (mechanical) and treat read as best-effort (judgment-call). The substrate is a read-side tool; in a write-forced/read-encouraged regime, read-side tooling is the lowest-priority habit to develop.

5. **The engine accumulates passive maintenance debt.** Each session preserves 50 first-class minorities + 13 OIs + 4 watchpoints + 2 (z5) ledger items + 12 EF records + 11 engine-version entries + 240+ decisions. The maintenance work (re-evaluate activation warrants; check reopen conditions; verify ledger freshness; audit decision relevance) is in-principle distributable across sessions but in-practice deferred because no session is required to substantively engage with the cumulative state. Each close-narrative says "preserved unchanged"; the preservation-claim is unverified.

6. **Operator-audit becomes the load-bearing cross-check.** The S063/S064/S067/S068 operator-audit-catches-what-in-session-discipline-missed pattern is the engine's outermost mechanism for detecting laundering. But operator-audit is per-session opt-in by the operator; it is not reliably triggered; when it triggers, it surfaces concrete concerns the engine missed. Operator-audit functions as designed; but its load suggests the engine's in-session mechanisms are insufficient. The system relies on operator engagement to catch what its own structural mechanisms cannot.

The operator's framing post-S068: "I don't know why the system is so passive with this laundering and maintenance." The passivity is structural — the engine has elaborated write-side discipline (40+ Tier 1 checks; 10 Tier 2 questions; Tier 2.5 reviewer; (z5) ledger; check 26/27/28; engine-version cadence; first-class minority preservation; watchpoint preservation; OI lifecycle) without proportionally elaborating read-side discipline. Read is the activity that consumes accumulated state; without read-side enforcement, accumulated state becomes accumulated ceremony.

## Suggested Change

This record proposes **two coupled architectural directions**, distinct from but interacting with the EF-068-substrate-load-bearing sibling EF (groups i+ii). Where the sibling addresses near-term harness-side enforcement (load MCP by default; require substrate calls; implement (z6) digest), this record addresses architectural rebalance (reduce write rate; promote query-driven read).

**Direction 3 (group iii): Demote default-read surface; promote query-driven read.**

This is the §10.4-M10 Substrate-N2 minority direction (records-as-source-of-truth applied broadly). Currently `records-contract.md` v1 phase-1 only migrated `records/sessions/`. Phase-2 (mirrored-minority migration) and phase-3 (engine-version history; feedback metadata; reference-validation §10) are deferred per WX-58-1 phase-2-gate.

Candidate scope for design-space deliberation:

- **Phase-2: minorities migration** (`records/minorities/M-NNN.md`). Each first-class minority becomes an authoritative record with frontmatter (id, source-session, status, reopen-warrants, vindication-status, etc.); body holds the minority's full text; `workspace-structure.md` v9 §10.4 becomes a thin index pointing to records. Activates §7.4 Substrate-N2 direction for the minority class. Cross-spec mirrors at `validation-approach.md` v7 §10 / `retrieval-contract.md` v1 §7 / `records-contract.md` v1 §7 / `reference-validation.md` v3 §10 collapse to single-source `records/minorities/`.
- **Phase-3: watchpoints + (z5) ledger + (eventually) decisions migration**. WX-NNN watchpoints become `records/watchpoints/WX-NNN.md`; (z5) ledger becomes `records/validation-debt/VD-NNN.md`; eventually decisions become `records/decisions/D-NNN.md`. Each migration eliminates a class of in-line cross-references in close-narratives in favour of substrate queries.
- **Default-read surface shrinks** as authoritative classes migrate to records-substrate. Per-family thin `index.md` is default-read; per-record files are session-scope read-as-needed (per `read-contract.md` v5 §2d applications-directory carve-out pattern + v6 records-directory clarification). Eventually default-read might be ~10-12 files (specs + dispatcher + per-family thin indexes); query-driven read becomes the engine's standard read-discipline mode.

Cost: substantial multi-session arc; high coordination across multiple specs; depends on substrate adoption (sibling EF-068-substrate-load-bearing) succeeding first. This direction should NOT activate before the sibling EF's harness-side enforcement is operational; otherwise records become writable-but-not-readable.

**Direction 4 (group iv): Reduce forced-write rate.**

Specifically the housekeeping-15-sub-section-per-close pattern.

Candidate scope:

- **Move stable-state housekeeping to records-substrate.** A `records/sessions/S<NNN>.md` row already exists per session; extend its frontmatter to include the stable-state fields (validator state at close; aggregate measurement; preservation depth; close-rotation metadata; etc.). The 15-sub-section housekeeping prose is replaced by structured frontmatter; the close-narrative §11 housekeeping decision becomes thin pointer to record.
- **Move per-session-delta-only content to close-narrative.** First-of-record events; substantive operational warrants advanced; substantive watchpoint changes (not stable-streak-increment); decisions with non-`[none]` triggers. The close-narrative becomes shorter and substantively-loaded, not scaffolding-loaded.
- **Trigger-based housekeeping**. Currently every close produces 15-sub-section housekeeping regardless of substantive content. Trigger-based variant: housekeeping fires only when at least one sub-section changes substantively (e.g., engine-version increment fires (c); MAD edit fires (i); first-class minority addition fires (d); reviewer audit fires (m)). Sessions with no substantive sub-section changes emit a thin "no housekeeping changes" close note.
- **Preservation-claim verification cadence**. Currently each close says "50 first-class minorities preserved" without verifying (operationally, the count is verified at close via wc-l on §10.4 block, but the *preservation* is unaudited — are the minorities still apt? Are reopen warrants still load-bearing?). Periodic substantive-engagement obligation — every 10 sessions, for example, one session is required to engage with the minorities + watchpoints + OIs in depth, audit which warrants have been re-fired or aged out, and update preservation status with substantive rationale.

Cost: moderate; mostly spec-side amendments; requires substrate maturity (Direction 3) for the records-shift. Could be partially adopted (trigger-based housekeeping; preservation-claim verification cadence) without full Direction 3 architectural shift.

**Joint-scope rationale (Direction 3 + Direction 4)**:

The two directions are coupled because:

- Direction 3 (records-substrate maturity) makes Direction 4 (reduced forced-write) tractable — once watchpoints + minorities are in records-substrate, the close-narrative can stop replicating their state-prose.
- Direction 4 (reduced forced-write) makes Direction 3 (records-substrate) operationally valuable — once the close stops replicating state, agents must query the records to access state, exercising the substrate.
- Joint adoption produces a virtuous cycle; sequential adoption (without coupling) risks records-as-write-only (D3 without D4) or close-as-stub (D4 without D3).

**Joint-scope cross-linkage with EF-068-substrate-load-bearing**:

The sibling EF (groups i+ii) addresses harness-side enforcement of substrate use. Without that enforcement, this record's directions cannot succeed (records-as-source-of-truth requires query-driven read; query-driven read requires substrate-as-default; substrate-as-default requires harness-side enforcement). **Sequencing**: sibling EF first (S069+); this record second (S069++).

If the S069+ joint-scope MAD adopts a phase-2 plan that activates harness-side enforcement, this record's design-space at S069++ becomes operationally tractable. If sibling EF adopts minimum-viable-only (per S062 §10.4-M16 P2 precedent), this record's directions remain blocked.

## Evidence

- S068 close §1d aggregate measurement: 83,386 words across 22 files default-read; 4 spec soft warnings; engine-feedback INDEX growing.
- S068 close §10 meta-observation 6: cross-linkage joint-scope adoption demonstrates substantive-arc bundling discipline, but bundle implementation is multi-session arc.
- S048+ housekeeping pattern: 40 consecutive `[none]`-trigger housekeeping decisions × 15 sub-sections (per any close-narrative; recent S067 close §11 housekeeping or S068 close §11 housekeeping).
- `workspace-structure.md` v9 §10.4 minority block: 50 first-class minorities accumulated S036→S064 across 5 substantive arcs (S036/S050/S058/S062/S064). Cross-spec mirrors at multiple specs.
- `read-contract.md` v6 §2c close-rotation rule: 6-session retention window + close-rotation as the primary aggregate-budget mechanism; write-side coping not read-side enforcement.
- `validation-approach.md` v7 §Principled Asymmetry articulation: routine claims may remain self-assessed but cross-session-state claims require stateful or distinct review. Articulation present; harness-side enforcement absent.
- `records-contract.md` v1 §6 phase-2 gate: phase-2 (mirrored-minority migration) deferred at S058 per WX-58-1; not subsequently activated despite WX-58-1 closure precondition met at S060.
- §10.4-M10 Substrate-N2 minority (Session 050): structured-artefacts-as-source-of-truth reframe preserved as activation-warrant-pending. Activation warrant: phase-2+ maintenance cost exceeds projection 2× across 3 consecutive sessions; multi-hop cross-reference query class dominates 5× prose-search over 5-session window. Neither warrant has fired empirically (because substrate is not used; non-use prevents data accumulation).
- §10.4-M14 P1 broader-phase-1 minority (Session 058): position that phase-1 should have included §10.4 minority block migration alongside SESSION-LOG.md; rejected at S058 in favour of narrow phase-1. Reopen warrant: §10.4 minority block crosses 1,500 words (currently ~1,800). Warrant fired empirically.

## Application-Scope Disposition

**Self-development workspace** (this workspace). The observation surfaced post-S068 close in operator-surfaced discussion. S068 close is committed and immutable per D-017; this EF record is the formal capture for S069+ scope.

**Sequencing relative to sibling EF-068-substrate-load-bearing-and-harness-telemetry**:

This record's directions are blocked-on the sibling EF's harness-side enforcement adoption. Recommended sequencing:

- **S069+ Path-AS Shape-1** (per S068 D-251 pre-ratification): primary scope is EF-067 + EF-059 + sibling EF-068-substrate-load-bearing. Three-record bundle.
- **S069++ Path-AS Shape-1** (this record's scope; deferred until sibling EF's harness-side enforcement is operational): primary scope is EF-068-read-write-rebalance (this record). Two-direction architectural arc.
- **S069+++ Path-AS-MAD-execution** (this record's phase-2): MAD on architectural rebalance per phase-1 design-space.
- **S069++++ implementation arc**: multi-session phase-3.

Alternative sequencing: bundle this record with sibling EF in single S069+ four-record design-space. Cost: design-space scope increases significantly (4 records × 4+ directions each); MAD lineup may need more than 4 perspectives. Tradeoff: the records are conceptually coupled (read-discipline asymmetry is the meta-frame; sibling addresses near-term enforcement; this addresses architectural rebalance) so bundling may be appropriate. Phase-1 design-space at S069+ could include explicit "bundle-vs-defer" question for MAD deliberation.

**Operator-audit cadence note**: this EF surfaced via operator-discretionary post-close audit per `validation-approach.md` v7 §Bootstrap-Paradox Layered Handling Layer 6.2. **Co-fourth-of-record operator-audit-catches-what-in-session-discipline-missed event** at S068 post-close (paired with sibling EF). The operator's explicit framing — "I don't know why the system is so passive with this laundering and maintenance" — names the structural pattern that this record articulates. The pattern reified at n=4 across S063/S064 + S067/S068×2 (sibling + this) suggests operator-audit is consistently catching engine-internal-mechanism-failure-modes. This itself is evidence that the engine's in-session mechanisms are bounded by their write-side-bias; the architectural rebalance proposed here is the structural response to that pattern.

Operator: please confirm sequencing preference (S069+ three-record vs S069+ four-record bundle) at S069 session-open. Default per S068 D-251 + this record's recommendation: three-record at S069+; four-record if operator surfaces preference for bundled scope.
