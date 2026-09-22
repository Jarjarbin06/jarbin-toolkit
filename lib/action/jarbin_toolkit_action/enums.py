# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import IntEnum
from typing import final


@final
class ActionStatus(IntEnum):


    INACTIVE = 0
    PENDING = 1
    RUNNING = 2
    PAUSED = 3
    SUCCESS = 4
    FAILED = 5
    CANCELLED = 6


@final
class ActionAsync(IntEnum):


    SUCCESS = 1
    FAILED = 0


__all__ = [
    'ActionStatus',
    'ActionAsync',
]
