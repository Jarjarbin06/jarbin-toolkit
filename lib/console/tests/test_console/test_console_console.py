# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : test_console_console.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest
from io import StringIO

from jarbin_toolkit_console.console import Console
from jarbin_toolkit_console.console import ConsoleAlign


def test_console_inherits_context():
    assert hasattr(Console, "alternate_screen")
    assert hasattr(Console, "normal_screen")


def test_console_inherits_cursor():
    assert hasattr(Console, "get_cursor_position")
    assert hasattr(Console, "move_cursor")
    assert hasattr(Console, "hide_cursor")
    assert hasattr(Console, "show_cursor")


def test_console_inherits_input():
    assert hasattr(Console, "input")
    assert hasattr(Console, "key")
    assert hasattr(Console, "keys")


def test_console_inherits_io():
    assert Console.stdout is not None
    assert Console.stdin is not None
    assert Console.stderr is not None


def test_console_inherits_output():
    assert hasattr(Console, "write")
    assert hasattr(Console, "print")
    assert hasattr(Console, "render")
    assert hasattr(Console, "flush")


def test_console_inherits_terminal():
    assert hasattr(Console, "size")
    assert hasattr(Console, "width")
    assert hasattr(Console, "height")
    assert hasattr(Console, "is_tty")


def test_console_print():
    stream = StringIO()

    Console.print(
        "Hello",
        width=20,
        stream=stream,
        reset=False,
    )

    assert stream.getvalue() == "Hello\n"


def test_console_print_alignment():
    stream = StringIO()

    Console.print(
        "Hello",
        width=10,
        stream=stream,
        align=ConsoleAlign.CENTER,
        reset=False,
    )

    assert stream.getvalue() == "\x1b[3GHello\n"


def test_console_write():
    stream = StringIO()

    Console.write(
        "Hello",
        stream=stream,
    )

    assert stream.getvalue() == "Hello"


def test_console_flush():
    class Stream(StringIO):


        def __init__(self):
            super().__init__()
            self.flushed = False


        def flush(self):
            self.flushed = True
            super().flush()


    stream = Stream()

    Console.flush(stream=stream)

    assert stream.flushed is True
