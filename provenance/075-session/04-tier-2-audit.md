---
session: 075
title: Tier 2.5 Cross-Family Reviewer Audit — Session 075
date: 2026-04-26
status: complete
reviewer: codex (GPT-5.5)
reviewer_provider: openai
reviewer_kind: non-anthropic-model
reviewer_overlap_with_recent_mad_perspectives: >-
  codex/GPT-5.5 family participated as prior MAD perspectives in S058, S062, S064, S071, and S073, and as S074 reviewer; no direct S075 implementation role, but scope-overlap exists for S073/S074 gamma mechanism premises audited at S075. Counterweighted by substrate-mediated checks against the digest, validator, ledger, feedback index, and file text; overlapping codex-originated claims are not treated as dispositive.
trigger_condition: multiple
session_under_review_subjects:
  - retention-window-closes:
      - provenance/070-session/03-close.md
      - provenance/071-session/03-close.md
      - provenance/072-session/03-close.md
      - provenance/073-session/03-close.md
      - provenance/074-session/03-close.md
      - provenance/075-session/03-close.md
  - validation-debt-ledger: validation-debt/index.md
  - active-watchpoints: WX-28-1 + WX-24-1 + aggregate-budget watch + WX-50-1/WX-58-1/WX-62-1 (closed)
  - engine-feedback-inbox: engine-feedback/INDEX.md
  - open-issues: open-issues/index.md
scope_coverage_table:
  retention-window-closes: "exercised: S070-S075 close pattern and aggregate/watchpoint trajectory read"
  validation-debt-ledger: "exercised: validation-debt/index.md authoritative ledger read"
  active-watchpoints: "exercised: WX-28-1, WX-24-1, aggregate-budget, and closed WX-50-1/WX-58-1/WX-62-1 read through closes"
  engine-feedback-inbox: "exercised: engine-feedback/INDEX.md and gamma-surface rows checked"
  open-issues: "exercised: open-issues/index.md active/resolved counts checked"
findings_count: 5
findings_dispositioned: 5
duration_minutes: 110 # producer_kind: agent-declared per REVD-2 quarantine
reviewer_prompt_template_version: 3
harness_telemetry_digest_available: true
bootstrap_status: limited-confidence
---

## §1 Scope and trigger basis

Tier 2.5 triggers fire on multiple conditions. S075 close records (a) engine-definition touching, (b) substantive-arc-class gamma phase-3.1 implementation, and (d) a validation-debt lifecycle event/disposition extension as YES at `provenance/075-session/03-close.md:66-76`. D-293 through D-299 are recorded at `provenance/075-session/02-decisions.md:12-131`.

Artefacts read: `provenance/070-session/03-close.md` through `provenance/075-session/03-close.md`; `provenance/075-session/00-assessment.md`; `provenance/075-session/02-decisions.md`; `provenance/075-session/harness-telemetry-digest.yaml`; `specifications/validation-approach.md`; `specifications/validation-approach-v8.md`; `specifications/workspace-structure.md`; `specifications/engine-manifest.md`; `tools/validate.sh`; `tools/digest_emitter.py`; `tools/digest_reconstructor.py`; `.claude/settings.json`; `validation-debt/index.md`; `engine-feedback/INDEX.md`; `open-issues/index.md`; and S074 audit carry-forward.

Reviewer-overlap handling: I am OpenAI/codex family. Prior codex participation includes S058, S062, S064, S071, and S073 MAD perspectives plus the S074 reviewer audit (`provenance/074-session/04-tier-2-audit.md:1-33`). S075 audits implementation of S073/S074 gamma/Tier 2.5 mechanism premises, so this is scope-overlap for those load-bearing claims. I counterweight by using substrate-mediated checks: current file text, validator implementation/output, digest metadata/records, ledger state, and feedback index state. I do not treat prior codex-originated perspective claims as independent validation.

## §2 (α)-flag coverage

Reviewer-run check 26 output:

```text
Check 26: honest-limit text repetition across §2c retention-window (validation-approach.md v9 §Tier 2.5 Layer 1; CHKD-2 evidence-consuming substrate-aware branch added engine-v15 Session 075)
  (substrate-aware: digest consumed at provenance/075-session/harness-telemetry-digest.yaml; substrate_calls=0; validator-as-evidence-consumer per §10.4-M33)
  ✓ check 26: no honest-limit text clusters detected across 6-close retention window (substrate-aware: digest consumed as evidence per CHKD-2 §10.4-M33; in-memory grep-fallback applied for cluster detection per S067 D-244)
```

No (α) WARN/FAIL item required disposition. The digest is present and consumed, but its CM1 primary `substrate_calls` section is empty at S075 (`provenance/075-session/harness-telemetry-digest.yaml:22`), consistent with the close's partial-capture honest limit (`provenance/075-session/03-close.md:135`).

## §3 Substantive evidence

## §3a Close correctness

The close correctly records the broad S075 decision set: D-293 Path-AS phase-3.1, D-294 validation-approach v9, D-295 validate.sh, D-296 new tooling/config, D-297 workspace-structure minor cleanup, D-298 engine-v15, and D-299 housekeeping at `provenance/075-session/03-close.md:46-56`. The amended-file list also matches the visible worktree surfaces (`provenance/075-session/03-close.md:24-42`).

F0: the current validator is not clean despite the close's validator forecast. A post-audit run of `./tools/validate.sh` passed check 27 for this audit but failed check 14 for D-293, D-294, D-295, and D-296: each declares d016_* triggers with zero perspective files and no exact `Single-agent reason:` annotation. The close forecast says 0 FAIL (`provenance/075-session/03-close.md:58-64`), while the actual run reports 1787 PASS / 4 FAIL / 41 WARN. This is the same form class S074 audit F1 caught before close; S075 repeats it on the phase-3.1 implementation decisions.

Close correctness is not clean. F1: S075 claims engine-feedback index and validation-debt lifecycle extensions occurred, but the authoritative surfaces still carry stale S074/S073-era text. D-299 says three engine-feedback rows were extended at S075 (`provenance/075-session/02-decisions.md:159-164`), yet `engine-feedback/INDEX.md` still says EF-068/EF-059/EF-067 will be fully resolved when S074 phase-3.1 lands (`engine-feedback/INDEX.md:21`, `engine-feedback/INDEX.md:23`, `engine-feedback/INDEX.md:24`). D-299 also says `validation-debt/index.md update` at S075 and names S075 gating progress (`provenance/075-session/02-decisions.md:166`), but the ledger frontmatter remains `updated-by-session: 073` (`validation-debt/index.md:1-6`) and VD-003 still describes S074+ phase-3.1/S075 phase-3.2 and CM1 PreToolUse+PostToolUse (`validation-debt/index.md:28`). Because v9 makes the ledger authoritative, this is a substantive close-correctness finding, not just narrative lag.

F2: the engine-manifest v15 entry is not cleanly ratified as D-298. D-298 says §2 should read established Session 075 per D-298 (`provenance/075-session/02-decisions.md:123-127`), but the manifest still says D-NNN at §2 and in the v15 index/detail (`specifications/engine-manifest.md:32`, `specifications/engine-manifest.md:150`, `specifications/engine-manifest.md:152`). The same detail entry labels S075 as Path-L even though D-293 and the close classify S075 as Path-AS phase-3.1 (`provenance/075-session/02-decisions.md:20-24`; `provenance/075-session/03-close.md:20-22`). It also carries a stale substrate-count forecast for VD-003 (`specifications/engine-manifest.md:160`) inconsistent with S075's n=5 claim.

F4: the close overstates digest evidence once. It says the smoke-test showed `tool_calls + substrate_calls records` (`provenance/075-session/03-close.md:86`), but the digest has `substrate_calls: []` (`provenance/075-session/harness-telemetry-digest.yaml:22`) and check 26 counted `substrate_calls=0`. The digest does show primary harness-measured tool-call records (`provenance/075-session/harness-telemetry-digest.yaml:23-29`), so this is an evidence wording error, not proof CM1 is nonfunctional.

## §3b Mechanism adequacy

The v9 mechanism mostly exists in concrete form. `validation-approach.md` codifies the SCD-3 location and capture-stack shape (`specifications/validation-approach.md:259-270`), the schema including per-record `producer_kind` and `authority_level` (`specifications/validation-approach.md:272-326`), REVD-2 quarantine (`specifications/validation-approach.md:330`), CHKD-2 (`specifications/validation-approach.md:332`), and reviewer-prompt-template v3 requirements (`specifications/validation-approach.md:334-340`). v8 is preserved as superseded (`specifications/validation-approach-v8.md:1-11`).

The validator implementation materially closes S074 F4: check 26 reads the current-session digest and counts substrate-call records without live MCP (`tools/validate.sh:1262-1282`), then runs the existing in-memory grep cluster logic (`tools/validate.sh:1300-1367`). Check 27 now requires §1 through §8 plus §3a/§3b/§3c and provider exclusion (`tools/validate.sh:1432-1475`). This aligns with the v9 audit-shape text at `specifications/validation-approach.md:205-226`.

The tooling also exists. CM1 writes SCD-3 frontmatter with `capture_adapter: claude-code-hook`, capabilities, and unobserved fields (`tools/digest_emitter.py:107-139`), routes substrate vs tool calls (`tools/digest_emitter.py:205-234`), and catches failures with exit 0 (`tools/digest_emitter.py:184-203`, `tools/digest_emitter.py:233-237`). CM3 emits agent-declared session-open declarations and post-hoc-reconstructed substrate-call records with secondary authority (`tools/digest_reconstructor.py:193-220`). `.claude/settings.json` configures only `PostToolUse` (`.claude/settings.json:1-16`).

Capture-adapter metadata coherence passes. The digest frontmatter claims `capture_adapter: claude-code-hook` (`provenance/075-session/harness-telemetry-digest.yaml:6`) and lists unobserved fields including `wall_clock_token_count` and `reviewer_invocation_wall_clock_seconds` (`provenance/075-session/harness-telemetry-digest.yaml:13-15`). Harness-measured records in this digest are tool-call records only (`provenance/075-session/harness-telemetry-digest.yaml:23-29`); `reviewer_invocations` is empty, and no harness-measured record claims authority over those unobserved fields.

F3: v9 still has spec-text/tooling drift around the just-adopted mechanism. The v9 version history says CM1 is `PreToolUse + PostToolUse` (`specifications/validation-approach.md:19`), while D-296 and the settings file make PostToolUse-only load-bearing (`provenance/075-session/02-decisions.md:84-92`; `.claude/settings.json:3-10`). The active spec still has D-NNN placeholders (`specifications/validation-approach.md:35`, `specifications/validation-approach.md:342`), and `tools/digest_emitter.py` repeats both `PreToolUse + PostToolUse` in the docstring and D-NNN in the engine line (`tools/digest_emitter.py:6`, `tools/digest_emitter.py:30`). The main §(z6) body is cleaner than v8, but the active mechanism text is not fully drift-free.

## §3c Trajectory discipline

The S071-S075 trajectory is engaged, not merely ceremonial: S071 made substrate use required and created VD-003; S072 produced the gamma design-space; S073 adopted the (gamma-6) staged hybrid; S074 inserted the operator-directed reviewer-policy amendment; S075 implemented the phase-3.1 stack. S075 close accurately names the S070-S075 path pattern as Path-AS/Path-L/Path-AS rather than repeated Path A (`provenance/075-session/03-close.md:106-112`).

The trajectory has two weak points. First, the authoritative state surfaces did not keep up with narrative progress. The ledger and feedback-index drift in F1 means the engine is relying on close prose to carry lifecycle state that v9 says should be checkable against authoritative ledgers (`specifications/validation-approach.md:234-240`). Second, aggregate pressure is still being carried by close-rotation rather than structural rebalance. S071 crossed the 90K soft band (`provenance/071-session/03-close.md:115-117`), S072 explicitly warned close-rotation alone was insufficient (`provenance/072-session/03-close.md:162-164`), S073 sustained the same trajectory concern (`provenance/073-session/03-close.md:200-202`), and S075 forecasts ~94K-95K with EF-068-read-write-rebalance still only operator-discretionary (`provenance/075-session/03-close.md:145`, `provenance/075-session/03-close.md:202`).

Per-direction staging is mostly preserved: D-293 rejects a fresh MAD because S073 already dispositioned the gamma directions, and D-294 through D-296 implement specific CM/SCD/CHKD/REVD/RAD pieces (`provenance/075-session/02-decisions.md:20-24`, `provenance/075-session/02-decisions.md:34-92`). The risk is not bundling-by-laundering inside S075's implementation choice; it is state-surface laundering afterward if ledgers and indexes continue to be described as updated without being updated.

## §4 Disposition table

| Item | Source citation | Disposition | Rationale |
|---|---|---|---|
| F0: validator check 14 fails D-293 through D-296 | `provenance/075-session/02-decisions.md:12-92`; post-audit `./tools/validate.sh` output | accepted | The decisions have substantive single-orchestrator rationale, but the validator requires the exact `Single-agent reason:` shape when d016_* triggers appear without perspective files. |
| F1: authoritative state surfaces lag S075 narrative | `validation-debt/index.md:1-6`, `validation-debt/index.md:28`, `engine-feedback/INDEX.md:21`, `engine-feedback/INDEX.md:23`, `engine-feedback/INDEX.md:24`, versus `provenance/075-session/02-decisions.md:159-166` | accepted | v9 makes the ledger authoritative, and the feedback index is the default-read inbox surface. S075 narrative claims progress/extensions that those surfaces do not carry. |
| F2: engine-manifest v15 entry has D-NNN placeholders and Path-L/path/gating drift | `specifications/engine-manifest.md:32`, `specifications/engine-manifest.md:150`, `specifications/engine-manifest.md:152`, `specifications/engine-manifest.md:160` | accepted | D-298 says v15 is established by D-298 and S075 is Path-AS phase-3.1. The manifest still contains placeholder and stale state text. |
| F3: active v9/tooling text retains stale PreToolUse and D-NNN wording | `specifications/validation-approach.md:19`, `specifications/validation-approach.md:35`, `specifications/validation-approach.md:342`, `tools/digest_emitter.py:6`, `tools/digest_emitter.py:30` | accepted | The implemented/configured mechanism is PostToolUse-only and decisions are D-293 through D-299. Residual stale text can mislead future mechanism interpretation. |
| F4: close overclaims substrate-call digest evidence | `provenance/075-session/03-close.md:86`, `provenance/075-session/harness-telemetry-digest.yaml:22`, check 26 reviewer-run output | accepted | CM1 has primary tool-call records and coherent metadata, but S075 has zero primary substrate-call records in the digest because session-open substrate use preceded hook activation. |

## §5 Stale-item escalation

No lifecycle item is past `review_by_session`: VD-001 and VD-002 are resolved; VD-003 is `in-progress` with `review_by_session: S076` (`validation-debt/index.md:24-28`). I do not escalate for lateness.

I do escalate the ledger/index mismatch as F1. It should be corrected before or during S076 VD-003 review: either update the authoritative ledger and feedback index to the S075 state, or explicitly record that close prose is provisional and the ledger remains authoritative until S076 disposition. Leaving both surfaces divergent would violate the v9 authoritative-not-witness discipline.

## §6 Reviewer metrics

Reviewer overlap: codex/GPT-5.5 family overlap with S058/S062/S064/S071/S073 perspectives and S074 reviewer; scope-overlap exists for S073/S074 gamma-mechanism premises; counterweighted by substrate-mediated checks. Findings count: 5. Findings dispositioned: 5. Duration minutes: 110, `producer_kind: agent-declared`, `authority_level: tertiary`. Harness telemetry digest available: true. Reviewer-prompt-template version: 3. This is v3 application n=1 after the counter reset, not a locked template.

REVD-2 quarantine applies: the duration in frontmatter and this section is not cited for §10.4-M25 P1 audit-cost-budget threshold arithmetic. It is only a cross-session pattern observation.

## §7 Next-session-shape critique

S075 recommends S076 as Path-AS phase-3.2 minor extensions plus VD-003 full review (`provenance/075-session/03-close.md:94-121`). That recommendation has enough affirmative no-action justification to avoid a disputed Path-A disposition, but it must include the state-surface repairs named above.

1. Open issues unprogressed across the retention window: present. `open-issues/index.md` still lists 13 active OIs (`open-issues/index.md:7-26`). The no-action justification is acceptable because S076 is a concrete VD-003/gamma-review session, not a watch default.

2. Engine-feedback inbox untriaged or repeatedly deferred: partially present. Counts are 0 new / 6 triaged / 10 resolved (`engine-feedback/INDEX.md:9-15`). The gamma rows are actively relevant but stale in text (F1). Non-gamma rows, especially EF-068-read-write-rebalance, remain deferred by operator-discretionary warrant; S076 should name that explicitly if not activating it.

3. Watchpoints stale, underspecified, or carried without decision: not stale on WX-28-1 and WX-24-1; both are actively tracked at S075 (`provenance/075-session/03-close.md:196-206`). The aggregate-budget watch remains substantively active because the trajectory is still rising.

4. Validation debt exists and next-session recommendation does not explain why it can wait: not fired. VD-003 is due at S076 and S075 explicitly names full review at S076 (`provenance/075-session/03-close.md:96-100`).

5. Recent closes repeatedly recommend watch without operator agenda: not fired. S075 itself names the S070-S075 window as Path-AS Shape-1 / Path-AS MAD / Path-AS design-space / Path-AS MAD / Path-L operator-directed / Path-AS phase-3.1 (`provenance/075-session/03-close.md:112`).

Disposition: S076 recommendation accepted with required repair agenda. If S076 treats F0-F3 as cosmetic and proceeds straight to lock-in/re-baseline, that would become a disputed next-session-shape issue.

## §8 Reviewer cost note

WX-62-1 five-field note:

| Field | Value |
|---|---|
| reviewer | codex (GPT-5.5), openai |
| wall_clock_minutes | 110 |
| token_count | not harness-measured; unavailable |
| producer_kind | agent-declared |
| authority_level | tertiary |

Comparison: S071 audit self-reported 55 minutes, S073 official audit 25 minutes, S073 codex cross-check 58 minutes, and S074 codex audit 72 minutes (`provenance/071-session/04-tier-2-audit.md:108-112`; `provenance/073-session/04-tier-2-audit.md:97-103`; `provenance/073-session/04-tier-2-audit-codex-cross-check.md:31`; `provenance/074-session/04-tier-2-audit.md:29-32`). This S075 value is higher because v3 required digest inspection plus spec/tool/ledger/feedback cross-checks. Under REVD-2, this remains agent-declared/tertiary and excluded from threshold arithmetic.

## §X Bootstrap status

Rules being audited under: this audit is produced under about-to-be-adopted `validation-approach.md` v9, while S075 opened under active v8. v9 itself revises the §Tier 2.5 mechanism by adding SCD-3 schema codification, reviewer-prompt-template v3 digest requirements, capture-adapter metadata checks, REVD-2 quarantine handling, and check 27 §1-§8 plus tripartite §3 enforcement (`specifications/validation-approach.md:19`, `specifications/validation-approach.md:77`, `specifications/validation-approach.md:334-340`).

Reviewer-overlap status: codex/GPT-5.5 has prior MAD-perspective participation in S058, S062, S064, S071, and S073, and reviewer participation in S074. I declare scope-overlap for S073/S074 gamma/Tier 2.5 mechanism premises that S075 implements. I counterweight through substrate-mediated checks of the actual digest, validator code/output, ledger, feedback index, manifest, and spec text; I exclude any assumption that prior codex perspective claims are clean independent evidence.

This audit MUST NOT be cited as clean validation of the revised v9 Tier 2.5 mechanism. It is a limited-confidence bootstrap audit of v9 adoption and records five accepted findings against the S075 state. It may support S076 repair/review planning, but it cannot close the revised mechanism as validated.
