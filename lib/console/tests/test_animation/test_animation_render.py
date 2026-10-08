# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : test_animation_render.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.animation import (
    AnimationRenderer,
    Frame,
)
from jarbin_toolkit_console import ConsoleJError


def test_renderer_basic():
    rendered = []

    renderer = AnimationRenderer(
        lambda frame: rendered.append(str(frame)),
    )

    renderer.render(Frame("Hello"))

    assert rendered == ["Hello"]


def test_renderer_converts_frame():
    rendered = []

    renderer = AnimationRenderer(
        lambda frame: rendered.append(frame),
    )

    renderer.render("Hello")

    assert isinstance(rendered[0], Frame)
    assert str(rendered[0]) == "Hello"


def test_renderer_clear():
    calls = []

    renderer = AnimationRenderer(
        lambda frame: None,
        clear=lambda: calls.append("clear"),
    )

    renderer.clear()

    assert calls == ["clear"]


def test_renderer_start():
    calls = []

    renderer = AnimationRenderer(
        lambda frame: None,
        start=lambda: calls.append("start"),
    )

    renderer.start()

    assert calls == ["start"]


def test_renderer_stop():
    calls = []

    renderer = AnimationRenderer(
        lambda frame: None,
        stop=lambda: calls.append("stop"),
    )

    renderer.stop()

    assert calls == ["stop"]


def test_renderer_optional_callbacks():
    renderer = AnimationRenderer(
        lambda frame: None,
    )

    renderer.start()
    renderer.clear()
    renderer.stop()


def test_renderer_context_manager():
    calls = []

    renderer = AnimationRenderer(
        lambda frame: calls.append(
            ("render", str(frame))
        ),
        start=lambda: calls.append("start"),
        stop=lambda: calls.append("stop"),
    )

    with renderer as active:
        assert active is renderer
        renderer.render("Hello")

    assert calls == [
        "start",
        ("render", "Hello"),
        "stop",
    ]


def test_renderer_context_manager_stops_on_exception():
    calls = []

    renderer = AnimationRenderer(
        lambda frame: None,
        stop=lambda: calls.append("stop"),
    )

    with pytest.raises(ConsoleJError):
        with renderer:
            raise ConsoleJError("failure")

    assert calls == ["stop"]


@pytest.mark.parametrize(
    "argument, message",
    [
        (None, "Render must be callable"),
        ("render", "Render must be callable"),
        (1, "Render must be callable"),
    ],
)
def test_renderer_invalid_render(argument, message):
    with pytest.raises(
        ConsoleJError,
        match=message,
    ):
        AnimationRenderer(argument)


def test_renderer_invalid_clear():
    with pytest.raises(
        ConsoleJError,
        match="Clear must be callable",
    ):
        AnimationRenderer(
            lambda frame: None,
            clear="clear",
        )


def test_renderer_invalid_start():
    with pytest.raises(
        ConsoleJError,
        match="Start must be callable",
    ):
        AnimationRenderer(
            lambda frame: None,
            start="start",
        )


def test_renderer_invalid_stop():
    with pytest.raises(
        ConsoleJError,
        match="Stop must be callable",
    ):
        AnimationRenderer(
            lambda frame: None,
            stop="stop",
        )
