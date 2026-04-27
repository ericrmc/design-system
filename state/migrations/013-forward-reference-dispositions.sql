-- Migration 013: forward_reference_dispositions table + T-26.
-- engine-v26 → engine-v27 (session 097, EF-S096-1 strong remedy).
--
-- Closes the gap surfaced by EF-S096-1: close_state_items rows with
-- facet='next_session_should' have no substrate link to the session that
-- addresses them. Without closure, `bin/selvedge orient` re-surfaces the
-- forward-reference indefinitely.
--
-- Design: separate disposition table (mirrors issue_dispositions / finding
-- disposition pattern) keyed on state_item_id with a UNIQUE constraint so
-- a forward-reference cannot be disposed twice. Resolution is a typed row
-- carrying the resolving session and an optional note atom.
--
-- T-26 refuses disposing close_state_items with a facet other than
-- next_session_should — only forward-references are dispositionable; other
-- facets (what_was_done / state_at_close / etc.) are descriptive close
-- state, not a queue.
--
-- T-15 compliance: ADD-only DDL (one new table, one new trigger). No
-- CHECK relaxation, no table recreation.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TABLE forward_reference_dispositions (
    disposition_id        INTEGER PRIMARY KEY,
    state_item_id         INTEGER NOT NULL REFERENCES close_state_items(state_item_id),
    resolved_session_id   INTEGER NOT NULL REFERENCES sessions(session_id),
    resolved_at           TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    note_atom_id          INTEGER REFERENCES text_atoms(atom_id),
    UNIQUE (state_item_id)
) STRICT;

CREATE INDEX idx_fwd_ref_disp_state_item ON forward_reference_dispositions(state_item_id);
CREATE INDEX idx_fwd_ref_disp_resolved_session ON forward_reference_dispositions(resolved_session_id);

CREATE TRIGGER t26_fwd_ref_disposition_facet_gate
BEFORE INSERT ON forward_reference_dispositions
FOR EACH ROW
WHEN NOT EXISTS (
    SELECT 1 FROM close_state_items
    WHERE state_item_id = NEW.state_item_id
      AND facet = 'next_session_should'
)
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T26: forward_reference_dispositions only admit close_state_items with facet=next_session_should');
END;

INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__','forward_reference_dispositions','insert');

INSERT INTO schema_migrations (name, sha256) VALUES ('013-forward-reference-dispositions.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
