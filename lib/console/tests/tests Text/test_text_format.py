import pytest


from jarbin_toolkit_console.Text import Text, Format
from jarbin_toolkit_console.ANSI import ANSI
from jarbin_toolkit_console.Animation import Animation, ProgressBar, Spinner
from jarbin_toolkit_console import (init, quit)


init()


def test_format_reset():
    text = ANSI("hi")
    s = text.reset()
    assert isinstance(s, ANSI)
    assert str(s) == "\x1b[0mhi"


def test_format_bold():
    text = Text("hi")
    s = text.bold()
    assert isinstance(s, Text)
    assert str(s) == "\x1b[1mhi"


def test_format_italic():
    text = ANSI("hi")
    s = text.italic()
    assert isinstance(s, ANSI)
    assert str(s) == "\x1b[3mhi"


def test_format_underline():
    text = Text("hi")
    s = text.underline()
    assert isinstance(s, Text)
    assert str(s) == "\x1b[4mhi"


def test_format_hide():
    text = ANSI("hi")
    s = text.hide()
    assert isinstance(s, ANSI)
    assert str(s) == "\x1b[8mhi"


def test_format_strikethrough():
    text = Text("hi")
    s = text.strikethrough()
    assert isinstance(s, Text)
    assert str(s) == "\x1b[9mhi"


def test_format_error():
    text = Text("hi")
    s = text.error()
    assert isinstance(s, Text)
    assert str(s) == "\x1b[31mhi"


def test_format_error_title():
    text = ANSI("hi")
    s = text.error(title=True)
    assert isinstance(s, ANSI)
    assert str(s) == "\x1b[41mhi"


def test_format_warning():
    text = Text("hi")
    s = text.warning()
    assert isinstance(s, Text)
    assert str(s) == "\x1b[33mhi"


def test_format_warning_title():
    text = ANSI("hi")
    s = text.warning(title=True)
    assert isinstance(s, ANSI)
    assert str(s) == "\x1b[43mhi"


def test_format_valid():
    text = Text("hi")
    s = text.valid()
    assert isinstance(s, Text)
    assert str(s) == "\x1b[32mhi"


def test_format_valid_title():
    text = ANSI("hi")
    s = text.valid(title=True)
    assert isinstance(s, ANSI)
    assert str(s) == "\x1b[42mhi"


def test_format_info():
    text = Text("hi")
    s = text.info()
    assert isinstance(s, Text)
    assert str(s) == "\x1b[0mhi"


def test_format_info_title():
    text = ANSI("hi")
    s = text.info(title=True)
    assert isinstance(s, ANSI)
    assert str(s) == "\x1b[7mhi"


def test_format_apply_to_text():
    t = Text("hello world")
    result = Format.apply(t, "s1")
    assert type(result) == Text
    assert "s1hello world" == str(result)


def test_format_apply_to_str():
    result = Format.apply("hello world", "s2")
    assert type(result) == str
    assert "s2hello world" == str(result)


def test_format_apply_to_animation():
    a = Animation(["hello", "world"])
    result = Format.apply(a, "s3")
    assert type(result) == Animation
    assert ["s3hello", "s3world"] == result.animation


def test_format_apply_to_progress_bar_no_spinner():
    a = ProgressBar(3)
    result = Format.apply(a, "s4")
    assert type(result) == ProgressBar
    assert ["s4|>--|", "s4|#>-|", "s4|##>|", "s4|###|"] == result.animation.animation


def test_format_apply_to_progress_bar_with_spinner():
    s = Spinner.stick()
    a = ProgressBar(3, spinner=s)
    result = Format.apply(a, "s4")
    assert type(result) == ProgressBar
    assert ["s4|>--|", "s4|#>-|", "s4|##>|", "s4|###|"] == result.animation.animation
    assert ["s4-", "s4\\", "s4|", "s4/"] == result.spinner.animation


def test_format_apply_without_sequence_uses_reset():
    result = Format.apply("hello world")
    assert "\x1b[0mhello world" in result


def test_format_apply_invalid_target():
    result = Format.apply(123, "s3")
    assert result == 123


def test_format_tree_dict():
    data = {
        "folder": {
            "file1": None,
            "subfolder": ["file2"],
        }
    }
    tree_output = Format.tree(data, title="Project")

    # basic structure checks
    assert "Project" in tree_output
    assert "folder" in tree_output
    assert "file1" in tree_output
    assert "subfolder" in tree_output
    assert "file2" in tree_output


def test_format_tree_list():
    data = ["a", "b", "c"]
    tree_output = Format.tree(data, title="List")

    assert "List" in tree_output
    assert "a" in tree_output
    assert "b" in tree_output
    assert "c" in tree_output


def test_format_tree_string():
    tree_output = Format.tree("hello", title="String")

    assert "String" in tree_output
    assert "hello" in tree_output


def test_format_module_tree():
    output = Format.module_tree()

    assert "jarbin_toolkit_console/" in output
    assert " Text/" in output
    assert " System/" in output
    assert " Time" in output


quit(delete_log=True)
