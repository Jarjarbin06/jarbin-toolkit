import pytest

from jarbin_toolkit_console import Text
from jarbin_toolkit_console.format import FormatPosition


def test_layout_pad():
    text = Text("Hello")

    assert str(text.f_layout_pad(2)) == "  Hello"
    assert str(text.f_layout_pad(2, align=FormatPosition.RIGHT)) == "Hello  "
    assert str(text.f_layout_pad(3, align=FormatPosition.CENTER)) == " Hello  "


@pytest.mark.parametrize(
    "method, expected",
    [
        (Text.f_layout_pad_left, "  Hello"),
        (Text.f_layout_pad_center, " Hello "),
        (Text.f_layout_pad_right, "Hello  "),
    ],
)
def test_layout_pad_shortcuts(method, expected):
    assert str(method(Text("Hello"), 2)) == expected


def test_layout_pad_custom_fill():
    assert str(
        Text("Hello").f_layout_pad(3, fill="-")
    ) == "---Hello"


@pytest.mark.parametrize(
    "fill",
    ["", "ab"],
)
def test_layout_pad_invalid_fill(fill):
    with pytest.raises(
        ValueError,
        match="Fill character must be a single character",
    ):
        Text("Hello").f_layout_pad(1, fill=fill)


def test_layout_pad_negative():
    with pytest.raises(ValueError, match="Amount must be non-negative"):
        Text("Hello").f_layout_pad(-1)


def test_layout_align():
    assert str(
        Text("Hello").f_layout_align(10, align=FormatPosition.LEFT)
    ) == "\x1b[1GHello"

    assert str(
        Text("Hello").f_layout_align(10, align=FormatPosition.CENTER)
    ) == "\x1b[3GHello"

    assert str(
        Text("Hello").f_layout_align(10, align=FormatPosition.RIGHT)
    ) == "\x1b[6GHello"


@pytest.mark.parametrize(
    "method, expected",
    [
        (Text.f_layout_align_left, "\x1b[1GHello"),
        (Text.f_layout_align_center, "\x1b[3GHello"),
        (Text.f_layout_align_right, "\x1b[6GHello"),
    ],
)
def test_layout_align_shortcuts(method, expected):
    assert str(method(Text("Hello"), 10)) == expected


def test_layout_align_small_width():
    assert str(
        Text("Hello").f_layout_align(3)
    ) == "\x1b[1GHel"


def test_layout_align_negative_width():
    with pytest.raises(ValueError, match="Width must be non-negative"):
        Text("Hello").f_layout_align(-1)


def test_layout_indent():
    assert str(
        Text("Hello\nWorld").f_layout_indent()
    ) == "    Hello\n    World"


def test_layout_indent_custom():
    assert str(
        Text("Hello\nWorld").f_layout_indent(
            2,
            fill="-",
            first_line="> ",
        )
    ) == "> --Hello\n--World"


def test_layout_dedent():
    assert str(
        Text("  Hello\n  World").f_layout_dedent()
    ) == "Hello\nWorld"


def test_layout_get_width():
    assert Text("Hello\nWorld!").f_layout_get_width() == 6


def test_layout_get_height():
    assert Text("Hello\nWorld").f_layout_get_height() == 2


def test_layout_wrap():
    assert str(
        Text("one two three four").f_layout_wrap(7)
    ) == "one two\nthree\nfour"


def test_layout_wrap_break_long_words():
    assert str(
        Text("abcdefgh ijk").f_layout_wrap(
            4,
            break_long_words=True,
        )
    ) == "abcd\nefgh\nijk"


def test_layout_wrap_invalid_width():
    with pytest.raises(
        ValueError,
        match="Width must be greater than zero",
    ):
        Text("Hello").f_layout_wrap(0)


def test_layout_wrap_invalid_break_long_words():
    with pytest.raises(
        TypeError,
        match="break_long_words must be a boolean",
    ):
        Text("Hello").f_layout_wrap(
            5,
            break_long_words=1,
        )


@pytest.mark.parametrize(
    "width, expected",
    [
        (20, "Hello world"),
        (8, "Hello…"),
        (6, "Hello…"),
        (1, "…"),
        (0, ""),
    ],
)
def test_layout_truncate(width, expected):
    assert str(
        Text("Hello world").f_layout_truncate(width)
    ) == expected


def test_layout_truncate_word_aware():
    assert str(
        Text("Hello world").f_layout_truncate(9)
    ) == "Hello…"


def test_layout_truncate_break_long_words():
    assert str(
        Text("Hello world").f_layout_truncate(
            9,
            break_long_words=True,
        )
    ) == "Hello wo…"


def test_layout_truncate_custom_suffix():
    assert str(
        Text("Hello world").f_layout_truncate(
            8,
            suffix="...",
        )
    ) == "Hello..."


def test_layout_truncate_invalid_suffix():
    with pytest.raises(TypeError, match="Suffix must be a string"):
        Text("Hello").f_layout_truncate(2, suffix=None)


def test_layout_truncate_invalid_break_long_words():
    with pytest.raises(
        TypeError,
        match="break_long_words must be a boolean",
    ):
        Text("Hello").f_layout_truncate(
            2,
            break_long_words=1,
        )


def test_layout_lines():
    text = Text("First\nSecond\nThird")

    assert text.f_layout_lines() == ["First", "Second", "Third"]
    assert text.f_layout_first_line() == "First"
    assert text.f_layout_last_line() == "Third"


def test_layout_prefix_suffix_lines():
    text = Text("First\nSecond")

    assert str(text.f_layout_prefix_lines("> ")) == "> First\n> Second"
    assert str(text.f_layout_suffix_lines(" !")) == "First !\nSecond !"


def test_layout_number_lines():
    assert str(
        Text("One\nTwo\nThree").f_layout_number_lines()
    ) == "1. One\n2. Two\n3. Three"


def test_layout_number_lines_custom():
    assert str(
        Text("One\nTwo").f_layout_number_lines(
            start=8,
            separator=") ",
        )
    ) == "8) One\n9) Two"


def test_layout_reverse_lines():
    # This intentionally specifies the intended API behavior.
    assert str(
        Text("One\nTwo\nThree").f_layout_reverse_lines()
    ) == "Three\nTwo\nOne"
