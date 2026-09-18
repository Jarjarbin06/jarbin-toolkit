# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : error_link.py
# Class        : ErrorLink
#
# Author       : Jarjarbin06
# ============================================================================


import inspect
import linecache
from os import PathLike
from os.path import (
    exists,
    abspath,
    dirname,
    normcase,
)
from typing import final

from jarbin_toolkit_error.enums import (
    FormatType,
    ErrorColor,
)


@final
class ErrorLink:


    def _str_detailed(
            self,
        ):

        if self.file is None:
            return ""

        location = (
            f"{ErrorColor.MUTED}"
            f'File "{self.file}"'
            f"{ErrorColor.RESET}"
        )

        if self.line is not None:
            location += (
                f"{ErrorColor.TEXT}, line {self.line}"
                f"{ErrorColor.RESET}"
            )

        if self.class_name is not None:
            location += (
                f"{ErrorColor.TEXT}, in {self.class_name}"
                f"{ErrorColor.RESET}"
            )

        return location


    def _str_traceback(
            self,
        ):

        values = []

        if self.file is not None:
            values.append(
                f"{ErrorColor.MUTED}"
                f'File "{self.file}"'
                f"{ErrorColor.RESET}"
            )

        if self.line is not None:
            values.append(
                f"{ErrorColor.TEXT}"
                f"line {self.line}"
                f"{ErrorColor.RESET}"
            )

        if self.column is not None:
            values.append(
                f"{ErrorColor.TEXT}"
                f"column {self.column}"
                f"{ErrorColor.RESET}"
            )

        result = ", ".join(values)

        context = []

        if self.function is not None:
            context.append(
                f"{ErrorColor.ERROR}"
                f"in {self.function}"
                f"{ErrorColor.RESET}"
            )

        if self.class_name is not None:
            context.append(
                f"{ErrorColor.ERROR}"
                f"class {self.class_name}"
                f"{ErrorColor.RESET}"
            )

        if self.module is not None:
            context.append(
                f"{ErrorColor.MUTED}"
                f"module {self.module}"
                f"{ErrorColor.RESET}"
            )

        if context:
            result += f"\n      → {', '.join(context)}"

        return result


    def _resolve_frame(
            self,
            frame
        ):

        if self.file is None:
            self.file = frame.f_code.co_filename

        if self.line is None:
            self.line = frame.f_lineno

        if self.function is None:
            self.function = frame.f_code.co_name

        if self.module is None:
            self.module = frame.f_globals.get(
                "__name__"
            )

        if self.class_name is None:
            instance = frame.f_locals.get("self")

            if instance is not None:
                self.class_name = type(instance).__name__
            else:
                cls = frame.f_locals.get("cls")

                if isinstance(cls, type):
                    self.class_name = cls.__name__

        if self.code is None:
            self.code = linecache.getline(
                self.file,
                self.line
            ).strip() or None

        if self.column is None:
            self.column = self._resolve_column(frame)


    def __init__(
            self,
            *,
            file = None,
            line = None,
            column = None,
            function = None,
            module = None,
            class_name = None,
            code = None
        ):

        if file is not None:
            if not isinstance(file, str | PathLike):
                raise TypeError(
                    "File must be of type str, PathLike or None"
                )

            if not exists(file):
                raise FileNotFoundError(
                    f"Failed to link to file {file}"
                )

            file = str(file)

        if line is not None:
            if not isinstance(line, int):
                raise TypeError(
                    "Line must be of type int or None"
                )

            if line <= 0:
                raise ValueError(
                    "Line must be greater than 0"
                )

        if column is not None:
            if not isinstance(column, int):
                raise TypeError(
                    "Column must be of type int or None"
                )

            if column <= 0:
                raise ValueError(
                    "Column must be greater than 0"
                )

        for name, value in (
            ("function", function),
            ("module", module),
            ("class_name", class_name),
            ("code", code),
        ):
            if value is not None and not isinstance(value, str):
                raise TypeError(
                    f"{name.capitalize()} must be of type str or None"
                )

        self.file = file
        self.line = line
        self.column = column
        self.function = function
        self.module = module
        self.class_name = class_name
        self.code = code

        self.resolve()


    def __repr__(
            self
        ) -> str:

        return (
            f"<{type(self).__name__}("
            f"file={self.file!r}, "
            f"line={self.line!r}, "
            f"column={self.column!r}, "
            f"function={self.function!r}, "
            f"module={self.module!r}, "
            f"class_name={self.class_name!r}, "
            f"code={self.code!r}"
            f")>"
        )


    def resolve(
            self
        ) -> None:

        frame = inspect.currentframe()

        if frame is None:
            return

        frame = frame.f_back

        while frame is not None:
            filename = frame.f_code.co_filename

            if not self._is_internal_frame(filename):
                self._resolve_frame(frame)
                return

            frame = frame.f_back


    def display_link(
            self,
            format
        ):

        if isinstance(format, str):
            format = FormatType(format)

        if not isinstance(format, FormatType):
            raise TypeError(
                "Format must be of type FormatType or str"
            )

        if format in (
                FormatType.COMPACT,
                FormatType.PRETTY,
            ):
            return ""
        elif format == FormatType.DETAILED:
            return self._str_detailed()
        elif format == FormatType.TRACEBACK:
            return self._str_traceback()

        return ""

    @staticmethod
    def _is_internal_frame(
            filename
        ):

        filename = normcase(
            abspath(filename)
            )

        package_dir = normcase(
            abspath(dirname(__file__))
        )

        if (
            filename == package_dir
            or filename.startswith(package_dir + "/")
        ):
            return True

        parts = filename.split("/")

        return any(
            part.startswith("jarbin_toolkit_")
            for part in parts
        )


    @staticmethod
    def _resolve_column(
            frame
        ):

        try:
            instruction = frame.f_lasti
            positions = list(
                frame.f_code.co_positions()
            )

            position = positions[instruction // 2]

            column = position[2]

            if column is None:
                return None

            return column + 1

        except (IndexError, TypeError, AttributeError):
            return None


__all__ = [
    'ErrorLink',
]
