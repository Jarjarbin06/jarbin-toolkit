from typing import (
    Optional,
    Any,
)

from .exception import JException
from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType


class JErrorRuntime(JException):
    """
        RuntimeError equivalent
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


class JErrorNotImplemented(JException):
    """
        NotImplementedError equivalent
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


class JErrorRecursion(JException):
    """
        RecursionError equivalent
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


class JErrorSystem(JException):
    """
        SystemError equivalent
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


__all__: list[str]
