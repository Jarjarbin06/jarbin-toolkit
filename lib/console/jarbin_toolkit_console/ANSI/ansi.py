#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###    ----ansi.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any
from jarbin_toolkit_console.Text.format import Format
from jarbin_toolkit_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "ANSI.ANSI: imported")


class ANSI(Format):
    """
        ANSI class.

        ANSI string tool.

        Attributes:
            ESC (str) : ANSI escape (ANSI sequence starter).
    """


    ESC: str = "\x1b["


    def __init__(
            self,
            sequence : list[Any | str] | Any | str = ""
        ) -> None:
        """
            Create an ANSI sequence.

            Parameters:
                sequence (list[ANSI | str] | Any | str, optional): ANSI sequence
        """

        self.sequence : str = ""

        if type(sequence) in [list]:
            for item in sequence:
                self.sequence += str(item)

        else:
            self.sequence = str(sequence)


    def __add__(
            self,
            other : Any
        ) -> Any:
        """
            Add 2 ANSI sequences together.
            'other' must have __str__ method.

            Parameters:
                other (ANSI | Animation | StopWatch | ProgressBar | Text | Any): ANSI sequence

            Returns:
                ANSI: ANSI sequence
        """

        from jarbin_toolkit_console.Animation.animation import Animation
        from jarbin_toolkit_console.Animation.progressbar import ProgressBar
        from jarbin_toolkit_console.Text.text import Text
        from jarbin_toolkit_console.System.stopwatch import StopWatch

        if type(other) in [ANSI]:
            return ANSI(f"{self.sequence}{other.sequence}")

        elif type(other) in [Animation, StopWatch, ProgressBar, Text, str]:
            return ANSI(f"{self.sequence}{str(other)}")

        else:
            return self


    def __mul__(
            self,
            other : int
        ) -> Any:
        """
            Multiply ANSI sequences.
        """

        return ANSI(str(self) * other)


    def __str__(
            self
        ) -> str:
        """
            Convert ANSI object to string.

            Returns:
                str: ANSI string
        """

        return str(self.sequence)


    def __len__(
            self
        ) -> int:
        """
            Return the number of ANSI sequences.
        """

        return len(self.sequence)


    def __repr__(
            self
        ) -> str:
        """
            Convert ANSI object to string.

            Returns:
                str: ANSI string
        """

        return f"ANSI({repr(self.sequence)})"


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "ANSI.ANSI: created")
