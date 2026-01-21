#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###     ----line.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any
from jarbin_toolkit_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "ANSI.Line: imported")


class Line:
    """
        Line class.

        Manipulate the lines of the console.
    """

    from jarbin_toolkit_console.ANSI.ansi import ANSI


    @staticmethod
    def clear_line(
        ) -> ANSI:
        """
            Clear the current line

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}2K")


    @staticmethod
    def clear_start_line(
        ) -> ANSI:
        """
            Clear the current line from the start to the cursor's position

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}1K")


    @staticmethod
    def clear_end_line(
        ) -> ANSI:
        """
            Clear the current line from the cursor's position to the end

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}K")


    @staticmethod
    def clear_screen(
        ) -> ANSI:
        """
            Clear the screen

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}2J")


    @staticmethod
    def clear(
        ) -> ANSI:
        """
            Clear the screen and bring the cursor to the top left corner

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.cursor import Cursor

        return Line.clear_screen() + Cursor.top()


    @staticmethod
    def clear_previous_line(
            n : int = 1
    ) -> ANSI:
        """
            Clear the previous line.

            Parameters:
                n (int): line up

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.cursor import Cursor

        return Cursor.previous(n) + Line.clear_line()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "ANSI.Line: created")
