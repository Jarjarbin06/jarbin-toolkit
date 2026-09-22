# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Time
# File         : test_time.py
#
# Author       : Jarjarbin06
# ============================================================================


from time import time
from datetime import datetime

import pytest

from jarbin_toolkit_time import (
    Time,
    TimeFormat,
    TimeTypeJError,
    TimeValueJError,
)


def test_default_values():
    before = datetime.now()
    value = Time()
    after = datetime.now()

    assert before <= value._datetime <= after
    assert value.format == TimeFormat.DEFAULT


@pytest.mark.parametrize(
    "format",
    [
        TimeFormat.DEFAULT,
        TimeFormat.ISO_DATE,
        TimeFormat.ISO_DATETIME,
        TimeFormat.ISO_DATETIME_MILLISECONDS,
        TimeFormat.EUROPEAN_DATE,
        TimeFormat.AMERICAN_DATE,
        TimeFormat.LOG_DATETIME,
        TimeFormat.LOG_DATETIME_MILLISECONDS,
        TimeFormat.COMPACT_DATETIME,
        TimeFormat.TIME_24_HOUR,
    ],
)
def test_format_enum(format):
    value = Time(
        format=format,
    )

    assert value.format == format


def test_timestamp():
    timestamp = 1758541950.0
    value = Time(
        timestamp=timestamp,
    )

    assert value.timestamp() == timestamp


@pytest.mark.parametrize(
    "timestamp",
    [
        0,
        1,
        1234567890,
        1758541950,
        1758541950.123,
    ],
)
def test_timestamp_values(timestamp):
    value = Time(
        timestamp=timestamp,
    )

    assert value.timestamp() == pytest.approx(timestamp)


def test_datetime_values():
    value = Time(
        year=2026,
        month=9,
        day=22,
        hour=13,
        minute=52,
        second=30,
        millisecond=500,
    )

    assert value._datetime == datetime(
        2026,
        9,
        22,
        13,
        52,
        30,
        500000,
    )


def test_year():
    value = Time(
        year=2020,
    )

    assert value._datetime.year == 2020


def test_month():
    value = Time(
        year=2026,
        month=5,
    )

    assert value._datetime.month == 5


def test_day():
    value = Time(
        year=2026,
        month=5,
        day=15,
    )

    assert value._datetime.day == 15


def test_hour():
    value = Time(
        year=2026,
        month=5,
        day=15,
        hour=18,
    )

    assert value._datetime.hour == 18


def test_minute():
    value = Time(
        year=2026,
        month=5,
        day=15,
        hour=18,
        minute=42,
    )

    assert value._datetime.minute == 42


def test_second():
    value = Time(
        year=2026,
        month=5,
        day=15,
        hour=18,
        minute=42,
        second=37,
    )

    assert value._datetime.second == 37


@pytest.mark.parametrize(
    "millisecond",
    [
        0,
        1,
        100,
        500,
        999,
    ],
)
def test_millisecond(millisecond):
    value = Time(
        year=2026,
        month=5,
        day=15,
        millisecond=millisecond,
    )

    assert value._datetime.microsecond == millisecond * 1000


def test_partial_datetime():
    value = Time(
        year=2026,
        month=9,
        day=22,
    )

    assert value._datetime.year == 2026
    assert value._datetime.month == 9
    assert value._datetime.day == 22


def test_timestamp_cannot_be_combined_with_datetime():
    with pytest.raises(
        TimeValueJError,
        match="Timestamp cannot be combined with date components",
    ):
        Time(
            timestamp=1758541950,
            year=2026,
        )


@pytest.mark.parametrize(
    "name",
    [
        "year",
        "month",
        "day",
        "hour",
        "minute",
        "second",
        "millisecond",
    ],
)
def test_datetime_component_type(name):
    with pytest.raises(
        TimeTypeJError,
        match=f"{name.capitalize()} must be of type int",
    ):
        Time(
            **{name: "invalid"},
        )


@pytest.mark.parametrize(
    "format",
    [
        "invalid",
        "%Y-%m-%d",
        123,
        None,
    ],
)
def test_invalid_format_type(format):
    with pytest.raises(
        TimeTypeJError,
        match="Format must be of type TimeFormat",
    ):
        Time(
            format=format,
        )


@pytest.mark.parametrize(
    "timestamp",
    [
        "1234567890",
        None,
        [],
        {},
    ],
)
def test_invalid_timestamp_type(timestamp):
    if timestamp is None:
        return

    with pytest.raises(
        TimeTypeJError,
        match="Timestamp must be of type float or int",
    ):
        Time(
            timestamp=timestamp,
        )


@pytest.mark.parametrize(
    "kwargs",
    [
        {"month": 0},
        {"month": 13},
        {"day": 0},
        {"day": 32},
        {"hour": -1},
        {"hour": 24},
        {"minute": -1},
        {"minute": 60},
        {"second": -1},
        {"second": 60},
        {"millisecond": -1},
        {"millisecond": 1000},
    ],
)
def test_invalid_datetime_values(kwargs):
    values = {
        "year": 2026,
        "month": 1,
        "day": 1,
    }

    values.update(kwargs)

    with pytest.raises(TimeValueJError):
        Time(
            **values,
        )


def test_invalid_date():
    with pytest.raises(TimeValueJError):
        Time(
            year=2026,
            month=2,
            day=29,
        )


def test_valid_leap_date():
    value = Time(
        year=2028,
        month=2,
        day=29,
        hour=0,
        minute=0,
        second=0,
        millisecond=0
    )

    assert value._datetime == datetime(
        2028,
        2,
        29,
    )


def test_string():
    value = Time(
        format=TimeFormat.LOG_DATETIME,
        year=2026,
        month=9,
        day=22,
        hour=13,
        minute=52,
        second=30,
    )

    assert str(value) == "2026-09-22 13:52:30"


def test_repr():
    value = Time(
        format=TimeFormat.LOG_DATETIME,
        year=2026,
        month=9,
        day=22,
        hour=13,
        minute=52,
        second=30,
    )

    assert repr(value) == "2026-09-22 13:52:30"


def test_string_milliseconds():
    value = Time(
        format=TimeFormat.LOG_DATETIME_MILLISECONDS,
        year=2026,
        month=9,
        day=22,
        hour=13,
        minute=52,
        second=30,
        millisecond=500,
    )

    assert str(value) == "2026-09-22 13:52:30,500000"


def test_parse():
    value = Time.parse(
        "2026-09-22 13:52:30",
        TimeFormat.LOG_DATETIME,
    )

    assert isinstance(value, Time)
    assert value._datetime == datetime(
        2026,
        9,
        22,
        13,
        52,
        30,
    )


def test_parse_milliseconds():
    value = Time.parse(
        "2026-09-22 13:52:30,500000",
        TimeFormat.LOG_DATETIME_MILLISECONDS,
    )

    assert value._datetime == datetime(
        2026,
        9,
        22,
        13,
        52,
        30,
        500000,
    )


def test_parse_invalid_value_type():
    with pytest.raises(
        TimeTypeJError,
        match="Value must be of type str",
    ):
        Time.parse(
            1234567890,
        )


def test_parse_invalid_format_type():
    with pytest.raises(
        TimeTypeJError,
        match="Format must be of type TimeFormat",
    ):
        Time.parse(
            "2026-09-22",
            "%Y-%m-%d",
        )


def test_parse_invalid_value():
    with pytest.raises(ValueError):
        Time.parse(
            "not a date",
            TimeFormat.LOG_DATETIME,
        )


def test_parse_invalid_date():
    with pytest.raises(ValueError):
        Time.parse(
            "2026-02-30",
            TimeFormat.ISO_DATE,
        )


def test_epoch():
    before = time()

    result = Time.epoch()

    after = time()

    assert before <= result <= after


def test_tick():
    first = Time.tick()
    second = Time.tick()

    assert isinstance(first, float)
    assert second >= first


def test_epoch_is_close_to_timestamp():
    assert Time.epoch() == pytest.approx(
        datetime.now().timestamp(),
        abs=1,
    )


def test_tick_is_monotonic():
    values = [
        Time.tick()
        for _ in range(10)
    ]

    assert values == sorted(values)
