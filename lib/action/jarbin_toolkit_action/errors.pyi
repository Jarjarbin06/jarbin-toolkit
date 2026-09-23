from typing import final

from jarbin_toolkit_error import (
    JErrorType,
    JErrorValue,
    JException,
)


@final
class ActionTypeJError(JErrorType):
    """
        Type error for Action
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
class ActionValueJError(JErrorValue):
    """
        Value error for Action
        (JErrorValue)
    """


    def __init__(
            self,
            message: str,
        ) -> None:
        """
            Value error

            Parameters
            ----------
            message : str
                Message to be displayed when the error is raised
        """
        ...


@final
class ActionArgumentJError(JException):
    """
        Argument error for Action
        (JException)
    """


    def __init__(
            self,
            message: str,
        ) -> None:
        """
            Argument error

            Parameters
            ----------
            message : str
                Message to be displayed when the error is raised
        """
        ...


@final
class ActionExecutionJError(JException):
    """
        Execution error for Action
        (JException)
    """


    def __init__(
            self,
            message: str,
        ) -> None:
        """
            Execution error

            Parameters
            ----------
            message : str
                Message to be displayed when the error is raised
        """
        ...


@final
class ActionThreadJError(JException):
    """
        Thread error for Action
        (JException)
    """


    def __init__(
            self,
            message: str,
        ) -> None:
        """
            Therad error

            Parameters
            ----------
            message : str
                Message to be displayed when the error is raised
        """
        ...


__all__: list[str]
