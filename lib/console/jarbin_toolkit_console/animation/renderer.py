# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : renderer.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.animation.frame import Frame


class AnimationRenderer:


    def __init__(
            self,
            render,
            *,
            clear = None,
            start = None,
            stop = None,
        ):

        if not callable(render):
            raise TypeError("Render must be callable")

        if clear is not None and not callable(clear):
            raise TypeError("Clear must be callable")

        if start is not None and not callable(start):
            raise TypeError("Start must be callable")

        if stop is not None and not callable(stop):
            raise TypeError("Stop must be callable")

        self._render = render
        self._clear = clear
        self._start = start
        self._stop = stop


    def start(
            self,
        ):

        if self._start is not None:
            self._start()


    def render(
            self,
            frame,
        ):

        if not isinstance(frame, Frame):
            frame = Frame(frame)

        self._render(frame)


    def clear(
            self,
        ):

        if self._clear is not None:
            self._clear()


    def stop(
            self,
        ):

        if self._stop is not None:
            self._stop()


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
    'AnimationRenderer',
]
