# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI
# File         : ansi.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.text import Text


class ANSI(Text):


    PREFIX = ""


    def __new__(
            cls,
            value,
        ):
        if not isinstance(value, str):
            raise TypeError("ANSI value must be a string")

        return super().__new__(cls, f"{cls.PREFIX}{value}")


    def __add__(
            self,
            other,
        ):
        if isinstance(other, (str, Text)):
            return Text(str.__add__(self, str(other)))

        return NotImplemented


    def __radd__(
            self,
            other,
        ):
        if isinstance(other, (str, Text)):
            return Text(str.__add__(str(other), self))

        return NotImplemented


    def __repr__(
            self
        ) -> str:
        return f"ANSI({str.__repr__(self)})"


class ESC(ANSI):


    PREFIX = "\033"


class CSI(ANSI):


    PREFIX = "\033["


class OSC(ANSI):


    PREFIX = "\033]"

class G0(ANSI):


    PREFIX = "\033("


class G1(ANSI):


    PREFIX = "\033)"


class G2(ANSI):


    PREFIX = "\033*"


class G3(ANSI):


    PREFIX = "\033+"


class DCS(ANSI):


    PREFIX = "\033P"


__all__ = [
    'ANSI',
    'ESC',
    'CSI',
    'OSC',
    'G0',
    'G1',
    'G2',
    'G3',
    'DCS',
]
