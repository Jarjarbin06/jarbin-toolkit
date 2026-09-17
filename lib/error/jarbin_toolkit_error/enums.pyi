from enum import StrEnum
from typing import (
    Self,
    Optional,
)


class FormatType(StrEnum):
    """
        Format types enum
        (StrEnum)

        Attributes
        ----------
        COMPACT : str
            Compact format

        PRETTY : str
            Pretty format

        DETAILED : str
            Detailed format

        TRACEBACK : str
            Traceback format
    """


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
    """
        Color enum for error
        (StrEnum)

        Attributes
        ----------
        RESET : str
            Color reset

        TEXT : str
            Bright white color

        MUTED : str
            Dim color

        ERROR : str
            Error foreground color

        WARNING : str
            Warning foreground color

        ERROR_BACKGROUND : str
            Error background color

        WARNING_BACKGROUND : str
            Warning background color
    """


    RESET: str
    TEXT: str
    MUTED: str
    ERROR: str
    WARNING: str
    ERROR_BACKGROUND: str
    WARNING_BACKGROUND: str


__all__: list[str]
