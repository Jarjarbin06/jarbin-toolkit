from jarbin_toolkit_error import BaseError


class ActionTypeError(BaseError):
    """
        Type error for Action
        (BaseError)

        Methods
        ----------
        ActionTypeError(message: str) -> None
            Creates a new ActionTypeError instance with the given message
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


class ActionValueError(BaseError):
    """
        Value error for Action
        (BaseError)

        Methods
        ----------
        ActionValueError(message: str) -> None
            Creates a new ActionValueError instance with the given message
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


class ActionArgumentError(BaseError):
    """
        Argument error for Action
        (BaseError)

        Methods
        ----------
        ActionArgumentError(message: str) -> None
            Creates a new ActionArgumentError instance with the given message
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


class ActionExecutionError(BaseError):
    """
        Execution error for Action
        (BaseError)

        Methods
        ----------
        ActionExecutionError(message: str) -> None
            Creates a new ActionExecutionError instance with the given message
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


__all__: list[str]
