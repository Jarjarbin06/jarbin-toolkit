#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###  ----basepack.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any
from jarbin_toolkit_console.System.setting import Setting


Setting.update()


class BasePack:
    """
        BasePack class.

        Base animation pack ready for use.

        Attributes:
            P_ERROR (tuple): error tuple of color.
            P_WARNING (tuple): warning tuple of color.
            P_VALID (tuple): validation tuple of color.
            P_INFO (tuple): information tuple of color.
    """


    from jarbin_toolkit_console.ANSI.ansi import ANSI


    P_CRITIC : tuple[ANSI | str, ANSI | str] = ("\033[0m", "\033[0m")
    P_ERROR : tuple[ANSI | str, ANSI | str] = ("\033[0m", "\033[0m")
    P_WARNING : tuple[ANSI | str, ANSI | str] = ("\033[0m", "\033[0m")
    P_VALID : tuple[ANSI | str, ANSI | str] = ("\033[0m", "\033[0m")
    P_DEBUG : tuple[ANSI | str, ANSI | str] = ("\033[0m", "\033[0m")
    P_INFO : tuple[ANSI | str, ANSI | str] = ("\033[0m", "\033[0m")


    @staticmethod
    def update(
        ) -> None:
        """
            Initialize the BasePack class
        """

        from jarbin_toolkit_console.ANSI.color import Color

        BasePack.P_CRITIC = (Color(Color.C_FG_DARK_RED) + Color.rgb_bg(0, 0, 0), Color(Color.C_FG_DARK_RED) + Color.rgb_bg(0, 0, 0))
        BasePack.P_ERROR = (Color(Color.C_BG_DARK_RED), Color(Color.C_FG_DARK_RED))
        BasePack.P_WARNING = (Color(Color.C_BG_DARK_YELLOW), Color(Color.C_FG_DARK_YELLOW))
        BasePack.P_VALID = (Color(Color.C_BG_DARK_GREEN), Color(Color.C_FG_DARK_GREEN))
        BasePack.P_DEBUG = (Color(Color.C_BG_DARK_BLUE), Color(Color.C_FG_DARK_BLUE))
        BasePack.P_INFO = (Color(Color.C_BG), Color(Color.C_RESET))
