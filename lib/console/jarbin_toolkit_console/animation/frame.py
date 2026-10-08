# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : frame.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.error import ConsoleJError
from jarbin_toolkit_console.text import Text


class Frame(Text):


    _can_format = False


    def __new__(
            cls,
            content = "",
            *,
            duration = None,
        ):

        if duration is not None and duration <= 0:
            raise ConsoleJError("Duration must be greater than zero")

        instance = super().__new__(
            cls,
            str(content),
        )

        instance._duration = duration

        return instance


    @property
    def content(
            self,
        ):

        return Text(str(self))


    @property
    def duration(
            self,
        ):

        return self._duration


    def render(
            self,
        ):

        return self.content


__all__ = [
    'Frame',
]
