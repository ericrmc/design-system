---
triage_id: EF-047-brief-slot-template-triage
feedback_ref: ../inbox/EF-047-brief-slot-template-hidden-arc-leakage.md
triaged_in_session: 048
triaged_at: 2026-04-24
status: triaged
disposition: adoption bundled with S049 MAD as minor alongside EF-047-retrieval-discipline substantive scope; both suggested options (a) bootstrap --hidden-arc flag + prompts/application.md paragraph, and (b) workspace-structure.md §applications documentary clarification, remain candidates at S049
opened_issue: null
scheduled_mad_session: 049
engine_version_impact_pending: minor (bundled with S049 MAD engine-v bump if retrieval-discipline adoption also bumps)
---

# Triage — EF-047 brief-slot-template-hidden-arc-leakage

## Classification

**Target**: engine. **Severity on inbox record**: friction. **Source**: `selvedge-self-development` Session 047, direct-to-inbox out-of-session operator observation.

**Disposition**: **triaged; adoption bundled with S049 MAD** per operator ratification at S048 Halt 1 Q4 = (b). Both suggested options ((a) `--hidden-arc` flag in `tools/bootstrap-external-workspace.sh` + `prompts/application.md` paragraph; (b) `specifications/workspace-structure.md` v5 §applications documentary clarification) remain candidates at S049; selection between (a) / (b) / bundled-(a)+(b) is an S049 deliberation question.

## Why not adopted this session

Option selection ((a) engine-level mechanism vs. (b) documentary convention vs. both) is under-determined from the inbox record alone. Operator explicitly ratified bundled-with-S049-MAD rather than unilateral adoption at S048. The friction itself is pre-execution-caught and operationally mitigated for the in-flight `selvedge-disaster-response` arc via operator's lean-populate-plus-leave-optionals-empty workaround (per EF-047-brief-slot-template §Application-Scope Disposition).

## Scheduled S049 MAD scope (bundled)

At S049, the brief-slot-template feedback composes with the retrieval-discipline scope at the external-application-workspace boundary. Specific S049 sub-questions for this record:

- Is option (a) (engine-level bootstrap flag + `prompts/application.md` paragraph) the right mechanism, given that hidden-arc applications are a sub-class of external applications that the engine should recognise explicitly?
- Is option (b) (documentary convention in `specifications/workspace-structure.md` v5 §applications) sufficient, on the grounds that operator-discipline is the actual enforcement layer regardless of engine-level mechanism?
- Should the candidate `--hidden-arc` flag's behaviour be mandatory-when-operator-declares-hidden-arc or opt-in?

## What the bundled-minor adoption at S049 looks like

If S049 adopts option (a): minor addition to `tools/bootstrap-external-workspace.sh` (flag parsing + conditional brief.md template; no engine-v bump by itself); minor documentary addition to `prompts/application.md` §This application's context explaining the hidden-arc case. Bundled with retrieval-discipline substantive (which bumps engine), so the minor rides in the v8→v9 bump.

If S049 adopts option (b) only: minor addition to `specifications/workspace-structure.md` v5 §applications; no engine-v bump on its own; may ride in the v8→v9 retrieval-discipline bump or close as v5 minor amendment analogous to S045 D-138.

If S049 adopts both (a) and (b): bundled-minor; same v-bump treatment as option (a).

## Forward observations

- The §11 transport-instructions leakage language in `provenance/047-session/arc-plan.md` ("statement that subsequent session inputs will arrive at each T0") is a sealed historical witness per D-017. Forward arcs use the operator's refined lean-populate-plus-leave-optionals-empty workaround; S049 adoption codifies the convention for future applications.

## OI impact

No OI opened. No OI resolved.
