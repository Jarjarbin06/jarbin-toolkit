#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###    ----style.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any
from jarbin_toolkit_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Animation.Style: imported")


class Style:
    """
        Style class.

        Animation style.
    """


    def __init__(
            self,
            on : str = "#",
            off : str = "-",
            arrow_left : str = "<",
            arrow_right : str = ">",
            border_left : str = "|",
            border_right : str = "|"
        ) -> None:
        """
            Create a new style object.

            Parameters:
                on (str, optional): "#"
                off (str, optional): "-"
                arrow_left (str, optional): "<"
                arrow_right (str, optional): ">"
                border_left (str, optional): "|"
                border_right (str, optional): "|"
        """

        self.on = on
        self.off = off
        self.arrow_left = arrow_left
        self.arrow_right = arrow_right
        self.border_left = border_left
        self.border_right = border_right


    def __str__(
            self
        ) -> str:
        """
            Returns the string representation of the style.

            Returns:
                str: String representation of the style.
        """

        return (
            f'on="{self.on}";off="{self.off}";' +
            f'arrow_left="{self.arrow_left}";arrow_right="{self.arrow_right}";' +
            f'border_left="{self.border_left}";border_right="{self.border_right}"'
        )


    def __repr__(
            self
        ) -> str:
        """
            Convert Style object to string.

            Returns:
                str: Style string
        """

        return f"Style({repr(self.on)}, {repr(self.off)}, {repr(self.arrow_left)}, {repr(self.arrow_right)}, {repr(self.border_left)}, {repr(self.border_right)})"


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Animation.Style: created")
