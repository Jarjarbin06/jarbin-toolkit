# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/SGR
# File         : test_ansi_sgr.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.ansi import (
    ANSI,
    ESC,
    CSI,
    OSC,
    G0,
    G1,
    G2,
    G3,
    DCS,
)
from jarbin_toolkit_console import Text


@pytest.mark.parametrize(
    "ansi, expected",
    [
        (ANSI, "test"),
        (ESC, "\x1btest"),
        (CSI, "\x1b[test"),
        (OSC, "\x1b]test"),
        (G0, "\x1b(test"),
        (G1, "\x1b)test"),
        (G2, "\x1b*test"),
        (G3, "\x1b+test"),
        (DCS, "\x1bPtest"),
    ],
)
def test_ansi_bases(ansi, expected):
    assert str(ansi("test")) == expected


@pytest.mark.parametrize(
    "ansi",
    [
        ANSI,
        ESC,
        CSI,
        OSC,
        G0,
        G1,
        G2,
        G3,
        DCS,
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
        TypeError,
        match="ANSI value must be a string",
    ):
        ansi(value)


def test_ansi_add():
    ansi = CSI("test")

    result = ansi + "hello"

    assert isinstance(result, Text)
    assert str(result) == "\x1b[testhello"


def test_ansi_radd():
    ansi = CSI("test")

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
    ansi = CSI("test")

    assert ansi.__add__(other) is NotImplemented
    assert ansi.__radd__(other) is NotImplemented


def test_ansi_repr():
    assert repr(ANSI("test")) == "ANSI('test')"
    assert repr(CSI("test")) == "ANSI('\\x1b[test')"
