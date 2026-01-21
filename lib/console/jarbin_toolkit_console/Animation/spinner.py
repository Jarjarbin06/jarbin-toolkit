#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###   ----spinner.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any
from jarbin_toolkit_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Animation.Spinner: imported")


class Spinner:
    """
        ProgressBar class.

        Progress-bar tool.
    """


    from jarbin_toolkit_console.Animation.animation import Animation
    from jarbin_toolkit_console.Animation.style import Style


    @staticmethod
    def stick(
            *,
            style : Any = Style("#", " ", "#", "#", "", "")
        ) -> Animation:
        """
            Stick spinner.

            Parameters:
                style (Style, optional): Style of the animations.

            Returns:
                Animation: Stick animation.
        """

        from jarbin_toolkit_console.Animation.animation import Animation

        return Animation(
            [
                f"{style.border_left}-{style.border_right}",
                f"{style.border_left}\\{style.border_right}",
                f"{style.border_left}|{style.border_right}",
                f"{style.border_left}/{style.border_right}"
            ]
        )


    @staticmethod
    def plus(
            *,
            style : Any = Style("#", " ", "#", "#", "", "")
        ) -> Animation:
        """
            Plus spinner.

            Parameters:
                style (Style, optional): Style of the animations.

            Returns:
                Animation: Plus animation.
        """

        from jarbin_toolkit_console.Animation.animation import Animation

        return Animation(
            [
                f"{style.border_left}-{style.border_right}",
                f"{style.border_left}|{style.border_right}"
            ]
        )


    @staticmethod
    def cross(
            *,
            style : Any = Style("#", " ", "#", "#", "", "")
        ) -> Animation:
        """
            Cross spinner.

            Parameters:
                style (Style, optional): Style of the animations.

            Returns:
                Animation: Cross animation.
        """

        from jarbin_toolkit_console.Animation.animation import Animation

        return Animation(
            [
                f"{style.border_left}/{style.border_right}",
                f"{style.border_left}\\{style.border_right}"
            ]
        )


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Animation.Spinner: created")
