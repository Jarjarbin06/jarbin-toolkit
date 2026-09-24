# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Log
# File         : comment.py
#
# Author       : Jarjarbin06
# ============================================================================


from typing import final

from jarbin_toolkit_log.errors import LogTypeJError
from jarbin_toolkit_log.enums import LogType


@final
class LogComment:


    PREFIX = "    | "


    def __init__(
            self,
            message,
            type,
        ):

        if not isinstance(message, str):
            raise LogTypeJError(
                "Message must be of type str"
            )

        self.message = message

        try:
            self._type = LogType(type)
        except Exception as error:
            raise LogTypeJError(
                "Type must be of type str"
            ) from error


    def __repr__(
            self,
        ):

        lines = self.message.splitlines()

        if not lines:
            return self.PREFIX.rstrip()

        if self._type == LogType.JAR_LOG:
            return (
                f"{self.PREFIX}"
                + f"\n{self.PREFIX}".join(lines)
            )

        return self.message


__all__ = [
    'LogComment',
]
