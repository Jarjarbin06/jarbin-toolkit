#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###    ----text.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any
from jarbin_toolkit_console.Text.format import Format
from jarbin_toolkit_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Text.Text: imported")


class Text(Format):
    """
        Text class.

        Text tool.
    """


    def __init__(
            self,
            text : list[Any | str] | Any | str = ""
        ) -> None:
        """
            Create a text.

            Parameters:
                text (list[Any | str] | ANSI | str, optional): text
        """

        from jarbin_toolkit_console.ANSI.ansi import ANSI

        self.text : str = ""

        if type(text) in [list]:
            for item in text:
                self.text += str(item)

        elif type(text) in [ANSI]:
            self.text = text.sequence

        else :
            self.text = str(text)


    def __add__(
            self,
            other : Any | str
        ) -> Any:
        """
            Add 2 Texts together.

            Parameters:
                other (ANSI | Text | str): text

            Returns:
                Text: text
        """

        return Text(str(self) + str(other))


    def __mul__(
            self,
            other : int
        ) -> Any:
        """
            Multiply Text sequences.
        """

        return Text(str(self) * other)


    def __str__(
            self
        ) -> str :
        """
            Convert Text object to string.

            Returns:
                str: Text string
        """

        return str(self.text)


    def __len__(
            self
        ) -> int:
        """
            Get length of Text object.

            Returns:
                int: Length of Text object
        """

        return len(self.text)


    def __repr__(
            self
        ) -> str:
        """
            Convert Text object to string.

            Returns:
                str: Text string
        """

        return f"Text({repr(self.text)})"


    @staticmethod
    def url_link(
            url: str,
            text: str | None = None
        ) -> Any:
        """
            Get url link to line 'line' of the file 'path' (may not work in IDE's console).

            Parameters:
                url (str): URL to website.
                text (int, optional): Text to show instead of the url (show the url if no text).

            Returns:
                str: url link.
        """

        if not text:
            text = url

        return Text(f'\033]8;;{url}\033\\{text}\033]8;;\033\\')


    @staticmethod
    def file_link(
            path: str,
            line: int | None = None
        ) -> Any:
        """
            Get file link to line 'line' of the file 'path' (needs CLion from JetBrains to work).

            Parameters:
                path (str): Path to the file.
                line (int, optional): Line of the file.

            Returns:
                str: file link.
        """

        if line:
            return Text(f'\033]8;;jetbrains://clion/navigate/reference?file={path}&line={line}\033\\File "{path}", line {line}\033]8;;\033\\')
        else:
            return Text(f'\033]8;;jetbrains://clion/navigate/reference?file={path}\033\\File "{path}"\033]8;;\033\\')


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Text.Text: created")
