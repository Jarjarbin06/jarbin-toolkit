# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error/python
# File         : logic.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.exceptions.exception import JException
from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType


class JErrorArithmetic(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        super().__init__(
            f"→ {message}",
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorZeroDivision(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            dividend = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "Nice try. Mathematics says no.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if dividend is not EmptyField:
            msg += f"  Dividend: {dividend!r}\n"

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            f"→ {message}",
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorOverflow(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "We put too much number in the number box.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            f"→ {message}",
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorFloatingPoint(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        super().__init__(
            f"→ {message}",
            format = format,
            link = link,
            do_raise = do_raise
        )


__all__ = [
    'JErrorArithmetic',
    'JErrorZeroDivision',
    'JErrorOverflow',
    'JErrorFloatingPoint',
]
