# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : layout.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.format.enums import FormatPaddingPosition


class Layout:


    def _get_layout_text(
            self,
            sequence,
        ):

        if not getattr(self, "_can_format", False):
            return self

        return self.__class__("".join(map(str, sequence)))


    def f_layout_pad(
            self,
            width,
            *,
            fill = " ",
            align = FormatPaddingPosition.LEFT,
        ):

        if len(fill) != 1:
            raise ValueError("Fill character must be a single character")

        if width < 0:
            raise ValueError("Width must be non-negative")

        remaining_width = width - len(self)

        new_text = self

        if align == FormatPaddingPosition.LEFT:
            new_text = (fill * remaining_width) + self[:width]

        elif align == FormatPaddingPosition.CENTER:
            half_remaining = remaining_width // 2
            half_remaining_r = remaining_width % 2

            new_text = (fill * half_remaining) + self[:width] + (fill * (half_remaining + half_remaining_r))

        elif align == FormatPaddingPosition.RIGHT:
            new_text = self[:width] + (fill * remaining_width)

        return self._get_layout_text(new_text)


    def f_layout_pad_left(
            self,
            width,
            *,
            fill = " ",
        ):

        return self.f_layout_pad(width, fill=fill, align=FormatPaddingPosition.LEFT)


    def f_layout_pad_center(
            self,
            width,
            *,
            fill = " ",
        ):

        return self.f_layout_pad(width, fill=fill, align=FormatPaddingPosition.CENTER)


    def f_layout_pad_right(
            self,
            width,
            *,
            fill = " ",
        ):

        return self.f_layout_pad(width, fill=fill, align=FormatPaddingPosition.RIGHT)
