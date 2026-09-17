from enum import IntEnum


class ActionStatus(IntEnum):
    """
        Action status enum
        (IntEnum)
    
        Attributes
        ----------
        INACTIVE : int
            Action | ActionBatch is inactive

        PENDING : int
            Action | ActionBatch is waiting to start

        RUNNING : int
            Action is actively running

        PAUSED : int
            Action is paused

        SUCCESS : int
            Action has succeeded

        FAILED : int
            Action has failed

        CANCELLED : int
            Action has been killed
    """


    INACTIVE: int
    PENDING: int
    RUNNING: int
    PAUSED: int
    SUCCESS: int
    FAILED: int
    CANCELLED: int


class ActionAsync(IntEnum):
    """
        Action async startup enum
        (IntEnum)

        Attributes
        ----------
        SUCCESS : int
            Action sync has successfully started

        FAILED : int
            Action has failed to start
    """


    SUCCESS: int
    FAILED: int


__all__: list[str]
