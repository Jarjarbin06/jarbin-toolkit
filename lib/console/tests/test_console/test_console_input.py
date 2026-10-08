# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : test_console_input.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.console import Input


class FakeStream:


    def __init__(
            self,
            value,
            *,
            tty=True,
        ):
        self.value = list(value)
        self.tty = tty


    def isatty(self):
        return self.tty


    def fileno(self):
        return 42


    def read(self, count):
        if not self.value:
            return ""

        return self.value.pop(0)


def patch_raw(monkeypatch):
    monkeypatch.setattr(
        "jarbin_toolkit_console.console.input.termios.tcgetattr",
        lambda fd: "OLD_SETTINGS",
    )

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.input.termios.tcsetattr",
        lambda fd, action, settings: None,
    )

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.input.tty.setraw",
        lambda fd: None,
    )

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.input.select.select",
        lambda *args: ([args[0][0]], [], []),
    )


def test_input(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: f"{prompt}value",
    )

    assert Input.input(prompt=">>> ") == ">>> value"


def test_raw_count(monkeypatch):
    patch_raw(monkeypatch)

    stream = FakeStream("abc")

    assert Input.raw(
        stream=stream,
        count=3,
        break_char=None,
    ) == "abc"


def test_raw_break_char(monkeypatch):
    patch_raw(monkeypatch)

    stream = FakeStream("ab\ncd")

    assert Input.raw(
        stream=stream,
        break_char="\n",
    ) == "ab"


def test_raw_non_tty():
    stream = FakeStream("abc", tty=False)

    assert Input.raw(stream=stream) == ""


@pytest.mark.parametrize(
    "count",
    [-1, -10],
)
def test_raw_negative_count(count):
    with pytest.raises(
        ValueError,
        match="Count must be non-negative",
    ):
        Input.raw(count=count)


@pytest.mark.parametrize(
    "timeout",
    [-1, -10],
)
def test_raw_negative_timeout(timeout):
    with pytest.raises(
        ValueError,
        match="Timeout must be non-negative",
    ):
        Input.raw(timeout=timeout)


def test_key(monkeypatch):
    values = []

    def raw(cls, **kwargs):
        values.append(kwargs)
        return "a"

    monkeypatch.setattr(Input, "raw", classmethod(raw))

    assert Input.key(timeout=2) == "a"

    assert values == [
        {
            "stream": None,
            "count": 1,
            "timeout": 2,
            "break_char": None,
            "only_tty": True,
        },
    ]


def test_keys(monkeypatch):
    values = []

    def raw(cls, **kwargs):
        values.append(kwargs)
        return "abc"

    monkeypatch.setattr(Input, "raw", classmethod(raw))

    assert Input.keys(
        count=3,
        break_char=";",
        timeout=2,
    ) == "abc"

    assert values == [
        {
            "stream": None,
            "count": 3,
            "timeout": 2,
            "break_char": ";",
            "only_tty": True,
        },
    ]


def test_raw_timeout(monkeypatch):
    patch_raw(monkeypatch)

    calls = []

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.input.monotonic",
        lambda: 0,
    )

    stream = FakeStream("abc")

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.input.select.select",
        lambda *args: calls.append(args) or ([], [], []),
    )

    assert Input.raw(
        stream=stream,
        timeout=1,
    ) == ""

    assert calls
