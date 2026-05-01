"""Pure-unit tests for selvedge.aliases regexes and the basis-aware diagnostic
emitted by `_resolve_alias_to_object_id` for issue/forward-reference shapes.

S158 / DV-S158-1: the diagnostic detects `OI-...` and `FR-...` alias shapes that
cannot resolve via `objects.alias` and emits a guidance message instead of the
generic "unresolved alias" refusal. The regex must admit all real issue-alias
forms in the substrate (legacy `OI-NNN`, compound `OI-NNN-NNN`, session-form
`OI-SNNN-N`) and reject DV/SPEC/EF aliases plus malformed input.
"""
from __future__ import annotations

import sqlite3

import pytest

from selvedge.aliases import _ISSUE_ALIAS_RE, _FR_ALIAS_RE, _resolve_alias_to_object_id
from selvedge.errors import SelvedgeError


@pytest.mark.parametrize("alias", [
    "OI-001",
    "OI-019",
    "OI-079-001",
    "OI-086-003",
    "OI-S088-1",
    "OI-S156-2",
    "OI-S001-12",
])
def test_issue_alias_regex_admits_real_forms(alias):
    assert _ISSUE_ALIAS_RE.match(alias) is not None


@pytest.mark.parametrize("alias", [
    "OI-foo",
    "OI-1",
    "OI-S156",
    "OI-SS156-1",
    "DV-S156-1",
    "EF-S157-1",
    "SPEC-prompt-development-v14",
    "FR-S156-6",
])
def test_issue_alias_regex_rejects_non_issue_forms(alias):
    assert _ISSUE_ALIAS_RE.match(alias) is None


@pytest.mark.parametrize("alias", [
    "FR-S156-6",
    "FR-S001-1",
    "FR-S999-99",
])
def test_fr_alias_regex_admits_real_forms(alias):
    assert _FR_ALIAS_RE.match(alias) is not None


@pytest.mark.parametrize("alias", [
    "FR-156-6",
    "FR-S156",
    "FR-S1-1",
    "OI-S156-1",
])
def test_fr_alias_regex_rejects_non_fr_forms(alias):
    assert _FR_ALIAS_RE.match(alias) is None


@pytest.fixture
def empty_objects_conn():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute(
        "CREATE TABLE objects (object_id INTEGER PRIMARY KEY, alias TEXT)"
    )
    return conn


def test_resolve_issue_alias_emits_basis_aware_hint(empty_objects_conn):
    with pytest.raises(SelvedgeError) as exc:
        _resolve_alias_to_object_id(empty_objects_conn, "OI-S156-1")
    assert exc.value.code == "E_REFUSAL_T01"
    msg = str(exc.value)
    assert "issue alias" in msg
    assert "EF-" in msg
    assert "DV-" in msg


def test_resolve_legacy_issue_alias_emits_hint(empty_objects_conn):
    with pytest.raises(SelvedgeError) as exc:
        _resolve_alias_to_object_id(empty_objects_conn, "OI-001")
    assert "issue alias" in str(exc.value)


def test_resolve_fr_alias_emits_basis_aware_hint(empty_objects_conn):
    with pytest.raises(SelvedgeError) as exc:
        _resolve_alias_to_object_id(empty_objects_conn, "FR-S156-6")
    assert exc.value.code == "E_REFUSAL_T01"
    msg = str(exc.value)
    assert "forward-reference alias" in msg
    assert "DV-" in msg


def test_resolve_unknown_shape_falls_through_to_generic(empty_objects_conn):
    with pytest.raises(SelvedgeError) as exc:
        _resolve_alias_to_object_id(empty_objects_conn, "ZZ-not-real")
    msg = str(exc.value)
    assert "unresolved alias" in msg
    assert "issue alias" not in msg
    assert "forward-reference alias" not in msg


def test_resolve_returns_object_id_when_alias_present(empty_objects_conn):
    empty_objects_conn.execute(
        "INSERT INTO objects (object_id, alias) VALUES (?, ?)",
        (42, "DV-S158-1"),
    )
    assert _resolve_alias_to_object_id(empty_objects_conn, "DV-S158-1") == 42
