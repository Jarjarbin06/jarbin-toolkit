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
            file_name : str | None = None,
            json : bool = False
        ) -> None:
        """
            Log class constructor.

            Parameters:
                path (str): path to log file
                file_name (str | None, optional): name of log file
                json (bool, optional): switch from log file to JSON file
        """

        from datetime import datetime
        from platform import system

        self.log_path : str = (path if path[-1] in ["/", "\\"] else path + ("\\" if system() == "Windows" else "/"))
        self.log_file_name : str = str(datetime.now()).replace(":", "_") if not file_name else file_name
        self.log_file_type : str = "json" if json else "jar-log"

        try:
            open(f"{self.log_path}{self.log_file_name}.{self.log_file_type}", 'x').close()

            with open(f"{self.log_path}{self.log_file_name}.{self.log_file_type}", 'a') as log_file:
                if self.log_file_type == "jar-log" :
                    log_file.write("   date          time      | [TYPE]  title      | detail\n\n---START---")
                elif self.log_file_type == "json":
                    log_file.write(
                        "{\n    \"file_name\": \"" + f"{self.log_file_name}.{self.log_file_type}" +
                        "\",\n    \"logs\":\n    [")
            log_file.close()

            self.closed : bool = False


        ## cannot be tested with pytest ##

        except FileNotFoundError as error: # pragma: no cover
            raise error # pragma: no cover

        except FileExistsError:
            self.closed : bool = True

        if not self.closed:
            try:
                with open(f"{self.log_path}{self.log_file_name}.{self.log_file_type}", 'r') as log_file:
                    string = log_file.read()
                log_file.close()

                if self.log_file_type == "jar-log":
                    assert "   date          time      | [TYPE]  title      | detail\n\n---START---" in string

                elif self.log_file_type == "json":
                    assert ("{\n    \"file_name\": \"" + f"{self.log_file_name}.{self.log_file_type}" +
                            "\",\n    \"logs\":\n    [" in string)

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

        if not self.closed:
            if self.log_file_type == "jar-log":
                status = f"[{status}]"
                status += " " * 7
                status = status[:7]
                title += " " * (10 - len(title))
                title = title[:10]

            log_time : str = str(datetime.now())
            log_str: str = ""

            if self.log_file_type == "jar-log":
                log_str = f"{log_time} | {status} {title} | {description}"
            elif self.log_file_type == "json":
                log_str = (
                        "\n        {\n            \"time\": \"" +log_time +
                        "\",\n            \"level\": \"" + status +
                        "\",\n            \"title\": \"" + title +
                        "\",\n            \"msg\": \"" + description +
                        "\"\n        },")

            self.save(log_str)


    def comment(
            self,
            comment : str
        ) -> None:
        """
            Save a comment in the log file.

            (does not work with json files yet)


            Parameters:
                comment (str): comment
        """

        if not self.closed:
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

        if not self.closed:
            with open(f"{self.log_path}{self.log_file_name}.{self.log_file_type}", 'a') as log_file :
                log_file.write(f"\n{log_str}" if self.log_file_type == "jar-log" else log_str)
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

        if not self.closed:
            if self.log_file_type == "jar-log":
                with open(f"{self.log_path}{self.log_file_name}.{self.log_file_type}", 'a') as log_file :
                    log_file.write(f"\n----END----\n")
                log_file.close()

            elif self.log_file_type == "json":
                string : str = self.read()[:-1]

                with open(f"{self.log_path}{self.log_file_name}.{self.log_file_type}", 'w') as log_file:
                    log_file.write(string + "\n    ]\n}")
                log_file.close()

            self.closed = True

            if delete :
                self.delete()


    def delete(
            self
        ) -> None:
        """
            Delete the log file.
        """

        from os import remove

        remove(f"{self.log_path}{self.log_file_name}.{self.log_file_type}")


    def read(
            self
        ) -> str :
        """
            Read the log file and returns its content.

            Returns:
                str: content of the log file
        """

        log_str : str = ""

        with open(f"{self.log_path}{self.log_file_name}.{self.log_file_type}", 'r') as log_file:
            log_str = log_file.read()
        log_file.close()

        return log_str


    def __str__(
            self,
            filter : list[str] | str | None = None
        ) -> str :
        """
            Returns a formated log file.

            Parameters:
                filter (list[str] | str | None, optional): filter

            Return:
                str: formated log string
        """

        log_str = self.read()

        if self.log_file_type == "jar-log":
            return self._jar_log_str(filter)

        elif self.log_file_type == "json":
            return self._json_str(filter)

        return log_str


    def _jar_log_str(
            self,
            filter : list[str] | str | None = None
        ) -> str:
        """
            Returns a formated jar-log file.

            Parameters:
                filter (list[str] | str | None, optional): filter

            Return:
                str: formated log string
        """

        from os import get_terminal_size
        from sys import stdin

        log_str = self.read()

        color_dict: dict[str, tuple[str, str]] = {
            "[INFO] ": ("\x1b[7m", "\x1b[0m"),
            "[VALID]": ("\x1b[42m", "\x1b[32m"),
            "[WARN] ": ("\x1b[43m", "\x1b[33m"),
            "[ERROR]": ("\x1b[41m", "\x1b[31m")
        }
        start: int = log_str.index("---START---\n") + len("---START---\n")
        end: int = log_str.index("----END----\n")
        logs: list = [lines.split(" | ") for lines in log_str[start:end].splitlines()]
        t_size = get_terminal_size().columns if stdin.isatty() else 100
        footer: str = f"\x1b[4m\x1b[7m|\x1b[0m\x1b[1m\x1b[4m"
        detail_size: int
        string: str = ""

        string += f"JAR-LOG\n\n"
        string += (
                f"\x1b[4m\x1b[7m|\x1b[0m\x1b[1m\x1b[4m    date          time      | \x1b[0m" +
                "\x1b[4m\x1b[7m[TYPE] \x1b[0m\x1b[1m\x1b[4m title      | detail" +
                (" " * (t_size - 58)) + f"\x1b[0m\n")
        string += f"\x1b[7m|\x1b[0m\x1b[1m" + (" " * (t_size - 1)) + f"\x1b[0m\n"

        for log_line in logs:
            if not filter or log_line[0].replace(" ", "")[1:-1] in filter:
                if log_line[0][:3] == ">>>":
                    string += f"\x1b[7m>>>\x1b[0m \x1b[0m{log_line[0][3:]}\x1b[0m\n"

                else:
                    if len(log_line) == 3 and log_line[1][:7].upper() in color_dict:
                        color = color_dict[log_line[1][:7].upper()]
                        string += (
                                f"{color[0]}|\x1b[0m " +
                                f"{color[1]}{log_line[0]}\x1b[0m | " +
                                f"{color[0]}{log_line[1][0:7]}\x1b[0m " +
                                f"{color[1]}\x1b[1m{log_line[1][8:]}\x1b[0m | " +
                                (
                                    f"{log_line[2][:(t_size - 1)]}..." if len(log_line[2]) > (t_size - 1) else
                                    f"{color[1]}{log_line[2]}") + f"\x1b[0m\n")

                    ## cannot be tested with pytest ##

                    elif len(log_line) == 1:  # pragma: no cover
                        string += f"\x1b[44m|\x1b[0m " + f"\x1b[34mUNFORMATTED\n\"{log_line[0]}\"\x1b[0m\n"  # pragma: no cover

        string += footer + (" " * (t_size - 1)) + f"\x1b[0m"

        return string


    def _json_str(
            self,
            filter : list[str] | str | None = None
        ) -> str:
        """
            Returns a formated json file.

            Parameters:
                filter (list[str] | str | None, optional): filter

            Return:
                str: formated log string
        """

        import json

        log_str = self.read()
        parsed_json : list = json.loads(log_str)
        string : str = ""

        string += f"JSON => {parsed_json["file_name"]}"
        string += f"\n{'=' * 50}\n"
        for log_line in parsed_json["logs"]:
            if not filter or log_line["level"] in filter:
                string += f"{log_line["time"]} | {(log_line["level"] + (" " * 5))[:5]} {(log_line["title"] + (" " * 10))[:10]} | {log_line["msg"]}\n"
        string += f"{'=' * 50}"

        return string


    def str_filtered(
            self,
            f : list[str] | str
        ) -> str:
        """
            Returns a formated and filtered log file.

            Parameters:
                f (list[str] | str): filter

            Return:
                str: formated log string
        """

        if isinstance(f, list):
            for index in range(len(f)):
                f[index] = f[index].upper()

        else:
            f = f.upper()

        return self.__str__(f)


    def __repr__(
            self
        ) -> str:
        """
            Convert Log object to string.

            Returns:
                str: Log string
        """

        return f"Log({repr(self.log_path)}, {repr(self.log_file_name)}, {repr(True if self.log_file_type == 'json' else False)})"
