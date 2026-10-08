# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import (
    IntEnum,
    auto,
)


class AnimationMode(IntEnum):


    ONCE = auto()
    LOOP = auto()
    PING_PONG = auto()


class AnimationDirection(IntEnum):


    FORWARD = auto()
    BACKWARD = auto()


class AnimationState(IntEnum):


    READY = auto()
    RUNNING = auto()
    PAUSED = auto()
    FINISHED = auto()
    STOPPED = auto()


__all__ = [
    'AnimationMode',
    'AnimationDirection',
    'AnimationState',
]
