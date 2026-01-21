#!/usr/bin/env python3
"""
    FULL EPITECH_CONSOLE – SYSTEM MODULE DEMO
    ========================================

    This script is a REAL MANUAL TEST of the System module.

    It covers:
    - Console.print(...)
    - Console.print with sleep
    - Console.print start / end
    - Console.print custom file
    - len(Console)
    - Time.wait(...)
    - Time.pause(...)
    - StopWatch (start, stop, elapsed, update, reset)
    - Action
    - Actions (single, list, iteration, execution)
    - Config.exist
    - Config.create
    - Config.read
    - Edge cases and combinations

    Run in a REAL terminal.
"""


def system_demo(
    ) -> None:
    from epitech_console import System

    Console = System.Console
    Time = System.Time
    StopWatch = System.StopWatch
    Config = System.Config
    Action = System.Action
    Actions = System.Actions


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
    # TIME.WAIT
    # ============================================================

    print("\n=== TIME.WAIT ===")

    print("Waiting 1 second...")
    Time.wait(1)

    print("Waiting 0.3 second...")
    Time.wait(0.3)

    print("Done waiting")


    # ============================================================
    # TIME.PAUSE
    # ============================================================

    print("\n=== TIME.PAUSE ===")

    Time.pause("Press ENTER to continue after manual confirmation")


    # ============================================================
    # STOPWATCH – BASIC
    # ============================================================

    print("\n=== STOPWATCH BASIC ===")

    sw = StopWatch(start=True)
    Time.wait(1)
    sw.stop()

    elapsed = sw.elapsed()
    print(f"Elapsed time (≈1s): {elapsed:.3f} seconds")


    # ============================================================
    # STOPWATCH – MANUAL START / STOP
    # ============================================================

    print("\n=== STOPWATCH MANUAL START / STOP ===")

    sw = StopWatch()
    sw.start()
    Time.wait(0.5)
    sw.stop()

    print(f"Elapsed time (≈0.5s): {sw.elapsed():.3f} seconds")


    # ============================================================
    # STOPWATCH – UPDATE
    # ============================================================

    print("\n=== STOPWATCH UPDATE ===")

    sw = StopWatch(start=True)
    Time.wait(0.3)
    sw.update()
    Time.wait(0.3)
    sw.update()
    sw.stop()

    print(f"Elapsed time after updates (≈0.6s): {sw.elapsed():.3f} seconds")


    # ============================================================
    # STOPWATCH – RESET
    # ============================================================

    print("\n=== STOPWATCH RESET ===")

    sw.reset()
    print(f"Elapsed after reset (should be 0): {sw.elapsed():.3f} seconds")


    # ============================================================
    # ACTION – BASIC
    # ============================================================

    print("\n=== ACTION BASIC ===")

    def say_hello(name):
        Console.print(f"Hello {name}")

    action = Action("hello_action", say_hello, "Epitech")

    action.function(*action.args, **action.kwargs)

    print("\n(Action executed manually)")


    # ============================================================
    # ACTION – WITH KEYWORDS
    # ============================================================

    print("\n=== ACTION WITH KWARGS ===")

    def show_data(a, b, c=0):
        Console.print(f"a={a}, b={b}, c={c}")

    action = Action("data_action", show_data, 1, 2, c=3)
    action.function(*action.args, **action.kwargs)

    print("\n(Action with kwargs executed)")


    # ============================================================
    # ACTIONS – SINGLE ACTION
    # ============================================================

    print("\n=== ACTIONS SINGLE ===")

    actions = Actions(action)

    for act in actions.actions:
        act.function(*act.args, **act.kwargs)

    print("\n(Actions container with one Action works)")


    # ============================================================
    # ACTIONS – MULTIPLE ACTIONS
    # ============================================================

    print("\n=== ACTIONS MULTIPLE ===")

    a1 = Action("a1", Console.print, "First action")
    a2 = Action("a2", Console.print, "Second action")
    a3 = Action("a3", Console.print, "Third action")

    actions = Actions([a1, a2, a3])

    for act in actions.actions:
        act.function(*act.args, **act.kwargs)

    print("\n(All actions executed in order)")


    # ============================================================
    # CONFIG – EXIST (EXISTING)
    # ============================================================

    print("\n=== CONFIG EXIST (EXISTING) ===")

    config_path = "./demo/output"

    exists = Config.exist(config_path)
    print(f"Config exists before deletion: {exists}")


    # ============================================================
    # CONFIG – DELETE
    # ============================================================

    print("\n=== CONFIG DELETE ===")

    config = Config(config_path)
    config.delete(config_path)
    exists = Config.exist(config_path)
    print(f"Config do not exist after deletion: {not exists}")


    # ============================================================
    # CONFIG – EXIST WITH FILE NAME
    # ============================================================

    print("\n=== CONFIG EXIST WITH FILE NAME ===")

    exists = Config.exist(config_path, file_name="config.ini")
    print(f"Config do not exists with explicit file name: {not exists}")


    # ============================================================
    # CONFIG – CREATE
    # ============================================================

    print("\n=== CONFIG CREATE ===")

    config = Config(config_path, {
        "GENERAL": {
            "theme": "dark",
            "language": "en"
        },
        "USER": {
            "username": "guest",
            "email": "guest@example.com"
        }
    })

    exists = Config.exist(config_path)
    print(f"Config exists after creation: {exists}")


    # ============================================================
    # CONFIG – READ
    # ============================================================

    print("\n=== CONFIG READ ===")

    for section, values in config.config.items():
        print(f"[{section}]")
        for k, v in values.items():
            print(f"  {k} = {v}")

    print("\n(Config read successfully)")


    # ============================================================
    # FINAL MESSAGE
    # ============================================================

    print("\n=== SYSTEM MODULE DEMO COMPLETE ===")
    print("If all outputs behaved as described, the System module works as expected.")


if __name__ == "__main__":
    system_demo()
