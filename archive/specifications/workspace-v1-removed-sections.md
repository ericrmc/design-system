---
title: workspace-v1 removed sections (per 078 D-7)
status: superseded
superseded-by: workspace-v2 (engine-v17, session 079)
superseded-on: 2026-04-27
provenance: provenance/079-substrate-vertical-slice/
---

# Sections removed from workspace.md by 079 application of 078 D-7

## §"Top-level layout" — directory tree (replaced per D-7 step 5)

The directory tree was a transition aid for engine-v16 enumerating the loaded-by-default surface. v2 replaces it with the normative rule: *"The manifest defines engine-definition files; session records live under `provenance/`; generated exports are not the source of truth once the substrate exists."*

Original tree from v1:

```
PROMPT.md                       # entry point (engine-definition)
MODE.md                         # workspace-identity
CLAUDE.md                       # harness instructions (per-workspace, optional)
prompts/                        # engine-definition
  development.md
  application.md
specifications/                 # engine-definition
  methodology.md
  constraints.md
  workspace.md
  engine-manifest.md
tools/                          # engine-definition
  validate.sh
applications/                   # application
  NNN-<slug>/
    brief.md
    <produced artefacts>
provenance/                     # provenance
  NNN-<slug>/
    00-assessment.md
    01-deliberation.md          # when applicable
    02-decisions.md
    03-close.md
    04-review.md                # when applicable
engine-feedback/                # operator-mediated, optional
  EF-<session>-<slug>.md
open-issues/                    # workspace-scope, optional
  OI-<id>-<slug>.md
  index.md
archive/                        # superseded files; not loaded by the engine
```

And the trailing transitional sentence:

> This layout will likely change in the successor design (sessions 077–078) when the database substrate replaces some of the directory-based bookkeeping. Until then, the layout above is what an active workspace looks like.

**Why removed.** Per 078 D-7 step 5, the tree as-loaded was a transition-aid; the substrate is the source of truth from engine-v17 forward. The new normative rule names the manifest as the authority and `provenance/` as the persistent record location, leaving the rest as derived.

---

## §"What this file does not say" (removed in full per D-7 step 4)

This workspace specification intentionally does not specify:

- A read budget or default-read enumeration. The seventy-five-session engine accumulated a closed-enumeration default-read whose growth consumed half the agent's context window at session-open; the successor design will not repeat that arrangement. Until the successor lands, sessions read what they need and record what they read in the assessment.
- A retrieval substrate, alias resolution, or cross-reference index. The next two sessions will design the database substrate that replaces these.
- Cross-session counters, decision-IDs across sessions, or other structured state currently maintained in narrative form. These will move to the database substrate when the successor design provides one.

These omissions are deliberate. The minimum here is what allows session 077 to run.

**Why removed.** Same reason as `methodology.md` §"What this kernel does not say": 078 closed the items the section deferred (D-1 substrate-shape, D-9 substrate technology, the deterministic counters in `selvedge id-allocate`). The "did-not-say" list is no longer load-bearing.
