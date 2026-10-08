# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
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
class ActionStatus(IntEnum):


    INACTIVE = auto()
    PENDING = auto()
    RUNNING = auto()
    PAUSED = auto()
    SUCCESS = auto()
    FAILED = auto()
    CANCELLED = auto()


@final
class ActionAsync(IntEnum):


    SUCCESS = auto()
    FAILED = auto()


__all__ = [
    'ActionStatus',
    'ActionAsync',
]
