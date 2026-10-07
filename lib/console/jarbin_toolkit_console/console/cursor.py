# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : cursor.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.ansi.cursor.cursor import CursorMode
from jarbin_toolkit_console.ansi.cursor.cursor import CursorPosition
from jarbin_toolkit_console.console.output import Output
from jarbin_toolkit_console.ansi.query import Query


class Cursor:


    @classmethod
    def get_cursor_position(
            cls,
        ):

        return Query.cursor_position()


    @classmethod
    def move_cursor(
            cls,
            x,
            y,
        ):

        Output.write(CursorPosition.position(x, y))


    @classmethod
    def hide_cursor(
            cls,
        ):

        Output.write(CursorMode.hide())


    @classmethod
    def show_cursor(
            cls,
        ):

        Output.write(CursorMode.show())


__all__ = [
    'Cursor',
]
