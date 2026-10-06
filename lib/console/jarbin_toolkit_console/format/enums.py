# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import (
    StrEnum,
    Enum,
)
from typing import final


@final
class FormatPosition(StrEnum):


    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


@final
class FormatOrder(StrEnum):


    BEFORE = "before"
    AFTER = "after"


@final
class FormatStrength(StrEnum):


    LIGHT = "light"
    HEAVY = "heavy"
    DOUBLE = "double"
    ROUND = "round"
    ASCII = "ascii"


@final
class FormatStyle(Enum):


    BOLD = ("1", "22")
    FAINT = ("2",  "22")
    ITALIC = ("3", "23")
    UNDERLINE = ("4", "24")
    SLOW_BLINK = ("5", "25")
    FAST_BLINK = ("6", "25")
    REVERSE = ("7", "27")
    HIDE = ("8", "28")
    STRIKETHROUGH = ("9", "29")
    DOUBLE_UNDERLINE = ("21", "24")


__all__ = [
    'FormatPosition',
    'FormatOrder',
    'FormatStrength',
    'FormatStyle',
]
