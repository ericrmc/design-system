---
session: 003
title: Shared brief — Session 003 deliberation (system-model v2 multi-view revision)
date: 2026-04-24
status: complete
engine_version: engine-v7
---

# Shared brief — Session 003 deliberation

This file captures the non-role-specific content distributed to every
perspective in Session 003's deliberation per MAD v4 §Stance Briefs.
Sections 1 (Methodology context), 2 (Problem statement), 3 (Design
questions), 5 (Response format), and 6 (Constraint on external
imports) are byte-identical across all perspective briefs. Each
perspective receives an additional Section 4 (Role-specific stance)
not preserved in this file — those role-specific sections appear only
in the per-role `01A`/`01B`/`01C`/`01D` prompt files.

## 1. Methodology context

You are participating in a multi-agent deliberation under the Selvedge
engine at `engine-v7`. The engine is the current loadable
implementation of a self-hosting methodology for specification-driven
multi-perspective reasoning: perspectives reason independently, a
synthesiser merges them, decisions are recorded with rejected
alternatives preserved, and provenance is kept verbatim.

This workspace is the **external-problem application of the engine
to a fictional disaster-response scenario** (Laurel Delta, Nivaro;
workspace_id `selvedge-disaster-response`). The brief is entirely
fictional — no real geography, no real disaster case, no real
emergency-management protocol is in scope (`CON-01` in the
assumption ledger, anti-laundering per PROMPT.md external-imports
rule).

Session 001 produced v1 of the **system model** (a typed dependency
map of Laurel Delta at T0+36h: populations `POP-*`, infrastructure
`INF-*`, services `SVC-*`, dependencies `DEP-*`, external interfaces
`EXT-*`, first-class silences `SIL-*`) and v1 of the **assumption
ledger** (43 rows typed `GIV-*` / `CON-*` / `ASM-*` / `DEC-*` /
`EXT-SURVEY-*`). Session 002 produced v1 of the **risk register**
(22 `RSK-*` entries) and v1 of the **response plan** (23 `ACT-*`
actions in 11 concurrent service-family streams). All four
artefacts carry `validation: workspace-only` per kernel v6 §7.

Session 002 activated a first-class preserved minority from Session
001: the **§5.1 Adversarial Skeptic single-document-form dissent**.
The Session 001 v1 model is a single-document shape — populations,
infrastructure, services, dependencies, external interfaces, and
silences in six sections. The §5.1 minority argued for a multi-view
shape (e.g., settlement-local topology + cohort × service + per-
service dependency chain) on the grounds that a flat shape forces
readers to re-derive dependency chains under session pressure. The
warrant fired at Session 002 close: across 5 perspectives, 23
independent instances of re-derivation cost were recorded; every
perspective individually exceeded the ≥3-instance activation
threshold. Per Session 002 D-019: *"The multi-view model form is the
preferred revision direction for Session 003 or later."*

Session 003's **primary increment** is producing v2 of
`system-model.md` in a multi-view form that reduces the
re-derivation cost observed at Session 002 while preserving the v1
ID discipline, cohort individuation, silence visibility, and
anti-laundering posture.

Session 002 D-018 additionally flagged `ASM-19` (central-government
counterparty reliability) for split into two rows: `ASM-19a`
recipient-reliability (the 10-day plan has a fillable recipient)
and `ASM-19b` delivery-reliability (any action that requires
`EXT-01` as delivery partner depends on a different reliability
claim). The split is a small ledger update tightly coupled to any
v2 view that exposes external-actor topology.

## 2. Problem statement

Design the shape of `applications/001-disaster-response/system-
model.md` v2. The revision must:

- **Reduce re-derivation cost** for the kinds of dependency-chain
  reasoning that Session 002 repeatedly performed (e.g., "for
  `POP-09` dialysis, the chain is `SVC-03` → `INF-04` inaccessible
  → referral via `INF-02` requires `SVC-07` requires `INF-15`
  requires `ASM-11` persistence"). A v2 that natively exposes such
  chains saves Session 004+ from re-deriving them.
- **Preserve every v1 ID** (`POP-*`, `INF-*`, `SVC-*`, `DEP-*`,
  `EXT-*`, `SIL-*`). Downstream artefacts `risk-register.md` and
  `response-plan.md` cite v1 IDs; those citations must remain
  resolvable after v2 adoption.
- **Preserve cohort individuation** (`POP-08` through `POP-15` remain
  first-class, not collapsed into `POP-5K-parent` or aggregate
  cohorts).
- **Preserve silence visibility** (`SIL-*` entries remain first-
  class, not buried inside notes columns of view tables).
- **Avoid laundering external taxonomies** into view structure
  (UN/IASC cluster catalogues per `EXT-SURVEY-02`; lifelines /
  critical-infrastructure-sector taxonomies per `EXT-SURVEY-04`;
  ICS/NIMS per `EXT-SURVEY-01`; enterprise-architecture view
  frameworks like TOGAF / Zachman from pretraining). Any view shape
  that resembles these must be surveyed-and-adopted-with-reason
  rather than silently imported.
- **Remain readable** under the `read-contract.md` v4 §2 8,000-word
  per-file hard ceiling (with 6,000-word soft warning). The
  application-artefacts directory is not on the default-read
  surface (artefacts in `applications/NNN-<slug>/` are application-
  scope, not default-read per `read-contract.md` §1); the per-file
  budget technically does not apply, but an 8,000-word ceiling is a
  good readability heuristic. Exceeding 10,000 words would be a
  readability concern regardless of where the file sits.

Revision scope for this session:

1. `system-model.md` v2 shape (primary).
2. `assumption-ledger.md` `ASM-19` split into `ASM-19a` /
   `ASM-19b`.
3. Optionally `POP-12` sub-individuation (`POP-12a` oxygen /
   `POP-12b` CPAP) iff the v2 shape exposes them naturally.

**Out of scope**: revising `risk-register.md` or `response-plan.md`
in this session. Downstream v1.1 work inherits from v2 but is
Session 004+ work per Session 001 D-009 increment-boundary
discipline. If v2 shape decisions imply v1.1 work, flag it for
Session 003's close narrative to hand forward.

## 3. Design questions

Answer each question from your role's stance. Cite specific v1 IDs,
specific Session 002 re-derivation instances, or specific external
frames as the context requires. Quote specific language where your
argument turns on it rather than paraphrasing.

**Q1. View count and axes.** How many views should `system-model.md`
v2 contain, and what axis organises each? Candidate axes surfaced
by Session 002 re-derivation patterns: (a) cohort × service
dependency (for each `POP-*`, the services it consumes and the
infrastructure those services require); (b) service chain
(upstream-to-downstream `SVC-*` through `DEP-*`); (c) settlement-
local topology (what lives where); (d) external-actor / `EXT-*`
view (what depends on which external counterparty, split by
recipient vs delivery roles per D-018 flag); (e) silence / evidence
view (`SIL-*` organised by which model elements they touch). Is
there a minimum set? A maximum? Should the v1 single-document form
be retained as a base layer plus views, or replaced entirely, or
subsumed as one view among several?

**Q2. ID discipline.** How should v1 IDs relate to v2 view entries?
Are v1 IDs still canonical? Does each view add view-scoped derived
rows (e.g., a cohort × service view row might be keyed as
`COH-POP-09`), or does each view just re-organise existing IDs in a
new layout? What discipline prevents ID drift between views — i.e.,
ensures that `POP-09` in the cohort view is the same entity as
`POP-09` in the settlement view? Is ID-preservation enforced by
discipline or by a mechanical cross-reference?

**Q3. `ASM-19` split.** Per D-018, split `ASM-19` into `ASM-19a`
(recipient-reliability — `EXT-01` can receive the 10-day plan and
acknowledge it) and `ASM-19b` (delivery-reliability — `EXT-01` can
execute specific delivery commitments: fuel logistics, sea/air lift,
etc.). What falsifier does each row carry? Do both rows need review
triggers? Should the v2 model expose the two aspects separately as
attributes on `EXT-01` (e.g., split the external-actor view into
recipient-role + delivery-role sub-views)? Should `RSK-019` (the
cross-cutting risk in the risk register) be updated to reference
both `ASM-19a` and `ASM-19b` explicitly? (Note: risk-register
update is out-of-scope for this session per §2; flag the update as
Session 004+ follow-on if you propose it.)

**Q4. `POP-12` sub-individuation.** Should `POP-12` (CPAP / home-
oxygen dependents) split into `POP-12a` (oxygen-dependent, hours-
band time-to-harm) and `POP-12b` (CPAP-dependent, 1–3 days band)
as first-class cohorts at v2? Session 001 D-007 declined on count-
silence grounds (`ASM-06`: sub-cohort size distribution not
specified). Session 002 [`01C`, Q2] named the internal split as
structurally invisible — a §5.1 re-derivation instance. If
splitting, what is the falsifier for each sub-cohort's count
silence? If not splitting, how should v2 expose the clinical
time-to-harm differentiation that the dual-window treatment on
`RSK-004` captures only awkwardly?

**Q5. Migration and supersession.** How is v1 preserved when v2 is
committed? Candidate forms:
- **Form A — supersession-chain file.** `system-model-v1.md` kept
  in the application directory with `status: superseded` and
  `superseded-by: system-model.md`; v2 takes the canonical
  filename. Parallels the specifications-directory v-suffix
  convention.
- **Form B — copy-plus-reference.** Per `workspace-structure.md` v5
  §applications regularization clause: keep the v1 provenance
  witness at `provenance/001-session/` (it does not exist there in
  this workspace — v1 was produced directly in `applications/`);
  copy v1 to `applications/001-disaster-response/system-model-
  v1.md` as a historical witness; v2 takes the canonical filename.
  Matches Session 009 D-054 precedent.
- **Form C — git-history-only preservation.** v2 replaces v1 in
  place; v1 is recoverable via `git log` / `git show HEAD~`;
  `last-revised-session: 003` on the replacement file makes the
  history findable. Lightweight but relies on version-control
  transparency.
What frontmatter carries the supersession marker (the existing v1
frontmatter has `originating_session`, `artefact_kind`, `domain`,
`engine_version`, `validation`, `status`, `created`,
`last-revised-session` per Session 001's produce step; v2 needs
either a `supersedes:` field or a `version-history:` field if we
want the chain legible without reading git).

**Q6. Risk-plan downstream impact.** If v2 natively exposes
dependency chains, do any v1 `RSK-*` or `ACT-*` rows become visibly
under-specified? Specific candidates worth checking:
- `RSK-014` (regional-hospital generator fuel exhaustion — multi-
  downstream; `cohort_affected:` currently blank; chains to
  `POP-10` dialysis, `POP-11` neonatal, `SVC-01` acute).
- `RSK-019` (`EXT-01` counterparty reliability — cross-cutting;
  traverses four streams; would a per-external-actor view make the
  cross-cutting shape computable?).
- `ACT-005` (cold-chain spanning `POP-13`/`POP-14`/`POP-15` with
  differing sub-cohort windows; Session 002 flagged this as a
  §5.1 re-derivation instance).
- Any `RSK-*` whose `dependency_chain` column was sparse at v1
  despite referencing multiple infrastructure nodes (`RSK-015`
  freight-rail-bridge + fibre shared-fate; `RSK-008` aged-care
  cluster welfare).
Flag cases where v2 shape would make a v1.1 risk or action
specification visibly thinner than v2 supports. This feeds Session
003 close's "decisions-not-taken" forwarding to Session 004+.

**Q7. Anti-laundering check.** Which external frames risk being
laundered into v2's view structure if adopted without explicit
surveying? List the external frames your proposed v2 shape
resembles (even partially). Explicitly state for each whether it
was surveyed and declined at v1 per `assumption-ledger.md`
`EXT-SURVEY-*` rows, or whether you are proposing adoption-with-
reason, or whether you are ambivalent. Do not adopt any frame
silently. Specific frames to check against: UN/IASC clusters
(`EXT-SURVEY-02` declined-v1); lifelines / critical-infrastructure-
sector taxonomies (`EXT-SURVEY-04` declined-v1); ICS/NIMS
(`EXT-SURVEY-01` declined-v1); enterprise-architecture view
frameworks (TOGAF view catalogues, Zachman rows/columns, C4-model
layers) not explicitly surveyed at v1; systems-dependency-modelling
frames (DoDAF views, ArchiMate layers, causal-loop diagrams).

## 4. (Role-specific stance)

Your role-specific stance appears in the per-role prompt file. It
is the only section that varies between perspectives.

## 5. Response format

Respond in Markdown with one top-level section per question
(`## Q1`, `## Q2`, etc., through `## Q7`). Length target:
900–1,800 words total across all seven questions, with uneven
distribution permitted as the questions require (Q1 and Q5 may
warrant more; Q3, Q4 may be shorter). A closing `## Honest limits`
section (up to 200 words) records what you cannot answer from the
brief alone.

Quote specific v1 IDs (`POP-09`, `ASM-19`, `SIL-01`, etc.) and
cite the deliberation artefacts where your position depends on them
(`[Session 001 01-deliberation.md §5.1]`,
`[Session 002 01-deliberation.md §5.2]`, etc.). Where you disagree
with another perspective, name the specific claim you disagree with
rather than gesturing at a general position.

The response will be committed verbatim into this session's
provenance as `01<letter>-perspective-<role>.md`. Brief editing for
markdown-formatting-only is permitted; substantive content is
immutable per D-017 + `workspace-structure.md` §provenance.

## 6. Constraint on external imports

Per PROMPT.md anti-silent-import rule and per OI-015 laundering-
enforcement: reason primarily from this brief and from the v1
artefacts summarised here. If an insight arrived from pretraining
(a recognised pattern, a standard framework, a canonical emergency-
management convention), name the source frame explicitly in your
Q7 answer and mark it as either surveyed-and-decline-to-adopt,
surveyed-and-adopt-with-reason, or ambivalent. Do not commit
pretrained frames directly to view proposals; surface them through
Q7.

Specifically forbidden: applying UN/IASC cluster catalogue as view
structure; applying ICS/NIMS as view structure; applying Sphere
Handbook or lifelines-sector taxonomies as view structure — all
surveyed and declined at Session 001 per `EXT-SURVEY-*` rows. If
your proposed view shape happens to resemble one of these, your Q7
answer must name the resemblance, state whether the view shape is
derived from the brief or from the frame, and if from the frame,
argue for adoption-with-reason.

The adversarial visibility purpose of Q7 is the primary
anti-laundering defence. A perspective that does not answer Q7
substantively weakens the deliberation's defence. Skipping Q7 is
recorded as a refusal, preserved per MAD v4 §Graceful Degradation.

---

## Supplementary context: v1 artefact summaries

Each perspective has access to these summaries via the brief; full
v1 artefact text is in `applications/001-disaster-response/` and
is the canonical reference. These summaries are informational; any
claim you make that turns on specific v1 content should cite by ID
and may quote the canonical file.

### v1 system model — shape summary

Six sections: §1 Time-frame (`WIN-acute`, `WIN-stab`); §2 POP-*
(structural, age, medical-fragility, access-constrained cohorts —
24 `POP-*` entries); §3 INF-* (health, water, power, transport,
communications, shelter, logistics — 19 `INF-*` entries); §4 SVC-*
(15 services keyed by delivering `INF-*` and consuming `POP-*`);
§5 DEP-* (22 typed dependency edges); §6 EXT-* (3 external
interfaces); §7 SIL-* (24 first-class silences); §8 Out-of-scope
for v1; §9 Hand-off to Session 002.

Load-bearing discipline decisions embedded in v1 per Session 001
D-001 through D-010:
- **D-006** Attribute-indexed (populations / infrastructure /
  services keyed independently; settlement is an attribute, not a
  top-level axis).
- **D-001** First-class `SIL-*` silences.
- **D-003** Cohort individuation (medical-fragility cohorts
  first-class).
- **D-005** + `ASM-20` — no pretrained clinical time-to-harm
  numbers; qualitative window labels only.
- **D-010** Four-link traceability (every claim resolves from
  action → risk → service → infrastructure → assumption).

### v1 assumption ledger — shape summary

Single Markdown table, 43 rows, typed. Columns: `id`, `type`,
`statement`, `source`, `rationale`, `model_refs`, `dependents`,
`falsifier`, `review_trigger`, `status`. Rows split: 5 `GIV-*`
(given-flagged-for-survey); 5 `CON-*` (constraint); 21 `ASM-*`
(assumption, with falsifiers); 7 `DEC-*` (decision recorded in
model); 10 `EXT-SURVEY-*` (external frameworks surveyed-and-
declined). `ASM-19` is the single row D-018 flags for split.

### v1 risk register — shape summary (produced Session 002)

22 `RSK-*` entries organised across four cohort-fragility tiers
(per D-012). T1: 8 individuated medical-fragility cohort risks
(`RSK-001` through `RSK-008`); T2: 2 cohort-silence risks
(`RSK-009`, `RSK-010`); T3: 3 aggregate-population risks
(`RSK-011` through `RSK-013`); T4: 9 upstream-infrastructure /
silence-closing risks (`RSK-014` through `RSK-022`).

### v1 response plan — shape summary (produced Session 002)

23 `ACT-*` actions across 11 concurrent `STR-*` service-family
streams (per D-013). Sub-windows `WIN-acute` / `WIN-stab` treated
as review gates, not operational compartments (D-014). `ACT-022`
time-triggered gate at T0+72h; `ACT-023` information-triggered
gate when ≥4 of 8 priority `SIL-*` close. Actions carry
`actor_class` + `fallback_ref` per D-018.

### Session 002 re-derivation instance pattern (for §5.1 activation)

Across Session 002's 5 perspectives, 23 independent instances of
re-derivation were recorded in Q7 answers. Cleanest empirical
pattern: **per-service dependency chain**. Examples:
`SVC-03` → `INF-04`/`INF-01` → `INF-30` generator → `INF-32` fuel;
`SVC-08` cold chain → `SVC-05` power → `INF-11` grid OR
`INF-31` on-site generators; `SVC-13` telecoms → `INF-17` fibre via
`INF-14` bridge carriage (shared-fate). Every perspective
individually exceeded the ≥3-instance activation threshold. The
multi-view proposal in Session 001's 01C raw was specifically
cohort × service dependency + settlement-local topology + per-
service chain; that 3-view shape is one of the candidate v2 shapes
for this session to evaluate among others.
