# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : test_animation_frame.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.animation import Frame


def test_frame_basic():
    frame = Frame("Hello")

    assert str(frame) == "Hello"
    assert str(frame.content) == "Hello"
    assert frame.duration is None


def test_frame_default_content():
    frame = Frame()

    assert str(frame) == ""


@pytest.mark.parametrize(
    "content",
    [
        "Hello",
        123,
        1.5,
        None,
        True,
    ],
)
def test_frame_content_conversion(content):
    frame = Frame(content)

    assert str(frame) == str(content)


def test_frame_duration():
    frame = Frame(
        "Hello",
        duration=0.5,
    )

    assert frame.duration == 0.5


@pytest.mark.parametrize(
    "duration",
    [
        0,
        -1,
        -0.5,
    ],
)
def test_frame_invalid_duration(duration):
    with pytest.raises(
        ValueError,
        match="Duration must be greater than zero",
    ):
        Frame(
            "Hello",
            duration=duration,
        )


@pytest.mark.parametrize(
    "duration",
    [
        "1",
        None,
    ],
)
def test_frame_duration_types(duration):
    if duration is None:
        frame = Frame(
            "Hello",
            duration=duration,
        )

        assert frame.duration is None
        return

    with pytest.raises(TypeError):
        Frame(
            "Hello",
            duration=duration,
        )


def test_frame_render():
    frame = Frame("Hello")

    assert str(frame.render()) == "Hello"


def test_frame_formatting_disabled():
    frame = Frame("Hello")

    assert frame._can_format is False


def test_frame_is_text():
    frame = Frame("Hello")

    assert isinstance(frame, str)
