# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : console.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.console.context import (
    Context,
    _ContextMeta,
)
from jarbin_toolkit_console.console.cursor import Cursor
from jarbin_toolkit_console.console.input import Input
from jarbin_toolkit_console.console.io import IO
from jarbin_toolkit_console.console.output import Output
from jarbin_toolkit_console.console.terminal import Terminal


class Console(Context, Cursor, Input, IO, Output, Terminal, metaclass=_ContextMeta):


    pass


__all__ = [
    'Console',
]
