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


class _Error(BaseError):
    """
        _Error exception
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


class ErrorImport(_Error):
    """
        ErrorImport exception
    """


    def __init__(
            self,
            message : str = "import error",

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


class ErrorType(_Error):
    """
        ErrorType exception
    """


    def __init__(
            self,
            message : str = "type error",

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


class ErrorValue(_Error):
    """
        ErrorValue exception
    """


    def __init__(
            self,
            message : str = "value error",

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


class ErrorAttribute(_Error):
    """
        ErrorAttribute exception
    """


    def __init__(
            self,
            message : str = "attribute error",

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


class ErrorRuntime(_Error):
    """
        ErrorRuntime exception
    """


    def __init__(
            self,
            message : str = "runtime error",

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


class ErrorKey(_Error):
    """
        ErrorKey exception
    """


    def __init__(
            self,
            message : str = "key error",

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


class ErrorIndex(_Error):
    """
        ErrorIndex exception
    """


    def __init__(
            self,
            message : str = "index error",

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


class ErrorFileNotFound(_Error):
    """
        ErrorFileNotFound exception
    """


    def __init__(
            self,
            message : str = "file not found error",

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
