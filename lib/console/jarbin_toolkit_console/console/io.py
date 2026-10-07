# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : io.py
#
# Author       : Jarjarbin06
# ============================================================================


import sys

from jarbin_toolkit_console.decorator import classproperty


class IO:


    @classproperty
    def stdout(
            cls,
        ):

        return sys.stdout


    @classproperty
    def stdin(
            cls,
        ):

        return sys.stdin


    @classproperty
    def stderr(
            cls,
        ):

        return sys.stderr


__all__ = [
    'IO',
]
