# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : test_format_format.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console import Text
from jarbin_toolkit_console.format import (
    Layout,
    Color,
    Style,
    Border,
    Decoration,
    Collection,
    Composition,
    FormatStyle,
    FormatStrength,
    FormatOrder,
    FormatPosition,
)


def test_format_inheritance():
    assert issubclass(Text, Style)
    assert issubclass(Text, Color)
    assert issubclass(Text, Layout)
    assert issubclass(Text, Border)
    assert issubclass(Text, Decoration)
    assert issubclass(Text, Collection)
    assert issubclass(Text, Composition)


def test_format_flags():
    assert Text._can_format is True
    assert Text._sgr is None or Text._sgr.__name__.endswith("sgr")


def test_format_lazy_sgr():
    Text._sgr = None

    sgr = Text._get_sgr()

    assert sgr is not None
    assert Text._sgr is sgr


def test_format_lazy_cursor():
    Text._cursor = None

    cursor = Text._get_cursor()

    assert cursor is not None
    assert Text._cursor is cursor


def test_format_exports():
    assert Layout.__name__ == "Layout"
    assert Color.__name__ == "Color"
    assert Style.__name__ == "Style"
    assert Border.__name__ == "Border"
    assert Decoration.__name__ == "Decoration"
    assert Collection.__name__ == "Collection"
    assert Composition.__name__ == "Composition"
    assert FormatStyle.__name__ == "FormatStyle"
    assert FormatStrength.__name__ == "FormatStrength"
    assert FormatOrder.__name__ == "FormatOrder"
    assert FormatPosition.__name__ == "FormatPosition"
