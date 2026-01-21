#!/usr/bin/env python3
"""
    FULL Jarbin-ToolKit:Config – Config MODULE DEMO
    ========================================

    This script is a REAL MANUAL TEST of the Config module.

    It covers:
    - Action
    - Actions (single, list, iteration, execution)

    Run in a REAL terminal.
"""


def config_demo(
    ) -> None:
    from jarbin_toolkit_config import Config


    # ============================================================
    # ACTION – BASIC
    # ============================================================

    print("\n=== ACTION BASIC ===")

    def say_hello(name):
        print(f"Hello {name}")

    action = Action("hello_action", say_hello, "Epitech")

    action.function(*action.args, **action.kwargs)

    print("\n(Action executed manually)")


    # ============================================================
    # ACTION – WITH KEYWORDS
    # ============================================================

    print("\n=== ACTION WITH KWARGS ===")

    def show_data(a, b, c=0):
        print(f"a={a}, b={b}, c={c}")

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

    a1 = Action("a1", print, "First action")
    a2 = Action("a2", print, "Second action")
    a3 = Action("a3", print, "Third action")

    actions = Actions([a1, a2, a3])

    for act in actions.actions:
        act.function(*act.args, **act.kwargs)

    print("\n(All actions executed in order)")


    # ============================================================
    # FINAL MESSAGE
    # ============================================================

    print("\n=== CONFIG MODULE DEMO COMPLETE ===")
    print("If all outputs behaved as described, the System module works as expected.")


if __name__ == "__main__":
    config_demo()
