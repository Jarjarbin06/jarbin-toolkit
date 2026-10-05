# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : format.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.format.layout import Layout
from jarbin_toolkit_console.format.color import Color
from jarbin_toolkit_console.format.style import Style
from jarbin_toolkit_console.format.border import Border
from jarbin_toolkit_console.format.decoration import Decoration


class Format(Style, Color, Layout, Border, Decoration):


    _can_format = True
    _sgr = None
    _cursor = None


    @classmethod
    def _get_sgr(
            cls,
        ):

        if cls._sgr is None:
            import jarbin_toolkit_console.ansi.sgr as SGR

            cls._sgr = SGR

        return cls._sgr


    @classmethod
    def _get_cursor(
            cls,
        ):

        if cls._cursor is None:
            import jarbin_toolkit_console.ansi.cursor as Cursor

            cls._cursor = Cursor

        return cls._cursor
