# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Time
# File         : enums.py
#
# Author       : Jarjarbin06
# ============================================================================


from enum import (
    IntEnum,
    StrEnum,
)
from typing import final


@final
class StopWatchState(IntEnum):


    STOPPED = 0
    RUNNING = 1
    PAUSED = 2


@final
class TimeFormat(StrEnum):
    DEFAULT = "%Y-%m-%d %H:%M:%S"

    # ISO 8601 / international
    ISO_DATE = "%Y-%m-%d"
    ISO_TIME = "%H:%M:%S"
    ISO_TIME_MILLISECONDS = "%H:%M:%S.%f"
    ISO_DATETIME = "%Y-%m-%d %H:%M:%S"
    ISO_DATETIME_MILLISECONDS = "%Y-%m-%d %H:%M:%S.%f"
    ISO_DATETIME_T = "%Y-%m-%dT%H:%M:%S"
    ISO_DATETIME_T_MILLISECONDS = "%Y-%m-%dT%H:%M:%S.%f"
    ISO_DATETIME_TZ = "%Y-%m-%dT%H:%M:%S%z"
    ISO_DATETIME_TZ_MILLISECONDS = "%Y-%m-%dT%H:%M:%S.%f%z"

    # Common database formats
    DATABASE_DATE = "%Y-%m-%d"
    DATABASE_DATETIME = "%Y-%m-%d %H:%M:%S"
    DATABASE_DATETIME_MILLISECONDS = "%Y-%m-%d %H:%M:%S.%f"

    # European formats
    EUROPEAN = "%Y-%m-%d %H:%M:%S"
    EUROPEAN_DATE = "%d/%m/%Y"
    EUROPEAN_DATE_DASHED = "%d-%m-%Y"
    EUROPEAN_DATE_DOTTED = "%d.%m.%Y"
    EUROPEAN_DATETIME = "%d/%m/%Y %H:%M:%S"
    EUROPEAN_SHORT_DATE = "%d/%m/%y"

    # American formats
    AMERICAN_DATE = "%m/%d/%Y"
    AMERICAN_DATE_DASHED = "%m-%d-%Y"
    AMERICAN_DATETIME = "%m/%d/%Y %I:%M:%S %p"
    AMERICAN_SHORT_DATE = "%m/%d/%y"

    # Human-readable formats
    HUMAN_DATE = "%B %-d, %Y"
    HUMAN_DATE_SHORT = "%b %-d, %Y"
    HUMAN_DATETIME = "%B %-d, %Y at %-I:%M:%S %p"
    HUMAN_DATETIME_SHORT = "%b %-d, %Y %-I:%M %p"

    # 12-hour clock formats
    TIME_12_HOUR = "%I:%M %p"
    TIME_12_HOUR_SECONDS = "%I:%M:%S %p"
    TIME_12_HOUR_SECONDS_COMPACT = "%-I:%M:%S %p"

    # 24-hour clock formats
    TIME_24_HOUR = "%H:%M"
    TIME_24_HOUR_SECONDS = "%H:%M:%S"
    TIME_24_HOUR_SECONDS_COMPACT = "%-H:%M:%S"

    # RFC / email / HTTP formats
    RFC_2822 = "%a, %d %b %Y %H:%M:%S %z"
    RFC_5322 = "%a, %d %b %Y %H:%M:%S %z"
    RFC_7231 = "%a, %d %b %Y %H:%M:%S GMT"

    # Log formats
    LOG_DATE = "%Y-%m-%d"
    LOG_DATETIME = "%Y-%m-%d %H:%M:%S"
    LOG_DATETIME_MILLISECONDS = "%Y-%m-%d %H:%M:%S,%f"
    LOG_DATETIME_TZ = "%Y-%m-%dT%H:%M:%S%z"

    # Unix-style and compact formats
    COMPACT_DATE = "%Y%m%d"
    COMPACT_TIME = "%H%M%S"
    COMPACT_DATETIME = "%Y%m%d%H%M%S"
    COMPACT_DATETIME_MILLISECONDS = "%Y%m%d%H%M%S%f"

    # Week and month formats
    YEAR_MONTH = "%Y-%m"
    MONTH_YEAR = "%m/%Y"
    MONTH_NAME_YEAR = "%B %Y"
    SHORT_MONTH_NAME_YEAR = "%b %Y"
    WEEK_OF_YEAR = "%G-W%V"
    WEEK_OF_YEAR_WITH_DAY = "%G-W%V-%u"


__all__ = [
    'StopWatchState',
    'TimeFormat',
]
