from typing import final

from jarbin_toolkit_error import (
    JErrorType,
    JErrorValue,
    JErrorRuntime,
    JException,
)


@final
class LogTypeJError(JErrorType):
    """
        Type error for Log
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
class LogValueJError(JErrorValue):
    """
        Value error for Log
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
class LogRuntimeJError(JErrorRuntime):
    """
        Runtime error for Log
        (JErrorRuntime)
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
class LogStateJError(JException):
    """
        State error for Log
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


__all__: list[str]
