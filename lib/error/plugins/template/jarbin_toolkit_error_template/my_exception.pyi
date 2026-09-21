from typing import (
    Optional,
    Any,
)

from jarbin_toolkit_error import JException
from jarbin_toolkit_error import _EmptyFieldClass, _EmptyField
from jarbin_toolkit_error import FormatType


class JErrorMyException(JException):
    """
        My custom exception
        (JException)

        Attributes
        ----------
        message : str
            Error message

        error : str
            Error name
    """


    message: str
    error: str


    def __init__(
            self,
            message: str = _EmptyField,
            *,
            format: FormatType = FormatType.TRACEBACK,
            link: Optional[dict[str, Any]] = None,
            do_raise: bool = False,
        ):
        """
            Initialize the exception
        
            Parameters
            ----------
            message : str
                EmptyField

            format : FormatType
                Error format

            link : Optional[dict[str, Any]]
                Error link

            do_raise : bool
                Error is raised on creation

            Raises
            ----------
            TypeError
                Message, error, format type invalid

            ValueError
                Invalid link
        """
        ...


__all__: list[str]
