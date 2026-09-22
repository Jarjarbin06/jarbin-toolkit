# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : errors.py
#
# Author       : Jarjarbin06
# ============================================================================


from typing import final

from jarbin_toolkit_error import (
    JErrorType,
    JErrorValue,
    JErrorAttribute,
    JException,
)


@final
class ActionTypeJError(JErrorType):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class ActionValueJError(JErrorValue):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class ActionArgumentJError(JException):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class ActionExecutionJError(JException):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class ActionThreadJError(JException):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


__all__ = [
    'ActionTypeJError',
    'ActionValueJError',
    'ActionArgumentJError',
    'ActionExecutionJError',
    'ActionThreadJError',
]
