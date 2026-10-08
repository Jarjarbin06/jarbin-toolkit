# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : test_console_context.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.console import (
    Context,
    _ContextMeta,
)
from jarbin_toolkit_console import ConsoleJError


def test_alternate_screen(monkeypatch):
    values = []

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.context.Output.write",
        lambda value: values.append(value),
    )

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.context.ScreenBuffer.alternate",
        lambda: "ALTERNATE",
    )

    Context._is_alternate = False

    Context.alternate_screen()

    assert values == ["ALTERNATE"]
    assert Context._is_alternate is True


def test_alternate_screen_already_active():
    Context._is_alternate = True

    try:
        with pytest.raises(ConsoleJError, match="Already on alternate screen"):
            Context.alternate_screen()
    finally:
        Context._is_alternate = False


def test_normal_screen(monkeypatch):
    values = []

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.context.Output.write",
        lambda value: values.append(value),
    )

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.context.ScreenBuffer.normal",
        lambda: "NORMAL",
    )

    Context._is_alternate = True

    Context.normal_screen()

    assert values == ["NORMAL"]
    assert Context._is_alternate is False


def test_normal_screen_already_active():
    Context._is_alternate = False

    try:
        with pytest.raises(ConsoleJError, match="Already on normal screen"):
            Context.normal_screen()
    finally:
        Context._is_alternate = False


def test_context_metaclass_enter(monkeypatch):
    values = []

    monkeypatch.setattr(
        Context,
        "alternate_screen",
        classmethod(lambda cls: values.append("alternate")),
    )

    _ContextMeta.__enter__(Context)

    assert values == ["alternate"]


def test_context_metaclass_exit(monkeypatch):
    values = []

    monkeypatch.setattr(
        Context,
        "normal_screen",
        classmethod(lambda cls: values.append("normal")),
    )

    _ContextMeta.__exit__(Context, None, None)

    assert values == ["normal"]
