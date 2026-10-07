# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : test_format_border.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.format import Border
from jarbin_toolkit_console import (
    Text,
    PresetBorder,
)


def test_border_helpers():
    text = Text("Hello\nWorld")

    assert text._get_border_lines() == ["Hello", "World"]
    assert text._get_border_width(["Hello", "World"]) == 5
    assert str(text._get_border_text(["A", "B"])) == "AB"


def test_border_helpers_empty():
    text = Text("")

    assert text._get_border_lines() == [""]
    assert text._get_border_width([""]) == 0


@pytest.mark.parametrize(
    "method, expected",
    [
        (
            lambda text: text.f_border_top(),
            "─────\nHello\nWorld",
        ),
        (
            lambda text: text.f_border_bottom(),
            "Hello\nWorld\n─────",
        ),
        (
            lambda text: text.f_border_left(),
            "│Hello\n│World",
        ),
        (
            lambda text: text.f_border_right(),
            "Hello│\nWorld│",
        ),
        (
            lambda text: text.f_border_separator(),
            "─────",
        ),
    ],
)
def test_border_single_operations(method, expected):
    assert str(method(Text("Hello\nWorld"))) == expected


@pytest.mark.parametrize(
    "border, horizontal, vertical",
    [
        (PresetBorder.SINGLE, "─", "│"),
        (PresetBorder.DOUBLE, "═", "║"),
        (PresetBorder.HEAVY, "━", "┃"),
        (PresetBorder.ROUNDED, "─", "│"),
        (PresetBorder.ASCII, "-", "|"),
    ],
)
def test_border_box_variants(border, horizontal, vertical):
    result = str(
        Text("Hello\nWorld").f_border_box(border=border)
    )

    assert result.splitlines()[0] == (
        border.value[2] + horizontal * 5 + border.value[3]
    )
    assert result.splitlines()[1] == f"{vertical}Hello{vertical}"
    assert result.splitlines()[2] == f"{vertical}World{vertical}"
    assert result.splitlines()[3] == (
        border.value[4] + horizontal * 5 + border.value[5]
    )


def test_border_padding():
    result = str(
        Text("Hello").f_border_box(padding=1)
    )

    assert result == (
        "┌─────────┐\n"
        "│         │\n"
        "│  Hello  │\n"
        "│         │\n"
        "└─────────┘"
    )


@pytest.mark.parametrize(
    "method",
    [
        lambda text: text.f_border_top(padding=-1),
        lambda text: text.f_border_bottom(padding=-1),
        lambda text: text.f_border_left(padding=-1),
        lambda text: text.f_border_right(padding=-1),
        lambda text: text.f_border_box(padding=-1),
        lambda text: text.f_border_title("Title", padding=-1),
    ],
)
def test_border_negative_padding(method):
    with pytest.raises(ValueError, match="Padding cannot be negative"):
        method(Text("Hello"))


def test_border_title():
    result = str(
        Text("Hello").f_border_title("My Title")
    )

    assert result == (
        "┌─ My Title ─┐\n"
        "│Hello       │\n"
        "└────────────┘"
    )


def test_border_title_with_padding():
    result = str(
        Text("Hello").f_border_title("Title", padding=1)
    )

    assert result.splitlines()[0] == "┌─ Title ─────┐"
    assert result.splitlines()[1] == "│             │"
    assert result.splitlines()[2] == "│  Hello      │"
    assert result.splitlines()[3] == "│             │"
    assert result.splitlines()[4] == "└─────────────┘"


@pytest.mark.parametrize(
    "method, border",
    [
        (Text.f_border_single, PresetBorder.SINGLE),
        (Text.f_border_double, PresetBorder.DOUBLE),
        (Text.f_border_heavy, PresetBorder.HEAVY),
        (Text.f_border_rounded, PresetBorder.ROUNDED),
        (Text.f_border_ascii, PresetBorder.ASCII),
    ],
)
def test_border_shortcuts(method, border):
    text = Text("Hello")
    assert str(method(text)) == str(text.f_border_box(border=border))


def test_border_nested():
    result = Text("Hello").f_border_nested(depth=2)

    assert str(result) == (
        "┌───────┐\n"
        "│┌─────┐│\n"
        "││Hello││\n"
        "│└─────┘│\n"
        "└───────┘"
    )
