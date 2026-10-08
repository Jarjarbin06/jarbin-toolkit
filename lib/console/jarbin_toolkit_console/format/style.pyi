from typing import (
    Any,
    Optional,
)

from jarbin_toolkit_console.ansi.sgr import SGRAdvancedUnderline
from jarbin_toolkit_console.text import Text
from jarbin_toolkit_console.color import (
    ColorRGB,
    Color256,
    ColorHEX,
)


class Style:
    """
        Style formatting
    """


    def f_style_reset(
            self,
        ) -> Text:
        """
            Reset format

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_bold(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Bold text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_faint(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Faint text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_dim(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Dim text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_italic(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Italic text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_underline(
            self,
            *,
            style: Optional[SGRAdvancedUnderline] = None,
            color: Optional[ColorRGB | Color256 | ColorHEX] = None,
            reset: bool = True,
        ) -> Text:
        """
            Underline text (leave style and color empty for regular underline)

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_strikethrough(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Strikethrough text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_blink(
            self,
            *,
            is_fast: bool = False,
            reset: bool = True,
        ) -> Text:
        """
            Blink text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_reverse(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Reverse color text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_hide(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Hide text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_show(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Show text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_frame(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Frame text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_encircle(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Encircle text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_overline(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Overline text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_superscript(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Superscript text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_style_subscript(
            self,
            *,
            reset: bool = True,
        ) -> Text:
        """
            Subscript text

            Returns
            ----------
            Text
                New format
        """
        ...


    def _get_style_sequence(
            self,
            style: Any,
        ) -> Text:
        ...


__all__: list[str]
