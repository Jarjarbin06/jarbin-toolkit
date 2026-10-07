# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : terminal.py
#
# Author       : Jarjarbin06
# ============================================================================


from os import get_terminal_size

from jarbin_toolkit_console.console.io import IO


class Terminal:


    @classmethod
    def size(
            cls,
            *,
            stream = None
        ):

        if stream is None:
            stream = IO.stdout

        if not cls.is_tty(stream=stream):
            return None

        size = get_terminal_size(stream.fileno())

        return size.columns, size.lines


    @classmethod
    def width(
            cls,
            *,
            stream = None
        ):

        return cls.size(stream=stream)[0]


    @classmethod
    def height(
            cls,
            *,
            stream = None
        ):

        return cls.size(stream=stream)[1]


    @classmethod
    def is_tty(
            cls,
            *,
            stream = None
        ):

        if stream is None:
            stream = IO.stdout

        return stream.isatty()


__all__ = [
    'Terminal',
]
