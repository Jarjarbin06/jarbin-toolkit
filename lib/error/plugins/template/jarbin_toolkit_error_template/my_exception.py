# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error-Template
# File         : my_exception.py
#
# Author       : Jarjarbin06
# ============================================================================



from jarbin_toolkit_error import JException
from jarbin_toolkit_error import _EmptyField
from jarbin_toolkit_error import FormatType


class JErrorMyException(JException):


    def __init__(
            self,
            message = _EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        msg = (
            "My custom exception likes this new error style.\n\n"
            if self._show_funny(__class__)
            else ""
        )

        if message is not _EmptyField:
            msg += f"  → {message}"

        super().__init__(
            msg,
            format = format,
            link = link,
            do_raise = do_raise
        )


__all__ = [
    'JErrorMyException',
]
