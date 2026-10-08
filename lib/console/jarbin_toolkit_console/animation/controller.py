# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : controller.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_time import Time

from jarbin_toolkit_console.error import ConsoleJError
from jarbin_toolkit_console.animation.animation import Animation
from jarbin_toolkit_console.animation.enums import AnimationState


class AnimationController:


    def __init__(
            self,
            animation,
            *,
            clock = Time.tick,
        ):

        if not isinstance(animation, Animation):
            raise ConsoleJError("Animation must be an Animation")

        if not callable(clock):
            raise ConsoleJError("Clock must be callable")

        self._animation = animation
        self._clock = clock
        self._state = AnimationState.READY
        self._started_at = None
        self._elapsed = 0.0


    @property
    def animation(
            self,
        ):

        return self._animation


    @property
    def state(
            self,
        ):

        return self._state


    @property
    def running(
            self,
        ):

        return self._state == AnimationState.RUNNING


    @property
    def paused(
            self,
        ):

        return self._state == AnimationState.PAUSED


    @property
    def stopped(
            self,
        ):

        return self._state == AnimationState.STOPPED


    @property
    def finished(
            self,
        ):

        return self._state == AnimationState.FINISHED


    @property
    def elapsed(
            self,
        ):

        if self._started_at is None:
            return self._elapsed

        return self._elapsed + (
            self._clock() - self._started_at
        )


    def start(
            self,
        ):

        if self._animation.finished:
            self._animation.reset()

        self._state = AnimationState.RUNNING
        self._started_at = self._clock()


    def pause(
            self,
        ):

        if not self.running:
            return

        self._elapsed += self._clock() - self._started_at
        self._started_at = None
        self._state = AnimationState.PAUSED


    def resume(
            self,
        ):

        if not self.paused:
            return

        self._started_at = self._clock()
        self._state = AnimationState.RUNNING


    def stop(
            self,
        ):

        if self.running:
            self._elapsed += self._clock() - self._started_at

        self._started_at = None
        self._state = AnimationState.STOPPED


    def reset(
            self,
        ):

        self._animation.reset()
        self._state = AnimationState.READY
        self._started_at = None
        self._elapsed = 0.0

    def update(
            self,
            elapsed=None,
    ):

        if not self.running:
            return self._animation.current

        if elapsed is None:
            now = self._clock()
            elapsed = now - self._started_at
            self._started_at = now

        if elapsed < 0:
            raise ConsoleJError("Elapsed time must be non-negative")

        self._elapsed += elapsed

        frame = self._animation.update(elapsed)

        if self._animation.finished:
            self._state = AnimationState.FINISHED
            self._started_at = None

        return frame


    def tick(
            self,
        ):

        previous_frame = self._animation.frame

        self.update()

        return previous_frame != self._animation.frame


    def __enter__(
            self,
        ):

        self.start()

        return self


    def __exit__(
            self,
            exc_type,
            exc_value,
            traceback,
        ):

        self.stop()


__all__ = [
    'AnimationController',
]
