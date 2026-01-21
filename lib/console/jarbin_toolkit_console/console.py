#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###   ----console.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object, type
from typing import Any
from jarbin_toolkit_console.System.setting import Setting


Setting.update()


class ConsoleMeta(type):
    """
        Metaclass for Console classe.
    """


    def __len__(
            cls
        ) -> int:
        """
            get length of the current terminal (number of columns)

            Returns:
                int: length of the terminal
        """

        from os import get_terminal_size

        size: int

        try :
            size = get_terminal_size().columns

        except OSError:
            size = 100

        return size


class Console(metaclass=ConsoleMeta):
    """
        Console class.

        Console tool.
    """


    from sys import stdout


    @staticmethod
    def execute(
        ) -> None:
        """
            Execute code in the console.
        """

        ## cannot be tested with pytest ##

        pass # pragma: no cover #yet to be implemented


    @staticmethod
    def print(
            *args,
            separator: str = " ",
            start: str = "",
            end: str = "\n",
            file: Any = stdout,
            auto_reset: bool = True,
            cut: bool = False,
            sleep: int | float | None = None
        ) -> Any:
        """
            Print on the console.

            WARNING : 'cut_to_terminal_size' does not work with ANSI sequence
            WARNING : 'cut_to_terminal_size' does not work properly when changing terminal size

            Parameters:
                *args: Any values to print.
                separator (str, optional): Separator between values.
                start (str, optional): String prepended before printing.
                end (str, optional): String appended after printing.
                file (Any, optional): File-like object to write into.
                auto_reset (bool, optional): Automatically reset ANSI sequence.
                cut (bool, optional): Cut output to terminal width.
                sleep (int | float | None, optional): Delay in seconds after printing.

            Returns:
                Text: Text printed on the console.
        """

        from jarbin_toolkit_console.System import Time
        from jarbin_toolkit_console.ANSI.color import Color
        from jarbin_toolkit_console.Text.text import Text

        string_list : list[str]
        string : str = ""
        final_string : Text = Text("")

        for idx in range(len(args)):
            if idx and idx < len(args):
                string += separator
            string += str(args[idx])

        string_list = string.split("\n")

        for idx in range(len(string_list)):
            if cut and (len(string_list[idx]) - (string_list[idx].count("\033[") * 2)) > (len(Console) + 6):
                string_list[idx] = string_list[idx][:(len(Console) + 2 + string_list[idx].count("\033[") * 2)] + "..." + str(Color(Color.C_RESET))
            final_string += Text(string_list[idx]) + (Text("\n") if len(string_list) > 1 else Text(""))

        final_string = Text(start) + final_string + (Color(Color.C_RESET) if auto_reset else Text("")) + Text(end)

        print(final_string, end="", file=file)

        if sleep:
            Time.wait(sleep)

        return final_string


    @staticmethod
    def input(
            msg : str = "Input",
            separator : str = " >>> ",
            wanted_type : type = str
        ) -> Any:
        """
            Get user text input from the console.

            Parameters:
                msg (str, optional) : Message to show when user enters input.
                separator (str, optional): Separator between message and input.
                wanted_type (type, optional): Type of input to return.

            Returns:
                Any: User input as 'type' type.
        """

        ## cannot be tested with pytest ##

        return wanted_type(input(msg + separator)) # pragma: no cover


    @staticmethod
    def get_key_press(
        ) -> str:
        """
            Wait for a key press and return it.
            (code from AI)

            Returns:
                str: Key pressed.
        """

        ## cannot be tested with pytest ##

        import sys
        import tty
        import termios

        if not sys.stdin.isatty():
            return ""

        fd = sys.stdin.fileno() # pragma: no cover
        old_settings = termios.tcgetattr(fd) # pragma: no cover

        try: # pragma: no cover
            tty.setraw(fd) # pragma: no cover
            ch1 = sys.stdin.read(1) # pragma: no cover

            if ch1 == '\x1b':  # ESC # pragma: no cover
                ch2 = sys.stdin.read(1) # pragma: no cover
                ch3 = sys.stdin.read(1) # pragma: no cover
                return ch1 + ch2 + ch3 # pragma: no cover
            return ch1 # pragma: no cover
        finally: # pragma: no cover
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # pragma: no cover


    @staticmethod
    def get_cursor_position(
        ) -> tuple[int, int]:
        """
            Return cursor position in console.
            (code from AI)

            Returns:
                tuple: cursor position in console.
        """

        ## cannot be tested with pytest ##

        import sys
        import tty
        import termios
        import re

        if not sys.stdin.isatty():
            return 0, 0

        fd = sys.stdin.fileno() # pragma: no cover
        old = termios.tcgetattr(fd) # pragma: no cover

        try: # pragma: no cover
            tty.setraw(fd) # pragma: no cover

            # Request cursor position
            sys.stdout.write("\x1b[6n") # pragma: no cover
            sys.stdout.flush() # pragma: no cover

            # Read response: ESC [ row ; col R
            response = "" # pragma: no cover
            while True: # pragma: no cover
                ch = sys.stdin.read(1) # pragma: no cover
                response += ch # pragma: no cover
                if ch == "R": # pragma: no cover
                    break # pragma: no cover

        finally: # pragma: no cover
            termios.tcsetattr(fd, termios.TCSADRAIN, old) # pragma: no cover

        match = re.match(r"\x1b\[(\d+);(\d+)R", response) # pragma: no cover
        if not match: # pragma: no cover
            raise RuntimeError(f"Invalid response: {repr(response)}") # pragma: no cover

        row, col = map(int, match.groups()) # pragma: no cover
        return row, col # pragma: no cover


    @staticmethod
    def get_size(
        ) -> tuple[int, int]:
        """
            get the size of the current terminal

            Returns:
                tuple: size (width, height) of the terminal
        """

        import sys
        from os import get_terminal_size

        if not sys.stdin.isatty():
            return 0, 0

        size : tuple[int, int] # pragma: no cover

        t_size = get_terminal_size() # pragma: no cover
        size = (t_size.columns, t_size.lines) # pragma: no cover

        return size # pragma: no cover


    @staticmethod
    def flush(
            stream : Any = stdout,
        ) -> None:
        """
            Flush console output.

            Parameters:
                stream (Any, optional) : Stream object to be flushed (generally stdin, stdout and stderr).
        """

        ## cannot be tested with pytest ##

        stream.flush() # pragma: no cover
