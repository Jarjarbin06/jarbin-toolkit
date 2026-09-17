from typing import (
    Optional,
    Any,
)

from jarbin_toolkit_error.enums import FormatType
from jarbin_toolkit_error.error_link import ErrorLink


class BaseError(Exception):


    message: str
    error: str


    def __init__(
            self,
            message: str,
            *,
            error = None,
            format = FormatType.COMPACT,
            link: Optional[dict[str, Any]] = None,
            do_raise: bool = False,
        ):
        ...


    def __str__(
            self
        ) -> str:
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
