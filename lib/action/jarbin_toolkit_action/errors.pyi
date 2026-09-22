from typing import final

from jarbin_toolkit_error import BaseJError


@final
class ActionTypeJError(BaseJError):
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
class ActionValueJError(BaseJError):
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
class ActionArgumentJError(BaseJError):
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
class ActionExecutionJError(BaseJError):
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
class ActionThreadJError(BaseJError):
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
