import pytest


from jarbin_toolkit_console.ANSI import ANSI
from jarbin_toolkit_console.Text import Text
from jarbin_toolkit_console import (init, quit)


init()


def test_text_string_initialization(
    ) -> None:
    t = Text("hello")
    assert str(t) == "hello"


def test_text_ansi_initialization(
    ) -> None:
    t = Text(ANSI("hello"))
    assert str(t) == "hello"


def test_ansi_list_init(
    ) -> None:
    a = Text(["Hello", " World", "!!!"])
    assert str(a) == "Hello World!!!"


def test_text_empty_initialization(
    ) -> None:
    t = Text()
    assert str(t) == ""


def test_text_add(
    ) -> None:
    t1 = Text("hello")
    t2 = Text("world")
    t3 = t1 + t2
    assert len(t3) == 10
    assert str(t3) == "helloworld"


def test_text_mul(
    ) -> None:
    t1 = Text("0")
    t2 = t1 * 10
    assert len(t2) == 10
    assert str(t2) == "0000000000"


def test_text_length(
    ) -> None:
    t = Text("hello")
    assert len(t) == 5


def test_text_repr(
    ) -> None:
    t = Text("hello")
    assert repr(t) == "Text(\'hello\')"


def test_text_url_link_no_text(
    ) -> None:
    link = Text.url_link("https://example.com")
    assert "\x1b]8;;https://example.com\x1b\\" in str(link)
    assert "\x1b]8;;\x1b\\" in str(link)


def test_text_url_link_custom_text(
    ) -> None:
    link = Text.url_link("https://example.com", text="CLICK")

    assert str(link) == '\x1b]8;;https://example.com\x1b\\CLICK\x1b]8;;\x1b\\'


def test_text_url_link_escape_sequences(
    ) -> None:
    link = Text.url_link("https://example.com/test")

    assert str(link) == '\x1b]8;;https://example.com/test\x1b\\https://example.com/test\x1b]8;;\x1b\\'


def test_text_file_link_simple(
    ) -> None:
    link = Text.file_link("/tmp/file.py")

    assert str(link) == '\x1b]8;;jetbrains://clion/navigate/reference?file=/tmp/file.py\x1b\\File "/tmp/file.py"\x1b]8;;\x1b\\'


def test_text_file_link_line_number(
    ) -> None:
    link = Text.file_link("/tmp/file.py", line=42)

    assert str(link) == '\x1b]8;;jetbrains://clion/navigate/reference?file=/tmp/file.py&line=42\x1b\\File "/tmp/file.py", line 42\x1b]8;;\x1b\\'


quit(delete_log=True)
