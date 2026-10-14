# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error/exceptions
# File         : module.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.exceptions.exceptions import JException
from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType


class JErrorMemory(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "The RAM is full. Please remove some thoughts.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorBuffer(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "The buffer has buffered its last buffer.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


__all__ = [
    'JErrorMemory',
    'JErrorBuffer',
]
