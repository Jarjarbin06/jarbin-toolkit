# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/Cursor
# File         : test_ansi_cursor.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.ansi.cursor import (
    CursorPosition,
    CursorSave,
    CursorStyle,
    CursorMode,
    CursorStyles,
)


def test_cursor_position():
    assert str(CursorPosition.up()) == "\x1b[1A"
    assert str(CursorPosition.down()) == "\x1b[1B"
    assert str(CursorPosition.right()) == "\x1b[1C"
    assert str(CursorPosition.left()) == "\x1b[1D"

    assert str(CursorPosition.next_line()) == "\x1b[1E"
    assert str(CursorPosition.previous_line()) == "\x1b[1F"

    assert str(CursorPosition.column()) == "\x1b[1G"
    assert str(CursorPosition.row()) == "\x1b[1d"

    assert str(CursorPosition.position()) == "\x1b[1;1H"

    assert str(CursorPosition.tab()) == "\x1b[1I"
    assert str(CursorPosition.back_tab()) == "\x1b[1Z"

    assert str(CursorPosition.column_relative()) == "\x1b[1a"
    assert str(CursorPosition.row_relative()) == "\x1b[1e"
    assert str(CursorPosition.position_relative()) == "\x1b[1;1f"


def test_cursor_position_values():
    assert str(CursorPosition.up(3)) == "\x1b[3A"
    assert str(CursorPosition.down(3)) == "\x1b[3B"
    assert str(CursorPosition.right(3)) == "\x1b[3C"
    assert str(CursorPosition.left(3)) == "\x1b[3D"

    assert str(CursorPosition.next_line(3)) == "\x1b[3E"
    assert str(CursorPosition.previous_line(3)) == "\x1b[3F"

    assert str(CursorPosition.column(12)) == "\x1b[12G"
    assert str(CursorPosition.row(8)) == "\x1b[8d"

    assert str(CursorPosition.position(8, 12)) == "\x1b[8;12H"

    assert str(CursorPosition.tab(4)) == "\x1b[4I"
    assert str(CursorPosition.back_tab(4)) == "\x1b[4Z"

    assert str(CursorPosition.column_relative(12)) == "\x1b[12a"
    assert str(CursorPosition.row_relative(8)) == "\x1b[8e"
    assert str(CursorPosition.position_relative(8, 12)) == "\x1b[8;12f"


@pytest.mark.parametrize(
    "method",
    [
        CursorPosition.up,
        CursorPosition.down,
        CursorPosition.right,
        CursorPosition.left,
        CursorPosition.next_line,
        CursorPosition.previous_line,
        CursorPosition.tab,
        CursorPosition.back_tab,
    ],
)
@pytest.mark.parametrize("value", [0, -1, -100])
def test_cursor_position_invalid_n(method, value):
    with pytest.raises(
        ValueError,
        match="CursorPosition n must be a positive integer",
    ):
        method(value)


@pytest.mark.parametrize(
    "method",
    [
        CursorPosition.up,
        CursorPosition.down,
        CursorPosition.right,
        CursorPosition.left,
        CursorPosition.next_line,
        CursorPosition.previous_line,
        CursorPosition.tab,
        CursorPosition.back_tab,
    ],
)
@pytest.mark.parametrize("value", ["1", 1.5, None])
def test_cursor_position_invalid_n_type(method, value):
    with pytest.raises(
        ValueError,
        match="CursorPosition n must be a positive integer",
    ):
        method(value)


@pytest.mark.parametrize(
    "method",
    [
        CursorPosition.column,
        CursorPosition.column_relative,
    ],
)
@pytest.mark.parametrize("value", [0, -1, -100, "1", 1.5, None])
def test_cursor_position_invalid_x(method, value):
    with pytest.raises(
        ValueError,
        match="CursorPosition x must be a positive integer",
    ):
        method(value)


@pytest.mark.parametrize(
    "method",
    [
        CursorPosition.row,
        CursorPosition.row_relative,
    ],
)
@pytest.mark.parametrize("value", [0, -1, -100, "1", 1.5, None])
def test_cursor_position_invalid_y(method, value):
    with pytest.raises(
        ValueError,
        match="CursorPosition y must be a positive integer",
    ):
        method(value)


@pytest.mark.parametrize(
    "method",
    [
        CursorPosition.position,
        CursorPosition.position_relative,
    ],
)
@pytest.mark.parametrize(
    "y",
    [0, -1, -100, "1", 1.5, None],
)
def test_cursor_position_invalid_y_position(method, y):
    with pytest.raises(
        ValueError,
        match="CursorPosition y and x must be a positive integer",
    ):
        method(y, 1)


@pytest.mark.parametrize(
    "method",
    [
        CursorPosition.position,
        CursorPosition.position_relative,
    ],
)
@pytest.mark.parametrize(
    "x",
    [0, -1, -100, "1", 1.5, None],
)
def test_cursor_position_invalid_x_position(method, x):
    with pytest.raises(
        ValueError,
        match="CursorPosition y and x must be a positive integer",
    ):
        method(1, x)


def test_cursor_save():
    assert str(CursorSave.save()) == "\x1b[s"
    assert str(CursorSave.restore()) == "\x1b[u"


def test_cursor_style():
    assert str(
        CursorStyle.set(CursorStyles.DEFAULT)
    ) == "\x1b[0 q"


@pytest.mark.parametrize(
    "style",
    list(CursorStyles),
)
def test_cursor_style_values(style):
    assert str(CursorStyle.set(style)) == f"\x1b[{style} q"


@pytest.mark.parametrize(
    "style",
    [
        "0",
        0,
        None,
    ],
)
def test_cursor_style_invalid(style):
    with pytest.raises(
        TypeError,
        match="CursorStyle style must be CursorStyles",
    ):
        CursorStyle.set(style)


def test_cursor_mode():
    assert str(CursorMode.application_keys()) == "\x1b[?1h"
    assert str(CursorMode.normal_keys()) == "\x1b[?1l"

    assert str(CursorMode.blink()) == "\x1b[?12h"
    assert str(CursorMode.no_blink()) == "\x1b[?12l"

    assert str(CursorMode.show()) == "\x1b[?25h"
    assert str(CursorMode.hide()) == "\x1b[?25l"

    assert str(CursorMode.origin()) == "\x1b[?6h"
    assert str(CursorMode.absolute()) == "\x1b[?6l"

    assert str(CursorMode.autowrap()) == "\x1b[?7h"
    assert str(CursorMode.no_autowrap()) == "\x1b[?7l"

    assert str(CursorMode.save_state()) == "\x1b[?1048h"
    assert str(CursorMode.restore_state()) == "\x1b[?1048l"
