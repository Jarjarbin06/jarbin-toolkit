# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : collection.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.format.enums import FormatStrength
from jarbin_toolkit_console.enums import (
    PresetSymbol,
    PresetBox,
    PresetBorder,
)


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
            items,
            *,
            marker = PresetSymbol.BULLET,
        ):

        new_text = [
            f"{marker} {line}"
            for line in items
        ]

        return self._get_collection_text("\n".join(new_text))


    def f_collection_numbered_list(
            self,
            items,
            *,
            start = 1,
            separator = ". ",
        ):

        new_text = []

        len_items = len(items)
        len_num = len(str(len_items + start))

        for line in range(0, len_items):
            new_text.append(f"{line + start:0{len_num}d}{separator}{items[line]}")

        return self._get_collection_text("\n".join(new_text))


    def f_collection_checklist(
            self,
            checked,
            items,
            *,
            marker_unchecked = PresetSymbol.UNCHECKED,
            marker_checked = PresetSymbol.CHECKED,
        ):

        len_items = len(items)

        if len(checked) != len_items:
            raise ValueError("Checked must be the same length as the number of items")

        new_text = [
            f"{marker_checked if checked[line] else marker_unchecked} {items[line]}"
            for line in range(len_items)
        ]

        return self._get_collection_text("\n".join(new_text))


    def f_collection_list_item(
            self,
            item,
            *,
            marker=PresetSymbol.BULLET,
        ):

        return self._get_collection_text(f"{marker} {item}")


    def f_collection_tree_item(
            self,
            item,
            *,
            depth = 0,
            last = False,
            parents = None,
            strength = FormatStrength.LIGHT,
        ):

        if depth == 0:
            return self._get_collection_text(str(item))

        if parents is None:
            parents = [False] * (depth - 1)

        if len(parents) != depth - 1:
            raise ValueError(
                "parents must contain one value for each parent level"
            )

        if strength == FormatStrength.LIGHT:
            vertical = PresetBox.LIGHT_VERTICAL
            horizontal = PresetBox.LIGHT_HORIZONTAL
            corner = PresetBox.LIGHT_CORNER_BOTTOM_LEFT
            tee = PresetBox.LIGHT_TEE_LEFT

        elif strength == FormatStrength.HEAVY:
            vertical = PresetBox.HEAVY_VERTICAL
            horizontal = PresetBox.HEAVY_HORIZONTAL
            corner = PresetBox.HEAVY_CORNER_BOTTOM_LEFT
            tee = PresetBox.HEAVY_TEE_LEFT

        elif strength == FormatStrength.DOUBLE:
            vertical = PresetBox.DOUBLE_VERTICAL
            horizontal = PresetBox.DOUBLE_HORIZONTAL
            corner = PresetBox.DOUBLE_CORNER_BOTTOM_LEFT
            tee = PresetBox.DOUBLE_TEE_LEFT

        elif strength == FormatStrength.ROUND:
            vertical = PresetBox.ROUND_VERTICAL
            horizontal = PresetBox.ROUND_HORIZONTAL
            corner = PresetBox.ROUND_CORNER_BOTTOM_LEFT
            tee = PresetBox.ROUND_TEE_LEFT

        elif strength == FormatStrength.ASCII:
            vertical = PresetBox.ASCII_VERTICAL
            horizontal = PresetBox.ASCII_HORIZONTAL
            corner = PresetBox.ASCII_CORNER_BOTTOM_LEFT
            tee = PresetBox.ASCII_TEE_LEFT

        else:
            raise ValueError(f"Unsupported format strength: {strength}")

        indent = "".join(
            "    " if parent_last else f"{vertical}   "
            for parent_last in parents
        )

        connector = corner if last else tee

        new_text = [
            indent,
            connector,
            horizontal,
            horizontal,
            " ",
            str(item),
        ]

        return self._get_collection_text("".join(new_text))


    def f_collection_tree_branch(
            self,
            items,
            *,
            depth = 0,
            parents = None,
            strength = FormatStrength.LIGHT,
        ):

        if parents is None:
            parents = []

        if not hasattr(items, "__iter__") or isinstance(items, str):
            raise TypeError("items must be an iterable of tree items")

        items = list(items)
        result = []

        for index, item in enumerate(items):
            item_last = index == len(items) - 1

            if isinstance(item, tuple):
                if len(item) != 2:
                    raise ValueError(
                        "Tree branches must contain an item and its children"
                    )

                value, children = item
            else:
                value = item
                children = None

            result.append(
                self.f_collection_tree_item(
                    value,
                    depth=depth,
                    last=item_last,
                    parents=parents,
                    strength=strength,
                )
            )

            if children is not None:
                result.append(
                    self.f_collection_tree_branch(
                        children,
                        depth=depth + 1,
                        parents=[
                            *parents,
                            item_last,
                        ],
                        strength=strength,
                    )
                )

        return self._get_collection_text("\n".join(map(str, result)))


    def f_collection_tree(
            self,
            items,
            *,
            prefix = "",
            strength = FormatStrength.LIGHT,
        ):

        if not hasattr(items, "__iter__") or isinstance(items, str):
            raise TypeError("items must be an iterable of tree items")

        if not isinstance(prefix, str):
            raise TypeError("prefix must be a string")

        tree = f"{self}\n{self.f_collection_tree_branch(items, depth=1, strength=strength)}"

        if prefix:
            tree = "\n".join(
                f"{prefix}{line}"
                for line in str(tree).splitlines()
            )

        return self._get_collection_text(tree)


    def f_collection_key_value(
            self,
            key,
            value,
            *,
            separator = ": ",
        ):

        return self._get_collection_text(f"{key}{separator}{value}")


    def f_collection_key_values(
            self,
            values,
            *,
            separator = ": ",
        ):

        new_text = [
            f"{key}{separator}{value}"
            for key, value in values.items()
        ]

        return self._get_collection_text("\n".join(new_text))


    def f_collection_code_block(
            self,
            *lines,
            language = "Code",
            border = PresetBorder.SINGLE,
        ):

        new_text = self

        if lines:
            new_text = "\n".join(lines)

        return self.__class__(new_text).f_border_title(language.upper(), border=border)


__all__ = [
    'Collection',
]
