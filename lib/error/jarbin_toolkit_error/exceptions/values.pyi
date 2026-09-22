from typing import (
    Optional,
    Any,
    Sized,
)

from .exceptions import JException
from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType


class JErrorType(JException):
    """
        TypeError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,
            *,
            expected: type = EmptyField,
            actual: object = EmptyField,
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

            expected : type
                Expected type

            actual : object
                Object that had the wrong type

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


class JErrorValue(JException):
    """
        ValueError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,
            *,
            value: Any = EmptyField,
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

            value : Any
                Any value

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


class JErrorAttribute(JException):
    """
        AttributeError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,
            *,
            attribute: str = EmptyField,
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

            attribute : str
                Invalid attribute

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


class JErrorName(JException):
    """
        NameError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,
            *,
            name: str = EmptyField,
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

            name : str
                Invalid name

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


class JErrorIndex(JException):
    """
        IndexError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,
            *,
            index: int = EmptyField,
            obj: Sized = EmptyField,
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

            index : int
                Requested invalid index

            obj : Sized
                len()-compatible / sized object

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


class JErrorKey(JException):
    """
        KeyError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,
            *,
            key: Any = EmptyField,
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

            key : Any
                Invalid key

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
