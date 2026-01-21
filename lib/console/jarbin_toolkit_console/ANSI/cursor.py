#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###   ----cursor.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any
from jarbin_toolkit_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "ANSI.Cursor: imported")


class Cursor:
    """
        Cursor class.

        Manipulate the cursor's position.
    """

    from jarbin_toolkit_console.ANSI.ansi import ANSI


    @staticmethod
    def up(
            n: int = 1
        ) -> ANSI:
        """
            Bring the cursor up 'n' lines

            Parameters:
                n (int, optional): number of lines up

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}{n}A")


    @staticmethod
    def down(
            n: int = 1
        ) -> ANSI:
        """
            Bring the cursor down 'n' lines

            Parameters:
                n (int, optional): number of lines down

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}{n}B")


    @staticmethod
    def left(
            n: int = 1
        ) -> ANSI:
        """
            Bring the cursor left 'n' column

            Parameters:
                n (int, optional): number of column left

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}{n}D")


    @staticmethod
    def right(
            n: int = 1
        ) -> ANSI:
        """
            Bring the cursor right 'n' column

            Parameters:
                n (int, optional): number of column right

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}{n}C")


    @staticmethod
    def top(
        ) -> ANSI:
        """
            Move the cursor to the top left corner of the console

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}H")


    @staticmethod
    def previous(
            n: int = 1
        ) -> ANSI:
        """
            Move the cursor to the beginning of the 'n' previous line

            Parameters:
                n (int, optional): number of column up

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}{n}F")


    @staticmethod
    def next(
            n: int = 1
        ) -> ANSI:
        """
            Move the cursor to the beginning of the 'n' next line

            Parameters:
                n (int, optional): number of column right

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}{n}E")


    @staticmethod
    def move(
            y : int = 0,
            x : int = 0
        ) -> ANSI:
        """
            Move the cursor to the column x and line y

            Parameters:
                y (int, optional): row y position
                x (int, optional): column x position

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}{y};{x}H")


    @staticmethod
    def move_column(
            x : int = 0
        ) -> ANSI:
        """
            Move the cursor to the column x and line y

            Parameters:
                x (int, optional): column x position

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}{x}G")


    @staticmethod
    def set(
        ) -> ANSI:
        """
            Save the cursor's position

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}7")


    @staticmethod
    def reset(
        ) -> ANSI:
        """
            Move the cursor to the saved position

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}8")


    @staticmethod
    def show(
        ) -> ANSI:
        """
            Show the cursor

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}?25h")


    @staticmethod
    def hide(
        ) -> ANSI:
        """
            Hide the cursor

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}?25l")


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "ANSI.Cursor: created")
