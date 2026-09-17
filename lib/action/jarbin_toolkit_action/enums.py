# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import IntEnum


class ActionStatus(IntEnum):


    INACTIVE = 0
    PENDING = 1
    RUNNING = 2
    PAUSED = 3
    SUCCESS = 4
    FAILED = 5
    CANCELLED = 6


class ActionAsync(IntEnum):


    FAILED = 0  # Not-in-use
    SUCCESS = 1


__all__ = [
    'ActionStatus',
    'ActionAsync',
]
