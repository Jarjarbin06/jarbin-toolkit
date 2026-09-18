# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import StrEnum


class FormatType(StrEnum):


    COMPACT = "compact"
    PRETTY = "pretty"
    DETAILED = "detailed"
    TRACEBACK = "traceback"


    @classmethod
    def _missing_(
            cls,
            value
        ):
        if not isinstance(value, str):
            return None

        value = value.lower()
        matches = [member for member in cls if member.value.startswith(value)]

        if len(matches) == 1:
            return matches[0]

        return None


class ErrorColor(StrEnum):


    RESET = "\x1b[0m"

    TEXT = "\x1b[38;2;235;235;235m"
    MUTED = "\x1b[38;2;150;150;150m"

    ERROR = "\x1b[38;2;255;90;90m"
    WARNING = "\x1b[38;2;255;190;70m"

    ERROR_BACKGROUND = "\x1b[48;2;120;25;25m"
    WARNING_BACKGROUND = "\x1b[48;2;110;75;15m"


__all__ = [
    'FormatType',
    'ErrorColor',
]
