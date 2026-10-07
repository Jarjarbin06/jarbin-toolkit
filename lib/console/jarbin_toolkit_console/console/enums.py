# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import StrEnum
from typing import final


@final
class ConsoleAlign(StrEnum):


    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class ConsoleOverflow(StrEnum):


    TRUNCATE = "truncate"
    ELLIPSIS = "ellipsis"


class ConsoleOutputMode(StrEnum):


    NORMAL = "normal"
    OVERWRITE = "overwrite"


__all__ = [
    'ConsoleAlign',
    'ConsoleOverflow',
    'ConsoleOutputMode',
]
