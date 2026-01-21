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


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Animation.BasePack: imported")


class BasePack:
    """
        BasePack class.

        Base animation pack ready for use.

        Attributes:
            P_SLIDE_R (tuple): slide right animation.
            P_SLIDE_L (tuple): slide left animation.
            P_SLIDER_R (tuple): slider right animation.
            P_SLIDER_L (tuple): slider left animation.
            P_FILL_R (tuple): fill right animation.
            P_FILL_L (tuple): fill left animation.
            P_EMPTY_R (tuple): empty right animation.
            P_EMPTY_L (tuple): empty left animation.
            P_FULL (tuple): full animation.
            P_EMPTY (tuple): empty animation.
    """


    from jarbin_toolkit_console.Animation.style import Style


    P_SLIDE_R = []
    P_SLIDE_L = []
    P_SLIDER_R = []
    P_SLIDER_L = []
    P_FILL_R = []
    P_FILL_L = []
    P_EMPTY_R = []
    P_EMPTY_L = []
    P_FULL = []
    P_EMPTY = []


    @staticmethod
    def update(
            style: Style = Style("#", "-", "<", ">", "|", "|")
        ) -> None:
        """
            Initialize the BasePack class

            Parameters:
                style (Style, optional): Style of the BasePack animations.
        """

        from jarbin_toolkit_console.Animation.style import Style

        if not type(style) in [Style]:

            ## cannot be tested with pytest ##

            from jarbin_toolkit_console.Error.error import ErrorType # pragma: no cover
            from jarbin_toolkit_console import quit # pragma: no cover

            if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("ERROR", "type", f"Animation.BasePack.update: style is of an unsupported type (supported: Style ; current: {type(style)})") # pragma: no cover
            quit() # pragma: no cover
            raise ErrorType() from None # pragma: no cover

        BasePack.P_SLIDE_R = [
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.border_right}"
        ]

        BasePack.P_SLIDE_L = [
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}"
        ]

        BasePack.P_SLIDER_R = [
            f"{style.border_left}{style.arrow_right}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.arrow_right}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.arrow_right}{style.off}{style.border_right}"
        ]

        BasePack.P_SLIDER_L = [
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.arrow_left}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.arrow_left}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.arrow_left}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}"
        ]

        BasePack.P_FILL_R = [
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_right}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_right}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_right}{style.border_right}"
        ]

        BasePack.P_FILL_L = [
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.arrow_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.arrow_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.arrow_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}"
        ]

        BasePack.P_EMPTY_R = [
            f"{style.border_left}{style.arrow_right}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.arrow_right}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.on}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.arrow_right}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}"
        ]

        BasePack.P_EMPTY_L = [
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_left}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_left}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.on}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.arrow_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}",
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}"
        ]

        BasePack.P_FULL = [
            f"{style.border_left}{style.arrow_left}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.on}{style.arrow_right}{style.border_right}"
        ]

        BasePack.P_EMPTY = [
            f"{style.border_left}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.off}{style.border_right}"
        ]


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Animation.BasePack: created")
