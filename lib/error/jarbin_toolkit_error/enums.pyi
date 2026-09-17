from enum import StrEnum
from typing import (
    Self,
    Optional,
)


class FormatType(StrEnum):


    COMPACT: str
    PRETTY: str
    DETAILED: str
    TRACEBACK: str


    @classmethod
    def _missing_(
            cls,
            value: object
        ) -> Optional[Self]:
        ...


class ErrorColor(StrEnum):


    RESET: str
    TEXT: str
    MUTED: str
    ERROR: str
    WARNING: str
    ERROR_BACKGROUND: str
    WARNING_BACKGROUND: str


__all__: list[str]
