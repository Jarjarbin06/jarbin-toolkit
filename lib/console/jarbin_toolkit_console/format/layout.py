# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : layout.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.error import ConsoleJError
from jarbin_toolkit_console.enums import PresetSymbol
from jarbin_toolkit_console.format.enums import FormatPosition


class Layout:


    def _get_layout_text(
            self,
            layout,
        ):

        if not getattr(self, "_can_format", False):
            return self

        return self.__class__("".join(map(str, layout)))


    def f_layout_pad(
            self,
            amount,
            *,
            fill = " ",
            align = FormatPosition.LEFT,
        ):

        if len(fill) != 1:
            raise ConsoleJError("Fill character must be a single character")

        if amount < 0:
            raise ConsoleJError("Amount must be non-negative")

        lines = self.splitlines()
        new_text = []

        for line in lines:

            if align == FormatPosition.LEFT:
                new_text.append(f"{fill * amount}{line}")

            elif align == FormatPosition.CENTER:
                half_amount = amount // 2
                half_amount_r = amount % 2

                new_text.append(f"{fill * half_amount}{line}{fill * (half_amount + half_amount_r)}")

            elif align == FormatPosition.RIGHT:
                new_text.append(f"{line}{fill * amount}")

        return self._get_layout_text("\n".join(new_text))


    def f_layout_pad_left(
            self,
            amount,
            *,
            fill = " ",
        ):

        return self.f_layout_pad(amount, fill=fill, align=FormatPosition.LEFT)


    def f_layout_pad_center(
            self,
            amount,
            *,
            fill = " ",
        ):

        return self.f_layout_pad(amount, fill=fill, align=FormatPosition.CENTER)


    def f_layout_pad_right(
            self,
            amount,
            *,
            fill = " ",
        ):

        return self.f_layout_pad(amount, fill=fill, align=FormatPosition.RIGHT)


    def f_layout_align(
            self,
            width,
            *,
            align = FormatPosition.LEFT,
        ):

        Cursor = self._get_cursor()

        if width < 0:
            raise ConsoleJError("Width must be non-negative")

        lines = self.splitlines()
        new_text = []

        for line in lines:

            remaining_width = width - len(line)

            if remaining_width < 1 or align == FormatPosition.LEFT:
                new_text.append(f"{Cursor.CursorPosition.column(1)}{line[:width]}")

            elif align == FormatPosition.CENTER:
                new_text.append(f"{Cursor.CursorPosition.column(remaining_width // 2 + 1)}{line[:width]}")

            elif align == FormatPosition.RIGHT:
                new_text.append(f"{Cursor.CursorPosition.column(remaining_width + 1)}{line[:width]}")

        return self._get_layout_text("\n".join(new_text))


    def f_layout_align_left(
            self,
            width,
        ):

        return self.f_layout_align(width, align=FormatPosition.LEFT)


    def f_layout_align_center(
            self,
            width,
        ):

        return self.f_layout_align(width, align=FormatPosition.CENTER)


    def f_layout_align_right(
            self,
            width,
        ):

        return self.f_layout_align(width, align=FormatPosition.RIGHT)


    def f_layout_indent(
            self,
            indent = 1,
            *,
            width = 4,
            fill = " ",
            first_line = None,
        ):

        if width == 0 and first_line is None:
            return self

        new_text = []

        for line in self.splitlines():
            new_text.append(f"{(fill * width) * indent}{line}")

        if first_line is not None:
            new_text[0] = f"{first_line}{new_text[0]}"

        return self._get_layout_text("\n".join(new_text))


    def f_layout_dedent(
            self,
            fill = " ",
        ):

        lines = self.splitlines()

        if not lines:
            return self

        indent = min(
            len(line) - len(line.lstrip(fill))
            for line in lines
            if line
        )

        new_text = [
            line[indent:]
            for line in lines
        ]

        return self._get_layout_text("\n".join(new_text))


    def f_layout_get_width(
            self,
        ):

        return max(len(line) for line in self.splitlines())


    def f_layout_get_height(
            self,
        ):

        return len(self.splitlines())


    def f_layout_wrap(
            self,
            width,
            *,
            break_long_words = False,
        ):

        if width <= 0:
            raise ConsoleJError("Width must be greater than zero")

        if not isinstance(break_long_words, bool):
            raise ConsoleJError("break_long_words must be a boolean")

        words = self.split()
        lines = []
        current_line = ""

        for word in words:

            if len(word) > width and break_long_words:
                if current_line:
                    lines.append(current_line)
                    current_line = ""

                while len(word) > width:
                    lines.append(word[:width])
                    word = word[width:]

                if word:
                    current_line = word

                continue

            if not current_line:
                current_line = word
                continue

            if len(current_line) + 1 + len(word) <= width:
                current_line += " " + word
                continue

            lines.append(current_line)
            current_line = word

        if current_line:
            lines.append(current_line)

        return self._get_layout_text("\n".join(lines))


    def f_layout_truncate(
            self,
            width,
            *,
            suffix = PresetSymbol.ELLIPSIS,
            break_long_words = False,
        ):

        if width < 0:
            raise ConsoleJError("Width must be non-negative")

        if not isinstance(suffix, str):
            raise ConsoleJError("Suffix must be a string")

        if not isinstance(break_long_words, bool):
            raise ConsoleJError("break_long_words must be a boolean")

        if len(self) <= width:
            return self

        if len(suffix) >= width:
            return self._get_layout_text(suffix[:width])

        available_width = width - len(suffix)
        text = self[:available_width]

        if not break_long_words and available_width < len(self):
            previous_char = text[-1:]
            next_char = self[available_width:available_width + 1]

            previous_is_word = (
                    previous_char.isalnum()
                    or previous_char == "_"
            )

            next_is_word = (
                    next_char.isalnum()
                    or next_char == "_"
            )

            if (
                    previous_char
                    and next_char
                    and previous_is_word
                    and next_is_word
            ):
                last_space = text.rfind(" ")

                if last_space != -1:
                    text = text[:last_space]

        return self._get_layout_text(text.rstrip() + suffix)


    def f_layout_lines(
            self,
        ):

        return [self.__class__(line) for line in self.splitlines()]


    def f_layout_first_line(
            self,
        ):

        return self.f_layout_lines()[0]


    def f_layout_last_line(
            self,
        ):

        return self.f_layout_lines()[-1]


    def f_layout_prefix_lines(
            self,
            prefix,
        ):

        new_text = []

        for line in self.splitlines():
            new_text.append(f"{prefix}{line}")

        return self._get_layout_text("\n".join(new_text))


    def f_layout_suffix_lines(
            self,
            suffix,
        ):

        new_text = []

        for line in self.splitlines():
            new_text.append(f"{line}{suffix}")

        return self._get_layout_text("\n".join(new_text))


    def f_layout_number_lines(
            self,
            start = 1,
            separator = ". ",
        ):

        lines = self.splitlines()
        new_text = []
        len_num = len(str(len(lines) + start - 1))

        for line in range(0, len(lines)):
            new_text.append(f"{line + start:0{len_num}d}{separator}{lines[line]}")

        return self._get_layout_text("\n".join(new_text))


    def f_layout_reverse_lines(
            self,
        ):

        new_text = self.splitlines()[::-1]

        return self._get_layout_text("\n".join(new_text))


    def f_layout_hyperlink(
            self,
            *,
            link = None,
        ):

        OSC = self._get_osc()

        new_text = [
            OSC.OSCHyperlink.open(link or self),
            self,
            OSC.OSCHyperlink.close(),
        ]

        return self._get_layout_text(new_text)


    def f_layout_file_link(
            self,
            *,
            file = None,
        ):

        OSC = self._get_osc()

        new_text = [
            OSC.OSCFileLink.open(file or self),
            self,
            OSC.OSCFileLink.close(),
        ]

        return self._get_layout_text(new_text)


__all__ = [
    'Layout',
]
