# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Format
# File         : test_format_collection.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console import (
    PresetSymbol,
    PresetBorder,
    Text,
)
from jarbin_toolkit_console.format import FormatStrength


def test_collection_list():
    assert str(
        Text("ignored").f_collection_list(["One", "Two"])
    ) == "• One\n• Two"


def test_collection_list_custom_marker():
    assert str(
        Text("").f_collection_list(
            ["One", "Two"],
            marker="-",
        )
    ) == "- One\n- Two"


@pytest.mark.parametrize(
    "start, expected",
    [
        (1, "1. One\n2. Two\n3. Three"),
        (0, "0. One\n1. Two\n2. Three"),
        (8, "08. One\n09. Two\n10. Three"),
    ],
)
def test_collection_numbered_list(start, expected):
    assert str(
        Text("").f_collection_numbered_list(
            ["One", "Two", "Three"],
            start=start,
        )
    ) == expected


def test_collection_numbered_list_custom_separator():
    assert str(
        Text("").f_collection_numbered_list(
            ["One", "Two"],
            separator=") ",
        )
    ) == "1) One\n2) Two"


def test_collection_checklist():
    assert str(
        Text("").f_collection_checklist(
            [False, True],
            ["Todo", "Done"],
        )
    ) == "☐ Todo\n☑ Done"


def test_collection_checklist_invalid_length():
    with pytest.raises(
        ValueError,
        match="Checked must be the same length as the number of items",
    ):
        Text("").f_collection_checklist(
            [True],
            ["One", "Two"],
        )


def test_collection_checklist_custom_markers():
    assert str(
        Text("").f_collection_checklist(
            [False, True],
            ["Todo", "Done"],
            marker_unchecked="[ ]",
            marker_checked="[x]",
        )
    ) == "[ ] Todo\n[x] Done"


def test_collection_list_item():
    assert str(
        Text("").f_collection_list_item("Hello")
    ) == "• Hello"


def test_collection_tree_item_root():
    assert str(
        Text("").f_collection_tree_item("Root")
    ) == "Root"


@pytest.mark.parametrize(
    "strength",
    list(FormatStrength),
)
def test_collection_tree_item_strength(strength):
    result = str(
        Text("").f_collection_tree_item(
            "Child",
            depth=1,
            last=True,
            strength=strength,
        )
    )

    assert result.endswith(" Child")


def test_collection_tree_item_default_parents():
    assert str(
        Text("").f_collection_tree_item(
            "Child",
            depth=2,
            last=False,
        )
    ) == "│   ├── Child"


def test_collection_tree_item_parent_state():
    assert str(
        Text("").f_collection_tree_item(
            "Grandchild",
            depth=3,
            last=True,
            parents=[False, True],
        )
    ) == "│       └── Grandchild"


def test_collection_tree_item_invalid_parents():
    with pytest.raises(
        ValueError,
        match="parents must contain one value for each parent level",
    ):
        Text("").f_collection_tree_item(
            "Child",
            depth=2,
            parents=[],
        )


def test_collection_tree_branch():
    result = str(
        Text("Title").f_collection_tree(
            [
                ("src", [
                    "main.py",
                    "utils.py",
                ]),
                "README.md",
            ]
        )
    )

    assert result == (
        "Title\n"
        "├── src\n"
        "│   ├── main.py\n"
        "│   └── utils.py\n"
        "└── README.md"
    )


def test_collection_tree_branch_invalid_items():
    with pytest.raises(
        TypeError,
        match="items must be an iterable of tree items",
    ):
        Text("").f_collection_tree_branch("invalid")


def test_collection_tree_branch_invalid_tuple():
    with pytest.raises(
        ValueError,
        match="Tree branches must contain an item and its children",
    ):
        Text("").f_collection_tree_branch(
            [("invalid", "children", "extra")]
        )


def test_collection_tree_prefix():
    assert str(
        Text("Root").f_collection_tree(
            ["Child"],
            prefix="> ",
        )
    ) == "> Root\n> └── Child"


def test_collection_tree_invalid_items():
    with pytest.raises(
        TypeError,
        match="items must be an iterable of tree items",
    ):
        Text("").f_collection_tree("invalid")


def test_collection_tree_invalid_prefix():
    with pytest.raises(TypeError, match="prefix must be a string"):
        Text("").f_collection_tree([], prefix=1)


def test_collection_key_value():
    assert str(
        Text("").f_collection_key_value("name", "Jarbin")
    ) == "name: Jarbin"


def test_collection_key_value_custom_separator():
    assert str(
        Text("").f_collection_key_value("name", "Jarbin", separator=" = ")
    ) == "name = Jarbin"


def test_collection_key_values():
    assert str(
        Text("").f_collection_key_values(
            {"name": "Jarbin", "version": "1.0"}
        )
    ) == "name: Jarbin\nversion: 1.0"


def test_collection_code_block():
    assert str(
        Text("ignored").f_collection_code_block(
            "print('Hello')",
            language="python",
            border=PresetBorder.SINGLE,
        )
    ) == (
        "┌─ PYTHON ─────┐\n"
        "│print('Hello')│\n"
        "└──────────────┘"
    )


def test_collection_code_block_without_lines():
    assert str(
        Text("Hello").f_collection_code_block(language="text")
    ) == (
        "┌─ TEXT ─┐\n"
        "│Hello   │\n"
        "└────────┘"
    )
