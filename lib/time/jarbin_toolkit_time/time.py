# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Time
# File         : time.py
#
# Author       : Jarjarbin06
# ============================================================================


from time import (
    monotonic,
    time,
)
from typing import final
from datetime import datetime

from jarbin_toolkit_time.enums import TimeFormat
from jarbin_toolkit_time.errors import (
    TimeTypeJError,
    TimeValueJError,
)


@final
class Time:


    def __init__(
            self,
            *,
            format = TimeFormat.DEFAULT,
            timestamp = None,
            year = None,
            month = None,
            day = None,
            hour = None,
            minute = None,
            second = None,
            millisecond = None,
        ):

        if not isinstance(format, TimeFormat):
            raise TimeTypeJError(
                "Format must be of type TimeFormat"
            )

        values = {
            "year": year,
            "month": month,
            "day": day,
            "hour": hour,
            "minute": minute,
            "second": second,
            "millisecond": millisecond,
        }

        for name, value in values.items():
            if value is not None and not isinstance(value, int):
                raise TimeTypeJError(
                    f"{name.capitalize()} must be of type int"
                )

        if timestamp is not None:
            if not isinstance(timestamp, float | int):
                raise TimeTypeJError(
                    "Timestamp must be of type float or int"
                )

            if any(value is not None for value in values.values()):
                raise TimeValueJError(
                    "Timestamp cannot be combined with date components"
                )

            self._datetime = datetime.fromtimestamp(timestamp)
        elif any(value is not None for value in values.values()):
            current = datetime.now()

            try:
                self._datetime = datetime(
                    year=current.year if year is None else year,
                    month=current.month if month is None else month,
                    day=current.day if day is None else day,
                    hour=current.hour if hour is None else hour,
                    minute=current.minute if minute is None else minute,
                    second=current.second if second is None else second,
                    microsecond=(
                        current.microsecond
                        if millisecond is None
                        else millisecond * 1000
                    ),
                )
            except ValueError as error:
                raise TimeValueJError(
                    str(error)
                ) from error
        else:
            self._datetime = datetime.now()

        self.format = format


    def __str__(
            self,
        ) -> str:

        return self._datetime.strftime(self.format)


    def __repr__(
            self,
        ) -> str:

        return self._datetime.strftime(self.format)


    def timestamp(
            self,
        ):

        return self._datetime.timestamp()


    @staticmethod
    def parse(
            value,
            format = TimeFormat.DEFAULT,
        ):

        if not isinstance(value, str):
            raise TimeTypeJError(
                "Value must be of type str"
            )

        if not isinstance(format, TimeFormat):
            raise TimeTypeJError(
                "Format must be of type TimeFormat"
            )

        result = Time()

        result._datetime = datetime.strptime(value, format)
        result.format = format

        return result


    @staticmethod
    def epoch(
        ):

        return time()


    @staticmethod
    def tick(
        ):

        return monotonic()
