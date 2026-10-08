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

        size = cls.size(stream=stream)

        return size[0] if size is not None else None


    @classmethod
    def height(
            cls,
            *,
            stream = None
        ):

        size = cls.size(stream=stream)

        return size[1] if size is not None else None


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
