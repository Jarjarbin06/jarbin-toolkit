#############################
###                       ###
###     Jarbin-ToolKit    ###
###         error         ###
### ----base_error.py---- ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class BaseError(Exception):
    """
    BaseError class for pretty printed error handling.
    """


    def __init__(
            self,
            message : str = "an error occurred",

            *,
            error : str = "Error",
            link : tuple[str , int | None] | None = None
        ) -> None:
        """
            Create an Error.

            Parameters:
                message (str, optional): The error message.
                error (str, optional): The error type (title).
                link (tuple[str, int | None] | None, optional): The link to where the error comes from (file and line).
        """

        self.message : str = message
        self.error : str = error
        self.link_data : tuple[str, int | None] | None = link
        self.link : str | None = None

        self.create_link()


    def log(
            self
        ) -> None:
        """
            Log the error.
        """

        pass

        """from epitech_console.System.setting import Setting

        Setting.update()

        if Setting.S_SETTING_LOG_MODE:

            ## cannot be tested with pytest ##

            Setting.S_LOG_FILE.log("ERROR", "error", f"\"{self.error}\": {self.message}") # pragma: no cover

            if self.link_data: # pragma: no cover
                if self.link_data[1] is None: # pragma: no cover
                    Setting.S_LOG_FILE.comment(f"A file as been linked to the previous error:") # pragma: no cover
                    Setting.S_LOG_FILE.comment(f"\"{self.link_data[0]}\"") # pragma: no cover

                else: # pragma: no cover
                    Setting.S_LOG_FILE.comment(f"A file and line number as been linked to the previous error:") # pragma: no cover
                    Setting.S_LOG_FILE.comment(f"\"{self.link_data[0]}\" line {self.link_data[1]}") # pragma: no cover"""


    def create_link(
            self
        ) -> None:
        """
            Create an error link.
            Create an error link.
        """

        #from epitech_console.Text.text import Text

        if self.link_data:
            if self.link_data[1] is None:
                self.link = f"File \"{self.link_data[0]}\""

            elif self.link_data[1] > 0:
                self.link = f"File \"{self.link_data[0]}\", line {self.link_data[1]}"

            #if self.link_data[1] is None:
            #    self.link = str(Text.file_link(self.link_data[0]))

            #else:
            #    if self.link_data[1] > 0:
            #        self.link = str(Text.file_link(self.link_data[0], self.link_data[1]))


    @staticmethod
    def lauch_error(
        ) -> str:
        """
            Returns lauch error message.

            Return:
                str: Lauch error message.
        """

        ## cannot be tested with pytest ##

        return (
            f"\x1b[103m \x1b[0m \x1b[93mjarbin_toolkit_console launched with error\x1b[0m\n"
            f"\x1b[103m \x1b[0m\n"
            f"\x1b[103m \x1b[0m \x1b[93mPlease reinstall with :\x1b[0m\n"
            f"\x1b[103m \x1b[0m \x1b[93m    'pip install --upgrade --force-reinstall jarbin_toolkit_console'\x1b[0m\n"
            f"\x1b[103m \x1b[0m\n"
            f"\x1b[103m \x1b[0m \x1b[93mPlease report the issue here : https://github.com/Jarjarbin06/jarbin_toolkit/issues\x1b[0m\n"
        ) # pragma: no cover


    def __str__(
            self,
        ) -> str:
        """
            Get string representation of the error.

            Returns:
                str: String representation of the error.
        """

        error: str | None = self.error
        message: str = self.message

        string: str = ""
        if error and error.startswith("\n"):
            string = "\n"
        if message.startswith("\n"):
            message = message[1:]
            string = "\n"
        string += "\x1b[101m \x1b[0m \x1b[91m"
        string += (error or "ErrorUnknown").replace("\n", "")
        string += (":" if len(message) > 0 else "")

        if len(message) > 0:
            for line in message.splitlines():
                string += "\n\x1b[101m \x1b[0m     \x1b[91m"
                string += line

        string += ("\n\x1b[101m \x1b[0m \x1b[91m" + f"\n\x1b[101m \x1b[0m\n\x1b[101m \x1b[0m  \x1b[91m" + str(self.link)) if self.link else ""

        return string


    def __repr__(
            self
        ) -> str:
        """
            Convert Error object to string.

            Returns:
                str: Error string
        """

        name = type(self).__name__
        message = self.message
        error = self.error
        link_data = self.link_data

        return f"{name}({message=!r}, {error=!r}{f', {link_data=!r}' if self.link else ''})"
