# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/SGR
# File         : sgr.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.ansi.sgr.enums import (
    SGRReset,
    SGRStandardColorBackgroundBright,
    SGRStandardColorBackground,
    SGRStandardColorForeground,
    SGRStandardColorForegroundBright,
    SGRAttribute,
    SGRColorExtender,
    SGRAdvancedUnderline,
    SGRPosition,
    SGRColorMode,
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
            *values,
        ):

        if not values:
            raise ValueError("SGR values are required")

        if not all(isinstance(value, str | Color) for value in values):
            raise TypeError("SGR values must be strings or Color")

        return super().__new__(cls, f"{';'.join([str(value) for value in values])}m")


    @classmethod
    def reset(
            cls,
            *values,
        ):

        if not values:
            return cls(SGRReset.ALL)

        if not all(isinstance(value, SGRReset) for value in values):
            raise TypeError("SGR values must all be SGRReset")

        return cls(*values)


    @classmethod
    def attribute(
            cls,
            *values,
        ):

        if not all(isinstance(value, SGRAttribute) for value in values):
            raise TypeError("SGR values must be SGRAttribute")

        return cls(*values)


    @classmethod
    def foreground(
            cls,
            color,
        ):

        if not isinstance(color, SGRStandardColorForeground | SGRStandardColorForegroundBright):
            raise TypeError("SGR color must be SGRStandardColorForeground or SGRStandardColorForegroundBright")

        return cls(color)


    @classmethod
    def background(
            cls,
            color,
        ):

        if not isinstance(color, SGRStandardColorBackground | SGRStandardColorBackgroundBright):
            raise TypeError("SGR color must be SGRStandardColorBackground or SGRStandardColorBackgroundBright")

        return cls(color)


    @classmethod
    def color(
            cls,
            extender,
            color,
        ):

        if not isinstance(extender, SGRColorExtender):
            raise TypeError("SGR extender must be SGRColorExtender")

        if not isinstance(color, Color256 | ColorRGB):
            raise TypeError("SGR color must be Color256 or ColorRGB")

        mode = SGRColorMode.RGB if isinstance(color, ColorRGB) else SGRColorMode.INDEXED

        return cls(extender, mode, color)


    @classmethod
    def underline(
            cls,
            style = SGRAdvancedUnderline.SINGLE,
            color = None,
        ):

        if not isinstance(style, SGRAdvancedUnderline):
            raise TypeError("SGR style must be SGRAdvancedUnderline")

        if color is not None:

            if not isinstance(color, Color256 | ColorRGB):
                raise TypeError("SGR color must be Color256 or ColorRGB")

            mode = SGRColorMode.RGB if isinstance(color, ColorRGB) else SGRColorMode.INDEXED

            return cls(style, SGRColorExtender.UNDERLINE, mode, color)

        return cls(style)


    @classmethod
    def position(
            cls,
            value,
        ):

        if not isinstance(value, SGRPosition):
            raise TypeError("SGR type must be SGRPosition")

        return cls(value)



__all__ = [
    'SGR',
]
