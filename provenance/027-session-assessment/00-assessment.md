---
session: 027
title: Assessment — Folder-naming discipline deliberation; operator-surfaced convention drift
date: 2026-04-23
status: in-progress
engine_version_loaded: engine-v4
---

# Session 027 Assessment

## §1 Read

### §1a Default-read surface (per `read-contract.md` v2 §1)

Read in full at session open:

- **Dispatcher and prompts.** `PROMPT.md`; `prompts/development.md`; `prompts/application.md`.
- **Engine manifest.** `specifications/engine-manifest.md`.
- **Active specifications.** `specifications/methodology-kernel.md` v5; `specifications/workspace-structure.md` v4; `specifications/multi-agent-deliberation.md` v4; `specifications/read-contract.md` v2; `specifications/validation-approach.md` v5 (honest-limit: read prior to session for context; structural-check gating-conventions consulted in §3 below rather than re-read in full this open); `specifications/identity.md` v2 (honest-limit: not re-read this open; carries three-layer denotation; not load-bearing for folder-naming question); `specifications/reference-validation.md` v2 (honest-limit: not re-read this open; sealed three-cell protocol; not load-bearing for folder-naming question).
- **Session index.** `SESSION-LOG.md` (Sessions 001-026).
- **Open-issues index.** `open-issues/index.md` (13 active; OI-018 deferred with R9 escalation aged out).
- **Prior close files.** Session 026 close read in full (`provenance/026-session-assessment/03-close.md`). Session 015 close read in full as the load-bearing precedent case for placeholder-folder-name convention. Sessions 002-014, 016-025 `03-close.md` files not re-read in full this open; content consulted via `SESSION-LOG.md` thin-index and Session 026 close's documented history of runway/counter state. Honest-limit declared: the folder-naming deliberation's load-bearing precedent is Session 015 (single-perspective planning → placeholder kept); Session 022 (renamed to reflect content); Sessions 023/024 (substantive work but placeholder kept — the drift the operator surfaced). These three precedents are covered by direct reads in this session or Session 026's detailed consultation. No other prior-close content is load-bearing for this session.
- **Current-session provenance.** `provenance/027-session-assessment/` contains only this `00-assessment.md` at commit time of the open.

### §1b Archive-surface records consulted

None relied on for load-bearing claims this assessment. No archive-token citations produced by this file (the `[archive: path]` convention per `read-contract.md` §6 is not exercised this session — no archive-surface record is load-bearing for the folder-naming deliberation).

## §2 Session 026 synthesis-fidelity audit

Per Session 026 close's §Next Session item 2, narrower audit surface than deliberation sessions — three specific audit points from that close.

### §2.1 D-092's recording of the R9 escalation-window closure

Session 026 D-092 recorded both Path A ratification and the D-086 R9 cadence-escalation window aging out. The close asked whether the R9 closure should have been noted only in D-093 housekeeping rather than as part of D-092's normative content.

Finding: D-092's placement is defensible. R9 was defined at Session 023 as firing on any further engine-v-bump in 024/025/026. Session 026 is the pivot session closing that window. The aging-out is a pre-committed trigger's disposition at its own terminal clock — the decision to accept aging-out-as-resolution (rather than, say, re-activating the cadence concern on content grounds) is a genuine D-092 decision content. D-093 would have been weaker placement because D-093 carries "housekeeping" framing; R9's closure is load-bearing for §5.4 Session 022 cadence minority's future activation mechanism. No revision warranted.

### §2.2 D-092's R2 condition-(ii) call repeats Session 025's observational-only limitation

Session 026 applied D-088 R2 condition-(ii) "content-driven" test to a null edit (no MAD edit proposed), trivially returning content-driven-negative. Session 026 close flagged this as "observational-only" and flagged the first-real-exercise as still pending.

Finding: the observational-only framing held faithful. Session 027 proposes no MAD edit; the test remains unexercised. However, Session 027 will propose a minor amendment to `workspace-structure.md` (not the MAD file). This is not a test of R2 condition-(ii) — condition (ii) is scoped to the multi-agent-deliberation.md file specifically, not to any spec edit. No misapplication; the test remains pending a future session proposing an MAD edit.

### §2.3 Whether R9 aging-out warranted §5.4 content re-examination independent of R9

Session 026 treated R9's closure as mechanical aging-out without re-deliberating §5.4 on content grounds. The close flagged this as a possible audit concern — whether passive treatment was appropriate.

Finding: passive treatment was appropriate at Session 026 because no Session 026 work created grounds for content-level §5.4 re-examination. Session 026 was Path A carry-the-warning with no engine-v bump proposed. §5.4's minority warrant is "three engine-v-bumps in four adjacent sessions OR external-application portability confusion" — the original pattern. At Session 026's close, the pattern was 3-of-7 (non-firing), and no external-application portability confusion was observed this session. No content case surfaced. Session 027+ re-examination on content grounds remains available if a future engine-v bump is proposed.

### §2.4 Additional finding not in Session 026's audit agenda

Session 026 close did not itself flag the folder-naming drift. The operator surfaced it at Session 027 open. This is a **new-eyes finding** the prior session's self-audit did not produce, paralleling the Session 015 pattern of an opening session surfacing an observation the prior close's self-assessment did not flag. Recorded here as an observation about the audit-at-N+1 discipline: audits-of-prior can miss patterns that span multiple sessions because the single-session audit frame sees only the immediate prior session's content.

## §3 Workspace state at open

### §3a Validator baseline

`tools/validate.sh` at session open: 680 pass, 2 fail, 1 warn.

**Two failures are expected opening-state:**
- `Session 027 missing from SESSION-LOG.md` — clears at close when Session 027 entry added per R8a thin-index form.
- `027-session-assessment — empty (no .md files)` — clears as soon as this `00-assessment.md` is committed.

**One warning persists (designed):**
- `specifications/multi-agent-deliberation.md` at 6,386 words exceeds 6,000-word soft warning (within 8,000 hard ceiling). Per Session 024 D-088 R1 + D-090 + D-092 this is the designed carry-the-warning state; Session 027 does not propose an MAD edit, so the warning persists. Five consecutive session opens with MAD held at 6,386.

### §3b Aggregate default-read surface report

At session open (per check 20 §2a informational): **99,087 words across 38 files** (live validator measurement at open; matches Session 026 close projection). Advisory threshold ≥90,000 crossed since Session 024 close; activation threshold ≥100,000 **not yet reached but within 913 words**. Session 026 close warned that any Session 027 `03-close.md` over ~468 body words would push aggregate over 100,000 by accretion alone; Session 027 is a substantive deliberation producing a spec amendment, so its close will be larger than 468 body words. **Activation crossing is likely this session.**

Key note per §5.3 Pacer minority framing: the activation warrant is "aggregate ≥ 100,000 OR aggregate grows >10% in a single session without compensating restructure." A substantive-deliberation session that produces spec-revision content is not the accretion failure mode the minority targets; the minority's target is verbose-close accretion across Path-A no-substance sessions (Session 026 close flagged close-verbosity pattern n=2). Session 027 is neither Path A nor no-substance, so the growth this session is in-scope content, not accretion.

### §3c §5 minority counter states at open

Per Session 026 close:

- **§5.1 Splitter A.2 counter**: zero (no content-completion case surfaced since D-088 adoption).
- **§5.2 Session 023 Skeptic vindication runway**: 4-of-5 sessions elapsed with conditions holding (Sessions 023/024/025/026). **Session 027 is the final session in the runway.** If conditions hold through Session 027 close (no default-read file above 7,500 words; no restructure-for-budget event), Skeptic no-change + warrant-literalism minority is retroactively vindicated per `read-contract.md` v2 §5.2.
- **§5.3 Pacer aggregate-hard-budget minority**: not activated (aggregate under 100,000 at open; Session 027 close likely crosses). If activation fires at close, §5.3 minority becomes first-activation candidate; deliberation of adopting aggregate hard budget becomes appropriate at Session 028+.
- **§5.4 Session 022 engine-v-cadence minority**: activated-not-escalated; D-086 R9 escalation-window aged out at Session 026 close; operates on content grounds alone at Session 027+.
- **§5.5 tokeniser-drift watch minority**: no single-Read failure observed on default-read files; not activated.

Plus five Session 024 minorities from D-088 A.4 deliberation (Splitter A.2; Archivist A.3; Skeptic A.1; Outsider carry-the-warning; plus the converged position) — all preserved unchanged at Session 026 close, carry forward unchanged to Session 027.

### §3d Other state

- **MAD status**: 6,386 words; five consecutive session opens at this count.
- **OI-004 tally**: 8-of-3 required; voluntary:required 9:8; criterion-3 cumulative 67. State 3 (Articulated; awaiting closure-retrospective).
- **OI-018**: Open — deferred; R9 activation trigger aged out at Session 026 close; remaining activation trigger is "external-application portability confusion" (unexercised) or operator-directed prospective engagement.
- **Engine-v4 preserved** across Sessions 024/025/026; four consecutive non-bump sessions since engine-v4 adoption.

## §4 Operator agenda

At Session 027 open, the operator surfaced an observation prior to session dispatch:

> "Operator notes the last 4 provenance folders are all named 'session-assessment' and not renamed."

Factual verification:

| Session | Folder name | Content | SESSION-LOG title (abbrev.) |
|---|---|---|---|
| 023 | `023-session-assessment` | Substantive (engine-v4 bump; read-contract.md v1→v2) | "Read-Contract Budget Recalibration; engine-v3 → engine-v4" |
| 024 | `024-session-assessment` | Substantive (D-088 A.4 carry-the-warning; R6 cleanup) | "MAD 6K-Soft-Warn Response — A.4 Carry-the-Warning" |
| 025 | `025-session-assessment` | Path A execution; D-090/D-091 both `[none]` | "Path A Executed — Carry-the-Warning Continues" |
| 026 | `026-session-assessment` | Path A execution; D-092/D-093 both `[none]` | "Path A Executed — D-086 R9 Cadence-Escalation Window Ages Out" |

Historical comparison (sessions that received meaningful folder names reflecting content):

- `017-oi017-reframing-deliberation`, `018-reference-validation-exercise-1`, `019-reference-validation-revision`, `020-workspace-scaling-deliberation`, `021-oi004-criterion4-articulation`, `022-workspace-scaling-trajectory` — each renamed from opening default to reflect session content.

Placeholder-kept precedent:

- `015-session-assessment` — single-perspective planning session; one `[none]` decision; no spec revision. Close file characterises it as "Session 002 precedent for minimal no-deliberation sessions."

**Pattern observed**: opening default folder name is `NNN-session-assessment`. The practice of renaming at close to reflect content exists but is not specified in `workspace-structure.md` v4 §provenance or in `prompts/development.md`. The convention has been informally observed (020/021/022 rename cases) or informally broken (023/024 substantive cases kept placeholder) without any explicit governance.

The operator ratified option 2 from the pre-session exchange: "Treat this as the sole agenda for Session 027 — deliberate the folder-naming discipline, produce a minor amendment to `workspace-structure.md` or `prompts/development.md`, and optionally authorise a retroactive rename with an explicit dispensation against D-017 for path-string updates."

## §5 Scope of the Session 027 deliberation

### §5a In-scope

1. **Folder-naming convention for `provenance/NNN-title/`** — what "title" means; when it is chosen; who has authority to change it.
2. **Close-step obligation** — whether the session's close should include an explicit folder-naming decision (rename-or-affirm-placeholder).
3. **Retroactive disposition** of Sessions 023/024/025/026 folder names — rename with dispensation against D-017 for path-string updates, or leave as historical record.
4. **Opening default name** — whether `NNN-session-assessment` is the right opening default or should change (e.g., `NNN-opening`, `NNN-<date-stamp>`, `NNN-pending-title`).
5. **Spec-location of the rule** — `workspace-structure.md` v4 §provenance, `prompts/development.md`, or `read-contract.md` (unlikely).

### §5b Out-of-scope

1. **Other provenance naming conventions** — `00-assessment.md`, `01-brief-shared.md`, etc. These are already specified and not under drift.
2. **Applications-directory naming** (`applications/NNN-slug/`). Not surfaced by the operator observation.
3. **Renumbering sessions**. Session numbers are immutable.
4. **Archive-pack naming**. Stable per `read-contract.md` v2 §5.
5. **Wholesale revision of `workspace-structure.md`** — scope this session at minor-amendment level per OI-002 heuristic. Engine-v bump only if amendment qualifies as substantive (likely not — adding a close-step is within existing spec scope).

### §5c Trigger-coverage analysis (per `multi-agent-deliberation.md` v4)

- **d016_1** (modifies methodology-kernel.md): NO. Session 027 does not propose a kernel revision.
- **d016_2** (creates or substantively revises a spec in `specifications/`): **conditional** — if the amendment is substantive per OI-002 heuristic, this fires. Current scoping is minor (adding a close-step is within existing §provenance scope and doesn't change file classes/top-level structure). The deliberation itself decides minor-vs-substantive. **Mark this session as d016_2-conditional-on-outcome.**
- **d016_3** (reasonable practitioners could disagree; ≥2 plausible positions namable before deliberation): **YES**. Author can name ≥4 plausible positions:
  - G1: leave as-is; operator observation noted, no spec change.
  - G2: forward-rename-at-close-when-substantive discipline; add close-step; no retroactive action.
  - G3: G2 plus retroactive rename with D-017 dispensation for path-string updates.
  - G4: drop renaming practice entirely; standardise on `NNN-session-assessment` forever; amend spec to name the default as the permanent form.
- **d016_4** (load-bearing for another reason): YES. The pattern surfaced by operator is data about the engine's self-observability — missed in four consecutive self-audits. The deliberation's output shapes whether that class of drift is governable.

**d016_3 and d016_4 fire**. Multi-agent deliberation is required.

- **d023_1** (modifies methodology-kernel.md): NO.
- **d023_2** (creates or substantively revises `multi-agent-deliberation.md`): NO.
- **d023_3** (creates or substantively revises `validation-approach.md` Tier 2): NO (no Q1-Q9 edit proposed; potentially a new Tier 1 check but that's check-namespace not Tier 2).
- **d023_4** (asserts OI-004 state change): NO.

**d023_* does not fire**. Non-Claude participation is not required. Recommended status available; Session 027 operator did not convene an Outsider pre-session, and the external-signal role (surfacing the drift) was filled by the operator's own observation — functionally equivalent to an Outsider intervention. **Session 027 will not convene a non-Claude participant this session.** Voluntary:required ratio remains 9:8 (unchanged); this session does not claim non-Claude narrowing.

## §6 Determination

Session 027 is a **three-perspective Claude-family deliberative session** on the folder-naming discipline question. Produces:

1. A synthesis (`01-deliberation.md`) of perspectives' positions with minority preservation.
2. Decisions (`02-decisions.md`) — expected D-094 resolving the convention; possibly D-095 for retroactive disposition; possibly D-096 for OI housekeeping.
3. A spec amendment to `workspace-structure.md` (most likely minor per OI-002; substantive-vs-minor is itself a deliberation question).
4. Close with Tier 2 guided-assessment (`03-close.md`).

No Outsider convened. No external artefact. No MAD edit. No engine-v bump unless deliberation produces a substantive spec revision (judged at Decide time).

### §6a Convening — perspectives to run

Three perspectives with genuinely different stakes in the question:

- **Archivist** — holds D-017 immutability as load-bearing; distrusts retroactive edits even with dispensation; preservation-first; skeptical of adding ceremony around folder-naming. Adversarial role: if deliberation drifts toward retroactive repair, Archivist argues preservation.
- **Discoverer** (pragmatist framing) — discoverability and navigation are the load-bearing properties a folder name serves; the opening-default placeholder is a design miss; forward discipline plus retroactive repair is worth the D-017 cost if the cost is scoped (path-strings inside the renamed folders, not content mutations).
- **Minimalist** — the engine is adding discipline faster than it's removing it (OI-007 scaling pressure); the operator observation is real but the right answer might be to stop renaming entirely, standardise on the placeholder, and remove the informal rename practice rather than formalise it.

Adversarial coverage: Archivist and Minimalist both provide adversarial pressure from different angles (preserve vs. simplify); Discoverer is the forward-momentum position. Expected disagreement: Archivist vs. Discoverer on retroactive rename; Minimalist vs. both on whether to add rules at all.

### §6b Non-convening — rationale for Claude-only

Per §5c trigger analysis, d023_* does not fire. Optional-recommended, not required. Operator's observation (which could have been an Outsider's job) arrived externally at session open — the adversarial-external function is already served. Voluntary:required ratio 9:8 has sufficient runway; Session 027 skip does not regress the ratio below 1.0.

### §6c Spec-revision scale

Amendment will be framed as **minor per OI-002 heuristic**: adding a close-step obligation to `workspace-structure.md` §provenance is within existing §provenance scope and does not change file classes, top-level structure, or the `NNN-title/` naming convention itself (which already permits any descriptive title). Engine-v4 preserved unless deliberation produces a larger change.

## §7 Honest-limits summary

- **Specifications not re-read in full this open**: `validation-approach.md` v5, `identity.md` v2, `reference-validation.md` v2. All three are not load-bearing for folder-naming discipline. Honest-limit: if the deliberation surfaces a cross-spec dependency I did not anticipate, I will halt and read.
- **Prior session closes not re-read**: 002-014, 016-021, 023-025. Relied on SESSION-LOG.md thin-index and Session 026 close's documented runway/counter state. Honest-limit: if a perspective cites a prior-session rejection I need to verify, I will read that close before proceeding.
- **Per-OI files not read at session open**: none of the 13 active OIs are load-bearing for folder-naming discipline per §5 scope. Honest-limit: if deliberation touches OI-002 (minor vs. substantive heuristic) or OI-007 (scaling), I will read those per-OI files before the relevant decision.
- **Archive records not consulted**: none relevant to folder-naming question.

## §8 Halt (for perspective convening)

Proceeding to write `01-brief-shared.md` and convene perspectives. No operator halt solicited between §6 convening determination and perspective dispatch; the operator's pre-session ratification of option 2 is the authorisation for this deliberation's shape. Operator may redirect at any point.
