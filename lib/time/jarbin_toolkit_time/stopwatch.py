# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Time
# File         : stopwatch.py
#
# Author       : Jarjarbin06
# ============================================================================


from time import (
    monotonic,
    time,
)

from jarbin_toolkit_time.enums import StopWatchState
from jarbin_toolkit_time.errors import TimeStateJError
from jarbin_toolkit_time.time import Time


class StopWatch:


    def __init__(
            self,
            *,
            start = False,
        ):

        self._state = StopWatchState.STOPPED
        self._start = None
        self._started_at = None
        self._stopped_at = None
        self._elapsed = 0.0
        self._saved = []

        if start:
            self.start()


    def start(
            self,
            *,
            restart = False,
        ):

        if not restart:
            if self._state == StopWatchState.RUNNING:
                raise TimeStateJError(
                    "StopWatch is already running"
                )
            elif self._state == StopWatchState.PAUSED:
                raise TimeStateJError(
                    "StopWatch is paused"
                )

        self._elapsed = 0.0
        self._saved.clear()
        self._start = monotonic()
        self._started_at = time()
        self._stopped_at = None
        self._state = StopWatchState.RUNNING


    def pause(
            self,
        ):

        if self._state != StopWatchState.RUNNING:
            raise TimeStateJError(
                "StopWatch is not running"
            )

        self._elapsed += monotonic() - self._start
        self._start = None
        self._state = StopWatchState.PAUSED


    def resume(
            self,
        ):

        if self._state != StopWatchState.PAUSED:
            raise TimeStateJError(
                "StopWatch is not paused"
            )

        self._start = monotonic()
        self._state = StopWatchState.RUNNING


    def save(
            self,
        ):

        elapsed = self.elapsed()

        self._saved.append(elapsed)

        return elapsed


    def stop(
            self,
        ):

        if self._state != StopWatchState.RUNNING:
            raise TimeStateJError(
                "StopWatch is not running"
            )

        self._elapsed += monotonic() - self._start
        self._start = None
        self._stopped_at = time()
        self._state = StopWatchState.STOPPED


    def reset(
            self,
        ):

        self._state = StopWatchState.STOPPED
        self._start = None
        self._started_at = None
        self._stopped_at = None
        self._elapsed = 0.0
        self._saved.clear()


    def elapsed(
            self,
        ):

        if self._state == StopWatchState.RUNNING:
            return self._elapsed + (
                monotonic() - self._start
            )

        return self._elapsed


    @property
    def started_at(
            self,
        ):

        if self._started_at is None:
            return None

        return Time(
            timestamp=self._started_at,
        )

    @property
    def stopped_at(
            self,
        ):

        if self._stopped_at is None:
            return None

        return Time(
            timestamp=self._stopped_at,
        )


    @property
    def state(
            self,
        ):

        return self._state


    @property
    def saved(
            self,
        ):

        return self._saved.copy()


__all__ = [
    'StopWatch',
]
