# Open issues — substrate-canonical (engine-v22)

Issues are now stored in the `issues` substrate table per S088 D-1 (DV-S088-1). The 25 markdown files that lived here through engine-v21 were backfilled into substrate rows by the S088 backfill subagent and then deleted; their full prose remains in git history.

This file is preserved as a pointer, not a tracker. **Do not edit issues here.** Use the CLI:

```sh
# What should I work on next?
bin/selvedge query "SELECT i.citable_alias, i.priority, ta.text AS title FROM issues i JOIN text_atoms ta ON ta.atom_id=i.title_atom_id WHERE i.status='open' AND NOT EXISTS (SELECT 1 FROM issue_links l JOIN issues b ON b.issue_id=l.source_issue_id WHERE l.relation='blocks' AND l.target_issue_id=i.issue_id AND b.status IN ('open','blocked','in_progress')) ORDER BY CASE i.priority WHEN 'HIGH' THEN 0 WHEN 'MEDIUM' THEN 1 ELSE 2 END, i.surfaced_session_id ASC"

# Inspect a single issue:
bin/selvedge query "SELECT i.*, ta.text AS title, ts.text AS summary, tb.text AS body FROM issues i JOIN text_atoms ta ON ta.atom_id=i.title_atom_id LEFT JOIN text_atoms ts ON ts.atom_id=i.summary_atom_id LEFT JOIN text_atoms tb ON tb.atom_id=i.body_atom_id WHERE i.citable_alias='OI-XXX'"

# Disposition history of a resolved issue:
bin/selvedge query "SELECT d.seq, d.from_status, d.to_status, ta.text AS reason FROM issue_dispositions d JOIN text_atoms ta ON ta.atom_id=d.reason_atom_id WHERE d.issue_id=(SELECT issue_id FROM issues WHERE citable_alias='OI-XXX') ORDER BY d.seq"
```

CLI submit kinds: `submit issue`, `submit issue-disposition`, `submit issue-link`, `submit issue-note`. Schema in `state/migrations/009-issues-table.sql`.

Pre-S088 markdown OIs are in git history. To recover the prose for a specific issue:

```sh
git show HEAD~1:open-issues/OI-002.md
```

The substrate body atoms compress most issues to under 4000 chars. For five large issues (OI-002, OI-004, OI-016, OI-019, OI-080-001 — variously 12K to 41K chars in their pre-substrate form) the substrate body is a compressed canonical summary, with the verbatim prose preserved only in git history. If you need verbatim text, use git.
