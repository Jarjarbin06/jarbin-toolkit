from .layout import Layout
from .style import Style
from .color import Color


class Format(Style, Color, Layout):


    _can_format: bool = True
    _sgr: object = None
    _cursor: object = None


    @classmethod
    def _get_sgr(
            cls,
        ) -> object:
        ...


    @classmethod
    def _get_cursor(
            cls,
        ) -> object:
        ...
