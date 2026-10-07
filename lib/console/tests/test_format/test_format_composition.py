# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : test_format_composition.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console import (
    ColorRGB,
    Color256,
    ColorHEX,
    Text,
)
from jarbin_toolkit_console.format import FormatStyle


def test_composition_style():
    assert str(
        Text("Hello").f_composition_style(FormatStyle.BOLD)
    ) == "\x1b[1mHello\x1b[22m"


def test_composition_multiple_styles():
    assert str(
        Text("Hello").f_composition_style(
            FormatStyle.BOLD,
            FormatStyle.ITALIC,
        )
    ) == "\x1b[1;3mHello\x1b[23;22m"


def test_composition_style_invalid():
    with pytest.raises(TypeError, match="Styles must be FormatStyle"):
        Text("Hello").f_composition_style("bold")


@pytest.mark.parametrize(
    "kwargs, expected",
    [
        (
            {"foreground": ColorRGB(255, 0, 0)},
            "\x1b[38;2;255;0;0mHello\x1b[39m",
        ),
        (
            {"background": Color256(42)},
            "\x1b[48;5;42mHello\x1b[49m",
        ),
        (
            {
                "foreground": ColorHEX("#FF0000"),
                "background": ColorRGB(0, 255, 0),
            },
            "\x1b[38;2;255;0;0m\x1b[48;2;0;255;0mHello\x1b[49m\x1b[39m",
        ),
    ],
)
def test_composition_colored(kwargs, expected):
    from jarbin_toolkit_console.enums import PresetColor

    class ColorHolder:
        def __init__(self, value):
            self.value = value

    converted = {
        key: ColorHolder(value)
        for key, value in kwargs.items()
    }

    assert str(
        Text("Hello").f_composition_colored(**converted)
    ) == expected


@pytest.mark.parametrize(
    "name",
    ["foreground", "background"],
)
def test_composition_colored_invalid(name):
    class ColorHolder:
        value = "invalid"

    with pytest.raises(
        TypeError,
        match=f"{name} must contain a Color256, ColorRGB or ColorHEX",
    ):
        Text("Hello").f_composition_colored(
            **{name: ColorHolder()}
        )


def test_composition_chain():
    result = Text("Hello").f_composition_chain(
        lambda value: value.f_style_bold(),
        lambda value: value.f_color_red(),
        lambda value: value.f_decoration_prefix("> "),
    )

    assert str(result) == (
        "> \x1b[31m\x1b[1mHello\x1b[22m\x1b[39m"
    )


def test_composition_chain_empty():
    text = Text("Hello")
    assert text.f_composition_chain() is text


def test_composition_helpers_non_format():
    from jarbin_toolkit_console.format.composition import Composition

    composition = Composition()
    assert composition.f_composition_chain() is composition
