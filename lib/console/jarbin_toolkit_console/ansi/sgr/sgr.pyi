from .enums import (
    SGRReset,
    SGRStandardColorForeground,
    SGRStandardColorForegroundBright,
    SGRAttribute,
    SGRColorExtender,
    SGRAdvancedUnderline,
    SGRPosition,
)
from jarbin_toolkit_console.color import (
    Color,
    ColorRGB,
    Color256,
)
from jarbin_toolkit_console.ansi.ansi import CSI


class SGR(CSI):


    def __new__(
            cls,
            *values: str | Color,
        ) -> SGR:
        """
            Create a new SGR ANSI sequence
        
            Parameters
            ----------
            *values : str | Color
                Ansi sequence (accepts colors for formatting)
        """
        ...


    @classmethod
    def reset(
            cls,
            *resets: SGRReset,
        ) -> SGR:
        """
            Reset sequence
        
            Parameters
            ----------
            *resets : SGRReset
                Reset type
        """
        ...


    @classmethod
    def attribute(
            cls,
            *attributes: SGRAttribute,
        ) -> SGR:
        """
            Set attribute sequence.

            Parameters
            ----------
            *attributes : SGRAttribute
                Text attributes
        """
        ...


    @classmethod
    def foreground(
            cls,
            color: SGRStandardColorForeground | SGRStandardColorForegroundBright,
        ) -> SGR:
        """
            Foreground color sequence.

            Parameters
            ----------
            color : SGRStandardColorForeground | SGRStandardColorForegroundBright
                Color for foreground
        """
        ...


    @classmethod
    def background(
            cls,
            color: SGRStandardColorForeground | SGRStandardColorForegroundBright,
        ) -> SGR:
        """
            Background color sequence.

            Parameters
            ----------
            color : SGRStandardColorForeground | SGRStandardColorForegroundBright
                Color for background
        """
        ...


    @classmethod
    def color(
            cls,
            extender: SGRColorExtender,
            color: Color256 | ColorRGB,
        ) -> SGR:
        """
            Color sequence for the given extender.

            Parameters
            ----------
            extender : SGRColorExtender
                Color extender

            color : Color256 | ColorRGB
                Color for text
        """
        ...


    @classmethod
    def underline(
            cls,
            style: SGRAdvancedUnderline = SGRAdvancedUnderline.SINGLE,
            color = None,
        ) -> SGR:
        """
            Color sequence for the given extender.

            Parameters
            ----------
            style : SGRAdvancedUnderline
                Underline style

            color : Color256 | ColorRGB
                Color for text
        """
        ...


    @classmethod
    def position(
            cls,
            position: SGRPosition,
        ):
        """
            Position of the text.

            Parameters
            ----------
            position : SGRPosition
                Text position
        """
        ...



__all__: list[str]
