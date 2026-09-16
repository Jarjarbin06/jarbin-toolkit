# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import Enum


class ActionStatus(Enum):
    INACTIVE = 0
    PENDING = 1
    RUNNING = 2
    SUCCESS = 3
    FAILED = 4
    CANCELLED = 5  # Not-in-use


__all__ = [
    'ActionStatus',
]
