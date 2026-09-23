# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Log
# File         : errors.py
#
# Author       : Jarjarbin06
# ============================================================================


from typing import final

from jarbin_toolkit_error import (
    JErrorType,
    JErrorValue,
    JErrorRuntime,
    JException,
)


@final
class LogTypeJError(JErrorType):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class LogValueJError(JErrorValue):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class LogRuntimeJError(JErrorRuntime):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class LogStateJError(JException):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


__all__ = [
    'LogTypeJError',
    'LogValueJError',
    'LogRuntimeJError',
    'LogStateJError',
]
