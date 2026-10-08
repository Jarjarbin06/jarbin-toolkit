from typing import (
    Any,
    TextIO,
    Optional,
)

from jarbin_toolkit_console.console.enums import (
    ConsoleAlign,
    ConsoleOutputMode,
    ConsoleOverflow,
)
from jarbin_toolkit_console.text import Text


class Output:
    """
        Output console controller
    """


    @classmethod
    def write(
            cls,
            value: str,
            *,
            stream: Optional[TextIO] = None,
        ) -> None:
        """
            Write a text onto stream (stdout if stream left empty)
        
            Parameters
            ----------
            value : str
                Value to write

            stream : Optional[TextIO]
                Stream to write in
        """
        ...


    @classmethod
    def print(
            cls,
            *values: Any,
            separator: str = " ",
            end: str = "\n",
            stream: Optional[TextIO] = None,
            prefix: str = "",
            suffix: str = "",
            reset: bool = True,
            width: Optional[int] = None,
            align: Optional[ConsoleAlign] = None,
            overflow: Optional[ConsoleOverflow] = None,
            wrap: bool = False,
            indent: int = 0,
            mode: ConsoleOutputMode = ConsoleOutputMode.NORMAL,
            flush: bool = False,
        ) -> Text:
        """
            Print a formated text onto stream (stdout if stream left empty)

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

            Returns
            ----------
            Text
                Final printed text
        """
        ...


    @classmethod
    def render(
            cls,
            value: Text,
            *,
            stream: Optional[TextIO] = None,
            flush: bool = True,
        ) -> None:
        """
            Render a Text object (stdout if stream left empty)

            Parameters
            ----------
            value : Text
                Text to render

            stream : Optional[TextIO]
                Stream to render in

            flush : bool
                Flush output to stdout after rendering
        """
        ...


    @classmethod
    def flush(
            cls,
            *,
            stream: Optional[TextIO] = None,
        ) -> None:
        """
            Flush a stream (stdout if stream left empty)
        
            Parameters
            ----------
            stream : Optional[TextIO]
                Stream to flush
        """


    _previous_height: int


__all__ = [
    'Output',
]
