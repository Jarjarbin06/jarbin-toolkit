import pytest
from jarbin_toolkit_console.ANSI import Line
from jarbin_toolkit_console import (init, quit)


init()



def test_clear_line(
    ) -> None:
    assert str(Line.clear_line()) == "\x1b[2K"


def test_clear_start_line(
    ) -> None:
    assert str(Line.clear_start_line()) == "\x1b[1K"


def test_clear_end_line(
    ) -> None:
    assert str(Line.clear_end_line()) == "\x1b[K"


def test_clear_screen(
    ) -> None:
    assert str(Line.clear_screen()) == "\x1b[2J"


def test_clear(
    ) -> None:
    assert str(Line.clear()) == "\x1b[2J\x1b[H"


def test_clear_previous_line(
    ) -> None:
    assert str(Line.clear_previous_line()) == "\x1b[1F\x1b[2K"


quit(delete_log=True)
