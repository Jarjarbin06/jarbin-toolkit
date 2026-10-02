# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI
# File         : test_ansi_color.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console import (
    Color256,
    ColorRGB,
    ColorHEX,
    _Color,
)


def test_color():
    color = _Color(first=1, second=2, third=3)

    assert str(color) == "1;2;3"


def test_color256():
    color = Color256(42)

    assert color.color == 42
    assert str(color) == "42"


@pytest.mark.parametrize("value", [-1, 256, "42", None, 1.5])
def test_color256_invalid(value):
    with pytest.raises(ValueError, match="Color must be a number between 0 and 255"):
        Color256(value)


def test_color_rgb():
    color = ColorRGB(10, 20, 30)

    assert color.r == 10
    assert color.g == 20
    assert color.b == 30
    assert str(color) == "10;20;30"


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


def test_color_hex():
    color = ColorHEX("058AcF")

    assert str(color) == "058ACF"


def test_color_hex_with_hashtag():
    color = ColorHEX("#058AcF")

    assert str(color) == "058ACF"


@pytest.mark.parametrize("value", [-1, "42", None, 1.5, "0000000", "X00er0", "'00000", ""],
)
def test_color_hex_invalid(value):
    with pytest.raises(
        ValueError,
        match="HEX color must be string and contain exactly 6 hexadecimal digits",
    ):
        ColorHEX(value)


def test_color_rgb_to_hex():
    color = ColorRGB(10, 20, 30).to_hex()

    assert str(color) == "0A141E"


def test_color_hex_to_rgb():
    color = ColorHEX("0A141E").to_rgb()

    assert color.r == 10
    assert color.g == 20
    assert color.b == 30
    assert str(color) == "10;20;30"
