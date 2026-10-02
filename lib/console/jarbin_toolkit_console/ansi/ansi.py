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
    _can_format = False


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


    PREFIX = "\x1b"


class CSI(ANSI):


    PREFIX = "\x1b["


class OSC(ANSI):


    PREFIX = "\x1b]"

class G0(ANSI):


    PREFIX = "\x1b("


class G1(ANSI):


    PREFIX = "\x1b)"


class G2(ANSI):


    PREFIX = "\x1b*"


class G3(ANSI):


    PREFIX = "\x1b+"


class DCS(ANSI):


    PREFIX = "\x1bP"


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
