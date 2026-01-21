#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###   ----format.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


from jarbin_toolkit_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Text.Format: imported")


class Format:
    """
        Format class.

        Format tool.
    """


    def reset(
            self
        ) -> Any:
        """
            Apply the 'reset' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                Any: formatted object.
        """

        from jarbin_toolkit_console.ANSI.color import Color

        return Format.apply(self, Color(Color.C_RESET))



    def bold(
            self
        ) -> Any:
        """
            Apply the 'bold' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                Any: formatted object.
        """

        from jarbin_toolkit_console.ANSI.color import Color

        return Format.apply(self, Color(Color.C_BOLD))


    def italic(
            self
        ) -> Any:
        """
            Apply the 'italic' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                Any: formatted object.
        """
        from jarbin_toolkit_console.ANSI.color import Color

        return Format.apply(self, Color(Color.C_ITALIC))


    def underline(
            self
        ) -> Any:
        """
            Apply the 'underline' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                Any: formatted object.
        """

        from jarbin_toolkit_console.ANSI.color import Color

        return Format.apply(self, Color(Color.C_UNDERLINE))


    def hide(
            self
        ) -> Any:
        """
            Apply the 'hide' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                Any: formatted object.
        """

        from jarbin_toolkit_console.ANSI.color import Color

        return Format.apply(self, Color(Color.C_HIDDEN))


    def strikethrough(
            self
        ) -> Any:
        """
            Apply the 'strikethrough' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                Any: formatted object.
        """

        from jarbin_toolkit_console.ANSI.color import Color

        return Format.apply(self, Color(Color.C_STRIKETHROUGH))


    def error(
            self,
            *,
            title : bool = False
        ) -> Any:
        """
            Apply the 'error' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Parameters:
                title (bool, optional): whether it is a title or not

            Returns:
                Any: formatted object.
        """

        from jarbin_toolkit_console.ANSI.color import Color
        from jarbin_toolkit_console.ANSI.basepack import BasePack

        if title:
            return Format.apply(self, Color(BasePack.P_ERROR[0]))
        return Format.apply(self, Color(BasePack.P_ERROR[1]))


    def warning(
            self,
            *,
            title : bool = False
        ) -> Any:
        """
            Apply the 'warning' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Parameters:
                title (bool, optional): whether it is a title or not

            Returns:
                Any: formatted object.
        """

        from jarbin_toolkit_console.ANSI.color import Color
        from jarbin_toolkit_console.ANSI.basepack import BasePack

        if title:
            return Format.apply(self, Color(BasePack.P_WARNING[0]))
        return Format.apply(self, Color(BasePack.P_WARNING[1]))


    def valid(
            self,
            *,
            title : bool = False
        ) -> Any:
        """
            Apply the 'ok' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Parameters:
                title (bool, optional): whether it is a title or not

            Returns:
                Any: formatted object.
        """

        from jarbin_toolkit_console.ANSI.color import Color
        from jarbin_toolkit_console.ANSI.basepack import BasePack

        if title:
            return Format.apply(self, Color(BasePack.P_VALID[0]))
        return Format.apply(self, Color(BasePack.P_VALID[1]))


    def info(
            self,
            *,
            title : bool = False
        ) -> Any:
        """
            Apply the 'info' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Parameters:
                title (bool, optional): whether it is a title or not

            Returns:
                Any: formatted object.
        """

        from jarbin_toolkit_console.ANSI.color import Color
        from jarbin_toolkit_console.ANSI.basepack import BasePack

        if title:
            return Format.apply(self, Color(BasePack.P_INFO[0]))
        return Format.apply(self, Color(BasePack.P_INFO[1]))


    @staticmethod
    def apply(
            obj : Any,
            sequence : Any | None = None
        ) -> Any:
        """
            Apply a format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Parameters:
                obj (Text | ANSI | Animation | ProgressBar | str): object to be formatted.
                sequence (ANSI, optional): format.

            Returns:
                Any: formatted object.
        """

        from jarbin_toolkit_console.ANSI.color import Color
        from jarbin_toolkit_console.Text.text import Text
        from jarbin_toolkit_console.ANSI.ansi import ANSI
        from jarbin_toolkit_console.Animation.animation import Animation
        from jarbin_toolkit_console.Animation.progressbar import ProgressBar

        if not sequence:
            sequence: ANSI = Color(Color.C_RESET)

        if type(obj) in [str]:
            return str(sequence) + str(obj)

        if type(obj) in [Text]:
            return Text(str(sequence) + str(obj))

        if type(obj) in [ANSI]:
            return ANSI(str(sequence) + str(obj))

        if type(obj) in [Animation]:
            animation : list[str] = [(str(sequence) + str(line)) for line in obj.animation]
            return Animation(animation)

        if type(obj) in [ProgressBar]:
            animation : Animation = Animation([(str(sequence) + str(line)) for line in obj.animation])
            spinner : Animation | None = None
            if obj.spinner:
                spinner: Animation = Animation([(str(sequence) + str(line)) for line in obj.spinner])
            return ProgressBar(obj.length, animation=animation, style=obj.style, percent_style=obj.percent_style,  spinner=spinner, spinner_position=obj.spinner_position)

        else:
            return obj


    @staticmethod
    def tree(
            d : dict | str | list,
            title : str | None = None,
            indent : int = 0
        ) -> str:
        """
            Format a dict into a tree (bash) formatted string.

            Parameters:
                d (dict | str | list): dictionary to be formatted
                title (str | None, optional): the title of the tree
                indent (int, optional): indent level

            Returns:
                str: formatted string.
        """

        string : str = ((title + "/\n") if title else "")

        if d is None:
            return string

        elif type(d) == str:
            string += ("│   " * indent) + "├── " + d + "\n"

        elif type(d) == list:
            for line in d:
                string += ("│   " * indent) + "├── " + line + "\n"

        else :
            for key in d:
                string += ("│   " * indent) + "├── " + key + "/\n"
                string += Format.tree(d[key], None, indent + 1) + "\n"

        return string[:-1]

    @staticmethod
    def module_tree(
        ) -> str:
        """
            Get the module's tree.

            Returns:
                str: formatted string.
        """

        return Format.tree(
            {
                "Text": [
                    "Text",
                    "Format"
                ],
                "Animation": [
                    "Animation",
                    "BasePack",
                    "ProgressBar",
                    "Spinner",
                    "Style"
                ],
                "ANSI": [
                    "ANSI",
                    "BasePack",
                    "Color",
                    "Cursor",
                    "Line"
                ],
                "System": [
                    "Console",
                    "Setting"
                ]
            },
            "jarbin_toolkit_console")


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Text.Format: created")
