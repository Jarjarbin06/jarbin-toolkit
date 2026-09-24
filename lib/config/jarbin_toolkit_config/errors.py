# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Config
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
    #JErrorFileNotFound,
)


@final
class ConfigTypeJError(JErrorType):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class ConfigValueJError(JErrorValue):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class ConfigRuntimeJError(JErrorRuntime):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


@final
class ConfigFileNotFoundJError(JException):


    def __init__(
            self,
            message,
        ):

        super().__init__(message)


__all__ = [
    'ConfigTypeJError',
    'ConfigValueJError',
    'ConfigRuntimeJError',
    'ConfigFileNotFoundJError',
]
