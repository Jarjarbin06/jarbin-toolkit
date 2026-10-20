from typing import (
    Any,
)

from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType

from .exceptions import JException

class JErrorImport(JException):
    """
        ImportError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,  # pyright: ignore[reportArgumentType]
            *,
            from_name: str = EmptyField,  # pyright: ignore[reportArgumentType]
            import_name: str = EmptyField,  # pyright: ignore[reportArgumentType]
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

            from_name : str
                Name of the module you are trying to import from

            import_name : str
                Name of the module/class you are trying to import

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


class JErrorModuleNotFound(JException):
    """
        ModuleNotFoundError equivalent
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
                Name of the module you are trying to import

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
    'JErrorImport',
    'JErrorModuleNotFound',
]
