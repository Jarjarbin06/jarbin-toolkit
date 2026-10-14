# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Time
# File         : errors.py
#
# Author       : Jarjarbin06
# ============================================================================


from typing import final

from jarbin_toolkit_error import (
    JErrorType,
    JErrorValue,
    JException,
)


@final
class TimeTypeJError(JErrorType):
    """
        Type error for Time
        (JErrorType)
    """


    def __init__(
            self,
            message: str,
        ):
        """
            Value error

            Parameters
            ----------
            message : str
                Message to be displayed when the error is raised
        """
        ...


@final
class TimeValueJError(JErrorValue):
    """
        Value error for Time
        (JErrorValue)
    """


    def __init__(
            self,
            message: str,
        ):
        """
            Value error

            Parameters
            ----------
            message : str
                Message to be displayed when the error is raised
        """
        ...


@final
class TimeStateJError(JException):
    """
        State error for Time
        (JException)
    """


    def __init__(
            self,
            message: str,
        ):
        """
            Value error

            Parameters
            ----------
            message : str
                Message to be displayed when the error is raised
        """
        ...


__all__: list[str] = [
    'TimeTypeJError',
    'TimeValueJError',
    'TimeStateJError',
]
