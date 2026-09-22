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


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class TimeValueJError(JErrorValue):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class TimeStateJError(JException):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


__all__ = [
    'TimeTypeJError',
    'TimeValueJError',
    'TimeStateJError',
]
