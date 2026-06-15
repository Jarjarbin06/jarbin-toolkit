#############################
###                       ###
###     Jarbin-ToolKit    ###
###         error         ###
###    ----old_error.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from jarbin_toolkit_error.base_error import BaseError


class _StateError(BaseError):
    """
        _StateError exception
    """


    def __init__(
            self,
            message : str = "",

            *,
            link : tuple[str , int | None] | None = None
        ) -> None:
        """
            Create an Error.

            Parameters:
                message (str, optional): The error message.
                link (tuple[str, int | None] | None, optional): The link to where the error comes from (file and line).
        """

        super().__init__(message, link=link)
        self.error += f" State"


class ErrorState(_StateError):
    """
        ErrorState exception
    """


    def __init__(
            self,
            message : str = "state error",

            *,
            link : tuple[str , int | None] | None = None
        ) -> None:
        """
            Create an Error.

            Parameters:
                message (str, optional): The error message.
                link (tuple[str, int | None] | None, optional): The link to where the error comes from (file and line).
        """

        super().__init__(message, link=link)
        self.error += f"({type(self).__name__})"


class ErrorStateNotInitialized(_StateError):
    """
        ErrorStateNotInitialized exception
    """


    def __init__(
            self,
            message : str = "not initialized error",

            *,
            link : tuple[str , int | None] | None = None
        ) -> None:
        """
            Create an Error.

            Parameters:
                message (str, optional): The error message.
                link (tuple[str, int | None] | None, optional): The link to where the error comes from (file and line).
        """

        super().__init__(message, link=link)
        self.error += f"({type(self).__name__})"
