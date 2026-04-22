---
session: 018
title: Anti-Drift Witnesses — Source URLs + Fetch Dates
date: 2026-04-22
status: sealed
component: anti-drift-witnesses
---

# Anti-Drift Witnesses

Per `reference-validation.md` §1 C1, this file records the sources consulted and fetched during Cell 1 reference sourcing. It serves as the anti-drift witness: subsequent sessions reading the reference envelope can verify the reference has not shifted by re-fetching these URLs.

## Fetched sources (Session 018)

### Prime Directive (verbatim text)

| URL | Fetch date | Quote extracted |
|---|---|---|
| https://retrospectivewiki.org/index.php?title=The_Prime_Directive | 2026-04-22 | Prime Directive 40-word text + Kerth 2001 book attribution |
| https://www.teamretro.com/retro-template/norm-kerth-original-four-prime-directive/ | 2026-04-22 | Prime Directive 40-word text + opening usage note |
| https://www.funretrospectives.com/the-retrospective-prime-directive/ | 2026-04-22 | Prime Directive 40-word text + Kerth attribution |

**Cross-source verification status:** All three sources quote the Prime Directive with no word-level variation.

### Safety Poll (procedure description)

| URL | Fetch date | Content extracted |
|---|---|---|
| https://medium.com/@JoshuaKerievsky/norm-kerths-safety-poll-bcccd5be6e44 | 2026-04-22 | Safety Poll procedure (step 2 of 4-step safety check), 1-to-5 scale, anonymous ballot procedure |

**Source qualification:** Derivative secondary source (Kerievsky's blog post). The Safety Poll as rendered in this reference envelope is a paraphrase of Kerievsky's description of Kerth's procedure. Full Kerth verbatim requires the 2001 book.

## Book citation (canonical source, not fetched)

Norman L. Kerth. *Project Retrospectives: A Handbook for Team Reviews*. Dorset House Publishing, 2001. ISBN 0-932633-44-7. 288 pages.

## L2 Case Steward contamination flag

The Case Steward (Claude Opus 4.7, orchestrating agent) has pretraining exposure to the Prime Directive text (widely documented in software-engineering corpora) and to retrospective facilitation literature generally. Per D-072's L2 known-limitation flag, this is recorded for inclusion in the eventual `contamination-audit.md` at Cell 3.

The Case Steward attempted to source the Safety Poll procedure primarily from the Kerievsky URL during Cell 1 rather than from memory. The Safety Poll text in `02-safety-poll.md` is derived from WebFetch output of the Kerievsky URL, with paraphrase performed in the Case Steward's own words based on the fetched content; specific direct quotes are flagged in `02-safety-poll.md` with source-marker quotation marks.
