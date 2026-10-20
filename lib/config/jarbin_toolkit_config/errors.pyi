from typing import final

from jarbin_toolkit_error import (
    JErrorFileNotFound,
    JErrorRuntime,
    JErrorType,
    JErrorValue,
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


@final
class ConfigValueJError(JErrorValue):
    """
        Value error for Config
        (JErrorValue)
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


@final
class ConfigRuntimeJError(JErrorRuntime):
    """
        Runtime error for Config
        (JErrorRuntime)
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


@final
class ConfigFileNotFoundJError(JErrorFileNotFound):
    """
        Fila not found error for Config
        (JErrorFileNotFound)
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


__all__: list[str] = [
    'ConfigFileNotFoundJError',
    'ConfigRuntimeJError',
    'ConfigTypeJError',
    'ConfigValueJError',
]
