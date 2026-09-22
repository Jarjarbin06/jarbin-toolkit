# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Time
# File         : test_stopwatch.py
#
# Author       : Jarjarbin06
# ============================================================================


from time import (
    time,
    sleep,
)

import pytest

from jarbin_toolkit_time import (
    StopWatch,
    StopWatchState,
    Time,
    TimeStateJError,
)


def test_default_values():
    value = StopWatch()

    assert value.state == StopWatchState.STOPPED
    assert value._start is None
    assert value._started_at is None
    assert value._stopped_at is None
    assert value._elapsed == 0.0
    assert value.saved == []


def test_start_on_creation():
    value = StopWatch(
        start=True,
    )

    assert value.state == StopWatchState.RUNNING
    assert value._start is not None
    assert isinstance(value.started_at, Time)
    assert value.stopped_at is None


def test_start():
    value = StopWatch()

    value.start()

    assert value.state == StopWatchState.RUNNING
    assert value._start is not None
    assert isinstance(value.started_at, Time)
    assert value.stopped_at is None


def test_start_already_running():
    value = StopWatch(
        start=True,
    )

    with pytest.raises(
        TimeStateJError,
        match="StopWatch is already running",
    ):
        value.start()


def test_start_restart():
    value = StopWatch(
        start=True,
    )

    value.save()

    old_start = value._start

    sleep(0.001)

    value.start(
        restart=True,
    )

    assert value.state == StopWatchState.RUNNING
    assert value._start is not None
    assert value._start >= old_start
    assert value.elapsed() < 0.1
    assert value.saved == []


def test_start_paused():
    value = StopWatch(
        start=True,
    )

    value.pause()

    with pytest.raises(
        TimeStateJError,
        match="StopWatch is paused",
    ):
        value.start()


def test_start_paused_restart():
    value = StopWatch(
        start=True,
    )

    sleep(0.001)
    value.pause()

    value.save()

    value.start(
        restart=True,
    )

    assert value.state == StopWatchState.RUNNING
    assert value._start is not None
    assert value.saved == []
    assert value.elapsed() < 0.1


def test_pause():
    value = StopWatch(
        start=True,
    )

    sleep(0.005)

    value.pause()

    assert value.state == StopWatchState.PAUSED
    assert value._start is None
    assert value.elapsed() > 0


def test_pause_not_running():
    value = StopWatch()

    with pytest.raises(
        TimeStateJError,
        match="StopWatch is not running",
    ):
        value.pause()


def test_pause_already_paused():
    value = StopWatch(
        start=True,
    )

    value.pause()

    with pytest.raises(
        TimeStateJError,
        match="StopWatch is not running",
    ):
        value.pause()


def test_resume():
    value = StopWatch(
        start=True,
    )

    sleep(0.005)
    value.pause()

    elapsed = value.elapsed()

    sleep(0.005)

    value.resume()

    assert value.state == StopWatchState.RUNNING
    assert value._start is not None
    assert value.elapsed() >= elapsed


def test_resume_not_paused():
    value = StopWatch()

    with pytest.raises(
        TimeStateJError,
        match="StopWatch is not paused",
    ):
        value.resume()


def test_resume_running():
    value = StopWatch(
        start=True,
    )

    with pytest.raises(
        TimeStateJError,
        match="StopWatch is not paused",
    ):
        value.resume()


def test_stop():
    value = StopWatch(
        start=True,
    )

    sleep(0.005)

    value.stop()

    assert value.state == StopWatchState.STOPPED
    assert value._start is None
    assert value._elapsed > 0
    assert isinstance(value.stopped_at, Time)


def test_stop_not_running():
    value = StopWatch()

    with pytest.raises(
        TimeStateJError,
        match="StopWatch is not running",
    ):
        value.stop()


def test_stop_paused():
    value = StopWatch(
        start=True,
    )

    value.pause()

    with pytest.raises(
        TimeStateJError,
        match="StopWatch is not running",
    ):
        value.stop()


def test_elapsed_running():
    value = StopWatch(
        start=True,
    )

    first = value.elapsed()

    sleep(0.005)

    second = value.elapsed()

    assert second > first


def test_elapsed_stopped():
    value = StopWatch(
        start=True,
    )

    sleep(0.005)
    value.stop()

    elapsed = value.elapsed()

    sleep(0.005)

    assert value.elapsed() == elapsed


def test_elapsed_paused():
    value = StopWatch(
        start=True,
    )

    sleep(0.005)
    value.pause()

    elapsed = value.elapsed()

    sleep(0.005)

    assert value.elapsed() == elapsed


def test_save():
    value = StopWatch(
        start=True,
    )

    sleep(0.005)

    result = value.save()

    assert result == value.saved[0]
    assert result <= value.elapsed()
    assert len(value.saved) == 1


def test_multiple_save():
    value = StopWatch(
        start=True,
    )

    sleep(0.005)
    first = value.save()

    sleep(0.005)
    second = value.save()

    assert len(value.saved) == 2
    assert value.saved == [
        first,
        second,
    ]
    assert second > first


def test_saved_is_copy():
    value = StopWatch(
        start=True,
    )

    value.save()

    saved = value.saved
    saved.clear()

    assert len(value.saved) == 1


def test_started_at():
    before = time()

    value = StopWatch(
        start=True,
    )

    after = time()

    assert isinstance(value.started_at, Time)
    assert before <= value.started_at.timestamp() <= after


def test_started_at_after_restart():
    value = StopWatch(
        start=True,
    )

    first = value.started_at.timestamp()

    sleep(0.005)

    value.start(
        restart=True,
    )

    second = value.started_at.timestamp()

    assert second > first


def test_stopped_at():
    value = StopWatch(
        start=True,
    )

    before = time()

    sleep(0.005)
    value.stop()

    after = time()

    assert isinstance(value.stopped_at, Time)
    assert before <= value.stopped_at.timestamp() <= after


def test_stopped_at_running():
    value = StopWatch(
        start=True,
    )

    assert value.stopped_at is None


def test_reset():
    value = StopWatch(
        start=True,
    )

    sleep(0.005)
    value.save()
    value.stop()

    value.reset()

    assert value.state == StopWatchState.STOPPED
    assert value._start is None
    assert value._started_at is None
    assert value._stopped_at is None
    assert value._elapsed == 0.0
    assert value.saved == []


def test_reset_running():
    value = StopWatch(
        start=True,
    )

    sleep(0.005)
    value.reset()

    assert value.state == StopWatchState.STOPPED
    assert value.elapsed() == 0.0
    assert value.started_at is None
    assert value.stopped_at is None


def test_reset_can_start_again():
    value = StopWatch(
        start=True,
    )

    sleep(0.005)
    value.reset()
    value.start()

    assert value.state == StopWatchState.RUNNING
    assert value.started_at is not None
    assert value.elapsed() >= 0


def test_pause_resume_preserves_elapsed():
    value = StopWatch(
        start=True,
    )

    sleep(0.005)
    value.pause()

    first = value.elapsed()

    sleep(0.01)

    value.resume()
    sleep(0.005)
    value.stop()

    second = value.elapsed()

    assert second > first
    assert second < 0.1
