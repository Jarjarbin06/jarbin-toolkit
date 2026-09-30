# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI
# File         : color.py
#
# Author       : Jarjarbin06
# ============================================================================


class Color:


    def __init__(
            self,
            **values,
        ):

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

        super().__init__(color=color)


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

        super().__init__(r=r, g=g, b=b)


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


    def to_hex(
            self,
        ):

        return ColorHEX(f"{self.r:02X}{self.g:02X}{self.b:02X}")


class ColorHEX(Color):


    _allowed = "0123456789ABCDEF"


    def __init__(
            self,
            color,
        ):

        if str(color).startswith("#"):
            color = str(color)[1:]

        if not isinstance(color, str) or len(color) != 6 or not all(
            char.upper() in self._allowed
            for char in color
        ):
            raise ValueError("HEX color must be string and contain exactly 6 hexadecimal digits")

        super().__init__(color=color.upper())


    @property
    def color(
            self,
        ):

        return self._values["color"]


    def to_rgb(
            self,
        ):

        return ColorRGB(
            int(self.color[0:2], 16),
            int(self.color[2:4], 16),
            int(self.color[4:6], 16),
        )


__all__ = [
    'Color',
    'Color256',
    'ColorRGB',
    'ColorHEX',
]
