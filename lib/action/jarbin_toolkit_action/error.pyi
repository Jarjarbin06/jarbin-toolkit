from jarbin_toolkit_error import BaseError


class ActionTypeError(BaseError):
    """
        Type error for Action
        (BaseError)
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


class ActionThreadError(BaseError):
    """
        Thread error for Action
        (BaseError)
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
