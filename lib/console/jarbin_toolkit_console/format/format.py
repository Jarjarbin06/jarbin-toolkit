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


class Format(Style, Color, Layout):


    _can_format = True
    _sgr = None


    @classmethod
    def _get_sgr(
            cls,
        ):

        if cls._sgr is None:
            import jarbin_toolkit_console.ansi.sgr as SGR

            cls._sgr = SGR

        return cls._sgr
