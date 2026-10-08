# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : test_animation_console.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.animation import (
    Animation,
    AnimationMode,
    Spinner,
)
from jarbin_toolkit_console import PresetSpinner


@pytest.mark.parametrize(
    "factory, preset",
    [
        (Spinner.line, PresetSpinner.LINE),
        (Spinner.dot, PresetSpinner.DOTS),
        (Spinner.braille, PresetSpinner.BRAILLE),
        (Spinner.block, PresetSpinner.BLOCK),
    ],
)
def test_spinner_preset(factory, preset):
    animation = factory()

    assert isinstance(animation, Animation)
    assert tuple(
        map(str, animation.frames)
    ) == tuple(
        map(str, preset.value)
    )


@pytest.mark.parametrize(
    "factory",
    [
        Spinner.line,
        Spinner.dot,
        Spinner.braille,
        Spinner.block,
    ],
)
def test_spinner_default_mode(factory):
    animation = factory()

    assert animation.mode == AnimationMode.LOOP


@pytest.mark.parametrize(
    "factory",
    [
        Spinner.line,
        Spinner.dot,
        Spinner.braille,
        Spinner.block,
    ],
)
def test_spinner_custom_duration(factory):
    animation = factory(
        duration=0.25,
    )

    assert animation.duration == 0.25


@pytest.mark.parametrize(
    "factory",
    [
        Spinner.line,
        Spinner.dot,
        Spinner.braille,
        Spinner.block,
    ],
)
def test_spinner_custom_mode(factory):
    animation = factory(
        mode=AnimationMode.ONCE,
    )

    assert animation.mode == AnimationMode.ONCE


def test_spinner_line():
    animation = Spinner.line()

    assert tuple(map(str, animation.frames)) == (
        "-",
        "\\",
        "|",
        "/",
    )


def test_spinner_dot():
    animation = Spinner.dot()

    assert tuple(map(str, animation.frames)) == tuple(
        map(str, PresetSpinner.DOTS.value)
    )


def test_spinner_braille():
    animation = Spinner.braille()

    assert tuple(map(str, animation.frames)) == tuple(
        map(str, PresetSpinner.BRAILLE.value)
    )


def test_spinner_block():
    animation = Spinner.block()

    assert tuple(map(str, animation.frames)) == tuple(
        map(str, PresetSpinner.BLOCK.value)
    )


def test_spinner_once():
    animation = Spinner.line(
        mode=AnimationMode.ONCE,
        duration=0.1,
    )

    animation.update(0.4)

    assert animation.finished is True
    assert animation.frame == len(animation) - 1
