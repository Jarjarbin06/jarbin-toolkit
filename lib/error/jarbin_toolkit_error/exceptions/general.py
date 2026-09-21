# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error/python
# File         : general.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.exceptions.exception import JException
from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType


class JErrorRuntime(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "A bug has escaped containment. Please remain calm.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if message is not EmptyField:
            msg += f"  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorNotImplemented(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "This feature is still waiting for its developer.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if message is not EmptyField:
            msg += f"  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorRecursion(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "We went so deep, even the stack gave up.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if message is not EmptyField:
            msg += f"  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorSystem(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "The system did something weird. Even Python is concerned.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if message is not EmptyField:
            msg += f"  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


__all__ = [
    'JErrorRuntime',
    'JErrorNotImplemented',
    'JErrorRecursion',
    'JErrorSystem',
]
