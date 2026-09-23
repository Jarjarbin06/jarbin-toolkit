from enum import StrEnum
from typing import (
    final,
    Optional,
    Self,
)


@final
class LogType(StrEnum):
    """
        Log file type
        (StrEnum)

        Attributes
        ----------
        JAR_LOG : str
            Jar-Log format

        LOG : str
            Common log format

        name : str
            Get log file type name

        datetime_format : str
            Get log file datetime format
    """


    JAR_LOG: str
    LOG: str
    name: str
    datetime_format: str


    @classmethod
    def _missing_(
            cls,
            value: object
        ) -> Optional[Self]:
        ...


@final
class LogLevel(StrEnum):
    """
        Log level
        (StrEnum)

        Attributes
        ----------
        DEBUG : str
            Debug level

        INFO : str
            Info level

        NOTICE : str
            Notice level

        WARNING : str
            Warning level

        ERROR : str
            Error level

        CRITICAL : str
            Critical level
    """


    DEBUG: str
    INFO: str
    NOTICE: str
    WARNING: str
    ERROR: str
    CRITICAL: str


    @classmethod
    def _missing_(
            cls,
            value: object
        ) -> Optional[Self]:
        ...


_log_level_max_len: int


__all__: list[str]
