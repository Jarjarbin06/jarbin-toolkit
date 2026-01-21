import pytest
import time


from jarbin_toolkit_time import StopWatch


def test_stopwatch_default_start_false(
    ) -> None:
    sw = StopWatch()
    assert sw._start == 0.0
    assert sw == 0.0


def test_stopwatch_start_and_stop(
    ) -> None:
    sw = StopWatch()
    sw.start()
    time.sleep(0.1)
    sw.stop()

    assert 0.1 < sw < 0.11


def test_stopwatch_elapsed_auto_update(
    ) -> None:
    sw = StopWatch(start=True)
    time.sleep(0.1)
    elapsed = sw.elapsed()

    assert elapsed >= 0.1


def test_stopwatch_elapsed_manual_update(
    ) -> None:
    sw = StopWatch(start=True)
    time.sleep(0.05)
    elapsed = sw.elapsed(auto_update=False)

    assert elapsed == 0.0


def test_stopwatch_str(
    ) -> None:
    sw = StopWatch(start=True)
    time.sleep(0.05)
    elapsed = str(sw)

    assert "0.0" in elapsed


def test_stopwatch_reset(
    ) -> None:
    sw = StopWatch(start=True)
    time.sleep(0.1)
    sw.stop()
    sw.reset()

    assert sw == 0.0
    assert sw._start == 0.0


def test_stopwatch_double_start(
    ) -> None:
    sw = StopWatch(start=True)
    old_start = sw._start
    time.sleep(0.1)
    sw.start()  # Should restart

    assert sw._start != old_start
    assert sw == 0.0


def test_stopwatch_update(
    ) -> None:
    sw = StopWatch(start=True)
    time.sleep(0.1)
    sw.update()

    assert sw > 0.0


def test_stopwatch_equal(
    ) -> None:
    sw = StopWatch(start=True)
    elapsed = sw.elapsed(auto_update=False)

    assert elapsed == 0.0


def test_stopwatch_greater(
    ) -> None:
    sw = StopWatch(start=True)
    elapsed = sw.elapsed()

    assert elapsed > 0.0


def test_stopwatch_greater_or_equal(
    ) -> None:
    sw = StopWatch(start=True)
    elapsed = sw.elapsed()

    assert elapsed >= 0.0
    assert elapsed >= elapsed


def test_stopwatch_lesser(
    ) -> None:
    sw = StopWatch(start=True)
    elapsed = sw.elapsed()

    assert elapsed < 0.1


def test_stopwatch_lesser_or_equal(
    ) -> None:
    sw = StopWatch(start=True)
    elapsed = sw.elapsed()

    assert elapsed <= 0.1
    assert elapsed <= elapsed


def test_stopwatch_not_equal(
    ) -> None:
    sw = StopWatch(start=True)

    assert repr(sw) == "StopWatch(?)"
