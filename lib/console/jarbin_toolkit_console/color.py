# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI
# File         : color.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.error import ConsoleJError


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
            raise ConsoleJError("Color must be a number between 0 and 255")

        super().__init__(color=color)


    @property
    def color(
            self,
        ):

        return self._values["color"]

    @classmethod
    def test(
            cls,
        ):  # pragma: no cover

        from jarbin_toolkit_console.ansi.sgr.sgr import SGR
        from jarbin_toolkit_console.ansi.sgr.enums import (
            SGRColorExtender,
            SGRReset,
        )

        def print_color(
                color,
            ):
            print(
                SGR.color(SGRColorExtender.BACKGROUND, cls(color)),
                f"{color:3d}",
                SGR.reset(SGRReset.BACKGROUND_COLOR),
                end="",
            )

        print("System colors:")
        for start in (0, 8):
            for color in range(start, start + 8):
                print_color(color)
            print()

        print("\nColor cube (16-231):")

        for green in range(6):
            for red in range(6):
                for blue in range(6):
                    color = 16 + (red * 36) + (green * 6) + blue
                    print_color(color)

                print()

            print()

        print("Grayscale (232-255):")

        for color in range(232, 256):
            print_color(color)

        print()


class ColorRGB(Color):


    def __init__(
            self,
            r,
            g,
            b,
        ):

        if not all(isinstance(value, int) and 0 <= value <= 255 for value in [r, g, b]):
            raise ConsoleJError("RGB values must all be numbers between 0 and 255")

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
            raise ConsoleJError("HEX color must be string and contain exactly 6 hexadecimal digits")

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
