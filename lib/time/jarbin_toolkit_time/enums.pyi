from enum import (
    IntEnum,
    StrEnum,
)
from typing import final


@final
class StopWatchState(IntEnum):
    """
        StopWatch state
        (IntEnum)

        Attributes
        ----------
        STOPPED : int
            Not running

        RUNNING : int
            Running

        PAUSED : int
            Paused
    """


    STOPPED: int
    RUNNING: int
    PAUSED: int


@final
class TimeFormat(StrEnum):
    """
        Pre-made time format
        (StrEnum)

        Attributes
        ----------
        DEFAULT : str
            Default date and time format

        ISO_DATE : str
            ISO 8601 date format

        ISO_TIME : str
            ISO 8601 time format with seconds

        ISO_TIME_MILLISECONDS : str
            ISO 8601 time format with microseconds

        ISO_DATETIME : str
            ISO 8601 date and time format

        ISO_DATETIME_MILLISECONDS : str
            ISO 8601 date and time format with microseconds

        ISO_DATETIME_T : str
            ISO 8601 date and time format using 'T' as separator

        ISO_DATETIME_T_MILLISECONDS : str
            ISO 8601 date and time format using 'T' as separator,
            with microseconds

        ISO_DATETIME_TZ : str
            ISO 8601 date and time format with timezone

        ISO_DATETIME_TZ_MILLISECONDS : str
            ISO 8601 date and time format with timezone and microseconds

        DATABASE_DATE : str
            Database-compatible date format

        DATABASE_DATETIME : str
            Database-compatible date and time format

        DATABASE_DATETIME_MILLISECONDS : str
            Database-compatible date and time format with microseconds

        EUROPEAN : str
            European date and time format

        EUROPEAN_DATE : str
            European date format using slashes

        EUROPEAN_DATE_DASHED : str
            European date format using dashes

        EUROPEAN_DATE_DOTTED : str
            European date format using dots

        EUROPEAN_DATETIME : str
            European date and time format using slashes

        EUROPEAN_SHORT_DATE : str
            Short European date format

        AMERICAN_DATE : str
            American date format using slashes

        AMERICAN_DATE_DASHED : str
            American date format using dashes

        AMERICAN_DATETIME : str
            American date and time format using a 12-hour clock

        AMERICAN_SHORT_DATE : str
            Short American date format

        HUMAN_DATE : str
            Human-readable long date format

        HUMAN_DATE_SHORT : str
            Human-readable short date format

        HUMAN_DATETIME : str
            Human-readable long date and time format

        HUMAN_DATETIME_SHORT : str
            Human-readable short date and time format

        TIME_12_HOUR : str
            12-hour time format with minutes

        TIME_12_HOUR_SECONDS : str
            12-hour time format with minutes and seconds

        TIME_12_HOUR_SECONDS_COMPACT : str
            Compact 12-hour time format with seconds

        TIME_24_HOUR : str
            24-hour time format with minutes

        TIME_24_HOUR_SECONDS : str
            24-hour time format with minutes and seconds

        TIME_24_HOUR_SECONDS_COMPACT : str
            Compact 24-hour time format with seconds

        RFC_2822 : str
            RFC 2822 date and time format

        RFC_5322 : str
            RFC 5322 date and time format

        RFC_7231 : str
            HTTP date and time format defined by RFC 7231

        LOG_DATE : str
            Log-compatible date format

        LOG_DATETIME : str
            Log-compatible date and time format

        LOG_DATETIME_MILLISECONDS : str
            Log-compatible date and time format with microseconds

        LOG_DATETIME_TZ : str
            Log-compatible date and time format with timezone

        COMPACT_DATE : str
            Compact date format without separators

        COMPACT_TIME : str
            Compact time format without separators

        COMPACT_DATETIME : str
            Compact date and time format without separators

        COMPACT_DATETIME_MILLISECONDS : str
            Compact date and time format without separators,
            with microseconds

        YEAR_MONTH : str
            Year and month format

        MONTH_YEAR : str
            Month and year format

        MONTH_NAME_YEAR : str
            Full month name and year format

        SHORT_MONTH_NAME_YEAR : str
            Abbreviated month name and year format

        WEEK_OF_YEAR : str
            ISO week and year format

        WEEK_OF_YEAR_WITH_DAY : str
            ISO week, year, and weekday format
    """
    DEFAULT: str

    # ISO 8601 / international
    ISO_DATE: str
    ISO_TIME: str
    ISO_TIME_MILLISECONDS: str
    ISO_DATETIME: str
    ISO_DATETIME_MILLISECONDS: str
    ISO_DATETIME_T: str
    ISO_DATETIME_T_MILLISECONDS: str
    ISO_DATETIME_TZ: str
    ISO_DATETIME_TZ_MILLISECONDS: str

    # Common database formats
    DATABASE_DATE: str
    DATABASE_DATETIME: str
    DATABASE_DATETIME_MILLISECONDS: str

    # European formats
    EUROPEAN: str
    EUROPEAN_DATE: str
    EUROPEAN_DATE_DASHED: str
    EUROPEAN_DATE_DOTTED: str
    EUROPEAN_DATETIME: str
    EUROPEAN_SHORT_DATE: str

    # American formats
    AMERICAN_DATE: str
    AMERICAN_DATE_DASHED: str
    AMERICAN_DATETIME: str
    AMERICAN_SHORT_DATE: str

    # Human-readable formats
    HUMAN_DATE: str
    HUMAN_DATE_SHORT: str
    HUMAN_DATETIME: str
    HUMAN_DATETIME_SHORT: str

    # 12-hour clock formats
    TIME_12_HOUR: str
    TIME_12_HOUR_SECONDS: str
    TIME_12_HOUR_SECONDS_COMPACT: str

    # 24-hour clock formats
    TIME_24_HOUR: str
    TIME_24_HOUR_SECONDS: str
    TIME_24_HOUR_SECONDS_COMPACT: str

    # RFC / email / HTTP formats
    RFC_2822: str
    RFC_5322: str
    RFC_7231: str

    # Log formats
    LOG_DATE: str
    LOG_DATETIME: str
    LOG_DATETIME_MILLISECONDS: str
    LOG_DATETIME_TZ: str

    # Unix-style and compact formats
    COMPACT_DATE: str
    COMPACT_TIME: str
    COMPACT_DATETIME: str
    COMPACT_DATETIME_MILLISECONDS: str

    # Week and month formats
    YEAR_MONTH: str
    MONTH_YEAR: str
    MONTH_NAME_YEAR: str
    SHORT_MONTH_NAME_YEAR: str
    WEEK_OF_YEAR: str
    WEEK_OF_YEAR_WITH_DAY: str


__all__ = [
    'StopWatchState',
    'TimeFormat',
]
