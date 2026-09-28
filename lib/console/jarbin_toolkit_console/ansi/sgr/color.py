# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/SGR
# File         : color.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.ansi.sgr.enums import SGRColorMode


class Color:


    def __init__(
            self,
            **values,
        ):

        if not all(isinstance(value, int) for key, value in values.items() if key != "mode"):
            raise ValueError("Color values must all be numbers")

        self._values = values


    def __str__(
            self,
        ):
        return ";".join(str(value) for value in self._values.values())


class Color256(Color):


    def __init__(
            self,
            color,
        ):

        if not isinstance(color, int) or not 0 <= color <= 255:
            raise ValueError("Color must be a number between 0 and 255")

        super().__init__(mode=SGRColorMode.INDEXED, color=color)


    @property
    def mode(
            self,
        ):
        return self._values["mode"]


    @property
    def color(
            self,
        ):
        return self._values["color"]


class ColorRGB(Color):


    def __init__(
            self,
            r,
            g,
            b,
        ):

        if not all(isinstance(value, int) and 0 <= value <= 255 for value in [r, g, b]):
            raise ValueError("RGB values must all be numbers between 0 and 255")

        super().__init__(mode=SGRColorMode.RGB, r=r, g=g, b=b)


    @property
    def mode(
            self,
        ):
        return self._values["mode"]


    @property
    def r(
            self,
        ):
        return self._values["r"]


    @property
    def g(
            self,
        ):
        return self._values["g"]


    @property
    def b(
            self,
        ):
        return self._values["b"]


__all__ = [
    'Color',
    'Color256',
    'ColorRGB',
]
