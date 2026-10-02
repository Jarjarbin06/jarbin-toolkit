# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : style.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.color import (
    ColorRGB,
    Color256,
    ColorHEX,
)
from jarbin_toolkit_console.enums import PresetColor


class Style:


    def _get_sequence(
            self,
            sequence,
        ):

        if not getattr(self, "_can_format", False):
            return self

        return self.__class__("".join(map(str, sequence)))


    def f_style_reset(
            self,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRReset.ALL),
            self
        ]

        return self._get_sequence(sequence)


    def f_style_bold(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRAttribute.BOLD),
            self,
            (
                SGR.SGR(SGR.SGRReset.BOLD)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_faint(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRAttribute.FAINT),
            self,
            (
                SGR.SGR(SGR.SGRReset.FAINT)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_dim(
            self,
            *,
            reset = True,
        ):

        return self.f_style_faint(reset=reset)


    def f_style_italic(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRAttribute.ITALIC),
            self,
            (
                SGR.SGR(SGR.SGRReset.ITALIC)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_underline(
            self,
            *,
            style = None,
            color = None,
            reset = True,
        ):

        SGR = self._get_sgr()

        if style is not None:

            if color:
                mode = SGR.SGRColorMode.RGB if isinstance(color, ColorRGB) else SGR.SGRColorMode.INDEXED

                sequence = [
                    SGR.SGR(style, SGR.SGRColorExtender.UNDERLINE, mode, color),
                    self,
                    (
                        SGR.SGR(SGR.SGRReset.UNDERLINE)
                        if reset else
                        ""
                    )
                ]

            else:
                sequence = [
                    SGR.SGR(style),
                    self,
                    (
                        SGR.SGR(SGR.SGRReset.UNDERLINE)
                        if reset else
                        ""
                    )
                ]

        else:

            sequence = [
                SGR.SGR(SGR.SGRAttribute.UNDERLINE),
                self,
                (
                    SGR.SGR(SGR.SGRReset.UNDERLINE)
                    if reset else
                    ""
                )
            ]

        return self._get_sequence(sequence)


    def f_style_strikethrough(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRAttribute.STRIKETHROUGH),
            self,
            (
                SGR.SGR(SGR.SGRReset.STRIKETHROUGH)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_blink(
            self,
            *,
            is_fast = False,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRAttribute.FAST_BLINK if is_fast else SGR.SGRAttribute.SLOW_BLINK),
            self,
            (
                SGR.SGR(SGR.SGRReset.BLINK)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_reverse(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRAttribute.REVERSE),
            self,
            (
                SGR.SGR(SGR.SGRReset.REVERSE)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_hide(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRAttribute.HIDE),
            self,
            (
                SGR.SGR(SGR.SGRReset.HIDE)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_show(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRReset.HIDE),
            self,
            (
                SGR.SGR(SGR.SGRAttribute.HIDE)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_frame(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRDecoration.FRAME),
            self,
            (
                SGR.SGR(SGR.SGRReset.FRAME)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_encircle(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRDecoration.ENCIRCLE),
            self,
            (
                SGR.SGR(SGR.SGRReset.ENCIRCLE)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_overline(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRDecoration.OVERLINE),
            self,
            (
                SGR.SGR(SGR.SGRReset.OVERLINE)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_superscript(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRPosition.SUPERSCRIPT),
            self,
            (
                SGR.SGR(SGR.SGRPosition.NORMAL)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_subscript(
            self,
            *,
            reset = True,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRPosition.SUBSCRIPT),
            self,
            (
                SGR.SGR(SGR.SGRPosition.NORMAL)
                if reset else
                ""
            )
        ]

        return self._get_sequence(sequence)


    def f_style_foreground(
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

        return self._get_sequence(sequence)


    def f_style_background(
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

        return self._get_sequence(sequence)


    def f_style_default_foreground(
            self,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRReset.FOREGROUND_COLOR),
            self,
        ]

        return self._get_sequence(sequence)


    def f_style_default_background(
            self,
        ):

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRReset.BACKGROUND_COLOR),
            self,
        ]

        return self._get_sequence(sequence)


    def f_style_success(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.SUCCESS.value

        if background:
            return self.f_style_background(
                color,
                reset=reset,
            )

        return self.f_style_foreground(
            color,
            reset=reset,
        )


    def f_style_failure(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.FAILURE.value

        if background:
            return self.f_style_background(
                color,
                reset=reset,
            )

        return self.f_style_foreground(
            color,
            reset=reset,
        )


    def f_style_error(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.ERROR.value

        if background:
            return self.f_style_background(
                color,
                reset=reset,
            )

        return self.f_style_foreground(
            color,
            reset=reset,
        )


    def f_style_warning(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.WARNING.value

        if background:
            return self.f_style_background(
                color,
                reset=reset,
            )

        return self.f_style_foreground(
            color,
            reset=reset,
        )


    def f_style_notice(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.NOTICE.value

        if background:
            return self.f_style_background(
                color,
                reset=reset,
            )

        return self.f_style_foreground(
            color,
            reset=reset,
        )


    def f_style_info(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.INFO.value

        if background:
            return self.f_style_background(
                color,
                reset=reset,
            )

        return self.f_style_foreground(
            color,
            reset=reset,
        )


    def f_style_debug(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.DEBUG.value

        if background:
            return self.f_style_background(
                color,
                reset=reset,
            )

        return self.f_style_foreground(
            color,
            reset=reset,
        )


    def f_style_critical(
            self,
            *,
            background = False,
            reset = True,
        ):

        color = PresetColor.CRITICAL.value

        if background:
            return self.f_style_background(
                color,
                reset=reset,
            )

        return self.f_style_foreground(
            color,
            reset=reset,
        )
