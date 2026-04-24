---
session: 048
title: Decisions — S048 Path T (Triage-classify) inbox engine-feedback; EF-001 operator-directed resolution adopted substantive read-contract.md v4→v5 (§1 applications clarification + §2d per-file-budget carve-out + chunked-read-on-demand + optional index) + minor prompts/application.md §Read clarification; engine-v7 → engine-v8 first-ever inbox-record-driven bump (new bump-provenance class); four triage records produced (EF-001 resolved; EF-047-retrieval-discipline + EF-047-brief-slot-template + EF-047-session-inputs all triaged with S049 MAD adoption-scheduling); §10.4-M5 activation-pending resolves on arc-produced-feedback criterion; forward observations WX-34-1 SESSION-LOG word count re-emergence + inbox-to-triage first-exercise clean + D-138 folder-name default third exercise clean + §5.4 cadence minority no re-escalation per precedent chain
date: 2026-04-24
status: complete
---

# Decisions — Session 048

## D-152: Path T (Triage-classify) ratified; operator ratified defaults on Halt 1 Q1 + Q2 + Q3 + Q4 + Q5

**Triggers met:** [none]

**Triggers rationale:** Path ratification is an administrative decision selecting among already-considered paths in the session's 00-assessment. No specification is edited by this decision; no OI state transitions; no new triggers fire. Q5 "no other agenda" means no additional work is introduced beyond the proposed Path T scope. This decision unblocks D-153 / D-154 / D-155 / D-156; those decisions carry their own triggers where applicable.

**Single-agent reason:** Default-agent session; operator has ratified directly ("Q1-Q4: Recommendations all OK. Q5: no other agenda"). No deliberation available or appropriate for the administrative ratification itself.

**Decision:**

1. **Path T (Triage-classify) adopted.** The session executes triage-classification of all 4 inbox engine-feedback records with adoption paths staged per operator ratification on Q2/Q3/Q4.

2. **Q1 ratified yes.** Proceed with Path T.

3. **Q2 ratified (a).** Execute EF-001 adoption this session as single-orchestrator per the operator_directed_resolution frontmatter field declaring not-for-deliberation on the source inbox record. Substantive `read-contract.md` v4→v5 + minor `prompts/application.md` §Read clarification + engine-v7→v8 bump. D-153 executes the substantive adoption; D-154 records the engine-v bump.

4. **Q3 ratified (i).** EF-047-retrieval-discipline-and-text-system-scaling-ceiling scheduled as S049 dedicated 4-perspective two-family MAD (per S044 R2 standing preference). Level (A) substantive kernel §1 amendment is minimum-expected adoption scope. Level (B) and (C) MAD scope is an S049 deliberation question.

5. **Q4 ratified (b).** EF-047-brief-slot-template-hidden-arc-leakage + EF-047-session-input-files-redundant-with-verbatim-capture bundled-minor with S049 MAD (alongside retrieval-discipline substantive). Both remain candidates at S049 for specific adoption shape.

6. **Q5 no other agenda.** No scope extension beyond the proposed Path T work.

Operator ratification quoted verbatim: "Q1-Q4: Recommendations all OK. Q5: no other agenda".

---

## D-153: Adopt EF-001 operator-directed resolution via substantive `read-contract.md` v4 → v5 (§1 applications-directory clarification + §2d new carve-out section) + minor `prompts/application.md` §Read clarification

**Triggers met:** [d016_2]

**Triggers rationale:** `d016_2` fires because this decision substantively revises an engine-definition specification (`read-contract.md` v4 → v5; new §2d section; revised §1 clarification paragraph; §10 versioning update). Per MAD v4 §When Multi-Agent Deliberation Is Required, substantive engine-definition revisions normally require multi-agent deliberation. This decision is executed single-orchestrator per the operator_directed_resolution frontmatter on EF-001 declaring the resolution direction as not-for-deliberation; see Single-agent reason below. `prompts/application.md` §Read is minor-documentary (brings prompt's Read enumeration into alignment with `read-contract.md` §1 closure + codifies session-scope-read-as-needed language; no new normative rule beyond what §2d introduces). No `d023_*` trigger fires: kernel is unchanged (no d023_1); MAD v4 is unchanged (no d023_2); validation-approach v5 is unchanged (no d023_3); OI-004 state unchanged (no d023_4).

**Single-agent reason:** Operator-directed resolution recorded on the source inbox record EF-001 as `operator_directed_resolution` frontmatter field declaring "not open to deliberation" (pre-declared direction for all four resolution items: (1) exclude applications/ from §2 per-file budget; (2) §2b aggregate budget continues; (3) chunked-read-on-demand via Read-tool offset/limit; (4) optional manifest/index pattern). Deliberation is structurally excluded by operator direction. Adopting session implements the pre-ratified direction as single-orchestrator work rather than re-deliberating. Operator ratified this adoption path at S048 Halt 1 Q2=(a). This pattern is the first-ever exercise of a new bump-provenance class (operator-directed inbox-record resolution; see D-154 for engine-v-bump classification).

**Decision:**

1. **`specifications/read-contract.md` v4 → v5 (substantive).** Changes applied:

   - **Frontmatter**: `version: 4 → 5`; `last-updated: 2026-04-24`; `updated-by-session: 048`; `supersedes: read-contract-v4.md`.

   - **§1 header update**: "The default-read surface enumeration at engine-v4 (of this spec; engine-v7 of the manifest)" → "engine-v5 (of this spec; engine-v8 of the manifest)".

   - **§1 new closing paragraph** immediately after the "enumeration is closed" sentence: "Applications directory clarification (added v5, Session 048). The `applications/NNN-<slug>/` directory and its contents are NOT part of the §1 default-read enumeration. Files in `applications/` are read at **session scope** — as-needed during session work — rather than at session-open-in-full. This applies in both self-development and external-problem workspaces. See §2d for the consequent per-file budget carve-out and the chunked-read-on-demand mechanism."

   - **§2d new section** "Applications-directory carve-out (added v5, Session 048 per D-153)": codifies the operator-directed resolution's four items:
     - The carve-out: `applications/NNN-<slug>/` files not subject to §2 per-file budget; not counted in §2b aggregate (because outside §1 closed enumeration).
     - Rationale: §2 values calibrated against methodology-content files; domain artefacts have different size profiles; applying default-read budget forces compression / splitting / archive-pack misuse.
     - Session-scope read-as-needed mechanism: small artefacts full-read; larger via Read tool `offset`/`limit`; no new archive-pack machinery.
     - Optional `applications/NNN-<slug>/index.md` navigation pointer: thin (target under 1,000 words); not mandatory; recommended for large-artefact applications.
     - What the carve-out does NOT change: §1 closure preserved; §2 budget applies to §1 files; §2b aggregate scope unchanged; §2c close-rotation unchanged; §3 archive-surface discipline unchanged; §4–§9 archive-pack discipline unchanged.
     - Context-window pressure from applications/ reads is session-scope concern distinct from default-read growth discipline.
     - Interaction with `prompts/application.md` §Read: v8 clarification removes the "and `applications/`" pre-v8 inclusion per documentary alignment.

   - **§10 Versioning**: new v5 entry added after v4 entry.

2. **`specifications/read-contract-v4.md` preserved as superseded witness.** `cp` of v4 active file; frontmatter `status: active → status: superseded`; `superseded-by: read-contract.md` + `superseded-in-session: 048` added.

3. **`prompts/application.md` §Read (minor documentary clarification per OI-002).** Changes applied:

   - **Workspace-reading bullet** rewritten to enumerate `read-contract.md` §1 items explicitly (MODE.md; active-status specs; PROMPT.md + prompts; SESSION-LOG.md; open-issues/index.md; prior 03-close.md subject to §2c close-rotation; currently-active session provenance; conditionally engine-feedback/INDEX.md in self-development mode). **Removes the pre-v8 "and `applications/`" inclusion** that was the source of S047 P3 Outsider latent spec-contradiction finding.

   - **Domain-reading bullet** restructured to "Domain reading — `applications/` scope" heading; references `read-contract.md` v5 §2d; names **chunked-read-on-demand** via Read tool `offset`/`limit`; names optional `applications/NNN-<slug>/index.md` navigation pointer; states `applications/` files not bound by §2 per-file budget and not contributing to §2b aggregate.

   - No change to Engine-reading bullet; no change to Convene/Deliberate/Validate/Produce/Record and Close sections; no change to §Engine-feedback pathway or §Anti-silent-import and anti-laundering or §Now begin.

   No prior version of `prompts/application.md` preserved as a separate file per Session 017 / engine-v7 `PROMPT.md`-rewrite precedent (prompts are prompt text with history in git rather than versioned-via-suffix documents).

4. **`tools/validate.sh` unchanged.** Check 20 (default-read per-file budget) is not affected by this revision at constants level because `applications/` files were already not in the default-read aggregate counted by check 20 (§1 was already closed pre-v5); the §2d carve-out makes the pre-existing behaviour explicit and extends it by documentation without adding any new enforcement mechanism. Check 22 (archive-pack citation consistency) unchanged. Check 23 (MODE.md presence) unchanged. No new validator check required.

5. **S047 D-150 deferred spec-amendment candidate (iv) subsumed by direction.** The S047 P3 Outsider's unique finding (`read-contract.md` §1 closed enumeration omits `applications/` while `prompts/application.md` §Read treats `applications/` as a read input) is resolved by this adoption: §1 remains closed; `applications/` is explicitly outside §1 by the new clarifying paragraph; `prompts/application.md` §Read is re-aligned to §1 closure by the minor documentary amendment. No remaining (iv)-scope work required at S049 or post-arc self-dev review.

**Rationale for operator-directed-resolution class validity.** The operator-directed-resolution pattern is compatible with the engine's preservation-and-dissent-recording machinery: the feedback record itself is the preservation artefact; the `operator_directed_resolution` frontmatter field makes the non-deliberation explicit; the adopting session documents the adoption as a single-orchestrator implementation of a pre-ratified direction rather than as a deliberation. The pattern does not bypass deliberation when deliberation is warranted; it recognises that some operator interventions (narrow scope; directionally clear; single possible resolution shape) are appropriately handled as single-orchestrator implementations. First-ever exercise of the pattern at this adoption. Forward-convention candidate: `specifications/workspace-structure.md` v5 §engine-feedback may benefit from a minor documentary codification of the `operator_directed_resolution` field; deferred to a future session (not bundled with S049 MAD because its scope is §engine-feedback documentation rather than the retrieval-discipline methodology territory of the S049 scope).

---

## D-154: Engine-v7 → engine-v8 (documentary; reflects D-153 substantive revision to `read-contract.md`)

**Triggers met:** [none]

**Triggers rationale:** `engine-manifest.md` edits for engine-v-bump are classified as documentary per Session 021 / 023 / 028 / 033 / 036 engine-v-bump sub-pattern ("documentary update per Session 021 sub-pattern" is cited in the existing engine-manifest §7 text for v2/v3/v4/v5/v6/v7 entries). The edits are: frontmatter `last-updated` + `updated-by-session`; §2 current version name v7 → v8; §3 heading v7 → v8; §7 new v8 entry describing the v7→v8 bump's substantive content. The manifest's own frontmatter `version: 1` is unchanged (no manifest-spec-version bump). No new engine-definition file is added. No engine-definition file is removed or superseded at engine-v8 boundary. D-153 is the decision that carries the d016_2 trigger for the substantive read-contract.md revision; D-154 is consequential documentation of D-153's engine-level impact.

**Single-agent reason:** Documentary decision consequential to D-153; no deliberation available or appropriate for the version-name update itself. Session 021 D-082 established the precedent for documentary engine-v-bump decisions at engine-v-establishment sessions.

**Decision:**

1. **Current engine version**: `engine-v7` → `engine-v8`. `specifications/engine-manifest.md` §2 updated. "Established Session 036 per D-114" → "Established Session 048 per D-154".

2. **§3 heading**: "Engine-definition files at `engine-v7`" → "Engine-definition files at `engine-v8`". Underlying file table unchanged (no file added/removed; `read-contract.md` continues to point at the active file which is now v5).

3. **§7 Engine version history** extended with new `engine-v8` bullet entry detailing:
   - The bump as the **first-ever driven by operator-directed resolution of an inbox engine-feedback record** (new bump-provenance class distinct from preserved-minority activation / §9 trigger firing / watchpoint firing / operator-surfaced mid-session deliberation).
   - Substantive file: `specifications/read-contract.md` v4 → v5 (new §2d; §1 clarification; §10 versioning); v4 preserved as `read-contract-v4.md` status superseded.
   - Minor file: `prompts/application.md` §Read (documentary alignment).
   - All other engine-definition files unchanged at boundary: `PROMPT.md`; `prompts/development.md`; `methodology-kernel.md` v6; `multi-agent-deliberation.md` v4; `validation-approach.md` v5; `workspace-structure.md` v5; `identity.md` v2; `reference-validation.md` v3; `engine-manifest.md` (this documentary update).
   - `tools/validate.sh` unchanged (no new enforcement mechanism required).
   - S047 D-150 candidate (iv) subsumed by direction.
   - Engine-v8 is the seventh engine-v-bump overall; the fourth post-cadence-maturation content-driven bump.
   - §5.4 Session 022 engine-v-cadence minority does NOT re-escalate at this bump (preservation window 11 preceded; content-driven; precedent chain Session 028 D-096 / Session 033 D-107 / Session 036 D-114 holds). OI-018 unchanged.
   - Aggregate default-read surface effectively unchanged (carve-out clarifies pre-existing exclusion; §1 count unchanged). `read-contract.md` grows ~4,762 → ~5,624 words (under §2 6K soft warning). Close-rotation continues standard per §2c; Session 042 close rotates OUT at Session 048 close.

4. **Frontmatter update**: `last-updated: 2026-04-24`; `updated-by-session: 048`.

---

## D-155: Triage + adoption-scheduling for three remaining inbox records (EF-047-retrieval-discipline S049 dedicated MAD substantive; EF-047-brief-slot-template + EF-047-session-inputs bundled-minor with S049 MAD)

**Triggers met:** [none]

**Triggers rationale:** This decision records triage classification + adoption scheduling for three inbox records; it does not execute any specification amendment this session. No engine-definition file is edited by this decision; no OI state transitions (OI-019 is cross-referenced but not closed; no new OI opened); no engine-v bump. Triage classification is a structural recording activity per `workspace-structure.md` v5 §engine-feedback, not a deliberative decision. Adoption of the scheduled S049 substantive amendments will carry its own `d016_*` triggers at S049 close when executed.

**Single-agent reason:** Structural recording of classification + disposition + adoption scheduling; operator has ratified the scheduling at S048 Halt 1 Q3=(i) and Q4=(b). Deliberation on the scheduled amendments is the S049 MAD's scope by design; pre-MAD single-orchestrator triage is appropriate here.

**Decision:**

1. **EF-047-retrieval-discipline-and-text-system-scaling-ceiling** → `engine-feedback/triage/EF-047-retrieval-discipline-and-text-system-scaling-ceiling.md`. Status: triaged. Adoption scheduled: S049 dedicated 4-perspective two-family MAD (per S044 R2 standing preference). Scope: level (A) substantive kernel §1 amendment minimum-expected; level (B) cross-spec sync via `syncs_with:` field MAD-deliberated; level (C) structured retrieval substrate direction-of-travel decision MAD-deliberated. Expected engine-v impact: engine-v8 → engine-v9 candidate at S049 close conditional on adoption. Cross-references: OI-019 sub-question (f) extended-baseline visibility mechanism.

2. **EF-047-brief-slot-template-hidden-arc-leakage** → `engine-feedback/triage/EF-047-brief-slot-template-hidden-arc-leakage.md`. Status: triaged. Adoption scheduled: bundled-minor with S049 MAD. Both source-record options ((a) bootstrap `--hidden-arc` flag + `prompts/application.md` paragraph; (b) `workspace-structure.md` v5 §applications documentary clarification) remain candidates at S049. Selection between (a)/(b)/both is an S049 deliberation question.

3. **EF-047-session-input-files-redundant-with-verbatim-capture** → `engine-feedback/triage/EF-047-session-input-files-redundant-with-verbatim-capture.md`. Status: triaged. Practice-level already adopted (operator workflow for `selvedge-disaster-response` arc dropped the `session-inputs/` subdirectory; verbatim capture at 00-assessment.md §2). Spec-level minor documentary amendment scheduled: bundled-minor with S049 MAD.

4. **EF-001 resolved via D-153** as the fourth inbox record; triage record at `engine-feedback/triage/EF-001-read-contract-budget-scaling-for-domain-artefacts.md` records the disposition.

5. **`engine-feedback/INDEX.md` updated** to reflect the full inbox→triage lifecycle transitions: New count 4 → 0; Triaged count 0 → 3; Resolved count 0 → 1; Rejected 0. Records table amended with triage session (048) + OI/Disposition columns.

6. **Inbox-intake files preserved verbatim per §engine-feedback lifecycle convention.** `status: inbox` frontmatter on intake records is not modified; current lifecycle state is carried by the triage record's `status:` field and the INDEX.md Status column.

---

## D-156: Housekeeping — observational windows and watchpoints at S048 close

**Triggers met:** [none]

**Triggers rationale:** Housekeeping records forward observations and watchpoint evaluations; no specification edit; no OI state transitions beyond recording; no engine-v bump implication. Ordinary close-step discipline.

**Single-agent reason:** Observational and evaluative work; not an axis on which deliberation is warranted.

**Decision (observational record):**

1. **§10.4-M5 activation-pending RESOLVES at S048.** S046 D-146 disposition on §10.4-M5 was "Reviser OI-tag-only feedback pathway activation-pending on selvedge-disaster-response arc outcome". Arc execution has produced inbox records (EF-001 is operator-relayed from `selvedge-disaster-response` Session 001 Case Steward statement; source_session=001 per frontmatter). The activation-pending condition is therefore satisfied: the feedback pathway has produced a feedback record originating from arc execution. §10.4-M5 transitions from activation-pending to **discharged-as-vindicated** (the Reviser's concern that OI-tag-only pathway would underperform is not vindicated — the first arc-produced feedback was received through the spec'd mechanism without operational friction at the feedback-pathway layer; the friction surfaced in EF-001 is content-about-read-contract-scope, not about the feedback-pathway mechanism itself). Window concludes.

2. **§10.4-M2 continues preservation.** M2 (Skeptic-preserver premature-feedback-pathway) activation-warrant language (per workspace-structure.md v5 §10.4-M2) does not fire at S048: the inbox is operationally exercised for the first time at S048 with clean execution (no structural retrofit required to the §engine-feedback spec; the triage-file schema `feedback_ref:` frontmatter + status progression worked as designed on first use). Continued preservation against future-event horizon.

3. **§10.4-M1/M4/M6** all continuing preservation. No firing event at S048.

4. **§5.4 Session 022 engine-v-cadence minority does NOT re-escalate at engine-v7→v8 bump.** Precedent chain holds: Session 028 D-096 / Session 033 D-107 / Session 036 D-114 all established "content-driven-bump does not re-escalate cadence minority"; Session 048 D-154 is the fourth post-cadence-maturation content-driven bump and follows an 11-session preservation window. §5.4 preservation status unchanged (activated-not-escalated since S023). OI-018 unchanged.

5. **§5.6 GPT-family-concentration minority** — no deliberation at S048 (single-orchestrator path per D-152). S048 does not produce a new data point for §5.6 (reopen warrant (ii) literal discharge was at S043; spirit-level sustained-exercise re-examination happens at next MAD session which is S049).

6. **WX-28-1 close-rotation-exception-frequency watchpoint**: S048 records **twentieth close-rotation zero retention-exceptions** (eighteenth consecutive S029-S048 all zero). Watchpoint continues vindicated (tracked at 18-of-18 cumulative per S046 + now 20-of-20 including S047 + S048). Window concluded at S038 10-of-10; pattern continues sustained beyond window close.

7. **WX-34-1 standing discipline** applied: SESSION-LOG.md at session open was 6,755 words exceeding the 6K soft warning. This is re-emergence of the post-S027 accretion pattern that S040 D-123 preemptively-restructured. The S040 compression was ~8K → ~2.4K; growth from S040 (close) to S048 (open) is ~4.3K across 7 sessions (S041–S047 rows), averaging ~600 words per row — consistent with the verbose substantive-row pattern. **Forward observation**: WX-34-1 pressure is returning; another preemptive restructure may be warranted within the next 2-3 sessions if the soft warning persists. S049 substantive MAD work may accelerate the pressure; S050 or S051 is a candidate preemptive-restructure session. Not adopted now to avoid double-burdening S048 with both substantive spec adoption and restructure work.

8. **WX-24-1 MAD stable 6,637** — no MAD revision this session; streak extends to **twenty-first-session no-growth** (post-S042 reset; S043/S044/S045/S046/S047/S048 all no-growth). New record.

9. **D-129 standing discipline** applied at 00-assessment.md §5b: five considered-and-rejected non-Path-T alternatives surfaced with non-vacuous rationales (Path A-pure; Path T-full; Path T-minimal; Path OC N/A; Path OS with MAD). Standing discipline exercised cleanly.

10. **D-133 M2 Convene-time role/lineage matrix** — does NOT fire this session (single-orchestrator). Second-of-3 verification carry from S047 continues pending to next self-dev MAD session (S049).

11. **Folder-name D-138 third exercise**: `048-session` (no suffix, no slug) continues the S046/S047/S048 pattern. Three consecutive default-agent / build / triage / infrastructure sessions using the clean default. No operational friction observed across three classes. Fourth data point from S049 MAD will test the default against a content-MAD session class.

12. **Inbox→triage lifecycle first operational exercise clean.** All four records transitioned from `status: new` (intake) to `status: resolved` (EF-001) or `status: triaged` (three others). Triage-file schema worked as designed (`feedback_ref:` frontmatter; `triaged_in_session:` + `disposition:` + `opened_issue:` + `engine_version_impact:` fields). No structural adjustment to `workspace-structure.md` v5 §engine-feedback required. First-ever operator-directed-resolution frontmatter field exercise also clean; forward-convention candidate for §engine-feedback documentary amendment noted but not bundled.

13. **WX-43-1 subagent self-commit OI-promotion evaluation** — no subagents this session (single-orchestrator); cumulative count unchanged at 6-of-8 from S045; carries forward to S049 MAD session.

14. **WX-44-1 independence-phase-breach** — no subagents this session; counter stable at n=3 from S047; carries forward.

15. **WX-44-2 codex CLI model-version-drift discipline** — no codex invocation this session; not exercised.

16. **Seventeenth close-rotation**: Session 042 close rotates OUT at S048 close; Session 048 close enters. Default-read close window post-rotation: S043/S044/S045/S046/S047/S048 (six files). Aggregate impact: S042 close rotates out (substantive row but close-file word count should be ~1K-2K by S042 being Path A; net aggregate reduction minimal).

17. **OI-004 state unchanged (Closed).** d023_4 does not fire. No tally movement this session.

18. **Aggregate default-read surface at close** — will be measured post-commit; read-contract.md growth 4,762 → 5,624 words is the largest single-file delta; manifest.md growth ~150 words from §7 v8 entry. Total default-read aggregate change estimated +1K words. Close-rotation removes S042 close (estimated ~1K-2K words). Net approximately 0 to slightly positive delta; well under §2b soft 90K.
