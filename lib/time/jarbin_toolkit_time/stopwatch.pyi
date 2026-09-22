# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Time
# File         : stopwatch.py
#
# Author       : Jarjarbin06
# ============================================================================


from typing import Optional

from .enums import StopWatchState
from .time import Time


class StopWatch:
    """
        StopWatch to measure time passing
    
        Attributes
        ----------
        started_at : Optional[Time]
            Time when stopwatch started

        stopped_at : Optional[Time]
            Time when stopwatch stopped

        state : StopWatchState
            State of the stopwatch

        saved : Optional[Time]
            Saved elapsed time list
    """


    started_at: Optional[Time]
    stopped_at: Optional[Time]
    state: StopWatchState
    saved: Optional[Time]


    def __init__(
            self,
            *,
            start: bool = False,
        ) -> None:
        """
            Initialize the stopwatch

            Parameters
            ----------
            start : bool
                Start at initialization
        """
        ...


    def start(
            self,
            *,
            restart: bool = False,
        ) -> None:
        """
            Start the stopwatch

            Parameters
            ----------
            restart : bool
                Restart instead of raising when already running

            Raises
            ----------
            TimeStateJError
                Status invalid
        """
        ...


    def pause(
            self,
        ) -> None:
        """
            Pause the stopwatch

            Raises
            ----------
            TimeStateJError
                Status invalid
        """
        ...


    def resume(
            self,
        ) -> None:
        """
            Resume the stopwatch

            Raises
            ----------
            TimeStateJError
                Status invalid
        """
        ...


    def save(
            self,
        ) -> float | int:
        """
            Save the current elapsed time

            Returns
            ----------
            float | int
                Saved elapsed time
        """
        ...


    def stop(
            self,
        ) -> None:
        """
            Stop the stopwatch

            Raises
            ----------
            TimeStateJError
                Status invalid
        """
        ...


    def reset(
            self,
        ) -> None:
        """
            Reset the stopwatch
        """
        ...


    def elapsed(
            self,
        ) -> float | int:
        """
            Get the elapsed time since start (works while running too)

            Returns
            ----------
            float | int
                Elapsed time
        """
        ...


    _state: StopWatchState
    _start: Optional[float | int]
    _started_at: Optional[float | int]
    _stopped_at: Optional[float | int]
    _elapsed: float | int
    _saved: list[float | int]


__all__: list[str]
