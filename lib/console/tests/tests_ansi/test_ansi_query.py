# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI
# File         : test_ansi_query.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.ansi import Query
from jarbin_toolkit_console.ansi.osc import OSCClipboardSelection


def test_query_cursor_position(monkeypatch):
    def request(sequence, terminator):
        assert str(sequence) == "\x1b[6n"
        assert terminator == "R"
        return "\x1b[12;34R"

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.cursor_position() == (12, 34)


def test_query_cursor_position_private(monkeypatch):
    def request(sequence, terminator):
        assert str(sequence) == "\x1b[?6n"
        assert terminator == "R"
        return "\x1b[?12;34R"

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.cursor_position(
        private=True,
    ) == (12, 34)


@pytest.mark.parametrize(
    "response",
    [
        None,
        "",
        "\x1b[12;34",
        "\x1b[12R",
        "\x1b[12;34X",
        "invalid",
    ],
)
def test_query_cursor_position_invalid_response(
        monkeypatch,
        response,
    ):
    monkeypatch.setattr(
        Query,
        "_request",
        lambda sequence, terminator: response,
    )

    assert Query.cursor_position() is None


@pytest.mark.parametrize(
    "response",
    [
        None,
        "",
        "\x1b[?12;34",
        "\x1b[12;34R",
        "\x1b[?12;34X",
        "invalid",
    ],
)
def test_query_cursor_position_private_invalid_response(
        monkeypatch,
        response,
    ):
    monkeypatch.setattr(
        Query,
        "_request",
        lambda sequence, terminator: response,
    )

    assert Query.cursor_position(
        private=True,
    ) is None


@pytest.mark.parametrize(
    "secondary, expected_sequence, response, expected",
    [
        (
            False,
            "\x1b[c",
            "\x1b[?1;2;3c",
            (1, 2, 3),
        ),
        (
            False,
            "\x1b[c",
            "\x1b[?1c",
            (1,),
        ),
        (
            False,
            "\x1b[c",
            "\x1b[?1;;3c",
            (1, 3),
        ),
        (
            True,
            "\x1b[>c",
            "\x1b[>1;2;3c",
            (1, 2, 3),
        ),
        (
            True,
            "\x1b[>c",
            "\x1b[>1c",
            (1,),
        ),
        (
            True,
            "\x1b[>c",
            "\x1b[>1;;3c",
            (1, 3),
        ),
    ],
)
def test_query_device_attributes(
        monkeypatch,
        secondary,
        expected_sequence,
        response,
        expected,
    ):
    def request(sequence, terminator):
        assert str(sequence) == expected_sequence
        assert terminator == "c"
        return response

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.device_attributes(
        secondary=secondary,
    ) == expected


@pytest.mark.parametrize(
    "secondary,response",
    [
        (False, None),
        (False, ""),
        (False, "\x1b[1;2;3c"),
        (False, "\x1b[?1;2;Xc"),
        (False, "invalid"),
        (True, None),
        (True, ""),
        (True, "\x1b[?1;2;3c"),
        (True, "\x1b[>1;2;Xc"),
        (True, "invalid"),
    ],
)
def test_query_device_attributes_invalid_response(
        monkeypatch,
        secondary,
        response,
    ):
    monkeypatch.setattr(
        Query,
        "_request",
        lambda sequence, terminator: response,
    )

    assert Query.device_attributes(
        secondary=secondary,
    ) is None


@pytest.mark.parametrize(
    "status,private,expected_sequence,response,expected",
    [
        (
            5,
            False,
            "\x1b[5n",
            "\x1b[0n",
            0,
        ),
        (
            5,
            True,
            "\x1b[?5n",
            "\x1b[?0n",
            0,
        ),
        (
            0,
            False,
            "\x1b[0n",
            "\x1b[0n",
            0,
        ),
        (
            25,
            False,
            "\x1b[25n",
            "\x1b[1n",
            1,
        ),
    ],
)
def test_query_device_status(
        monkeypatch,
        status,
        private,
        expected_sequence,
        response,
        expected,
    ):
    def request(sequence, terminator):
        assert str(sequence) == expected_sequence
        assert terminator == "n"
        return response

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.device_status(
        status,
        private=private,
    ) == expected


@pytest.mark.parametrize(
    "value",
    [-1, -100, "1", 1.5, None],
)
def test_query_device_status_invalid(value):
    with pytest.raises(
        ValueError,
        match="Query status must be a non-negative integer",
    ):
        Query.device_status(value)


def test_query_device_status_cursor_position(
        monkeypatch,
    ):
    def cursor_position(private):
        assert private is True
        return (12, 34)

    monkeypatch.setattr(
        Query,
        "cursor_position",
        cursor_position,
    )

    assert Query.device_status(
        6,
        private=True,
    ) == (12, 34)


@pytest.mark.parametrize(
    "private,response",
    [
        (False, None),
        (False, ""),
        (False, "\x1b[0"),
        (False, "\x1b[?0n"),
        (False, "invalid"),
        (True, None),
        (True, ""),
        (True, "\x1b[0n"),
        (True, "\x1b[?0"),
        (True, "invalid"),
    ],
)
def test_query_device_status_invalid_response(
        monkeypatch,
        private,
        response,
    ):
    monkeypatch.setattr(
        Query,
        "_request",
        lambda sequence, terminator: response,
    )

    assert Query.device_status(
        5,
        private=private,
    ) is None


@pytest.mark.parametrize(
    "mode,private,expected_sequence,response,expected",
    [
        (
            1,
            False,
            "\x1b[1$p",
            "\x1b[1;2$y",
            (1, 2),
        ),
        (
            4,
            False,
            "\x1b[4$p",
            "\x1b[4;1$y",
            (4, 1),
        ),
        (
            1,
            True,
            "\x1b[?1$p",
            "\x1b[?1;2$y",
            (1, 2),
        ),
        (
            4,
            True,
            "\x1b[?4$p",
            "\x1b[?4;1$y",
            (4, 1),
        ),
    ],
)
def test_query_mode(
        monkeypatch,
        mode,
        private,
        expected_sequence,
        response,
        expected,
    ):
    def request(sequence, terminator):
        assert str(sequence) == expected_sequence
        assert terminator == "y"
        return response

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.mode(
        mode,
        private=private,
    ) == expected


@pytest.mark.parametrize(
    "value",
    [-1, -100, "1", 1.5, None],
)
def test_query_mode_invalid(value):
    with pytest.raises(
        ValueError,
        match="Query mode must be a non-negative integer",
    ):
        Query.mode(value)


@pytest.mark.parametrize(
    "private,response",
    [
        (False, None),
        (False, ""),
        (False, "\x1b[1;2$"),
        (False, "\x1b[?1;2$y"),
        (False, "invalid"),
        (True, None),
        (True, ""),
        (True, "\x1b[?1;2$"),
        (True, "\x1b[1;2$y"),
        (True, "invalid"),
    ],
)
def test_query_mode_invalid_response(
        monkeypatch,
        private,
        response,
    ):
    monkeypatch.setattr(
        Query,
        "_request",
        lambda sequence, terminator: response,
    )

    assert Query.mode(
        1,
        private=private,
    ) is None


def test_query_status_string(monkeypatch):
    def request(sequence, terminator):
        assert str(sequence) == "\x1bP$qm\033\\"
        assert terminator == "\033\\"
        return "\x1bP1$rhello\033\\"

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.status_string("m") == (1, "hello")


def test_query_status_string_empty_value(monkeypatch):
    def request(sequence, terminator):
        assert str(sequence) == "\x1bP$q\033\\"
        assert terminator == "\033\\"
        return "\x1bP1$r\033\\"

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.status_string("") == (1, "")


@pytest.mark.parametrize(
    "value",
    [1, None, 1.5, True],
)
def test_query_status_string_invalid(value):
    with pytest.raises(
        TypeError,
        match="Query value must be a string",
    ):
        Query.status_string(value)


@pytest.mark.parametrize(
    "response",
    [
        None,
        "",
        "\x1bP1$rhello",
        "\x1bP$rhello\033\\",
        "\x1bP1hello\033\\",
        "invalid",
    ],
)
def test_query_status_string_invalid_response(
        monkeypatch,
        response,
    ):
    monkeypatch.setattr(
        Query,
        "_request",
        lambda sequence, terminator: response,
    )

    assert Query.status_string("m") is None


def test_query_version(monkeypatch):
    def request(sequence, terminator):
        assert str(sequence) == "\x1b[>0q"
        assert terminator == "\033\\"
        return "\x1bP>|xterm-380\033\\"

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.version() == "xterm-380"


@pytest.mark.parametrize(
    "response",
    [
        None,
        "",
        "\x1bP>xterm-380\033\\",
        "\x1bP>|xterm-380",
        "\x1bP>|xterm-380\033",
        "\x1bP>|xterm-380\033X",
        "\x1bP1+r6d73676f=some-value\033\\",
        "invalid",
    ],
)
def test_query_version_invalid_response(
        monkeypatch,
        response,
    ):
    monkeypatch.setattr(
        Query,
        "_request",
        lambda sequence, terminator: response,
    )

    assert Query.version() is None


def test_query_terminal_capability(monkeypatch):
    def request(sequence, terminator):
        assert str(sequence) == "\x1bP+q6d73676f\033\\"
        assert terminator == "\033\\"
        return "\x1bP1+r6d73676f=some-value\033\\"

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.terminal_capability(
        "msgo",
    ) == (
        "msgo",
        "some-value",
    )


def test_query_terminal_capability_empty_value(monkeypatch):
    def request(sequence, terminator):
        assert str(sequence) == "\x1bP+q6d73676f\033\\"
        assert terminator == "\033\\"
        return "\x1bP1+r6d73676f=\033\\"

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.terminal_capability(
        "msgo",
    ) == (
        "msgo",
        "",
    )


@pytest.mark.parametrize(
    "value",
    [1, None, 1.5, True],
)
def test_query_terminal_capability_invalid(value):
    with pytest.raises(
        TypeError,
        match="Query capability must be a string",
    ):
        Query.terminal_capability(value)


@pytest.mark.parametrize(
    "response",
    [
        None,
        "",
        "\x1bP1+r6d73676f\033\\",
        "\x1bP1+r6d73676f\033\\extra",
        "\x1bP2+r6d73676f=some-value\033\\",
        "\x1bP1+r6d73676f\033\\",
        "\x1bP1+rinvalid=some-value\033\\",
        "\x1bP1+rZZ=some-value\033\\",
        "invalid",
    ],
)
def test_query_terminal_capability_invalid_response(
        monkeypatch,
        response,
    ):
    monkeypatch.setattr(
        Query,
        "_request",
        lambda sequence, terminator: response,
    )

    assert Query.terminal_capability(
        "msgo",
    ) is None


def test_query_match_none():
    assert Query._match(
        None,
        r".*",
    ) is None


def test_query_match():
    match = Query._match(
        "hello",
        r"(hello)",
    )

    assert match is not None
    assert match.group(1) == "hello"


def test_query_clipboard(monkeypatch):
    def request(sequence, terminator):
        assert str(sequence) == "\x1b]52;c;?\x1b\\"
        assert terminator == "\x1b\\"
        return "\x1b]52;c;SGVsbG8=\x1b\\"

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.clipboard(
        OSCClipboardSelection.CLIPBOARD,
    ) == "Hello"


@pytest.mark.parametrize(
    "selection",
    list(OSCClipboardSelection),
)
def test_query_clipboard_selections(
        monkeypatch,
        selection,
    ):
    def request(sequence, terminator):
        assert str(sequence) == (
            f"\x1b]52;{selection};?\x1b\\"
        )
        assert terminator == "\x1b\\"
        return (
            f"\x1b]52;{selection};SGVsbG8=\x1b\\"
        )

    monkeypatch.setattr(
        Query,
        "_request",
        request,
    )

    assert Query.clipboard(
        selection,
    ) == "Hello"


@pytest.mark.parametrize(
    "selection",
    [
        "c",
        0,
        None,
        1.5,
        True,
    ],
)
def test_query_clipboard_invalid_selection(selection):
    with pytest.raises(
        TypeError,
        match="Query selection must be OSCClipboardSelection",
    ):
        Query.clipboard(selection)


@pytest.mark.parametrize(
    "response",
    [
        None,
        "",
        "\x1b]52;c;SGVsbG8=",
        "\x1b]52;c;SGVsbG8=\x1bX",
        "invalid",
    ],
)
def test_query_clipboard_invalid_response(
        monkeypatch,
        response,
    ):
    monkeypatch.setattr(
        Query,
        "_request",
        lambda sequence, terminator: response,
    )

    assert Query.clipboard(
        OSCClipboardSelection.CLIPBOARD,
    ) is None


@pytest.mark.parametrize(
    "value",
    [
        "invalid-base64",
        "//79",
    ],
    )
def test_query_clipboard_invalid_value(
        monkeypatch,
        value,
    ):
    response = (
        f"\x1b]52;c;{value}\x1b\\"
    )

    monkeypatch.setattr(
        Query,
        "_request",
        lambda sequence, terminator: response,
    )

    assert Query.clipboard(
        OSCClipboardSelection.CLIPBOARD,
    ) is None
