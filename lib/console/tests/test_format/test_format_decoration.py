import pytest

from jarbin_toolkit_console import (
    Text,
    PresetSymbol,
)
from jarbin_toolkit_console.format import FormatOrder


def test_decoration_prefix_suffix_wrap():
    text = Text("Hello")

    assert str(text.f_decoration_prefix("> ")) == "> Hello"
    assert str(text.f_decoration_suffix(" !")) == "Hello !"
    assert str(text.f_decoration_wrap("[", "]")) == "[Hello]"


@pytest.mark.parametrize(
    "method, expected",
    [
        (Text.f_decoration_brackets, "[Hello]"),
        (Text.f_decoration_parentheses, "(Hello)"),
        (Text.f_decoration_braces, "{Hello}"),
        (Text.f_decoration_quotes, '"Hello"'),
        (Text.f_decoration_backticks, "'Hello'"),
        (Text.f_decoration_angle_brackets, "<Hello>"),
    ],
)
def test_decoration_wrappers(method, expected):
    assert str(method(Text("Hello"))) == expected


@pytest.mark.parametrize(
    "order, expected",
    [
        (FormatOrder.BEFORE, "✓ Hello"),
        (FormatOrder.AFTER, "Hello ✓"),
    ],
)
def test_decoration_symbol(order, expected):
    assert str(
        Text("Hello").f_decoration_symbol(
            PresetSymbol.CHECK,
            order=order,
        )
    ) == expected


@pytest.mark.parametrize(
    "method, symbol",
    [
        (Text.f_decoration_check, PresetSymbol.CHECK),
        (Text.f_decoration_cross, PresetSymbol.CROSS),
        (Text.f_decoration_warning, PresetSymbol.WARNING),
        (Text.f_decoration_info, PresetSymbol.INFO),
        (Text.f_decoration_question, PresetSymbol.QUESTION),
        (Text.f_decoration_arrow, PresetSymbol.ARROW),
        (Text.f_decoration_star, PresetSymbol.STAR),
        (Text.f_decoration_ellipsis, PresetSymbol.ELLIPSIS),
    ],
)
def test_decoration_symbol_shortcuts(method, symbol):
    assert str(method(Text("Hello"))) == f"{symbol} Hello"


def test_decoration_symbol_invalid_order():
    assert str(
        Text("Hello").f_decoration_symbol(
            PresetSymbol.CHECK,
            order="invalid",
        )
    ) == "Hello"


@pytest.mark.parametrize(
    "fill, width, expected",
    [
        ("─", 5, "─────"),
        ("-", 3, "---"),
        ("*", 1, "*"),
    ],
)
def test_decoration_separator(fill, width, expected):
    assert str(
        Text("Hello").f_decoration_separator(
            fill=fill,
            width=width,
        )
    ) == expected


def test_decoration_separator_default_width():
    assert str(
        Text("Hello").f_decoration_separator()
    ) == "─────"
