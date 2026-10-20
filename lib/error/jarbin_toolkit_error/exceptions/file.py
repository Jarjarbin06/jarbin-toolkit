# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error/exceptions
# File         : file.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType
from jarbin_toolkit_error.exceptions.exceptions import JException


class JErrorIO(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = ""

        if message is not EmptyField:
            msg += f"\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorFileNotFound(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            path = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "We searched everywhere. The file is still playing hide-and-seek.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if path is not EmptyField:
            msg += f"  Path: {path}\n"

        if message is not EmptyField:
            msg += f"\n  → {message}"

        super().__init__(
            msg,
            format = format,  # pyright: ignore[reportArgumentType]
            link = link,
            do_raise = do_raise
        )


class JErrorFileExists(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            path = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "Surprise! That file already exists.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if path is not EmptyField:
            msg += f"  Path: {path}\n"

        if message is not EmptyField:
            msg += f"\n  → {message}"

        super().__init__(
            msg,
            format = format,  # pyright: ignore[reportArgumentType]
            link = link,
            do_raise = do_raise
        )


class JErrorPermission(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            path = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "Access denied. The computer has trust issues.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if path is not EmptyField:
            msg += f"  Path: {path}\n"

        if message is not EmptyField:
            msg += f"\n  → {message}"

        super().__init__(
            msg,
            format = format,  # pyright: ignore[reportArgumentType]
            link = link,
            do_raise = do_raise
        )


class JErrorIsADirectory(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            path = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "You asked for a file. We found an entire neighborhood.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if path is not EmptyField:
            msg += f"  Path: {path}\n"

        if message is not EmptyField:
            msg += f"\n  → {message}"

        super().__init__(
            msg,
            format = format,  # pyright: ignore[reportArgumentType]
            link = link,
            do_raise = do_raise
        )


class JErrorNotADirectory(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            path = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "That's a file, not a hallway.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if path is not EmptyField:
            msg += f"  Path: {path}\n"

        if message is not EmptyField:
            msg += f"\n  → {message}"

        super().__init__(
            msg,
            format = format,  # pyright: ignore[reportArgumentType]
            link = link,
            do_raise = do_raise
        )


class JErrorDirectoryNotEmpty(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            path = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "You can't remove this directory. It has emotional baggage.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if path is not EmptyField:
            msg += f"  Path: {path}\n"

        if message is not EmptyField:
            msg += f"\n  → {message}"

        super().__init__(
            msg,
            format = format,  # pyright: ignore[reportArgumentType]
            link = link,
            do_raise = do_raise
        )


__all__ = [
    'JErrorDirectoryNotEmpty',
    'JErrorFileExists',
    'JErrorFileNotFound',
    'JErrorIO',
    'JErrorIsADirectory',
    'JErrorNotADirectory',
    'JErrorPermission',
]
