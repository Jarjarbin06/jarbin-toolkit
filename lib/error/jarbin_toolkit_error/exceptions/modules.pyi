from typing import (
    Optional,
    Any,
)

from .exceptions import JException
from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType


class JErrorImport(JException):
    """
        ImportError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,
            *,
            from_name = EmptyField,
            import_name = EmptyField,
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
        ...


class JErrorModuleNotFound(JException):
    """
        ModuleNotFoundError equivalent
        (JException)
    """


    def __init__(
            self,
            message: str = EmptyField,
            *,
            name = EmptyField,
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
        ...


__all__: list[str]
