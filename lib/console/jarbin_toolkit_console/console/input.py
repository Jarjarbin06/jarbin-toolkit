# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : input.py
#
# Author       : Jarjarbin06
# ============================================================================


import select
from time import monotonic
import termios
import tty

from jarbin_toolkit_console.error import ConsoleJError
from jarbin_toolkit_console.console.io import IO


class Input:


    @classmethod
    def input(
            cls,
            *,
            prompt = "",
        ):


        return input(prompt)


    @classmethod
    def raw(
            cls,
            *,
            stream = None,
            count = None,
            timeout = None,
            break_char = "\n",
            only_tty = True,
        ):

        if count is not None and count < 0:
            raise ConsoleJError("Count must be non-negative")

        if timeout is not None and timeout < 0:
            raise ConsoleJError("Timeout must be non-negative")

        if stream is None:
            stream = IO.stdin

        if only_tty and not stream.isatty():
            return ""

        fd = stream.fileno()
        old_settings = termios.tcgetattr(fd)

        result = []
        start = monotonic()

        try:
            tty.setraw(fd)

            while count is None or len(result) < count:
                remaining = None

                if timeout is not None:
                    remaining = timeout - (monotonic() - start)

                    if remaining <= 0:
                        break

                ready, _, _ = select.select(
                    [fd],
                    [],
                    [],
                    remaining,
                )

                if not ready:
                    break

                char = stream.read(1)

                if not char:
                    break

                if break_char is not None and char == break_char:
                    break

                result.append(char)

        finally:
            termios.tcsetattr(
                fd,
                termios.TCSADRAIN,
                old_settings,
            )

        return "".join(result)


    @classmethod
    def key(
            cls,
            *,
            stream = None,
            timeout = None,
            only_tty = True,
        ):

        return cls.raw(
            stream=stream,
            count=1,
            timeout=timeout,
            break_char=None,
            only_tty=only_tty,
        )


    @classmethod
    def keys(
            cls,
            *,
            stream = None,
            count = None,
            break_char = "\n",
            timeout = None,
            only_tty = True,
        ):

        return cls.raw(
            stream=stream,
            count=count,
            timeout=timeout,
            break_char=break_char,
            only_tty=only_tty,
        )


__all__ = [
    'Input',
]
