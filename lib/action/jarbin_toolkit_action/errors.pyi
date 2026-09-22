from typing import final

from jarbin_toolkit_error import BaseJError


@final
class ActionTypeError(BaseJError):
    """
        Type error for Action
        (BaseJError)
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
class ActionValueError(BaseJError):
    """
        Value error for Action
        (BaseJError)
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
class ActionArgumentError(BaseJError):
    """
        Argument error for Action
        (BaseJError)
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
class ActionExecutionError(BaseJError):
    """
        Execution error for Action
        (BaseJError)
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
class ActionThreadError(BaseJError):
    """
        Thread error for Action
        (BaseJError)
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
