#!/usr/bin/env python3
"""
    FULL EPITECH_CONSOLE – ANSI MODULE DEMO
    =====================================

    This script is a REAL MANUAL TEST of the ANSI module.

    It covers:
    - ANSI class construction and concatenation
    - ANSI ESC constant
    - BasePack usage
    - Color foreground/background (basic + RGB)
    - Epitech color helpers (light + dark)
    - Cursor movements (all directions, save/restore)
    - Cursor visibility
    - Line clearing (all variants)
    - Combination of multiple ANSI sequences
    - Edge cases and chained usage

    Run in a REAL terminal (not an IDE output window).
"""


def ansi_demo(
    ) -> None:
    from epitech_console import ANSI, System

    Console = System.Console
    Time = System.Time


    # ============================================================
    # BASIC ANSI OBJECT
    # ============================================================

    print("\n=== BASIC ANSI OBJECT ===")

    a = ANSI.ANSI()
    b = ANSI.ANSI("TEST")

    print("Empty ANSI:", repr(a))
    print("ANSI with content:", repr(b))


    # ============================================================
    # ESC CONSTANT
    # ============================================================

    print("\n=== ANSI ESC CONSTANT ===")

    print("ESC character repr:", repr(ANSI.ANSI.ESC))


    # ============================================================
    # BASIC FOREGROUND COLORS
    # ============================================================

    print("\n=== BASIC FOREGROUND COLORS ===")

    print(ANSI.Color.color_fg(1) + "RED TEXT" + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.color_fg(2) + "GREEN TEXT" + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.color_fg(3) + "YELLOW TEXT" + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.color_fg(4) + "BLUE TEXT" + ANSI.Color(ANSI.Color.C_RESET))


    # ============================================================
    # BASIC BACKGROUND COLORS
    # ============================================================

    print("\n=== BASIC BACKGROUND COLORS ===")

    print(ANSI.Color.color_bg(1) + " RED BG " + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.color_bg(2) + " GREEN BG " + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.color_bg(3) + " YELLOW BG " + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.color_bg(4) + " BLUE BG " + ANSI.Color(ANSI.Color.C_RESET))


    # ============================================================
    # RGB COLORS (FOREGROUND)
    # ============================================================

    print("\n=== RGB FOREGROUND COLORS ===")

    print(ANSI.Color.rgb_fg(255, 0, 0) + "RGB RED" + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.rgb_fg(0, 255, 0) + "RGB GREEN" + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.rgb_fg(0, 0, 255) + "RGB BLUE" + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.rgb_fg(255, 255, 0) + "RGB YELLOW" + ANSI.Color(ANSI.Color.C_RESET))


    # ============================================================
    # RGB COLORS (BACKGROUND)
    # ============================================================

    print("\n=== RGB BACKGROUND COLORS ===")

    print(ANSI.Color.rgb_bg(80, 0, 0) + " DARK RED BG " + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.rgb_bg(0, 80, 0) + " DARK GREEN BG " + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.rgb_bg(0, 0, 80) + " DARK BLUE BG " + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.rgb_bg(80, 80, 0) + " DARK YELLOW BG " + ANSI.Color(ANSI.Color.C_RESET))


    # ============================================================
    # EPITECH COLOR PRESETS
    # ============================================================

    print("\n=== EPITECH COLOR PRESETS ===")

    print(ANSI.Color.epitech_fg() + "EPITECH LIGHT FG" + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.epitech_bg() + " EPITECH LIGHT BG " + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.epitech_dark_fg() + "EPITECH DARK FG" + ANSI.Color(ANSI.Color.C_RESET))
    print(ANSI.Color.epitech_dark_bg() + " EPITECH DARK BG " + ANSI.Color(ANSI.Color.C_RESET))


    # ============================================================
    # COMBINED FOREGROUND + BACKGROUND
    # ============================================================

    print("\n=== COMBINED FG + BG ===")

    combo = (
        ANSI.Color.rgb_fg(255, 255, 255) +
        ANSI.Color.rgb_bg(60, 60, 60)
    )

    print(combo + "WHITE ON DARK GRAY" + ANSI.Color(ANSI.Color.C_RESET))


    # ============================================================
    # CURSOR MOVEMENT (BASIC)
    # ============================================================

    print("\n=== CURSOR MOVEMENT ===")

    print("Line 1")
    print("Line 2")
    print("Line 3")

    Time.wait(1)
    print(ANSI.Cursor.up(2) + "← moved up 2 lines", end="")

    Time.wait(1)
    print(ANSI.Cursor.down(1) + "← moved down 1 line", end="")

    Time.wait(1)
    print(ANSI.Cursor.right(10) + "→ right 10", end="")

    Time.wait(1)
    print(ANSI.Cursor.left(5) + "← left 5", end="")


    # ============================================================
    # CURSOR POSITIONING
    # ============================================================

    print("\n=== CURSOR POSITIONING ===")

    Time.wait(1)
    print(ANSI.Cursor.move(5, 10) + "Moved to (5,10)", end="")

    Time.wait(1)
    print(ANSI.Cursor.move_column(1) + "Column 1", end="")


    # ============================================================
    # CURSOR SAVE / RESTORE
    # ============================================================

    print("\n=== CURSOR SAVE / RESTORE ===")

    print("Saving cursor position here.")
    print(ANSI.Cursor.set(), end="")

    Time.wait(1)
    print(ANSI.Cursor.move(10, 30) + "Temporary text")

    Time.wait(1)
    print(ANSI.Cursor.reset() + "Back to saved position")


    # ============================================================
    # CURSOR VISIBILITY
    # ============================================================

    print("\n=== CURSOR VISIBILITY ===")

    print("Cursor hidden for 2 seconds...")
    print(ANSI.Cursor.hide(), end="")
    Time.wait(2)

    print(ANSI.Cursor.show() + "Cursor visible again")


    # ============================================================
    # LINE CLEARING
    # ============================================================

    print("\n=== LINE CLEARING ===")

    print("This line will be cleared")
    Time.wait(1)
    print(ANSI.Line.clear_line() + "← cleared line")

    print("1234567890")
    Time.wait(1)
    print(ANSI.Cursor.left(5) + ANSI.Line.clear_end_line() + "← cleared end", end="")

    print("ABCDEFGHIJ")
    Time.wait(1)
    print(ANSI.Cursor.right(5) + ANSI.Line.clear_start_line() + "← cleared start", end="")


    # ============================================================
    # SCREEN CLEAR
    # ============================================================

    print("\n=== SCREEN CLEAR (WAIT 2s) ===")
    Time.wait(2)
    print(ANSI.Line.clear_screen())

    print("Screen cleared but cursor not moved")


    Time.wait(2)
    print(ANSI.Line.clear())
    print("Screen cleared and cursor reset")


    # ============================================================
    # CHAINED ANSI OBJECTS
    # ============================================================

    print("\n=== CHAINED ANSI OBJECTS ===")

    chain = (
        ANSI.Color.rgb_fg(255, 0, 255) +
        ANSI.Color.rgb_bg(0, 0, 0) +
        ANSI.Cursor.right(5)
    )

    print(chain + "CHAINED ANSI SEQUENCES" + ANSI.Color(ANSI.Color.C_RESET))


    # ============================================================
    # EDGE CASES
    # ============================================================

    print("\n=== EDGE CASES ===")

    print(ANSI.Cursor.up(0) + "Cursor up 0 (no-op)")
    print(ANSI.Cursor.left(0) + "Cursor left 0 (no-op)")
    print(ANSI.Color.rgb_fg(0, 0, 0) + "Black RGB" + ANSI.Color(ANSI.Color.C_RESET))


    # ============================================================
    # FINAL MESSAGE
    # ============================================================

    print("\n=== ANSI MODULE DEMO COMPLETE ===")
    print("If everything behaved correctly, the ANSI module works as expected.")


if __name__ == "__main__":
    ansi_demo()
