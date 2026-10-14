from typing import (
    Optional,
    Any,
)

from .exceptions import JException
from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType


class JErrorMemory(JException):
    """
        MemoryError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,
            *,
            format: FormatType = FormatType.TRACEBACK,
            link: Optional[dict[str, Any]] = None,
            do_raise: bool = False,
        ):
        """
            Initialize the error

            Parameters
            ----------
            message : str
                Error message

            format : FormatType
                Error format

            link : Optional[dict[str, Any]]
                Error link

            do_raise : bool
                Error is raised on creation

            Raises
            ----------
            TypeError
                Message, format type invalid

            ValueError
                Invalid link
        """
        ...


class JErrorBuffer(JException):
    """
        BufferError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,
            *,
            format: FormatType = FormatType.TRACEBACK,
            link: Optional[dict[str, Any]] = None,
            do_raise: bool = False,
        ):
        """
            Initialize the error

            Parameters
            ----------
            message : str
                Error message

            format : FormatType
                Error format

            link : Optional[dict[str, Any]]
                Error link

            do_raise : bool
                Error is raised on creation

            Raises
            ----------
            TypeError
                Message, format type invalid

            ValueError
                Invalid link
        """
        ...


__all__: list[str] = [
    'JErrorMemory',
    'JErrorBuffer',
]
