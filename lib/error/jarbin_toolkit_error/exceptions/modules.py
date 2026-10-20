# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error/exceptions
# File         : module.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType
from jarbin_toolkit_error.exceptions.exceptions import JException


class JErrorImport(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            from_name = EmptyField,
            import_name = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "The import knocked. Nobody answered.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if from_name is not EmptyField:
            msg += f"  From: {from_name!r}\n"

        if import_name is not EmptyField:
            msg += f"  Import: {import_name!r}\n"

        if message is not EmptyField:
            msg += f"\n  → {message}"

        super().__init__(
            msg,
            format = format,  # pyright: ignore[reportArgumentType]
            link = link,
            do_raise = do_raise
        )


class JErrorModuleNotFound(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            name = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "This module has apparently chosen a new career path.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if name is not EmptyField:
            msg += f"  Import: {name!r}\n"

        if message is not EmptyField:
            msg += f"\n  → {message}"

        super().__init__(
            msg,
            format = format,  # pyright: ignore[reportArgumentType]
            link = link,
            do_raise = do_raise
        )


__all__ = [
    'JErrorImport',
    'JErrorModuleNotFound',
]
