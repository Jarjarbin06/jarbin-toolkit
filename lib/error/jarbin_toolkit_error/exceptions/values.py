# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error/python
# File         : value.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.exceptions.exceptions import JException
from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType


class JErrorType(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            expected = EmptyField,
            actual = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "The types have refused to cooperate.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if expected is not EmptyField:
            msg += f"  Expected: {expected.__name__ if isinstance(expected, type) else expected}\n"

            if actual is not EmptyField:
                msg += f"  Actual: {type(actual).__name__}\n"
                msg += f"  Value: {actual!r}\n"

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorValue(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            value = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "The value looked valid. It was not.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if value is not EmptyField:
            msg += f"  Value: {value!r}\n"

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorAttribute(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            attribute = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "That attribute went to get milk and never came back.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if attribute is not EmptyField:
            msg += f"  Attribute: {attribute!r}\n"

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorName(JException):


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
            "We looked everywhere for that name. Absolutely nowhere.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if name is not EmptyField:
            msg += f"  Name: {name!r}\n"

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorIndex(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            index = EmptyField,
            obj = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "That index went beyond the edge of reality.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if index is not EmptyField:
            msg += f"  Index: {index!r}\n"

        if obj is not EmptyField:
            length= len(obj)
            msg += f"  Actual length: {length!r}\n"
            msg += f"  Last index: {length - 1!r}\n"

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


class JErrorKey(JException):


    def __init__(
            self,
            message = EmptyField,
            *,
            key = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "That key does not unlock this dictionary.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if key is not EmptyField:
            msg += f"  Key: {key!r}\n"

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


__all__ = [
    'JErrorType',
    'JErrorValue',
    'JErrorAttribute',
    'JErrorName',
    'JErrorIndex',
    'JErrorKey',
]
