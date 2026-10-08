# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/SGR
# File         : test_ansi_sgr.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.ansi import Sequence
from jarbin_toolkit_console import (
    Text,
    ConsoleJError,
)


@pytest.mark.parametrize(
    "ansi, expected",
    [
        (Sequence.ANSI, "test"),
        (Sequence.ESC, "\x1btest"),
        (Sequence.CSI, "\x1b[test"),
        (Sequence.OSC, "\x1b]test"),
        (Sequence.G0, "\x1b(test"),
        (Sequence.G1, "\x1b)test"),
        (Sequence.G2, "\x1b*test"),
        (Sequence.G3, "\x1b+test"),
        (Sequence.DCS, "\x1bPtest"),
    ],
)
def test_ansi_bases(ansi, expected):
    assert str(ansi("test")) == expected


@pytest.mark.parametrize(
    "ansi",
    [
        Sequence.ANSI,
        Sequence.ESC,
        Sequence.CSI,
        Sequence.OSC,
        Sequence.G0,
        Sequence.G1,
        Sequence.G2,
        Sequence.G3,
        Sequence.DCS,
    ],
)
@pytest.mark.parametrize(
    "value",
    [
        1,
        None,
        1.5,
        True,
    ],
)
def test_ansi_invalid_value(ansi, value):
    with pytest.raises(
        ConsoleJError,
        match="ANSI value must be a string",
    ):
        ansi(value)


def test_ansi_add():
    ansi = Sequence.CSI("test")

    result = ansi + "hello"

    assert isinstance(result, Text)
    assert str(result) == "\x1b[testhello"


def test_ansi_radd():
    ansi = Sequence.CSI("test")

    result = "hello" + ansi

    assert isinstance(result, Text)
    assert str(result) == "hello\x1b[test"


@pytest.mark.parametrize(
    "other",
    [
        1,
        1.5,
        None,
        True,
        object(),
    ],
)
def test_ansi_invalid_add(other):
    ansi = Sequence.CSI("test")

    assert ansi.__add__(other) is NotImplemented
    assert ansi.__radd__(other) is NotImplemented


def test_ansi_repr():
    assert repr(Sequence.ANSI("test")) == "ANSI('test')"
    assert repr(Sequence.CSI("test")) == "ANSI('\\x1b[test')"
