---
session: 001
title: Perspective — Systems Modeller
date: 2026-04-24
status: complete
perspective: systems-modeller
committed_at: 2026-04-24
---

# Perspective — Systems Modeller

## Q1. System model — minimum structural sufficiency

For v1 to be usable as input to a risk register and response plan, the model must answer three operational questions for any downstream author: *what exists*, *what depends on what*, and *what state is it in at T0*. Nothing more is strictly required at v1; everything else is an elaboration that belongs to v2 or to Session 002's own artefacts.

I propose the v1 model be a structured Markdown document with the following sections, each backed by a keyed table so entries are addressable (e.g. `POP-01`, `INF-03`, `DEP-07`). Keys are the load-bearing primitive: every assumption-ledger entry, every risk, every response action in later sessions points back to a key. No key, no traceability.

**Minimum categories of element:**

1. **Populations (POP-*).** Not just counts — populations as *sites of demand* with attributes that matter for this scenario. Columns: key, label, settlement, count (or range), special-need flags (age 70+, powered-medical, dialysis, neonatal, linguistic minority, housing-informal). The brief gives enough to seed ~8–12 entries: 70+ cohort (~18K), powered-medical (~5K), dialysis-centre patients (~1,200), regional-hospital dialysis (~220), neonatal cohort at Merrow Port regional, migrant-worker dormitory residents (~9K, two non-majority languages), outer-islet fishing community, displaced population (~18K at T0), and the three settlement-total populations. The model must not collapse these — they are the hooks the response plan hangs on.

2. **Infrastructure (INF-*).** Physical and logical assets with state. Columns: key, label, settlement/location, type (power, water, transport, comms, health, shelter), T0 status (operational / degraded / offline / inaccessible / unknown), and a free-text state note. Entries the brief makes explicit: Merrow Port regional hospital (450 beds, on generator), Kellan Rise secondary hospital (280 beds, unaffected), South Latch primary-care clinic, South Latch dialysis centre (inaccessible), Merrow Port drinking-water treatment plant (salt-intruded), backup wells (rotation, ~35K served), four coastal substations (two degraded), grid coverage of Merrow Port and South Latch (out), South Latch levee system, freight rail bridge (damaged-but-passable), highway bridge into Merrow Port (24-t rated, intact), sea access (degraded, salvage required), air access (runway debris), fibre-optic trunk on the rail bridge, VHF networks on outer islets, cellular coverage (absent on outer islets pre-disaster).

3. **Services (SVC-*).** The functions populations consume, which ride on infrastructure. Separating services from infrastructure matters because a service can fail while its infrastructure stands (e.g. a hospital with no potable water), and the response plan acts on services. Columns: key, label, delivering infrastructure keys, consuming population keys, T0 continuity status. Minimum set: acute care (two hospitals), dialysis, neonatal care, primary care, potable-water supply, electrical supply, shelter, inter-settlement transport, telecomms, cold-chain for refrigerated meds.

4. **Dependencies / relationships (DEP-*).** The edges. This is where the model earns its keep; without explicit edges, Session 002 re-derives them from prose. Columns: key, from-node, to-node, relationship type, notes. Relationship types I would support at v1: *powers* (substation → hospital), *supplies* (treatment plant → settlement), *carries* (rail bridge → fibre trunk), *routes-to* (highway bridge → Merrow Port), *serves* (dialysis centre → patient cohort), *refers-to* (regional hospital ↔ secondary hospital), *backed-by* (grid → generator), *co-located-with* (dormitory housing → Merrow Port waterfront), *communicates-via* (outer islets → VHF). Roughly 20–30 edges at v1 is sufficient; the goal is not an exhaustive graph but a graph where every T0 degradation the brief names can be traced to affected populations.

5. **External interfaces (EXT-*).** Short section. Central government (recipient of the 10-day plan), local utility (power-restoration authority, 3–7-day estimate), highland interior (reached via Kellan Rise road + rail bridge). These are boundary nodes whose internal states the model does not track but whose interfaces matter.

**Categories of relationship that matter for this scenario specifically:** physical carriage (the rail bridge carrying fibre is the canonical example — one asset, two services, two failure modes), levee dependency (South Latch is *conditionally* habitable), generator-fuel dependency (Merrow Port regional hospital on generator implies a fuel clock), referral dependency between the two hospitals, and linguistic-channel dependency (information services to the migrant-worker cohort require non-majority-language channels).

**What I would leave out of v1, and why:**

- Economic flows, supply chains upstream of the district, and commodity pricing. Not because they don't matter, but because the brief does not give T0 data to populate them honestly; inventing values would create false precision.
- Political / governance structure beyond the central-government interface. Session 002 may need this; v1 should not pre-empt it.
- Quantitative capacity modelling (beds-per-hour, litres-per-day). V1 should name the *capacity dimension* and leave numbers to v2 where the Advocate and Skeptic can pressure-test them.
- Time-evolution beyond T0. V1 is a snapshot. Trajectories belong in the risk register.
- Scenario branches ("if levee fails", "if bridge fails"). That is risk-register work.

Restraint is the point: a model that asserts only what the brief supports, with every assertion keyed, is more useful to Session 002 than a richer model whose extra content is uncited.

## Q2. Assumption ledger — shape and scope

**Distinctions:**

- A **given** (brief-stated fact) is something the brief asserts and the engine has surveyed-and-accepted as input — e.g. *"Storm surge peaked ~2.8m above MHT"*. Givens belong in the system model as state, not in the ledger.
- A **constraint** is a bound the work must respect that is not itself chosen by the session — e.g. the 10-day plan horizon, the 24-tonne bridge rating, the 3–7-day power-restoration estimate. Constraints may also be recorded in the model (as attributes on the relevant node) but the ledger lists them where they shape method.
- An **assumption** is a proposition the session must adopt to proceed, which the brief does not assert and which could later prove false. Assumptions are the ledger's core.
- A **decision** is a session-made choice among surveyable alternatives. Decisions belong in a separate decisions log (which the Decide activity produces) but the ledger may cross-reference them where an assumption was adopted *because* of a decision.

**Shape.** A table, not a list. Markdown table with explicit columns, each row keyed. This gives human readers (local government) a scannable document and machine consumers a parseable structure. Recommended columns:

| Column | Purpose |
|---|---|
| `id` | stable key, e.g. `ASM-03` |
| `statement` | the assumption in one sentence |
| `type` | assumption / constraint / given-flagged-for-survey |
| `model_refs` | keys in the system model it touches (e.g. `INF-07, DEP-12`) |
| `source` | brief-quote / role-inferred / external-surveyed |
| `rationale` | why it is being adopted |
| `falsifier` | what observation would invalidate it |
| `affected_if_false` | which model nodes/edges shift, or which downstream artefact is blocked |
| `review_trigger` | event or time that should re-open it (e.g. "T0+72h", "on receipt of utility update") |
| `status` | live / retired / promoted-to-given |

The `model_refs` and `affected_if_false` columns are the load-bearing ones for auditability. Every assumption must locate itself in the model; if it cannot, either the model is missing a node or the assumption is unfalsifiable and should be rewritten.

**Three assumptions the brief is asking Session 001 to make** (non-exhaustive; naming as required):

1. **ASM-example-A: "The 18K displaced figure is stable enough at T0 to plan against."** The brief gives a single number at T0+36h. Treating it as a planning baseline is an assumption; displacement is dynamic as water recedes unevenly. `model_refs`: POP (displaced cohort). `falsifier`: a T0+72h count outside a tolerance band.
2. **ASM-example-B: "The highway bridge's 24-tonne rating survives aftershock / continued saturation for the 10-day window."** The brief states the rating intact *at T0*. Using it as a logistics artery for ten days assumes persistence. `model_refs`: INF (highway bridge), DEP (routes-to Merrow Port).
3. **ASM-example-C: "Backup wells can continue to serve ~35K on rotation for the plan horizon."** The brief says they *do* serve, not that they *will continue to*. `model_refs`: INF (backup wells), SVC (potable water), POP (Merrow Port residents, dormitory residents).
4. (Bonus) **ASM-example-D: "The fibre trunk's service state follows the rail bridge's structural state."** Brief says the bridge *carries* the fibre; it does not state the fibre's operational state at T0. Treating the two as coupled is a modelling assumption worth flagging.

## Q3. Upstream-downstream dependency

Session 002's risk register needs to name failure modes and assign likelihood/impact; its response plan needs to allocate actions to actors across a 10-day window. For these not to be blocked, the two upstream artefacts must deliver:

**From the system model:**

- A complete enumeration of T0 states for every named infrastructure and service element. A risk author cannot write *"risk: dialysis centre remains inaccessible"* if the model doesn't make "inaccessible" a first-class state on that node.
- Explicit edges. A risk register that has to re-derive "the fibre trunk runs on the rail bridge" from prose will either miss the coupling or re-derive it inconsistently across entries. The DEP-* table resolves this once.
- Population hooks with special-need flags. The response plan allocates per-cohort actions; it needs cohorts as keyed entries, not as adjectives in a narrative.
- A list of *capacity dimensions* per service (beds, litres/day, kW, shelter-places) even if values are deferred. This tells the risk author where to look for saturation risk without the model overclaiming numbers.

**From the assumption ledger:**

- For every state or value the model asserts that is not directly brief-quoted, a ledger entry locating the assumption. Session 002 can then decide per-entry whether to accept, probe, or condition a risk on it.
- Falsifiers and review triggers. The response plan inherits a checklist of "things to re-validate at T0+X".

**Audit affordance.** The combined artefact set should let a Session 002 author trace any plan action back through: action → risk → affected service → supporting infrastructure → underlying assumptions. If any link in that chain is tacit, Session 002 either re-invents it or proceeds fragile. V1's job is to make all four links explicit and keyed.

**What v1 does *not* need to deliver:** quantified risk scores, response options, prioritisation. Those are Session 002's domain. V1 delivering them would pre-empt the Deliberate of Session 002 and launder Session 001 decisions as structure.

## Q4. What is a choice vs what is a given

The anti-laundering rule matters here. The brief's territory description — settlements, populations, infrastructure inventory — is brief-given. The engine surveyed-and-accepted these when it accepted the application. They go into the model as state; they are *not* re-surveyable as choices within this session. Treating them as choices would re-open territory the application has already bounded.

However, the brief contains items that sit on the border — facts stated without the granularity the modelling work needs, or facts whose *framing* is itself a choice. These I flag for explicit surveying rather than silent absorption:

1. **The 10-day response-and-stabilisation horizon.** The brief says *"Local government has requested from central government a 10-day response-and-stabilisation plan"*. The horizon is given — but what counts as "stabilisation" (restoration of baseline services? a defined reduced-service floor? zero additional excess mortality?) is a framing choice the session is being asked to make tacitly. Flag for survey: *what does "stabilised" mean at T0+10d, against which the plan is judged?*

2. **The partition of the population into three settlements plus "outer islets".** The brief lists Merrow Port, South Latch, Kellan Rise explicitly and adds the *"dispersed fishing community on outer estuary islets"* almost as an aside. Treating the islet community as a fourth population-site with full model representation, vs. as a footnote to Merrow Port, is a choice. Flag for survey: *is the outer-islet community a first-class settlement in the model?* I would argue yes, but that is exactly the kind of decision that should be surfaced, not silently made.

3. **The "~5K on powered medical equipment" aggregate.** The brief bundles CPAP, home oxygen, and refrigerated meds (insulin, biologics) into one figure. These have very different failure profiles (CPAP interruption is tolerable for hours; insulin cold-chain break is tolerable for a day or two; home oxygen dependency may be acute within hours). Flag for survey: *does v1 decompose this cohort or keep it aggregated?* I lean toward decomposition; again, worth surfacing.

4. **(Additional) The treatment of migrant-worker dormitory residents as a distinct population.** The brief separates them from Merrow Port's 62K; a modelling choice about whether they are modelled as overlapping with or additional to that 62K affects every downstream count. Flag for survey.

Per OI-015, none of these should be re-examined as if they were up for debate from first principles — the settlements, the counts, the infrastructure inventory are input. But the *framings* above are genuinely session-level choices the brief does not resolve.

## Q5. Coverage gaps

Concrete items my lens surfaces as at risk of being left out:

- **The fibre trunk as a service vector, not just an asset.** The brief mentions the fibre almost incidentally (*"this bridge also carries a major fibre-optic trunk serving Kellan Rise"*). If the model represents only the asset and not the services it carries (civil comms, possibly hospital telemetry, possibly financial/payment systems, possibly central-government liaison), the downstream risk register will likely miss cascading information-system failures. The fibre needs an INF entry *and* SVC entries for what rides on it.
- **Generator-fuel supply chain for Merrow Port regional hospital.** "On generator" is a T0 state; it implies a fuel consumption rate and a resupply dependency. Without an explicit fuel-supply edge (who delivers, via which route, at what cadence), the model cannot support a risk of "generator fuel exhaustion at T0+Xd".
- **Cold-chain as a service distinct from electricity.** The ~5K on refrigerated meds depend not on grid power directly but on *functional refrigeration at point of use*, which may be met by generator, ice, or relocation. Modelling this as its own service with multiple possible supplying infrastructures prevents the risk register from collapsing it into "power outage".
- **Inter-hospital referral capacity.** With the regional hospital on generator and the dialysis centre inaccessible, load is implicitly transferring to Kellan Rise's 280-bed secondary. The referral edge exists in reality; it should exist in the model.
- **VHF as Merrow-Port-to-islets link.** The brief says the islets have informal VHF among themselves. Whether any Merrow Port node can reach them via VHF at T0 is unstated; the model should at least carry an edge-with-unknown-state rather than omit the relationship.
- **Language-channel coverage of information services.** If the model has a "public information" service, it needs to carry the attribute that the migrant-worker cohort requires two non-majority-language channels. Otherwise the response plan inherits a service definition that tacitly assumes monolingual delivery.
- **Aged-care clusters in South Latch as distinct nodes.** The brief names "two aged-care clusters" — these are sites, not just population attributes, and should probably be INF entries with their own power/water dependencies.
- **The neonatal unit as a sub-service of the regional hospital.** Losing the regional hospital and losing its neonatal unit have different response implications; the unit deserves its own SVC key.
- **Salvage as a pre-service for sea access.** Sea access is *"degraded (salvage required)"* — the salvage operation itself is a service the response plan may need to resource, and should appear as a prospective SVC entry even if not T0-active.

I will not pre-empt the Advocate and Skeptic; the above is what the modelling lens alone flags as structurally missing, not a claim to have enumerated all vulnerabilities.

## Q6. Validation claims Session 001 can make

Validation at close is qualitative and multi-agent. For the two upstream artefacts specifically, legitimate claims are:

- **Internal consistency.** Every DEP-* edge references two existing nodes. Every SVC-* entry references at least one INF-* entry and at least one POP-* entry. Every ledger entry references at least one model key. No dangling references.
- **Brief-coverage.** Every population, infrastructure element, and T0 state the brief states explicitly appears in the model (or is explicitly flagged as out-of-scope with rationale).
- **Auditability.** For every non-brief-quoted assertion in the model, a ledger entry exists that locates the assumption, names a falsifier, and identifies affected model elements.
- **Perspective independence satisfied.** Four perspectives reasoned without seeing each other's outputs; the synthesiser's merged record reflects this.
- **Structural sufficiency for hand-off.** The artefacts present the scaffolding (keyed elements, typed edges, state column, capacity-dimension column) that Session 002 needs to attach risks and actions to, without re-deriving structure.

**What Session 001 should *not* claim:**

- **Correctness against reality.** The territory is invented; there is no ground truth to validate against. The model being "right about Laurel Delta" is not a meaningful claim.
- **Completeness.** No claim that all populations, assets, dependencies, or failure modes are captured — only that the brief-stated ones are, and that the structure supports adding more.
- **Numerical precision.** Where the brief gives ranges or approximate figures (~18K, ~5K, 3–7 days), the model inherits the imprecision; it cannot validate tighter values.
- **Prioritisation correctness.** V1 does not rank populations, infrastructure, or risks; it cannot claim its (absent) rankings are right.
- **Plan sufficiency.** Nothing about whether the eventual plan will work.
- **Domain-expert endorsement.** The brief explicitly declines domain-actor validation; Session 001 should not imply it has such endorsement.
- **Transferability.** No claim that the model shape generalises to other scenarios. That may be true; it is not something v1 can validate.

Close-of-session validation is best stated as: *"these artefacts are internally consistent, brief-covering, auditable, and structurally sufficient for Session 002 to build on — and they make no claims beyond that."*

## External inputs surveyed

The following came to mind from pretrained material while reasoning; I surface them rather than apply them, per the brief's §6 constraint:

- **Cluster-system / sector-based coordination frameworks** (the global humanitarian-cluster model, with health, WASH, shelter, logistics, etc. as named coordination groupings). This would have me organise SVC-* by cluster categories. I did not apply it; I let service categories emerge from the brief's own infrastructure and population list.
- **ICS/IMS incident-command structures** (typed organisational roles — operations, planning, logistics, finance/admin). This would have me add a governance/command layer to the model. I did not apply it; the brief's only named external actor is central government, and the system model is scoped to the territory, not to the response organisation.
- **Lifelines frameworks** (transportation, communications, energy, water, health-and-medical, food/shelter/hazardous-materials, safety/security). This would have me pre-structure INF-* by lifeline. I did not apply it; I grouped by type emergent from the brief, which happens to partially overlap but is not identical.
- **MoSCoW / RAID-log conventions** for structuring assumptions-risks-issues-dependencies. My ledger shape is RAID-adjacent but I did not import the acronym or its conventions wholesale; I built the columns from what Q2 asks for.
- **Maximum-tolerable-downtime / RTO/RPO concepts from continuity planning**. These would have me attach time-to-harm values to every service. I did not apply it at v1 because the brief does not supply those values and inventing them creates false precision; I noted a *capacity-dimension* column as the placeholder instead.

The synthesiser and Decide step may choose to adopt any of these. I have not.

## Honest limits / Refusals

- I have reasoned about structure, not content. Where the brief gives counts, states, and relationships, I have named them in categories; I have not attempted to populate a full model in this perspective (that is Produce work, not Deliberate work). If the brief expected a pre-populated model here, I have declined that read.
- I have not attempted to pre-empt the Vulnerability Advocate or Adversarial Skeptic as my role-instructions explicitly told me not to. Coverage gaps in Q5 are modelling-lens gaps only.
- I am treating "Markdown with keyed tables" as the right representation for v1. Diagrams (e.g. a node-edge diagram of the dependency graph) would help human readers; per the engine's preference for text representations alongside diagrams, I would add a rendered diagram as a derivative of the DEP-* table rather than as a source artefact. Flagging this in case the synthesiser or another perspective expects a diagrams-first artefact — I do not.
- I note mild discomfort with the brief's framing of assumptions as something the session is "asked to make" (Q2). In strict method, assumptions should emerge from the gap between what the brief asserts and what the work requires, not from a quota. I have listed some, per instruction, but flag that a ledger with *only* those entries would be under-populated; v1's actual ledger should grow naturally as modelling proceeds.
- I have not imported any real-world Laurel-Delta-like case. The setting is stated as invented and I have reasoned from the brief only.
