#############################
###                       ###
###    Epitech Console    ###
###     ----log.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


class Log:
    """
        Log class.

        Log file tool.
    """


    def __init__(
            self,
            path : str,
            file_name : str | None = None
        ) -> None:
        """
            Log class constructor.

            Parameters:
                path (str): path to log file
                file_name (str | None, optional): name of log file
        """

        from datetime import datetime
        from platform import system

        self.log_path : str = (path if path[-1] in ["/", "\\"] else path + ("\\" if system() == "Windows" else "/"))
        self.log_file_name : str = str(datetime.now()).replace(":", "_") if not file_name else file_name

        try :
            open(f"{self.log_path}{self.log_file_name}.log", 'x').close()

            with open(f"{self.log_path}{self.log_file_name}.log", 'a') as log_file:
                log_file.write("   date          time      | [TYPE]  title      | detail\n\n---START---")
            log_file.close()


        ## cannot be tested with pytest ##

        except FileNotFoundError as error: # pragma: no cover
            raise error # pragma: no cover

        except FileExistsError:
            pass

        try :
            with open(f"{self.log_path}{self.log_file_name}.log", 'r') as log_file:
                string = log_file.read()
            log_file.close()

            assert "   date          time      | [TYPE]  title      | detail\n\n---START---" in string

        ## cannot be tested with pytest ##

        except FileNotFoundError or AssertionError as error: # pragma: no cover
            raise error # pragma: no cover


    def log(
            self,
            status : str,
            title : str,
            description : str
        ) -> None:
        """
            Format a log message then save it.

            Parameters:
                status (str): log status
                title (str): log title
                description (str): log description
        """

        from datetime import datetime

        status = f"[{status}]"
        status += " " * (7 - len(status))
        status = status[:7]
        title += " " * (10 - len(title))
        title = title[:10]

        log_time : str = str(datetime.now())
        log_str : str = f"{log_time} | {status} {title} | {description}"

        self.save(log_str)


    def comment(
            self,
            comment : str
        ) -> None:
        """
            Save a comment in the log file.

            Parameters:
                comment (str): comment
        """

        self.save(f">>> {comment}")


    def save(
            self,
            log_str : str
        ) -> None:
        """
            Save a new log in the log file.

            Parameters:
                log_str (str): log string
        """

        with open(f"{self.log_path}{self.log_file_name}.log", 'a') as log_file :
            log_file.write(f"\n{log_str}")
        log_file.close()


    def close(
            self,
            *,
            delete : bool = False
        ) -> None :
        """
            Close the log file.

            Parameters:
                delete (bool, optional): delete the log file
        """

        with open(f"{self.log_path}{self.log_file_name}.log", 'a') as log_file :
            log_file.write(f"\n----END----\n")
        log_file.close()

        if delete :
            self.delete()


    def delete(
            self
        ) -> None:
        """
            Delete the log file.
        """

        from os import remove

        remove(f"{self.log_path}{self.log_file_name}.log")


    def read(
            self
        ) -> str :
        """
            Read the log file and returns its content.

            Returns:
                str: content of the log file
        """

        log_str : str = ""

        with open(f"{self.log_path}{self.log_file_name}.log", 'r') as log_file:
            log_str = log_file.read()
        log_file.close()

        return log_str


    def __str__(
            self
        ) -> str :
        """
            Returns a formated log file.
        """

        from os import get_terminal_size

        log_str = self.read()

        color_dict: dict[str, tuple[str, str]] = {
            "[INFO] " : ("\x1b[7m", "\x1b[0m"),
            "[VALID]" : ("\x1b[42m", "\x1b[32m"),
            "[WARN] " : ("\x1b[43m", "\x1b[33m"),
            "[ERROR]" : ("\x1b[41m", "\x1b[31m")
        }
        start : int = log_str.index("---START---\n") + len("---START---\n")
        end : int = log_str.index("----END----\n")
        logs : list = [lines.split(" | ") for lines in log_str[start:end].splitlines()]
        t_size = get_terminal_size().columns
        footer : str = f"\x1b[4m\x1b[7m|\x1b[0m\x1b[1m\x1b[4m"
        detail_size : int
        string : str = ""

        string += f"\x1b[4m\x1b[7m|\x1b[0m\x1b[1m\x1b[4m    date          time      | \x1b[0m\x1b[4m\x1b[7m[TYPE] \x1b[0m\x1b[1m\x1b[4m title      | detail" + (" " * (t_size - 58)) + f"\x1b[0m\n"
        string += f"\x1b[7m|\x1b[0m\x1b[1m" + (" " * (t_size - 1)) + f"\x1b[0m\n"

        for log_line in logs :
            if log_line[0][:3] == ">>>" :
                string += f"\x1b[7m>>>\x1b[0m \x1b[0m{log_line[0][3:]}\x1b[0m\n"

            else :
                if len(log_line) == 3 and log_line[1][:7].upper() in color_dict :
                    color = color_dict[log_line[1][:7].upper()]
                    string += (
                        f"{color[0]}|\x1b[0m " +
                        f"{color[1]}{log_line[0]}\x1b[0m | " +
                        f"{color[0]}{log_line[1][0:7]}\x1b[0m " +
                        f"{color[1]}\x1b[1m{log_line[1][8:]}\x1b[0m | " +
                        (f"{log_line[2][:(t_size - 1)]}..." if len(log_line[2]) > (t_size - 1) else f"{color[1]}{log_line[2]}") +
                        f"\x1b[0m\n")

                ## cannot be tested with pytest ##

                elif len(log_line) == 1: # pragma: no cover
                    string += f"\x1b[44m|\x1b[0m " + f"\x1b[34mUNFORMATTED\n\"{log_line[0]}\"\x1b[0m\n" # pragma: no cover

        string += footer + (" " * (t_size - 1)) + f"\x1b[0m\n"

        return string


    def __repr__(
            self
        ) -> str:
        """
            Convert Log object to string.

            Returns:
                str: Log string
        """

        return f"Log({repr(self.log_path)}, {repr(self.log_file_name)})"
