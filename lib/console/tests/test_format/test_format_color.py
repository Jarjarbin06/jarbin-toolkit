# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : test_format_color.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console import (
    PresetColor,
    Color256,
    ColorRGB,
    ColorHEX,
    Text,
)
from jarbin_toolkit_console.ansi.sgr import (
    SGR,
    SGRColorExtender,
    SGRReset,
    SGRColorMode,
)


def test_color_foreground_rgb():
    assert str(
        Text("Hello").f_color_foreground(ColorRGB(255, 0, 0))
    ) == "\x1b[38;2;255;0;0mHello\x1b[39m"


def test_color_foreground_256():
    assert str(
        Text("Hello").f_color_foreground(Color256(42))
    ) == "\x1b[38;5;42mHello\x1b[39m"


def test_color_foreground_hex():
    assert str(
        Text("Hello").f_color_foreground(ColorHEX("#FF0000"))
    ) == "\x1b[38;2;255;0;0mHello\x1b[39m"


def test_color_foreground_without_reset():
    assert str(
        Text("Hello").f_color_foreground(
            ColorRGB(255, 0, 0),
            reset=False,
        )
    ) == "\x1b[38;2;255;0;0mHello"


def test_color_foreground_standard():
    from jarbin_toolkit_console.ansi.sgr import SGRStandardColorForeground

    assert str(
        Text("Hello").f_color_foreground(
            SGRStandardColorForeground.RED
        )
    ) == "\x1b[31mHello\x1b[39m"


def test_color_background_rgb():
    assert str(
        Text("Hello").f_color_background(ColorRGB(0, 255, 0))
    ) == "\x1b[48;2;0;255;0mHello\x1b[49m"


def test_color_background_256():
    assert str(
        Text("Hello").f_color_background(Color256(42))
    ) == "\x1b[48;5;42mHello\x1b[49m"


def test_color_background_hex():
    assert str(
        Text("Hello").f_color_background(ColorHEX("#00FF00"))
    ) == "\x1b[48;2;0;255;0mHello\x1b[49m"


def test_color_background_standard():
    from jarbin_toolkit_console.ansi.sgr import SGRStandardColorBackground

    assert str(
        Text("Hello").f_color_background(
            SGRStandardColorBackground.BLUE
        )
    ) == "\x1b[44mHello\x1b[49m"


@pytest.mark.parametrize(
    "method, reset",
    [
        (Text.f_color_black, "\x1b[30mHello\x1b[39m"),
        (Text.f_color_red, "\x1b[31mHello\x1b[39m"),
        (Text.f_color_green, "\x1b[32mHello\x1b[39m"),
        (Text.f_color_yellow, "\x1b[33mHello\x1b[39m"),
        (Text.f_color_blue, "\x1b[34mHello\x1b[39m"),
        (Text.f_color_magenta, "\x1b[35mHello\x1b[39m"),
        (Text.f_color_cyan, "\x1b[36mHello\x1b[39m"),
        (Text.f_color_white, "\x1b[37mHello\x1b[39m"),
    ],
)
def test_color_standard_shortcuts(method, reset):
    assert str(method(Text("Hello"))) == reset


@pytest.mark.parametrize(
    "method",
    [
        Text.f_color_black,
        Text.f_color_red,
        Text.f_color_green,
        Text.f_color_yellow,
        Text.f_color_blue,
        Text.f_color_magenta,
        Text.f_color_cyan,
        Text.f_color_white,
    ],
)
def test_color_background_shortcuts(method):
    result = str(method(Text("Hello"), background=True))
    assert result.startswith("\x1b[4")
    assert result.endswith("Hello\x1b[49m")


@pytest.mark.parametrize(
    "method",
    [
        Text.f_color_black,
        Text.f_color_red,
        Text.f_color_green,
        Text.f_color_yellow,
        Text.f_color_blue,
        Text.f_color_magenta,
        Text.f_color_cyan,
        Text.f_color_white,
    ],
)
def test_color_bright_shortcuts(method):
    result = str(method(Text("Hello"), bright=True))
    assert result.endswith("Hello\x1b[39m")


def test_color_default_foreground():
    assert str(
        Text("Hello").f_color_default_foreground()
    ) == "\x1b[39mHello"


def test_color_default_background():
    assert str(
        Text("Hello").f_color_default_background()
    ) == "\x1b[49mHello"


@pytest.mark.parametrize(
    "method, color",
    [
        (Text.f_color_success, PresetColor.SUCCESS),
        (Text.f_color_failure, PresetColor.FAILURE),
        (Text.f_color_error, PresetColor.ERROR),
        (Text.f_color_warning, PresetColor.WARNING),
        (Text.f_color_notice, PresetColor.NOTICE),
        (Text.f_color_info, PresetColor.INFO),
        (Text.f_color_debug, PresetColor.DEBUG),
        (Text.f_color_critical, PresetColor.CRITICAL),
    ],
)
def test_color_semantic_shortcuts(method, color):
    expected = SGR(
        SGRColorExtender.FOREGROUND,
        SGRColorMode.RGB,
        color.value,
    )
    reset = SGR(SGRReset.FOREGROUND_COLOR)

    assert str(method(Text("Hello"))) == f"{expected}Hello{reset}"


def test_color_semantic_background():
    result = Text("Hello").f_color_success(background=True)

    assert str(result).startswith(
        str(
            SGR(
                SGRColorExtender.BACKGROUND,
                SGRColorMode.RGB,
                PresetColor.SUCCESS.value,
            )
        )
    )
    assert str(result).endswith("Hello\x1b[49m")


def test_color_non_format_instance():
    class Dummy:
        _can_format = False

        def _get_sgr(self):
            raise AssertionError("SGR must not be requested")

    dummy = Dummy()
    assert ColorRGB(1, 2, 3) is not dummy
