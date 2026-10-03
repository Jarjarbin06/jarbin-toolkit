from .layout import Layout
from .style import Style
from .color import Color


class Format(Style, Color, Layout):


    @classmethod
    def _get_sgr(
            cls,
        ) -> object:
        ...


    _can_format: bool = True
    _sgr: object = None
