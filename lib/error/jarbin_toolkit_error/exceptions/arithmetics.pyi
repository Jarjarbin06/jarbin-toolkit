from typing import (
    Any,
)

from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType

from .exceptions import JException

class JErrorArithmetic(JException):
    """
        ArithmeticError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
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


class JErrorZeroDivision(JException):
    """
        ZeroDivisionError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            dividend: float = EmptyField,  # pyright: ignore[reportArgumentType]
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

            dividend : float | int
                Number that got divided by 0

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


class JErrorOverflow(JException):
    """
        OverflowError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
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


class JErrorFloatingPoint(JException):
    """
        FloatingPointError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
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
    'JErrorArithmetic',
    'JErrorFloatingPoint',
    'JErrorOverflow',
    'JErrorZeroDivision',
]
