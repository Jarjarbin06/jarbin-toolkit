#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
### ----progressbar.py----###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any
from jarbin_toolkit_console.Text.format import Format
from jarbin_toolkit_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Animation.ProgressBar: imported")


class ProgressBar(Format):
    """
        ProgressBar class.

        Progress-bar tool.
    """

    from jarbin_toolkit_console.Animation.animation import Animation
    from jarbin_toolkit_console.ANSI.color import Color
    from jarbin_toolkit_console.Animation.style import Style


    def __init__(
            self,
            length : int,

            *,
            animation : Animation | None = None,
            style : Any = Style("#", "-", "<", ">", "|", "|"),
            percent_style : str = "bar",
            spinner : Animation | None = None,
            spinner_position : str = "a"
        ) -> None:
        """
            Create a Progress-bar object.

            Parameters:
                length (int): Progress bar length.

                animation (Animation | None, optional): Animation object.
                style (Style | None, optional): Progress bar style.
                percent_style (str, optional): Progress bar percent style (num/bar/mix).
                spinner (Animation | None, optional): Progress bar spinner.
                spinner_position (str, optional): Progress bar spinner position (b/a).
        """

        from jarbin_toolkit_console.Animation.animation import Animation
        from jarbin_toolkit_console.Animation.style import Style

        def create_progress_bar(
                new_length : int,
                new_style : Style
            ) -> list[str]:
            """
                Create the Progress-bar animation.

                Parameters:
                    new_length (int): Progress bar length.
                    new_style (Style): Progress bar style.

                Returns:
                    list[str]: Progress bar animation.
            """

            new_animation: list[str] = []

            for y in range(new_length):
                new_animation += [new_style.border_left]

                for x in range(y):
                    new_animation[y] += new_style.on

                new_animation[y] += new_style.arrow_right

                for x in range((new_length - y) - 1):
                    new_animation[y] += new_style.off

                new_animation[y] = new_animation[y][0:-1] + new_style.border_right

            return new_animation

        if not animation :
            animation = Animation(create_progress_bar(length + 1, style))

        self.length = length
        self.animation : Animation = animation
        self.style : Style = style
        self.percent : int | float = 0
        self.percent_style : str = percent_style
        self.spinner : Animation | None = spinner
        self.spinner_position : str = spinner_position


    def __getitem__(
            self,
            item : int,
            *,
            color : Any = Color(Color.C_RESET)
        ) -> str :
        """
            Get the current step of the animations and convert it to a string.

            Parameters:
                item (int): Step number
                color (ANSI, optional): Color

            Returns:
                str: Animations string
        """

        from jarbin_toolkit_console.ANSI.color import Color

        return str(color + self.animation[item] + str(Color(Color.C_RESET)))


    def __str__(
            self,
            *,
            color : tuple[Any, Any, Any] = (Color(Color.C_RESET), Color(Color.C_RESET), Color(Color.C_RESET)),
            hide_spinner : bool = False
        ) -> str :
        """
            Convert ProgressBar object to string.

            Parameters:
                color (tuple[ANSI, ANSI, ANSI], optional): Color
                hide_spinner (bool, optional): hide the spinner

            Returns:
                str: ProgressBar string
        """

        from jarbin_toolkit_console.ANSI.color import Color

        string : str = ""

        if self.spinner and self.spinner_position == "b" and not hide_spinner :
            string += self.spinner.__str__(color=color[1])

        if self.percent_style in ["bar", "mix"] :
            idx : int = int((self.percent / 100) * self.length)

            if idx >= self.length:
                idx = self.length

            string += self.__getitem__(idx, color=color[0])

        if self.spinner and self.spinner_position == "a" and not hide_spinner :
            string += self.spinner.__str__(color=color[1])

        if self.percent_style in ["num", "mix"] :
            string += f" {color[2]}{str(self.percent)}%{Color(Color.C_RESET)}"

        return string


    def __call__(
            self
        ) -> None:
        """
            Do a step of the animations.
        """

        self.update(self.percent + 1)


    def update(
            self,
            percent : int = 0,
            *,
            update_spinner : bool = True,
            auto_reset: bool = True
        ) -> None:
        """
            Do a step of the animations.

            Parameters:
                percent (int, optional): Percentage
                update_spinner (bool, optional): Update spinner
                auto_reset (bool, optional): Auto reset spinner
        """

        if self.spinner and update_spinner :
            self.spinner.update(auto_reset=auto_reset)

        if percent > 100:
            percent = 100

        self.percent = percent


    def render(
            self,
            *,
            color : Any | tuple[Any, Any, Any] = Color(Color.C_RESET),
            hide_spinner_at_end: bool = True,
            delete : bool = False
        ) -> Any:
        """
            Convert ProgressBar object to string.

            Parameters:
                color (ANSI | tuple[ANSI, ANSI, ANSI], optional): Color
                hide_spinner_at_end (bool, optional): Hide spinner at end
                delete (bool, optional): Delete previous line and right on it

            Returns:
                str: ProgressBar string
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI
        from jarbin_toolkit_console.ANSI.line import Line
        from jarbin_toolkit_console.Text.text import Text

        string : str = ""

        if type(color) not in [tuple]:
            color : tuple[Any, Any, Any] = (ANSI(color), ANSI(color), ANSI(color))

        string += str(self.__str__(color=color, hide_spinner=(hide_spinner_at_end and self.percent == 100)))

        if delete:
            string += str(Line.clear_previous_line())

        return Text(string)


    def __repr__(
            self
        ) -> str:
        """
            Convert ProgressBar object to string.

            Returns:
                str: ProgressBar string
        """

        return f"ProgressBar({repr(self.length)}, animation=[{repr(self.animation[0])}, ..., {repr(self.animation[-1])}], style={repr(self.style)}, percent_style={repr(self.percent_style)}, spinner={repr(self.spinner)}, spinner_position={repr(self.spinner_position)})"


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Animation.ProgressBar: created")
