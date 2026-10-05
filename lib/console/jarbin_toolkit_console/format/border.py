# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : border.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.enums import PresetBorder


class Border:


    def _get_border_text(
            self,
            border,
        ):

        if not getattr(self, "_can_format", False):
            return self

        return self.__class__("".join(map(str, border)))


    def _get_border_lines(
            self,
        ):

        lines = self.splitlines()

        if not lines:
            return [""]

        return lines


    def _get_border_width(
            self,
            lines,
        ):

        return max(len(line) for line in lines)


    def f_border_top(
            self,
            *,
            border = PresetBorder.SINGLE,
            padding = 0,
        ):

        if padding < 0:
            raise ValueError("Padding cannot be negative")

        h, _, _, _, _, _ = border.value

        lines = self._get_border_lines()
        width = self._get_border_width(lines)

        pad = [" " * width for _ in range(padding)]

        new_text = [
            h * width,
            *pad,
            *lines,
        ]

        return self._get_border_text("\n".join(new_text))


    def f_border_bottom(
            self,
            *,
            border = PresetBorder.SINGLE,
            padding = 0,
        ):

        if padding < 0:
            raise ValueError("Padding cannot be negative")

        h, _, _, _, _, _ = border.value

        lines = self._get_border_lines()
        width = self._get_border_width(lines)

        pad = [" " * width for _ in range(padding)]

        new_text = [
            *lines,
            *pad,
            h * width,
        ]

        return self._get_border_text("\n".join(new_text))


    def f_border_left(
            self,
            *,
            border = PresetBorder.SINGLE,
            padding = 0,
        ):

        if padding < 0:
            raise ValueError("Padding cannot be negative")

        _, v, _, _, _, _ = border.value

        lines = self._get_border_lines()
        horizontal_padding = "  " * padding

        new_text = []

        for line in lines:
            new_text.append(
                f"{v}{horizontal_padding}{line}"
            )

        return self._get_border_text("\n".join(new_text))


    def f_border_right(
            self,
            *,
            border = PresetBorder.SINGLE,
            padding = 0,
        ):

        if padding < 0:
            raise ValueError("Padding cannot be negative")

        _, v, _, _, _, _ = border.value

        lines = self._get_border_lines()
        horizontal_padding = "  " * padding

        new_text = []

        for line in lines:
            new_text.append(
                f"{line}{horizontal_padding}{v}"
            )

        return self._get_border_text("\n".join(new_text))


    def f_border_box(
            self,
            *,
            border=PresetBorder.SINGLE,
            padding=0,
        ):

        if padding < 0:
            raise ValueError("Padding cannot be negative")

        h, v, tl, tr, bl, br = border.value

        lines = self._get_border_lines()
        width = self._get_border_width(lines)

        horizontal_padding = "  " * padding
        vertical_padding = [
            f"{v}{' ' * (width + (padding * 4))}{v}"
            for _ in range(padding)
        ]

        content = []

        for line in lines:
            content.append(
                f"{v}"
                f"{horizontal_padding}"
                f"{line}"
                f"{' ' * (width - len(line))}"
                f"{horizontal_padding}"
                f"{v}"
            )

        top = (
                tl
                + h * (width + (padding * 4))
                + tr
        )

        bottom = (
                bl
                + h * (width + (padding * 4))
                + br
        )

        new_text = [
            top,
            *vertical_padding,
            *content,
            *vertical_padding,
            bottom,
        ]

        return self._get_border_text("\n".join(new_text))


    def f_border_separator(
            self,
            *,
            border = PresetBorder.SINGLE,
        ):

        h, _, _, _, _, _ = border.value

        lines = self._get_border_lines()
        width = self._get_border_width(lines)

        new_text = [
            h * width
        ]

        return self._get_border_text("\n".join(new_text))


    def f_border_single(
            self,
        ):

        return self.f_border_box(border=PresetBorder.SINGLE)


    def f_border_double(
            self,
        ):

        return self.f_border_box(border=PresetBorder.DOUBLE)


    def f_border_heavy(
            self,
        ):

        return self.f_border_box(border=PresetBorder.HEAVY)


    def f_border_rounded(
            self,
        ):

        return self.f_border_box(border=PresetBorder.ROUNDED)


    def f_border_ascii(
            self,
        ):

        return self.f_border_box(border=PresetBorder.ASCII)


    def f_border_title(
            self,
            title,
            *,
            border=PresetBorder.SINGLE,
            padding=0,
        ):

        if padding < 0:
            raise ValueError("Padding cannot be negative")

        h, v, tl, tr, bl, br = border.value

        lines = self._get_border_lines()
        width = self._get_border_width(lines)

        horizontal_padding = " " * (padding * 2)
        padding_width = padding * 4

        content_width = max(
            width + padding_width,
            len(title) + 2 + padding_width,
        )

        vertical_padding = [
            f"{v}{' ' * content_width}{v}"
            for _ in range(padding)
        ]

        content = []

        for line in lines:
            content.append(
                f"{v}"
                f"{horizontal_padding}"
                f"{line}"
                f"{' ' * (content_width - len(line) - padding * 4)}"
                f"{horizontal_padding}"
                f"{v}"
            )

        title_line = (
            f"{tl}"
            f"{h * (padding * 2)}"
            f" {title} "
            f"{h * (content_width - (padding * 2) - len(title) - 2)}"
            f"{tr}"
        )

        bottom = (
                bl
                + h * content_width
                + br
        )

        new_text = [
            title_line,
            *vertical_padding,
            *content,
            *vertical_padding,
            bottom,
        ]

        return self._get_border_text("\n".join(new_text))
