from enum import IntEnum


class ActionStatus(IntEnum):


    INACTIVE: int
    PENDING: int
    RUNNING: int
    PAUSED: int
    SUCCESS: int
    FAILED: int
    CANCELLED: int


class ActionAsync(IntEnum):


    FAILED: int  # Not-in-use
    SUCCESS: int


__all__: list[str]
