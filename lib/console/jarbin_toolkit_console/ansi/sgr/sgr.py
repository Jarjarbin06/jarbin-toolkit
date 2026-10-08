# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/SGR
# File         : sgr.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.error import ConsoleJError
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
    ColorHEX,
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
            raise ConsoleJError("SGR values are required")

        if not all(isinstance(value, str | Color) for value in values):
            raise ConsoleJError("SGR values must be strings or Color")

        return super().__new__(cls, f"{';'.join([str(value) for value in values])}m")


    @classmethod
    def reset(
            cls,
            *resets,
        ):

        if not resets:
            return cls(SGRReset.ALL)

        if not all(isinstance(reset, SGRReset) for reset in resets):
            raise ConsoleJError("SGR resets must all be SGRReset")

        return cls(*resets)


    @classmethod
    def attribute(
            cls,
            *attributes,
        ):

        if not all(isinstance(atr, SGRAttribute) for atr in attributes):
            raise ConsoleJError("SGR attributes must be SGRAttribute")

        return cls(*attributes)


    @classmethod
    def foreground(
            cls,
            color,
        ):

        if not isinstance(color, SGRStandardColorForeground | SGRStandardColorForegroundBright):
            raise ConsoleJError("SGR color must be SGRStandardColorForeground or SGRStandardColorForegroundBright")

        return cls(color)


    @classmethod
    def background(
            cls,
            color,
        ):

        if not isinstance(color, SGRStandardColorBackground | SGRStandardColorBackgroundBright):
            raise ConsoleJError("SGR color must be SGRStandardColorBackground or SGRStandardColorBackgroundBright")

        return cls(color)


    @classmethod
    def color(
            cls,
            extender,
            color,
        ):

        if not isinstance(extender, SGRColorExtender):
            raise ConsoleJError("SGR extender must be SGRColorExtender")

        if isinstance(color, ColorHEX):
            color = color.to_rgb()

        if not isinstance(color, Color256 | ColorRGB):
            raise ConsoleJError("SGR color must be Color256 or ColorRGB")

        mode = SGRColorMode.RGB if isinstance(color, ColorRGB) else SGRColorMode.INDEXED

        return cls(extender, mode, color)


    @classmethod
    def underline(
            cls,
            style = SGRAdvancedUnderline.SINGLE,
            color = None,
        ):

        if not isinstance(style, SGRAdvancedUnderline):
            raise ConsoleJError("SGR style must be SGRAdvancedUnderline")

        if color is not None:

            if isinstance(color, ColorHEX):
                color = color.to_rgb()

            if not isinstance(color, Color256 | ColorRGB):
                raise ConsoleJError("SGR color must be Color256 or ColorRGB")

            mode = SGRColorMode.RGB if isinstance(color, ColorRGB) else SGRColorMode.INDEXED

            return cls(style, SGRColorExtender.UNDERLINE, mode, color)

        return cls(style)


    @classmethod
    def position(
            cls,
            position,
        ):

        if not isinstance(position, SGRPosition):
            raise ConsoleJError("SGR position must be SGRPosition")

        return cls(position)



__all__ = [
    'SGR',
]
