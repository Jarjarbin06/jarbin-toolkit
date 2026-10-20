from datetime import datetime
from typing import (
    final,
)

from .enums import TimeFormat

@final
class Time:
    """
        Time management

        Attributes
        ----------
        format : TimeFormat
            Time format
    """


    format: TimeFormat


    def __init__(
            self,
            *,
            format: TimeFormat | str = TimeFormat.DEFAULT,
            timestamp: float | None = None,
            year: int | None = None,
            month: int | None = None,
            day: int | None = None,
            hour: int | None = None,
            minute: int | None = None,
            second: int | None = None,
            millisecond: int | None = None,
        ) -> None:
        """
            Initialize new Time object

            Parameters
            ----------
            format : TimeFormat
                Format of the time

            Raises
            ----------
            TimeTypeJError
                Format, year, month, day, hour, minute, second, millisecond type invalid
                Timestamp type invalid

            TimeValueJError
                Timestamp combined with date arguments
                <other>
        """






    def timestamp(
            self,
        ) -> float | int:
        """
            Get the current POSIX timestamp

            Returns
            ----------
            float | int
                Time representation
        """


    @staticmethod
    def parse(
            value: str,
            format: TimeFormat | str = TimeFormat.DEFAULT,
        ) -> Time:
        """
            Get a Time object from a formated string

            Parameters
            ----------
            value : str
                Time to parse

            format : TimeFormat
                Format of the value

            Returns
            ----------
            Time
                New Time object

            Raises
            ----------
            TimeTypeJError
                Value, format type invalid
        """


    @staticmethod
    def epoch(
        ) -> float | int:
        """
            Current time in seconds since the Epoch

            Returns
            ----------
            float | int
                Time since Epoch
        """


    @staticmethod
    def tick(
        ) -> float | int:
        """
            Monotonic clock

            Returns
            ----------
            float | int
                Monotonic tick
        """


    _datetime: datetime


__all__: list[str] = [
    'Time',
]
