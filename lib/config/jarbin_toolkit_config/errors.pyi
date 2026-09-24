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
    """
        Type error for Config
        (JErrorType)
    """


    def __init__(
            self,
            message: str,
        ) -> None:
        """
            Type error

            Parameters
            ----------
            message : str
                Message to be displayed when the error is raised
        """
        ...


@final
class ConfigValueJError(JErrorValue):
    """
        Value error for Config
        (JErrorType)
    """


    def __init__(
            self,
            message: str,
        ) -> None:
        """
            Type error

            Parameters
            ----------
            message : str
                Message to be displayed when the error is raised
        """
        ...


@final
class ConfigRuntimeJError(JErrorRuntime):
    """
        Runtime error for Config
        (JErrorType)
    """


    def __init__(
            self,
            message: str,
        ) -> None:
        """
            Type error

            Parameters
            ----------
            message : str
                Message to be displayed when the error is raised
        """
        ...


@final
class ConfigFileNotFoundJError(JException):
    """
        Fila not found error for Config
        (JErrorType)
    """


    def __init__(
            self,
            message: str,
        ) -> None:
        """
            Type error

            Parameters
            ----------
            message : str
                Message to be displayed when the error is raised
        """
        ...


__all__:list[str]
