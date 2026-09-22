from typing import (
    final,
    Optional,
)
from datetime import datetime

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
            format: TimeFormat = TimeFormat.DEFAULT,
            timestamp: Optional[float | int] = None,
            year: Optional[int] = None,
            month: Optional[int] = None,
            day: Optional[int] = None,
            hour: Optional[int] = None,
            minute: Optional[int] = None,
            second: Optional[int] = None,
            millisecond: Optional[int] = None,
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
        ...


    def __str__(
            self,
        ) -> str:
        """
            Represent the time into selected format

            Returns
            ----------
            str
                Time representation
        """
        ...


    def __repr__(
            self,
        ) -> str:
        """
            Represent the time into selected format

            Returns
            ----------
            str
                Time representation
        """
        ...


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
        ...


    @staticmethod
    def parse(
            value: str,
            format: TimeFormat = TimeFormat.DEFAULT,
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
        ...


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
        ...


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
        ...


    _datetime: datetime


__all__: list[str]
