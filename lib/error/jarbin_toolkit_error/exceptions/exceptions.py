# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error/python
# File         : exception.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.base_error import BaseJError
from jarbin_toolkit_error.empty_field import EmptyField
from jarbin_toolkit_error.enums import FormatType


class JException(BaseJError):


    funny_message = None


    def _show_funny(
            self,
            _class,
        ):
        return self.funny_message or type(self) is _class


    def __init__(
            self,
            message = EmptyField,
            *,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        super().__init__(
            message if message is not EmptyField else "",
            format = format,
            link = link,
            do_raise = do_raise
        )


__all__ = [
    'JException',
]
