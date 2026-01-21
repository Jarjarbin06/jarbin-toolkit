#!/usr/bin/env python3
"""
    FULL Jarbin-ToolKit:Console – Console MODULE DEMO
    ========================================

    This script is a REAL MANUAL TEST of the Console module.

    It covers:
    - Console.print(...)
    - Console.print with sleep
    - Console.print start / end
    - Console.print custom file
    - len(Console)

    Run in a REAL terminal.
"""


def console_demo(
    ) -> None:
    from jarbin_toolkit_console import Console


    # ============================================================
    # CONSOLE PRINT – BASIC
    # ============================================================

    print("\n=== CONSOLE.PRINT BASIC ===")

    Console.print("Hello from Console.print()")
    Console.print(123)
    Console.print(12.34)
    Console.print(["a", "b", "c"])
    Console.print({"key": "value"})

    print("\n(All basic Python objects printed correctly)")


    # ============================================================
    # CONSOLE PRINT – START / END
    # ============================================================

    print("\n=== CONSOLE.PRINT START / END ===")

    Console.print("World", start="Hello ", end=" !!!\n")
    Console.print("Same line...", end="")
    Console.print(" done.")

    print("\n(start and end parameters applied)")


    # ============================================================
    # CONSOLE PRINT – SLEEP
    # ============================================================

    print("\n=== CONSOLE.PRINT WITH SLEEP ===")

    Console.print("This message waits 1 second", sleep=1)
    Console.print("This message waits 0.5 second", sleep=0.5)
    Console.print("Immediate message")

    print("\n(sleep delays respected)")


    # ============================================================
    # CONSOLE PRINT – CUSTOM FILE
    # ============================================================

    print("\n=== CONSOLE.PRINT CUSTOM FILE ===")

    with open("demo/output/console_output_test.txt", "w") as f:
        Console.print("This goes into a file", file=f)
        Console.print("Another line in file", file=f)

    print("Check 'console_output_test.txt' for output")


    # ============================================================
    # CONSOLE LEN COMPATIBILITY
    # ============================================================

    print("\n=== CONSOLE LEN COMPATIBILITY ===")

    Console.print("12345")
    Console.print("abcdef")

    try:
        size = len(Console)
        print(f"len(Console) returned: {size}")
    except Exception as e:
        print("len(Console) raised an error:", e)

    print("\n(len(Console) tested)")


    # ============================================================
    # FINAL MESSAGE
    # ============================================================

    print("\n=== SYSTEM MODULE DEMO COMPLETE ===")
    print("If all outputs behaved as described, the System module works as expected.")


if __name__ == "__main__":
    console_demo()
