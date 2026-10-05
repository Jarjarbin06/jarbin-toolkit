# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : layout.py
#
# Author       : Jarjarbin06
# ============================================================================


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
            raise ValueError("Fill character must be a single character")

        if amount < 0:
            raise ValueError("Amount must be non-negative")

        new_text = self

        if align == FormatPosition.LEFT:
            new_text = (fill * amount) + self

        elif align == FormatPosition.CENTER:
            half_amount = amount // 2
            half_amount_r = amount % 2

            new_text = (fill * half_amount) + self + (fill * (half_amount + half_amount_r))

        elif align == FormatPosition.RIGHT:
            new_text = self + (fill * amount)

        return self._get_layout_text(new_text)


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
            raise ValueError("Width must be non-negative")

        remaining_width = width - len(self)

        new_text = self

        if remaining_width < 1 or align == FormatPosition.LEFT:
            new_text = Cursor.CursorPosition.column(1) + self[:width]

        elif align == FormatPosition.CENTER:
            new_text = Cursor.CursorPosition.column(remaining_width // 2 + 1) + self[:width]

        elif align == FormatPosition.RIGHT:
            new_text = Cursor.CursorPosition.column(remaining_width + 1) + self[:width]

        return self._get_layout_text(new_text)


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
            width = 4,
            *,
            fill = " ",
            first_line = None,
        ):

        new_text = []

        for line in self.splitlines():
            new_text.append(f"{fill * width}{line}")

        if first_line is not None:
            new_text[0] = f"{first_line}{new_text[0]}"

        return self._get_layout_text(new_text)


    def f_layout_dedent(
            self,
            fill = " ",
        ):

        new_text = []

        for line in self.splitlines():
            new_text.append(line.removeprefix(fill))

        return self._get_layout_text(new_text)


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
            break_long_words=False,
        ):

        if width <= 0:
            raise ValueError("Width must be greater than zero")

        if not isinstance(break_long_words, bool):
            raise TypeError("break_long_words must be a boolean")

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
            suffix="…",
            break_long_words=False,
        ):

        if width < 0:
            raise ValueError("Width must be non-negative")

        if not isinstance(suffix, str):
            raise TypeError("Suffix must be a string")

        if not isinstance(break_long_words, bool):
            raise TypeError("break_long_words must be a boolean")

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

        return self.splitlines()


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
        len_num = len(str(len(lines) + start))

        for line in range(0, len(lines)):
            new_text.append(f"{line + start:0{len_num}d}{separator}{lines[line]}")

        return self._get_layout_text("\n".join(new_text))


    def f_layout_reverse_lines(
            self,
        ):

        new_text: list = self.splitlines().reverse()

        return self._get_layout_text("\n".join(new_text))


__all__ = [
    'Layout',
]
