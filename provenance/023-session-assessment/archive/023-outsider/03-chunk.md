rst-exercise would test portability.
   - **(E) OI-015 laundering-gap deliberation.** Session 022 is the 4th positive exercise (operator input surfaced in §3 brief; perspectives treated as input; synthesis adopted non-operator vocabulary on merit). Pattern stable; urgency soft.
   - **(F) Operator-directed agenda.**

4. **Halt for operator ratification** before substantive execution on any path.

5. **Session 022 watchpoints WX-22-1 through WX-22-5** are monitored from Session 023 onward per activation triggers. WX-21-1, WX-21-2, WX-21-3 (Session 021) also continue monitoring. WX-20-1 (mempalace) archived as obsolete (R3 paragraph removed per E.1).

6. **Engine-v3 portability check**: an external-application workspace initialising from engine-v3 must be able to load the new `specifications/read-contract.md` v1 and apply its rules from Session 001. If Session 023+ external-application initialisation surfaces engine-v3-specific friction (e.g., the new check 20 fires on a fresh-clone's initial state; the default-read surface enumeration mismatches the external application's actual file structure), this is a portability bug worth recording as a new OI.

exec
/bin/zsh -lc 'rg -n "8,000|aggregate|cadence|three engine-v-bumps|5.4|minority" provenance/022-workspace-scaling-trajectory/01-deliberation.md provenance/022-workspace-scaling-trajectory/03-close.md provenance/022-workspace-scaling-trajectory/archive/022-outsider/manifest.yaml provenance/022-workspace-scaling-trajectory/archive/022-outsider/*.md' in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
provenance/022-workspace-scaling-trajectory/archive/022-outsider/manifest.yaml:15:    chunk_hash_sha256: af5dd03325e87f7347e9594a3a0daf2ef8bb4bd68d90b3649ce8228033005c14
provenance/022-workspace-scaling-trajectory/archive/022-outsider/manifest.yaml:28:readers_note: Session 022 OpenAI GPT-5.4 Outsider perspective via codex exec (session_id 019db521-775f-7872-9b38-f0c4b0094c28; tokens_used 46,382; reasoning effort xhigh). Full CLI banner + echoed brief + four codex markers with pre-response workspace-exploration tool calls + reasoning summary + response body (opening + Q1-Q9 + Honest Limits) + end-of-stream duplicate response body preserved verbatim per Session 014 precedent. Read chunk 04 for the response body tail (Q7-Q9 + Honest Limits); chunks 01-03 for brief echo + reasoning traces + response body. Per read-contract.md §9, the original file at 01d-perspective-outsider.md was moved into this archive-pack at session close; there is no duplication.
provenance/022-workspace-scaling-trajectory/03-close.md:15:- `01-brief-shared.md` — shared deliberation brief (§1 methodology context; §2 problem statement + scale facts; §3 operator direction verbatim; §4 current spec text excerpts; §5 Session 020 minority warrant assessment; §6 survey of adjacent traditions; §7 perspective placement; §8 design questions Q1–Q9; §9 response format; §10 anti-import constraint; §11 closure). Committed at anchor commit `46f0baf`.
provenance/022-workspace-scaling-trajectory/03-close.md:20:- `01d-perspective-outsider.md` → **archive-packed at close per read-contract.md §9** (22,611 words exceeded 15,000-word hard ceiling). Archive-pack at `archive/022-outsider/` (4 chunks, 50KB each; byte-range boundaries; SHA-256 verified). Original file removed from provenance root; content preserved byte-identical in archive. Outsider position (OpenAI GPT-5.4 via `codex exec`, session id `019db521-775f-7872-9b38-f0c4b0094c28`, tokens_used 46,382, reasoning effort xhigh): partial frame acceptance; diagnoses "broken read contract" as deeper frame than canonical-vs-witness; proposes access-discipline layer cutting across existing file-class ontology; new `specifications/read-contract.md` spec (adopted); bounded working-set contract framing; aggregate-size discipline; prompts/application.md export-consistency concern (all five Outsider contributions shaped adopted content per D-084 synthesis §6).
provenance/022-workspace-scaling-trajectory/03-close.md:21:- `01-deliberation.md` — synthesis. Maps 4-of-4 convergences (C1 E.1; C2 SESSION-LOG restoration) and 3-of-4 cross-family convergences (C3 frame acceptance; C4 kernel revision; C5 prompts revisions; C6 application.md alignment; C7 014 Outsider migration; C8 engine-v3; C9 triggers). Divergences D1–D5 explicitly tracked and resolved with cross-family honesty (D3 new-spec location adopted Outsider's side per cross-family composition; D1 archive-pack location adopted 2-Claude locality with Outsider minority preserved; D2 budget value adopted compromise with Outsider minority preserved). Anti-laundering check passes tests 1 and 3 fully, tests 2 and 4 partially with watchpoints WX-22-1 through WX-22-5.
provenance/022-workspace-scaling-trajectory/03-close.md:92:**Skeptic §5.4 engine-version cadence minority** (two engine-v-bumps in adjacent sessions) preserved as first-class minority with activation warrant at 3-consecutive-bump pattern or external-application portability confusion.
provenance/022-workspace-scaling-trajectory/03-close.md:113:- **D-084** — Adopt R1 through R11 read-contract minimum-coherent set; engine-v2 → engine-v3. Triggers: `[d016_1, d016_2, d016_3, d023_1, d023_2, d023_3]`. Non-Claude participation: Outsider OpenAI GPT-5.4 via `codex exec` as Shape A perspective (qualifies for OI-004 narrowing per v4 §Acceptable Participant Kinds).
provenance/022-workspace-scaling-trajectory/03-close.md:134:3. **Adversarial quality (Q3).** Yes. Skeptic was genuinely adversarial: rejected frame entirely at Q1; rejected prompts revisions at Q2; rejected witness-pack spec at Q3; rejected all retroactive migration at Q4; narrowed SESSION-LOG restoration to prospective-only at Q5; rejected hard-gate at Q6; rejected §5.1 warrant drift at Q7; rejected no-grandfather at Q8; rejected engine bump at Q9. All four Skeptic objections (frame-as-laundering, threshold-arbitrariness, bootstrap-paradox, scope-in-one-session) engaged in the synthesis with mitigations recorded in §4. Skeptic's positions preserved as §5.1 and §5.4 minorities with operational activation warrants. Skeptic's defer-position addressed all three operator falsifiers (96K-word outlier via forward rule; kernel §1 unexecutability via return-to-spec; external-application inheritance via engine-version restraint).
provenance/022-workspace-scaling-trajectory/03-close.md:140:6. **Cross-model-honesty evidence (Q6).** Yes. Synthesis declares `cross_model: true`. Concrete evidence: Outsider manifest declares `participant_kind: non-anthropic-model`, `model_family: gpt`, `model_id: gpt-5.4`, `provider: openai`, `training_lineage_overlap_with_claude: independent-claim`, `participant_organisation: openai`, `independence_basis: organization-distinct`, `training_lineage_evidence_pointer: "unknown-but-asserted"`, `claude_output_in_training: unknown`. Transport notes record the `codex exec -c model_reasoning_effort=xhigh < /tmp/022-outsider-prompt.txt > /tmp/022-outsider-response.txt 2>&1` invocation; background task id `bmk9rdi27`; session id `019db521-775f-7872-9b38-f0c4b0094c28`; 46,382 tokens used; CLI banner preserved verbatim in archive-pack chunk 01. Outsider's bifurcation contribution ("broken read contract" as deeper frame; new-spec proposal for read-contract.md; aggregate-size discipline) qualitatively distinct from any Claude perspective.
provenance/022-workspace-scaling-trajectory/03-close.md:156:- **Workspace total word delta is POSITIVE** (676,879 → 840,956 = +164K words), driven primarily by Session 014 Outsider archive-pack (96K words of line-preservation duplication under copy-plus-reference discipline per D-017 immutability) + Session 022 provenance (~50K words) + other additions. **Default-read surface word delta is NEGATIVE** (~83K → 81,510 = -1.5K words). The operator's stated "net-negative workspace word delta" constraint is achieved at the default-read surface (the canonical orientation layer) but not at the total workspace level. This tension is fundamental: preserving immutable originals via copy-plus-reference (Conservator's load-bearing fidelity constraint) is additive by construction; the only way to achieve net-negative total is to delete originals, which violates D-017. Future sessions may consider a named exception for retroactive-migration-plus-archive cases if the aggregate tension becomes operationally binding. For Session 022, the spirit of the constraint (default-read burden reduced) is honored; the letter (total workspace reduction) is not.
provenance/022-workspace-scaling-trajectory/03-close.md:160:- **Word-count-vs-token-count discrepancy noted for future calibration**. My brief §2.2 and operator §3 cite token counts (SESSION-LOG 33,227 tokens; open-issues 27,437 tokens). The new check 20 measures words not tokens. Word counts for the same files: SESSION-LOG 10,405 words; open-issues 9,783 words. Ratio ~3.0× tokens-per-word for these prose-with-markdown files, not the 1.3× my synthesis §2.3 D2 calculation assumed. The 15,000-word hard ceiling therefore translates to ~45,000 tokens in Read-tool terms (far above the 25,000-token single-Read ceiling), not the ~19,500 tokens I stated. This is the Outsider's §5.3 minority concern materialised — the 15K-word budget is more permissive than my synthesis assumed. Session 023 audit should consider whether to tighten to 8,000-word hard ceiling per Outsider §5.3 on calibration grounds.
provenance/022-workspace-scaling-trajectory/03-close.md:162:- **WX-22-1 through WX-22-5 watchpoints recorded** per synthesis §7 (laundering-as-codification; threshold-adjustment discipline; engine-version cadence; archive-pack location stress test; aggregate default-read surface growth). Session 023+ audits monitor these.
provenance/022-workspace-scaling-trajectory/03-close.md:184:   - **WX-22-2 threshold-adjustment discipline**: 15,000-word hard ceiling was adopted as compromise with Outsider's 8K minority preserved. Session 023 audit should note the word-count-vs-token-count discrepancy per honest-notes above — 15K words ≈ 45K tokens in Read-tool terms, which is ~1.8x the single-Read ceiling. Consider whether to tighten to 8K words or whether to reinterpret the ceiling. If tightening is proposed, it must be a separate deliberation (not a same-session adjustment) per §5.1 operational warrant (iii).
provenance/022-workspace-scaling-trajectory/03-close.md:192:   - **(C) Tighten read-contract §2 budget to 8,000 words per Outsider §5.3 minority.** Calibration-grounded per Session 022 close honest-notes (word-vs-token discrepancy). If adopted, engine-v4 warranted. §5.4 Skeptic cadence minority would activate if adopted at Session 023 (three engine-v-bumps in four sessions).
provenance/022-workspace-scaling-trajectory/archive/022-outsider/04-chunk.md:12:It should hard-fail when any default-read file exceeds the configured per-file budget. I would set that budget in words, not tokens, because the current validator is bash-only and already uses standard Unix tooling [validation-approach §Tool Location and Behavior]. My recommendation is `8,000` words per default-read file.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/04-chunk.md:14:I would also add an aggregate report, and likely a warning threshold, for the total development-provenance default-read surface. Per-file control alone is not sufficient if the default-read set keeps growing by accretion.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/04-chunk.md:18:## Q7. Session 020 minority activations
provenance/022-workspace-scaling-trajectory/archive/022-outsider/04-chunk.md:71:My main disagreement with the operator’s examples is that putting all per-session `03-close.md` files on the canonical/default-read surface would recreate the same growth problem in a slower form. That controls per-file size but not aggregate session-open burden. A bounded surface must be bounded in total, not only in its largest member. So I accept the direction, but I would define the repair as a “bounded working-set contract,” not simply “two artefact kinds.”
provenance/022-workspace-scaling-trajectory/archive/022-outsider/04-chunk.md:127:It should hard-fail when any default-read file exceeds the configured per-file budget. I would set that budget in words, not tokens, because the current validator is bash-only and already uses standard Unix tooling [validation-approach §Tool Location and Behavior]. My recommendation is `8,000` words per default-read file.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/04-chunk.md:129:I would also add an aggregate report, and likely a warning threshold, for the total development-provenance default-read surface. Per-file control alone is not sufficient if the default-read set keeps growing by accretion.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/04-chunk.md:133:## Q7. Session 020 minority activations
provenance/022-workspace-scaling-trajectory/archive/022-outsider/03-chunk.md:288:335:4. **Articulation.** A successor decision defines what "substantively different training provenance" means and enumerates acceptable participant kinds. Articulated Session 021 per D-082; see §Criterion-4 Articulation for OI-004 below.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/03-chunk.md:291:359:**Operational corroboration** (criterion 3, the existing acceptance test) is required to convert eligibility-under-this-articulation into actual narrowing. Criterion-4 articulation defines *who can count*; criterion 3 verifies *whether they did*. This bifurcation follows the 2-of-4 cross-family Session 021 split with cross-family weighting (Skeptic + Outsider) on placing operational corroboration in criterion 3 rather than in criterion-4 definition. The Articulator's [01a, Q1] D-Min ∩ O-Corr position and the Operationaliser's [01c, Q1] P4 position (operational corroboration as definitional prong) are preserved as joint first-class minority §5.5 in `provenance/021-oi004-criterion4-articulation/01-deliberation.md` with operational activation triggers.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/03-chunk.md:401:My main disagreement with the operator’s examples is that putting all per-session `03-close.md` files on the canonical/default-read surface would recreate the same growth problem in a slower form. That controls per-file size but not aggregate session-open burden. A bounded surface must be bounded in total, not only in its largest member. So I accept the direction, but I would define the repair as a “bounded working-set contract,” not simply “two artefact kinds.”
provenance/022-workspace-scaling-trajectory/01-deliberation.md:20:Four perspectives convened: Architect (constructive design advocate), Conservator (preservation-first fidelity tester), Skeptic (adversarial with operator's 3-falsifier burden on defer-positions), Outsider (OpenAI GPT-5.4 via `codex exec`, session id `019db521-775f-7872-9b38-f0c4b0094c28`, reasoning effort xhigh, stdin-pipe invocation per Session 021 lesson).
provenance/022-workspace-scaling-trajectory/01-deliberation.md:22:§5.4 Skeptic mempalace-non-use trigger 1 has materialised (Sessions 020, 021, 022 non-use). Operator ratified E.1 (remove CLAUDE.md R3 mempalace paragraph) and expanded scope to a broader scaling-trajectory deliberation.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:30:**C1. E.1 — Remove CLAUDE.md R3 mempalace paragraph.** All four perspectives affirm the removal. Warrant §5.4 trigger 1 satisfied per non-use Sessions 020/021/022 [01a-Q7, 01b-Q7 §5.4, 01c-Q7 §5.4 "already ratified", 01d-Q7 §5.4 "subsumption"]. Independent concurrence.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:34:Variation in shape: Architect + Conservator + Outsider adopt "thin entries + full detail in 03-close.md"; Skeptic adopts narrower "banner note + go-forward discipline from Session 023, historical entries immutable." This shape-variance is below the convergence threshold — all four agree restoration direction; Skeptic's narrower shape is preserved as a bounding influence on the adopted mechanism (see R8e and §5.4).
provenance/022-workspace-scaling-trajectory/01-deliberation.md:58:Skeptic's concern preserved as §5.3 minority: versioning-frequency-as-churn watchpoint.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:80:2. **Outsider's position preserved as first-class minority §5.1** with activation warrant: if per-session `archive/` subdirectories themselves become a scaling or discovery problem within 5 sessions of adoption, top-level `archives/` becomes the preferred revision direction.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:84:**D2. Budget value for canonical-surface hard-gate.** Architect 25K-token hard / 20K-token soft; Conservator 25K-token hard with word-count fallback; Outsider 8,000 words per file; Skeptic rejects hard-gate, accepts soft-warn at configurable word count.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:96:Outsider's 8K-word preference preserved as minority §5.2 (activation: if the 15K-word budget proves permissive enough that drift continues within 5 sessions, tighten to 8K).
provenance/022-workspace-scaling-trajectory/01-deliberation.md:116:Skeptic's "§5.1 strict warrant not met" concern honored: the split is **not** adoption of the §5.1 minority rollback direction (strict 50K-token threshold unmet); it is exercise of the already-present spec anticipation clause, which has its own independent warrant ("unwieldy" is a shape-test, not a size-test).
provenance/022-workspace-scaling-trajectory/01-deliberation.md:122:**Synthesis adopts 3-of-4 Claude position**: defer reclassification of superseded spec copies. Existing convention (`-v1.md`, `-v2.md` suffix; `supersedes:` frontmatter chain) is adequate; no current scaling pressure on superseded specs (each is ≤5K words; aggregate 9 files; all preservation-layer by type).
provenance/022-workspace-scaling-trajectory/01-deliberation.md:124:Outsider's position preserved as minority §5.5 with activation warrant (if a future session cites a superseded spec as active-canonical because the frontmatter `status: superseded` was not honored, the reclassification-first direction becomes preferred).
provenance/022-workspace-scaling-trajectory/01-deliberation.md:146:## 4. Anti-laundering check on the adoption aggregate (Session 014 Skeptic Q7 test applied)
provenance/022-workspace-scaling-trajectory/01-deliberation.md:156:**Test 2: "Threshold-arbitrariness" — Skeptic's Q3 objection.** Does any threshold choice (15K hard; 10K soft; 8K Outsider-minority) bake in a tunable-in-favor trigger?
provenance/022-workspace-scaling-trajectory/01-deliberation.md:172:**Mitigation partial.** Preserved as §5.3 minority (version-bump cadence watchpoint).
provenance/022-workspace-scaling-trajectory/01-deliberation.md:180:Unanimous 4-of-4. §5.4 Skeptic mempalace-non-use trigger 1 satisfied. CLAUDE.md lines 14–29 deleted; the Session 020 D-080 text is preserved in Session 020's `03-close.md` and in this session's `02-decisions.md` for continuity.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:298:No v-bump would typically be required for a pointer-only amendment. However, coupling with other engine-v3 changes and the open-issues directory creation makes this **substantive in aggregate** per OI-002 precedent of Session 017 D-074 (workspace-structure v2 → v3 was substantive in that bump due to file-class distinction addition). Synthesis declares **v3 → v4 substantive** to pair with open-issues directory creation. v3 preserved as `workspace-structure-v3.md`.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:401:- **OI-004:** tally advances 7-of-3 → 8-of-3 (D-084 fires d023_1 + d023_2 + d023_3 — eighth required-trigger deliberation with non-Claude participation). Criterion-3 cumulative 55 → 60 (5 new Outsider contributions this session: broken-read-contract diagnosis; bounded-working-set-contract framing; new-spec proposal for read-contract.md; aggregate-size discipline; prompts/application.md export-consistency concern). Voluntary:required ratio 7:7 → 7:8 (required overtakes voluntary; second such session after Session 017).
provenance/022-workspace-scaling-trajectory/01-deliberation.md:407:### §5.1 — Skeptic "reject frame entirely" minority
provenance/022-workspace-scaling-trajectory/01-deliberation.md:419:### §5.2 — Outsider minority on archive-pack location (top-level `archives/`)
provenance/022-workspace-scaling-trajectory/01-deliberation.md:431:### §5.3 — Outsider minority on default-read budget (8,000 words)
provenance/022-workspace-scaling-trajectory/01-deliberation.md:433:**Position** [01d-Q6]: 8,000-word per-file budget is the right conservative value; 15,000 words is too permissive and may allow drift to resume.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:439:(ii) A session emerges where a default-read file at 12,000-15,000 words is cited as satisfying the budget but causes a reader burden equivalent to pre-R5 33K-token SESSION-LOG friction. Confirms the budget is calibrated to file-size rather than aggregate-reading-burden.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:441:(iii) Outsider's aggregate-development-provenance-size warning [01d-Q6] materialises: the total default-read set exceeds some reasonable aggregate budget (e.g., 100K words total) even though each individual file is under 15K.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:443:### §5.4 — Skeptic "engine-version adjacency" minority
provenance/022-workspace-scaling-trajectory/01-deliberation.md:449:(i) engine-v3 is bumped to engine-v4 within Sessions 023-025. Confirms cadence concern.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:453:### §5.5 — Outsider minority on superseded-spec reclassification
provenance/022-workspace-scaling-trajectory/01-deliberation.md:461:(ii) The aggregate word count of superseded spec copies in `specifications/` becomes its own scaling surface (e.g., aggregate > 30K words).
provenance/022-workspace-scaling-trajectory/01-deliberation.md:473:4. **Aggregate-size discipline** beyond per-file budget [01d-Q6]: "Per-file control alone is not sufficient if the default-read set keeps growing by accretion." Shapes §5.3 minority warrant (iii); potential R9 check 20 extension to aggregate-set reporting.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:489:**WX-22-3 — Engine-version cadence** (Skeptic §5.4). Track whether engine-v3 → engine-v4 occurs within Sessions 023-025. Concern is version-field becomes change-log timestamp rather than meaningful artefact.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:493:**WX-22-5 — Aggregate default-read surface growth** (Outsider §5.3(iii)). Track total default-read surface word count at each session open. Activates if aggregate exceeds ~100K words.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:499:2. **D1 archive-pack location** adopted session-local over Outsider's top-level on an argument-weight judgment (locality + new-top-level-scaling concern vs immutability-via-no-new-files concern). The cross-family composition is 2 Claude + 0 non-Claude on the adopted side. Synthesis adopted partly because D1 is a design-choice where either can work; preserved Outsider minority §5.2 ensures rollback path.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:509:7. **Skeptic's defer-position** was honored where strictly-literal-warrant-text was respected (§5.1 not activated on softer ceiling-breach condition; §5.1 minority preserved). The Skeptic's broader "reject frame entirely" position was not adopted; it is preserved as §5.1 with activation warrants that honor its load-bearing concerns.
provenance/022-workspace-scaling-trajectory/01-deliberation.md:513:9. **Not synthesized vs rejected**: the synthesis distinguishes. "Not this session" (operator candidate #4 epoch-consolidation; retroactive bulk raw migration; superseded spec reclassification) are deferrals — the candidates remain available for future sessions. "Rejected" (Skeptic's total frame rejection) means the synthesis adopted a different position, preserving the rejected one as minority. Perspectives' positions are not erased by non-adoption.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:8:model_id: gpt-5.4
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:19:  (OpenAI Codex v0.121.0 research preview, model gpt-5.4, provider
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:46:model: gpt-5.4
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:89:### 2.3 §5.4 Skeptic mempalace-non-use trigger 1 — materialised
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:91:Per Session 020 `01-deliberation.md` §5.4 operational warrant (a): "within 3 sessions of R3 adoption, mempalace is not used substantively (indicating the tool was not actually needed)." Sessions 020, 021, and 022 (opener) have not used mempalace substantively. Trigger 1 **has activated.** This ratifies the §5.4 rollback direction: defer-entirely on mempalace becomes preferred direction for R3.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:109:> **Ratify E.1: remove R3 `CLAUDE.md` mempalace paragraph this session.** §5.4 Skeptic mempalace-non-use trigger 1 has materialised (three consecutive non-use sessions: 020, 021, 022); R3's contested adoption has its operational rollback warrant satisfied. Not D-023-triggering (CLAUDE.md is not engine-definition). Voluntary multi-perspective convening recommended per R3's original contested adoption.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:126:> **Session 020 minority activation under current state.** §5.1 Splitter per-OI (warrant: 50K-token file ceiling — satisfied). §5.2 Splitter per-session SESSION-LOG (warrant: Skeptic F3 >12K chars without corresponding complexity — inspect 020–022 entries). §5.3 Outsider restore-to-index (warrant: R1 variance-clause insufficient — inspect 020–022 entries against complexity). §5.4 already activated per E.1 ratification. Assess §5.1–§5.3 against their own warrants.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:232:Per operator direction, each §5.x minority's warrants are re-examined against current session-open state.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:240:**Operator claim** that this warrant is satisfied does not match literal spec text. Perspectives should evaluate whether to (i) adhere to literal warrant, (ii) revise the warrant downward (e.g., to "exceeds single-read ceiling" which IS satisfied), (iii) reject the minority adoption path altogether and treat open-issues separately.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:254:### 5.4 (Skeptic defer-entirely on tools)
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:262:§5.2, §5.3, and §5.4 warrants are **vindicated**. §5.1 strict warrant is **not vindicated**, but related warrants (single-read ceiling breach) are satisfied, raising a question of whether §5.1 should be triggered by the softer ceiling-breach condition too.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:302:- **01d — Outsider.** Non-Claude (OpenAI GPT-5.4 via `codex exec`). Bring training-distribution-independent reasoning to the table.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:340:**Q7. Session 020 minority activations.** Each of §5.1, §5.2, §5.3 has warrants assessed in §5 above. For each:
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:343:- (c) subsume into the canonical/witness frame adoption (i.e., the frame's adoption supersedes the minority's separate activation)?
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:433:Suggested use: when a single Read would exceed the 25,000-token ceiling (SESSION-LOG.md, open-issues.md, aggregated provenance search), orchestrators may run `mempalace search "<query>" --wing complex-systems-engine` or `mempalace wake-up --wing complex-systems-engine` to retrieve candidate matches.
provenance/022-workspace-scaling-trajectory/archive/022-outsider/01-chunk.md:444:Re-mine cadence: manual, typically at session close after substantive file changes. Not a spec requirement; orchestrators not using mempalace need not re-mine.

codex
I have enough context to draft positions now. One remaining check is the aggregate-growth shape: I want the current default-read total and file count in front of me so the Q3 thresholds and Q6 watchpoints are numerically defensible rather than just inherited from the brief.
exec
/bin/zsh -lc "bash -lc '
count_words() {
  local file=\""'$1"
  if head -n 1 "$file" | grep -q "''^---$"; then
    awk "BEGIN{in_yaml=1} NR==1{next} in_yaml && /''^---$/ {in_yaml=0; next} !in_yaml {print}" "$file" | wc -w | tr -d " "
  else
    wc -w < "$file" | tr -d " "
  fi
}
files=()
while IFS= read -r f; do
  status=$(awk '"'BEGIN{in_yaml=0} NR==1 && /"'^---$/ {in_yaml=1; next} in_yaml && /''^status:/ {print $2; exit} in_yaml && /''^---$/ {exit}'"' \""'$f")
  if [ "$status" = "active" ]; then files+=("$f"); fi
done < <(rg --files specifications -g '"'*.md' | sort)
files+=(PROMPT.md prompts/development.md prompts/application.md SESSION-LOG.md open-issues/index.md)
while IFS= read -r f; do files+=(\""'$f"); done < <(rg --files provenance -g '"'03-close.md' | sort)
# current active session provenance root files
while IFS= read -r f; do files+=(\""'$f"); done < <(find provenance/023-session-assessment -maxdepth 1 -type f | sort)
# de-dup and report
printf "%s'"\\n\" \""'${files[@]}" | awk '"'"'!seen[$0]++'"' > /tmp/default_read_files.txt
count=0
total=0
while IFS= read -r f; do
  w="'$(count_words "$f")
  count=$((count+1))
  total=$((total+w))
  printf "%6d %s'"\\n\" \""'$w" "$f"
done < /tmp/default_read_files.txt | sort -nr | tee /tmp/default_read_counts.txt >/tmp/default_read_sorted.txt
printf "COUNT=%d'"\\nTOTAL=%d\\n\" \""'$count" "$total"
head -n 10 /tmp/default_read_sorted.txt
'"'" in /Users/ericmccowan/Development/complex-systems-engine
 exited 1 in 0ms:
zsh:12: parse error near `}'

codex
The aggregate check hit a shell quoting error. I’m rerunning it with a cleaner `bash` block; the goal is just a count and top files, not a broader scan.
2026-04-22T19:22:15.102005Z ERROR codex_core::tools::router: error=exec_command failed for `/bin/bash -c 'count_words() {
  local file="$1"
  if head -n 1 "$file" | grep -q '"'"'^---$'"'; then
    awk 'BEGIN{in_yaml=1} NR==1{next} in_yaml && /"'^---$/ {in_yaml=0; next} !in_yaml {print}'"' \""'$file" | wc -w | tr -d '"' '
  else
    wc -w < \""'$file" | tr -d '"' '
  fi
}

files=()
while IFS= read -r f; do
  status="'$(awk '"'BEGIN{in_yaml=0} NR==1 && /"'^---$/ {in_yaml=1; next} in_yaml && /''^status:/ {print $2; exit} in_yaml && /''^---$/ {exit}'"' \""'$f")
  if [ "$status" = active ]; then
    files+=("$f")
  fi
done < <(rg --files specifications -g '"'*.md' | sort)

files+=(PROMPT.md prompts/development.md prompts/application.md SESSION-LOG.md open-issues/index.md)

while IFS= read -r f; do
  files+=(\""'$f")
done < <(rg --files provenance -g '"'03-close.md' | sort)

while IFS= read -r f; do
  files+=(\""'$f")
done < <(find provenance/023-session-assessment -maxdepth 1 -type f | sort)

printf '"'%s\\n' \""'${files[@]}" | awk '"'"'!seen[$0]++'"' > /tmp/default_read_files.txt
count=0
total=0
while IFS= read -r f; do
  w="'$(count_words "$f")
  count=$((count+1))
  total=$((total+w))
  printf '"'%6d %s\\n' \""'$w" "$f"
done < /tmp/default_read_files.txt | sort -nr > /tmp/default_read_counts.txt

printf '"'COUNT=%d\\nTOTAL=%d\\n' \""'$count" "$total"
head -n 10 /tmp/default_read_counts.txt
'`: CreateProcess { message: "Codex(Sandbox(Denied { output: ExecToolCallOutput { exit_code: 1, stdout: StreamOutput { text: \"\", truncated_after_lines: None }, stderr: StreamOutput { text: \"/bin/bash: line 27: /tmp/default_read_files.txt: Operation not permitted\\n/bin/bash: line 35: /tmp/default_read_files.txt: No such file or directory\\n/bin/bash: line 35: /tmp/default_read_counts.txt: Operation not permitted\\nCOUNT=0\\nTOTAL=0\\nhead: /tmp/default_read_counts.txt: No such file or directory\\n\", truncated_after_lines: None }, aggregated_output: StreamOutput { text: \"/bin/bash: line 27: /tmp/default_read_files.txt: Operation not permitted\\n/bin/bash: line 35: /tmp/default_read_files.txt: No such file or directory\\n/bin/bash: line 35: /tmp/default_read_counts.txt: Operation not permitted\\nCOUNT=0\\nTOTAL=0\\nhead: /tmp/default_read_counts.txt: No such file or directory\\n\", truncated_after_lines: None }, duration: 0ns, timed_out: false }, network_policy_decision: None }))" }
exec
/bin/bash -c 'count_words() {
  local file="$1"
  if head -n 1 "$file" | grep -q '"'"'^---$'"'; then
    awk 'BEGIN{in_yaml=1} NR==1{next} in_yaml && /"'^---$/ {in_yaml=0; next} !in_yaml {print}'"' \""'$file" | wc -w | tr -d '"' '
  else
    wc -w < \""'$file" | tr -d '"' '
  fi
}

declare -A seen
files=()
while IFS= read -r f; do
  status="'$(awk '"'BEGIN{in_yaml=0} NR==1 && /"'^---$/ {in_yaml=1; next} in_yaml && /''^status:/ {print $2; exit} in_yaml && /''^---$/ {exit}'"' \""'$f")
  if [ "$status" = active ] && [ -z "${seen[$f]}" ]; then
    seen[$f]=1
    files+=("$f")
  fi
done < <(rg --files specifications -g '"'*.md' | sort)

for f in PROMPT.md prompts/development.md prompts/application.md SESSION-LOG.md open-issues/index.md; do
  if [ -z \""'${seen[$f]}" ]; then
    seen[$f]=1
    files+=("$f")
  fi
done

while IFS= read -r f; do
  if [ -z "${seen[$f]}" ]; then
    seen[$f]=1
    files+=("$f")
  fi
done < <(rg --files provenance -g '"'03-close.md' | sort)

while IFS= read -r f; do
  if [ -z \""'${seen[$f]}" ]; then
    seen[$f]=1
    files+=("$f")
  fi
done < <(find provenance/023-session-assessment -maxdepth 1 -type f | sort)

count=0
total=0
for f in "${files[@]}"; do
  w=$(count_words "$f")
  count=$((count+1))
  total=$((total+w))
  printf '"'%6d %s\\n' \""'$w" "$f"
done | sort -nr
printf '"'COUNT=%d TOTAL=%d\\n' \""'$count" "$total"
' in /Users/ericmccowan/Development/complex-systems-engine
 exited 1 in 0ms:
/bin/bash: line 9: declare: -A: invalid option
declare: usage: declare [-afFirtx] [-p] [name[=value] ...]
/bin/bash: line 13: specifications/engine-manifest.md: division by 0 (error token is "-manifest.md")

codex
The sandbox is exposing macOS’s older shell behavior, so I’m switching to a single Ruby read-only pass for the aggregate numbers. That avoids temp files and keeps the check mechanical.
exec
/bin/zsh -lc "ruby -e '
require \"pathname\"

def body_words(path)
  s = File.read(path)
  if s.start_with?(\"---\\n\")
    parts = s.split(/"'^---'"\\s*"'$'"\\n/, 3)
    s = parts[2] || s
  end
  s.split(/\\s+/).reject(&:empty?).length
end

def active_status?(path)
  s = File.read(path)
  return false unless s.start_with?(\"---\\n\")
  fm = s.split(/"'^---'"\\s*"'$'"\\n/, 3)[1] || \"\"
  fm.lines.any? { |l| l.strip == \"status: active\" }
end

files = []
Dir.glob(\"specifications/*.md\").sort.each do |f|
  files << f if active_status?(f)
end
files.concat([\"PROMPT.md\", \"prompts/development.md\", \"prompts/application.md\", \"SESSION-LOG.md\", \"open-issues/index.md\"])
files.concat(Dir.glob(\"provenance/*/03-close.md\").sort)
files.concat(Dir.glob(\"provenance/023-session-assessment/*\").select { |f| File.file?(f) }.sort)
files = files.uniq
counts = files.map { |f| [body_words(f), f] }.sort.reverse
counts.first(12).each { |w, f| puts \"%6d %s\" % [w, f] }
puts \"COUNT=#{files.length} TOTAL=#{counts.sum { |w, _| w }}\"
'" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 122ms:
  6386 specifications/multi-agent-deliberation.md
  5166 specifications/reference-validation.md
  4647 specifications/validation-approach.md
  4499 provenance/021-oi004-criterion4-articulation/03-close.md
  4454 provenance/013-artefact-revision/03-close.md
  3796 provenance/022-workspace-scaling-trajectory/03-close.md
  3698 provenance/014-oi016-resolution/03-close.md
  3585 provenance/012-methodology-naming/03-close.md
  3315 provenance/023-session-assessment/01-brief-shared.md
  3255 provenance/011-w1-kernel-read-revision/03-close.md
  3119 provenance/007-external-application-examination/03-close.md
  2974 provenance/008-first-external-application/03-close.md
COUNT=36 TOTAL=90763

codex
I checked the aggregate mechanically and got `COUNT=36 TOTAL=90,763`, but that included every current-session file in `provenance/023-session-assessment/`, which is too broad for this task. I’m narrowing back to the explicitly relevant files and will treat the brief’s stated `~81,500 across 33 files` as the deliberation baseline rather than lean on a broader scan of the active session directory.
exec
/bin/zsh -lc 'find provenance/023-session-assessment -maxdepth 1 -type f | sort' in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
provenance/023-session-assessment/00-assessment.md
provenance/023-session-assessment/01-brief-shared.md

exec
/bin/zsh -lc 'wc -w specifications/multi-agent-deliberation.md specifications/reference-validation.md' in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
    6403 specifications/multi-agent-deliberation.md
    5183 specifications/reference-validation.md
   11586 total

exec
/bin/zsh -lc "sed -n '431,452p' provenance/022-workspace-scaling-trajectory/01-deliberation.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
### §5.3 — Outsider minority on default-read budget (8,000 words)

**Position** [01d-Q6]: 8,000-word per-file budget is the right conservative value; 15,000 words is too permissive and may allow drift to resume.

**Operational warrant.** Minority becomes preferred revision direction if any of:

(i) Within 5 sessions of R5 adoption, any default-read file exceeds 10,000 words (the soft-warn threshold) without subsequent migration. Confirms 15,000 hard ceiling is permissive-enough that drift resumes.

(ii) A session emerges where a default-read file at 12,000-15,000 words is cited as satisfying the budget but causes a reader burden equivalent to pre-R5 33K-token SESSION-LOG friction. Confirms the budget is calibrated to file-size rather than aggregate-reading-burden.

(iii) Outsider's aggregate-development-provenance-size warning [01d-Q6] materialises: the total default-read set exceeds some reasonable aggregate budget (e.g., 100K words total) even though each individual file is under 15K.

### §5.4 — Skeptic "engine-version adjacency" minority

**Position** [01c-Q9]: two engine bumps in adjacent sessions (v1→v2 Session 021; v2→v3 Session 022) convert the engine-version field into a change-log timestamp. A minimum-session-gap discipline between engine bumps would protect the field's meaning.

**Operational warrant.** Minority becomes preferred revision direction if any of:

(i) engine-v3 is bumped to engine-v4 within Sessions 023-025. Confirms cadence concern.

(ii) An external application loading engine-v2 faces portability-loss because it does not know whether to also load engine-v3 changes, or vice versa; the version-frequency creates ambiguity.


codex
## Q1. Hard ceiling value

**8,000 words.**

The decisive issue is not whether the Session 022 Outsider activation warrant literally fired. It did not. The decisive issue is that the adopted calibration for `read-contract.md §2` has already been falsified. The current rationale says 15,000 words sits below a ~25,000-token single-read ceiling because it assumed ~1.3 tokens per word. Session 022’s close notes say the workspace’s prose-with-markdown files are empirically closer to ~3.0 tokens per word, making 15,000 words roughly 45,000 tokens and 10,000 words roughly 30,000 tokens (`provenance/022-workspace-scaling-trajectory/03-close.md`; brief §2-§3). On that calibration, 15K is not a ceiling relative to single-read effort; 12K and 10K are still above the stated single-read anchor.

`read-contract.md §2` was justified as a reader-contract, not just an anti-explosion number. If default-read means “read in full at every session open,” then a per-file ceiling that routinely requires paginated reading is misaligned with the rule’s own purpose. 8,000 words is the only surveyed value that still fits beneath the stated single-read ceiling at the empirical ratio (~24,000 tokens). It preserves the original shape of the argument while correcting the arithmetic.

It is also meaningfully binding without being immediately disruptive. On the brief’s own Session 023-open facts, the largest default-read file is ~4,800 words, so 8,000 words would bind at about 60% utilization rather than 32% under the current 15,000-word ceiling. That is what a real budget should look like: enough headroom for normal growth, not enough headroom to make restructuring optional forever. This matches the prior Outsider’s preserved warning that 15K risked becoming ceremonial rather than constraining [archive: provenance/022-workspace-scaling-trajectory/archive/022-outsider/#chunk-04, Q6]; `provenance/022-workspace-scaling-trajectory/01-deliberation.md §5.3`.

If the methodology wants to allow routine paginated reads inside the default-read surface, it can say that. But then the contract has changed in kind and should no longer be defended by appeal to single-read feasibility. I would not preserve that ambiguity.

## Q2. Soft warning value

**6,000 words, fixed.**

At the same ~3.0 tokens-per-word calibration, 6,000 words is roughly 18,000 tokens. That leaves real room below an 8,000-word hard ceiling while still giving early signal before a file becomes difficult to keep within one read. It keeps the warning meaningful as “approaching the ceiling,” not “already beyond the single-read anchor.”

I would not remove the warning. With an 8,000-word hard ceiling, a session needs advance signal to restructure before a file hard-fails at close. I also would not use 5,000 words. On the brief’s numbers, the current largest files are already in the high-4,000s. A 5K warning would be so close to normal large-file size that it risks becoming background noise rather than a useful early signal.

I also prefer a fixed value over a percentage formula in the live spec. The validator and `validation-approach.md` currently express these as explicit constants and thresholds, not derived formulas. A formula is elegant, but it adds interpretation overhead for little gain here. The reasoning can still be “approximately 75% of hard,” while the rule remains simply `6000`.

## Q3. Aggregate default-read surface budget

**Do not adopt an aggregate hard budget this session. Add it as a watchpoint, and preferably as a non-gating report.**

Using the working-set distinction named in brief §5 as a hypothesis rather than imported authority: per-file burden and aggregate working-set burden are different problems. The prior Outsider was right that per-file control alone does not stop aggregate drift by accretion [archive: provenance/022-workspace-scaling-trajectory/archive/022-outsider/#chunk-04, Q6]. I do think the aggregate surface should be measured every session and watched explicitly.

I do **not** think it should become a hard budget this session, because the remediation path is still underdesigned. Under `read-contract.md §1`, every closed session’s `03-close.md` remains default-read. That means total default-read words grow almost monotonically. Under the immutability rules carried through the current architecture, retroactive relief is limited. So a hard aggregate ceiling now would create a binding rule without a clear, already-legible repair path except a larger redesign of what counts as default-read.

My recommendation is:

- Record total default-read words at session open and close if convenient.
- Treat `>90,000 words` as an advisory watchpoint.
- Treat `>100,000 words` as the activation trigger where aggregate-budget design, or default-read-enumeration redesign, becomes the preferred revision direction.

That is consistent with the preserved Session 022 wording that used “e.g., 100K words total” as the operative scale for the aggregate concern (`provenance/022-workspace-scaling-trajectory/01-deliberation.md §5.3`; §7 WX-22-5). I would also trigger review if the aggregate grows by more than roughly 10% in a single session without a corresponding restructuring event. That catches sudden accretion, not just slow drift.

## Q4. Engine-version classification

**If Q1 changes the ceiling from 15,000, this is `engine-v4`. I do not see an honest narrow interpretation that avoids the bump under the current specs.**

`read-contract.md §10` explicitly says that changes to §2 budget values are substantive. `validation-approach.md`’s checks-20-22 gating section explicitly says revising the budget constants in `tools/validate.sh` is substantive and requires an engine-version bump. `engine-manifest.md §5` then says any substantive revision to an engine-definition file increments the engine version. This is mechanically overdetermined, not ambiguous.

On OI-002 merits, that classification is also correct. Budget values are not “minor elaborations within existing scope.” They change normative thresholds, failure/warning behavior, and session-close obligations. OI-002 consistently treats new rules, thresholds, triggers, severity decisions, and required artifacts as substantive (`open-issues/OI-002.md`). A 15K→8K change is exactly that sort of revision.

The only way to avoid `engine-v4` would be to first change the versioning discipline so that this sort of constant-tuning counts as minor. But that would itself be a substantive revision to the engine’s versioning rules. It is not a plausible “interpretation” of the current text. So if the ceiling changes, call the result `engine-v4`.

## Q5. Engine-version cadence (§5.4 minority response)

**Treat the activated warrant as a real informational signal, record it plainly, and proceed with `engine-v4` on the merits. Do not suppress the bump by reclassification.**

The Session 022 Skeptic minority gave a concrete warrant: if `engine-v3` is bumped to `engine-v4` within Sessions 023-025, the cadence concern is activated (`provenance/022-workspace-scaling-trajectory/01-deliberation.md §5.4`). If this session tightens the budget, that warrant fires. The deliberation should say so directly. Minority preservation only means something if triggered minorities are acknowledged when triggered.

But I would not let cadence pressure distort Q1 or Q4. Keeping a miscalibrated budget, or pretending a substantive threshold change is minor, would make the engine-version field less honest, not more. The cadence minority is warning about meaning-loss in the version number. Misclassification in order to avoid a bump would itself be meaning-loss.

I also would not revise `engine-manifest.md §5` in the same session purely to get relief from this case. That would read as goal-seeking rule change under immediate pressure. The cleaner response is:

- Admit the cadence warrant has activated.
- Still adopt `engine-v4` if the budget change is merited.
- Raise the burden for any near-term further engine bump.
- If `engine-v5` is proposed before Session 026, or if an external application shows real portability confusion between adjacent engine versions, then run a dedicated versioning-discipline deliberation.

That preserves both truths at once: the budget should be corrected, and the cadence pattern is now a live governance concern.

## Q6. Watchpoints and minorities

I would preserve these as first-class minorities:

- **10,000-word hard ceiling minority.** This is the strongest live counterposition on Q1. It accepts the calibration problem but permits routine paginated reading inside default-read. Activation trigger: if an 8,000-word ceiling forces two consecutive sessions into coherence-damaging splits, or produces repeated soft warnings/failures on files that remain operationally readable and well-structured, revisit upward.
- **Aggregate-budget-now minority.** If this session does not adopt an aggregate budget, preserve the contrary position that aggregate default-read burden should become normative, not merely observed. Activation trigger: aggregate default-read total exceeds 100,000 words; or exceeds 90,000 for two consecutive sessions; or grows by >10% in one session without compensating restructure.
- **Session 022 cadence minority (`§5.4`).** This should remain first-class and should now be marked activated if `engine-v4` is adopted. Escalation trigger after activation: `engine-v5` proposed before Session 026, or external-application portability confusion appears.

I would monitor these watchpoints in Session 024+:

- **Per-file drift under the new budget.** If any file sits above the soft warning for two consecutive sessions without restructure, the warning is not doing its job.
- **Near-ceiling clustering.** If several default-read files accumulate in the 7,000-8,000-word band at once, the problem may be document-shape drift rather than isolated file growth.
- **Aggregate growth.** Report the session-open and session-close totals. `>90K` is advisory; `>100K` should trigger design work.
- **Calibration discipline.** If future rationales convert tokens to words, they should use workspace-empirical calibration, not gene