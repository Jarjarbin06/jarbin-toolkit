from typing import Optional

from .layout import Layout
from .color import Color
from .style import Style
from .border import Border
from .decoration import Decoration
from .collection import Collection
from .composition import Composition


class Format(Style, Color, Layout, Border, Decoration, Collection, Composition):
    """
        Formatting
        (Style, Color, Layout, Border, Decoration, Collection, Composition)
    """


    _can_format: bool = True
    _sgr: Optional[object] = None
    _cursor: Optional[object] = None
    _osc: Optional[object] = None


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


__all__: list[str]
