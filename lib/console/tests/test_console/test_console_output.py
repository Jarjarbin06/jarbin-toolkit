# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : test_console_output.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest
from io import StringIO

from jarbin_toolkit_console.console import (
    ConsoleAlign,
    ConsoleOutputMode,
    ConsoleOverflow,
    Output,
)


@pytest.fixture(autouse=True)
def reset_output_state():
    Output._previous_height = 0
    yield
    Output._previous_height = 0


def test_write():
    stream = StringIO()

    Output.write(
        "Hello",
        stream=stream,
    )

    assert stream.getvalue() == "Hello"


def test_write_default_stream(monkeypatch):
    values = []

    monkeypatch.setattr(
        "jarbin_toolkit_console.console.output.IO.stdout",
        StringIO(),
    )

    Output.write("Hello")

    assert Output._previous_height == 0


def test_flush():
    class Stream(StringIO):


        def __init__(self):
            super().__init__()
            self.flushed = False


        def flush(self):
            self.flushed = True
            super().flush()


    stream = Stream()

    Output.flush(stream=stream)

    assert stream.flushed is True


def test_print_basic():
    stream = StringIO()

    Output.print(
        "Hello",
        width=20,
        stream=stream,
        reset=False,
    )

    assert stream.getvalue() == "Hello\n"


def test_print_multiple_values():
    stream = StringIO()

    Output.print(
        "A",
        "B",
        "C",
        width=20,
        stream=stream,
        reset=False,
    )

    assert stream.getvalue() == "A B C\n"


def test_print_separator():
    stream = StringIO()

    Output.print(
        "A",
        "B",
        "C",
        sep=" | ",
        width=20,
        stream=stream,
        reset=False,
    )

    assert stream.getvalue() == "A | B | C\n"


def test_print_end():
    stream = StringIO()

    Output.print(
        "Hello",
        end="...",
        width=20,
        stream=stream,
        reset=False,
    )

    assert stream.getvalue() == "Hello..."


def test_print_prefix_suffix():
    stream = StringIO()

    Output.print(
        "Hello",
        width=20,
        stream=stream,
        prefix="[",
        suffix="]",
        reset=False,
    )

    assert stream.getvalue() == "[Hello]\n"


def test_print_reset():
    stream = StringIO()

    Output.print(
        "Hello",
        width=20,
        stream=stream,
    )

    assert stream.getvalue() == "Hello\x1b[0m\n"


@pytest.mark.parametrize(
    "align, expected",
    [
        (ConsoleAlign.LEFT, "\x1b[1GHello\n"),
        (ConsoleAlign.CENTER, "\x1b[8GHello\n"),
        (ConsoleAlign.RIGHT, "\x1b[16GHello\n"),
    ],
)
def test_print_alignment(align, expected):
    stream = StringIO()

    Output.print(
        "Hello",
        width=20,
        stream=stream,
        align=align,
        reset=False,
    )

    assert stream.getvalue() == expected


def test_print_truncate():
    stream = StringIO()

    Output.print(
        "Hello world",
        width=8,
        stream=stream,
        overflow=ConsoleOverflow.TRUNCATE,
        reset=False,
    )

    assert stream.getvalue() == "Hello\n"


def test_print_ellipsis():
    stream = StringIO()

    Output.print(
        "Hello world",
        width=8,
        stream=stream,
        overflow=ConsoleOverflow.ELLIPSIS,
        reset=False,
    )

    assert stream.getvalue() == "Hello…\n"


def test_print_wrap():
    stream = StringIO()

    Output.print(
        "one two three",
        width=7,
        stream=stream,
        wrap=True,
        reset=False,
    )

    assert stream.getvalue() == "one two\nthree\n"


def test_print_indent():
    stream = StringIO()

    Output.print(
        "Hello\nWorld",
        width=20,
        stream=stream,
        indent=1,
        reset=False,
    )

    assert stream.getvalue() == (
        "    Hello\n"
        "    World\n"
    )


def test_print_overflow_wrap_invalid():
    stream = StringIO()

    with pytest.raises(
        ValueError,
        match="Overflow cannot be used with wrap",
    ):
        Output.print(
            "Hello",
            width=10,
            stream=stream,
            overflow=ConsoleOverflow.TRUNCATE,
            wrap=True,
        )


def test_render():
    stream = StringIO()

    Output.render(
        "Hello",
        stream=stream,
        flush=False,
    )

    assert stream.getvalue() == "Hello"


def test_render_flush(monkeypatch):
    class Stream(StringIO):


        def __init__(self):
            super().__init__()
            self.flushed = False


        def flush(self):
            self.flushed = True
            super().flush()


    stream = Stream()

    Output.render(
        "Hello",
        stream=stream,
        flush=True,
    )

    assert stream.getvalue() == "Hello"
    assert stream.flushed is True


def test_overwrite_single_line():
    stream = StringIO()

    Output.print(
        "BEFORE",
        width=20,
        stream=stream,
        reset=False,
    )

    Output.print(
        "AFTER",
        width=20,
        stream=stream,
        reset=False,
        mode=ConsoleOutputMode.OVERWRITE,
    )

    assert stream.getvalue() == (
        "BEFORE\n"
        "\x1b[1F"
        "\x1b[1G"
        "\x1b[2K"
        "AFTER\n"
    )


def test_overwrite_multiple_lines():
    stream = StringIO()

    Output.print(
        "Line 1\nLine 2\nLine 3",
        width=20,
        stream=stream,
        reset=False,
    )

    Output.print(
        "NEW",
        width=20,
        stream=stream,
        reset=False,
        mode=ConsoleOutputMode.OVERWRITE,
    )

    assert stream.getvalue() == (
        "Line 1\n"
        "Line 2\n"
        "Line 3\n"
        "\x1b[1F"
        "\x1b[1G"
        "\x1b[2K"
        "\x1b[1F"
        "\x1b[1G"
        "\x1b[2K"
        "\x1b[1F"
        "\x1b[1G"
        "\x1b[2K"
        "NEW\n"
    )
