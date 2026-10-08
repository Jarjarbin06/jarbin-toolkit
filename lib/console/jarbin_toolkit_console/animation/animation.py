# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : animation.py
#
# Author       : Jarjarbin06
# ============================================================================


from numbers import Real

from jarbin_toolkit_console.animation.enums import (
    AnimationDirection,
    AnimationMode,
)
from jarbin_toolkit_console.animation.frame import Frame


class Animation:


    def __init__(
            self,
            frames,
            *,
            start_frame = 0,
            mode = AnimationMode.LOOP,
            direction = AnimationDirection.FORWARD,
            duration = 0.1,
        ):

        frames = tuple(
            frame if isinstance(frame, Frame) else Frame(frame)
            for frame in frames
        )

        if not frames:
            raise ValueError("Animation must contain at least one frame")

        if not isinstance(mode, AnimationMode):
            raise TypeError("Mode must be an AnimationMode")

        if not isinstance(direction, AnimationDirection):
            raise TypeError(
                "Direction must be an AnimationDirection"
            )

        self._validate_index(
            start_frame,
            len(frames),
        )

        self._validate_duration(duration)

        self._frames = frames
        self._length = len(frames)
        self._start_frame = start_frame
        self._current = start_frame
        self._mode = mode
        self._direction = direction
        self._duration = duration
        self._elapsed = 0.0
        self._finished = self._is_terminal()


    @staticmethod
    def _validate_index(
            index,
            length,
        ):

        if not isinstance(index, int):
            raise TypeError("Frame index must be an integer")

        if index < 0 or index >= length:
            raise ValueError("Frame index out of range")


    @staticmethod
    def _validate_duration(
            duration,
        ):

        if duration is None:
            return

        if (
                not isinstance(duration, Real)
                or isinstance(duration, bool)
        ):
            raise TypeError("Duration must be a number")

        if duration <= 0:
            raise ValueError("Duration must be greater than zero")


    def _frame_duration(
            self,
        ):

        duration = self.current.duration

        if duration is None:
            duration = self._duration

        if duration is None:
            raise RuntimeError(
                "Animation has no duration"
            )

        return duration


    def _is_terminal(
            self,
        ):

        if self._mode != AnimationMode.ONCE:
            return False

        if self._direction == AnimationDirection.FORWARD:
            return self._current == self._length - 1

        return self._current == 0


    def _advance_once(
            self,
            direction,
        ):

        next_frame = self._current + direction

        if 0 <= next_frame < self._length:
            self._current = next_frame
            return

        self._current = (
            self._length - 1
            if direction > 0
            else 0
        )

        self._finished = True


    def _advance_loop(
            self,
            direction,
        ):

        self._current = (
            self._current + direction
        ) % self._length


    def _advance_ping_pong(
            self,
        ):

        if self._direction == AnimationDirection.FORWARD:
            step = 1
        else:
            step = -1

        next_frame = self._current + step

        if 0 <= next_frame < self._length:
            self._current = next_frame
            return

        self.reverse()

        step = -step
        next_frame = self._current + step

        if 0 <= next_frame < self._length:
            self._current = next_frame


    def _advance(
            self,
            direction,
        ):

        if self._length == 1:
            if self._mode == AnimationMode.ONCE:
                self._finished = True

            return

        if self._mode == AnimationMode.ONCE:
            self._advance_once(direction)
            return

        if self._mode == AnimationMode.LOOP:
            self._advance_loop(direction)
            return

        self._advance_ping_pong()


    def __iter__(
            self,
        ):

        return iter(self._frames)


    def __len__(
            self,
        ):

        return self._length


    @property
    def frames(
            self,
        ):

        return self._frames


    @property
    def current(
            self,
        ):

        return self._frames[self._current]


    @property
    def frame(
            self,
        ):

        return self._current


    @property
    def length(
            self,
        ):

        return self._length


    @property
    def mode(
            self,
        ):

        return self._mode


    @property
    def direction(
            self,
        ):

        return self._direction


    @property
    def duration(
            self,
        ):

        return self._duration


    @property
    def progress(
            self,
        ):

        if self._length == 1:
            return 1.0

        return self._current / (self._length - 1)


    @property
    def finished(
            self,
        ):

        return self._finished


    def next(
            self,
            *,
            steps = 1,
        ):

        if not isinstance(steps, int):
            raise TypeError("Steps must be an integer")

        if steps < 0:
            raise ValueError("Steps must be non-negative")

        for _ in range(steps):
            self._advance(1)

        return self.current


    def previous(
            self,
            *,
            steps = 1,
        ):

        if not isinstance(steps, int):
            raise TypeError("Steps must be an integer")

        if steps < 0:
            raise ValueError("Steps must be non-negative")

        for _ in range(steps):
            self._advance(-1)

        return self.current


    def forward(
            self,
        ):

        self._direction = AnimationDirection.FORWARD


    def backward(
            self,
        ):

        self._direction = AnimationDirection.BACKWARD


    def reverse(
            self,
        ):

        if self._direction == AnimationDirection.FORWARD:
            self._direction = AnimationDirection.BACKWARD
        else:
            self._direction = AnimationDirection.FORWARD


    def set_mode(
            self,
            mode,
        ):

        if not isinstance(mode, AnimationMode):
            raise TypeError("Mode must be an AnimationMode")

        self._mode = mode
        self._finished = self._is_terminal()


    def set_start_frame(
            self,
            start,
        ):

        self._validate_index(
            start,
            self._length,
        )

        self._start_frame = start


    def set_duration(
            self,
            duration,
        ):

        self._validate_duration(duration)

        self._duration = duration


    def reset(
            self,
        ):

        self._current = self._start_frame
        self._elapsed = 0.0
        self._finished = self._is_terminal()


    def update(
            self,
            elapsed,
        ):

        if not isinstance(elapsed, Real) or isinstance(elapsed, bool):
            raise TypeError("Elapsed time must be a number")

        if elapsed < 0:
            raise ValueError("Elapsed time must be non-negative")

        if self._finished:
            return self.current

        self._elapsed += elapsed

        while not self._finished:
            duration = self._frame_duration()

            if self._elapsed < duration:
                break

            self._elapsed -= duration

            self._advance(
                1
                if self._direction == AnimationDirection.FORWARD
                else -1
            )

        return self.current


__all__ = [
    'Animation',
]
