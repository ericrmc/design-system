---
feedback_id: EF-003-archive-citation-convention-for-closed-session-files
source_workspace_id: selvedge-disaster-response
source_session: 003
created_at: 2026-04-24
reported_by: application-agent
target: engine
target_files:
  - specifications/read-contract.md
  - tools/validate.sh
severity: observation
status: outbound
---

# EF-003 — Archive citation convention for closed-session files

## Observation

`specifications/read-contract.md` v4 §6 Reference conventions
prescribes the stable citation form:

```
[archive: provenance/NNN-title/archive/<slug>/]
```

With optional chunk-level precision:

```
[archive: provenance/NNN-title/archive/<slug>/#chunk-02]
```

This form is archive-pack-directory-scoped. The check 22 parser in
`tools/validate.sh` pattern-matches `[archive:
provenance/<NNN-title>/archive/<slug>/]` references and verifies
they resolve to an existing archive-pack directory.

§3 of the same specification enumerates archive-surface by
exclusion:

> - Raw perspective files (`provenance/NNN-title/01X-perspective-
>   <role>.md`) from closed sessions.
> - Superseded specification versions (`specifications/*-v1.md`,
>   `*-v2.md`, etc., carrying `status: superseded`).
> - Deliberation synthesis files (`provenance/NNN-title/01-
>   deliberation.md`) from closed sessions.
> - Decision files (`provenance/NNN-title/02-decisions.md`) from
>   closed sessions.
> - Assessment files (`provenance/NNN-title/00-assessment.md`)
>   from closed sessions.
> - ...

So archive-surface contains two structurally-distinct classes:

1. **Archive-pack directories** (§4 layout: `provenance/NNN-title/
   archive/<slug>/` with `manifest.yaml` + chunks). §6 citation
   convention is explicitly scoped to this class.
2. **Closed-session files** (§3 enumeration above: raw
   perspectives / `01-deliberation.md` / `02-decisions.md` /
   `00-assessment.md` / manifests / participants.yaml from closed
   sessions). §6 citation convention is silent on this class.

In this external-problem workspace (Application 001 disaster-
response), no archive-pack has ever been created. All archive-
surface material is in class 2 (closed-session files). Every
load-bearing archive-surface citation this workspace has made
takes the form:

```
[archive: provenance/NNN-session/02-decisions.md]
[archive: provenance/NNN-session/01-deliberation.md §5.1]
[archive: provenance/NNN-session/01X-perspective-<role>.md]
```

— a form §6 does not prescribe but readers understand as "the
closed-session file at that path, accessed by reference not by
default-read". Sessions 001, 002, and 003 close narratives all
note that check 22 is out-of-scope for this form:

> "the validator's check 22 pattern-matches `archive/<slug>/`
> directory references, not closed-session file references, so
> these citations are out-of-scope for the automated check but
> honoured in spirit per `read-contract.md` §6."

(Session 003 close §3; Session 002 close §3; Session 001 close
§3 — same observation three times.)

## Why it matters

Three concerns:

1. **Spec silence on the dominant archive-surface citation form
   in external-problem workspaces.** Per `read-contract.md` §2c
   close-rotation adoption at engine-v5, closed-session files
   outside the 6-session retention window become archive-surface
   by exclusion. In self-development workspaces with 30+ sessions,
   this pattern activates routinely; in external-problem
   workspaces, closed-session files are the *only* archive-
   surface class until a single over-budget file forces archive-
   pack creation. The spec's §6 convention is archive-pack-first,
   leaving the dominant citation form in external-problem
   workspaces underspecified.

2. **Check 22 coverage gap.** Check 22 verifies archive-pack
   citation consistency. Closed-session file citations of the
   form `[archive: provenance/NNN-title/<filename>.md]` are
   silently out-of-scope — they neither pass nor fail. A citation
   that names a non-existent closed-session file (a typo, a drift
   across v-suffix migrations, a reference to a session that was
   never created) would not be caught. In this workspace, three
   sessions have made ~15 such citations in total; a manual
   audit confirms they all resolve, but no automated check
   verifies this.

3. **Cross-reference form variation across workspaces.** The
   self-development source workspace has archive-packs (Session
   014 Outsider per Session 022 R8c; Session 022 Outsider per
   R8c'); its citations mix the two forms (archive-pack
   directories and closed-session files). External-problem
   workspaces until first-archive-pack-creation use only closed-
   session-file citations. The spec's §6 narrowly addresses the
   first form; readers of §6 alone could miss that the second
   form is also expected discipline.

## Suggested change

Three candidate directions:

**Direction 1 (narrow; spec clarification only).** Add a sub-
section to `read-contract.md` §6 explicitly naming the closed-
session-file citation form:

> **Closed-session files (added).** Archive-surface closed-session
> files (per §3) are cited using the form:
>
> ```
> [archive: provenance/NNN-title/<filename>.md]
> ```
>
> with optional section precision:
>
> ```
> [archive: provenance/NNN-title/<filename>.md §X]
> ```
>
> This form parallels the archive-pack form above; both resolve
> via the same `[archive: path]` convention. Readers reading a
> closed-session-file citation consult the cited file directly
> (there is no manifest intermediary).

**Direction 2 (medium; check 22 coverage).** Extend check 22 to
pattern-match `[archive: provenance/<NNN-title>/<filename>.md]`
references in addition to `archive/<slug>/` references, and verify
that the cited file exists and that the `NNN-title` directory
corresponds to a closed session (presence of `03-close.md` or
numeric prefix ≥ 1 below the current session). Session-number-gate
this extension to sessions ≥ the adoption session.

**Direction 3 (broadest; citation taxonomy).** Refactor §6 to
explicitly name the three archive-surface classes and their
citation forms: (a) archive-pack directory (existing §6 language);
(b) closed-session file (new); (c) superseded spec version (e.g.,
`[archive: specifications/read-contract-v3.md]`, also not
currently named in §6). Each with its resolution-path and validator
implications.

Direction 1 is cheap; Direction 2 closes the validator coverage
gap; Direction 3 is structural.

## Evidence

Three sessions of this workspace (Application 001 disaster-
response):

- **Session 001** (`provenance/001-session/03-close.md` §3):
  documents the pattern as out-of-scope; no remediation proposed.
- **Session 002** (`provenance/002-session/03-close.md` §3):
  same observation, citing the Session 001 close-comment verbatim.
  Three archive-pack citations this session to Session 001 files.
- **Session 003** (`provenance/003-session/03-close.md` §3):
  same observation, third consecutive session. ~8 closed-session-
  file citations this session (to Session 001 D-001 through D-010,
  Session 002 D-011 through D-020, Session 001 + 002 deliberation
  §5.1 through §5.4 minority texts).

Across the three sessions, all citations resolve. No citation has
been broken; no typo or drift has surfaced. The check 22 coverage
gap is therefore theoretical in this workspace to date — but the
absence of evidence is not evidence of absence, since no check is
looking.

## Application-scope disposition

The application handled this locally via the honest-limits note
in each close narrative ("out-of-scope for the automated check but
honoured in spirit per `read-contract.md` §6"). Recorded here as
engine-feedback because the observation has recurred in every
consecutive session of this workspace and because the dominant
archive-surface-citation form in an external-problem workspace's
first several sessions is the closed-session-file form.

This feedback is written in outbox role per `specifications/
workspace-structure.md` v5 §engine-feedback and is pending
operator-mediated transport to the self-development source
workspace's `engine-feedback/inbox/` for triage.
