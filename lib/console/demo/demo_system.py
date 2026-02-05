#!/usr/bin/env python3
"""
    FULL Jarbin-ToolKit:Console – SYSTEM MODULE DEMO
    ========================================

    This script is a REAL MANUAL TEST of the System module.

    It covers:
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
    from jarbin_toolkit_console import System, Console

    Time = System.Time
    StopWatch = System.StopWatch
    Config = System.Config
    Action = System.Action
    Actions = System.Actions


    # ============================================================
    # TIME.WAIT
    # ============================================================

    Console.print("\n=== TIME.WAIT ===")

    Console.print("Waiting 1 second...")
    Time.wait(1)

    Console.print("Waiting 0.3 second...")
    Time.wait(0.3)

    Console.print("Done waiting")


    # ============================================================
    # TIME.PAUSE
    # ============================================================

    Console.print("\n=== TIME.PAUSE ===")

    Time.pause("Press ENTER to continue after manual confirmation")


    # ============================================================
    # STOPWATCH – BASIC
    # ============================================================

    Console.print("\n=== STOPWATCH BASIC ===")

    sw = StopWatch(start=True)
    Time.wait(1)
    sw.stop()

    elapsed = sw.elapsed()
    Console.print(f"Elapsed time (≈1s): {elapsed:.3f} seconds")


    # ============================================================
    # STOPWATCH – MANUAL START / STOP
    # ============================================================

    Console.print("\n=== STOPWATCH MANUAL START / STOP ===")

    sw = StopWatch()
    sw.start()
    Time.wait(0.5)
    sw.stop()

    Console.print(f"Elapsed time (≈0.5s): {sw.elapsed():.3f} seconds")


    # ============================================================
    # STOPWATCH – UPDATE
    # ============================================================

    Console.print("\n=== STOPWATCH UPDATE ===")

    sw = StopWatch(start=True)
    Time.wait(0.3)
    sw.update()
    Time.wait(0.3)
    sw.update()
    sw.stop()

    Console.print(f"Elapsed time after updates (≈0.6s): {sw.elapsed():.3f} seconds")


    # ============================================================
    # STOPWATCH – RESET
    # ============================================================

    Console.print("\n=== STOPWATCH RESET ===")

    sw.reset()
    Console.print(f"Elapsed after reset (should be 0): {sw.elapsed():.3f} seconds")


    # ============================================================
    # ACTION – BASIC
    # ============================================================

    Console.print("\n=== ACTION BASIC ===")

    def say_hello(name):
        Console.print(f"Hello {name}")

    action = Action("hello_action", say_hello, "Jarbin-ToolKit:Console")

    action.function(*action.args, **action.kwargs)

    Console.print("\n(Action executed manually)")


    # ============================================================
    # ACTION – WITH KEYWORDS
    # ============================================================

    Console.print("\n=== ACTION WITH KWARGS ===")

    def show_data(a, b, c=0):
        Console.print(f"a={a}, b={b}, c={c}")

    action = Action("data_action", show_data, 1, 2, c=3)
    action.function(*action.args, **action.kwargs)

    Console.print("\n(Action with kwargs executed)")


    # ============================================================
    # ACTIONS – SINGLE ACTION
    # ============================================================

    Console.print("\n=== ACTIONS SINGLE ===")

    actions = Actions(action)

    for act in actions.actions:
        act.function(*act.args, **act.kwargs)

    Console.print("\n(Actions container with one Action works)")


    # ============================================================
    # ACTIONS – MULTIPLE ACTIONS
    # ============================================================

    Console.print("\n=== ACTIONS MULTIPLE ===")

    a1 = Action("a1", Console.print, "First action")
    a2 = Action("a2", Console.print, "Second action")
    a3 = Action("a3", Console.print, "Third action")

    actions = Actions([a1, a2, a3])

    for act in actions.actions:
        act.function(*act.args, **act.kwargs)

    Console.print("\n(All actions executed in order)")


    # ============================================================
    # CONFIG – EXIST (EXISTING)
    # ============================================================

    Console.print("\n=== CONFIG EXIST (EXISTING) ===")

    config_path = "./demo/output"

    exists = Config.exist(config_path)
    Console.print(f"Config exists before deletion: {exists}")


    # ============================================================
    # CONFIG – DELETE
    # ============================================================

    Console.print("\n=== CONFIG DELETE ===")

    config = Config(config_path)
    config.delete(config_path)
    exists = Config.exist(config_path)
    Console.print(f"Config do not exist after deletion: {not exists}")


    # ============================================================
    # CONFIG – EXIST WITH FILE NAME
    # ============================================================

    Console.print("\n=== CONFIG EXIST WITH FILE NAME ===")

    exists = Config.exist(config_path, file_name="config.ini")
    Console.print(f"Config do not exists with explicit file name: {not exists}")


    # ============================================================
    # CONFIG – CREATE
    # ============================================================

    Console.print("\n=== CONFIG CREATE ===")

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
    Console.print(f"Config exists after creation: {exists}")


    # ============================================================
    # CONFIG – READ
    # ============================================================

    Console.print("\n=== CONFIG READ ===")

    for section, values in config.config.items():
        Console.print(f"[{section}]")
        for k, v in values.items():
            Console.print(f"  {k} = {v}")

    Console.print("\n(Config read successfully)")


    # ============================================================
    # FINAL MESSAGE
    # ============================================================

    Console.print("\n=== SYSTEM MODULE DEMO COMPLETE ===")
    Console.print("If all outputs behaved as described, the System module works as expected.")


if __name__ == "__main__":
    system_demo()
