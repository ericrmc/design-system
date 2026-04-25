---
feedback_ref: engine-feedback/inbox/EF-055-substrate-aware-format-and-archive-rethink-substantive-arc.md
triage_session: 056
status: resolved
classification: substantive
opened_issue: none
resolved_by: provenance/058-session/
---

# Triage — EF-055-substrate-aware-format-and-archive-rethink-substantive-arc

## Triage decision

**Classified substantive-arc; scheduled for dedicated MAD session(s); not resolved at S056.**

Per S056 D-192 (single-orchestrator Path T classification), EF-055 is classified **substantive-arc** in shape — closer to **EF-047-retrieval-discipline-and-text-system-scaling-ceiling** (which produced S049 design-space synthesis → S050 4-perspective two-family MAD → engine-v9 + new engine-definition spec adoption) than to **EF-051 / EF-053 / EF-054** (each resolved as defect-fix-shaped minor implementation within one or two sessions per S052 / S054 Path T+L precedent).

The triage decision does NOT pre-commit Direction A / B / C choice; the dedicated session(s) deliberate. Operator's stated preference at intake (Direction A — substantive Substrate-N2 reframe arc activating §10.4-M10) is durable input that the deliberation will treat as one position to consider, not as foreclosure. Directions B (tactical thin-index extension to SESSION-LOG.md alone via Path L+A) and C (defer until §10.4-M10 activation warrants empirically fire) preserved per the inbox-record-disposition convention (S051 / S053 / S054 precedent).

## Scope and arc shape (planned; for the dedicated session(s) to ratify)

The intake's §Suggested Change names a two-to-four-session arc estimate. Concrete planned shape:

- **Phase 1 — synthesis / design-space session** (Path AS-style per S049 D-157 precedent). Surveys reframe candidates including the §10.4-M10 Substrate-N2 frame, alternative architectures, and the cost/benefit profile across the named target files (`SESSION-LOG.md` / `engine-manifest.md` §7 / `workspace-structure.md` §10.4 / `reference-validation.md` §10 / `retrieval-contract.md` §7 / `engine-feedback/INDEX.md` / `aliases.yaml`). Re-reads S050 raw perspectives (P1 Substrate Architect / P2 Incrementalist Skeptic / P3 Outsider Frame-Completion / P4 Cross-Family Reviewer) per intake §Evidence pointer list. Produces `provenance/NNN-session/design-space.md` artefact per S049 D-158 precedent. Engine-v preserved (synthesis-only is non-bumping per S049 precedent).
- **Phase 2 — MAD session** (Path AS-style 4-perspective two-family per S050 lineup precedent). Likely 2 Claude + 2 Codex/GPT-5.5 per D-133 M2 lineage-constraint matrix. Perspective composition candidates: Substrate Architect / Incrementalist Skeptic / Outsider non-Claude / Cross-Family Reviewer non-Claude. Precise composition is the MAD-session's own first ratification step (per S050 precedent, perspective lineup is decided at the MAD session not the scheduling session). Adopts a direction (A / B / C / synthesis variant); engine-v10 candidate if Direction A or substantial variant adopted; minor if Direction B alone; no engine-v change if Direction C alone.
- **Phase 3 — adoption** (Path AS-style or single-orchestrator depending on phase-2 direction). Substantive spec edits (`read-contract.md` / `workspace-structure.md` / accretive-spec-blocks per direction adopted) + engine-v10 candidate + archive-pack preservation of pre-restructure state per S022 R8a / S040 D-123 / S051 D-178 precedent chain.

Possible compression: phase-1 + phase-2 collapse to a single MAD session if synthesis is judged adequate within MAD scope. Possible expansion: phase-3 may itself be multi-session if direction adopted requires staged migration. Two-to-four-session estimate per intake stands as bracketing.

## Direction-specific scheduling notes

- **Direction A adoption**: engine-v10 candidate. Multi-session arc as scheduled above. Triggers `read-contract.md` v5 → v6 (or higher) substantive revision; `workspace-structure.md` v6 → v7 substantive revision; `engine-manifest.md` §7 entry for engine-v10 (which itself is a substantive accretive entry — meta-question for the deliberation: does the reframe target `engine-manifest.md` §7's own format?). The arc would necessarily revisit `read-contract.md` §1 closed enumeration, §2 per-file budget calibration, §2c retention-window value (substrate makes "older closes" still queryable), and §4 archive-pack structure (may simplify if structured-records replace prose blocks).
- **Direction B adoption alone**: minor per OI-002 per S022 R8a / S040 D-123 / S051 D-178 precedent chain. Single-session Path L+A execution. SESSION-LOG.md compressed to thin pointer-only rows; pre-restructure preserved as archive-pack at `provenance/NNN-session/archive/pre-L-SESSION-LOG/`. Buys ≥30 sessions of SESSION-LOG headroom under new asymptote. Does not address `engine-manifest.md` §7 / `workspace-structure.md` §10.4 / `reference-validation.md` §10 / `retrieval-contract.md` §7 accretive blocks. Compatible with Direction A as a subset (Direction A subsumes Direction B's SESSION-LOG-only restructure).
- **Direction C adoption alone**: no spec edit; preserve existing structure; allow §10.4-M10 to activate per its written warrants ((a) cumulative phase-2+ maintenance time exceeds projection 2× across 3 consecutive sessions; (b) multi-hop cross-reference query class dominates ≥5× prose-search over a 5-session window). Restrict near-term action to periodic SESSION-LOG restructure per S057–S060 candidate window per S055 D-190g forecast. Engine-v9 preserved. Honours §10.4-M10 minority's preservation rationale.

## Forward-dependency observations

- **Phase-2 substrate WX-50-1 gate** (`retrieval-contract.md` v1 §6) is currently paused per S053 close §6 disposition. EF-055 may interact with the gate's status by surfacing query-class data (multi-hop, structured-filter) that activates §10.4-M10 / §10.4-M8 from a different angle. The dedicated MAD session(s) should consider whether the EF-055 deliberation itself constitutes a Condition-2 firing event (operator-surfacing channel for §10.4-M10 activation, distinct from the §6 gate's count-based mechanisms).
- **§10.4-M10 / §7.4 mirrored-minorities**: the intake explicitly proposes §10.4-M10 as the activation target. Per the minority's source `provenance/050-session/01c-perspective-outsider-frame-completion.md` §2 Substrate-N2, the activation channel adds to the existing (a) maintenance-cost-2× and (b) multi-hop-dominance-5× warrants; this triage records **operator-surfacing as a third de-facto activation channel** for §10.4-M10, precedent established at S036 / S043 / S044 / S045 / S047 Path PD/OS/OC sub-class lineage but applied here to a preserved-minority activation rather than to a fresh deliberation surface.
- **`engine-feedback/INDEX.md` is itself a target file** of the EF-055 reframe per its frontmatter `target_files`. The dedicated MAD must consider whether `engine-feedback/INDEX.md` (currently 7 lifecycle records, will be 8 at S056 close after this triage) follows the open-issues-style thin-index pattern adequately or needs further tightening.
- **`specifications/aliases.yaml` is named in `target_files`** but the intake's §Suggested Change body says "already structured/bounded; no change." This is an inconsistency in the intake (target_files lists it; suggested change exempts it). The dedicated MAD should disambiguate.
- **EF-047-brief-slot-template still triaged-deferred** at S056 open per S050 D-174 / S048 D-155 chain (deferred to next self-dev or external-arc session exercising arc-plan brief slots; earliest selvedge-disaster-response S002+). EF-055 substantive arc and EF-047-brief-slot-template are independent scopes; no scheduling collision.
- **S047 D-150 three deferred candidates (i)/(ii)/(iii)** preserved for post-arc self-dev review. Direction A scope of EF-055 may overlap with candidate (iv) (read-contract.md §1 vs prompts/application.md §Read ambiguity — already subsumed by EF-001 resolution at S048 D-153) and possibly with (i) kernel §7 qualitative-multi-agent label question. The dedicated MAD should consider candidate (i)/(ii)/(iii) cross-linkage as a sub-question.

## Cross-references

- **Inbox record**: `engine-feedback/inbox/EF-055-substrate-aware-format-and-archive-rethink-substantive-arc.md` (preserved verbatim per workspace-structure §engine-feedback "intake files preserved verbatim" convention).
- **Decision authorising this triage**: `provenance/056-session/02-decisions.md` D-191 + D-192.
- **Activation-target minority**: `specifications/workspace-structure.md` v6 §10.4-M10 / mirrored at `specifications/retrieval-contract.md` v1 §7.4.
- **Pattern-arc precedent (substantive arc class)**: EF-047-retrieval-discipline → S049 design-space (D-157/D-158/D-159) → S050 4-perspective MAD (D-163 through D-176) → engine-v9 + retrieval-contract.md v1 + workspace-structure.md v5→v6 + tools/build_retrieval_index.py + tools/retrieval_server.py + .mcp.json + specifications/aliases.yaml.
- **Pattern-arc precedent (operator-surfacing for minority activation)**: S036 PD / S043 PSD / S044 OC / S045 OS minority-activation pathway (D-138 first minority activation via operator-observation pathway; precedent for §10.4-M10 activation via operator-surfacing).
- **Routine-restructure precedent (Direction B baseline)**: S022 R8a / S040 D-123 / S051 D-178 SESSION-LOG.md thin-index restoration.

## Disposition

- **Status**: resolved (updated S058 D-199 through D-205).
- **Resolution**: at S058 via Substrate-N3.5 pilot toward Direction A — phase-1 = SESSION-LOG.md only as proving slice migrated to records/sessions/. New engine-definition spec records-contract.md v1 + workspace-structure.md v6→v7 + read-contract.md v5→v6 + engine-manifest.md engine-v10 entry + tools/validate.sh check 25 + tools/build_retrieval_index.py record-aware indexing. Engine-v9→v10 (second-instance MAD-adopted-new-engine-definition-spec class). Four new minorities §10.4-M12 through §10.4-M15 preserved (count 36→40). §10.4-M10 written-warrant amendment formalised (clause c operator-surfacing channel). Phase-2 (mirrored-minority migration) gated on phase-2-gate conditions per records-contract.md v1 §6.
- **No OI opened**: substantive resolution achieved within the engine-feedback lifecycle; deliberation produced four first-class minorities + one warrant amendment as preservation discipline.
- **Forward-tracker**: this triage record is the canonical scheduling artefact for the substantive-arc resolution. Phase-2 (S059) and phase-3 (S060+) sessions should reference S058 close §7 forward observations + records-contract.md v1 §6 phase-2 gate.
