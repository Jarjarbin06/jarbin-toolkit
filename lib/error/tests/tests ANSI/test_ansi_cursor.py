import pytest


from jarbin_toolkit_console.ANSI import Cursor
from jarbin_toolkit_console import (init, quit)


init()



def test_cursor_up(
    ) -> None:
    assert str(Cursor.up(3)) == "\x1b[3A"


def test_cursor_down(
    ) -> None:
    assert str(Cursor.down(2)) == "\x1b[2B"


def test_cursor_left(
    ) -> None:
    assert str(Cursor.left(5)) == "\x1b[5D"


def test_cursor_right(
    ) -> None:
    assert str(Cursor.right(7)) == "\x1b[7C"


def test_cursor_top(
    ) -> None:
    assert str(Cursor.top()) == "\x1b[H"


def test_cursor_previous(
    ) -> None:
    assert str(Cursor.previous(2)) == "\x1b[2F"


def test_cursor_next(
    ) -> None:
    assert str(Cursor.next(4)) == "\x1b[4E"


def test_cursor_move(
    ) -> None:
    assert str(Cursor.move(5, 10)) == "\x1b[5;10H"


def test_cursor_move_column(
    ) -> None:
    assert str(Cursor.move_column(15)) == "\x1b[15G"


def test_cursor_save(
    ) -> None:
    assert str(Cursor.set()) == "\x1b[7"


def test_cursor_restore(
    ) -> None:
    assert str(Cursor.reset()) == "\x1b[8"


def test_cursor_hide(
    ) -> None:
    assert str(Cursor.hide()) == "\x1b[?25l"


def test_cursor_show(
    ) -> None:
    assert str(Cursor.show()) == "\x1b[?25h"


quit(delete_log=True)
