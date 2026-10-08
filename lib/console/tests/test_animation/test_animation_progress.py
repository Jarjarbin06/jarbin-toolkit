# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Animation
# File         : test_animation_progress.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

from jarbin_toolkit_console.animation import (
    Progress,
    ProgressRenderer,
)
from jarbin_toolkit_console.enums import PresetProgress


def test_progress_basic():
    progress = Progress()

    assert progress.minimum == 0
    assert progress.maximum == 100
    assert progress.value == 0
    assert progress.percentage == 0
    assert progress.finished is False


def test_progress_custom_range():
    progress = Progress(
        minimum=10,
        maximum=110,
        value=60,
    )

    assert progress.minimum == 10
    assert progress.maximum == 110
    assert progress.value == 60
    assert progress.percentage == 50


def test_progress_minimum():
    progress = Progress(
        minimum=10,
        maximum=20,
        value=10,
    )

    assert progress.percentage == 0


def test_progress_maximum():
    progress = Progress(
        minimum=10,
        maximum=20,
        value=20,
    )

    assert progress.percentage == 100
    assert progress.finished is True


@pytest.mark.parametrize(
    "minimum, maximum",
    [
        (0, 0),
        (10, 10),
        (10, 0),
    ],
)
def test_progress_invalid_range(minimum, maximum):
    with pytest.raises(
        ValueError,
        match="Maximum must be greater than minimum",
    ):
        Progress(
            minimum=minimum,
            maximum=maximum,
        )


@pytest.mark.parametrize(
    "value",
    [
        -1,
        101,
    ],
)
def test_progress_invalid_value(value):
    with pytest.raises(
        ValueError,
        match="Progress value out of range",
    ):
        Progress(value=value)


@pytest.mark.parametrize(
    "value",
    [
        "1",
        None,
        True,
        object(),
    ],
)
def test_progress_invalid_value_type(value):
    with pytest.raises(
        TypeError,
        match="Progress value must be a number",
    ):
        Progress(value=value)


def test_progress_set():
    progress = Progress()

    progress.set(50)

    assert progress.value == 50
    assert progress.percentage == 50


def test_progress_increment():
    progress = Progress(value=25)

    progress.increment(10)

    assert progress.value == 35


def test_progress_increment_default():
    progress = Progress(value=25)

    progress.increment()

    assert progress.value == 26


def test_progress_decrement():
    progress = Progress(value=25)

    progress.decrement(10)

    assert progress.value == 15


def test_progress_decrement_default():
    progress = Progress(value=25)

    progress.decrement()

    assert progress.value == 24


def test_progress_increment_to_maximum():
    progress = Progress(value=99)

    progress.increment()

    assert progress.value == 100
    assert progress.finished is True


def test_progress_increment_past_maximum():
    progress = Progress(value=99)

    with pytest.raises(
        ValueError,
        match="Progress value out of range",
    ):
        progress.increment(2)


def test_progress_decrement_past_minimum():
    progress = Progress(value=1)

    with pytest.raises(
        ValueError,
        match="Progress value out of range",
    ):
        progress.decrement(2)


def test_progress_reset():
    progress = Progress(
        minimum=10,
        maximum=100,
        value=50,
    )

    progress.reset()

    assert progress.value == 10
    assert progress.percentage == 0


def test_progress_renderer_basic():
    progress = Progress(value=50)

    renderer = ProgressRenderer(
        width=10,
    )

    result = renderer.render(progress)

    assert str(result) == "[█████░░░░░] 50%"


@pytest.mark.parametrize(
    "preset",
    list(PresetProgress),
)
def test_progress_renderer_presets(preset):
    progress = Progress(value=50)

    renderer = ProgressRenderer(
        width=10,
        preset=preset,
    )

    result = renderer.render(progress)

    filled, empty = preset.value

    assert str(result) == (
        f"[{filled * 5}"
        f"{empty * 5}] 50%"
    )


def test_progress_renderer_custom_characters():
    progress = Progress(value=50)

    renderer = ProgressRenderer(
        width=10,
        filled="#",
        empty="-",
    )

    assert str(
        renderer.render(progress)
    ) == "[#####-----] 50%"


def test_progress_renderer_no_percentage():
    progress = Progress(value=50)

    renderer = ProgressRenderer(
        width=10,
        show_percentage=False,
    )

    assert str(
        renderer.render(progress)
    ) == "[█████░░░░░]"


def test_progress_renderer_width():
    progress = Progress(value=50)

    renderer = ProgressRenderer(
        width=20,
    )

    assert renderer.width == 20
    assert str(
        renderer.render(progress)
    ) == "[██████████░░░░░░░░░░] 50%"


def test_progress_renderer_set_width():
    progress = Progress(value=50)

    renderer = ProgressRenderer(
        width=10,
    )

    renderer.set_width(20)

    assert renderer.width == 20
    assert str(
        renderer.render(progress)
    ) == "[██████████░░░░░░░░░░] 50%"


@pytest.mark.parametrize(
    "width",
    [
        0,
        -1,
        -10,
    ],
)
def test_progress_renderer_invalid_width(width):
    with pytest.raises(
        ValueError,
        match="Width must be greater than zero",
    ):
        ProgressRenderer(width=width)


@pytest.mark.parametrize(
    "width",
    [
        0,
        -1,
        -10,
    ],
)
def test_progress_renderer_set_invalid_width(width):
    renderer = ProgressRenderer()

    with pytest.raises(
        ValueError,
        match="Width must be greater than zero",
    ):
        renderer.set_width(width)


@pytest.mark.parametrize(
    "filled, empty",
    [
        ("#", None),
        (None, "-"),
    ],
)
def test_progress_renderer_missing_character(
        filled,
        empty,
    ):

    with pytest.raises(
        ValueError,
        match="Both filled and empty must be provided",
    ):
        ProgressRenderer(
            filled=filled,
            empty=empty,
        )


@pytest.mark.parametrize(
    "preset",
    [
        None,
        "BLOCK",
        1,
    ],
)
def test_progress_renderer_invalid_preset(preset):
    with pytest.raises(
        TypeError,
        match="Preset must be a PresetProgress",
    ):
        ProgressRenderer(
            preset=preset,
        )


def test_progress_renderer_invalid_progress():
    renderer = ProgressRenderer()

    with pytest.raises(
        TypeError,
        match="Progress must be a Progress",
    ):
        renderer.render(50)


@pytest.mark.parametrize(
    "value, width, expected",
    [
        (0, 10, 0),
        (25, 10, 2),
        (50, 10, 5),
        (75, 10, 8),
        (100, 10, 10),
    ],
)
def test_progress_renderer_rounding(
        value,
        width,
        expected,
    ):

    progress = Progress(value=value)

    renderer = ProgressRenderer(
        width=width,
        show_percentage=False,
    )

    result = str(renderer.render(progress))

    assert result.count("█") == expected
