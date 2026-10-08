# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import (
    IntEnum,
    auto,
)
from typing import final


@final
class ConsoleAlign(IntEnum):


    LEFT = auto()
    CENTER = auto()
    RIGHT = auto()


class ConsoleOverflow(IntEnum):


    TRUNCATE = auto()
    ELLIPSIS = auto()


class ConsoleOutputMode(IntEnum):


    NORMAL = auto()
    OVERWRITE = auto()


__all__ = [
    'ConsoleAlign',
    'ConsoleOverflow',
    'ConsoleOutputMode',
]
