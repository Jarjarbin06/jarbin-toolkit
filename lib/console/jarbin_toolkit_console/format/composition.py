# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : composition.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.error import ConsoleJError
from jarbin_toolkit_console.format.enums import FormatStyle
from jarbin_toolkit_console.color import (
    Color256,
    ColorHEX,
    ColorRGB,
)


class Composition:


    def _get_composition_text(
            self,
            composition,
        ):

        if not getattr(self, "_can_format", False):
            return self

        return self.__class__("".join(map(str, composition)))


    def f_composition_style(
            self,
            *styles,
        ):

        SGR = self._get_sgr()

        if any(not isinstance(style, FormatStyle) for style in styles):
            raise ConsoleJError("Styles must be FormatStyle")

        prefix = [style.value[0] for style in styles]
        suffix = [style.value[1] for style in styles]
        suffix.reverse()

        new_text = [
            SGR.SGR(*prefix),
            self,
            SGR.SGR(*suffix)
        ]

        return self._get_composition_text(new_text)


    def f_composition_colored(
            self,
            *,
            foreground = None,
            background = None,
        ):

        colors = (
            ("foreground", foreground),
            ("background", background),
        )

        for name, color in colors:
            if color is None:
                continue

            if not isinstance(color.value, (Color256, ColorRGB, ColorHEX)):
                raise ConsoleJError(
                    f"{name} must contain a Color256, ColorRGB or ColorHEX"
                )

        SGR = self._get_sgr()

        foreground_code = (
            SGR.SGR.color(
                SGR.SGRColorExtender.FOREGROUND,
                foreground.value,
            )
            if foreground is not None else ""
        )

        background_code = (
            SGR.SGR.color(
                SGR.SGRColorExtender.BACKGROUND,
                background.value,
            )
            if background is not None else ""
        )

        foreground_reset = (
            SGR.SGR.reset(SGR.SGRReset.FOREGROUND_COLOR)
            if foreground is not None else ""
        )

        background_reset = (
            SGR.SGR.reset(SGR.SGRReset.BACKGROUND_COLOR)
            if background is not None else ""
        )

        new_text = [
            foreground_code,
            background_code,
            self,
            background_reset,
            foreground_reset,
        ]

        return self._get_composition_text(new_text)


    def f_composition_chain(
            self,
            *operations,
        ):

        new_text = self

        for op in operations:
            new_text = op(new_text)

        return new_text


__all__ = [
    'Composition',
]
