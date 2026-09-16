# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : error.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error import BaseError


class ActionTypeError(BaseError):


    def __init__(
            self,
            message,
        ):

        super().__init__(message, error=type(self).__name__)


class ActionValueError(BaseError):


    def __init__(
            self,
            message,
        ):

        super().__init__(message, error=type(self).__name__)


class ActionArgumentError(BaseError):


    def __init__(
            self,
            message,
        ):

        super().__init__(message, error=type(self).__name__)


class ActionExecutionError(BaseError):


    def __init__(
            self,
            message,
        ):

        super().__init__(message, error=type(self).__name__)


__all__ = [
    'ActionTypeError',
    'ActionValueError',
    'ActionArgumentError',
    'ActionExecutionError',
]
