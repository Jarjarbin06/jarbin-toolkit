from typing import (
    Optional,
    Any,
)

from jarbin_toolkit_error.enums import FormatType
from jarbin_toolkit_error.error_link import ErrorLink


class BaseJError(Exception):
    """
        Base error exception
        (Exception)
    
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
            message: str,
            *,
            error: Optional[str] = None,
            format: FormatType = FormatType.COMPACT,
            link: Optional[dict[str, Any]] = None,
            do_raise: bool = False,
        ):
        """
            Initialize the error
        
            Parameters
            ----------
            message : str
                Error message

            error : Optional[str]
                Error name (if not touched, automatically set to Exception's name)

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


    def __str__(
            self
        ) -> str:
        """
            Representation of the error (following specified format)

            Returns
            ----------
            str
                Error's representation
        """
        ...


    _format: FormatType
    _link: ErrorLink


    def _str_compact(
            self
        ) -> str:
        ...


    def _str_pretty(
            self
        ) -> str:
        ...


    def _str_detailed(
            self
        ) -> str:
        ...


    def _str_traceback(
            self
        ) -> str:
        ...


__all__: list[str]
