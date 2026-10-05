# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import StrEnum
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


__all__ = [
    'FormatPosition',
    'FormatOrder',
]
