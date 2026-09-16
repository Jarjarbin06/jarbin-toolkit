from enum import Enum


class ActionStatus(Enum):
    INACTIVE: int
    PENDING: int
    RUNNING: int
    SUCCESS: int
    FAILED: int
    CANCELLED: int


__all__: list[str]
