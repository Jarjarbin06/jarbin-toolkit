# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/OSC
# File         : test_ansi_sgr.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.ansi.query import Query
from jarbin_toolkit_console.ansi.osc import (
    OSCTitle,
    OSCColor,
    OSCWindow,
    OSCHyperlink,
    OSCFileLink,
    OSCNotification,
    OSCClipboard,
    OSCShell,
    OSCClipboardSelection,
)
from jarbin_toolkit_console import ConsoleJError


ST = "\x1b\\"


# ============================================================================
# OSCTitle
# ============================================================================


def test_osc_title():
    assert str(
        OSCTitle.set_name("Terminal")
    ) == f"\x1b]0;Terminal{ST}"

    assert str(
        OSCTitle.set_icon("Icon")
    ) == f"\x1b]1;Icon{ST}"

    assert str(
        OSCTitle.set_title("My Terminal")
    ) == f"\x1b]2;My Terminal{ST}"

    assert str(
        OSCTitle.set_property("title", "My Terminal")
    ) == f"\x1b]3;title=My Terminal{ST}"


@pytest.mark.parametrize(
    "method, value",
    [
        (OSCTitle.set_name, 1),
        (OSCTitle.set_icon, 1),
        (OSCTitle.set_title, 1),
    ],
)
def test_osc_title_invalid_value(
        method,
        value,
    ):
    with pytest.raises(
        ConsoleJError,
        match="OSCTitle name must be string",
    ):
        method(value)


@pytest.mark.parametrize(
    "value",
    [
        (1, "value"),
        ("name", 1),
        (None, None),
        (1, None),
        (None, "value"),
    ],
)
def test_osc_title_invalid_property(value):
    with pytest.raises(
        ConsoleJError,
        match="OSCTitle name and value must be strings",
    ):
        OSCTitle.set_property(*value)


# ============================================================================
# OSCColor
# ============================================================================


def test_osc_color():
    assert str(
        OSCColor.foreground("FF0000")
    ) == f"\x1b]10;#FF0000{ST}"

    assert str(
        OSCColor.background("00FF00")
    ) == f"\x1b]11;#00FF00{ST}"

    assert str(
        OSCColor.cursor("0000FF")
    ) == f"\x1b]12;#0000FF{ST}"

    assert str(
        OSCColor.pointer_foreground("FFFFFF")
    ) == f"\x1b]13;#FFFFFF{ST}"

    assert str(
        OSCColor.pointer_background("000000")
    ) == f"\x1b]14;#000000{ST}"


def test_osc_color_reset():
    assert str(
        OSCColor.reset_foreground()
    ) == f"\x1b]110{ST}"

    assert str(
        OSCColor.reset_background()
    ) == f"\x1b]111{ST}"

    assert str(
        OSCColor.reset_cursor()
    ) == f"\x1b]112{ST}"

    assert str(
        OSCColor.reset_pointer_foreground()
    ) == f"\x1b]113{ST}"

    assert str(
        OSCColor.reset_pointer_background()
    ) == f"\x1b]114{ST}"


# ============================================================================
# OSCWindow
# ============================================================================


def test_osc_window(tmp_path):
    path = tmp_path / "directory"
    path.mkdir()

    assert str(
        OSCWindow.set_directory(str(path), force=True)
    ) == f"\x1b]7;file://{path.resolve()}{ST}"


def test_osc_window_invalid_type():
    with pytest.raises(
        ConsoleJError,
        match="OSCWindow path must be string",
    ):
        OSCWindow.set_directory(1)


def test_osc_window_missing_path(tmp_path):
    path = tmp_path / "missing"

    with pytest.raises(
        ConsoleJError,
        match="OSCWindow path must exist",
    ):
        OSCWindow.set_directory(str(path))


def test_osc_window_file(tmp_path):
    path = tmp_path / "file"
    path.touch()

    with pytest.raises(
        ConsoleJError,
        match="OSCWindow path must be a directory",
    ):
        OSCWindow.set_directory(str(path))


# ============================================================================
# OSCHyperlink
# ============================================================================


def test_osc_hyperlink():
    assert str(
        OSCHyperlink.open("https://example.com")
    ) == f"\x1b]8;;https://example.com{ST}"

    assert str(
        OSCHyperlink.close()
    ) == f"\x1b]8;;{ST}"


@pytest.mark.parametrize(
    "link",
    [
        1,
        None,
        1.5,
        True,
    ],
)
def test_osc_hyperlink_invalid_link(link):
    with pytest.raises(
        ConsoleJError,
        match="OSCHyperlink link must be string",
    ):
        OSCHyperlink.open(link)


# ============================================================================
# OSCFileLink
# ============================================================================


def test_osc_hyperlink():
    assert str(
        OSCFileLink.open("/home/user/file.txt")
    ) == f"\x1b]8;;file:///home/user/file.txt{ST}"

    assert str(
        OSCFileLink.close()
    ) == f"\x1b]8;;{ST}"


@pytest.mark.parametrize(
    "file",
    [
        1,
        None,
        1.5,
        True,
    ],
)
def test_osc_hyperlink_invalid_link(file):
    with pytest.raises(
        ConsoleJError,
        match="OSCFileLink file must be string",
    ):
        OSCFileLink.open(file)


# ============================================================================
# OSCNotification
# ============================================================================


def test_osc_notification():
    assert str(
        OSCNotification.notify_simple("Hello")
    ) == f"\x1b]9;Hello{ST}"

    assert str(
        OSCNotification.notify_advanced(
            "Build",
            "Build finished",
        )
    ) == f"\x1b]777;notify;Build;Build finished{ST}"


@pytest.mark.parametrize(
    "message",
    [
        1,
        None,
        1.5,
        True,
    ],
)
def test_osc_notification_invalid_simple(message):
    with pytest.raises(
        ConsoleJError,
        match="OSCNotification message must be string",
    ):
        OSCNotification.notify_simple(message)


@pytest.mark.parametrize(
    "title, message",
    [
        (1, "message"),
        ("title", 1),
        (None, "message"),
        ("title", None),
        (1, 1),
    ],
)
def test_osc_notification_invalid_advanced(
        title,
        message,
    ):
    with pytest.raises(
        ConsoleJError,
        match="OSCNotification title and message must be string",
    ):
        OSCNotification.notify_advanced(
            title,
            message,
        )


# ============================================================================
# OSCClipboard
# ============================================================================


def test_osc_clipboard_copy():
    assert str(
        OSCClipboard.copy("Hello")
    ) == f"\x1b]52;c;SGVsbG8={ST}"


@pytest.mark.parametrize(
    "selection",
    list(OSCClipboardSelection),
)
def test_osc_clipboard_copy_selections(selection):
    assert str(
        OSCClipboard.copy(
            "Hello",
            selection,
        )
    ) == f"\x1b]52;{selection};SGVsbG8={ST}"


@pytest.mark.parametrize(
    "value",
    [
        1,
        None,
        1.5,
        True,
    ],
)
def test_osc_clipboard_copy_invalid_value(value):
    with pytest.raises(
        ConsoleJError,
        match="OSCClipboard value must be string",
    ):
        OSCClipboard.copy(value)


@pytest.mark.parametrize(
    "selection",
    [
        "c",
        0,
        None,
        True,
    ],
)
def test_osc_clipboard_copy_invalid_selection(selection):
    with pytest.raises(
        ConsoleJError,
        match="OSCClipboard selection must be OSCClipboardSelection",
    ):
        OSCClipboard.copy(
            "Hello",
            selection,
        )


def test_osc_clipboard_clear():
    assert str(
        OSCClipboard.clear()
    ) == f"\x1b]52;c;{ST}"


@pytest.mark.parametrize(
    "selection",
    list(OSCClipboardSelection),
)
def test_osc_clipboard_clear_selections(selection):
    assert str(
        OSCClipboard.clear(selection)
    ) == f"\x1b]52;{selection};{ST}"


@pytest.mark.parametrize(
    "selection",
    [
        "c",
        0,
        None,
        True,
    ],
)
def test_osc_clipboard_clear_invalid_selection(selection):
    with pytest.raises(
        ConsoleJError,
        match="OSCClipboard selection must be OSCClipboardSelection",
    ):
        OSCClipboard.clear(selection)


def test_osc_clipboard_paste(monkeypatch):
    expected = "Hello"

    def clipboard(selection):
        assert selection == OSCClipboardSelection.CLIPBOARD
        return expected

    monkeypatch.setattr(
        Query,
        "clipboard",
        clipboard,
    )

    assert OSCClipboard.paste() == expected


@pytest.mark.parametrize(
    "selection",
    list(OSCClipboardSelection),
)
def test_osc_clipboard_paste_selections(
        monkeypatch,
        selection,
    ):
    def clipboard(value):
        assert value == selection
        return "Hello"

    monkeypatch.setattr(
        Query,
        "clipboard",
        clipboard,
    )

    assert OSCClipboard.paste(selection) == "Hello"
    assert OSCClipboard.paste(selection) == "Hello"


@pytest.mark.parametrize(
    "selection",
    [
        "c",
        0,
        None,
        True,
    ],
)
def test_osc_clipboard_paste_invalid_selection(selection):
    with pytest.raises(
        ConsoleJError,
        match="OSCClipboard selection must be OSCClipboardSelection",
    ):
        OSCClipboard.paste(selection)


# ============================================================================
# OSCShell
# ============================================================================


def test_osc_shell():
    assert str(
        OSCShell.prompt_start()
    ) == f"\x1b]133;A{ST}"

    assert str(
        OSCShell.prompt_end()
    ) == f"\x1b]133;B{ST}"

    assert str(
        OSCShell.command_output()
    ) == f"\x1b]133;C{ST}"

    assert str(
        OSCShell.command_end()
    ) == f"\x1b]133;D{ST}"
