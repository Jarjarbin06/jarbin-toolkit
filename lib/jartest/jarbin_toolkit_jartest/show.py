#############################
###                       ###
###     Jarbin-ToolKit    ###
###        JarTest        ###
###    ----show.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


import inspect
from jarbin_toolkit_console import Console, ANSI
from jarbin_toolkit_error import BaseError


class Show:


    _current_test: str | None = None
    _current_test_number: int | None = None
    _printing: bool = False
    _show_output: bool | None = None


    _C = {
        "DIM": ANSI.Color(ANSI.Color.C_FG_DARK).s,
        "RESET": ANSI.Color(ANSI.Color.C_RESET).s,
        "TITLE": ANSI.Color.rgb_fg(255, 160, 0).s,
        "KEY": ANSI.Color.rgb_fg(255, 160, 0).s,
        "VALUE": ANSI.Color.rgb_fg(0, 255, 255).s,
        "TYPE": ANSI.Color.rgb_fg(100, 100, 255).s,
        "SUCCESS": ANSI.Color.rgb_fg(100, 255, 100).s,
        "WARNING": ANSI.Color.rgb_fg(255, 160, 0).s,
        "ERROR": ANSI.Color.rgb_fg(255, 100, 100).s,
        "CRITICAL": ANSI.Color.rgb_fg(255, 0, 255).s,
    }


    @staticmethod
    def _print(
            *values: object,
            end: str | None = None
        ) -> None:

        if not Show._show_output:
            return

        if end is None:
            end = Show._C["DIM"] + "│ \n" + Show._C["RESET"]

        stack = inspect.stack()

        jt_frame = next(
            (
                frame for frame in stack[1:]
                if frame.function.startswith("JT_")
            ),
            None
        )

        if jt_frame is None:
            return

        run_frame = next(
            (
                frame for frame in stack[1:]
                if frame.function == "run_test"
            ),
            None
        )

        if run_frame is None:
            return

        test_name = run_frame.frame.f_locals.get("test_name")

        test_obj = run_frame.frame.f_locals.get("test")

        jar_test = run_frame.frame.f_locals.get("self")

        if (
                test_name is None
                or test_obj is None
                or jar_test is None
        ):
            return

        test_number = list(jar_test.tests.keys()).index(test_name)

        # ------------------------------------------------------------
        # Open output section when entering a new test
        # ------------------------------------------------------------

        if Show._current_test != test_name:
            Show._current_test = test_name
            Show._current_test_number = test_number
            Show._printing = True

            width = 112

            title = (
                f"--- {test_number:03d} --- "
                f"{test_name.removeprefix('JT_')} --- output ---"
            )

            Console.print(
                Show._C["TITLE"]
                + title.center(width, "-"),
                separator=""
            )

        # ------------------------------------------------------------
        # Recursive formatter
        # ------------------------------------------------------------

        def _format(value: object, indent: int = 0) -> list[str]:

            prefix = " " * indent

            if isinstance(value, dict):

                if not value:
                    return [
                        prefix + Show._C["DIM"] + "{}" + Show._C["RESET"]
                    ]

                lines = [
                    prefix + Show._C["DIM"] + "{" + Show._C["RESET"]
                ]

                items = list(value.items())

                for index, (key, item) in enumerate(items):

                    item_lines = _format(
                        item,
                        indent + 4
                    )

                    key_line = (
                            " " * (indent + 4)
                            + Show._C["KEY"]
                            + repr(key)
                            + Show._C["RESET"]
                            + ": "
                            + item_lines[0].lstrip()
                    )

                    if len(item_lines) == 1:

                        if index < len(items) - 1:
                            key_line += ","

                        lines.append(key_line)

                    else:

                        lines.append(key_line)
                        lines.extend(item_lines[1:-1])

                        closing = item_lines[-1]

                        if index < len(items) - 1:
                            closing += ","

                        lines.append(closing)

                lines.append(
                    prefix + Show._C["DIM"] + "}" + Show._C["RESET"]
                )

                return lines

            if isinstance(value, (list, tuple)):

                if not value:
                    empty = "[]" if isinstance(value, list) else "()"

                    return [
                        prefix + Show._C["DIM"] + empty + Show._C["RESET"]
                    ]

                opening = "[" if isinstance(value, list) else "("
                closing = "]" if isinstance(value, list) else ")"

                lines = [
                    prefix + Show._C["DIM"] + opening + Show._C["RESET"]
                ]

                for index, item in enumerate(value):

                    item_lines = _format(
                        item,
                        indent + 4
                    )

                    first = item_lines[0].lstrip()

                    line = (
                            " " * (indent + 4)
                            + Show._C["DIM"]
                            + f"{index:03d}"
                            + Show._C["RESET"]
                            + " │ "
                            + first
                    )

                    if len(item_lines) == 1:

                        if index < len(value) - 1:
                            line += ","

                        lines.append(line)

                    else:

                        lines.append(line)
                        lines.extend(item_lines[1:-1])

                        closing_line = item_lines[-1]

                        if index < len(value) - 1:
                            closing_line += ","

                        lines.append(closing_line)

                lines.append(
                    prefix + Show._C["DIM"] + closing + Show._C["RESET"]
                )

                return lines

            return [
                prefix
                + Show._C["VALUE"]
                + str(value)
                + Show._C["RESET"]
            ]

        # ------------------------------------------------------------
        # Print
        # ------------------------------------------------------------

        lines = []

        for value in values:
            if isinstance(value, str):
                for line in value.split("\n"):
                    lines.extend(
                        _format(line)
                    )

            else:
                lines.extend(
                    _format(value)
                )

        Console.print(
            Show._C["DIM"] + "│ " + Show._C["RESET"]
            + f"\n{Show._C['DIM']}│ {Show._C['RESET']}".join(lines),
            end=end,
            separator=""
        )

    @staticmethod
    def _close(
        ) -> None:

        from jarbin_toolkit_console import Console, ANSI

        if not Show._printing:
            return

        Console.print(
            ANSI.Color.rgb_fg(255, 160, 0).s
            + "-" * 112,
            separator=""
        )

        Show._current_test = None
        Show._current_test_number = None
        Show._printing = False

    @staticmethod
    def print(
            *values: str
        ) -> None:
        Show._print(*values, end="\n")

    class Log:

        @staticmethod
        def debug(
                title: str,
                msg: str
            ) -> None:
            Show._print(
                Show._C["TYPE"] + "DEBUG"
                + Show._C["RESET"] + "    │ "
                + Show._C["TYPE"] + title
                + Show._C["RESET"] + " │ "
                + Show._C["DIM"] + msg
                + Show._C["RESET"],
                end="\n"
            )

        @staticmethod
        def info(
                title: str,
                msg: str
            ) -> None:
            Show._print(
                Show._C["VALUE"] + "INFO"
                + Show._C["RESET"] + "     │ "
                + Show._C["VALUE"] + title
                + Show._C["RESET"] + " │ "
                + msg,
                end="\n"
            )

        @staticmethod
        def valid(
                title: str,
                msg: str
            ) -> None:
            Show._print(
                Show._C["SUCCESS"] + "VALID"
                + Show._C["RESET"] + "    │ "
                + Show._C["SUCCESS"] + title
                + Show._C["RESET"] + " │ "
                + msg,
                end="\n"
            )

        @staticmethod
        def warning(
                title: str,
                msg: str
            ) -> None:
            Show._print(
                Show._C["WARNING"] + "WARNING"
                + Show._C["RESET"] + "  │ "
                + Show._C["WARNING"] + title
                + Show._C["RESET"] + " │ "
                + msg,
                end="\n"
            )

        @staticmethod
        def error(
                title: str,
                msg: str
            ) -> None:
            Show._print(
                Show._C["ERROR"] + "ERROR"
                + Show._C["RESET"] + "    │ "
                + Show._C["ERROR"] + title
                + Show._C["RESET"] + " │ "
                + msg,
                end="\n"
            )

        @staticmethod
        def critical(
                title: str,
                msg: str
            ) -> None:
            Show._print(
                Show._C["CRITICAL"] + "CRITICAL"
                + Show._C["RESET"] + " │ "
                + Show._C["CRITICAL"] + title
                + Show._C["RESET"] + " │ "
                + msg,
                end="\n"
            )

    class Section:

        @staticmethod
        def show(
                title: str
            ) -> None:

            width = 108

            line = (
                f"--- {Show._C["RESET"] + Show._C["TITLE"] + title + Show._C["RESET"] + Show._C["DIM"]} "
                .center(width, "-")
            )

            Show._print(
                Show._C["RESET"]
                + Show._C["DIM"]
                + line
                + Show._C["RESET"],
                end="\n"
            )

    class Request:

        @staticmethod
        def show(
                method: str,
                url: str,
                *,
                params: object | None = None,
                headers: object | None = None,
                body: object | None = None
            ) -> None:

            Show._print(
                Show._C["TYPE"]
                + "REQUEST"
                + Show._C["RESET"],
                end="\n"
            )

            Show._print(
                Show._C["KEY"]
                + "Method"
                + Show._C["RESET"]
                + "  │ "
                + Show._C["VALUE"]
                + method.upper()
                + Show._C["RESET"],
                end="\n"
            )

            Show._print(
                Show._C["KEY"]
                + "URL"
                + Show._C["RESET"]
                + "     │ "
                + Show._C["VALUE"]
                + url
                + Show._C["RESET"],
                end="\n"
            )

            if params is not None:
                Show._print(
                    Show._C["KEY"]
                    + "Params"
                    + Show._C["RESET"]
                    + "  │ ",
                    params
                )

            if headers is not None:
                Show._print(
                    Show._C["KEY"]
                    + "Headers"
                    + Show._C["RESET"]
                    + " │ ",
                    headers
                )

            if body is not None:
                Show._print(
                    Show._C["KEY"]
                    + "Body"
                    + Show._C["RESET"]
                    + "    │ ",
                    body
                )

            Show._print(
                end="\n"
            )

    class Response:

        @staticmethod
        def show(
                response: object,
                *,
                body: bool = True,
                headers: bool = False
            ) -> None:

            Show._print(
                Show._C["TYPE"]
                + "RESPONSE"
                + Show._C["RESET"],
                end="\n"
            )

            status_code = getattr(
                response,
                "status_code",
                None
            )

            elapsed = getattr(
                response,
                "elapsed",
                None
            )

            url = getattr(
                response,
                "url",
                None
            )

            status_color = (
                Show._C["SUCCESS"]
                if status_code is not None
                and 200 <= status_code < 400
                else Show._C["ERROR"]
            )

            Show._print(
                Show._C["KEY"]
                + "Status"
                + Show._C["RESET"]
                + "  │ "
                + status_color
                + str(status_code)
                + Show._C["RESET"],
                end="\n"
            )

            if url is not None:
                Show._print(
                    Show._C["KEY"]
                    + "URL"
                    + Show._C["RESET"]
                    + "     │ "
                    + Show._C["VALUE"]
                    + str(url)
                    + Show._C["RESET"],
                    end="\n"
                )

            if elapsed is not None:
                Show._print(
                    Show._C["KEY"]
                    + "Elapsed"
                    + Show._C["RESET"]
                    + " │ "
                    + Show._C["VALUE"]
                    + str(elapsed)
                    + Show._C["RESET"],
                    end="\n"
                )

            if headers:
                response_headers = getattr(
                    response,
                    "headers",
                    None
                )

                if response_headers is not None:
                    Show._print(
                        Show._C["KEY"]
                        + "Headers"
                        + Show._C["RESET"]
                        + " │ ",
                        dict(response_headers)
                    )

            if body:
                try:
                    content = response.json()
                except Exception:
                    content = getattr(
                        response,
                        "text",
                        ""
                    )

                Show._print(
                    Show._C["KEY"]
                    + "Body"
                    + Show._C["RESET"]
                    + "    │ ",
                    content
                )

    class Exception:

        @staticmethod
        def show(
                exception: BaseException | BaseError
            ) -> None:

            Show._print(
                Show._C["ERROR"]
                + "EXCEPTION"
                + Show._C["RESET"],
                end="\n"
            )

            Show._print(
                Show._C["KEY"]
                + "Type"
                + Show._C["RESET"]
                + " │ "
                + Show._C["TYPE"]
                + type(exception).__name__
                + Show._C["RESET"],
                end="\n"
            )

            Show._print(
                Show._C["KEY"]
                + "Message"
                + Show._C["RESET"]
                + " │ "
                + exception.message if isinstance(exception, BaseError) else str(exception),
                end="\n"
            )

    class Table:

        @staticmethod
        def show(
                headers: list[object] | tuple[object, ...],
                rows: list[list[object] | tuple[object, ...]]
            ) -> None:

            if not headers:
                return

            columns = len(headers)

            normalized_rows = [
                list(row[:columns])
                for row in rows
            ]

            widths = [
                len(str(headers[index]))
                for index in range(columns)
            ]

            for row in normalized_rows:
                for index, value in enumerate(row):
                    widths[index] = max(
                        widths[index],
                        len(str(value))
                    )

            separator = (
                Show._C["DIM"]
                + "├"
                + "┼".join(
                    "─" * (width + 2)
                    for width in widths
                )
                + "┤"
                + Show._C["RESET"]
            )

            header = (
                Show._C["KEY"]
                + "│ "
                + " │ ".join(
                    str(value).ljust(width)
                    for value, width
                    in zip(headers, widths)
                )
                + " │"
                + Show._C["RESET"]
            )

            Show._print(
                header,
                end="\n"
            )
            Show._print(
                separator,
                end="\n"
            )

            for row in normalized_rows:

                values = []

                for index, width in enumerate(widths):

                    value = (
                        row[index]
                        if index < len(row)
                        else ""
                    )

                    values.append(
                        str(value).ljust(width)
                    )

                Show._print(
                    Show._C["VALUE"]
                    + "│ "
                    + " │ ".join(values)
                    + " │"
                    + Show._C["RESET"],
                end="\n"
                )

            Show._print(
                "",
                end="\n"
            )

    class Progress:

        def __init__(
                self,
                length: int,
                *,
                percent_style: str = "mix",
                percent_position: str = "a"
            ) -> None:

            from jarbin_toolkit_console.Animation.progressbar import ProgressBar

            self.bar = ProgressBar(
                length,
                percent_style=percent_style,
                percent_position=percent_position
            )

            self._started = False

        def update(
                self,
                percent: int
            ) -> None:

            self.bar.update(percent)

            if not self._started:
                self._started = True

                Show._print(
                    self.bar.render(
                        color=Show._C["VALUE"]
                    )
                )

                return

            Show._print(
                ANSI.Cursor.previous(),
                end=""
            )

            Show._print(
                self.bar.render(
                    color=Show._C["VALUE"]
                )
            )

        def finish(
                self
            ) -> None:

            self.bar.update(100)

            if self._started:
                Show._print(
                    ANSI.Cursor.previous(),
                    end=""
                )

            Show._print(
                self.bar.render(
                    color=Show._C["SUCCESS"]
                )
            )

            self._started = False
