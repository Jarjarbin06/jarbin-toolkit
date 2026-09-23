# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Log
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import StrEnum
from typing import final

from jarbin_toolkit_time import TimeFormat


@final
class LogType(StrEnum):


    JAR_LOG = f"jar-log {TimeFormat.LOG_DATETIME_MILLISECONDS}"
    LOG = f"log {TimeFormat.ISO_DATETIME_TZ_MILLISECONDS}"


    @property
    def name(self):
        return self.value.split(maxsplit=1)[0]


    @property
    def datetime_format(self):
        return self.value.split(maxsplit=1)[1]


    @classmethod
    def _missing_(
            cls,
            value
        ):
        if not isinstance(value, str):
            return None

        value = value.lower()

        matches = [
            member
            for member in cls
            if member.name.startswith(value)
        ]

        if len(matches) == 1:
            return matches[0]

        return None


@final
class LogLevel(StrEnum):


    DEBUG = "DEBUG"
    INFO = "INFO"
    NOTICE = "NOTICE"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


    @classmethod
    def _missing_(
            cls,
            value
        ):
        if not isinstance(value, str):
            return None

        value = value.upper()
        matches = [member for member in cls if member.value.startswith(value)]

        if len(matches) == 1:
            return matches[0]

        return None


_log_level_max_len = max(
    len(lvl)
    for lvl in LogLevel
)


__all__ = [
    'LogType',
    'LogLevel',
    '_log_level_max_len',
]
