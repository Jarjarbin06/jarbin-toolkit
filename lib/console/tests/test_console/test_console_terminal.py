# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : test_console_terminal.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.console import Terminal


class FakeStream:


    def __init__(
            self,
            *,
            tty=True,
            fd=1,
        ):
        self.tty = tty
        self.fd = fd


    def isatty(self):
        return self.tty


    def fileno(self):
        return self.fd


def test_terminal_is_tty():
    assert Terminal.is_tty(stream=FakeStream(tty=True))
    assert not Terminal.is_tty(stream=FakeStream(tty=False))


def test_terminal_size(monkeypatch):
    class Size:
        columns = 120
        lines = 40

    def get_terminal_size(fd):
        assert fd == 42
        return Size()

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.terminal.get_terminal_size",
        get_terminal_size,
    )

    stream = FakeStream(fd=42)

    assert Terminal.size(stream=stream) == (120, 40)


def test_terminal_size_non_tty():
    stream = FakeStream(tty=False)

    assert Terminal.size(stream=stream) is None


def test_terminal_width(monkeypatch):
    monkeypatch.setattr(
        Terminal,
        "size",
        classmethod(lambda cls, **kwargs: (120, 40)),
    )

    assert Terminal.width(stream=FakeStream()) == 120


def test_terminal_height(monkeypatch):
    monkeypatch.setattr(
        Terminal,
        "size",
        classmethod(lambda cls, **kwargs: (120, 40)),
    )

    assert Terminal.height(stream=FakeStream()) == 40
