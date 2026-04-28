---
session: 001
title: Decisions — Session 001
date: 2026-04-24
status: complete
---

# Decisions — Session 001

Each decision is traceable to the synthesis in `01-deliberation.md` and
to the raw perspective files cited inline. Triggers per MAD v4
§Trigger-Coverage Annotation Schema. This session is ≥ 006; the schema
applies.

## D-001: System model structural shape

**Triggers met:** [d016_3]

**Triggers rationale:** Reasonable practitioners could genuinely
disagree on model structure (multi-view vs single-document vs cohort-
first vs settlement-first). Four plausible positions were articulated
pre-deliberation; three-of-four cross-family convergence on a single
keyed-table structure was the outcome; 01C's multi-view alternative is
preserved as §5.1 first-class minority in `01-deliberation.md`.

**Decision:** The v1 system model is a single Markdown document at
`applications/001-disaster-response/system-model.md` containing these
keyed-table sections, each with row IDs:

- `POP-*` — Population cohorts (attribute-indexed, not settlement-
  indexed).
- `INF-*` — Infrastructure elements with T0 state and epistemic-source
  tag.
- `SVC-*` — Services (separate from the infrastructure that delivers
  them).
- `DEP-*` — Dependencies / relationships as typed edges.
- `EXT-*` — External interfaces (central government, local utility,
  highland interior).
- `SILENCE-*` — First-class unknowns the brief does not resolve.
- An "Out of scope for v1" section explaining exclusions.

**Why:** 3-of-4 cross-family convergence on the keyed-element shape
[01A, 01B, 01D]. Separation of services from infrastructure is
load-bearing [01A, 01B, 01D]: a service can fail while its
infrastructure stands. `SILENCE-*` as first-class realises 01B's
*"silences/unknowns as first-class entries"* requirement
[`01B-perspective-vulnerability-advocate.md`, Q1] and 01C's
*"explicit 'what is not in the model' register"*
[`01C-perspective-adversarial-skeptic.md`, Q1].

**Rejected alternatives:**

- **Multi-view model** (01C-proposed): settlement-local models + a
  dependency overlay, or population-indexed view alongside
  infrastructure-indexed view. Rejected for v1 on pragmatic grounds:
  Session 002 needs one artefact to key against. Preserved as §5.1
  first-class minority in `01-deliberation.md` with activation
  warrant.
- **Settlement-first indexing** (implicit default): rejected per
  D-006.
- **Diagrams-first representation:** rejected at v1 because a text
  representation is needed alongside per the engine's preference
  (`prompts/development.md` §preference for text-based artefacts);
  diagrams may be added as derivative.

## D-002: Assumption ledger structural shape

**Triggers met:** [d016_3]

**Triggers rationale:** Reasonable practitioners disagree on what
columns a ledger must carry; minimum-column alternatives were
articulated pre-deliberation. Four-of-four convergence on the
multi-column table shape; variations in column sets reconciled in
synthesis.

**Decision:** The v1 assumption ledger is a single Markdown table at
`applications/001-disaster-response/assumption-ledger.md` with the
following columns, all required on every row:

| Column | Purpose |
|---|---|
| `id` | Stable key: `ASM-01`, `CON-01`, `GIV-01`, `DEC-01`, etc. |
| `type` | `assumption` / `constraint` / `given-flagged-for-survey` / `decision` |
| `statement` | One sentence. |
| `source` | `brief:§X` quote-reference, `inferred-from`, `session-chosen`, or `external-surveyed`. |
| `rationale` | Why adopted. |
| `model_refs` | Keys in the system model this touches (e.g. `INF-07, DEP-12`). |
| `dependents` | What downstream reasoning rests on it (what breaks if false). |
| `falsifier` | What observation would invalidate it. |
| `review_trigger` | Event or time that should re-open it. |
| `status` | `live` / `retired` / `promoted-to-given`. |

**Why:** 4-of-4 convergence on a table with these columns
[01A, 01B, 01C, 01D]. 01B's non-negotiable on `dependents` and
`falsifier` columns adopted verbatim [`01B`, Q2]. 01A's equivalent
non-negotiable on `model_refs` and `affected_if_false` adopted in
synthesised form [`01A`, Q2].

**Rejected alternatives:**

- **Prose-list form:** rejected; loses audit metadata
  [`01B`, Q2: "A bare list loses the audit metadata that makes the
  ledger useful to Session 002"].
- **Separate files per assumption:** rejected at v1; single-table form
  is the simpler starting point and can be split later if ledger
  grows over budget.
- **Fewer columns (e.g., skipping `falsifier`):** rejected;
  *"an assumption with no falsification condition is a belief in
  costume"* [`01B`, Q2].

## D-003: Cohort individuation

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** d016_3: reasonable practitioners disagree
whether cohorts should appear as first-class model entries or be
aggregated. d016_4: operator-adjacent load-bearing designation —
cohort individuation is the load-bearing claim 01B flagged as
non-negotiable from the vulnerability-lens, and the synthesis adopted
it because failure here causes downstream response-plan harm
(*"the averages kill the dialysis patients"* [`01B`, Q3]).

**Decision:** Named medical-fragility cohorts appear as first-class
`POP-*` entries in the system model with vulnerability attributes and
explicit links to the services they consume:

- South Latch dialysis patients (~1,200; centre inaccessible T0)
- Merrow Port regional dialysis patients (~220)
- Merrow Port regional neonatal unit occupants (count unknown T0)
- CPAP / home-oxygen cohort (sub-set of ~5K; count decomposed where
  brief permits, else `count: unknown`)
- Insulin-dependent cohort (sub-set of ~5K)
- Refrigerated-biologic-dependent cohort (sub-set of ~5K)
- Other refrigerated-med dependents (sub-set of ~5K)
- Aged 70+ cohort (~18K; distributed across all three settlements)
- Institutionally housed aged (South Latch aged-care clusters;
  resident count unknown)
- Migrant-worker dormitory cohort (~9K; two non-majority languages)
- Outer-islet fishing community (count unknown)
- Displaced persons (~18K T0)

Plus structural populations (settlement totals) as additional `POP-*`
entries. These cohorts are **not** collapsed into settlement totals
downstream.

**Why:** 01B insisted on individuation as structurally required
[`01B`, Q1, Q3]; 01A enumerated the same cohorts from a modelling
lens [`01A`, Q1]; 01D concurred [`01D`, Q1, Q5]; 01C endorsed via
coverage-gaps [`01C`, Q5]. Four-of-four convergence.

**Rejected alternatives:**

- **Aggregate population with attributes:** rejected; attributes
  applied to aggregate lose cohort-size individuation.
- **Settlement totals only:** rejected; cohorts cross settlements
  (dialysis, ~5K medical-equipment, over-70s).

## D-004: Time-frame posture for the 10-day horizon

**Triggers met:** [d016_3]

**Triggers rationale:** Reasonable practitioners disagree on whether
the 10-day horizon is a physical fact about stabilisation or a
request-framing artefact; all four perspectives flagged it as the
latter requiring explicit acknowledgement. Four-of-four convergence.

**Decision:** The 10-day horizon is recorded in the assumption ledger
as `type: given-flagged-for-survey`, `source: brief:§Time-constraints`,
`statement: "10-day response-and-stabilisation horizon per local
government request"`, `rationale: "accepted as input; not physically
derived"`, `dependents: "plan time-window; risk-register horizon;
some time-to-harm clocks exceed this window"`, `falsifier:
"central-government revision of horizon; or evidence that 10 days
cannot cover stabilisation meaningfully"`, `review_trigger: "on
Session 002 open"`.

The system model exposes sub-windows the plan will need to address
within the 10-day frame. Specifically, v1 names two:

- **Acute window**, approximately 0–72 hours (some time-to-harm
  clocks are in this range).
- **Stabilisation window**, approximately 72 hours to 10 days.

These are orientation labels, not operational compartments; v1 does
not prescribe activity within them.

**Why:** 4-of-4 convergence that the 10-day frame is a request
artefact [01A, 01B, 01C, 01D]. Convergence that sub-window exposure
is needed for time-to-harm alignment [01B, 01C — 01A and 01D concur
via acute/stabilisation distinction].

**Rejected alternatives:**

- **Accept 10 days silently:** rejected per anti-laundering rule.
- **Override the 10-day frame:** rejected; the frame is brief-given
  even if it is a request-artefact, and overriding it would exceed
  the application's bounds.
- **Single window only:** rejected; collapses time-to-harm
  distinctions Session 002 will need.

## D-005: Time-to-harm clock attribute

**Triggers met:** [d016_3]

**Triggers rationale:** Reasonable practitioners disagree on whether
time-to-harm values belong in the system model (01B position) or in
the risk register (implicit 01A/01C position). 01B's argument that
*"omitting this category produces a model Session 002 will silently
rebuild from scratch, probably worse"* [`01B`, Q1] is load-bearing.
01D partially endorses by including *"time horizons to failure where
known or clearly unknown"* in its model-elements list [`01D`, Q1].

**Decision:** Every `POP-*` entry whose cohort is medical-fragility
carries a `time_to_harm` attribute. The attribute is structured as:

- `window` — a qualitative label (e.g., "hours", "1–3 days",
  "2–5 days", "weeks").
- `driver` — the underlying constraint (e.g., "dialysis interval",
  "insulin thermal tolerance", "generator fuel runtime").
- `source` — `brief` (none in this scenario), `pretrained-clinical-
  knowledge-declined`, `to-be-supplied-by-domain-review`, or
  `unknown`.

At v1, no specific numeric values imported from pretrained clinical
knowledge. All `time_to_harm.window` values at v1 are either
`unknown` or the most conservative qualitative band the brief
permits. Session 002 (or a later session with domain-review input)
may refine.

**Why:** Adopts 01B's load-bearing position [`01B`, Q1] in the
structurally cleanest form; preserves the anti-laundering rule by
declining numeric imports from pretrained clinical knowledge.

**Rejected alternatives:**

- **No time-to-harm category at v1:** rejected; Session 002 would
  rebuild it.
- **Import specific numeric clinical values at v1:** rejected per
  anti-laundering (values would come from pretrained distribution,
  not the brief).

## D-006: Model axis

**Triggers met:** [d016_3]

**Triggers rationale:** Reasonable practitioners disagree on whether
settlement or cohort is the model's primary index. 3-of-4 convergence
[01A, 01B, 01C] that using the settlement partition as the primary
index would launder spatial framing into the cohort structure.

**Decision:** Populations, infrastructure, and services are keyed
independently (`POP-*`, `INF-*`, `SVC-*`). Settlement is recorded as
an **attribute** on entries (e.g., `POP-07`'s `settlement` field =
"Merrow Port"), not as the top-level organising axis. Entries with
cross-settlement scope (e.g., over-70s cohort, ~5K
powered-medical-equipment cohort) carry `settlement:
district-wide` or equivalent.

Ledger records this as `DEC-01`, rejected alternative: *settlement-
indexed primary axis*.

**Why:** 01B's argument that *"dialysis patients span two
settlements; the ~5K on powered medical equipment span all three;
the over-70s span all three"* [`01B`, Q4]. 01A and 01C concur.

**Rejected alternatives:**

- **Settlement-first structure:** rejected (see above).
- **Three parallel per-settlement models:** this is 01C's multi-view
  proposal, rejected at v1 per D-001 preserved as §5.1 minority.

## D-007: Decomposition of ~5K powered-medical aggregate

**Triggers met:** [d016_3]

**Triggers rationale:** Reasonable practitioners disagree on whether
to decompose the aggregate (CPAP, home-oxygen, insulin,
refrigerated-biologics bundle together in the brief). 3-of-4
[01A, 01B, 01D] argue for decomposition because failure profiles
differ; 01C is silent but does not oppose.

**Decision:** The ~5K figure is represented in the model as a
parent cohort (`POP-5K-powered-medical`) with named sub-cohorts:

- `POP-CPAP-home-oxygen` (count: unknown; grid-dependent)
- `POP-insulin-dependent` (count: unknown; cold-chain + resupply
  dependent)
- `POP-refrigerated-biologic` (count: unknown; cold-chain dependent)
- `POP-other-refrigerated-med` (count: unknown)

Counts are `unknown` rather than imputed; the ledger carries an
assumption entry noting that the ~5K aggregate is decomposed
conceptually but the size distribution within the aggregate is not
brief-specified.

**Why:** 3-of-4 convergence [01A, 01B, 01D]. 01A
[`01A`, Q4]: *"CPAP interruption is tolerable for hours; insulin
cold-chain break is tolerable for a day or two; home oxygen
dependency may be acute within hours"*. Failure profiles differ;
risk-register work that collapses the aggregate will mis-prioritise.

**Rejected alternatives:**

- **Keep ~5K aggregate undecomposed:** rejected; loses
  failure-profile distinctions.
- **Impute sub-cohort counts from pretrained epidemiological
  distributions:** rejected per anti-laundering.

## D-008: Validation posture for Session 001 close

**Triggers met:** [d016_3]

**Triggers rationale:** Reasonable practitioners disagree on what
"qualitative multi-agent validation" legitimately warrants. Four-of-
four convergence on the scope of legitimate vs illegitimate claims.

**Decision:** Workspace validation applies this session. Neither
Domain validation nor Reference-provisional substitute applies
(brief precludes domain-actor; no documented proven solution exists
for this fictional scenario, so reference-validation exercise does
not apply). Artefacts carry frontmatter `validation: workspace-only`
per `methodology-kernel.md` v6 §7 and `reference-validation.md` v3
§8 label conventions.

Legitimate close-of-session claims:
- Internal coherence (every structural element traces to brief or
  ledger).
- Brief-coverage for what is included.
- Multi-perspective independence satisfied (4 perspectives, distinct
  contexts, parallel commit).
- Cross-family signal present (1 non-Claude participant).
- Auditability via ledger cross-references.
- Structural sufficiency for Session 002 hand-off.

Not claimed:
- Correctness against reality (territory is fictional).
- Completeness.
- Numerical precision beyond brief-inherited.
- Prioritisation correctness (v1 does not rank).
- Plan sufficiency (deferred).
- Domain-expert endorsement.
- Process-rigor-equals-evidentiary-rigor [01C caveat preserved].
- Cross-model deliberation diversity beyond what 1 non-Claude
  participant narrows (MAD v4 §Limitations applies).

**Why:** 4-of-4 convergence on these bounds
[01A-Q6, 01B-Q6, 01C-Q6, 01D-Q6].

**Rejected alternatives:**

- **Claim reference-validated:** not applicable (no reference case).
- **Claim domain-validated:** explicitly precluded by brief.
- **Claim correctness or completeness:** not supported by the
  validation procedure.

## D-009: Session 001 scope

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** d016_3: the scope question (four artefacts in
one session vs split) has reasonable disagreement. d016_4: operator
marked this load-bearing at session open by directing the split.

**Decision:** Session 001 produces v1 of two artefacts: system model
and assumption ledger. Risk register and response plan are deferred
to Session 002. Session 001 close explicitly flags the two v1
artefacts remaining for Session 002.

**Why:** Operator direction at Session 001 open; 01B explicitly
endorses the scoping move [`01B`, Q3] ("the decisions made by
Session 001 about scope... Session 002 needs to know what it inherits
vs what it must do itself"); kernel §Application Model favours
narrower-deeper increments over broader-shallower ones.

**Rejected alternatives:**

- **Produce all four v1 artefacts in Session 001:** rejected per
  operator direction. [synth] additional rationale: quality risk,
  and the upstream-downstream dependency (D-010) makes sequential
  production principled rather than expedient.

## D-010: Session 002 hand-off artefact-integrity

**Triggers met:** [d016_3]

**Triggers rationale:** Reasonable practitioners disagree on what
counts as sufficient hand-off. 4-of-4 convergence on the four-link
traceability chain and stable-ID requirement.

**Decision:** The v1 artefacts carry:

- **Stable IDs** on every population, infrastructure, service,
  dependency, external interface, and silence entry, plus ledger row
  IDs. IDs are assigned once and not reused.
- **Evidentiary tags** on every non-brief-quoted claim (via the
  ledger's `source` column and the model's `source` tags where
  applicable).
- **Four-link traceability:** every claim in the model traces to
  either a brief clause or a ledger entry; every ledger entry traces
  to the model elements it touches (`model_refs`) and the downstream
  work it supports (`dependents`).
- **Explicit silence entries** and out-of-scope section.
- A session-001-close statement of what was deferred and what was
  explicitly not decided.

**Why:** 4-of-4 convergence [01A-Q3, 01B-Q3, 01C-Q3, 01D-Q3] on
traceability-chain and stable-ID requirements.

**Rejected alternatives:**

- **Narrative-only hand-off:** rejected; loses keyed cross-reference
  [`01B`, Q3: the risk if cohort individuation is lost].
- **No explicit silences or exclusions:** rejected per 01C's
  *"explicit 'what is not in the model' register"* [`01C`, Q1]
  requirement.

## Decisions not taken

Matters surfaced in deliberation but intentionally not decided this
session (recorded so Session 002 knows what it inherits as open):

- **Prioritisation among cohorts.** v1 does not rank dialysis vs
  neonatal vs insulin-dependent vs migrant-worker-language vs over-
  70s-care-circle. Session 002's risk register is the natural place
  to surface this; any ranking in v1 would pre-empt that.
- **Whether outer-islet fishing community is a first-class
  settlement.** Treated as a named cohort in `POP-*` with `settlement:
  outer-islets`; whether it rises to the structural status of Merrow
  Port / South Latch / Kellan Rise is left open.
- **Definition of "stabilised" at T0+10d.** Recorded as surveyable
  in the ledger; not resolved. Session 002 or later must define the
  observable criteria.
- **Treatment of the central-government counterparty.** Recorded as
  surveyable; the model names `EXT-central-gov` as an external
  interface but does not model its internals or assess its
  reliability.
- **OI-015 specific text.** The brief summary of the anti-laundering
  rule was used as-is; the full OI-015 text is in the
  self-development source workspace, not this workspace. Per the
  engine-manifest §6 bootstrap contract, external-application
  workspaces inherit engine-definition files but not
  development-provenance; the summary in PROMPT.md is sufficient.

## Summary of non-Claude participation and OI-004 posture

Non-Claude participation: 1 participant (Outsider, OpenAI via `codex
exec`). Participation was recommended-not-required per MAD v4 §When
Non-Claude Participation Is Required (no d023_* triggers fire on any
decision above). Invoked at operator discretion at session open.
No OI-004 narrowing claim made (`oi004_qualifying_participants: []`
in `participants.yaml`; Session 001 of this workspace is not a
sustained-practice contributor, and this workspace is an external-
problem application distinct from the engine's self-development
workspace where OI-004 is tracked).
