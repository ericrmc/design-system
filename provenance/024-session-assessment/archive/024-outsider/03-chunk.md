mily participants). Check 19 is out-of-scope for `participant_kind` other than `non-anthropic-model` (organisational origin closed-set membership is required only for non-Anthropic LLM participants). These are recorded inline in the validate.sh check implementation and in the honest-limit comments.
    95	
    96	**Closed-set extension discipline.** The PARTICIPANT_ORGANISATION_CLOSED_SET in `validate.sh` is initialised at engine-v2 with values `{anthropic, openai, google, meta, xai, mistral, deepseek, cohere, local, human-individual, other-named}`. Extending this set requires a named decision in a session's `02-decisions.md` and a same-session update to the constant. Adding a new provider is **not** a substantive revision to `multi-agent-deliberation.md` per OI-002 heuristic (the spec already permits the closed set to extend); it is a substantive update to `tools/validate.sh` per `engine-manifest.md` §5 only when the addition substantively changes what counts as criterion-4-eligible. Routine provider additions (e.g., adding `cohere` after first operational use) are treated as minor validator-data updates not triggering an engine-version bump. This convention is established Session 021 and may be revisited if it produces silent failures.
    97	
    98	**Consequence for prior sessions.** Sessions 001 through 020 are out-of-scope for checks 16, 17, 19. Session 021 and later sessions whose manifests claim OI-004 narrowing must include the new fields per the schema in `multi-agent-deliberation.md` v4. Pre-adoption sessions retain their original manifests unchanged.
    99	
   100	### Gating Conventions (checks 20, 21, 22) — Session-number and presence-gating
   101	
   102	**Session-number-gating (check 20).** Check 20 applies only to sessions numbered ≥ 022 (the session that adopted `specifications/read-contract.md` v1). The gate is encoded as an explicit constant `READ_CONTRACT_ADOPTION_SESSION=22` near the top of `validate.sh`. Out-of-scope sessions (001 through 021) produce no output from check 20 — pre-adoption SESSION-LOG.md / open-issues.md sizes are preserved as-is until the R8a / R8b migrations complete in Session 022.
   103	
   104	**Presence-gating (checks 21, 22).** Checks 21 and 22 fire only when at least one `provenance/*/archive/*/` directory exists. The archive-pack infrastructure does not exist until Session 022 creates the first archive-pack (Session 014 Outsider retroactive migration per R8c); pre-existence sessions are out-of-scope.
   105	
   106	**Rationale for mixed gating.** Check 20 measures default-read surface files that exist prospectively from the adoption session onward. Checks 21 and 22 measure archive-packs that exist only when created; presence-gating is the correct mechanism per Session 005 D-030 precedent.
   107	
   108	**Budget constants.** Encoded near the top of `validate.sh`:
   109	
   110	```
   111	DEFAULT_READ_HARD_WORD_CEILING=15000
   112	DEFAULT_READ_SOFT_WORD_CEILING=10000
   113	READ_CONTRACT_ADOPTION_SESSION=22
   114	```
   115	
   116	Any revision to these constants is a substantive revision to `tools/validate.sh` per `engine-manifest.md` §5 and requires an engine-version bump.
   117	
   118	**Measurement.** Check 20 measures word count via `wc -w` on body content after the closing YAML frontmatter delimiter. Frontmatter and the three-dash delimiters themselves are excluded.
   119	
   120	**Default-read surface detection.** The validator maintains a canonical default-read file-set derived from `read-contract.md` §1. The implementation uses a glob-based helper (not filename heuristics) reading the §1 enumeration patterns:
   121	- `specifications/*.md` where frontmatter `status: active` (not `superseded`, `draft`, or `deprecated`).
   122	- `PROMPT.md`, `prompts/development.md`, `prompts/application.md`.
   123	- `SESSION-LOG.md`.
   124	- `open-issues/index.md`.
   125	- `provenance/*/03-close.md`.
   126	- Files in the currently-active session's provenance directory (only the most recent NNN- directory containing an un-closed `03-close.md` or no `03-close.md` at all).
   127	
   128	Archive-pack files and superseded-status specifications are excluded from check 20 scope.
   129	
   130	### Sequencing (check 13 after check 12; check 14 after check 11; check 15 after check 12)
   131	
   132	Check 13 depends on well-formed manifests. If check 12 fails for a given session, check 13 reports `BLOCKED: check 12 failed for this session; cannot evaluate check 13` for that session and does not itself fail or warn. This prevents double-reporting of a single underlying problem and keeps the tool honest about what it actually evaluated.
   133	
   134	Check 14 depends on the three-raw-output floor established by check 11. If check 11 fails for a given session (fewer than three perspective files when multi-agent artefacts are asserted), check 14 reports `BLOCKED: check 11 failed for this session; cannot evaluate check 14`. Check 14 does **not** depend on check 12: it inspects perspective-file presence, not manifest content (per D-040, the Outsider's precision argument).
   135	
   136	Check 15 depends on well-formed manifests. If check 12 fails for a given session, check 15 reports `BLOCKED: check 12 failed for this session; cannot evaluate check 15`. Check 15 is independent of check 14 (a decision can fail 15 while passing 14 or vice versa).
   137	
   138	### Check 13's Honest Limit (mandatory inline documentation)
   139	
   140	Check 13 enforces **consistency of self-report**, not **truthfulness of self-report**. This limit is mandatory content in three locations:
   141	
   142	1. A comment block in `tools/validate.sh` directly above check 13's implementation.
   143	2. Check 13's failure message (as an inline NOTE).
   144	3. This specification (above).
   145	
   146	The language to preserve verbatim:
   147	
   148	> This check verifies the session's claim is internally consistent with its manifests. It does not and cannot verify that the manifests' lineage claims are themselves true. Manifest truth relies on operator integrity and the `participant_selected_by` field's accountability.
   149	
   150	**Known gaming modes** (recorded in D-029 and preserved for future maintainers):
   151	
   152	- **Value-flipping.** An operator edits `training_lineage_overlap_with_claude` in the manifest of a Claude subagent from `known-overlap` to `independent-claim`; the check passes.
   153	- **`unknown` laundering.** An operator sets one participant's lineage field to `unknown` (a valid value) when the true value is `known-overlap`; the check passes.
   154	- **Paper-human classification.** An operator records a nominal human participant who did not substantively participate; the check passes because `participant_kind: human` bypasses the lineage-value check.
   155	- **Wrapper impersonation.** An operator routes a Claude call through a wrapper that looks like a non-Claude CLI and lies in the `provider` field; the check cannot distinguish this from a genuine non-Claude invocation.
   156	
   157	These gaming modes are not fixed by check 13 alone. The Tier 2 question paired with check 13 (see below) is the methodology's designed counter-pressure to laundering by self-report.
   158	
   159	### Check 14's Honest Limit (mandatory inline documentation)
   160	
   161	Check 14 enforces **consistency between a decision's self-declared triggers and the session's multi-agent artefacts**, not **truthfulness of the declaration itself**. This limit is mandatory content in three locations:
   162	
   163	1. A comment block in `tools/validate.sh` directly above check 14's implementation.
   164	2. Check 14's failure message (as an inline NOTE).
   165	3. This specification (above).
   166	
   167	The language to preserve verbatim:
   168	
   169	> This check verifies consistency between a decision's self-declared `triggers_met:` and the session's multi-agent artefacts. It does not and cannot verify that the `triggers_met:` declaration is itself a truthful classification of the decision against D-016. The declaration's truth relies on operator integrity and the `triggers_rationale:` field's adversarial visibility to Tier 2 review.
   170	
   171	**Known false-compliance patterns** (recorded in D-040 rationale and preserved for future maintainers):
   172	
   173	- **Under-declaration.** Writing `triggers_met: [none]` on a decision that in fact modifies the kernel. Check 14 passes silently.
   174	- **Mono-perspective launder.** Three raw perspective files generated by re-prompting the same model with minor wording changes. Check 11 passes (three files present); check 14 passes (artefacts present for declared trigger); the substantive mono-perspective nature is undetected.
   175	- **Strawman positions.** A `triggers_met: [d016_3]` claim (reasonable-disagreement trigger) justified by "two plausible positions" that are in fact strawmen. Deliberation-quality is out of scope for Tier 1.
   176	- **Fabricated load-bearing claim.** A `triggers_met: [d016_4]` (operator-marked load-bearing) with a plausible-sounding Rationale that reclassifies a trivial decision as deliberation-worthy, or the inverse.
   177	
   178	These patterns are not fixed by check 14 alone. The Tier 2 Q7 question (see below) is the designed counter-pressure.
   179	
   180	### Check 15's Honest Limit (mandatory inline documentation)
   181	
   182	Check 15 enforces **consistency between a decision's self-declared `d023_*` triggers and the session's non-Claude participant manifests**, not **truthfulness of manifest labels or skip reasons**. This limit is mandatory content in three locations:
   183	
   184	1. A comment block in `tools/validate.sh` directly above check 15's implementation.
   185	2. Check 15's failure message (as an inline NOTE).
   186	3. This specification (above).
   187	
   188	The language to preserve verbatim:
   189	
   190	> This check verifies consistency between a decision's self-declared `d023_*` triggers and the session's non-Claude participant manifests. It does not verify that a manifest labeled non-Claude in fact represents a non-Claude participant (that is check 13's consistency scope) nor that the substantive adequacy of any skip reason is genuine (a Tier 2 concern). The declaration's truth relies on operator integrity.
   191	
   192	**Known false-compliance patterns** (recorded in D-040 rationale):
   193	
   194	- **Mislabeled manifest.** Relabeling a Claude-subagent manifest entry as `participant_kind: non-anthropic-model`. Check 15 passes; check 13's consistency scope catches this only if `cross_model: true` is also claimed.
   195	- **Bogus skip annotation.** `**Non-Claude participation:** skipped — reason: "time constraints"; retry_in_session: S999` with no intention of retry. Check 15 passes on field presence; the reason's quality and retry commitment are Tier 2 concerns.
   196	- **Pattern of skips.** Over-using the skip annotation across many sessions. No single check catches this; Tier 2 pattern-review is the counter-pressure.
   197	
   198	### Tier 2: Guided Assessment
   199	
   200	The following questions are printed for the assessor to consider:
   201	
   202	1. **Provenance continuity:** Did this session's Read activity use prior provenance to understand past decisions? Were any past decisions re-proposed without acknowledgment?
   203	2. **Specification consistency:** Are the current specifications semantically consistent with each other? Do any contradict or make assumptions that conflict?
   204	3. **Adversarial quality:** In deliberative work, did the adversarial perspective provide genuine challenge, or did it concede too easily?
   205	4. **Meaningful progress:** Is the methodology producing meaningful progress, or is it accumulating ceremony without advancing?
   206	5. **Specification-reality alignment:** Are there specifications that describe things that no longer exist, or things that exist without being specified?
   207	6. **Cross-model-honesty evidence (paired with check 13):** This session records `cross_model: true`. Name the concrete evidence — invocation transcript, CLI command, wall-clock gap, human presence — that distinguishes a genuine non-Claude participant from a Claude subagent with an edited manifest. If you cannot, flip `cross_model` to false. (Skip if this session does not claim cross-model participation.)
   208	
   209	7. **Trigger-coverage plausibility (new in v3; paired with checks 14 and 15):** For each decision in this session declaring `**Triggers met:**`, read the decision's `**Decision:**` and `**Rationale:**` text and state whether the declared trigger list is consistent with the decision's content. For any `**Non-Claude participation:** skipped` annotation, state whether the reason is substantive (not formulaic) and the `retry_in_session:` commitment is credible. Flag mismatches and weak reasons; they are the dishonesty surface this session's Tier 1 checks cannot reach.
   210	
   211	8. **OI-004 closure-retrospective substantive adequacy (new in v4; paired with check 18):** If this session contains an `oi-004-retrospective.md`, read its Qualifying Deliberations Table and P4 Assertion. For each row marked frame-replacement-or-novel-mechanism, verify the cited synthesis section actually contains a non-Claude-originated reframing (not paraphrase or restatement of a Claude perspective's argument). For the P4 assertion, verify the cited divergence shows the synthesis adopted a position that contradicts (or substantively augments) the Claude consensus, not merely supplemented it. Flag rows where the substantive claim is weaker than the structural claim suggests. (Skip if no `oi-004-retrospective.md` present.)
   212	
   213	9. **Read-contract adherence (new in v5; paired with check 22):** For this session's work, verify: (a) the default-read surface enumeration in `read-contract.md` §1 was actually followed — every enumerated file was read at session open before any substantive work; (b) any archive-surface records relied on for load-bearing claims are cited via the `[archive: path]` convention in default-read files; (c) any non-reads of relevant archive records were declared in the session's honest-limits section with the gap they leave. Flag silent skips — these are the harness-layer laundering pattern the read-contract exists to prevent. Flag reliance on archive-surface claims without corresponding reads (the "witness-dumping" pattern WX-22-1 tracks).
   214	
   215	### Tool Location and Behavior
   216	
   217	The validation tool is located at `tools/validate.sh`. It:
   218	- Is **read-only**: it never modifies any workspace file.
   219	- Produces a **structured report** with pass/fail/warning counts for Tier 1.
   220	- Prints the **Tier 2 questions** after the Tier 1 report.
   221	- Exits with **code 0** if no Tier 1 failures, **code 1** otherwise.
   222	- Has **no dependencies** beyond standard Unix tools (bash 3.2+, grep, sed, awk) and git.
   223	
   224	### When to Run
   225	
   226	Validation should be run:
   227	
   228	- At the **start** of each session, during or immediately after the Read activity.
   229	- After the **Produce** activity, to check that new artifacts meet structural requirements.
   230	- Before the **Close** activity, as a final coherence check.
   231	
   232	### Limitations
   233	
   234	Automated structural checks verify form, not meaning. Passing all structural checks does not mean:
   235	
   236	- Specifications are correct about what they describe.
   237	- Provenance captures the actual reasoning (it may be post-hoc rationalization).
   238	- Decisions were well-considered.
   239	- The methodology is serving its purpose.
   240	- Cross-model participation is genuine rather than theatrical (see check 13's honest limit).
   241	- Declared `triggers_met:` lists match the decisions they classify (see check 14 and 15 honest limits).
   242	- Independent-claim evidence pointers (check 16) point to truthful evidence (the check verifies presence only, not truthfulness — see check 16's honest limit in `validate.sh`).
   243	- Claude-output-in-training disclosures (check 17) are truthful (the check verifies disclosure presence, not truthfulness — same operator-integrity floor as check 13).
   244	- Closure-retrospective substantive content (check 18) is well-grounded (the check verifies structural well-formedness only; substantive adequacy is Tier 2 Q8).
   245	- Participant_organisation values (check 19) reflect actual model developers (the check verifies closed-set membership, not factual provenance).
   246	- Default-read budgets (check 20) measure file size, not file relevance to the session's work. A file under the budget may still be effectively not-read; a file over the budget has failed even if its content was fully read in segments.
   247	- Archive-pack manifest integrity (check 21) verifies hash match on stored-vs-computed, not that the archive's content is what was intended or that the archive is the right artefact to preserve.
   248	- Archive-pack citation consistency (check 22) verifies path and ordinal existence, not that the cited content supports the citing claim. Tier 2 Q9 is the designed counter-pressure.
   249	
   250	These deeper questions are the purpose of Tier 2, which depends on honest assessment by the agent or human conducting the session. The methodology acknowledges that when a single AI agent both does the work and assesses it, Tier 2 is self-assessment rather than independent validation. This is a known limitation (see D-009), mitigated by making the questions explicit and recording the assessment in provenance, and further mitigated since Session 005 by the D-023 non-Claude-participation rule for meta-deliberations on self-assessment mechanisms.
   251	
   252	The immutability check (Check 10) is a basic heuristic — it detects uncommitted changes to provenance files but does not verify full immutability across git history. Comprehensive immutability verification is a potential future improvement.
   253	
   254	Check 12 verifies the presence of D-024 required keys but does not verify that the values are correct. A manifest may have all required keys while containing nonsense values; check 12 passes. The boundary between key-presence and value-correctness is a deliberate archival choice (the Archivist's Q3 position in Session 005: "the check succeeds if a field literally contains the string `unknown`, because D-024 explicitly admits `unknown` as a truthful value").
   255	
   256	Check 13 is **consistency-of-self-report**, not **truthfulness-of-self-report**, as documented above. The Tier 2 Q6 is the methodology's designed complement. Passing check 13 *and* the operator answering Q6 with concrete evidence is stronger than either alone; neither is a truth certificate.
   257	
   258	Checks 14 and 15 are **consistency between self-declared triggers and session artefacts**, not **truthfulness of the trigger declaration itself**, as documented above. The Tier 2 Q7 is the methodology's designed complement. Passing checks 14 and 15 *and* the operator answering Q7 with a substantive per-decision plausibility check is stronger than either alone. Check 14's gating rule (session ≥ 006) means the check does not apply to pre-adoption sessions; the immutability-preserving alternative for retrospective trigger classification is a separate artefact (D-039's retrospective-artefact pattern), not a retroactive rewrite.
   259	
   260	## Validation
   261	
   262	To validate this specification:
   263	
   264	1. Run `tools/validate.sh` and verify it performs the twenty-two structural checks listed in the table above.
   265	2. Verify the tool prints the nine guided questions listed above.
   266	3. Compare the tool's actual checks against the table in this specification — they should match.
   267	4. Verify the tool is read-only (it makes no changes to any file).
   268	5. Verify the tool exits with code 0 when all fail-severity checks pass, and code 1 otherwise.
   269	6. Verify that check 13's honest-limit language appears in `tools/validate.sh` (comment block above check 13), in check 13's failure message, and in this specification's "Check 13's Honest Limit" subsection. Any divergence is a specification violation.
   270	7. Verify that check 13 reports `BLOCKED` (not `FAIL` and not `PASS`) for sessions where check 12 failed.
   271	8. Verify that check 14's honest-limit language appears in `tools/validate.sh` (comment block above check 14), in check 14's failure message, and in this specification's "Check 14's Honest Limit" subsection. Any divergence is a specification violation.
   272	9. Verify that check 15's honest-limit language appears in `tools/validate.sh` (comment block above check 15), in check 15's failure message, and in this specification's "Check 15's Honest Limit" subsection. Any divergence is a specification violation.
   273	10. Verify that check 14 reports `BLOCKED` for sessions where check 11 failed and check 15 reports `BLOCKED` for sessions where check 12 failed.
   274	11. Verify that checks 14 and 15 apply only to sessions numbered ≥ 006 (the `TRIGGERS_MET_ADOPTION_SESSION` constant in `validate.sh`).
   275	8. Verify that check 11 applies only to sessions with at least one `*-perspective-*.md` file, check 12 applies only to sessions with a `manifests/` subdirectory, and check 13 applies only to sessions that declare `cross_model: true`.

 succeeded in 0ms:
     1	---
     2	title: Multi-Agent Deliberation
     3	version: 4
     4	status: active
     5	created: 2026-04-17
     6	last-updated: 2026-04-22
     7	updated-by-session: 021
     8	supersedes: multi-agent-deliberation-v3.md
     9	---
    10	
    11	# Multi-Agent Deliberation
    12	
    13	## Purpose
    14	
    15	This specification defines how the methodology instantiates genuine multi-perspective deliberation. It describes when multi-agent deliberation is required, how perspectives are convened, how stance briefs are structured, how their outputs are synthesized, how the whole process is recorded, and what limitations remain. It serves the methodology's explicit injunction against single-perspective substantive work, and partially addresses Open Issue OI-004 (genuinely independent perspectives).
    16	
    17	This specification applies equally to the self-development application and to external-problem applications of the Selvedge engine. Triggers, shapes, schemas, and conventions defined here are engine-level and do not vary by application kind (per D-074, Session 017).
    18	
    19	The term "multi-agent deliberation" describes a property, not a mechanism: that the perspectives reasoning about a question arrive at their positions without seeing each other's positions. The current implementations realise this property via parallel context-isolated subagents of the Claude model family, optionally augmented by non-Claude participants (human reviewers or non-Anthropic models) following the Non-Claude Participation mechanism below. Future implementations may extend this further via different-model agents accessed through their own endpoints, persistent personas, or asynchronous cross-session deliberation; the specification is written so those extensions are changes of mechanism, not of pattern.
    20	
    21	Version 4 adds the OI-004 criterion-4 articulation (`### Criterion-4 Articulation for OI-004`), the acceptable-participant-kinds enumeration (`### Acceptable Participant Kinds for OI-004`), six new Layer 2 manifest fields (`participant_organisation`, `claude_output_in_training`, `training_lineage_evidence_pointer`, `aggregator_intermediary`, `selection_relationship_to_operator`, `independence_basis`), one new synthesis frontmatter field (`oi004_qualifying_participants`), one new session-level participants.yaml block (`mechanical_cross_family_invocation:`), the four-state OI-004 lifecycle, and the closure procedure (operationalised by `validate.sh` checks 16-19 and `validation-approach.md` v4 Tier 2 Q8). It supersedes v3 (`multi-agent-deliberation-v3.md`). Adopted Session 021 per D-082; engine-v1 → engine-v2 bump declared in `engine-manifest.md` §2 + §7.
    22	
    23	Version 3 added the Trigger-Coverage Annotation Schema (`triggers_met:` + `triggers_rationale:` per-decision) and the associated session-number gating rule, operationalising v2 Validation items 1 and 2 as `validate.sh` checks 14 and 15. It superseded v2 (`multi-agent-deliberation-v2.md`).
    24	
    25	Version 2 added the Non-Claude Participation mechanism, the three-layer heterogeneous-participant recording schema, and associated trigger rules. It superseded v1 (`multi-agent-deliberation-v1.md`).
    26	
    27	## Specification
    28	
    29	### When Multi-Agent Deliberation Is Required
    30	
    31	A session must convene a multi-agent deliberation for any decision where at least one of the following is true:
    32	
    33	1. The decision modifies `methodology-kernel.md`.
    34	2. The decision creates or substantively revises any specification in `specifications/`.
    35	3. The question is one on which reasonable practitioners could genuinely disagree — operationalised as: the session author can name at least two plausible positions before the deliberation begins.
    36	4. The session author has marked the decision load-bearing for any other reason and records why.
    37	
    38	For any decision that meets at least one of these triggers but is made by a single agent anyway, the decision record must state this explicitly, naming the reason (e.g., "Single-perspective; non-load-bearing: minor correction per D-014 precedent"). Unstated single-perspective decisions on triggered questions are a specification violation.
    39	
    40	Decisions that meet none of the triggers — typos, reordering, routine execution of already-decided plans — may be made by a single agent without annotation.
    41	
    42	### When Non-Claude Participation Is Required
    43	
    44	Distinct from the requirement to convene multi-agent deliberation at all, this specification governs when at least one participant must come from outside the Claude model family (human reviewer, non-Anthropic model, or both).
    45	
    46	Non-Claude participation is **required** for any deliberation whose decision falls in one of the following categories:
    47	
    48	1. Modifies `methodology-kernel.md`.
    49	2. Creates or substantively revises `multi-agent-deliberation.md`.
    50	3. Creates or substantively revises `validation-approach.md` in ways that touch semantic (Tier 2) validation.
    51	4. Asserts a change in the state of OI-004.
    52	
    53	Non-Claude participation is **recommended** for other decisions that meet the multi-agent triggers above.
    54	
    55	Non-Claude participation is **optional** for all other decisions.
    56	
    57	**Opt-out.** A session may make a required-trigger decision without a non-Claude participant, but must record in the decision:
    58	
    59	- `non_claude_participation: skipped`
    60	- A reason. Acceptable reasons: "no non-Claude participant available within session timebox"; "mechanism designer exempt" (the first-use bootstrap exemption, see below); "subject matter does not plausibly expose Claude-family blind spots" (must be argued in the decision record, not asserted).
    61	- `retry_in_session: NNN` — the session number where the missing non-Claude participation will be added.
    62	
    63	Unstated skips on required-trigger decisions are a specification violation.
    64	
    65	**Bootstrap exemption (one-time).** Session 004, which established these rules, was exempt because the rules did not exist when it began. Future sessions revising this mechanism do not share the exemption.
    66	
    67	### Trigger-Coverage Annotation Schema
    68	
    69	Added in v3 (Session 006) to make trigger coverage machine-verifiable by `tools/validate.sh` checks 14 and 15. The schema is prospective-only from Session 006; pre-adoption decisions (D-001 through D-036) are out-of-scope.
    70	
    71	**Field: `triggers_met:`.** A flat list of trigger identifiers that the decision meets.
    72	
    73	- Identifier format: lowercase-underscore, `d016_N` or `d023_N` where `N` is the clause number within the current D-016 or D-023 ruleset.
    74	- Current allowed values (as of v3): `d016_1`, `d016_2`, `d016_3`, `d016_4`, `d023_1`, `d023_2`, `d023_3`, `d023_4`.
    75	- Empty-state token: `triggers_met: [none]`. YAML-standard `triggers_met: []` is explicitly **not** valid — `[none]` is required as a positive author assertion. The convention is chosen to make it harder to silence the field accidentally.
    76	- Absence semantics: in a post-adoption session (≥006), absence of `triggers_met:` is a validation failure. In a pre-adoption session (<006), absence is expected and out-of-scope for checks 14 and 15.
    77	
    78	**Field: `triggers_rationale:`.** A required prose sibling providing a one-to-two-sentence explanation of why each listed trigger applies (or why none apply for `[none]`).
    79	
    80	- Purpose: adversarial visibility. A decades-later reviewer can audit whether the `triggers_met:` list aligns with the decision's content.
    81	- The checks do not parse `triggers_rationale:`; it is archival and adversarial content, not structural.
    82	- It is nevertheless a required field — a decision record with `triggers_met:` but no `triggers_rationale:` is malformed.
    83	
    84	**Placement.** Per-decision inline, directly under the decision's `## D-NNN:` heading, using the bolded-key format that matches existing decision-record idiom:
    85	
    86	```markdown
    87	## D-NNN: [Title]
    88	
    89	**Triggers met:** [d016_2, d016_3]
    90	
    91	**Triggers rationale:** One-to-two-sentence explanation of why each listed trigger applies.
    92	
    93	**Decision:** ...
    94	```
    95	
    96	The validator parses `**Triggers met:**` lines with a line-anchored regex; the bracketed list is extracted with a simple sed/awk expression. Multi-document YAML is not used.
    97	
    98	**Future rule additions.** The identifier namespace is append-only. A new D-NNN that introduces a trigger reserves fresh identifiers (e.g., `d040_1`). Existing records are not rewritten — their `triggers_met:` stays accurate as of their authoring. The validator's recognized-identifier set must be updated in the same session that introduces new identifiers.
    99	
   100	**Retroactivity.** No backfill of D-001 through D-036. The immutability rule (D-017; workspace-structure §provenance) is honored. `tools/validate.sh` gates checks 14 and 15 on session number ≥6 via an explicit `TRIGGERS_MET_ADOPTION_SESSION=6` constant (see `validation-approach.md` v3 Gating Conventions). If a future session needs historical trigger classification, that is a distinct session's job producing a new artefact (e.g., `reclassification.md`) that references pre-adoption decisions without editing them.
   101	
   102	**Complementary annotations.** Two additional decision-level annotations support the rules:
   103	
   104	- `**Single-agent reason:**` — a bolded-key line on any decision that declares a `d016_*` trigger but was made single-agent anyway. Required for check 14 to pass in that case.
   105	- `**Non-Claude participation:**` — a bolded-key line on any decision that declares a `d023_*` trigger but was made without non-Claude participation. Must include a `reason:` sub-field and a `retry_in_session:` sub-field. Required for check 15 to pass in that case.
   106	
   107	Both annotations are prose-plus-structured-fields; see `validation-approach.md` v3 for parse details.
   108	
   109	### Perspectives
   110	
   111	- **Number.** Default three. Up to five when the problem spans clearly different concern-domains. More than five requires a written justification recorded at convening time.
   112	- **Selection.** Perspectives are chosen for expected disagreement on *this* problem. There is no permanent roster. Reaffirms D-005.
   113	- **Adversarial requirement.** At least one perspective must be adversarial — its job is to challenge the emerging consensus and argue against the proposal. Reaffirms the methodology-kernel rule.
   114	- **Naming.** Each perspective has a short name (e.g., "The Pragmatist," "The Archivist") used consistently throughout briefs, raw outputs, synthesis, and decision records.
   115	
   116	### Stance Briefs
   117	
   118	Each perspective receives a stance brief before the independent phase begins. Every brief in a single deliberation has the same structure, in this order:
   119	
   120	1. **Methodology context** — shared, byte-identical across all briefs in the deliberation. A concise description of what the methodology is and its current state.
   121	2. **Problem statement** — shared, byte-identical. What question the deliberation is answering.
   122	3. **Design questions** — shared, byte-identical. The specific questions each perspective is asked to address.
   123	4. **Role-specific stance** — the only section that varies between briefs. Second person, imperative, naming the specific concerns the perspective holds. Target length 150–300 words.
   124	5. **Response format** — shared. What structure the response should take, length target, constraints on output.
   125	6. **Constraint on external imports** — shared. A reminder to reason primarily from the brief and to flag pretrained ideas as external inputs rather than committing them directly (per the PROMPT.md rule).
   126	
   127	Diffing two briefs from the same deliberation should reveal only the role-specific stance. This makes deliberations reproducible.
   128	
   129	**Workspace context per perspective.** Minimal and identical. Perspectives reason from the brief; they do not read workspace files or use other tools during the independent phase. This keeps the deliberation reproducible and prevents spurious disagreement from divergent reading. A future version may specify differentiated context per perspective (see Open Extensions below); until then, uniform minimal context is the rule.
   130	
   131	**Brief immutability.** Briefs are committed to the workspace (or otherwise preserved) before any perspective is launched. Briefs are not edited during the deliberation. The commit hash or equivalent timestamp at brief-finalisation is the deliberation's anchor.
   132	
   133	### Non-Claude Participation Mechanism
   134	
   135	A non-Claude participant joins a multi-agent deliberation in one of two shapes:
   136	
   137	**Shape A — Participant as perspective.** The non-Claude participant is treated as a perspective indistinguishable in role from the Claude perspectives:
   138	
   139	1. A brief is written following the Stance Briefs section above and committed before the participant sees it.
   140	2. The brief is delivered to the participant by whatever channel is available: for a human, a text editor; for a non-Anthropic model, a web UI paste or a CLI invocation from the workspace.
   141	3. The returned response is committed **verbatim** as a raw-output file at the session's provenance root (flat layout) or under `deliberations/<decision-id>/responses/` (subdirectory layout) with the same naming convention as Claude raw outputs.
   142	4. If the participant cannot respond synchronously, the session writes `provenance/NNN/STATUS.md` naming the awaited participant and **halts**. Synthesis does not proceed until the awaited response is committed.
   143	
   144	**Shape B — Participant as reviewer.** The non-Claude participant is a named auditor at synthesis-time:
   145	
   146	1. Claude raw outputs are committed as normal.
   147	2. Before the synthesizer runs, a named human reviewer (not the session operator) reads the raw outputs and writes `provenance/NNN/human-review.md` containing: the review's frontmatter (identity, relationship-to-operator, time-spent), a prose record of what was flagged, and the explicit field `reviewer_changed_synthesis: true | false`.
   148	3. The synthesizer reads `human-review.md` as an input alongside the raw perspective outputs.
   149	4. A reviewer is not a deliberator: they see the Claude outputs in raw form and their job is to flag what a Claude-only synthesis would likely miss.
   150	
   151	Shapes A and B may be used separately or in combination in the same deliberation, provided the manifest declares each participant's shape.
   152	
   153	**Transport guarantee.** The workspace guarantees the **record** (committed brief, verbatim response, attributable participant), not the **generation** (which depends on channels the workspace cannot automate). Convener fidelity to verbatim reproduction is a required property; attempts to automate faithfulness are a future direction, not a day-one requirement.
   154	
   155	### Heterogeneous-Participant Recording Schema
   156	
   157	Heterogeneous-participant deliberations record identity across three layers.
   158	
   159	**Layer 1 — Raw-output file frontmatter (minimal).** Required fields: `session`, `title`, `date`, `status`, `perspective`, `committed_at`. The response body is the payload; no identity, version, or transport fields appear here.
   160	
   161	**Layer 2 — Per-participant manifest.** One YAML file per participant at `provenance/NNN/manifests/<perspective>.manifest.yaml`. Required fields:
   162	
   163	```yaml
   164	perspective: <role name>
   165	participant_kind: claude-subagent | anthropic-other | non-anthropic-model | human | unknown
   166	participant_identity: <free text, canonicalized>
   167	model_family: <string or "unknown">
   168	model_id: <string or "n/a" for human or "unknown">
   169	model_version: <string or "unknown">
   170	provider: <anthropic | openai | google | local | human | unknown>
   171	endpoint: <string or "web-ui" | "in-person" | "unknown">
   172	invocation_method: <agent-tool | cli-wrapper | copy-paste | written-by-hand | unknown>
   173	sampling:
   174	  temperature: <value or "unknown">
   175	  top_p: <value or "unknown">
   176	  max_tokens: <value or "unknown">
   177	training_lineage_overlap_with_claude: known-overlap | unknown | independent-claim
   178	participant_selected_by: <operator identity>
   179	participant_selection_method: self | solicited-from-graph | solicited-externally | pre-registered
   180	identity_known: true | false | partial
   181	context_source: <path to brief, or "verbal" for humans>
   182	delivered_at: <ISO-8601 or "unknown">
   183	received_at: <ISO-8601 or "unknown">
   184	raw_response_file: <path>
   185	transport_notes: <free text>
   186	output_edited_after_submission: true | false
   187	participation_shape: perspective | reviewer
   188	```
   189	
   190	**Layer 2 fields added in v4 (D-082, Session 021)** — for OI-004 criterion-4 enforcement; see §Criterion-4 Articulation for OI-004 below for normative use:
   191	
   192	```yaml
   193	participant_organisation: <organisation-name from closed set>  # required when participant_kind: non-anthropic-model. Closed set enumerated in tools/validate.sh PARTICIPANT_ORGANISATION_CLOSED_SET; extensible by named decision per validation-approach.md v4 §Closed-set extension discipline. Operationalised by check 19.
   194	claude_output_in_training: known-yes | known-no | unknown | n/a  # required when participant_kind in {non-anthropic-model, human}; n/a permitted for human. Out-of-scope for {claude-subagent, anthropic-other}. Operationalised by check 17. The `unknown` value is signal per the Unknown-field rule and surfaces to Tier 2 Q8 review.
   195	training_lineage_evidence_pointer: <provenance-relative path | URL | "unknown-but-asserted">  # required when training_lineage_overlap_with_claude: independent-claim. Operationalised by check 16. The pointer must resolve to: a model card or training-data card published by the provider (URL); a provider-public statement on Claude-distillation policy (URL); a workspace-internal note explaining what evidence the operator inspected (provenance-relative path); or the literal string "unknown-but-asserted" with mandatory transport_notes explanation.
   196	aggregator_intermediary: <string or "n/a">  # required when access via aggregator (e.g., OpenRouter); names the aggregator. "n/a" for direct provider access.
   197	selection_relationship_to_operator: <free-text or "n/a">  # required when participant_kind: human. Records relationship-to-operator and selection method context per the OI-004 criterion-4 articulation human-branch requirement.
   198	independence_basis: organization-distinct | local-open-weights | human-selection-distinct | mixed-panel | unknown  # required for participants claimed for OI-004 narrowing. Records the basis on which the participant claims criterion-4 eligibility.
   199	```
   200	
   201	The v4 fields are required from session 021 onward for participants claimed for OI-004 narrowing; pre-adoption sessions (001-020) are out-of-scope per the immutability rule (D-017) and per the session-number gating in `validation-approach.md` v4.
   202	
   203	**Layer 3 — Session-level index.** `provenance/NNN/participants.yaml` (preferred) or `provenance/NNN/participants.md` listing each participant and their manifest path.
   204	
   205	**Composition fields (synthesis frontmatter).** The synthesis file's frontmatter records:
   206	
   207	```yaml
   208	participants_family: claude-only | mixed-anthropic | cross-model
   209	cross_model: true | false
   210	non_claude_participants: <integer>
   211	oi004_qualifying_participants: [<list-of-perspective-names>]  # added v4: explicit declaration of which perspectives' manifests satisfy criterion-4 articulation; empty list permitted for sessions making no OI-004-narrowing claim
   212	```
   213	
   214	**Session-level participants index extension (added v4, D-082, Session 021).** When mechanical cross-family invocation occurs outside the perspective-deliberation frame (e.g., the Session 018 contamination-canary pattern), it is recorded as a separate top-level block in `provenance/NNN/participants.yaml`:
   215	
   216	```yaml
   217	mechanical_cross_family_invocation:
   218	  - purpose: <free text, e.g. "C3 5-gram overlap test", "L1 contamination canary">
   219	    invoked_model: <model id>
   220	    provider: <provider id>
   221	    invocation_method: <cli-wrapper | api | other>
   222	    decision_shaped: <D-NNN id or "none">
   223	    evidence_pointer: <provenance-relative path>
   224	```
   225	
   226	This block records mechanical cross-family invocation as corroborating evidence for criterion 3 of OI-004 (recorded impact on outcomes); it is **not** a participant kind for criterion 4 (per §Acceptable Participant Kinds for OI-004 below). The block is optional; absence is permitted (most sessions will not record mechanical invocation).
   227	
   228	`participants_family: mixed-anthropic` is the value for intra-Claude-family size-mixing (Opus + Sonnet + Haiku, any combination) — this **is not** cross-model participation (see the Claude-Only-Is-Not-Cross-Model rule below). `cross_model: true` requires at least one participant with `training_lineage_overlap_with_claude` other than `known-overlap`.
   229	
   230	**Unknown-field rule.** Unknown values are recorded as the literal string `unknown`. Empty strings are forbidden. Missing required fields are a schema violation. `identity_known: partial` requires a `transport_notes` entry explaining what is and is not recorded. The literal `unknown` is signal — it says "this session could not determine the value" and is itself auditable.
   231	
   232	**Claude-Only-Is-Not-Cross-Model.** A deliberation whose participants are all members of the Claude model family (any mix of Opus, Sonnet, Haiku; any sizes; any post-training runs) does not constitute cross-model participation for OI-004 purposes. The manifest must record `participants_family: claude-only` (or `mixed-anthropic` for explicit size-mixing) and `cross_model: false`. Intra-family size-mixing may be recorded for separate reasons (see OI-011) but contributes nothing to OI-004.
   233	
   234	### Mechanism
   235	
   236	The required property is **independence-preservation during the independent phase**: no perspective's output can influence another perspective's reasoning while each is forming its position.
   237	
   238	The Claude-subagent implementation realises this via parallel subagents launched through Claude Code's Agent tool, each in an isolated context. Non-Claude participation realises it through the brief-drop pattern and halt-before-synthesis described above — the non-Claude participant reasons from the committed brief without access to Claude perspectives' outputs during the independent phase.
   239	
   240	The specification does not mandate any single mechanism. Alternative realisations that preserve the required property — different-model agents accessed via their own endpoints, persistent human reviewers briefed separately, asynchronous cross-session deliberations with explicit quarantine — are consistent with this specification.
   241	
   242	### Synthesis
   243	
   244	After all perspectives (Claude and non-Claude) have returned their raw outputs, a synthesis step produces a single deliberation record.
   245	
   246	- **Synthesizer identity.** The synthesizer must not have been one of the deliberation's perspectives. The synthesizer's identity (agent/model/date) is recorded in the synthesis file's frontmatter.
   247	- **Reviewer input.** If the deliberation includes a reviewer-shape non-Claude participant, the synthesizer reads `human-review.md` alongside the raw perspective outputs.
   248	- **Citation requirement.** Claims attributing a position to a perspective must cite the source file and section/question: `[source-file, Q#]` or `[source-file, section]`.
   249	- **Synthesizer-original claims.** Claims not directly sourced from any raw perspective are marked `[synth]`. This lets future readers compute the ratio of sourced to synthesised content and judge faithfulness.
   250	- **Quote over paraphrase for load-bearing claims.** Where a perspective's argument turns on specific language, the synthesis quotes that language rather than paraphrasing.
   251	- **Preserve dissent.** Disagreements are listed as disagreements. A minority position with a strong argument is preserved as-is, not diluted. Majority/minority structure is reported explicitly.
   252	- **Convergence vs coverage.** The synthesis distinguishes *convergence* (all perspectives independently reached a similar conclusion) from *coverage* (only one perspective raised a point; others were silent). These are different epistemic states.
   253	- **Synthesis order anchoring.** Perspectives are presented to the synthesis step in alphabetical order by role name, or in a fixed order documented in the synthesis file, to reduce ordering-induced synthesizer bias.
   254	
   255	Synthesis maps; it does not decide. The Decide activity operates on the synthesis, not on raw outputs directly.
   256	
   257	### Provenance Layout
   258	
   259	Tiered by the number of deliberations in a session.
   260	

codex
I’ve got the governing clauses. I’m filling in the later MAD sections, the OI/watchpoint texts, and the validator’s current measurement so I can challenge the brief where it’s sloppy instead of inheriting its numbers.
exec
/bin/zsh -lc "nl -ba open-issues/OI-018.md | sed -n '1,240p'" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "nl -ba specifications/multi-agent-deliberation.md | sed -n '260,460p'" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "nl -ba open-issues/OI-015.md | sed -n '1,220p'" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
     1	---
     2	id: OI-018
     3	status: Open
     4	surfaced-in-session: 023
     5	---
     6	
     7	### OI-018: Revisit engine-manifest.md §5 bump-trigger criteria in light of §5.4 cadence minority activation
     8	**Surfaced:** Session 023
     9	**Status:** Open — deferred to Session 024+; activation trigger-gated
    10	
    11	**Opened:** Session 023 D-086 R7 (per Skeptic [01c Q5] + Outsider [01d Q5] shared recommendation).
    12	
    13	**Context.** Session 022 §5.4 Skeptic engine-version-cadence minority activated at Session 023 engine-v3 → engine-v4 adoption per D-086 R9. The warrant text, preserved in `provenance/022-workspace-scaling-trajectory/01-deliberation.md` §5 per D-084:
    14	
    15	> Activation warrant: three engine-v-bumps in four adjacent sessions OR external-application portability confusion.
    16	
    17	First disjunct satisfied at Session 023 engine-v4 adoption:
    18	- engine-v1 → engine-v2: Session 021 (D-082)
    19	- engine-v2 → engine-v3: Session 022 (D-084)
    20	- engine-v3 → engine-v4: Session 023 (D-086)
    21	
    22	Three bumps in three adjacent sessions (also three in four if counting from engine-v1 at Session 017). The §5.4 minority expressed two concerns: (i) rapid v-bumps increase external-application-portability risk (an external application pinned to engine-vN versus engine-v(N+k) has materially different rules); (ii) engine-version numbers become "change-log timestamps" rather than meaningful version artefacts if bumps are too frequent.
    23	
    24	**Scope of the deliberation (Session 024+).**
    25	
    26	1. **Whether engine-manifest §5 bump-trigger criteria are too permissive.** Current criteria: any substantive revision to any engine-definition file triggers a bump. Alternative criteria to consider:
    27	   - Bundle-trigger: multiple substantive revisions within a session counted as one bump.
    28	   - Threshold-trigger: bump required only when cumulative substantive changes pass a na