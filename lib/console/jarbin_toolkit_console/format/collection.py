# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : collection.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.format.enums import FormatOrder
from jarbin_toolkit_console.enums import PresetSymbol


class Collection:


    def _get_collection_text(
            self,
            collection,
        ):

        if not getattr(self, "_can_format", False):
            return self

        return self.__class__("".join(map(str, collection)))


    def f_collection_list(
            self,
            *,
            marker = PresetSymbol.BULLET,
            split = "\n",
        ):

        new_text = [
            f"{marker} {line}"
            for line in self.split(split)
        ]

        return self._get_collection_text("\n".join(new_text))


    def f_collection_numbered_list(
            self,
            *,
            start = 1,
            separator = ". ",
            split = "\n",
        ):

        lines = self.split(split)
        new_text = []
        len_num = len(str(len(lines) + start))

        for line in range(0, len(lines)):
            new_text.append(f"{line + start:0{len_num}d}{separator}{lines[line]}")

        return self._get_layout_text("\n".join(new_text))


    def f_collection_checklist(
            self,
            checked,
            *,
            marker_unchecked = PresetSymbol.UNCHECKED,
            marker_checked = PresetSymbol.CHECKED,
            split = "\n",
        ):

        lines = self.split(split)

        if len(checked) != len(lines):
            raise ValueError("Checked must be the same length as the number of items")

        new_text = [
            f"{marker_checked if checked[line] else marker_unchecked} {lines[line]}"
            for line in range(len(lines))
        ]

        return self._get_collection_text("\n".join(new_text))


__all__ = [
    'Collection',
]
