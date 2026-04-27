---
title: Validation Approach
version: 5
status: superseded
created: 2026-04-17
last-updated: 2026-04-23
updated-by-session: 024
supersedes: validation-approach-v4.md
superseded-by: validation-approach.md (v6)
superseded-in-session: 063
---

# Validation Approach

## Purpose

This specification defines how the methodology validates itself: what is checked, how checks are organized, and what the checks can and cannot assure. It serves the methodology's self-hosting principle — a methodology that cannot verify its own specifications cannot evolve reliably.

**Scope note (added as a minor correction in Session 009 per D-056).** This specification covers **Workspace validation** as defined in `methodology-kernel.md` v2 §7. **Domain validation** (the second sense of §7, concerning whether an external artefact functions in its target domain) is performed by domain-actors outside this specification's Tier 1 / Tier 2 scope and is not automated by `tools/validate.sh`. Its governance lives in the kernel §7 text itself.

**Scope note (added as a minor correction in Session 017 per D-074).** The Tier 1 structural checks and Tier 2 guided-assessment questions defined in this specification apply equally to the self-development application and to external-problem applications of the Selvedge engine. Validation is engine-level; the specific artefacts checked (and the appropriate domain-validation pathway) vary by application kind, but the two-tier discipline is invariant.

Version 5 adds three new Tier 1 checks (20, 21, 22) operationalising the read-contract in `specifications/read-contract.md` v1 (D-084, Session 022), and one new Tier 2 question (Q9) addressing read-contract adherence. It specifies gating, severity, and sequencing rules for the new checks. It supersedes v4 (`validation-approach-v4.md`).

Version 4 adds four new Tier 1 checks (16, 17, 18, 19) operationalising the OI-004 criterion-4 articulation in `multi-agent-deliberation.md` v4 (D-082, Session 021), and one new Tier 2 question (Q8) paired with check 18's honest limit. It specifies gating, severity, and sequencing rules for the new checks. It superseded v3 (`validation-approach-v3.md`).

Version 3 added two new Tier 1 checks (14, 15) that operationalised v2 `multi-agent-deliberation.md` Validation items 1 and 2 (now v3+ Validation items), and one new Tier 2 question (Q7) paired with checks 14/15's honest limits. It specified gating, severity, and sequencing rules for those checks. It superseded v2 (`validation-approach-v2.md`).

Version 2 added three new Tier 1 checks (11, 12, 13) that enforce the D-024 heterogeneous-participant schema introduced by `multi-agent-deliberation.md` v2, and one new Tier 2 question paired with check 13's honest limit. It superseded v1 (`validation-approach-v1.md`).

## Specification

### Two-Tier Model

Validation has two tiers, reflecting the distinction between properties that can be checked mechanically and those that require judgment.

**Tier 1: Structural Checks** are automated checks run by `tools/validate.sh`. They verify that the workspace's files conform to the formats and conventions defined in other specifications. Structural checks are necessary but not sufficient for methodology health — a workspace can pass all structural checks while its specifications are semantically wrong or its provenance is misleading.

**Tier 2: Guided Assessment** is a set of questions printed by the validation tool for the agent or human conducting the session to consider. These questions address properties that cannot be checked mechanically: semantic consistency, provenance usefulness, and whether the methodology is making genuine progress.

### Tier 1: Structural Checks

The following checks are automated:

| # | Check | Source Spec | Severity | Gate |
|---|-------|-------------|----------|------|
| 1 | Required top-level files exist (PROMPT.md, SESSION-LOG.md, open-issues.md) | workspace-structure | Fail | unconditional |
| 2 | Required directories exist (specifications/, provenance/) | workspace-structure | Fail | unconditional |
| 3 | Each specification has YAML frontmatter with required fields (title, version, status, created, last-updated, supersedes) | workspace-structure | Fail | unconditional |
| 4 | Each specification has three required section headings (Purpose, Specification, Validation) | workspace-structure | Fail | unconditional |
| 5 | Provenance directories follow NNN-title naming convention | workspace-structure | Fail | unconditional |
| 6 | Session log has an entry for each provenance directory | workspace-structure | Fail | unconditional |
| 7 | Each provenance directory contains at least one .md file | methodology-kernel | Fail | unconditional |
| 8 | Provenance files have YAML frontmatter with required fields (session, title, date, status) | workspace-structure | Fail | unconditional |
| 9 | Decision records include rejected alternatives sections | methodology-kernel | Warning | unconditional |
| 10 | No uncommitted changes to provenance files (basic immutability heuristic) | workspace-structure | Warning | unconditional |
| 11 | Multi-agent three-raw-output floor: ≥3 files matching `*-perspective-*.md` | multi-agent-deliberation (v2 Validation #3) | Fail | session has ≥1 `*-perspective-*.md` file |
| 12 | Heterogeneous-participant schema well-formedness: each `manifests/*.manifest.yaml` has all D-024 required fields as literal keys | multi-agent-deliberation (v2 Validation #8) | Fail | session has `manifests/` subdirectory |
| 13 | Cross-model-claim honesty: `cross_model: true` implies ≥1 manifest with `training_lineage_overlap_with_claude` other than `known-overlap` OR `participant_kind: human` | multi-agent-deliberation (v2 Validation #9) | Fail | session declares `cross_model: true` AND check 12 passed for that session |
| 14 | Multi-agent trigger coverage: decision declares any `d016_*` trigger implies ≥3 raw perspective files plus synthesis OR `**Single-agent reason:**` annotation on the decision | multi-agent-deliberation (v3 Validation #1 operationalised) | Fail | session ≥ 006 AND session has ≥1 decision record with `**Triggers met:**` line |
| 15 | Non-Claude trigger coverage: decision declares any `d023_*` trigger implies ≥1 manifest with `participant_kind` outside `{claude-subagent, anthropic-other}` OR `**Non-Claude participation:**` skip annotation with `reason:` and `retry_in_session:` sub-fields | multi-agent-deliberation (v3 Validation #2 operationalised) | Fail | session ≥ 006 AND check 12 passed for that session |
| 16 | Independent-claim evidence-pointer presence: each manifest with `training_lineage_overlap_with_claude: independent-claim` has non-empty `training_lineage_evidence_pointer:` field | multi-agent-deliberation v4 §Heterogeneous-Participant Recording Schema | Fail | session ≥ 021 |
| 17 | Claude-output-in-training disclosure: each manifest with `participant_kind` in `{non-anthropic-model, human}` has a `claude_output_in_training:` field whose value is in `{known-yes, known-no, unknown, n/a}` | multi-agent-deliberation v4 §Heterogeneous-Participant Recording Schema | Fail | session ≥ 021 |
| 18 | OI-004 closure-retrospective well-formedness: any `provenance/*/oi-004-retrospective.md` artefact contains the three required sections `## Qualifying Deliberations Table`, `## Summary Tally`, `## P4 Assertion` | multi-agent-deliberation v4 §Closure Procedure for OI-004 | Fail | presence of `oi-004-retrospective.md` artefact |
| 19 | Non-Anthropic participant_organisation closed-set membership: each manifest with `participant_kind: non-anthropic-model` has non-empty `participant_organisation:` field whose value is in the spec-enumerated closed set | multi-agent-deliberation v4 §Acceptable Participant Kinds for OI-004 | Fail | session ≥ 021 |
| 20 | Default-read surface per-file budget: every file in `read-contract.md` §1 default-read enumeration has body-word-count ≤ `DEFAULT_READ_HARD_WORD_CEILING` (Fail) or ≤ `DEFAULT_READ_SOFT_WORD_CEILING` (Warn) | read-contract §2 | Fail/Warn | session ≥ 022 |
| 21 | Archive-pack manifest integrity: every `provenance/*/archive/*/manifest.yaml` has required keys and the stored `source_hash_sha256` matches actual hash of concatenated chunks in ordinal order | read-contract §7 | Fail | presence of any `archive/` subdirectory under `provenance/*/` |
| 22 | Archive-pack citation consistency: every `[archive: path]` reference in a default-read surface file resolves to an existing archive-pack path; chunk ordinals named in the reference exist in the manifest | read-contract §6 | Fail | presence of any `archive/` subdirectory under `provenance/*/` |

Checks marked **Fail** cause the tool to exit with a non-zero code. Checks marked **Warning** are reported but do not cause failure.

### Gating Conventions (checks 11, 12, 13)

**Presence-gating.** Checks 11, 12, and 13 apply only to sessions whose provenance exhibits the relevant artefact. A session without any `*-perspective-*.md` files is not a multi-agent session and is out-of-scope for check 11. A session without a `manifests/` subdirectory has not adopted the D-024 schema and is out-of-scope for check 12 (and by extension, check 13). Out-of-scope sessions produce no output from the gated check — no warning, no failure.

**Consequence for prior sessions.** Sessions 001 (Genesis) and 002 (Self-Validation) are not multi-agent; they are out-of-scope for all three new checks. Session 003 and Session 004 are multi-agent (have perspective files) but did not produce a `manifests/` subdirectory; they are in-scope for check 11 and out-of-scope for checks 12 and 13. Session 005 and later sessions that adopt the full schema are in-scope for all three.

**Rationale for the gate granularity.** Gating at `manifests/` subdirectory presence — rather than at `participants.yaml` presence or at session-number — was chosen to (a) keep Session 004's bootstrap-exempt minimal `participants.yaml` naturally out-of-scope without requiring an inline exemption list, (b) avoid encoding a numeric session cutoff that must be maintained in the tool, and (c) produce the same outcome in practice as session-number gating (Session 005 is the first session to have a `manifests/` subdirectory). This decision is recorded in D-030 (Session 005) along with the genuine cross-model disagreement that preceded it.

### Gating Conventions (checks 14, 15) — Session-number gating

**Session-number-gating.** Checks 14 and 15 apply only to sessions numbered ≥ 006. The gate is encoded as an explicit constant `TRIGGERS_MET_ADOPTION_SESSION=6` near the top of `validate.sh` so a future reader can see the history in one line. Out-of-scope sessions (001 through 005) produce no output from these checks — no warning, no failure.

**Rationale for session-number gating here (distinct from check 12's artefact-presence gating).** Session 006 deliberated (D-039) on whether to use presence-gating (as with checks 11–13) or session-number gating for checks 14 and 15. The cross-perspective result: three of four perspectives (Archivist, Skeptic, Outsider — cross-model) converged on session-number gating; one (Implementer) preferred presence-gating. The decisive arguments were (a) ambiguity of absence under presence-gating (a missing `**Triggers met:**` line cannot be distinguished from "pre-adoption" vs "author forgot"), and (b) bypass-by-omission: presence-gating invites operators who want to avoid a check to simply omit the triggering field. Session-number gating makes absence in a post-adoption session unambiguously a failure. This is the same cross-perspective divergence pattern that Session 005 faced (D-030); the resolution here is the opposite because the failure-mode calculus differs — check 12's artefact-presence gating could not be gamed-by-omission (the `manifests/` directory is a substantive artefact, not a trivially-omittable field), whereas `**Triggers met:**` can be trivially omitted.

**Consequence for prior sessions.** Sessions 001 through 005 are out-of-scope for checks 14 and 15. Session 006 and later sessions must include `**Triggers met:**` on every decision record (with `[none]` if no triggers fired).

### Gating Conventions (checks 16, 17, 19) — Session-number gating; Check 18 — presence-gating

**Session-number-gating (checks 16, 17, 19).** Apply only to sessions numbered ≥ 021. The gate is encoded as an explicit constant `CRITERION4_ARTICULATION_SESSION=21` near the top of `validate.sh` so a future reader can see the history in one line. Out-of-scope sessions (001 through 020) produce no output from these checks — no warning, no failure.

**Rationale for session-number gating.** Checks 16, 17, 19 enforce schema fields introduced by `multi-agent-deliberation.md` v4 §Heterogeneous-Participant Recording Schema (D-082, Session 021). Pre-adoption manifests do not have these fields and cannot have them retroactively per the immutability rule (D-017). Per the Session 006 D-039 precedent for checks 14/15, session-number gating is the correct mechanism for prospective-only schema adoption. Presence-gating would create the ambiguity-of-absence problem (a missing `claude_output_in_training:` field cannot be distinguished from "pre-adoption" vs "author forgot").

**Presence-gating (check 18).** Check 18 fires only when an `oi-004-retrospective.md` file is present anywhere under `provenance/*/`. The artefact does not exist until a future session writes it; pre-existence sessions are out-of-scope. Once written, check 18 verifies structural well-formedness; substantive adequacy is Tier 2 Q8 (paired).

**Out-of-scope behaviour for participant_kind values.** Check 17 is out-of-scope for `participant_kind` in `{claude-subagent, anthropic-other}` (no Claude-output disclosure required for Claude-family participants). Check 19 is out-of-scope for `participant_kind` other than `non-anthropic-model` (organisational origin closed-set membership is required only for non-Anthropic LLM participants). These are recorded inline in the validate.sh check implementation and in the honest-limit comments.

**Closed-set extension discipline.** The PARTICIPANT_ORGANISATION_CLOSED_SET in `validate.sh` is initialised at engine-v2 with values `{anthropic, openai, google, meta, xai, mistral, deepseek, cohere, local, human-individual, other-named}`. Extending this set requires a named decision in a session's `02-decisions.md` and a same-session update to the constant. Adding a new provider is **not** a substantive revision to `multi-agent-deliberation.md` per OI-002 heuristic (the spec already permits the closed set to extend); it is a substantive update to `tools/validate.sh` per `engine-manifest.md` §5 only when the addition substantively changes what counts as criterion-4-eligible. Routine provider additions (e.g., adding `cohere` after first operational use) are treated as minor validator-data updates not triggering an engine-version bump. This convention is established Session 021 and may be revisited if it produces silent failures.

**Consequence for prior sessions.** Sessions 001 through 020 are out-of-scope for checks 16, 17, 19. Session 021 and later sessions whose manifests claim OI-004 narrowing must include the new fields per the schema in `multi-agent-deliberation.md` v4. Pre-adoption sessions retain their original manifests unchanged.

### Gating Conventions (checks 20, 21, 22) — Session-number and presence-gating

**Session-number-gating (check 20).** Check 20 applies only to sessions numbered ≥ 022 (the session that adopted `specifications/read-contract.md` v1). The gate is encoded as an explicit constant `READ_CONTRACT_ADOPTION_SESSION=22` near the top of `validate.sh`. Out-of-scope sessions (001 through 021) produce no output from check 20 — pre-adoption SESSION-LOG.md / open-issues.md sizes are preserved as-is until the R8a / R8b migrations complete in Session 022.

**Presence-gating (checks 21, 22).** Checks 21 and 22 fire only when at least one `provenance/*/archive/*/` directory exists. The archive-pack infrastructure does not exist until Session 022 creates the first archive-pack (Session 014 Outsider retroactive migration per R8c); pre-existence sessions are out-of-scope.

**Rationale for mixed gating.** Check 20 measures default-read surface files that exist prospectively from the adoption session onward. Checks 21 and 22 measure archive-packs that exist only when created; presence-gating is the correct mechanism per Session 005 D-030 precedent.

**Budget constants.** Encoded near the top of `validate.sh`:

```
DEFAULT_READ_HARD_WORD_CEILING=8000
DEFAULT_READ_SOFT_WORD_CEILING=6000
READ_CONTRACT_ADOPTION_SESSION=22
```

Any revision to these constants is a substantive revision to `tools/validate.sh` per `engine-manifest.md` §5 and requires an engine-version bump.

**Measurement.** Check 20 measures word count via `wc -w` on body content after the closing YAML frontmatter delimiter. Frontmatter and the three-dash delimiters themselves are excluded.

**Default-read surface detection.** The validator maintains a canonical default-read file-set derived from `read-contract.md` §1. The implementation uses a glob-based helper (not filename heuristics) reading the §1 enumeration patterns:
- `specifications/*.md` where frontmatter `status: active` (not `superseded`, `draft`, or `deprecated`).
- `PROMPT.md`, `prompts/development.md`, `prompts/application.md`.
- `SESSION-LOG.md`.
- `open-issues/index.md`.
- `provenance/*/03-close.md`.
- Files in the currently-active session's provenance directory (only the most recent NNN- directory containing an un-closed `03-close.md` or no `03-close.md` at all).

Archive-pack files and superseded-status specifications are excluded from check 20 scope.

### Sequencing (check 13 after check 12; check 14 after check 11; check 15 after check 12)

Check 13 depends on well-formed manifests. If check 12 fails for a given session, check 13 reports `BLOCKED: check 12 failed for this session; cannot evaluate check 13` for that session and does not itself fail or warn. This prevents double-reporting of a single underlying problem and keeps the tool honest about what it actually evaluated.

Check 14 depends on the three-raw-output floor established by check 11. If check 11 fails for a given session (fewer than three perspective files when multi-agent artefacts are asserted), check 14 reports `BLOCKED: check 11 failed for this session; cannot evaluate check 14`. Check 14 does **not** depend on check 12: it inspects perspective-file presence, not manifest content (per D-040, the Outsider's precision argument).

Check 15 depends on well-formed manifests. If check 12 fails for a given session, check 15 reports `BLOCKED: check 12 failed for this session; cannot evaluate check 15`. Check 15 is independent of check 14 (a decision can fail 15 while passing 14 or vice versa).

### Check 13's Honest Limit (mandatory inline documentation)

Check 13 enforces **consistency of self-report**, not **truthfulness of self-report**. This limit is mandatory content in three locations:

1. A comment block in `tools/validate.sh` directly above check 13's implementation.
2. Check 13's failure message (as an inline NOTE).
3. This specification (above).

The language to preserve verbatim:

> This check verifies the session's claim is internally consistent with its manifests. It does not and cannot verify that the manifests' lineage claims are themselves true. Manifest truth relies on operator integrity and the `participant_selected_by` field's accountability.

**Known gaming modes** (recorded in D-029 and preserved for future maintainers):

- **Value-flipping.** An operator edits `training_lineage_overlap_with_claude` in the manifest of a Claude subagent from `known-overlap` to `independent-claim`; the check passes.
- **`unknown` laundering.** An operator sets one participant's lineage field to `unknown` (a valid value) when the true value is `known-overlap`; the check passes.
- **Paper-human classification.** An operator records a nominal human participant who did not substantively participate; the check passes because `participant_kind: human` bypasses the lineage-value check.
- **Wrapper impersonation.** An operator routes a Claude call through a wrapper that looks like a non-Claude CLI and lies in the `provider` field; the check cannot distinguish this from a genuine non-Claude invocation.

These gaming modes are not fixed by check 13 alone. The Tier 2 question paired with check 13 (see below) is the methodology's designed counter-pressure to laundering by self-report.

### Check 14's Honest Limit (mandatory inline documentation)

Check 14 enforces **consistency between a decision's self-declared triggers and the session's multi-agent artefacts**, not **truthfulness of the declaration itself**. This limit is mandatory content in three locations:

1. A comment block in `tools/validate.sh` directly above check 14's implementation.
2. Check 14's failure message (as an inline NOTE).
3. This specification (above).

The language to preserve verbatim:

> This check verifies consistency between a decision's self-declared `triggers_met:` and the session's multi-agent artefacts. It does not and cannot verify that the `triggers_met:` declaration is itself a truthful classification of the decision against D-016. The declaration's truth relies on operator integrity and the `triggers_rationale:` field's adversarial visibility to Tier 2 review.

**Known false-compliance patterns** (recorded in D-040 rationale and preserved for future maintainers):

- **Under-declaration.** Writing `triggers_met: [none]` on a decision that in fact modifies the kernel. Check 14 passes silently.
- **Mono-perspective launder.** Three raw perspective files generated by re-prompting the same model with minor wording changes. Check 11 passes (three files present); check 14 passes (artefacts present for declared trigger); the substantive mono-perspective nature is undetected.
- **Strawman positions.** A `triggers_met: [d016_3]` claim (reasonable-disagreement trigger) justified by "two plausible positions" that are in fact strawmen. Deliberation-quality is out of scope for Tier 1.
- **Fabricated load-bearing claim.** A `triggers_met: [d016_4]` (operator-marked load-bearing) with a plausible-sounding Rationale that reclassifies a trivial decision as deliberation-worthy, or the inverse.

These patterns are not fixed by check 14 alone. The Tier 2 Q7 question (see below) is the designed counter-pressure.

### Check 15's Honest Limit (mandatory inline documentation)

Check 15 enforces **consistency between a decision's self-declared `d023_*` triggers and the session's non-Claude participant manifests**, not **truthfulness of manifest labels or skip reasons**. This limit is mandatory content in three locations:

1. A comment block in `tools/validate.sh` directly above check 15's implementation.
2. Check 15's failure message (as an inline NOTE).
3. This specification (above).

The language to preserve verbatim:

> This check verifies consistency between a decision's self-declared `d023_*` triggers and the session's non-Claude participant manifests. It does not verify that a manifest labeled non-Claude in fact represents a non-Claude participant (that is check 13's consistency scope) nor that the substantive adequacy of any skip reason is genuine (a Tier 2 concern). The declaration's truth relies on operator integrity.

**Known false-compliance patterns** (recorded in D-040 rationale):

- **Mislabeled manifest.** Relabeling a Claude-subagent manifest entry as `participant_kind: non-anthropic-model`. Check 15 passes; check 13's consistency scope catches this only if `cross_model: true` is also claimed.
- **Bogus skip annotation.** `**Non-Claude participation:** skipped — reason: "time constraints"; retry_in_session: S999` with no intention of retry. Check 15 passes on field presence; the reason's quality and retry commitment are Tier 2 concerns.
- **Pattern of skips.** Over-using the skip annotation across many sessions. No single check catches this; Tier 2 pattern-review is the counter-pressure.

### Tier 2: Guided Assessment

The following questions are printed for the assessor to consider:

1. **Provenance continuity:** Did this session's Read activity use prior provenance to understand past decisions? Were any past decisions re-proposed without acknowledgment?
2. **Specification consistency:** Are the current specifications semantically consistent with each other? Do any contradict or make assumptions that conflict?
3. **Adversarial quality:** In deliberative work, did the adversarial perspective provide genuine challenge, or did it concede too easily?
4. **Meaningful progress:** Is the methodology producing meaningful progress, or is it accumulating ceremony without advancing?
5. **Specification-reality alignment:** Are there specifications that describe things that no longer exist, or things that exist without being specified?
6. **Cross-model-honesty evidence (paired with check 13):** This session records `cross_model: true`. Name the concrete evidence — invocation transcript, CLI command, wall-clock gap, human presence — that distinguishes a genuine non-Claude participant from a Claude subagent with an edited manifest. If you cannot, flip `cross_model` to false. (Skip if this session does not claim cross-model participation.)

7. **Trigger-coverage plausibility (new in v3; paired with checks 14 and 15):** For each decision in this session declaring `**Triggers met:**`, read the decision's `**Decision:**` and `**Rationale:**` text and state whether the declared trigger list is consistent with the decision's content. For any `**Non-Claude participation:** skipped` annotation, state whether the reason is substantive (not formulaic) and the `retry_in_session:` commitment is credible. Flag mismatches and weak reasons; they are the dishonesty surface this session's Tier 1 checks cannot reach.

8. **OI-004 closure-retrospective substantive adequacy (new in v4; paired with check 18):** If this session contains an `oi-004-retrospective.md`, read its Qualifying Deliberations Table and P4 Assertion. For each row marked frame-replacement-or-novel-mechanism, verify the cited synthesis section actually contains a non-Claude-originated reframing (not paraphrase or restatement of a Claude perspective's argument). For the P4 assertion, verify the cited divergence shows the synthesis adopted a position that contradicts (or substantively augments) the Claude consensus, not merely supplemented it. Flag rows where the substantive claim is weaker than the structural claim suggests. (Skip if no `oi-004-retrospective.md` present.)

9. **Read-contract adherence (new in v5; paired with check 22):** For this session's work, verify: (a) the default-read surface enumeration in `read-contract.md` §1 was actually followed — every enumerated file was read at session open before any substantive work; (b) any archive-surface records relied on for load-bearing claims are cited via the `[archive: path]` convention in default-read files; (c) any non-reads of relevant archive records were declared in the session's honest-limits section with the gap they leave. Flag silent skips — these are the harness-layer laundering pattern the read-contract exists to prevent. Flag reliance on archive-surface claims without corresponding reads (the "witness-dumping" pattern WX-22-1 tracks).

### Tool Location and Behavior

The validation tool is located at `tools/validate.sh`. It:
- Is **read-only**: it never modifies any workspace file.
- Produces a **structured report** with pass/fail/warning counts for Tier 1.
- Prints the **Tier 2 questions** after the Tier 1 report.
- Exits with **code 0** if no Tier 1 failures, **code 1** otherwise.
- Has **no dependencies** beyond standard Unix tools (bash 3.2+, grep, sed, awk) and git.

### When to Run

Validation should be run:

- At the **start** of each session, during or immediately after the Read activity.
- After the **Produce** activity, to check that new artifacts meet structural requirements.
- Before the **Close** activity, as a final coherence check.

### Limitations

Automated structural checks verify form, not meaning. Passing all structural checks does not mean:

- Specifications are correct about what they describe.
- Provenance captures the actual reasoning (it may be post-hoc rationalization).
- Decisions were well-considered.
- The methodology is serving its purpose.
- Cross-model participation is genuine rather than theatrical (see check 13's honest limit).
- Declared `triggers_met:` lists match the decisions they classify (see check 14 and 15 honest limits).
- Independent-claim evidence pointers (check 16) point to truthful evidence (the check verifies presence only, not truthfulness — see check 16's honest limit in `validate.sh`).
- Claude-output-in-training disclosures (check 17) are truthful (the check verifies disclosure presence, not truthfulness — same operator-integrity floor as check 13).
- Closure-retrospective substantive content (check 18) is well-grounded (the check verifies structural well-formedness only; substantive adequacy is Tier 2 Q8).
- Participant_organisation values (check 19) reflect actual model developers (the check verifies closed-set membership, not factual provenance).
- Default-read budgets (check 20) measure file size, not file relevance to the session's work. A file under the budget may still be effectively not-read; a file over the budget has failed even if its content was fully read in segments.
- Archive-pack manifest integrity (check 21) verifies hash match on stored-vs-computed, not that the archive's content is what was intended or that the archive is the right artefact to preserve.
- Archive-pack citation consistency (check 22) verifies path and ordinal existence, not that the cited content supports the citing claim. Tier 2 Q9 is the designed counter-pressure.

These deeper questions are the purpose of Tier 2, which depends on honest assessment by the agent or human conducting the session. The methodology acknowledges that when a single AI agent both does the work and assesses it, Tier 2 is self-assessment rather than independent validation. This is a known limitation (see D-009), mitigated by making the questions explicit and recording the assessment in provenance, and further mitigated since Session 005 by the D-023 non-Claude-participation rule for meta-deliberations on self-assessment mechanisms.

The immutability check (Check 10) is a basic heuristic — it detects uncommitted changes to provenance files but does not verify full immutability across git history. Comprehensive immutability verification is a potential future improvement.

Check 12 verifies the presence of D-024 required keys but does not verify that the values are correct. A manifest may have all required keys while containing nonsense values; check 12 passes. The boundary between key-presence and value-correctness is a deliberate archival choice (the Archivist's Q3 position in Session 005: "the check succeeds if a field literally contains the string `unknown`, because D-024 explicitly admits `unknown` as a truthful value").

Check 13 is **consistency-of-self-report**, not **truthfulness-of-self-report**, as documented above. The Tier 2 Q6 is the methodology's designed complement. Passing check 13 *and* the operator answering Q6 with concrete evidence is stronger than either alone; neither is a truth certificate.

Checks 14 and 15 are **consistency between self-declared triggers and session artefacts**, not **truthfulness of the trigger declaration itself**, as documented above. The Tier 2 Q7 is the methodology's designed complement. Passing checks 14 and 15 *and* the operator answering Q7 with a substantive per-decision plausibility check is stronger than either alone. Check 14's gating rule (session ≥ 006) means the check does not apply to pre-adoption sessions; the immutability-preserving alternative for retrospective trigger classification is a separate artefact (D-039's retrospective-artefact pattern), not a retroactive rewrite.

## Validation

To validate this specification:

1. Run `tools/validate.sh` and verify it performs the twenty-two structural checks listed in the table above.
2. Verify the tool prints the nine guided questions listed above.
3. Compare the tool's actual checks against the table in this specification — they should match.
4. Verify the tool is read-only (it makes no changes to any file).
5. Verify the tool exits with code 0 when all fail-severity checks pass, and code 1 otherwise.
6. Verify that check 13's honest-limit language appears in `tools/validate.sh` (comment block above check 13), in check 13's failure message, and in this specification's "Check 13's Honest Limit" subsection. Any divergence is a specification violation.
7. Verify that check 13 reports `BLOCKED` (not `FAIL` and not `PASS`) for sessions where check 12 failed.
8. Verify that check 14's honest-limit language appears in `tools/validate.sh` (comment block above check 14), in check 14's failure message, and in this specification's "Check 14's Honest Limit" subsection. Any divergence is a specification violation.
9. Verify that check 15's honest-limit language appears in `tools/validate.sh` (comment block above check 15), in check 15's failure message, and in this specification's "Check 15's Honest Limit" subsection. Any divergence is a specification violation.
10. Verify that check 14 reports `BLOCKED` for sessions where check 11 failed and check 15 reports `BLOCKED` for sessions where check 12 failed.
11. Verify that checks 14 and 15 apply only to sessions numbered ≥ 006 (the `TRIGGERS_MET_ADOPTION_SESSION` constant in `validate.sh`).
8. Verify that check 11 applies only to sessions with at least one `*-perspective-*.md` file, check 12 applies only to sessions with a `manifests/` subdirectory, and check 13 applies only to sessions that declare `cross_model: true`.
