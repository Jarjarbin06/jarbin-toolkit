from typing import (
    Optional,
    Any,
)

from jarbin_toolkit_error.base_error import BaseJError
from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType


class JException(BaseJError):
    """
        Exception equivalent
        (BaseJError)

        Attributes
        ----------
        funny_message : Optional[bool]
    """


    funny_message: Optional[bool] = None


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


    def _show_funny(
            self,
            _class: type,
        ):
        ...


__all__: list[str]
