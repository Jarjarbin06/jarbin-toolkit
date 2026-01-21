import pytest


from jarbin_toolkit_console.Animation import Animation
from jarbin_toolkit_console.Animation import ProgressBar
from jarbin_toolkit_console.Animation import Spinner
from jarbin_toolkit_console import (init, quit)


init()


def test_progressbar_initialization(
    ) -> None:
    pb = ProgressBar(10)
    assert pb.length == 10
    assert pb.percent == 0
    assert pb.style.on == "#"
    assert pb.style.off == "-"
    assert isinstance(pb.animation, Animation) or pb.animation is None


def test_progressbar_update_basic(
    ) -> None:
    pb = ProgressBar(10)
    pb.update(50)
    assert pb.percent == 50


def test_progressbar_update_greater_than_hundred(
    ) -> None:
    pb = ProgressBar(10)
    pb.update(500)
    assert pb.percent == 100


def test_progressbar_update_call(
    ) -> None:
    pb = ProgressBar(10)
    for _ in range(10):
        pb()
    assert pb.percent == 10
    for _ in range(90):
        pb()
    assert pb.percent == 100
    for _ in range(10):
        pb()
    assert pb.percent == 100


def test_progressbar_update_spinner_flag(
    ) -> None:
    sp = Spinner.plus()
    pb = ProgressBar(10, spinner=sp)

    first = pb.spinner.render().replace("\x1b[0m", "")
    pb.update(20, update_spinner=True)
    second = pb.spinner.render().replace("\x1b[0m", "")

    assert first != second


def test_progressbar_update_no_spinner(
    ) -> None:
    sp = Spinner.plus()
    pb = ProgressBar(10, spinner=sp)

    first = pb.spinner.render().replace("\x1b[0m", "")
    pb.update(20, update_spinner=False)
    second = pb.spinner.render().replace("\x1b[0m", "")

    assert first == second


def test_progressbar_render_basic(
    ) -> None:
    pb = ProgressBar(10)
    pb.update(40)
    result = str(pb.render()).replace("\x1b[0m", "")
    assert isinstance(result, str)
    assert "|" in result and "#" in result and ">" in result and "-" in result


def test_progressbar_render_hide_spinner_at_end(
    ) -> None:
    sp = Spinner.stick()
    pb = ProgressBar(10, spinner=sp)

    pb.update(100)
    result = str(pb.render(hide_spinner_at_end=True))

    assert isinstance(result, str)
    assert sp.render().replace("\x1b[0m", "") not in result  # spinner hidden


def test_progressbar_render_spinner_before_bar(
    ) -> None:
    sp = Spinner.stick()
    pb = ProgressBar(10, spinner=sp, spinner_position="b")

    result = str(pb.render())

    assert isinstance(result, str)
    assert sp.render().replace("\x1b[0m", "") in result  # spinner hidden


def test_progressbar_render_spinner_after_bar(
    ) -> None:
    sp = Spinner.stick()
    pb = ProgressBar(10, spinner=sp, spinner_position="a")

    result = str(pb.render())

    assert isinstance(result, str)
    assert sp.render().replace("\x1b[0m", "") in result  # spinner hidden


def test_progressbar_render_delete_flag(
    ) -> None:
    pb = ProgressBar(10)
    result = str(pb.render(delete=True)).replace("\x1b[0m", "")
    assert isinstance(result, str)


def test_progressbar_percent_style_bar(
    ) -> None:
    pb = ProgressBar(10, percent_style="bar")
    pb.update(60)
    text = str(pb.render()).replace("\x1b[0m", "")
    # Expect filling using style.on
    assert "#" in text


def test_progressbar_percent_style_number(
    ) -> None:
    pb = ProgressBar(10, percent_style="num")
    pb.update(60)
    text = str(pb.render()).replace("\x1b[0m", "")
    # Expect percentage
    assert text.split()[-1] == "60%"


def test_progressbar_percent_style_mix(
    ) -> None:
    pb = ProgressBar(length=10, percent_style="mix")
    pb.update(60)
    text = str(pb.render()).replace("\x1b[0m", "")
    # Mix style includes both bar and percent digits
    assert "#" in text
    assert "%" in text


def test_progressbar_repr(
    ) -> None:
    pb = ProgressBar(10)
    print(repr(pb))
    assert repr(pb) == "ProgressBar(10, animation=[\'|>---------|\', ..., \'|##########|\'], style=Style('#', '-', '<', '>', '|', '|'), percent_style=\'bar\', spinner=None, spinner_position=\'a\')"


quit(delete_log=True)
