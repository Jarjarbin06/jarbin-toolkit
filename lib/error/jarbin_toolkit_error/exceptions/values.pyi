from collections.abc import Sized
from typing import (
    Any,
)

from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType

from .exceptions import JException

class JErrorType(JException):
    """
        TypeError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            expected: type = EmptyField,  # pyright: ignore[reportArgumentType]
            actual: object = EmptyField,
            format: FormatType = FormatType.TRACEBACK,  # pyright: ignore[reportArgumentType]
            link: dict[str, Any] | None = None,
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


class JErrorValue(JException):
    """
        ValueError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            value: Any = EmptyField,
            format: FormatType = FormatType.TRACEBACK,  # pyright: ignore[reportArgumentType]
            link: dict[str, Any] | None = None,
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


class JErrorAttribute(JException):
    """
        AttributeError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            attribute: str = EmptyField,  # pyright: ignore[reportArgumentType]
            format: FormatType = FormatType.TRACEBACK,  # pyright: ignore[reportArgumentType]
            link: dict[str, Any] | None = None,
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


class JErrorName(JException):
    """
        NameError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            name: str = EmptyField,  # pyright: ignore[reportArgumentType]
            format: FormatType = FormatType.TRACEBACK,  # pyright: ignore[reportArgumentType]
            link: dict[str, Any] | None = None,
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


class JErrorIndex(JException):
    """
        IndexError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            index: int = EmptyField,  # pyright: ignore[reportArgumentType]
            obj: Sized = EmptyField,  # pyright: ignore[reportArgumentType]
            format: FormatType = FormatType.TRACEBACK,  # pyright: ignore[reportArgumentType]
            link: dict[str, Any] | None = None,
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


class JErrorKey(JException):
    """
        KeyError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            key: Any = EmptyField,
            format: FormatType = FormatType.TRACEBACK,  # pyright: ignore[reportArgumentType]
            link: dict[str, Any] | None = None,
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


__all__: list[str] = [
    'JErrorAttribute',
    'JErrorIndex',
    'JErrorKey',
    'JErrorName',
    'JErrorType',
    'JErrorValue',
]
