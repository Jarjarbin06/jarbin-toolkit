import pytest


from jarbin_toolkit_console.Animation import Style
from jarbin_toolkit_console import (init, quit)


init()


def test_style_initialization(
    ) -> None:
    s = Style(on="O", off=".", arrow_left="<", arrow_right=">", border_left="[", border_right="]")
    assert s.on == "O"
    assert s.off == "."
    assert s.arrow_left == "<"
    assert s.arrow_right == ">"
    assert s.border_left == "["
    assert s.border_right == "]"


def test_style_default_values(
    ) -> None:
    s = Style()
    assert s.on == "#"
    assert s.off == "-"
    assert s.arrow_left == "<"
    assert s.arrow_right == ">"
    assert s.border_left == "|"
    assert s.border_right == "|"


def test_style_string(
    ) -> None:
    s = Style()
    assert str(s) == "on=\"#\";off=\"-\";arrow_left=\"<\";arrow_right=\">\";border_left=\"|\";border_right=\"|\""


def test_style_repr(
    ) -> None:
    s = Style()
    assert repr(s) == "Style(\'#\', \'-\', \'<\', \'>\', \'|\', \'|\')"


quit(delete_log=True)
