import pytest

from jarbin_toolkit_console.ANSI import Color, ANSI
from jarbin_toolkit_console.Text import Text
from jarbin_toolkit_console import (init, quit)


init()


def test_color_str(
    ) -> None:
    seq = Color("hey")
    assert str(seq) == "hey"


def test_color_ansi(
    ) -> None:
    seq = Color(ANSI("hey"))
    assert str(seq) == "hey"


def test_color_int_valid(
    ) -> None:
    seq = Color(31)
    assert str(seq) == "\x1b[31m"


def test_color_int_invalid(
    ) -> None:
    seq = Color(-1)
    assert str(seq) == ""


def test_color_invalid_type(
    ) -> None:
    seq = Color(Text("hey"))
    assert str(seq) == ""


def test_color_fg_valid(
    ) -> None:
    seq = Color.color_fg(10)
    assert str(seq) == "\x1b[38;5;10m"


def test_color_bg_valid(
    ) -> None:
    seq = Color.color_bg(10)
    assert str(seq) == "\x1b[48;5;10m"


def test_color_fg_invalid_range(
    ) -> None:
    assert str(Color.color_fg(-1)) == ""
    assert str(Color.color_fg(256)) == ""


def test_color_bg_invalid_range(
    ) -> None:
    assert str(Color.color_bg(-1)) == ""
    assert str(Color.color_bg(256)) == ""


def test_rgb_fg_valid(
    ) -> None:
    seq = Color.rgb_fg(10, 20, 30)
    assert str(seq) == "\x1b[38;2;10;20;30m"


def test_rgb_bg_valid(
    ) -> None:
    seq = Color.rgb_bg(10, 20, 30)
    assert str(seq) == "\x1b[48;2;10;20;30m"


def test_rgb_fg_invalid_range(
    ) -> None:
    assert str(Color.rgb_fg(-1, 10, 10)) == ""
    assert str(Color.rgb_fg(10, 256, 10)) == ""


def test_rgb_bg_invalid_range(
    ) -> None:
    assert str(Color.rgb_bg(-1, 10, 10)) == ""
    assert str(Color.rgb_bg(10, 256, 10)) == ""


def test_static_colors(
    ) -> None:
    color = Color(Color.C_RESET)
    assert isinstance(color, ANSI)
    assert str(color) == "\x1b[0m"


def test_epitech_fg(
    ) -> None:
    seq = Color.epitech_fg()
    assert str(seq) == "\x1b[38;2;0;145;211m"


def test_epitech_bg(
    ) -> None:
    seq = Color.epitech_bg()
    assert str(seq) == "\x1b[48;2;0;145;211m"


def test_epitech_dark_fg(
    ) -> None:
    seq = Color.epitech_dark_fg()
    assert str(seq) == "\x1b[38;2;31;72;94m"


def test_epitech_dark_bg(
    ) -> None:
    seq = Color.epitech_dark_bg()
    assert str(seq) == "\x1b[48;2;31;72;94m"


def test_len_color(
    ) -> None:
    assert len(Color(Color.C_FG_RED)) == len("\x1b[91m")


quit(delete_log=True)
