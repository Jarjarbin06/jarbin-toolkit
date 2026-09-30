# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/SGR
# File         : test_ansi_sgr.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.ansi.sgr import (
    SGR,
    SGRReset,
    SGRAttribute,
    SGRAdvancedUnderline,
    SGRStandardColorForeground,
    SGRStandardColorBackground,
    SGRStandardColorForegroundBright,
    SGRStandardColorBackgroundBright,
    SGRColorExtender,
    SGRPosition,
)
from jarbin_toolkit_console.ansi import (
    Color256,
    ColorRGB,
)


def test_sgr():
    assert str(SGR(SGRAttribute.BOLD)) == "\x1b[1m"
    assert str(SGR(SGRAttribute.BOLD, SGRAttribute.ITALIC)) == "\x1b[1;3m"


def test_sgr_color():
    assert str(
        SGR(SGRColorExtender.FOREGROUND, ColorRGB(255, 0, 0))
    ) == "\x1b[38;2;255;0;0m"

    assert str(
        SGR(SGRColorExtender.BACKGROUND, Color256(42))
    ) == "\x1b[48;5;42m"


def test_sgr_empty():
    with pytest.raises(ValueError, match="SGR values are required"):
        SGR()


def test_sgr_invalid_value():
    with pytest.raises(TypeError, match="SGR values must be strings or Color"):
        SGR(123)


def test_sgr_reset():
    assert str(SGR.reset()) == "\x1b[0m"
    assert str(SGR.reset(SGRReset.BOLD)) == "\x1b[22m"
    assert str(
        SGR.reset(SGRReset.BOLD, SGRReset.ITALIC)
    ) == "\x1b[22;23m"


def test_sgr_reset_invalid():
    with pytest.raises(TypeError, match="SGR values must all be SGRReset"):
        SGR.reset(SGRAttribute.BOLD)


def test_sgr_attribute():
    assert str(SGR.attribute(SGRAttribute.BOLD)) == "\x1b[1m"
    assert str(
        SGR.attribute(SGRAttribute.BOLD, SGRAttribute.ITALIC)
    ) == "\x1b[1;3m"


def test_sgr_attribute_invalid():
    with pytest.raises(TypeError, match="SGR values must be SGRAttribute"):
        SGR.attribute(SGRReset.ALL)


def test_sgr_foreground():
    assert str(
        SGR.foreground(SGRStandardColorForeground.RED)
    ) == "\x1b[31m"

    assert str(
        SGR.foreground(SGRStandardColorForegroundBright.RED)
    ) == "\x1b[91m"


@pytest.mark.parametrize(
    "color",
    [
        SGRStandardColorBackground.RED,
        SGRStandardColorBackgroundBright.RED,
        SGRAttribute.BOLD,
        "31",
    ],
)
def test_sgr_foreground_invalid(color):
    with pytest.raises(
        TypeError,
        match="SGR color must be SGRStandardColorForeground or SGRStandardColorForegroundBright",
    ):
        SGR.foreground(color)


def test_sgr_background():
    assert str(
        SGR.background(SGRStandardColorBackground.BLUE)
    ) == "\x1b[44m"

    assert str(
        SGR.background(SGRStandardColorBackgroundBright.BLUE)
    ) == "\x1b[104m"


@pytest.mark.parametrize(
    "color",
    [
        SGRStandardColorForeground.BLUE,
        SGRStandardColorForegroundBright.BLUE,
        SGRAttribute.BOLD,
        "44",
    ],
)
def test_sgr_background_invalid(color):
    with pytest.raises(
        TypeError,
        match="SGR color must be SGRStandardColorBackground or SGRStandardColorBackgroundBright",
    ):
        SGR.background(color)


def test_sgr_color():
    assert str(
        SGR.color(
            SGRColorExtender.FOREGROUND,
            ColorRGB(255, 128, 0),
        )
    ) == "\x1b[38;2;255;128;0m"

    assert str(
        SGR.color(
            SGRColorExtender.BACKGROUND,
            Color256(42),
        )
    ) == "\x1b[48;5;42m"


def test_sgr_color_invalid_extender():
    with pytest.raises(
        TypeError,
        match="SGR extender must be SGRColorExtender",
    ):
        SGR.color(SGRAttribute.BOLD, ColorRGB(255, 0, 0))


def test_sgr_color_invalid_color():
    with pytest.raises(
        TypeError,
        match="SGR color must be Color256 or ColorRGB",
    ):
        SGR.color(SGRColorExtender.FOREGROUND, SGRAttribute.BOLD)


def test_sgr_underline():
    assert str(SGR.underline()) == "\x1b[4:1m"

    assert str(
        SGR.underline(SGRAdvancedUnderline.WAVY)
    ) == "\x1b[4:3m"

    assert str(
        SGR.underline(
            SGRAdvancedUnderline.DOUBLE,
            ColorRGB(255, 0, 0),
        )
    ) == "\x1b[4:2;58;2;255;0;0m"

    assert str(
        SGR.underline(
            SGRAdvancedUnderline.DOTTED,
            Color256(42),
        )
    ) == "\x1b[4:4;58;5;42m"


def test_sgr_underline_invalid_style():
    with pytest.raises(
        TypeError,
        match="SGR style must be SGRAdvancedUnderline",
    ):
        SGR.underline(SGRAttribute.UNDERLINE)


def test_sgr_underline_invalid_color():
    with pytest.raises(
        TypeError,
        match="SGR color must be Color256 or ColorRGB",
    ):
        SGR.underline(
            SGRAdvancedUnderline.SINGLE,
            SGRAttribute.BOLD,
        )


def test_sgr_position():
    assert str(
        SGR.position(SGRPosition.SUPERSCRIPT)
    ) == "\x1b[73m"

    assert str(
        SGR.position(SGRPosition.SUBSCRIPT)
    ) == "\x1b[74m"


def test_sgr_position_invalid():
    with pytest.raises(
        TypeError,
        match="SGR type must be SGRPosition",
    ):
        SGR.position(SGRAttribute.BOLD)
