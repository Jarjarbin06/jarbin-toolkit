# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : color.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.color import (
    ColorRGB,
    Color256,
    ColorHEX,
)
from jarbin_toolkit_console.enums import PresetColor


class Color:


    def _get_color_sequence(
            self,
            color,
        ):

        if not getattr(self, "_can_format", False):
            return self

        return self.__class__("".join(map(str, color)))


    def f_color_foreground(
            self,
            color = ColorRGB(255, 255, 255),
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        if isinstance(color, Color256 | ColorRGB | ColorHEX):
            color = color.to_rgb() if isinstance(color, ColorHEX) else color
            mode = SGR.SGRColorMode.RGB if isinstance(color, ColorRGB) else SGR.SGRColorMode.INDEXED

            sequence = [
                SGR.SGR(SGR.SGRColorExtender.FOREGROUND, mode, color),
                self,
                (
                    SGR.SGR(SGR.SGRReset.FOREGROUND_COLOR)
                    if reset else
                    ""
                )
            ]

        else:
            sequence = [
                SGR.SGR(color),
                self,
                (
                    SGR.SGR(SGR.SGRReset.FOREGROUND_COLOR)
                    if reset else
                    ""
                )
            ]

        return self._get_color_sequence(sequence)


    def f_color_black(
            self,
            *,
            background = False,
            bright = False,
            reset = True,
        ):

        SGR = self._get_sgr()

        if background:
            if bright:
                return self.f_color_background(SGR.SGRStandardColorBackgroundBright.BLACK, reset=reset)

            return self.f_color_background(SGR.SGRStandardColorBackground.BLACK, reset=reset)

        if bright:
            return self.f_color_foreground(SGR.SGRStandardColorForegroundBright.BLACK, reset=reset)

        return self.f_color_foreground(SGR.SGRStandardColorForeground.BLACK, reset=reset)


    def f_color_red(
            self,
            *,
            background = False,
            bright = False,
            reset = True,
        ):

        SGR = self._get_sgr()

        if background:
            if bright:
                return self.f_color_background(SGR.SGRStandardColorBackgroundBright.RED, reset=reset)

            return self.f_color_background(SGR.SGRStandardColorBackground.RED, reset=reset)

        if bright:
            return self.f_color_foreground(SGR.SGRStandardColorForegroundBright.RED, reset=reset)

        return self.f_color_foreground(SGR.SGRStandardColorForeground.RED, reset=reset)


    def f_color_green(
            self,
            *,
            background = False,
            bright = False,
            reset = True,
        ):

        SGR = self._get_sgr()

        if background:
            if bright:
                return self.f_color_background(SGR.SGRStandardColorBackground.GREEN, reset=reset)

            return self.f_color_background(SGR.SGRStandardColorBackground.GREEN, reset=reset)

        if bright:
            return self.f_color_foreground(SGR.SGRStandardColorForegroundBright.GREEN, reset=reset)

        return self.f_color_foreground(SGR.SGRStandardColorForeground.GREEN, reset=reset)


    def f_color_yellow(
            self,
            *,
            background = False,
            bright = False,
            reset = True,
        ):

        SGR = self._get_sgr()

        if background:
            if bright:
                return self.f_color_background(SGR.SGRStandardColorBackgroundBright.YELLOW, reset=reset)

            return self.f_color_background(SGR.SGRStandardColorBackground.YELLOW, reset=reset)

        if bright:
            return self.f_color_foreground(SGR.SGRStandardColorForegroundBright.YELLOW, reset=reset)

        return self.f_color_foreground(SGR.SGRStandardColorForeground.YELLOW, reset=reset)


    def f_color_blue(
            self,
            *,
            background = False,
            bright = False,
            reset = True,
        ):

        SGR = self._get_sgr()

        if background:
            if bright:
                return self.f_color_background(SGR.SGRStandardColorBackgroundBright.BLUE, reset=reset)

            return self.f_color_background(SGR.SGRStandardColorBackground.BLUE, reset=reset)

        if bright:
            return self.f_color_foreground(SGR.SGRStandardColorForegroundBright.BLUE, reset=reset)

        return self.f_color_foreground(SGR.SGRStandardColorForeground.BLUE, reset=reset)


    def f_color_magenta(
            self,
            *,
            background = False,
            bright = False,
            reset = True,
        ):

        SGR = self._get_sgr()

        if background:
            if bright:
                return self.f_color_background(SGR.SGRStandardColorBackgroundBright.MAGENTA, reset=reset)

            return self.f_color_background(SGR.SGRStandardColorBackground.MAGENTA, reset=reset)

        if bright:
            return self.f_color_foreground(SGR.SGRStandardColorForegroundBright.MAGENTA, reset=reset)

        return self.f_color_foreground(SGR.SGRStandardColorForeground.MAGENTA, reset=reset)


    def f_color_cyan(
            self,
            *,
            background = False,
            bright = False,
            reset = True,
        ):

        SGR = self._get_sgr()

        if background:
            if bright:
                return self.f_color_background(SGR.SGRStandardColorBackgroundBright.CYAN, reset=reset)

            return self.f_color_background(SGR.SGRStandardColorBackground.CYAN, reset=reset)

        if bright:
            return self.f_color_foreground(SGR.SGRStandardColorForegroundBright.CYAN, reset=reset)

        return self.f_color_foreground(SGR.SGRStandardColorForeground.CYAN, reset=reset)


    def f_color_white(
            self,
            *,
            background = False,
            bright = False,
            reset = True,
        ):

        SGR = self._get_sgr()

        if background:
            if bright:
                return self.f_color_background(SGR.SGRStandardColorBackgroundBright.WHITE, reset=reset)

            return self.f_color_background(SGR.SGRStandardColorBackground.WHITE, reset=reset)

        if bright:
            return self.f_color_foreground(SGR.SGRStandardColorForegroundBright.WHITE, reset=reset)

        return self.f_color_foreground(SGR.SGRStandardColorForeground.WHITE, reset=reset)


    def f_color_background(
            self,
            color = ColorRGB(255, 255, 255),
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        if isinstance(color, Color256 | ColorRGB | ColorHEX):
            color = color.to_rgb() if isinstance(color, ColorHEX) else color
            mode = SGR.SGRColorMode.RGB if isinstance(color, ColorRGB) else SGR.SGRColorMode.INDEXED

            sequence = [
                SGR.SGR(SGR.SGRColorExtender.BACKGROUND, mode, color),
                self,
                (
                    SGR.SGR(SGR.SGRReset.BACKGROUND_COLOR)
                    if reset else
                    ""
                )
            ]

        else:
            sequence = [
                SGR.SGR(color),
                self,
                (
                    SGR.SGR(SGR.SGRReset.BACKGROUND_COLOR)
                    if reset else
                    ""
                )
            ]

        return self._get_color_sequence(sequence)


    def f_color_default_foreground(
            self,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRReset.FOREGROUND_COLOR),
            self,
        ]

        return self._get_color_sequence(sequence)


    def f_color_default_background(
            self,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRReset.BACKGROUND_COLOR),
            self,
        ]

        return self._get_color_sequence(sequence)


    def f_color_success(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.SUCCESS.value

        if background:
            return self.f_color_background(
                color,
                reset=reset,
            )

        return self.f_color_foreground(
            color,
            reset=reset,
        )


    def f_color_failure(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.FAILURE.value

        if background:
            return self.f_color_background(
                color,
                reset=reset,
            )

        return self.f_color_foreground(
            color,
            reset=reset,
        )


    def f_color_error(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.ERROR.value

        if background:
            return self.f_color_background(
                color,
                reset=reset,
            )

        return self.f_color_foreground(
            color,
            reset=reset,
        )


    def f_color_warning(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.WARNING.value

        if background:
            return self.f_color_background(
                color,
                reset=reset,
            )

        return self.f_color_foreground(
            color,
            reset=reset,
        )


    def f_color_notice(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.NOTICE.value

        if background:
            return self.f_color_background(
                color,
                reset=reset,
            )

        return self.f_color_foreground(
            color,
            reset=reset,
        )


    def f_color_info(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.INFO.value

        if background:
            return self.f_color_background(
                color,
                reset=reset,
            )

        return self.f_color_foreground(
            color,
            reset=reset,
        )


    def f_color_debug(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.DEBUG.value

        if background:
            return self.f_color_background(
                color,
                reset=reset,
            )

        return self.f_color_foreground(
            color,
            reset=reset,
        )


    def f_color_critical(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.CRITICAL.value

        if background:
            return self.f_color_background(
                color,
                reset=reset,
            )

        return self.f_color_foreground(
            color,
            reset=reset,
        )


__all__ = [
    'Color',
]
