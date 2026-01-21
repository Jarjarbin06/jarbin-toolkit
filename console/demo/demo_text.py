#!/usr/bin/env python3
"""
    FULL EPITECH_CONSOLE – TEXT MODULE DEMO
    ======================================

    This script is a REAL MANUAL TEST of the Text module.

    It covers:
    - Text.Text constructor
    - len(Text)
    - reset
    - bold
    - italic
    - underline
    - hide
    - strikthrough
    - error / warning / ok / info (title & non-title)
    - chained formatting
    - reset after formatting
    - Format.apply on:
        - Text
        - str
    - tree() with:
        - dict
        - list
        - str
    - tree indentation
    - tree with title
    - module_tree()
    - url_link
    - file_link
    - mixed usage with ANSI sequences
    - edge cases (empty, nested, overwrite, reset)
    - real terminal rendering

    Run in a REAL terminal.
"""


def text_demo(
    ) -> None:
    from epitech_console import Text, ANSI, System

    Console = System.Console
    Format = Text.Format


    # ============================================================
    # BASIC TEXT CREATION
    # ============================================================

    print("\n=== BASIC TEXT CREATION ===")

    t1 = Text.Text("Hello World")
    Console.print(t1)

    t2 = Text.Text(123)
    Console.print(t2)

    t3 = Text.Text(["a", "b", "c"])
    Console.print(t3)

    print("\n(Text.Text accepts any object)")


    # ============================================================
    # LEN(TEXT) COMPATIBILITY
    # ============================================================

    print("\n=== LEN(TEXT) ===")

    t = Text.Text("abcdef")
    Console.print(f"Text: {t}")
    Console.print(f"len(Text) = {len(t)}")

    print("\n(len(Text) matches string length)")


    # ============================================================
    # BASIC FORMATTING
    # ============================================================

    print("\n=== BASIC FORMATTING ===")

    Console.print(Text.Text("Bold text").bold())
    Console.print(Text.Text("Italic text").italic())
    Console.print(Text.Text("Underline text").underline())
    Console.print(Text.Text("Hidden text").hide())
    Console.print(Text.Text("Strikethrough text").strikethrough())

    print("\n(All basic formatting styles rendered)")


    # ============================================================
    # FORMAT RESET
    # ============================================================

    print("\n=== FORMAT RESET ===")

    t = Text.Text("Formatted then reset")
    t.bold().underline()
    Console.print(t)

    t.reset()
    Console.print(t)

    print("\n(reset clears all formatting)")


    # ============================================================
    # CHAINED FORMATTING
    # ============================================================

    print("\n=== CHAINED FORMATTING ===")

    t = Text.Text("Bold Italic Underlined")
    t.bold().italic().underline()
    Console.print(t)

    print("\n(chained formatting applied)")


    # ============================================================
    # ERROR / WARNING / OK / INFO (NON TITLE)
    # ============================================================

    print("\n=== STATUS FORMATTING (NON TITLE) ===")

    Console.print(Text.Text("Error message").error())
    Console.print(Text.Text("Warning message").warning())
    Console.print(Text.Text("Valid message").valid())
    Console.print(Text.Text("Info message").info())

    print("\n(colored foreground styles)")


    # ============================================================
    # ERROR / WARNING / OK / INFO (TITLE)
    # ============================================================

    print("\n=== STATUS FORMATTING (TITLE) ===")

    Console.print(Text.Text("ERROR").error(title=True))
    Console.print(Text.Text("WARNING").warning(title=True))
    Console.print(Text.Text("VALID").valid(title=True))
    Console.print(Text.Text("INFO").info(title=True))

    print("\n(background colored styles)")


    # ============================================================
    # FORMAT.APPLY ON TEXT
    # ============================================================

    print("\n=== FORMAT.APPLY ON TEXT ===")

    t = Text.Text("Applied bold")
    Format.apply(t, ANSI.Color(ANSI.Color.C_BOLD))
    Console.print(t)

    print("\n(apply works on Text)")


    # ============================================================
    # FORMAT.APPLY ON STRING
    # ============================================================

    print("\n=== FORMAT.APPLY ON STRING ===")

    raw = "Raw string formatted"
    formatted = Format.apply(raw, ANSI.Color(ANSI.Color.C_UNDERLINE))
    Console.print(formatted)

    print("\n(apply works on raw string)")


    # ============================================================
    # MULTIPLE APPLY CALLS
    # ============================================================

    print("\n=== MULTIPLE APPLY CALLS ===")

    t = Text.Text("Multi-applied")
    Format.apply(t, ANSI.Color(ANSI.Color.C_BOLD))
    Format.apply(t, ANSI.Color(ANSI.Color.C_ITALIC))
    Format.apply(t, ANSI.Color(ANSI.Color.C_UNDERLINE))
    Console.print(t)

    print("\n(multiple ANSI sequences applied)")


    # ============================================================
    # TREE – DICTIONARY
    # ============================================================

    print("\n=== TREE (DICT) ===")

    data = {
        "src": {
            "utils": [
                "helpers.py"
            ]
        },
        "file": [
            "README.md"
        ]
    }

    tree = Format.tree(data)
    Console.print(tree)

    print("\n(dictionary tree rendered)")


    # ============================================================
    # TREE – LIST
    # ============================================================

    print("\n=== TREE (LIST) ===")

    tree = Format.tree(["a", "b", "c"])
    Console.print(tree)

    print("\n(list tree rendered)")


    # ============================================================
    # TREE – STRING
    # ============================================================

    print("\n=== TREE (STRING) ===")

    tree = Format.tree("single_node")
    Console.print(tree)

    print("\n(string tree rendered)")


    # ============================================================
    # TREE WITH TITLE
    # ============================================================

    print("\n=== TREE WITH TITLE ===")

    tree = Format.tree(
        {
            "bin": ["app", "tool"],
            "lib": ["core", "utils"]
        },
        title="PROJECT"
    )
    Console.print(tree)

    print("\n(tree rendered with title)")


    # ============================================================
    # TREE WITH INDENT
    # ============================================================

    print("\n=== TREE WITH INDENT ===")

    tree = Format.tree(
        {"a": {"b": ["c"]}},
        indent=4
    )
    Console.print(tree)

    print("\n(tree rendered with custom indentation)")


    # ============================================================
    # MODULE TREE
    # ============================================================

    print("\n=== MODULE TREE ===")

    tree = Format.module_tree()
    Console.print(tree)

    print("\n(epitech_console module tree displayed)")


    # ============================================================
    # URL LINK
    # ============================================================

    print("\n=== URL LINK ===")

    link = Text.Text.url_link(
        "https://github.com/Jarjarbin06/epitech_console",
        "Epitech Console Repository"
    )
    Console.print(link)

    print("\n(clickable link in supported terminals)")


    # ============================================================
    # FILE LINK
    # ============================================================

    print("\n=== FILE LINK ===")

    file_link = Text.Text.file_link(
        path="epitech_console/Text/text.py",
        line=10
    )
    Console.print(file_link)

    print("\n(clickable file link in supported terminals)")


    # ============================================================
    # FILE LINK WITHOUT LINE
    # ============================================================

    print("\n=== FILE LINK (NO LINE) ===")

    file_link = Text.Text.file_link(
        path="epitech_console/Text/text.py"
    )
    Console.print(file_link)


    # ============================================================
    # MIXED FORMATTING + LINKS
    # ============================================================

    print("\n=== MIXED FORMATTING + LINKS ===")

    t = Text.Text("Important Link").bold().underline()
    link = Text.Text.url_link("https://epitech.eu", "Epitech")
    Console.print(t, "-", link)

    print("\n(mixed Text objects render correctly)")


    # ============================================================
    # EMPTY TEXT EDGE CASE
    # ============================================================

    print("\n=== EMPTY TEXT EDGE CASE ===")

    t = Text.Text("")
    Console.print(f"Empty text: '{t}' (len={len(t)})")

    print("\n(empty text handled correctly)")


    # ============================================================
    # RESET AFTER APPLY
    # ============================================================

    print("\n=== RESET AFTER APPLY ===")

    t = Text.Text("Reset test")
    t.bold().italic()
    Console.print(t)

    t.reset()
    Console.print(t)

    print("\n(reset clears applied ANSI sequences)")


    # ============================================================
    # FINAL MESSAGE
    # ============================================================

    print("\n=== TEXT MODULE DEMO COMPLETE ===")
    print("If all styles, trees, and links displayed correctly, the Text module works as expected.")


if __name__ == "__main__":
    text_demo()
