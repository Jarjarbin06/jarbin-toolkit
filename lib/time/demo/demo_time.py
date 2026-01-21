#!/usr/bin/env python3
"""
    FULL Jarbin-ToolKit:Time – TIME MODULE DEMO
    ========================================

    This script is a REAL MANUAL TEST of the Time module.

    It covers:

    - Time.wait(...)
    - Time.pause(...)
    - StopWatch (start, stop, elapsed, update, reset)

    Run in a REAL terminal.
"""


def time_demo(
    ) -> None:
    from jarbin_toolkit_time import (Time, StopWatch)


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
    # FINAL MESSAGE
    # ============================================================

    print("\n=== TIME MODULE DEMO COMPLETE ===")
    print("If all outputs behaved as described, the System module works as expected.")


if __name__ == "__main__":
    time_demo()
