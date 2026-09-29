# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/SGR
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import StrEnum
from typing import final


@final
class CursorStyles(StrEnum):


    DEFAULT = "0"
    BLOCK_BLINKING = "1"
    BLOCK_STEADY = "2"
    UNDERLINE_BLINKING = "3"
    UNDERLINE_STEADY = "4"
    BAR_BLINKING = "5"
    BAR_STEADY = "6"
    INITIAL_RESOURCES = "7"


__all__ = [
    'CursorStyles',
]
