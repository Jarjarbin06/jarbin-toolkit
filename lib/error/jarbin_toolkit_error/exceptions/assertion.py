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


class JErrorAssertion(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "You said this would be true. It was not.\n\n"
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


class JErrorLookup(JException):


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
            msg += f"\n\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


__all__ = [
    'JErrorAssertion',
    'JErrorLookup',
]
