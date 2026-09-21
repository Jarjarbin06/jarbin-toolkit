# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Action
# File         : error.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error import BaseJError


class ActionTypeError(BaseJError):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


class ActionValueError(BaseJError):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


class ActionArgumentError(BaseJError):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


class ActionExecutionError(BaseJError):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


class ActionThreadError(BaseJError):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


__all__ = [
    'ActionTypeError',
    'ActionValueError',
    'ActionArgumentError',
    'ActionExecutionError',
    'ActionThreadError',
]
