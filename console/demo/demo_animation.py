#!/usr/bin/env python3
"""
    FULL EPITECH_CONSOLE – ANIMATION MODULE DEMO
    ===========================================

    This script is a REAL MANUAL TEST of the Animation module.

    It covers:
    - Animation(Animation)
    - Animation.update(auto_reset)
    - Animation.render(delete)
    - BasePack animations
    - BasePack.update(style)
    - Custom animations (list[str])
    - ProgressBar
    - ProgressBar.update(...)
    - ProgressBar.render(...)
    - Spinner (stick / plus / cross)
    - Spinner integration with ProgressBar
    - Style customization
    - All valid combinations and edge cases

    Run in a REAL terminal.
"""


def animation_demo(
    ) -> None:
    from epitech_console import Animation, System
    from epitech_console.Animation import (
        ProgressBar,
        Spinner,
        Style
    )


    Console = System.Console


    # ============================================================
    # BASIC ANIMATION (STRING)
    # ============================================================

    print("\n=== BASIC STRING ANIMATION ===")

    anim = Animation.Animation("Loading")
    for i in range(5):
        Console.print(anim.render(delete=True), sleep=0.1)
        anim.update()

    print("\n(no visual change expected, but render/update are exercised)")


    # ============================================================
    # CUSTOM ANIMATION (LIST OF FRAMES)
    # ============================================================

    print("\n=== CUSTOM FRAME ANIMATION ===")

    frames = ["Frame A", "Frame B", "Frame C"]
    anim = Animation.Animation(frames)

    for i in range(9):
        Console.print(anim.render(delete=True), sleep=0.1)
        anim.update()

    print("\n(should loop through A → B → C)")


    # ============================================================
    # AUTO RESET BEHAVIOR
    # ============================================================

    print("\n=== AUTO RESET TRUE ===")

    anim = Animation.Animation(["1", "2", "3"])

    for i in range(6):
        Console.print(anim.render(delete=True), sleep=0.1)
        anim.update(auto_reset=True)

    print("\n(animation loops automatically)")


    print("\n=== AUTO RESET FALSE ===")

    anim = Animation.Animation(["X", "Y", "Z"])

    for i in range(6):
        Console.print(anim.render(delete=True), sleep=0.1)
        anim.update(auto_reset=False)

    print("\n(animation should stop at last frame)")


    # ============================================================
    # BASEPACK ANIMATIONS
    # ============================================================

    print("\n=== BASEPACK: P_SLIDE_L ===")

    anim = Animation.Animation(Animation.BasePack.P_SLIDE_L)
    for _ in range(12):
        Console.print(anim.render(delete=True), sleep=0.1)
        anim.update()

    print("\n(should animate a character sliding to the left)")


    print("\n=== BASEPACK: P_SLIDER_L ===")

    anim = Animation.Animation(Animation.BasePack.P_SLIDER_L)
    for _ in range(12):
        Console.print(anim.render(delete=True), sleep=0.1)
        anim.update()

    print("\n(should animate a chain of character sliding to the left)")


    print("\n=== BASEPACK: P_FILL_L ===")

    anim = Animation.Animation(Animation.BasePack.P_FILL_L)
    for _ in range(12):
        Console.print(anim.render(delete=True), sleep=0.1)
        anim.update()

    print("\n(should animate characters filling to the left)")


    # ============================================================
    # BASEPACK STYLE UPDATE
    # ============================================================

    print("\n=== BASEPACK STYLE UPDATE ===")

    custom_style = Style(
        on="█",
        off="░",
        arrow_left="░",
        arrow_right="░",
        border_left="",
        border_right=""
    )

    Animation.BasePack.update(custom_style)

    anim = Animation.Animation(Animation.BasePack.P_FILL_R)
    for _ in range(12):
        Console.print(anim.render(delete=True), sleep=0.1)
        anim.update()

    print("\n(style change applied globally to BasePack)")


    # ============================================================
    # SPINNER TESTS
    # ============================================================

    print("\n=== SPINNER: STICK ===")

    spinner = Spinner.stick()
    for _ in range(8):
        Console.print(spinner.render(delete=True), sleep=0.1)
        spinner.update()

    print("\n(should animate a spinning character with 8 steps)")


    print("\n=== SPINNER: PLUS ===")

    spinner = Spinner.plus()
    for _ in range(8):
        Console.print(spinner.render(delete=True), sleep=0.1)
        spinner.update()

    print("\n(should animate a spinning character with 4 steps)")


    print("\n=== SPINNER: CROSS ===")

    spinner = Spinner.cross()
    for _ in range(8):
        Console.print(spinner.render(delete=True), sleep=0.1)
        spinner.update()

    print("\n(should animate a spinning character with 4 steps)")


    # ============================================================
    # PROGRESS BAR – BASIC
    # ============================================================

    print("\n=== PROGRESS BAR BASIC ===")

    bar = ProgressBar(length=20)

    for i in range(0, 101, 5):
        bar.update(percent=i)
        Console.print(bar.render(delete=True), sleep=0.1)

    print("\n(progress should reach 100%)")


    # ============================================================
    # PROGRESS BAR – PERCENT STYLES
    # ============================================================

    print("\n=== PROGRESS BAR: PERCENT STYLE = 'bar' ===")

    bar = ProgressBar(length=20, percent_style="bar")
    for i in range(0, 101, 5):
        bar.update(i)
        Console.print(bar.render(delete=True), sleep=0.1)

    print("\n(progress should be shown as a bar)")


    print("\n=== PROGRESS BAR: PERCENT STYLE = 'num' ===")

    bar = ProgressBar(length=20, percent_style="num")
    for i in range(0, 101, 5):
        bar.update(i)
        Console.print(bar.render(delete=True), sleep=0.1)

    print("\n(progress should be shown as a percentage)")


    print("\n=== PROGRESS BAR: PERCENT STYLE = 'mix' ===")

    bar = ProgressBar(length=20, percent_style="mix")
    for i in range(0, 101, 5):
        bar.update(i)
        Console.print(bar.render(delete=True), sleep=0.1)

    print("\n(progress should be shown as a bar and percentage)")


    # ============================================================
    # PROGRESS BAR WITH SPINNER
    # ============================================================

    print("\n=== PROGRESS BAR WITH SPINNER ===")

    spinner = Spinner.stick()
    bar = ProgressBar(
        length=30,
        spinner=spinner,
        percent_style="mix"
    )

    for i in range(0, 101, 5):
        bar.update(percent=i, update_spinner=True)
        Console.print(bar.render(delete=True), sleep=0.1)

    print("\n(progress should be shown while a character is spinning)")


    # ============================================================
    # PROGRESS BAR – COLORING
    # ============================================================

    print("\n=== PROGRESS BAR: COLOR RED = '\033[31m' ===")

    bar = ProgressBar(length=20, percent_style="mix")
    for i in range(0, 101, 5):
        bar.update(i)
        Console.print(bar.render(color=("\033[32m", "\033[31m", "\033[33m"), delete=True), sleep=0.1)

    print("\n(bar should be shown in green and percentage in yellow)")


    print("\n=== PROGRESS BAR: COLOR FLASHING = '\033[5m' ===")

    bar = ProgressBar(length=20, percent_style="mix")
    for i in range(0, 101, 5):
        bar.update(i)
        Console.print(bar.render(color=("\033[5m", "\033[5m", "\033[0m"), delete=True, hide_spinner_at_end=False), sleep=0.1)

    print("\n(bar should be flashing but not percentage)")


    # ============================================================
    # SPINNER POSITION TEST
    # ============================================================

    print("\n=== SPINNER POSITION: BEFORE BAR ===")

    bar = ProgressBar(
        length=25,
        spinner=Spinner.plus(),
        spinner_position="b"
    )

    for i in range(0, 101, 5):
        bar.update(i)
        Console.print(bar.render(delete=True), sleep=0.1)

    print("\n(progress should be shown while a character is spinning before the bar)")


    print("\n=== SPINNER POSITION: AFTER BAR ===")

    bar = ProgressBar(
        length=25,
        spinner=Spinner.plus(),
        spinner_position="a"
    )

    for i in range(0, 101, 5):
        bar.update(i)
        Console.print(bar.render(delete=True), sleep=0.1)
    print("\n(progress should be shown while a character is spinning after the bar)")


    # ============================================================
    # CUSTOM STYLE PROGRESS BAR
    # ============================================================

    print("\n=== CUSTOM STYLE PROGRESS BAR ===")

    style = Style(
        on="■",
        off="·",
        arrow_left="«",
        arrow_right="»",
        border_left="|",
        border_right="|"
    )

    bar = ProgressBar(
        length=30,
        style=style,
        spinner=Spinner.cross(),
        percent_style="mix"
    )

    for i in range(0, 101, 5):
        bar.update(i)
        Console.print(bar.render(delete=True), sleep=0.1)

    print("\n(progress should be shown with a custom style)")


    # ============================================================
    # HIDE SPINNER AT END
    # ============================================================

    print("\n=== HIDE SPINNER AT END ===")

    bar = ProgressBar(
        length=20,
        spinner=Spinner.stick()
    )

    for i in range(0, 101, 5):
        bar.update(i)
        Console.print(
            bar.render(
                hide_spinner_at_end=True,
                delete=True
            ),
            sleep=0.1
        )

    print("\n(spinner should hide at the end)")


    # ============================================================
    # FINAL MESSAGE
    # ============================================================

    print("\n=== ANIMATION MODULE DEMO COMPLETE ===")
    print("If all animations displayed correctly, the Animation module works as expected.")


if __name__ == "__main__":
    animation_demo()
