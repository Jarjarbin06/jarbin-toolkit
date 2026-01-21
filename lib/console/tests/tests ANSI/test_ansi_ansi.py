import pytest


from jarbin_toolkit_console.ANSI import ANSI
from jarbin_toolkit_console import (init, quit)


init()


def test_ansi_empty_initialization(
    ) -> None:
    a = ANSI()
    assert str(a) == ""


def test_ansi_string_initialization(
    ) -> None:
    a = ANSI("\x1b[31m")
    assert str(a) == "\x1b[31m"


def test_ansi_list_initialization(
    ) -> None:
    a = ANSI(["\x1b[31m", "\x1b[32m", "\x1b[33m"])
    assert str(a) == "\x1b[31m\x1b[32m\x1b[33m"


def test_ansi_addition(
    ) -> None:
    a = ANSI("\x1b[31m")
    b = ANSI("\x1b[1m")
    c = a + b
    assert str(c) == "\x1b[31m\x1b[1m"


def test_ansi_add(
    ) -> None:
    t1 = ANSI("hello")
    t2 = ANSI("world")
    t3 = t1 + t2
    assert len(t3) == 10
    assert str(t3) == "helloworld"


def test_ansi_mul(
    ) -> None:
    t1 = ANSI("0")
    t2 = t1 * 10
    assert len(t2) == 10
    assert str(t2) == "0000000000"


def test_ansi_len(
    ) -> None:
    a = ANSI("\x1b[31m")
    assert len(a) == len("\x1b[31m")


def test_ansi_add_with_str(
    ) -> None:
    a = ANSI("\x1b[31m")
    c = a + "hello"
    assert str(c) == "\x1b[31mhello"


def test_ansi_invalid_add(
    ) -> None:
    a = ANSI("\x1b[31m")
    b = a + 123
    assert str(b) == str(a)


def test_ansi_repr(
    ) -> None:
    a = ANSI("\x1b[32m")
    assert repr(a) == "ANSI(\'\\x1b[32m\')"


quit(delete_log=True)
