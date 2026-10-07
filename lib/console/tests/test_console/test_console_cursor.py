# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : test_format_cursor.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.console.cursor import Cursor


def test_get_cursor_position(monkeypatch):
    expected = (12, 34)

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.cursor.Query.cursor_position",
        lambda: expected,
    )

    assert Cursor.get_cursor_position() == expected


def test_move_cursor(monkeypatch):
    values = []

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.cursor.Output.write",
        lambda value: values.append(value),
    )

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.cursor.CursorPosition.position",
        lambda x, y: f"POSITION({x},{y})",
    )

    Cursor.move_cursor(12, 34)

    assert values == ["POSITION(12,34)"]


def test_hide_cursor(monkeypatch):
    values = []

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.cursor.Output.write",
        lambda value: values.append(value),
    )

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.cursor.CursorMode.hide",
        lambda: "HIDE",
    )

    Cursor.hide_cursor()

    assert values == ["HIDE"]


def test_show_cursor(monkeypatch):
    values = []

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.cursor.Output.write",
        lambda value: values.append(value),
    )

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.cursor.CursorMode.show",
        lambda: "SHOW",
    )

    Cursor.show_cursor()

    assert values == ["SHOW"]
