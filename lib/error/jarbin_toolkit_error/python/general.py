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


class JErrorRuntime(BaseJError):


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = "A bug has escaped containment. Please remain calm."

        if message is not EmptyField:
            msg += f"\n\n  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


__all__ = [
    'JErrorRuntime'
]
