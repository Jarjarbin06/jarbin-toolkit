from .border import Border
from .collection import Collection
from .color import Color
from .composition import Composition
from .decoration import Decoration
from .layout import Layout
from .style import Style

class Format(Style, Color, Layout, Border, Decoration, Collection, Composition):
    """
        Formatting
        (Style, Color, Layout, Border, Decoration, Collection, Composition)
    """


    _can_format: bool = True
    _sgr: object | None = None
    _cursor: object | None = None
    _osc: object | None = None


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


    @classmethod
    def _get_osc(
            cls,
        ) -> object:
        ...


__all__: list[str] = [
    'Format',
]
