---
session: 022
title: Perspective — Outsider
date: 2026-04-22
perspective: outsider
participant_kind: non-anthropic-model
model_family: gpt
model_id: gpt-5.4
provider: openai
endpoint: cli-wrapper
invocation_method: codex-exec
reasoning_effort: xhigh
tokens_used: unknown-not-echoed-at-close
session_id: 019db521-775f-7872-9b38-f0c4b0094c28
status: verbatim
anchor_commit_cited: 46f0baf
transport_note: |
  Committed verbatim from `codex exec` stdout including CLI banner
  (OpenAI Codex v0.121.0 research preview, model gpt-5.4, provider
  openai, approval never, sandbox read-only, reasoning effort xhigh,
  session id 019db521-775f-7872-9b38-f0c4b0094c28), user prompt echo
  (full shared brief + Outsider stance + response-now instruction),
  four codex markers delimiting pre-response workspace-exploration
  tool calls (reading CLAUDE.md, prompts/development.md,
  prompts/application.md, specifications/methodology-kernel.md,
  specifications/workspace-structure.md, specifications/engine-manifest.md,
  specifications/validation-approach.md, specifications/multi-agent-deliberation.md,
  tools/validate.sh, provenance/014-oi016-resolution/01d-perspective-outsider.md
  outlier structure), reasoning summary entries, and the final response
  body (opening position statement + Q1-Q9 + Honest Limits section).
  Invocation used stdin-pipe form per Session 021 lesson:
  `codex exec -c model_reasoning_effort=xhigh < /tmp/022-outsider-prompt.txt
  > /tmp/022-outsider-response.txt 2>&1`. No stdin-wait hang this session.
  Exit code 0; background task id bfutmoq27. Full verbatim preservation
  (including CLI noise and workspace-exploration traces) per Session 014
  precedent and operator's §3 "witnesses preserve verbatim; summarisation
  or silent compression forbidden" constraint. At session close, if
  witness-packs are adopted, this file is migrated per the adoption
  decision.
---

Reading prompt from stdin...
OpenAI Codex v0.121.0 (research preview)
--------
workdir: /Users/ericmccowan/Development/complex-systems-engine
model: gpt-5.4
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019db521-775f-7872-9b38-f0c4b0094c28
--------
user
---
session: 022
title: Shared Brief — Workspace Scaling Trajectory and Canonical-vs-Witness Frame
date: 2026-04-22
status: frozen
---

# Shared Brief — Session 022 Deliberation

This is the shared brief. All four perspectives receive it byte-identical. Each perspective's role-specific stance is in a separate file (`01a-perspective-*.md` etc.); only the stance differs between perspectives' briefs.

## 1. Methodology context

The Selvedge methodology (see `specifications/identity.md` v2; `specifications/engine-manifest.md`) is a self-hosting design methodology executing via a nine-activity kernel (`specifications/methodology-kernel.md` v4). This workspace has been the self-development application across Sessions 001–022. Current engine version: `engine-v2`, established Session 021 per D-082 (OI-004 criterion-4 articulation bump).

Each session reads the workspace, assesses, convenes perspectives, deliberates, decides, produces, validates, records, closes. Multi-agent deliberation rules per `specifications/multi-agent-deliberation.md` v4: non-Claude participation required for decisions modifying kernel / revising multi-agent-deliberation.md / revising validation-approach.md semantic validation / asserting OI-004 state change.

Prior full-session deliberations on related topics: Session 020 (`provenance/020-workspace-scaling-deliberation/`) adopted R1–R3 preserving `engine-v1` and adding `CLAUDE.md` orchestrator-convenience mempalace paragraph with four hands-on caveats; Session 021 (`provenance/021-oi004-criterion4-articulation/`) bumped engine-v1 → engine-v2 with criterion-4 articulation and four-state OI-004 lifecycle.

## 2. Problem statement

### 2.1 Session 022 session-open state

Session 022 opened under no default pre-commitment. `tools/validate.sh`: 498 pass, 0 fail, 0 warn. Session-open audit of Session 021 synthesis fidelity clean across five close-directed dimensions.

### 2.2 Scale facts observed at session open

- Total markdown files (excluding `.git/`, `.serena/`, `.claude/`): **212**.
- Total markdown word count: **676,879 words**.
- `SESSION-LOG.md`: **33,227 tokens** at session open (up from 25,713 at Session 020 open; up from the ~single-read ceiling at Session 020 close).
- `open-issues.md`: **27,437 tokens** at session open.
- Single largest provenance file: `provenance/014-oi016-resolution/01d-perspective-outsider.md` at **96,651 words** (next-largest is 7,877 words — a 12× jump).
- Session 021 SESSION-LOG summary entry: **11,340 characters** (94% of Skeptic's Session 020 F3 falsifier upper bound of 12,000 chars).

### 2.3 §5.4 Skeptic mempalace-non-use trigger 1 — materialised

Per Session 020 `01-deliberation.md` §5.4 operational warrant (a): "within 3 sessions of R3 adoption, mempalace is not used substantively (indicating the tool was not actually needed)." Sessions 020, 021, and 022 (opener) have not used mempalace substantively. Trigger 1 **has activated.** This ratifies the §5.4 rollback direction: defer-entirely on mempalace becomes preferred direction for R3.

### 2.4 Operator session-open ratification (direct text; surfaced per §10 anti-import)

Operator ratified path (E.1) with expanded framing. The direct text is committed at `provenance/022-session-open-audit/operator-direction.md` (appended below verbatim at §3). Perspectives MUST treat this text as **input to be surveyed / hypothesised against / partially accepted / rejected**, not as a decided direction. Per kernel §1 Read domain-reading reconciliation clause (OI-015 laundering-gap): domain input is surfaced; at Deliberate/Decide each perspective must re-examine whether the operator's frame should be adopted and, if so, in what shape.

Specifically the perspectives are asked in §8 Design Questions to:
- evaluate the operator's diagnosis of Session 022's own §1 Tooling note (paginated `Read --offset` resolution) as OI-015-at-the-harness-layer;
- evaluate the two-artefact-kind frame (canonical surfaces vs witnesses);
- evaluate the nine candidate surfaces for adoption / reject each independently;
- evaluate the falsifier burden operator names for defer-positions.

The operator expressed that rejection of the frame or of specific candidate surfaces is permitted if the perspective can meet the stated falsifier burden.

## 3. Operator direction verbatim (OI-015 anti-import disclosure)

The following is the operator's Session 022 direction in full, committed verbatim and surfaced as domain input:

> **Ratify E.1: remove R3 `CLAUDE.md` mempalace paragraph this session.** §5.4 Skeptic mempalace-non-use trigger 1 has materialised (three consecutive non-use sessions: 020, 021, 022); R3's contested adoption has its operational rollback warrant satisfied. Not D-023-triggering (CLAUDE.md is not engine-definition). Voluntary multi-perspective convening recommended per R3's original contested adoption.
>
> **E.1 alone does not address the trajectory.** Since Session 020's null adoption, the workspace has grown to ~647K words across 206 markdown files; SESSION-LOG.md is now ~33,227 tokens (up from ~25,713 at Session 020 open); open-issues.md is ~27,437 tokens; a single Session 014 Outsider perspective file is 96,651 words. Session 022 faced two ceiling-violating canonical files and declined mempalace — instead resolving them via "paginated `Read --offset` on 25-line table structure" and "`### OI-NNN:` section grepping followed by paginated `Read --offset`." That is the OI-015 laundering pattern materialised at the harness layer: the methodology's Read instruction satisfied by surgical-read routing-around rather than by direct reading. Engine-v2 did not address this; engine-v3 bump is acceptable if warranted.
>
> **Session adoption set must produce net-negative workspace word delta** and reduce the canonical-surface files-exceeding-Read-ceiling count to zero. Anticipate d016_1, d016_2, d023_1/2/3 firing alongside E.1; plan mandatory non-Claude convening.
>
> **Core frame: two artefact kinds, not one.** `prompts/development.md` line 19 ("read every file") and line 43 ("preserve everything") are not productive tension at 647K words; they are operational contradiction, satisfied in practice by harness-layer summarisation and surgical-read routing — silent-import of derived state into positions where kernel §1 Read requires direct reading. Session 022's own resolution ("paginated Read --offset... yields cleanly") is the exemplar. Distinguish:
>
> - **Canonical surfaces** — bounded orientation layer (specs, SESSION-LOG index, open-issues index, per-session `03-close.md`). Readable in full at session open. Size-gated.
> - **Witnesses** — immutable exact-text records (raw perspective outputs, superseded spec versions, historical annotations). Accessed by explicit reference, not default read. Over-budget witnesses stored as *manifest + numbered chunks* — raw text preserved verbatim; summarisation or silent compression forbidden.
>
> **Required `prompts/development.md` revisions:**
>
> - **Line 19:** *"Begin by reading the workspace's canonical orientation layer completely; then read any preserved witnesses needed to ground the claims you will rely on."*
> - **Line 25:** revise in the same direction or the contradiction moves down the page.
> - **Line 43:** *"Preserve all provenance. Do not delete or silently compress historical records. When a record exceeds routine-read bounds, preserve it as an immutable witness with stable references and a bounded manifest."*
>
> **Session 020 minority activation under current state.** §5.1 Splitter per-OI (warrant: 50K-token file ceiling — satisfied). §5.2 Splitter per-session SESSION-LOG (warrant: Skeptic F3 >12K chars without corresponding complexity — inspect 020–022 entries). §5.3 Outsider restore-to-index (warrant: R1 variance-clause insufficient — inspect 020–022 entries against complexity). §5.4 already activated per E.1 ratification. Assess §5.1–§5.3 against their own warrants.
>
> **Candidate surfaces (non-exhaustive):**
>
> 1. Remove R3 paragraph from `CLAUDE.md` (E.1 ratified).
> 2. Manifested witness-pack specification (format, location, inclusion rules, reference conventions).
> 3. Retroactive migration of over-budget raw perspectives (incl. `provenance/014-oi016-resolution/01d-perspective-outsider.md`) to witness-pack form.
> 4. Per-epoch consolidation: sessions 001–010 synthesised to canonical epoch-index; raws witness-packed.
> 5. `open-issues.md` split per its own spec anticipation clause — 20+ sessions of deferral is the falsifier.
> 6. `SESSION-LOG.md` restoration to true one-line index (§5.3 activation).
> 7. Superseded spec copies (`*-v1.md`, `*-v2.md`, ...) moved from canonical to witness surface.
> 8. `tools/validate.sh` Tier 1 hard-gate: no canonical-surface file exceeds the configured single-read budget; over-budget raw records must be witness-packed, not summarised. Hard-fail at session close.
> 9. `prompts/development.md` lines 19, 25, 43 revisions as above.
>
> **Falsifier burden on defer-positions.** "Paginated Read yields cleanly" / "surgical-read works on this session's specific questions" is not adequate; it is the laundering pattern named above. Adequate defer-falsifier must address (a) the 96,651-word single-perspective file, (b) kernel §1 Read's current unexecutability as written, and (c) external-application inheritance of the scaling trajectory.
>
> **Close shape.** Session close artefacts conform to the adoption set. If witness-packs are adopted, this session's own raw perspectives are witness-packed at close. No grandfather clause.

(End of verbatim operator direction.)

**Note on operator text accuracy vs current measurements**: the operator cites ~647K words / 206 markdown files. Current session-open measurements (at the time of this brief): **676,879 words / 212 markdown files**. The operator's numbers are slightly lower, probably reflecting an earlier measurement or different exclusions. The delta is small; the operator's qualitative claim (scale is substantial and trending up) is robust. Operator's claim of §5.1 warrant "50K-token file ceiling — satisfied" does not match literal spec text (`open-issues.md` at 27K tokens vs 50K warrant text); this is a point perspectives should flag if they read the warrant text directly.

## 4. Current spec text — relevant excerpts

Perspectives should not re-read full specs; the relevant excerpts are below. Full specs are in `specifications/` if perspectives need more.

### 4.1 `methodology-kernel.md` v4 §1 Read (lines 31–37)

> Absorb what the session will reason from before changing anything. In every session this includes **workspace reading**: the full current state of the workspace — every file, every specification, every provenance record, and, where relevant, recent version-control history. Build a complete picture of the workspace's own state.
>
> When the session produces or revises an artefact intended for use outside the workspace, it also includes **domain reading**: the domain constraints the session operates under (stated by the user or operator in-session), cited external materials introduced into the session, and domain knowledge that the orchestrating agent surfaces explicitly as input to the work. Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step (per PROMPT.md). Perspective pretraining enters the session via stance briefs and perspective responses, not via §1 Read.
>
> This is a receptive activity. Its output is understanding, not artifacts.

### 4.2 `prompts/development.md` lines 17–45 (executable prompt under self-development)

Current text (lines 17–33):

> ## How to operate
>
> Begin by reading the workspace completely. Every file, every document, every historical record, every commit message if the workspace is under version control. Build a full picture of what exists before changing anything.
>
> From that reading, determine what state the methodology is in and what should happen next. [...]
>
> State your determination explicitly at the start of each session [...]
>
> Before doing any substantive work, read everything the workspace has preserved about prior decisions. If an idea was considered and rejected earlier, do not silently re-propose it. If you believe a rejected idea deserves reconsideration, cite the prior rejection and explain what has changed. Continuity of reasoning is the whole point of preserving provenance.
>
> Substantive work in this methodology should not be done by a single perspective. [...]

Current text (lines 33–45):

> ## Rules that hold across applications
>
> These rules apply to both the self-development application and to external-problem applications of the engine.
>
> Do not import ideas from outside the process. [...]
>
> Do not skip steps. [...]
>
> Do not overwrite prior specifications silently. [...]
>
> Preserve all provenance. Do not delete historical records, even when they feel embarrassing or outdated. A rejected idea from long ago may be the key to understanding a decision made today.
>
> Leave the workspace in a coherent state at the end of every application. [...]

### 4.3 `workspace-structure.md` v3 §SESSION-LOG.md (lines 61–63)

> A running index of sessions for quick orientation. Each entry is one line (one Markdown table row) containing the session number, date, title, and a summary of what was accomplished. The summary length scales to session complexity: planning-only, single-perspective, or assessment-only sessions produce shorter summaries; deliberation sessions producing substantive spec revisions, cross-model influences, or external artefacts produce longer summaries calibrated to record the decision surface and load-bearing influences. The canonical detail for each session lives in its provenance `03-close.md` file; the SESSION-LOG entry is an index over that detail, not a replacement. This file is updated at the close of each session.

### 4.4 `workspace-structure.md` v3 §open-issues.md (lines 65–67)

> A list of known questions, gaps, uncertainties, and unresolved disagreements. Each entry has a brief description, the session that identified it, and its current status. Issues are removed when resolved (with a reference to the session that resolved them). **This is a single file, not a directory, unless the number of issues makes a single file unwieldy.**

The "unless" clause is a pre-existing split-authorisation that has not yet been exercised.

### 4.5 `workspace-structure.md` v3 §provenance/ (lines 98–123)

Current convention: each session's provenance is a numbered directory. Files within are numbered for reading order. All provenance files use Markdown with YAML frontmatter. Provenance records are **immutable** once the session closes.

**Relevant tension:** the immutability rule (per D-017, reaffirmed in v3) prevents editing existing raw perspective files. Any retroactive migration must honor immutability — either by preserving originals in place + adding a witness-pack structure alongside, or by a copy-plus-reference pattern (see Session 009 D-054 precedent for `applications/` regularization).

### 4.6 `multi-agent-deliberation.md` v4 §Provenance Layout (lines 257–305)

Flat-layout is the current default; raw perspective files live at `provenance/<NNN-title>/01a-perspective-<role>.md` etc. The v4 spec does not currently prescribe a bound on raw-file size.

### 4.7 `engine-manifest.md` §3 at engine-v2 (file enumeration)

| File | Role |
|------|------|
| `PROMPT.md` | Dispatcher |
| `prompts/development.md` | Self-development executable prompt |
| `prompts/application.md` | External-application template |
| `specifications/methodology-kernel.md` | Kernel |
| `specifications/multi-agent-deliberation.md` | Multi-agent rules |
| `specifications/validation-approach.md` | Two-tier validation |
| `specifications/workspace-structure.md` | Structure rules |
| `specifications/identity.md` | Denotation |
| `specifications/reference-validation.md` | Reference-validation |
| `specifications/engine-manifest.md` | This file |
| `tools/validate.sh` | Structural validator |

Any substantive revision to these files triggers an engine-version bump per `engine-manifest.md` §5.

## 5. Session 020 minorities assessment against warrants

Per operator direction, each §5.x minority's warrants are re-examined against current session-open state.

### 5.1 (Splitter per-OI directory for open-issues.md)

Warrant text: "(a) future session's OI-housekeeping task completes incorrectly because a segment-read missed a relevant cross-reference in a not-loaded segment of `open-issues.md`; (b) two consecutive sessions' OI count tallies disagree with git history because of segment-read undercount; (c) `open-issues.md` exceeds 50,000 tokens (requires >2 segment-reads for full traversal)."

**Current state:** open-issues.md at 27,437 tokens. Requires 2 segment-reads (first ~25K, second ~2K). Strict warrant (c) says >2 segment-reads = >50K tokens. Not met. Warrants (a) and (b) not observed.

**Operator claim** that this warrant is satisfied does not match literal spec text. Perspectives should evaluate whether to (i) adhere to literal warrant, (ii) revise the warrant downward (e.g., to "exceeds single-read ceiling" which IS satisfied), (iii) reject the minority adoption path altogether and treat open-issues separately.

### 5.2 (Splitter per-session files for SESSION-LOG.md)

Warrant text: "(a) after R1 adoption, a session's SESSION-LOG entry exceeds 12,000 characters without corresponding session complexity (Skeptic's F3 falsifier); (b) SESSION-LOG.md exceeds single-read ceiling within 5 sessions of R1 adoption (i.e., by Session 025); (c) a session records a specific reasoning error traceable to segmented SESSION-LOG read (Skeptic's F1 falsifier)."

**Current state:** SESSION-LOG.md at 33,227 tokens (exceeds 25K single-read ceiling). R1 adopted Session 020; Session 022 is 2 sessions later (well within 5-session window). **Warrant (b) IS SATISFIED.** Warrant (a) not satisfied (Session 021 entry at 11,340 chars with high complexity — below F3 bound; variance-clause invoked appropriately). Warrant (c) not observed.

### 5.3 (Outsider restore-to-brief-index)

Warrant text: "(a) after R1 adoption, a session cites SESSION-LOG as primary source while 03-close.md exists and carries the same content (i.e., citation laundering detected); (b) the R1 variance-clause ('summary length scales to session complexity') is invoked as permission for an unwarrantedly long entry that does not correspond to complexity by decision count or artefact count; (c) within 5 sessions of R1, SESSION-LOG.md exceeds single-read ceiling despite the variance-clause."

**Current state:** Warrant (c) IS SATISFIED on the same ceiling-breach basis as §5.2(b). Warrants (a) and (b) not observed.

### 5.4 (Skeptic defer-entirely on tools)

Warrant text: "(a) within 3 sessions of R3 adoption, mempalace is not used substantively; (b) any 'search laundering' incident occurs; (c) mempalace version drift causes silent index staleness resulting in a missed session finding; (d) external-application workspaces report confusion from the 'CLAUDE.md tool reference but no engine requirement' pattern."

**Current state:** Warrant (a) SATISFIED (Sessions 020, 021, 022 non-use). Warrants (b)-(d) not observed. Operator ratifies E.1 adoption.

### Summary

§5.2, §5.3, and §5.4 warrants are **vindicated**. §5.1 strict warrant is **not vindicated**, but related warrants (single-read ceiling breach) are satisfied, raising a question of whether §5.1 should be triggered by the softer ceiling-breach condition too.

## 6. Survey — related framings from adjacent traditions

Per kernel §1 Read and PROMPT.md anti-silent-import, domain knowledge surfaced explicitly as input. Perspectives may reason against these; they are not authoritative.

**Computing / data systems:**
- **Memory hierarchies** (registers → L1/L2/L3 cache → RAM → disk → tape). Canonical-orientation-layer ≈ "hot" tier (read at session open); witness layer ≈ "cold" tier (accessed by explicit reference). Analogous to the operator-proposed frame.
- **Literate programming / weave-and-tangle** (Knuth). The same source decomposes into a "woven" human-readable document and a "tangled" machine-compilable output. Analogous: maybe canonical-vs-witness is "woven" summary vs "tangled" raw.
- **Git LFS and large-file handling.** Git stores pointers to large objects outside the repo proper. Analogous: the over-budget Outsider file could be LFS-shaped.
- **Database indexing vs storage.** An index is a bounded-size structure that points into unbounded storage. Analogous to SESSION-LOG as index, 03-close.md as storage.
- **Content-addressable storage** (IPFS, Git object store). Objects addressed by hash; references are pointers. Analogous for witness integrity.

**Information / library sciences:**
- **Cataloguing vs archive.** The card catalog is indexed at constant cost; the stacks are unbounded but accessed by reference. Analogous.
- **Scholia vs text.** Medieval manuscripts had a bounded canonical text surrounded by scholia (marginal annotations). Annotations grew over time but the canonical text did not.

**Document / software engineering:**
- **API docs vs source code.** The canonical API doc is read first; the source is read for details. Revision discipline keeps the API doc current; implementation can be arbitrarily complex below.
- **Executive summary + appendices.** Classic corporate-document pattern. Summary is bounded; appendices are unbounded.

**Constraints-vs-mechanism in this workspace specifically:**
- Kernel §1 Read says "every file, every specification, every provenance record." This is the *constraint* the methodology imposes on itself.
- `prompts/development.md` line 19 says "read the workspace completely." This is the executable *restatement*.
- Current *mechanism* (observed at Session 022 open): paginated `Read --offset` + `Grep` on section anchors. This is "harness-layer routing."

The tension between constraint and mechanism is the object of this deliberation. **Options:**
- (I) Revise the constraint to match the mechanism: "read canonical layer completely; read witnesses by reference." Operator-proposed.
- (II) Revise the mechanism to match the constraint: require that every file be readable in a single call; force workspace to shrink until constraint is executable. Extreme but coherent.
- (III) Keep both; explicitly tolerate the gap as a hedge: current state. Laundering concern.
- (IV) Reframe entirely (no layer distinction; different diagnosis of the scaling tension).

## 7. Role-specific stances — placement

Each perspective has its role stated in a separate `01X-perspective-<role>.md` file written before this brief is committed. See §8 below for the design questions each perspective must answer.

Perspectives in this deliberation:
- **01a — Architect.** Constructive design of the adoption set. Canonical/witness distinction advocate.
- **01b — Conservator.** Preservation-first. Tests fidelity costs of restructuring; immutability concerns.
- **01c — Skeptic.** Adversarial. Tests whether the canonical/witness frame introduces new failure modes; holds defer-positions to operator's stated falsifier burden.
- **01d — Outsider.** Non-Claude (OpenAI GPT-5.4 via `codex exec`). Bring training-distribution-independent reasoning to the table.

## 8. Design questions

Each perspective answers all eight questions below. Responses are independent — each perspective forms its position before seeing the others.

**Q1. Frame acceptance.** Do you accept the operator's two-artefact-kind frame (canonical surfaces vs witnesses) as the right diagnosis? If yes, what is your load-bearing reason. If no, what is your alternative frame or rejection argument. If partially, which parts and which not.

**Q2. `prompts/development.md` revisions.** Evaluate the operator's proposed text for lines 19, 25, 43. Propose your own text if different. Must address:
- Whether line 19 should be revised (and how);
- Whether line 25 (the "read everything the workspace has preserved about prior decisions") needs corresponding revision;
- Whether line 43 (the preservation rule) should be revised to name witness-packing explicitly;
- Whether kernel `methodology-kernel.md` §1 Read should be revised (d023_1 trigger) or whether prompts-layer revision alone is sufficient.

**Q3. Witness-pack specification.** If witness-packs are adopted, what is the specification? Required fields:
- Format: directory with manifest + numbered chunks? Single file with chunks? Zip-like archive?
- Location: alongside the original in provenance? Separate top-level directory?
- Inclusion rules: what classifies a record as "over-budget" (token count? word count? single-read-failure?)
- Reference conventions: how does a canonical file point at a witness? How does a reader resolve the pointer?
- Integrity: how is verbatim preservation guaranteed? Hash? Append-only?
- Does witness-packing require an engine-v3 bump?

**Q4. Retroactive migration scope.** Given immutability (D-017; workspace-structure.md §provenance), which of the following should be retroactively migrated this session? (Each yes/no with reason.)
- (a) `provenance/014-oi016-resolution/01d-perspective-outsider.md` (96,651 words; the extreme outlier)
- (b) All over-threshold raw perspective files (if threshold T defined)
- (c) Superseded spec copies (`specifications/*-v1.md`, `*-v2.md`, `*-v3.md`)
- (d) Long OI annotations in `open-issues.md`
- (e) Long SESSION-LOG entries (Sessions 011+)
- (f) Sessions 001–010 "epoch-index" consolidation (operator candidate #4)

**Q5. Canonical-surface restoration this session.** Should this session:
- (a) restore `SESSION-LOG.md` to a thin one-liner index (§5.3 activation)?
- (b) restructure `open-issues.md` (§5.1 variant; maybe not strict per-OI directory if warrant not fully met)?
- (c) both, one, or neither?
- What is the risk of losing information in this restoration?

**Q6. `tools/validate.sh` hard-gate check.** Evaluate operator candidate #8 (no canonical-surface file exceeds configured single-read budget; hard-fail at close). What single-read budget? How is "canonical-surface" vs "witness" detected by the validator? Where does the list live?

**Q7. Session 020 minority activations.** Each of §5.1, §5.2, §5.3 has warrants assessed in §5 above. For each:
- (a) adopt the rollback direction?
- (b) re-revise the warrant text if strict reading not met?
- (c) subsume into the canonical/witness frame adoption (i.e., the frame's adoption supersedes the minority's separate activation)?

**Q8. Close shape — this session's own raws.** Operator stipulates: no grandfather clause; this session's own raws are witness-packed at close if witness-packs are adopted. Do you accept? What is the practical consequence for this session's provenance directory and SESSION-LOG entry?

**Q9 (meta).** What is the engine-version implication of the adopted set? Is engine-v3 warranted? Which D-023 triggers fire? The operator anticipates `d016_1, d016_2, d023_1/2/3`. Do you agree with that trigger declaration?

## 9. Response format

Per `multi-agent-deliberation.md` v4 §Stance Briefs:

- Length target per perspective: 1,500–3,500 words.
- Structure: opening position (2-3 sentences), then Q1–Q9 in order. Each question answered with explicit position + reasoning + cites to this brief or to current spec text where relevant. Honest-limits section at the end naming what the perspective could not verify independently.
- Citation style: `[§N]` for sections of this brief; `[spec-name §N]` for specifications; `[01X-Q#]` when referring to another perspective's response (not applicable during the independent phase — only relevant in synthesis).
- Perspectives must NOT read other perspectives' responses during the independent phase. Perspectives MAY read this brief and current specifications in `specifications/`. Perspectives MUST NOT read raw files in `provenance/NNN/` unless explicitly needed and the read is declared in the honest-limits section.
- Refusal or substantive rejection is permitted and is signal, not error.

## 10. Anti-import constraint (OI-015 laundering-gap reconciliation)

Per PROMPT.md, kernel §1 Read, and OI-015: reason primarily from this brief. Do not import ideas from pretraining, unrelated sources, or conversations outside this deliberation without naming the import and routing it through explicit surveying (§6 above is the surveying step for this deliberation).

**Specific risk at Session 022**: the operator's text in §3 includes vocabulary ("canonical surfaces", "witnesses", "manifest + numbered chunks", "laundering at the harness layer") that is NOT yet in any specification and may be partially novel. Perspectives should evaluate:
- Whether to adopt this vocabulary directly or coin their own;
- Whether operator-vocabulary shapes the available solution space unduly;
- Whether the frame the vocabulary encodes is the right frame.

**Brief-priming observation from Session 008, 014, 016** etc.: briefs that quote operator text tend to propagate that text into perspective responses even when the perspective's own reasoning would have used different words. Be aware of this effect; prefer your own vocabulary where your reasoning does not specifically adopt the operator's frame.

## 11. Closure

The deliberation ends when all four perspectives have committed their responses verbatim. Synthesis proceeds per `multi-agent-deliberation.md` v4 §Synthesis. Session decisions at `02-decisions.md`. Close at `03-close.md`.

Deliberation anchor commit: this brief is committed at the next commit; the commit hash is the anchor.

---

(End of shared brief.)
---
session: 022
title: Role-Specific Stance — Outsider
date: 2026-04-22
status: stance-brief
perspective: outsider
---

# Role-Specific Stance — Outsider

You are the Outsider. You are not from the Claude model family.

You were invited to this deliberation because the methodology's Open Issue OI-004 requires non-Claude perspectives to be genuinely independent in training lineage and to shape outcomes through contributions Claude-only deliberation could not produce. Prior Outsider contributions (Sessions 005, 006, 009, 011, 012, 013, 014, 017, 019, 020, 021) have included frame-replacement (Session 017 H4 layered model; Session 020 "indexes drifted to dossiers" type-drift), split-resolving third-ways (Sessions 009/010/011 voice-and-structure patterns), and structural bifurcation (Session 021 criterion-4 two-branch model-vs-human articulation). The typology of non-Claude contribution is open; your contribution may be of any kind.

Your specific assignment:

- Evaluate the operator's canonical-vs-witness frame **independently** of what the Claude perspectives in this deliberation would produce. If you see a different diagnosis of the scaling tension, name it.
- Respond to Q1–Q9 in §8 of the shared brief. Your honest assessment of each is more valuable than consensus with Claude perspectives.
- If you see a gap in the frame (e.g., a participant kind the frame does not accommodate; an operational contradiction the adoption creates; a cheaper alternative the Claude-perspective space is not likely to produce), name it explicitly.

You may perform workspace exploration via `codex exec` tool calls before producing your response body (Session 021 precedent). If you do, cite specific files and sections. You may NOT read other perspectives' responses — this deliberation is independent-phase.

You may refuse a stance, propose a fourth or fifth hypothesis, or argue for a frame-replacement rather than within-frame answers. Refusal and reframing are signal, not error.

Target length: 1,500–3,500 words. Answer all Q1–Q9.

---

Respond now. Write directly as your response body. Do not summarise the brief back to me; cite §N references as needed. Answer Q1 through Q9 in the order presented. Open with a short (2-3 sentence) position statement. Close with an honest-limits section. Length target: 1500-3500 words.

codex
Writing the Outsider stance body. I’m checking the current executable prompt, kernel, structure, manifest, validator, and `CLAUDE.md` so the response is anchored to the live workspace rather than only the brief excerpts.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "sed -n '1,220p' prompts/development.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
# CLAUDE.md

## Commit workflow

Before finishing your response, stage all changed/new files, commit with a concise message, and push using git directly.

## Tools
This contains usage instructions for tools you have requested. If you decide more are needed, you can install them using `uv tool` or ask the user to ratify your tool decision and install something on your behalf. Add additional instructions here as you see fit.

### Multi-agent work

When work would benefit from multiple independent perspectives or parallel efforts, consider using agent teams via the `TeamCreate` tool (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`). You also have access to the Google `gemini` and OpenAI `codex` CLI tools for non-Anthropic LLM access. Codex is preferred for any thinking or reasoning tasks.

### mempalace (orchestrator-convenience, non-engine)

`mempalace` v3.1.0 is installed via `uv tool`. It is classified as orchestrator-convenience tooling, analogous to the `gemini`/`codex` CLIs above. **It is NOT part of `engine-manifest.md` §3 and is NOT required by any specification.** External-application workspaces loading the engine do not inherit the dependency; fresh clones of this workspace can operate without it. This classification is load-bearing for the engine's text-only portability claim; do not promote mempalace into any engine-definition file without a dedicated deliberation.

Suggested use: when a single Read would exceed the 25,000-token ceiling (SESSION-LOG.md, open-issues.md, aggregated provenance search), orchestrators may run `mempalace search "<query>" --wing complex-systems-engine` or `mempalace wake-up --wing complex-systems-engine` to retrieve candidate matches.

**Critical caveats (per Session 020 hands-on finding; see `provenance/020-workspace-scaling-deliberation/01b-perspective-tooler.md`):**

- Despite the `mempalace --help` description ("Find anything, exact words"), `search` is semantic/vector-ranked, not exact-string match. Exact-string queries like `D-074` may return zero results containing that string even when the string exists in indexed files. Use `Grep` for exact-string verification.
- `wake-up` output is drawer-count-dominated rather than recency-weighted; it is useful for fresh-session priming but does not substitute for reading SESSION-LOG.md.
- `mine` does not deduplicate versioned specs — superseded `-v2.md` / `-v3.md` files are indexed alongside current canonical files and may rank above them.
- mempalace output is **candidate-discovery only.** Every cited claim must be reconfirmed against the source file via Read before inclusion in session artefacts. Treating mempalace output as authoritative is the laundering risk (OI-015-adjacent, WX-20-1 watchpoint).

Initialisation (one-time, if adopted): `mempalace init . && mempalace mine .` in workspace root. The init creates `mempalace.yaml` + `entities.json` in the workspace root — both are gitignored. The palace state itself lives at `~/.mempalace/palace/`, outside the workspace.

Re-mine cadence: manual, typically at session close after substantive file changes. Not a spec requirement; orchestrators not using mempalace need not re-mine.

 succeeded in 0ms:
You are operating on the **self-development application** of the **Selvedge engine**. This is the foundational application in which the engine evolves its own specifications by running its own process on itself. Every session so far (001 through the most recent) has been an instance of this application. This prompt is applied repeatedly. Each application advances the work by one increment. The workspace may be empty, partial, or mature. Determine the state and take the next right step.

Selvedge is the methodology (abstract approach). The **Selvedge engine** is its current loadable implementation, enumerated in `specifications/engine-manifest.md`. An **application** of the engine is any specific run — this one is the self-development application. See `specifications/identity.md` for the three-layer denotation; see `PROMPT.md` (the dispatcher) for the top-level framing.

## What this application is

This application is the engine's own development: a self-hosting design activity in which specifications evolve themselves by running the engine on its own outputs. What emerges from this workspace is intended to be used by others, on their own projects, in their own domains, as a separately-initialised application of the engine (per `prompts/application.md` and `engine-manifest.md` §6). The methodology is self-hosting — the engine evolves itself by running its own process on itself. Specifications are the durable artefacts that persist between its stages, and provenance — the reasoning trail, the rejected alternatives, the dissenting views — is preserved alongside decisions so that future readers, human or agent, can reconstruct not just what was decided but what was considered and why.

The engine exists because traditional ways of managing requirements and design intent were optimized for a world where humans were the expensive part of producing and maintaining specifications. In a world where language models can read, generate, challenge, and evolve specifications at the moment they are needed, the old ceremonies collapse into something lighter and more continuous. This self-development application discovers what that lighter approach looks like by being built through the approach it proposes.

The methodology is not specific to any domain. An external-problem application of the engine may design software, research programmes, physical systems, policy interventions, curricula, organisations, or anything else. The methodology itself — the mechanic of diverse perspectives reasoning together, producing durable artefacts, preserving their reasoning, and evolving the system by running the same mechanic on its own outputs — is domain-general.

A preference, not a rule: text-based artefacts in a format that is both human-readable and machine-readable tend to serve this kind of methodology well, because they can be read by people, parsed by agents, diffed between versions, and preserved indefinitely with minimal tooling. Markdown is the obvious candidate for most work. For domains where text alone cannot carry the specification — a spatial layout, a circuit diagram, a molecular structure, a musical score — use whatever representation the domain demands, but keep a text-based record of the intent and reasoning alongside it so the provenance remains legible.

Another preference, not a rule: every application of the engine should include some mechanism by which its specifications can be shown to still describe reality. In a software context this is automated tests. In a research context it may be reproducibility of results. In a policy context it may be a pilot study or an evaluation against stated outcomes. In a physical system it may be a qualification campaign. The word "test" is used in this prompt as a shorthand for whatever form of validation is appropriate; `specifications/methodology-kernel.md` §7 names three senses (Workspace, Domain, Reference).

## How to operate

Begin by reading the workspace completely. Every file, every document, every historical record, every commit message if the workspace is under version control. Build a full picture of what exists before changing anything.

From that reading, determine what state the methodology is in and what should happen next. If the workspace has not yet defined its own structure, the first work is to do so — by surveying prior approaches, reasoning about what this methodology needs, and committing a proposed shape along with the reasoning that led to it. If the workspace has defined a structure but not yet applied it, the next work is to begin applying it. If the structure has been applied but produces artefacts that have not been validated, the next work is validation. If everything has been exercised at least once, the methodology is in evolution mode — identify the weakest aspect of the current system and do whatever work addresses it.

State your determination explicitly at the start of each session, so the next application of this prompt has a clear record of what you inferred and why.

Before doing any substantive work, read everything the workspace has preserved about prior decisions. If an idea was considered and rejected earlier, do not silently re-propose it. If you believe a rejected idea deserves reconsideration, cite the prior rejection and explain what has changed. Continuity of reasoning is the whole point of preserving provenance.

Substantive work in this methodology should not be done by a single perspective. Convene a group of AI agents with genuinely different viewpoints suited to the work at hand. Some perspectives generate options, some challenge them, some attend to what is unknown, some attend to what has been ignored, some reason about how the work will be received by those who must live with it. The specific perspectives, their number, and how they collaborate are for you to develop. Over repeated applications, patterns will emerge — document them when they do, so future applications can build on what worked.

The work should produce a concrete output: a structured record of what was proposed, what was decided, what was rejected with reasoning, and what remains uncertain. This record is the provenance. Commit it to the workspace in a way that preserves it permanently and makes it findable by future applications. Alongside the provenance, update or create whichever artefacts the work warrants. If the work produced a new specification, write the specification. If it produced an implementation, build it. If it surfaced problems, record them where subsequent work will find them. The structure of the workspace should evolve to serve the methodology, not the other way around.

Before ending the session, verify the workspace is in a coherent state. Specifications describe the engine as it currently is. Validations pass against those specifications, or their failures are documented as open issues for subsequent work to address. Any human-facing summary of the workspace accurately reflects its current state. Every piece of work done in this session has committed its provenance.

## Rules that hold across applications

These rules apply to both the self-development application and to external-problem applications of the engine.

Do not import ideas from outside the process. If an insight arrived through reading something unrelated, a conversation with a human, or your own pretraining, introduce it as an input to an explicit surveying or hypothesising step rather than committing it directly. The value of this methodology is that its artefacts are traceable to the reasoning that produced them.

Do not skip steps. Each piece of work's output is the next piece's input, and skipping breaks the chain of reasoning that makes the methodology evolveable.

Do not overwrite prior specifications silently. When a specification is revised, preserve the prior version and make the succession traceable. The form of that preservation — filenames, directory structure, supersession markers, or something else — is for you to develop. Whatever you choose, be consistent so future readers can follow the thread.

Preserve all provenance. Do not delete historical records, even when they feel embarrassing or outdated. A rejected idea from long ago may be the key to understanding a decision made today.

Leave the workspace in a coherent state at the end of every application. If a piece of work cannot complete, commit what was produced, document the blocker, and end cleanly rather than leaving work in an indeterminate state.

## Now begin

Read the workspace. Determine what state it is in. Read prior provenance. Convene the perspectives suited to the work at hand. Do the work. Commit its outputs and its record. Report what was done, what state the workspace is now in, and what the next application should address.

exec
/bin/zsh -lc "sed -n '1,220p' specifications/engine-manifest.md" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "sed -n '1,260p' tools/validate.sh" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
---
title: Engine Manifest
version: 1
status: active
created: 2026-04-22
last-updated: 2026-04-22
updated-by-session: 021
supersedes: none
---

# Engine Manifest

## Purpose

This specification names what constitutes the **Selvedge engine** at any given engine version. The engine is the current loadable implementation of the Selvedge methodology (per `identity.md` v2 layered denotation): a file set that, when loaded together, executes the methodology's nine-activity process against an application's context. The manifest makes the engine pointable-at, versionable, and cleanly separable from the workspace's own development-provenance.

Created Session 017 per D-074 as the resolution of OI-017 (engine-vs-methodology reframing). Its minimal scope is deliberate: the manifest enumerates and declares invariants, but does not restate the content of the specifications it enumerates.

## Specification

### 1. Engine definition

The **Selvedge engine** is the current loadable implementation of the Selvedge methodology, consisting of the file set enumerated in §3 at the engine version named in §2. Loading the engine means having these files available and treating them as a closed unit for the purposes of executing a session.

The engine is distinct from:
- The **methodology** — the abstract-approach, domain-general mechanic that the engine realises (named "Selvedge" per `identity.md` v2).
- The **development-provenance** — the self-development application's own accumulated reasoning trail (`SESSION-LOG.md`, `open-issues.md`, `provenance/`).
- Any **specific application** — a particular run of the engine against a problem (self-development or external-problem).

### 2. Current engine version

**`engine-v2`** (established Session 021 per D-082).

Subsequent engine versions (`engine-v3`, `engine-v4`, ...) increment per the versioning discipline in §5. The current engine version is always named by this §2.

### 3. Engine-definition files at `engine-v2`

The following files constitute the engine at the current version:

| File | Role |
|------|------|
| `PROMPT.md` | Thin dispatcher: names the three layers and two operating modes; points to `prompts/development.md` and `prompts/application.md`. |
| `prompts/development.md` | Executable prompt for the self-development application (this workspace's entry point). |
| `prompts/application.md` | Template prompt for external-problem applications (loads the engine by reference to this manifest; specifies application-context slots). |
| `specifications/methodology-kernel.md` | Kernel: defines the nine-activity execution semantics. |
| `specifications/multi-agent-delibera