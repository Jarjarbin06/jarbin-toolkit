# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import (
    IntEnum,
    StrEnum,
    Enum,
    auto,
)
from typing import final


@final
class FormatPosition(IntEnum):


    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()


@final
class FormatOrder(IntEnum):


    BEFORE = auto()
    AFTER = auto()


@final
class FormatStrength(IntEnum):


    LIGHT = auto()
    HEAVY = auto()
    DOUBLE = auto()
    ROUND = auto()
    ASCII = auto()


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
