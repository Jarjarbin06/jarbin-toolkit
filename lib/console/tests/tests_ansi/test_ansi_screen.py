# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/Screen
# File         : test_ansi_screen.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.ansi.screen import (
    ScreenErase,
    ScreenEdit,
    ScreenScroll,
    ScreenMargins,
    ScreenWriteMode,
    ScreenBuffer,
    ScreenTest,
    ScreenRectangle,
    ScreenMode,
    ScreenSize,
    ScreenControl,
)
from jarbin_toolkit_console.ansi.screen import (
    ScreenDisplayEraseMode,
    ScreenLineEraseMode,
)


def test_screen_erase_display():
    assert str(
        ScreenErase.erase_display()
    ) == "\x1b[2J"

    assert str(
        ScreenErase.erase_display(ScreenDisplayEraseMode.BELOW_CURSOR)
    ) == "\x1b[0J"

    assert str(
        ScreenErase.erase_display(ScreenDisplayEraseMode.ABOVE_CURSOR)
    ) == "\x1b[1J"

    assert str(
        ScreenErase.erase_display(ScreenDisplayEraseMode.ALL)
    ) == "\x1b[2J"


@pytest.mark.parametrize(
    "mode",
    [
        ScreenLineEraseMode.CURSOR_TO_END,
        ScreenLineEraseMode.START_TO_CURSOR,
        ScreenLineEraseMode.ALL,
    ],
)
def test_screen_erase_line(mode):
    expected = {
        ScreenLineEraseMode.CURSOR_TO_END: "\x1b[0K",
        ScreenLineEraseMode.START_TO_CURSOR: "\x1b[1K",
        ScreenLineEraseMode.ALL: "\x1b[2K",
    }

    assert str(
        ScreenErase.erase_line(mode)
    ) == expected[mode]


@pytest.mark.parametrize(
    "mode",
    [
        "0",
        0,
        None,
        ScreenLineEraseMode.ALL,
    ],
)
def test_screen_erase_display_invalid(mode):
    with pytest.raises(
        ValueError,
        match="ScreenErase mode must be ScreenDisplayEraseMode",
    ):
        ScreenErase.erase_display(mode)


@pytest.mark.parametrize(
    "mode",
    [
        "0",
        0,
        None,
        ScreenDisplayEraseMode.ALL,
    ],
)
def test_screen_erase_line_invalid(mode):
    with pytest.raises(
        ValueError,
        match="ScreenErase mode must be ScreenLineEraseMode",
    ):
        ScreenErase.erase_line(mode)


def test_screen_edit():
    assert str(
        ScreenEdit.insert_characters()
    ) == "\x1b[1@"

    assert str(
        ScreenEdit.delete_characters()
    ) == "\x1b[1P"

    assert str(
        ScreenEdit.erase_characters()
    ) == "\x1b[1X"

    assert str(
        ScreenEdit.repeat_character()
    ) == "\x1b[1b"

    assert str(
        ScreenEdit.insert_lines()
    ) == "\x1b[1L"

    assert str(
        ScreenEdit.delete_lines()
    ) == "\x1b[1M"


@pytest.mark.parametrize(
    "method",
    [
        ScreenEdit.insert_characters,
        ScreenEdit.delete_characters,
        ScreenEdit.erase_characters,
        ScreenEdit.repeat_character,
        ScreenEdit.insert_lines,
        ScreenEdit.delete_lines,
    ],
)
def test_screen_edit_values(method):
    assert str(method(4)) in [
        "\x1b[4@",
        "\x1b[4P",
        "\x1b[4X",
        "\x1b[4b",
        "\x1b[4L",
        "\x1b[4M",
    ]


@pytest.mark.parametrize(
    "method",
    [
        ScreenEdit.insert_characters,
        ScreenEdit.delete_characters,
        ScreenEdit.erase_characters,
        ScreenEdit.repeat_character,
        ScreenEdit.insert_lines,
        ScreenEdit.delete_lines,
    ],
)
@pytest.mark.parametrize(
    "value",
    [0, -1, -100, "1", 1.5, None],
)
def test_screen_edit_invalid(method, value):
    with pytest.raises(
        ValueError,
        match="ScreenEdit n must be positive int",
    ):
        method(value)


def test_screen_scroll():
    assert str(
        ScreenScroll.left()
    ) == "\x1b[1 @"

    assert str(
        ScreenScroll.right()
    ) == "\x1b[1 A"

    assert str(
        ScreenScroll.left(3)
    ) == "\x1b[3 @"

    assert str(
        ScreenScroll.right(3)
    ) == "\x1b[3 A"

    assert str(
        ScreenScroll.set_region(2, 20)
    ) == "\x1b[2;20r"

    assert str(
        ScreenScroll.reset_region()
    ) == "\x1b[r"


@pytest.mark.parametrize(
    "method",
    [
        ScreenScroll.left,
        ScreenScroll.right,
    ],
)
@pytest.mark.parametrize(
    "value",
    [0, -1, -100, "1", 1.5, None],
)
def test_screen_scroll_invalid_n(method, value):
    with pytest.raises(
        ValueError,
        match="ScreenScroll n must be positive int",
    ):
        method(value)


@pytest.mark.parametrize(
    "top,bottom",
    [
        (0, 10),
        (10, 0),
        (-1, 10),
        (10, -1),
        ("1", 10),
        (1, "10"),
        (1.5, 10),
        (10, 1.5),
        (None, 10),
        (10, None),
    ],
)
def test_screen_scroll_invalid_region_values(top, bottom):
    with pytest.raises(
        ValueError,
        match="ScreenScroll top and bottom must be positive int",
    ):
        ScreenScroll.set_region(top, bottom)


@pytest.mark.parametrize(
    "top,bottom",
    [
        (1, 1),
        (5, 5),
        (10, 5),
    ],
)
def test_screen_scroll_invalid_region_order(top, bottom):
    with pytest.raises(
        ValueError,
        match="ScreenScroll top must be strictly smaller than bottom",
    ):
        ScreenScroll.set_region(top, bottom)


def test_screen_margins():
    assert str(
        ScreenMargins.set(1, 80)
    ) == "\x1b[1;80s"

    assert str(
        ScreenMargins.enable()
    ) == "\x1b[?69h"

    assert str(
        ScreenMargins.disable()
    ) == "\x1b[?69l"


@pytest.mark.parametrize(
    "left,right",
    [
        ("1", 80),
        (1, "80"),
        (1.5, 80),
        (1, 80.5),
        (None, 80),
        (1, None),
    ],
)
def test_screen_margins_invalid(left, right):
    with pytest.raises(
        ValueError,
        match="ScreenMargins left and right must be int",
    ):
        ScreenMargins.set(left, right)


def test_screen_write_mode():
    assert str(
        ScreenWriteMode.set_insert()
    ) == "\x1b[4h"

    assert str(
        ScreenWriteMode.set_replace()
    ) == "\x1b[4l"


def test_screen_buffer():
    assert str(
        ScreenBuffer.alternate()
    ) == "\x1b[?47h"

    assert str(
        ScreenBuffer.normal()
    ) == "\x1b[?47l"

    assert str(
        ScreenBuffer.xterm_alternate()
    ) == "\x1b[?1047h"

    assert str(
        ScreenBuffer.xterm_normal()
    ) == "\x1b[?1047l"

    assert str(
        ScreenBuffer.xterm_alternate_with_cursor()
    ) == "\x1b[?1049h"

    assert str(
        ScreenBuffer.xterm_normal_with_cursor()
    ) == "\x1b[?1049l"


def test_screen_test():
    assert str(
        ScreenTest.alignment_test()
    ) == "\x1b#8"


def test_screen_rectangle_erase():
    assert str(
        ScreenRectangle.erase(1, 2, 10, 20)
    ) == "\x1b[1;2;10;20$z"


def test_screen_rectangle_fill():
    assert str(
        ScreenRectangle.fill("X", 1, 2, 10, 20)
    ) == "\x1b[X;1;2;10;20$x"


@pytest.mark.parametrize(
    "char",
    ["", "XX", 1, None],
)
def test_screen_rectangle_fill_invalid_char(char):
    with pytest.raises(
        ValueError,
        match="ScreenRectangle char must be a single character",
    ):
        ScreenRectangle.fill(char, 1, 2, 10, 20)


@pytest.mark.parametrize(
    "method",
    [
        ScreenRectangle.erase,
        ScreenRectangle.fill,
    ],
)
@pytest.mark.parametrize(
    "values",
    [
        ("1", 2, 10, 20),
        (1, "2", 10, 20),
        (1, 2, "10", 20),
        (1, 2, 10, "20"),
        (1.5, 2, 10, 20),
        (1, 2.5, 10, 20),
        (1, 2, 10.5, 20),
        (1, 2, 10, 20.5),
        (None, 2, 10, 20),
        (1, None, 10, 20),
        (1, 2, None, 20),
        (1, 2, 10, None),
    ],
)
def test_screen_rectangle_invalid_position(method, values):
    if method == ScreenRectangle.fill:
        args = ("X", *values)
    else:
        args = values

    with pytest.raises(
        ValueError,
        match="ScreenRectangle top, left, bottom and right must be int",
    ):
        method(*args)


def test_screen_rectangle_copy():
    assert str(
        ScreenRectangle.copy(
            1,
            2,
            10,
            20,
            0,
            5,
            6,
            0,
        )
    ) == "\x1b[1;2;10;20;0;5;6;0$v"


@pytest.mark.parametrize(
    "values",
    [
        ("1", 2, 10, 20, 0, 5, 6, 0),
        (1, "2", 10, 20, 0, 5, 6, 0),
        (1, 2, "10", 20, 0, 5, 6, 0),
        (1, 2, 10, "20", 0, 5, 6, 0),
        (1, 2, 10, 20, "0", 5, 6, 0),
        (1, 2, 10, 20, 0, "5", 6, 0),
        (1, 2, 10, 20, 0, 5, "6", 0),
        (1, 2, 10, 20, 0, 5, 6, "0"),
        (1.5, 2, 10, 20, 0, 5, 6, 0),
        (1, 2.5, 10, 20, 0, 5, 6, 0),
        (1, 2, 10.5, 20, 0, 5, 6, 0),
        (1, 2, 10, 20.5, 0, 5, 6, 0),
        (1, 2, 10, 20, 0.5, 5, 6, 0),
        (1, 2, 10, 20, 0, 5.5, 6, 0),
        (1, 2, 10, 20, 0, 5, 6.5, 0),
        (1, 2, 10, 20, 0, 5, 6, 0.5),
        (None, 2, 10, 20, 0, 5, 6, 0),
        (1, None, 10, 20, 0, 5, 6, 0),
        (1, 2, None, 20, 0, 5, 6, 0),
        (1, 2, 10, None, 0, 5, 6, 0),
        (1, 2, 10, 20, None, 5, 6, 0),
        (1, 2, 10, 20, 0, None, 6, 0),
        (1, 2, 10, 20, 0, 5, None, 0),
        (1, 2, 10, 20, 0, 5, 6, None),
    ],
)
def test_screen_rectangle_copy_invalid(values):
    with pytest.raises(
        ValueError,
        match="ScreenRectangle .* must be int",
    ):
        ScreenRectangle.copy(*values)


def test_screen_mode():
    assert str(
        ScreenMode.enable_132_columns()
    ) == "\x1b[?3h"

    assert str(
        ScreenMode.disable_132_columns()
    ) == "\x1b[?3l"

    assert str(
        ScreenMode.disable_132_column_switching()
    ) == "\x1b[?40h"

    assert str(
        ScreenMode.enable_132_column_switching()
    ) == "\x1b[?40l"

    assert str(
        ScreenMode.preserve_screen_on_resize()
    ) == "\x1b[?95h"

    assert str(
        ScreenMode.clear_screen_on_resize()
    ) == "\x1b[?95l"

    assert str(
        ScreenMode.enable_reverse_video()
    ) == "\x1b[?5h"

    assert str(
        ScreenMode.disable_reverse_video()
    ) == "\x1b[?5l"

    assert str(
        ScreenMode.enable_smooth_scroll()
    ) == "\x1b[?4h"

    assert str(
        ScreenMode.disable_smooth_scroll()
    ) == "\x1b[?4l"


def test_screen_size():
    assert str(
        ScreenSize.set_columns(80)
    ) == "\x1b[80$|"

    assert str(
        ScreenSize.set_lines(24)
    ) == "\x1b[24*|"


@pytest.mark.parametrize(
    "value",
    [0, -1, -100, "1", 1.5, None],
)
def test_screen_size_invalid_columns(value):
    with pytest.raises(
        ValueError,
        match="ScreenSize columns must be a positive int",
    ):
        ScreenSize.set_columns(value)


@pytest.mark.parametrize(
    "value",
    [0, -1, -100, "1", 1.5, None],
)
def test_screen_size_invalid_lines(value):
    with pytest.raises(
        ValueError,
        match="ScreenSize lines must be a positive int",
    ):
        ScreenSize.set_lines(value)


def test_screen_control():
    assert str(
        ScreenControl.normal_index()
    ) == "\x1bD"

    assert str(
        ScreenControl.reverse_index()
    ) == "\x1bM"

    assert str(
        ScreenControl.next_line()
    ) == "\x1bE"
