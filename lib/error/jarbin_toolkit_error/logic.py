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


class _LogicError(BaseError):
    """
        _LogicError exception
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
        self.error += f" Logic"


class ErrorLogicContract(_LogicError):
    """
        ErrorLogicContract exception
    """


    def __init__(
            self,
            message : str = "contract error",

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


class ErrorLogicAssertion(_LogicError):
    """
        ErrorLogicAssertion exception
    """


    def __init__(
            self,
            message : str = "assertion error",

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
