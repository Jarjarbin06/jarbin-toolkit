from typing import Any, Optional

from jarbin_toolkit_console.enums import PresetSymbol
from jarbin_toolkit_console.text import Text
from .enums import FormatPosition


class Layout:
    """
        Layout formatting
    """


    def f_layout_pad(
            self,
            amount: int,
            *,
            fill: str = " ",
            align: FormatPosition = FormatPosition.LEFT,
        ) -> Text:
        """
            Pad text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_pad_left(
            self,
            amount: int,
            *,
            fill: str = " ",
        ) -> Text:
        """
            Pad on left of text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_pad_center(
            self,
            amount: int,
            *,
            fill: str = " ",
        ) -> Text:
        """
            Pad around the text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_pad_right(
            self,
            amount: int,
            *,
            fill: str = " ",
        ) -> Text:
        """
            Pad on right of text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_align(
            self,
            width: int,
            *,
            align: FormatPosition = FormatPosition.LEFT,
        ) -> Text:
        """
            Align text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_align_left(
            self,
            width: int,
        ) -> Text:
        """
            Align text on left

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_align_center(
            self,
            width: int,
        ) -> Text:
        """
            Align text on center

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_align_right(
            self,
            width: int,
        ) -> Text:
        """
            Align text on right

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_indent(
            self,
            indent: int = 1,
            *,
            width: int = 4,
            fill: str = " ",
            first_line: Optional[str] = None,
        ) -> Text:
        """
            Indent text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_dedent(
            self,
            fill: str = " ",
        ) -> Text:
        """
            Dedent text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_get_width(
            self,
        ) -> int:
        """
            Get text's width

            Returns
            ----------
            int
                Text width
        """
        ...


    def f_layout_get_height(
            self,
        ) -> int:
        """
            Get text's height

            Returns
            ----------
            int
                Text height
        """
        ...


    def f_layout_wrap(
            self,
            width: int,
            *,
            break_long_words: bool = False,
        ) -> Text:
        """
            Wrap text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_truncate(
            self,
            width: int,
            *,
            suffix: PresetSymbol | str = PresetSymbol.ELLIPSIS,
            break_long_words: bool = False,
        ) -> Text:
        """
            Truncate text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_lines(
            self,
        ) -> list[Text]:
        """
            Get text's lines

            Returns
            ----------
            list[Text]
                Lines
        """
        ...


    def f_layout_first_line(
            self,
        ) -> Text:
        """
            Get first line of text

            Returns
            ----------
            Text
                First line
        """
        ...


    def f_layout_last_line(
            self,
        ) -> Text:
        """
            Get last line of text

            Returns
            ----------
            Text
                Last line
        """
        ...


    def f_layout_prefix_lines(
            self,
            prefix: str,
        ) -> Text:
        """
            Add prefix to text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_suffix_lines(
            self,
            suffix: str,
        ) -> Text:
        """
            Add suffix to text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_number_lines(
            self,
            start: int = 1,
            separator: str = ". ",
        ) -> Text:
        """
            Add line numbers to text

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_reverse_lines(
            self,
        ) -> Text:
        """
            Reverse text's lines

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_hyperlink(
            self,
            *,
            link: str = None,
        ):
        """
            Create a hyperlink

            Returns
            ----------
            Text
                New format
        """
        ...


    def f_layout_file_link(
            self,
            *,
            file: str = None,
        ):
        """
            Create a file link

            Returns
            ----------
            Text
                New format
        """
        ...


    def _get_layout_text(
            self,
            layout: Any,
        ) -> Text:
        ...


__all__ = [
    'Layout',
]
