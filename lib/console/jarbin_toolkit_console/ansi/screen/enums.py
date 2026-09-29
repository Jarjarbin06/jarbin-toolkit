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
class ScreenDisplayEraseMode(StrEnum):


    BELOW_CURSOR = "0"
    ABOVE_CURSOR = "1"
    ALL = "2"


@final
class ScreenLineEraseMode(StrEnum):


    CURSOR_TO_END = "0"
    START_TO_CURSOR = "1"
    ALL = "2"


__all__ = [
    'ScreenDisplayEraseMode',
    'ScreenLineEraseMode',
]
