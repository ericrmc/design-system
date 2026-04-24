---
session: 049
title: Decisions — S049 operator-directed scope revision from substantive-adoption to synthesis-and-options meta-decision; design-space document produced at provenance/049-session/design-space.md covering five operator-named retrieval-substrate candidates (SQLite FTS5 / BM25 / inverted index / alias tables / MCP-exposed index) + six rejected alternatives with rationale (Meilisearch-Typesense / Tantivy / RDF / vector-embedding / Neo4j-Memgraph / rank_bm25-whoosh); Option A SQLite FTS5 + structured tables + MCP recommended; Option B DuckDB + FTS + edges table positioned as strongest competitor; S050 MAD pre-ratified as 4-perspective two-family (2 Claude Substrate Architect + Incrementalist Skeptic; 2 Codex/GPT-5.5 Outsider + Cross-Family Reviewer) with 8-question agenda; three triaged EF-047 records defer to S050; engine-v8 preserved at S049 (preservation window count 1); D-133 M2 third-of-3 verification window carries to S050; §5.6 GPT-family-concentration continuing worst-case-side; WX-43-1 OI-promotion evaluation carries forward; SESSION-LOG Q5=(a) thin-row discipline selected
date: 2026-04-24
status: complete
---

# Decisions — Session 049

## D-157: S049 scope revised from substantive-adoption to synthesis + options + meta-decision per operator Halt 1 direct guidance

**Triggers met:** [none]

**Triggers rationale:** No specification edited this session; no OI state transition; no engine-definition file modified; no decision producing substantive workspace state change. Session is a meta-decision session that produces input for S050 deliberation. The `d016_*` triggers would fire for the eventual substrate-adoption decision at S050, not for the meta-decision here about what S050 will deliberate. The `d023_*` triggers similarly defer to S050.

**Single-agent reason:** Operator direct ratification at S049 Halt 1. Operator response on 2026-04-24: "Yes proceed with default answers. For the discussion on retrieval, recommendations should include data structure changes rather than 'discipline' only. Use real scalable technical solutions here rather than being constrained by 'watching' growth or summarising or archiving. The system already has many decision IDs, watch points, open issues, sections and subsections of specifications. It demands real engineering rigour. Try using an inverted index with lexical/BM25 search; consider identifier normalization with an alias table; consider structured frontmatter with metadata filters; consider a simple key–value lookup for direct ID resolution; consider regex matching for exact patterns; and consider maintaining a local FTS5 index over full files (content plus metadata), exposed via MCP as a fast lookup layer to resolve identifiers and retrieve relevant file segments on demand. You have any tool you want at your disposal. You may wish to use this session to synthesise all the information and discuss options then defer to the following session for more discussion and deliberation before deciding. As in the decision step in this session might be a meta one rather than substantive." Operator's revision supersedes the S048 D-155 + S049 Halt 1 assessment default Q3=(a) scope; operator-directed session-shape revision analogous to S044 D-133 operator-corrective pattern.

**Decision:**

1. **Scope revised.** The EF-047-retrieval-discipline MAD scope named in the S049 assessment (Q3 default "(a) Level A minimum-expected adoption (kernel §1 Warrant-evaluation sub-activity + validator check on preserved-minority pointers); level B and C deliberated") is SET ASIDE for this session. The EF-047 record's level (A) framing as a kernel-discipline-only minor amendment is rejected per operator guidance that "recommendations should include data structure changes rather than 'discipline' only."

2. **S049 shape: synthesis + options + meta-decision.** This session produces a design-space document surveying the operator-named candidates (FTS5, BM25, inverted index, alias tables, MCP-exposed index) against workspace-specific needs; surfaces adjacent alternatives with rejection rationales; proposes S050 MAD agenda (perspectives, questions, input document). No substantive spec edit; no engine-definition file change; no code file produced.

3. **S050 executes substantive deliberation.** The dedicated 4-perspective two-family multi-agent deliberation on retrieval substrate is deferred to Session 050. Operator-ratified Q1 ("yes, proceed with S049 MAD") is reinterpreted under the revised scope as "yes, proceed with the session; with synthesis shape; MAD deliberation itself moves to S050."

4. **Engine-v8 preserved at S049.** No engine-v-bump this session. Engine-v8 preservation window count begins at 1 (S048 → v8 adopted; S049 first post-adoption session).

5. **Assessment 00-assessment.md committed pre-ratification is preserved unedited** per D-017 spirit. The scope revision is recorded here in 02-decisions.md; the 00-assessment.md remains as the pre-ratification record for honest-provenance purposes. Subsequent readers should read 00-assessment.md for the pre-revision framing and this 02-decisions.md D-157 for the operator-directed revision.

6. **Bundled-minor records defer with the substantive.** Operator's ratification of Halt 1 Q4=(b) (bundle EF-047-brief-slot-template + EF-047-session-inputs with the MAD) carries forward: the bundled minors defer to S050 alongside the retrieval MAD, per D-161 below.

---

## D-158: Design-space document produced at provenance/049-session/design-space.md

**Triggers met:** [none]

**Triggers rationale:** Produced artefact is a session-scope provenance file (not an engine-definition spec; not a code file; not an OI state change). §7 honest-limits records the synthesis's authorship (single-orchestrator Case Steward with research sub-agents) and bias surfaces. No specification edited. The document is input to S050 deliberation, not itself a decision record on substrate adoption.

**Single-agent reason:** Research + synthesis work is single-orchestrator-appropriate under operator-directed S049 scope revision (D-157). Three parallel research sub-agents launched (1× Explore agent for codebase survey; 2× general-purpose agents for operator-named candidates deep-dive and adjacent alternatives research); their outputs consolidated by Case Steward into the design-space document. No deliberation performed (MAD deferred to S050). No dissent to record (no perspectives convened at S049).

**Decision:**

1. **Document produced at `provenance/049-session/design-space.md`.** 5,165 words. 12 sections. Covers: problem restatement under operator revision (§1); workspace state measured (§2) including 457 markdown files / 1,417,639 words total / 66,372 words default-read aggregate / 31 preserved minorities / ~4,362 D-NNN grep count / ~4,243 OI-NNN grep count / 23 validate.sh checks with 1,129 assertions; core decision structure (§3); Option A SQLite FTS5 + structured tables + MCP detailed (§4); Option B DuckDB + FTS extension + edges table + MCP detailed (§5); six rejected alternatives with rationale (§6 Meilisearch-Typesense, Tantivy, RDF stores, vector-embedding explicit-rejection-with-Anthropic-contextual-retrieval-framing, Neo4j-Memgraph, rank_bm25-whoosh); three complementary components (§7 git-as-temporal, ripgrep-as-floor, validator-check-24); S050 MAD structure (§8) with 4-perspective composition + 8-question agenda; Option A implementation sketch (§9); scope boundaries of S049 meta-decision (§10); honest limits (§11); ready-for-S050 summary (§12).

2. **Workspace measurements preserved.** Measured rather than estimated: full-corpus wc -w 1,417,639 words; file count 457 markdown files; FTS5 availability confirmed on stock Apple Python 3 (SQLite 3.53.0); estimated index rebuild cost from external research ~140ms for 457-file corpus; sub-millisecond query latency on this scale.

3. **Raw research sub-agent transcripts not preserved as separate files** per single-orchestrator synthesis shape. The three sub-agent outputs are recoverable from the session's transcript if needed; this is an honest-limit on research-provenance preservation relative to what a true MAD would preserve (MAD would commit raw perspective files + synthesis as separate artefacts). Since S050 will execute the MAD with its own perspectives, the research sub-agent outputs serve as Case-Steward preparation rather than as independent-voice deliberation artefacts.

4. **Document is session-scope default-read while S049 is open**, archive-surface on close per read-contract.md v5 §1 item 8 (currently-active session provenance default-read while open). Per §2 per-file budget the document is under 8K hard ceiling (5,165 words). On S049 close, the document becomes archive-surface and is accessed via the archive-surface citation convention per read-contract.md v5 §6 if cited by later sessions. For S050 access, the document is default-read as long as S050's own session is the session reading it; S050 loads it explicitly as MAD input per the shared-brief convention.

---

## D-159: S050 MAD scope, perspectives, and questions pre-ratified (meta-decision on MAD agenda)

**Triggers met:** [none]

**Triggers rationale:** The pre-ratification of S050's MAD shape is a meta-decision about session scheduling and MAD configuration, not itself a substantive decision about the substrate. It records the MAD agenda explicitly so that S050's operator ratification at its own Halt 1 can confirm, revise, or reject the pre-ratified shape. The substantive decisions triggered by the MAD (substrate adoption; spec edits; engine-v bump) happen at S050, not S049.

**Single-agent reason:** Meta-decision under S049's revised scope (D-157). Operator ratified Halt 1 Q1/Q2 (proceed + 4-perspective two-family composition) in the same message that delivered the substantive scope revision; this decision records the operator-ratified composition + design-space-document-derived agenda for S050.

**Decision:**

1. **S050 convening: 4-perspective two-family per operator S044 R2 standing preference + D-133 M2 lineage-constraint + 21-for-21 Outsider-non-Claude convention.**

   | Perspective | Function | Participant-kind | Provider/model-family |
   |-------------|----------|------------------|----------------------|
   | **P1 — Substrate Architect** | Proposes specific architecture (tables, tokenizer config, MCP tool surface, indexer shape); advocates one of Options A/B with concrete rationale | claude-subagent | anthropic/claude |
   | **P2 — Incrementalist / Maintenance Skeptic** | Challenges adoption scope; asks what minimum-viable looks like; questions what each incremental addition buys; applies OI-002 restraint-discipline | claude-subagent | anthropic/claude |
   | **P3 — Outsider** | Frame-completion; asks if problem is framed correctly as substrate question; names 5th/6th alternative not on menu; tests for agent-memory / shrinking-discipline / hybrid-router reframings | non-anthropic-model | openai/gpt-5.5 (via `codex exec --sandbox read-only`; model_id verified per WX-44-2 discipline) |
   | **P4 — Cross-Family Reviewer** | Laundering audit per S047 P4 convention; anti-laundering guards (failed/strained criteria listing; revision traceability; cross-session touch); concrete measurable adoption criteria; shared-frame-blindness check on 4-of-4 convergence if it emerges | non-anthropic-model | openai/gpt-5.5 (via `codex exec --sandbox read-only`) |

   Synonym-drift guard (per S045 D-141): P3 "frame-completion" distinct from P4 "laundering-audit + frame-independence"; both non-Claude by operator preference. D-133 M2 Convene-time 7-column matrix populated at MAD launch.

2. **S050 MAD questions (from design-space §8.2):**

   - **Q1 Primary substrate choice.** Option A (SQLite FTS5) vs Option B (DuckDB + FTS) vs partial-hybrid vs defer-and-stay-lexical-tools-only.
   - **Q2 Adoption scope.** Full-kit (all five tables + FTS + aliases + MCP server + validator check 24 + kernel §1 amendment) vs incremental (phased over S051+).
   - **Q3 Kernel §1 amendment shape.** Does the kernel §1 Read activity gain a "Warrant evaluation" sub-activity calling the retrieval tool? What happens when the tool is unavailable?
   - **Q4 Alias vocabulary.** SKOS three-label (prefLabel/altLabel/hiddenLabel) vs simpler two-label (canonical + aliases) vs defer alias discipline.
   - **Q5 Rebuild trigger.** Git post-commit hook (auto) vs session-open mtime check (lazy) vs both.
   - **Q6 Cross-spec `syncs_with:` frontmatter field.** Redundant with `edges` table, or load-bearing at spec layer as declaration-of-intent?
   - **Q7 External-application inheritance.** Engine-definition (travels byte-identical) vs ancillary (local-only)? Per S046 D-142 precedent.
   - **Q8 Validator check 24 scope.** Preserved-minority pointer baseline, OR extended to [archive: path] resolution, OR extended further to prose-ID-reference resolution.

3. **S050 MAD input.** The design-space document produced at S049 per D-158 is the shared-brief Read input for S050 perspectives. Perspectives additionally read their stance briefs per MAD v4 §Stance Briefs; independent-phase inputs are minimal-and-identical per MAD v4. Workspace files (active specs, prior close files, this 02-decisions.md, engine-feedback/inbox/EF-047-retrieval-discipline-*.md, engine-feedback/triage/EF-047-retrieval-discipline-*.md) remain default-read per read-contract v5 §1 for the Case Steward orchestrating S050, not for the perspectives themselves during independent phase.

4. **S050 MAD convergence-check obligation** per EF-047-session-inputs triage forward observation: "S049's 4-perspective two-family MAD on retrieval-discipline + bundled-minor should include an explicit convergence-check step (naming counter-frames for each proposed adoption; any 4-of-4 convergence at S049 is a data point on whether the shared-frame blindness pattern recurred)." Transferred to S050: P4 Cross-Family Reviewer's laundering audit explicitly performs the convergence-check step, naming counter-frames for any proposed substrate choice; a 4-of-4 convergence at S050 is recorded as a data point on shared-frame blindness recurrence and examined at close.

5. **S050 expected deliverables** at close:

   - `provenance/050-session/01-brief-shared.md` + `01A/B/C/D-perspective-*.md` raw outputs + `01-deliberation.md` synthesis + `manifests/*.manifest.yaml` + `participants.yaml` per MAD v4 layout.
   - `02-decisions.md` recording Q1–Q8 outcomes + substrate adoption decision (if adopt) + engine-v8 → v9 bump (if substantive).
   - If adopt Option A full-kit: `tools/build_retrieval_index.py` + `tools/retrieval_server.py` + `specifications/aliases.yaml` + `.mcp.json` + `methodology-kernel.md` v6 → v7 (+ preserved v6 witness) + `tools/validate.sh` check 24 + `engine-manifest.md` update.
   - If adopt Option A incremental phase 1: subset of the above; phase 2+3 scheduled for S051+.
   - If defer: design-space document preserved; substrate decision rescheduled; rationale recorded.

6. **D-133 M2 third-of-3 verification window at S050.** S050 is the MAD session at which the 3-session verification window concludes (S045 first-of-3; S047 second-of-3; S050 third-of-3 per prior-session counting). Matrix population + lineage-constraint + synonym-drift guard + departure-discipline evaluation at S050 close. If vindication-side clean, convention graduates to standing discipline per D-129 precedent. Note: S049 assessment §7 honest-limit flagged count ambiguity between "MAD-sessions only (S045/S047/S049)" and "MAD-sessions-with-non-Claude (S045/S047/S050 — skipping S049 single-orchestrator)"; this decision adopts the latter interpretation for consistency with D-133's spirit (verification requires actual perspective convening, not single-orchestrator work).

---

## D-160: EF-047-retrieval-discipline triage-record status update; scheduled_mad_session 049 → 050; scheduled_mad_scope revised per design-space §8

**Triggers met:** [none]

**Triggers rationale:** Triage-record status update is administrative recording within the engine-feedback pathway per workspace-structure.md v5 §engine-feedback. Does not modify any active specification, kernel, or OI state. `d016_*` and `d023_*` do not fire.

**Single-agent reason:** Administrative recording of forward-schedule revision corresponding to D-157 scope revision. No deliberation warranted; mechanical update of the triage-file frontmatter to reflect the operator-directed S050 rescheduling.

**Decision:**

1. **`engine-feedback/triage/EF-047-retrieval-discipline-and-text-system-scaling-ceiling.md` frontmatter updated:**

   - `scheduled_mad_session: 049` → `scheduled_mad_session: 050`
   - `status: triaged` → `status: triaged` (unchanged; not yet resolved)
   - `disposition:` revised: "adoption scheduled for S049 dedicated multi-agent deliberation; level (A) adoption minimum expected; level (B) and level (C) MAD-deliberated for scope decision" → "adoption scheduled for S050 dedicated multi-agent deliberation per operator Halt-1 scope revision at S049; design-space document produced at `provenance/049-session/design-space.md` as MAD input; S050 Q1–Q8 agenda records eight deliberation questions covering primary substrate (Option A FTS5 vs Option B DuckDB vs defer), adoption scope (full-kit vs incremental), kernel §1 amendment shape, alias vocabulary, rebuild trigger, syncs_with field disposition, external-application inheritance, validator check 24 scope"
   - `scheduled_mad_scope:` body paragraph revised to reference the design-space document as the canonical scope source.

2. **`engine-feedback/INDEX.md` Records table column updates:**

   - `Triage session` column for the EF-047-retrieval-discipline row: `048` (unchanged; row was triaged at S048).
   - `OI/Disposition` column: "adoption scheduled S049 MAD (bundled minor with retrieval-discipline)" → "rescheduled to S050 MAD per S049 D-160 (operator scope revision: synthesis + options at S049 → substantive MAD at S050); design-space input produced provenance/049-session/design-space.md"
   - Status summary counts: New 0 / Triaged 3 / Resolved 1 / Rejected 0 UNCHANGED (no inbox → triaged transition; no triaged → resolved transition this session; no resolution until S050).

3. **Record state preserved.** `engine-feedback/inbox/EF-047-retrieval-discipline-and-text-system-scaling-ceiling.md` is NOT edited (inbox records immutable per workspace-structure.md v5 §engine-feedback). The scope revision is carried in the triage file (which is the mutable artefact in the lifecycle) and this decision record.

---

## D-161: Bundled-minor EF-047-brief-slot-template + EF-047-session-inputs defer to S050 alongside retrieval MAD

**Triggers met:** [none]

**Triggers rationale:** Per D-157 scope revision, the bundled-minor records defer with the substantive MAD. No spec edit; no code produced. Administrative bundling carried forward.

**Single-agent reason:** Operator's ratified Halt 1 Q4=(b) (bundle with S049 MAD) carries forward under D-157 scope revision: bundled-minors bundle with the MAD wherever the MAD runs; the MAD moves to S050, bundled minors move with it.

**Decision:**

1. **`engine-feedback/triage/EF-047-brief-slot-template-hidden-arc-leakage.md` frontmatter updated:**

   - `scheduled_mad_session: 049` → `scheduled_mad_session: 050`
   - `disposition:` body unchanged in substance; `S049` references updated to `S050`.

2. **`engine-feedback/triage/EF-047-session-input-files-redundant-with-verbatim-capture.md` frontmatter updated:**

   - `scheduled_mad_session: 049` → `scheduled_mad_session: 050`
   - `disposition:` body unchanged; `S049` references updated to `S050`.

3. **`engine-feedback/INDEX.md` Records table:** `scheduled_mad_session` references updated `049` → `050` for both records. Status summary counts unchanged (0 new / 3 triaged / 1 resolved / 0 rejected).

4. **Bundled-minor scope for S050 MAD** (informational; S050 MAD itself decides):

   - EF-047-brief-slot-template options (a) bootstrap `--hidden-arc` flag + `prompts/application.md` paragraph; (b) `workspace-structure.md` v5 §applications documentary clarification; both candidates remain available.
   - EF-047-session-inputs practice-level adopted (operator workflow already dropped session-inputs/ subdirectory for selvedge-disaster-response arc); spec-level minor documentary amendment bundled for S050 adoption.

---

## D-162: Housekeeping (watchpoint status, carry-forwards, standing-discipline applications, SESSION-LOG Q5=(a) thin-row)

**Triggers met:** [none]

**Triggers rationale:** Housekeeping record; no spec edit, no OI state change, no engine-v bump.

**Single-agent reason:** Administrative consolidation of operational observations and forward-carry commitments per standing close convention.

**Decision:**

1. **D-129 standing discipline applied cleanly.** `00-assessment.md` §5b surfaced five considered-and-rejected non-MAD alternatives with non-vacuous rationales (Path A-pure rejected on S048 D-155 breach; single-orchestrator level A alone rejected MAD v4 bypass; 3-perspective rejected operator S044 R2 preference; 5-perspective non-GPT-non-Claude rejected operator preference unrevised; Path L bundle SESSION-LOG rejected double-burdening). Fifth consecutive clean application post-graduation-to-standing-discipline S046. §5.12 Path-Selection Defender reopen warrant (a) "D-129 convention degradation" does not fire.

2. **D-133 M2 verification window count** interpretation adopted: MAD-sessions-with-non-Claude count. Per D-159(6) above, S045/S047/S050 constitute the 3-session window; S049 is single-orchestrator synthesis and is excluded from the matrix-populated M2 verification count (no matrix to populate at single-orchestrator shape). Third-of-3 verification moves from S049-anticipated to S050-executed.

3. **§5.6 GPT-family-concentration spirit-level re-examination carries forward to S050.** S049 is single-orchestrator (zero perspective composition; neither GPT-family-concentration nor non-concentration observable). S050 4-perspective composition continues worst-case-side (2 Codex/GPT-5.5 + 2 Claude + 0 non-GPT non-Claude per operator S044 R2 preference unrevised). Fourth consecutive substantive-deliberation data point at S050. Spirit-level observable-blindness question examined at S050 close.

4. **WX-43-1 OI-promotion evaluation carries forward to S050.** Baseline n=6-of-8 cumulative subagent-self-commit across S043+S044+S045; S047 explicit-instruction variant n=0-of-2 (separate observational window). S049 launched three subagents for research (1 Explore + 2 general-purpose); explicit-instruction variant (agents NOT instructed to self-commit; this session author commits). Adds 0-of-3 to explicit-instruction variant window (now n=0-of-5 across S047 + S049). Cumulative-window methodology remains the S050 MAD question (Q10 deferred per S047/S048 carry-forward pattern); not OI-promoted at S049 on pattern-consistency + agent-category-distinction (research sub-agents ≠ MAD perspectives on commit-discipline surface).

5. **WX-44-1 codex-CLI independence-phase breach** not exercised this session (no codex invocation at S049). Cumulative n=3 across S044+S045+S047 carries forward; S050 codex invocations test forward-convention candidate (codex-CLI prompts during independent phase exclude repo-wide search operations).

6. **WX-47-1 codex-CLI argv `---` YAML frontmatter parsing fragility** not exercised this session. Standing operational discipline (stdin-pipe workaround) carries forward to S050.

7. **Engine-v8 preservation window count 1.** S049 is first post-engine-v8-adoption session; no engine-v bump. Preservation window count begins fresh post-S048 D-154 adoption. Prior engine-v7 window depth 11 (S037–S047) — longest in workspace history; reference for future engine-v8 preservation expectations.

8. **WX-34-1 SESSION-LOG Q5=(a) thin-row discipline selected** per operator Halt 1 ratification ("Yes proceed with default answers"). Target S049 row length ≤180 words; detail in `03-close.md` and design-space document; SESSION-LOG serves as thin index per its stated header intent. Forward observation: whether thin-row discipline is feasible at substantive-session density is itself useful data for S050+ SESSION-LOG restructure decisions. If (a) proves uncomfortable in S049 practice, (b) bundle SESSION-LOG preemptive compression at S050 (S040 D-123 precedent) remains available.

9. **D-138 folder-name default fourth exercise clean.** `049-session` (no suffix, no slug). Four consecutive sessions (S046/S047/S048/S049) use the post-D-094/D-138 `NNN-session` default across distinct session classes: build / content-MAD / default-agent-triage / synthesis. Convention scales across class boundaries; continues standing-discipline post-S046 graduation.

10. **Active OI count unchanged at 13.** No OI opened; no OI resolved; no OI state transition. OI-019 is cross-referenced in the design-space document (§3.6 sub-question (f) "extended-baseline visibility mechanism") as territory that substrate adoption partially addresses; not amended this session. S050 MAD may amend OI-019 with adoption-outcome cross-linkage.

11. **31 first-class minorities preserved unchanged.** No new minority preserved (single-orchestrator synthesis; no deliberation; no dissent surface). No minority discharged. No reopen warrant fires at S049.

12. **Next-session expectation.** S050 is the substantive retrieval-substrate MAD. Operator Halt 1 ratification at S050 is the gate for MAD launch. If operator ratifies defaults, S050 executes 4-perspective two-family MAD per D-159 above; S050 close records substrate adoption decision + optionally engine-v8 → v9 bump + optionally substantive spec/tool/code artefacts. If operator revises scope at S050 Halt 1, session adapts accordingly.

13. **Inbox/triage status at S049 close:** 0 new / 3 triaged (EF-047-retrieval-discipline + EF-047-brief-slot-template + EF-047-session-inputs) / 1 resolved (EF-001) / 0 rejected. All three triaged records carry `scheduled_mad_session: 050` post-D-160/D-161.

14. **SESSION-LOG row at S049 close:** thin-row per Q5=(a). Target ≤180 words. Detail lives in `03-close.md` and `design-space.md`.

15. **WX-28-1 twentieth close-rotation at S049 close.** Session 043 close rotates OUT; Session 049 close enters. Zero retention-exceptions sustained (twenty consecutive rotations S029–S049). Watchpoint pattern continues vindicated.

16. **WX-24-1 MAD stable 6,637 twenty-second-session no-growth streak** (S043–S049 all no-growth; S049 no MAD spec edit). New record.

17. **Path AS (Adoption-Scheduled) forward-naming observation carries forward.** Single-occurrence path-label at S049; reification awaits second-instance confirmation. S050 may or may not be Path AS depending on operator scope at S050 Halt 1 (if S050 continues pre-committed MAD per S049 D-159 schedule, Path AS reifies as second-of-N; if operator surfaces new scope, S050 is Path OS/OC/etc).

18. **Validator state at S049 close** to be recorded post-commit. Expected: 1132+ PASS (additional assertions from design-space + 02-decisions files); 0 FAIL (S049 row in SESSION-LOG at close resolves the expected-fail); 9 warnings (6 decisions-no-rejected-alts design + 3 spec soft-warnings MAD 6,637 + reference-validation 7,160 + SESSION-LOG post-thin-row likely ~7,985 still in soft-warning band if thin-row successful).
