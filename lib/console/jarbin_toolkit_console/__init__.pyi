from typing import (
    Any,
    Optional,
    TextIO,
)


__author__: str
__email__: str
__version__: str
__license__: str
__github__: str


from . import ansi as ANSI
from .text import Text
from . import format as Format
from . import console as Console
from . import animation as Animation
from .color import (
    Color256,
    ColorRGB,
    ColorHEX,
)
from .enums import (
    PresetSymbol,
    PresetBorder,
    PresetColor,
    PresetBox,
    PresetProgress,
    PresetSpinner,
)
from .error import ConsoleJError
from .color import Color as _Color


def print(
        *values: Any,
        separator: str = " ",
        end: str = "\n",
        stream: Optional[TextIO] = None,
        prefix: str = "",
        suffix: str = "",
        reset: bool = True,
        width: Optional[int] = None,
        align: Optional[Console.ConsoleAlign] = None,
        overflow: Optional[Console.ConsoleOverflow] = None,
        wrap: bool = False,
        indent: int = 0,
        mode: Console.ConsoleOutputMode = Console.ConsoleOutputMode.NORMAL,
        flush: bool = False,
    ) -> None:
    """
        Print a formated text onto stream (stdout if left empty)

        Parameters
        ----------
        *values : Any
            Values to print

        separator : str
            Separator between each element of values

        end : str
            String to show at the very end

        stream : Optional[TextIO]
            Stream to print in

        prefix : str
            Prefix to add to each element of values

        suffix : str
            Suffix to add to each element of values

        reset : bool
            Reset SGR ANSI sequences

        width : Optional[int]
            Width to cut/truncate/wrap to

        align : Optional[ConsoleAlign]
            Align each element of values

        overflow : Optional[ConsoleOverflow]
            Type of overflow handling to use (incompatible with wrap)

        wrap : Optional[bool]
            Wrap each element of values (incompatible with overflow)

        indent : int
            Indent each element of values

        mode : ConsoleOutputMode
            Printing mode

        flush : bool
            Flush output to stdout after printing
    """


__all__: list[str]
