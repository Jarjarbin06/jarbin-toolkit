from os import PathLike
from typing import (
    Any,
)

from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType

from .exceptions import JException

class JErrorIO(JException):
    """
        IOError equivalent
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


class JErrorFileNotFound(JException):
    """
        FileNotFoundError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            path: PathLike | str = EmptyField,  # pyright: ignore[reportArgumentType]
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

            path : PathLike | str
                Path that triggered the error

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


class JErrorFileExists(JException):
    """
        FileExistsError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            path: PathLike | str = EmptyField,  # pyright: ignore[reportArgumentType]
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

            path : PathLike | str
                Path that triggered the error

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


class JErrorPermission(JException):
    """
        PermissionError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            path: PathLike | str = EmptyField,  # pyright: ignore[reportArgumentType]
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

            path : PathLike | str
                Path that triggered the error

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


class JErrorIsADirectory(JException):
    """
        IsADirectoryError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            path: PathLike | str = EmptyField,  # pyright: ignore[reportArgumentType]
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

            path : PathLike | str
                Path that triggered the error

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


class JErrorNotADirectory(JException):
    """
        NotADirectoryError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            path: PathLike | str = EmptyField,  # pyright: ignore[reportArgumentType]
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

            path : PathLike | str
                Path that triggered the error

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


class JErrorDirectoryNotEmpty(JException):
    """
        DirectoryNotEmptyError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            path: PathLike | str = EmptyField,  # pyright: ignore[reportArgumentType]
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

            path : PathLike | str
                Path that triggered the error

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
    'JErrorDirectoryNotEmpty',
    'JErrorFileExists',
    'JErrorFileNotFound',
    'JErrorIO',
    'JErrorIsADirectory',
    'JErrorNotADirectory',
    'JErrorPermission',
]
