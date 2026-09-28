# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/SGR
# File         : test_ansi_sgr_color.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.ansi.sgr import (
    SGRColorMode,
    Color256,
    ColorRGB,
    _Color,
)


def test_color():
    color = _Color(first=1, second=2, third=3)

    assert str(color) == "1;2;3"


def test_color_ignores_mode_validation():
    color = _Color(mode=SGRColorMode.RGB, value=255)

    assert str(color) == "2;255"


def test_color_invalid_value():
    with pytest.raises(ValueError, match="Color values must all be numbers"):
        _Color(value="invalid")


def test_color256():
    color = Color256(42)

    assert color.mode == SGRColorMode.INDEXED
    assert color.color == 42
    assert str(color) == "5;42"


@pytest.mark.parametrize("value", [-1, 256, "42", None, 1.5])
def test_color256_invalid(value):
    with pytest.raises(ValueError, match="Color must be a number between 0 and 255"):
        Color256(value)


def test_color_rgb():
    color = ColorRGB(10, 20, 30)

    assert color.mode == SGRColorMode.RGB
    assert color.r == 10
    assert color.g == 20
    assert color.b == 30
    assert str(color) == "2;10;20;30"


@pytest.mark.parametrize(
    "values",
    [
        (-1, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
        (256, 0, 0),
        (0, 256, 0),
        (0, 0, 256),
        ("255", 0, 0),
        (0, "255", 0),
        (0, 0, "255"),
    ],
)
def test_color_rgb_invalid(values):
    with pytest.raises(
        ValueError,
        match="RGB values must all be numbers between 0 and 255",
    ):
        ColorRGB(*values)
