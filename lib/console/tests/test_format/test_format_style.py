import pytest

from jarbin_toolkit_console import (
    ColorRGB,
    Color256,
    Text,
)
from jarbin_toolkit_console.ansi.sgr import SGRAdvancedUnderline


@pytest.mark.parametrize(
    "method, prefix, suffix",
    [
        (Text.f_style_bold, "\x1b[1m", "\x1b[22m"),
        (Text.f_style_faint, "\x1b[2m", "\x1b[22m"),
        (Text.f_style_dim, "\x1b[2m", "\x1b[22m"),
        (Text.f_style_italic, "\x1b[3m", "\x1b[23m"),
        (Text.f_style_strikethrough, "\x1b[9m", "\x1b[29m"),
        (Text.f_style_reverse, "\x1b[7m", "\x1b[27m"),
        (Text.f_style_hide, "\x1b[8m", "\x1b[28m"),
        (Text.f_style_frame, "\x1b[51m", "\x1b[54m"),
        (Text.f_style_encircle, "\x1b[52m", "\x1b[54m"),
        (Text.f_style_overline, "\x1b[53m", "\x1b[55m"),
        (Text.f_style_superscript, "\x1b[73m", "\x1b[75m"),
        (Text.f_style_subscript, "\x1b[74m", "\x1b[75m"),
    ],
)
def test_style_methods(method, prefix, suffix):
    assert str(method(Text("Hello"))) == f"{prefix}Hello{suffix}"


def test_style_reset():
    assert str(
        Text("Hello").f_style_reset()
    ) == "\x1b[0mHello"


def test_style_underline():
    assert str(
        Text("Hello").f_style_underline()
    ) == "\x1b[4mHello\x1b[24m"


@pytest.mark.parametrize(
    "style, expected",
    [
        (SGRAdvancedUnderline.SINGLE, "\x1b[4:1m"),
        (SGRAdvancedUnderline.DOUBLE, "\x1b[4:2m"),
        (SGRAdvancedUnderline.WAVY, "\x1b[4:3m"),
        (SGRAdvancedUnderline.DOTTED, "\x1b[4:4m"),
        (SGRAdvancedUnderline.DASHED, "\x1b[4:5m"),
    ],
)
def test_style_underline_variants(style, expected):
    assert str(
        Text("Hello").f_style_underline(style=style)
    ) == f"{expected}Hello\x1b[24m"


def test_style_underline_rgb_color():
    assert str(
        Text("Hello").f_style_underline(
            style=SGRAdvancedUnderline.DOUBLE,
            color=ColorRGB(255, 0, 0),
        )
    ) == "\x1b[4:2;58;2;255;0;0mHello\x1b[24m"


def test_style_underline_256_color():
    assert str(
        Text("Hello").f_style_underline(
            style=SGRAdvancedUnderline.DOTTED,
            color=Color256(42),
        )
    ) == "\x1b[4:4;58;5;42mHello\x1b[24m"


@pytest.mark.parametrize(
    "method",
    [
        Text.f_style_bold,
        Text.f_style_faint,
        Text.f_style_dim,
        Text.f_style_italic,
        Text.f_style_strikethrough,
        Text.f_style_blink,
        Text.f_style_reverse,
        Text.f_style_hide,
        Text.f_style_frame,
        Text.f_style_encircle,
        Text.f_style_overline,
        Text.f_style_superscript,
        Text.f_style_subscript,
    ],
)
def test_style_without_reset(method):
    assert "\x1b[" in str(method(Text("Hello"), reset=False))
    assert str(method(Text("Hello"), reset=False)).endswith("Hello")


def test_style_blink_slow():
    assert str(
        Text("Hello").f_style_blink()
    ) == "\x1b[5mHello\x1b[25m"


def test_style_blink_fast():
    assert str(
        Text("Hello").f_style_blink(is_fast=True)
    ) == "\x1b[6mHello\x1b[25m"


def test_style_show():
    # Intended behavior: disable the hidden attribute for the text,
    # then restore hidden state after the text when requested.
    assert str(
        Text("Hello").f_style_show()
    ) == "\x1b[28mHello\x1b[8m"
