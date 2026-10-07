# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : context.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.ansi.screen.screen import ScreenBuffer
from jarbin_toolkit_console.console.output import Output


class _ContextMeta(type):


    def __enter__(
            self
        ):
        Context.alternate_screen()


    def __exit__(
            self,
            exc_type,
            exc_value,
        ):
        Context.normal_screen()


class Context:


    _is_alternate = False


    @classmethod
    def alternate_screen(
            cls,
        ):

        if cls._is_alternate:
            raise IOError("Already on alternate screen")

        Output.write(ScreenBuffer.alternate())
        cls._is_alternate = True


    @classmethod
    def normal_screen(
            cls,
        ):

        if not cls._is_alternate:
            raise IOError("Already on normal screen")

        Output.write(ScreenBuffer.normal())
        cls._is_alternate = False


__all__ = [
    'Context',
    '_ContextMeta',
]
