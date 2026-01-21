#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###  ----animation.py---- ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any
from jarbin_toolkit_console.Text.format import Format
from jarbin_toolkit_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Animation.Animation: imported")


class Animation(Format):
    """
        Animation class.

        Animation tool.
    """


    from jarbin_toolkit_console.ANSI.color import Color


    def __init__(
            self,
            animation : list[Any] | str = ""
        ) -> None:
        """
            Create an animation.

            Parameters:
                animation (list[str] | str, optional): list of step
        """

        ## cannot be tested with pytest ##

        if not isinstance(animation, (list, str)): # pragma: no cover
            from jarbin_toolkit_console.Error.error import ErrorType # pragma: no cover
            from jarbin_toolkit_console import quit # pragma: no cover

            if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("ERROR", "type", f"Animation.Animation.__init__: animation is of an unsupported type (supported: list[Any], str ; current: {type(animation)})") # pragma: no cover
            quit() # pragma: no cover
            raise ErrorType(link=(f"{Setting.S_PACKAGE_PATH}Animation/animation", 36)) from None # pragma: no cover

        self.animation : list[str] = []

        if isinstance(animation, list):
            for step in animation:
                self.animation.append(str(step))

        else:
            self.animation = animation.split("\\")

        self.length : int = len(self.animation)
        self.step : int = 0


    def __add__(
            self,
            other : Any | str
        ) -> Any:
        """
            Add 2 Animations together.

            Parameters:
                other (Animation | ANSI | Text | StopWatch | str): Animation

            Returns:
                Animation: Animation
        """

        from jarbin_toolkit_console.Text.text import Text
        from jarbin_toolkit_console.ANSI.ansi import ANSI
        from jarbin_toolkit_console.System.stopwatch import StopWatch

        ## cannot be tested with pytest ##

        if not isinstance(other, (Animation, ANSI, Text, StopWatch, str)): # pragma: no cover
            from jarbin_toolkit_console.Error.error import ErrorType # pragma: no cover
            from jarbin_toolkit_console import quit # pragma: no cover

            if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("ERROR", "type", f"Animation.Animation.__add__: other is of an unsupported type (supported: Animation, ANSI, Text, StopWatch, str ; current: {type(other)})") # pragma: no cover
            quit() # pragma: no cover
            raise ErrorType() from None # pragma: no cover

        if type(other) in [Animation]:
            return Animation(self.animation + other.animation)

        elif type(other) in [Text, StopWatch, ANSI, str]:
            return Animation(self.animation + [str(other)])

        ## cannot be tested with pytest ##

        else:
            return Animation([]) # pragma: no cover


    def __getitem__(
            self,
            item : int
        ) -> str :
        """
            Get the current step of the animation and convert it to a string.

            Returns:
                str: Animation string
        """

        ## cannot be tested with pytest ##

        if not isinstance(item, int): # pragma: no cover
            from jarbin_toolkit_console.Error.error import ErrorType # pragma: no cover
            from jarbin_toolkit_console import quit # pragma: no cover

            if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("ERROR", "type", f"Animation.Animation.__getitem__: item is of an unsupported type (supported: int ; current: {type(item)})") # pragma: no cover
            quit() # pragma: no cover
            raise ErrorType() from None # pragma: no cover

        if self.is_last():
            return str(self.animation[self.length - 1])

        return str(self.animation[item])


    def __str__(
            self,
            *,
            color : Any = Color(Color.C_RESET)
        ) -> str :
        """
            Convert Animation object to string.

            Parameters:
                color (ANSI, optional): Color

            Returns:
                str: Animation string
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI
        from jarbin_toolkit_console.ANSI.color import Color

        ## cannot be tested with pytest ##

        if not isinstance(color, ANSI): # pragma: no cover
            if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("WARN", "type", f"Animation.Animation.__str__: color is of an unsupported type (supported: ANSI ; current: {type(color)})") # pragma: no cover

        return f"{color}{str(self[self.step])}{Color(Color.C_RESET)}"


    def __call__(
            self,
        ) -> None:
        """
            Do a step of the animation.
        """

        self.update()


    def __len__(
            self
        ) -> int:
        """
            Return the number of steps of the animation.

            Returns:
                int: Number of steps
        """

        return self.length


    def update(
            self,
            *,
            auto_reset: bool = True
        ) -> None:
        """
            Add a step to the animation.

            Parameters:
                auto_reset (bool, optional): Automatically reset the animation. Defaults to False.
        """

        ## cannot be tested with pytest ##

        if not isinstance(auto_reset, bool): # pragma: no cover
            if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("WARN", "type", f"Animation.Animation.update: auto_reset is of an unsupported type (supported: bool ; current: {type(auto_reset)})") # pragma: no cover

        self.step += 1

        if self.is_last() and auto_reset:
            self.reset()


    def render(
            self,
            *,
            color : Any = Color(Color.C_RESET),
            delete : bool = False
        ) -> str:
        """
            Convert Animation object to string.

            Parameters:
                color (ANSI | int, optional): Color to render in.
                delete (bool, optional): Delete the previous animation. Defaults to False.

            Returns:
                str: Animation string
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI
        from jarbin_toolkit_console.ANSI.cursor import Cursor
        from jarbin_toolkit_console.ANSI.color import Color

        ## cannot be tested with pytest ##

        if not isinstance(color, (ANSI, int)): # pragma: no cover
            if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("WARN", "type", f"Animation.Animation.render: color is of an unsupported type (supported: ANSI, int ; current: {type(color)})") # pragma: no cover

        if not isinstance(delete, bool): # pragma: no cover
            if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("WARN", "type", f"Animation.Animation.render: delete is of an unsupported type (supported: bool ; current: {type(delete)})") # pragma: no cover

        if type(color) == int:
            color = Color(color)

        string : str = ""

        string += self.__str__(color=color) + str(Color(Color.C_RESET))

        if delete:
            string += str(Cursor.up() + Cursor.move_column(0))

        return string


    def is_last(
            self
        ) -> bool:
        """
            Return whether it is or not the last step of the animation.

            Returns:
                bool: is the last step
        """

        return self.step >= self.length


    def reset(
            self
        ) -> None:
        """
            Reset the animation.
        """

        self.step = 0


    def __repr__(
            self
        ) -> str:
        """
            Convert Animation object to string.

            Returns:
                str: Animation string
        """

        return f"Animation({repr(self.animation)})"


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Animation.Animation: created")
