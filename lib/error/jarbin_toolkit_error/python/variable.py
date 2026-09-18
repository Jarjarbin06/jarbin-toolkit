# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error/python
# File         : python.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.base_error import BaseJError
from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType


class JErrorType(BaseJError):


    def __init__(
            self,
            message = EmptyField,
            *,
            obj = EmptyField,
            name = EmptyField,
            expected = EmptyField,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = ""

        if name is not EmptyField:
            msg += f"Invalid type for {name!r}"
        else:
            msg += "Invalid type"

        if expected is not EmptyField:
            msg += f"\n  Expected: {expected.__name__ if isinstance(expected, type) else expected}"

            if obj is not EmptyField:
                msg += f"\n  Received: {type(obj).__name__}\n  Value: {obj!r}"

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


__all__ = [
    'JErrorType'
]
