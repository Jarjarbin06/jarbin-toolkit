# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Log
# File         : entry.py
#
# Author       : Jarjarbin06
# ============================================================================


from typing import final

from jarbin_toolkit_time import Time

from jarbin_toolkit_log.enums import (
    LogType,
    LogLevel,
    _log_level_max_len,
)
from jarbin_toolkit_log.errors import LogTypeJError


@final
class LogEntry:


    def __init__(
            self,
            sequence,
            level,
            message,
            format,
            type,
            scope = "",
        ):

        if isinstance(level, str):
            level = LogLevel(level)

        if not isinstance(level, LogLevel):
            raise LogTypeJError(
                "Level must be of type LogLevel or str"
            )

        if isinstance(type, str):
            type = LogType(type)

        if not isinstance(type, LogType):
            raise LogTypeJError(
                "Type must be of type LogType or str"
            )

        self._sequence = sequence
        self._creation_time = Time(format=format)
        self.level = level
        self.message = message
        self.scope = scope
        self._type = type


    def __repr__(
            self,
        ):

        filling = " " * (_log_level_max_len - len(self.level))

        if self._type == LogType.JAR_LOG:
            return (
                f"{self._sequence:05}  "
                f"{self._creation_time!s:<29}  "
                f"{self.level.name:<9}  "
                f"{self.scope:<12}  "
                f"{self.message}"
            )

        return (
            f"{self._sequence:05} "
            f"{self.level}:{filling} "
            f"{self.message}"
        )


    @property
    def sequence(
            self,
        ):
        return self._sequence


__all__ = [
    'LogEntry',
]
