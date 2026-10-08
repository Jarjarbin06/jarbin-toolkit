# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : output.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.error import ConsoleJError
from jarbin_toolkit_console.format.enums import FormatPosition
from jarbin_toolkit_console.console.enums import ConsoleOverflow
from jarbin_toolkit_console.console.terminal import Terminal
from jarbin_toolkit_console.ansi.cursor.cursor import CursorPosition
from jarbin_toolkit_console.ansi.screen.screen import ScreenErase
from jarbin_toolkit_console.ansi.sgr.sgr import SGR
from jarbin_toolkit_console.ansi.sgr.enums import SGRReset
from jarbin_toolkit_console.console.enums import (
    ConsoleAlign,
    ConsoleOutputMode,
)
from jarbin_toolkit_console.text import Text
from jarbin_toolkit_console.console.io import IO


class Output:


    _previous_height = 0


    @classmethod
    def write(
            cls,
            value,
            *,
            stream = None,
        ):

        if stream is None:
            stream = IO.stdout

        stream.write(value)


    @classmethod
    def print(
            cls,
            *values,
            separator = " ",
            end = "\n",
            stream = None,
            prefix = "",
            suffix = "",
            reset = True,
            width = None,
            align = None,
            overflow = None,
            wrap = False,
            indent = 0,
            mode = ConsoleOutputMode.NORMAL,
            flush = False,
        ):

        if (
            align is not None and not isinstance(align, ConsoleAlign)
            or overflow is not None and not isinstance(overflow, ConsoleOverflow)
            or mode is not None and not isinstance(mode, ConsoleOutputMode)
        ):
            raise ConsoleJError("Align, overflow, and mode must be of type ConsoleOutputMode")

        if overflow is not None and wrap:
            raise ConsoleJError("Overflow cannot be used with wrap")

        if stream is None:
            stream = IO.stdout

        if width is None:
            width = Terminal.width(stream=stream)

        new_text = Text("")

        new_text += separator.join(
            f"{prefix}{value}{suffix}"
            for value in values
        )

        if reset:
            new_text += SGR.reset(SGRReset.ALL)

        if overflow == ConsoleOverflow.ELLIPSIS:
            new_text = new_text.f_layout_truncate(width)
        elif overflow == ConsoleOverflow.TRUNCATE:
            new_text = new_text.f_layout_truncate(width + 1, suffix="")
        elif wrap:
            new_text = new_text.f_layout_wrap(width)

        if align is not None:
            new_text = new_text.f_layout_align(width, align=FormatPosition(align))

        new_text = new_text.f_layout_indent(indent=indent)

        new_text += end

        tmp_previous_height = new_text.f_layout_get_height()

        if cls._previous_height > 0 and mode == ConsoleOutputMode.OVERWRITE:
            erase = Text("")

            for _ in range(cls._previous_height):
                erase += CursorPosition.previous_line()
                erase += CursorPosition.column()
                erase += ScreenErase.erase_line()

            new_text = erase + new_text

        cls._previous_height = tmp_previous_height

        print(
            new_text,
            end="",
            file=stream,
            flush=flush,
        )


    @classmethod
    def render(
            cls,
            value,
            *,
            stream = None,
            flush = True,
        ):

        if stream is None:
            stream = IO.stdout

        cls.write(value, stream=stream)

        if flush:
            cls.flush(stream=stream)


    @classmethod
    def flush(
            cls,
            *,
            stream = None,
        ):

        if stream is None:
            stream = IO.stdout

        stream.flush()


__all__ = [
    'Output',
]
