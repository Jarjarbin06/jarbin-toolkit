from jarbin_toolkit_console.text import Text
from jarbin_toolkit_console.color import (
    ColorRGB,
    Color256,
    ColorHEX,
)
from jarbin_toolkit_console.enums import PresetColor


class Style:


    def _get_sequence(
            self,
            sequence: Text,
        ) -> Text:
        ...


    def f_style_reset(
            self,
        ) -> Text:

        SGR = self._get_sgr()

        sequence = [
            SGR.SGR(SGR.SGRReset.ALL),
            self
        ]

        return self._get_sequence(sequence)


    def f_style_bold(
            self,
            *,
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

        return self.f_style_faint(reset=reset)


    def f_style_italic(
            self,
            *,
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

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
            is_fast: bool = False,
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

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
            reset: bool = True,
        ) -> Text:

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
            color: Color256 | ColorRGB | ColorHEX = ColorRGB(255, 255, 255),
            *,
            reset: bool = True,
        ) -> Text:
        """
            Set foreground color

            Parameters
            ----------
            color : Color256 | ColorRGB | ColorHEX
                Color object

            reset : bool
                Reset formatting after applying style

            Returns
            ----------
            Text
                Styled text
        """
        ...


    def f_style_background(
            self,
            color: Color256 | ColorRGB | ColorHEX = ColorRGB(255, 255, 255),
            *,
            reset: bool = True,
        ) -> Text:
        """
            Set background color

            Parameters
            ----------
            color : Color256 | ColorRGB | ColorHEX
                Color object

            reset : bool
                Reset formatting after applying style

            Returns
            ----------
            Text
                Styled text
        """
        ...


    def f_style_default_foreground(
            self,
        ) -> Text:
        """
            Set default foreground color

            Returns
            ----------
            Text
                Styled text
        """
        ...


    def f_style_default_background(
            self,
        ) -> Text:
        """
            Set default background color

            Returns
            ----------
            Text
                Styled text
        """
        ...


    def f_style_success(
            self,
            *,
            background: bool = False,
            reset: bool = True,
        ) -> Text:
        """
            Success preset color

            Parameters
            ----------
            background : bool
                Set color to background (default to foreground)

            reset : bool
                Reset formatting after applying style

            Returns
            ----------
            Text
                Styled text
        """
        ...


    def f_style_failure(
            self,
            *,
            background: bool = False,
            reset: bool = True,
        ) -> Text:
        """
            Failure preset color

            Parameters
            ----------
            background : bool
                Set color to background (default to foreground)

            reset : bool
                Reset formatting after applying style

            Returns
            ----------
            Text
                Styled text
        """
        ...


    def f_style_error(
            self,
            *,
            background: bool = False,
            reset: bool = True,
        ) -> Text:
        """
            Error preset color

            Parameters
            ----------
            background : bool
                Set color to background (default to foreground)

            reset : bool
                Reset formatting after applying style

            Returns
            ----------
            Text
                Styled text
        """
        ...


    def f_style_warning(
            self,
            *,
            background: bool = False,
            reset: bool = True,
        ) -> Text:
        """
            Warning preset color

            Parameters
            ----------
            background : bool
                Set color to background (default to foreground)

            reset : bool
                Reset formatting after applying style

            Returns
            ----------
            Text
                Styled text
        """
        ...


    def f_style_notice(
            self,
            *,
            background: bool = False,
            reset: bool = True,
        ) -> Text:
        """
            Notice preset color

            Parameters
            ----------
            background : bool
                Set color to background (default to foreground)

            reset : bool
                Reset formatting after applying style

            Returns
            ----------
            Text
                Styled text
        """
        ...


    def f_style_info(
            self,
            *,
            background: bool = False,
            reset: bool = True,
        ) -> Text:
        """
            Info preset color

            Parameters
            ----------
            background : bool
                Set color to background (default to foreground)

            reset : bool
                Reset formatting after applying style

            Returns
            ----------
            Text
                Styled text
        """
        ...


    def f_style_debug(
            self,
            *,
            background: bool = False,
            reset: bool = True,
        ) -> Text:
        """
            Debug preset color

            Parameters
            ----------
            background : bool
                Set color to background (default to foreground)

            reset : bool
                Reset formatting after applying style

            Returns
            ----------
            Text
                Styled text
        """
        ...


    def f_style_critical(
            self,
            *,
            background: bool = False,
            reset: bool = True,
        ) -> Text:
        """
            Critical preset color
        
            Parameters
            ----------
            background : bool
                Set color to background (default to foreground)

            reset : bool
                Reset formatting after applying style
        
            Returns
            ----------
            Text
                Styled text
        """
        ...
