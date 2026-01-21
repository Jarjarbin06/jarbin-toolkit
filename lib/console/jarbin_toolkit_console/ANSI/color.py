#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###    ----color.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any
from jarbin_toolkit_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "ANSI.Color: imported")


class Color:
    """
        Color class.

        ANSI coloring system.

        Attributes:
            C_RESET (int): Base color code.
            C_BOLD (int): Bold color code.
            C_ITALIC (int): Italic color code.
            C_UNDERLINE (int): Underline color code.
            C_FLASH_SLOW (int): Flash color code.
            C_FLASH_FAST (int): Flash color code.
            C_HIDDEN (int): Hidden color code.
            C_STRIKETHROUGH (int): Crossed color code.

            C_FG_DARK (int): Dark base color code.
            C_FG_DARK_GREY (int): Dark grey color code.
            C_FG_DARK_RED (int): Dark red color code.
            C_FG_DARK_GREEN (int): Dark green color code.
            C_FG_DARK_YELLOW (int): Dark yellow color code.
            C_FG_DARK_BLUE (int): Dark blue color code.
            C_FG_DARK_LAVANDA (int): Dark lavanda color code.
            C_FG_DARK_CYAN (int): Dark cyan color code.
            C_FG_DARK_WHITE (int): Dark white color code.
            C_FG_GREY (int): Grey color code.
            C_FG_RED (int): Red color code.
            C_FG_GREEN (int): Green color code.
            C_FG_YELLOW (int): Yellow color code.
            C_FG_BLUE (int): Blue color code.
            C_FG_LAVANDA (int): Lavanda color code.
            C_FG_CYAN (int): Cyan color code.
            C_FG_WHITE (int): White color code.

            C_BG (int): BACKGROUND color code.
            C_BG_DARK_GREY (int): BACKGROUND dark grey color code.
            C_BG_DARK_RED (int): BACKGROUND dark red color code.
            C_BG_DARK_GREEN (int): BACKGROUND dark green color code.
            C_BG_DARK_YELLOW (int): BACKGROUND dark yellow color code.
            C_BG_DARK_BLUE (int): BACKGROUND dark blue color code.
            C_BG_DARK_LAVANDA (int): BACKGROUND dark lavanda color code.
            C_BG_DARK_CYAN (int): BACKGROUND dark cyan color code.
            C_BG_DARK_WHITE (int): BACKGROUND dark white color code.
            C_BG_GREY (int): BACKGROUND grey color code.
            C_BG_RED (int): BACKGROUND red color code.
            C_BG_GREEN (int): BACKGROUND green color code.
            C_BG_YELLOW (int): BACKGROUND yellow color code.
            C_BG_BLUE (int): BACKGROUND blue color code.
            C_BG_LAVANDA (int): BACKGROUND lavanda color code.
            C_BG_CYAN (int): BACKGROUND cyan color code.
            C_BG_WHITE (int): BACKGROUND white color code.
    """

    from jarbin_toolkit_console.ANSI.ansi import ANSI

    C_RESET : int = 0
    C_BOLD : int = 1
    C_ITALIC : int = 3
    C_UNDERLINE : int = 4
    C_FLASH_SLOW : int = 5
    C_FLASH_FAST : int = 6
    C_HIDDEN : int = 8
    C_STRIKETHROUGH : int = 9

    C_FG_DARK : int = 2
    C_FG_DARK_GREY : int = 30
    C_FG_DARK_RED : int = 31
    C_FG_DARK_GREEN : int = 32
    C_FG_DARK_YELLOW : int = 33
    C_FG_DARK_BLUE : int = 34
    C_FG_DARK_LAVANDA : int = 35
    C_FG_DARK_CYAN : int = 36
    C_FG_DARK_WHITE : int = 37
    C_FG_GREY : int = 90
    C_FG_RED : int = 91
    C_FG_GREEN : int = 92
    C_FG_YELLOW : int = 93
    C_FG_BLUE : int = 94
    C_FG_LAVANDA : int = 95
    C_FG_CYAN : int = 96
    C_FG_WHITE : int = 97

    C_BG : int = 7
    C_BG_DARK_GREY : int = 40
    C_BG_DARK_RED : int = 41
    C_BG_DARK_GREEN : int = 42
    C_BG_DARK_YELLOW : int = 43
    C_BG_DARK_BLUE : int = 44
    C_BG_DARK_LAVANDA : int = 45
    C_BG_DARK_CYAN : int = 46
    C_BG_DARK_WHITE : int = 47
    C_BG_GREY : int = 100
    C_BG_RED : int = 101
    C_BG_GREEN : int = 102
    C_BG_YELLOW : int = 103
    C_BG_BLUE : int = 104
    C_BG_LAVANDA : int = 105
    C_BG_CYAN : int = 106
    C_BG_WHITE : int = 107


    def __new__(
            cls,
            *args
        ) -> ANSI:
        """
            Call Color.color()
        """

        return Color.color(*args)


    @staticmethod
    def color(
            color: Any | str | int
        ) -> ANSI:
        """
            Get ANSI sequence from the 'color' (color must be one of the preset C_?)

            Arguments:
                color (ANSI | str | int): color code

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        if type(color) in [ANSI, str]:
            return ANSI(str(color))

        elif type(color) in [int]:
            if 0 <= color <= 107:
                return ANSI(f"{ANSI.ESC}{str(color)}m")

            else:
                return ANSI("")

        else:
            return ANSI("")


    @staticmethod
    def color_fg(
            color : int
        ) -> ANSI:
        """
            Get ANSI sequence for the foreground color 'color'

            Arguments:
                color (int): color code

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        if 0 <= color <= 255:
            return ANSI(f"{ANSI.ESC}38;5;{color}m")

        return ANSI("")


    @staticmethod
    def color_bg(
            color : int
        ) -> ANSI:
        """
            Get ANSI sequence for the background color 'color'

            Arguments:
                color (int): color code

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        if 0 <= color <= 255:
            return ANSI(f"{ANSI.ESC}48;5;{color}m")

        return ANSI("")



    @staticmethod
    def rgb_fg(
            r : int,
            g : int,
            b : int
        ) -> ANSI:
        """
            Get ANSI sequence for the foreground color with 'r', 'g' and 'b'

            Arguments:
                r (int): red value (0->255)
                g (int): green value (0->255)
                b (int): blue value (0->255)

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return ANSI(f"{ANSI.ESC}38;2;{r};{g};{b}m")

        return ANSI("")


    @staticmethod
    def rgb_bg(
            r : int,
            g : int,
            b : int
        ) -> ANSI:
        """
            Get ANSI sequence for the background color with 'r', 'g' and 'b'

            Arguments:
                r (int): red value (0->255)
                g (int): green value (0->255)
                b (int): blue value (0->255)

            Returns:
                ANSI: ansi sequence
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return ANSI(f"{ANSI.ESC}48;2;{r};{g};{b}m")

        return ANSI("")


    @staticmethod
    def epitech_fg(
        ) -> ANSI:
        """
            Get ANSI sequence for the foreground color of epitech

            Returns:
                ANSI: ansi sequence
        """

        return Color.rgb_fg(0, 145, 211)


    @staticmethod
    def epitech_bg(
        ) -> ANSI:
        """
            Get ANSI sequence for the background color of epitech

            Returns:
                ANSI: ansi sequence
        """

        return Color.rgb_bg(0, 145, 211)


    @staticmethod
    def epitech_dark_fg(
        ) -> ANSI:
        """
            Get ANSI sequence for the foreground color of epitech

            Returns:
                ANSI: ansi sequence
        """

        return Color.rgb_fg(31, 72, 94)


    @staticmethod
    def epitech_dark_bg(
        ) -> ANSI:
        """
            Get ANSI sequence for the background color of epitech

            Returns:
                ANSI: ansi sequence
        """

        return Color.rgb_bg(31, 72, 94)


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "ANSI.Color: created")
