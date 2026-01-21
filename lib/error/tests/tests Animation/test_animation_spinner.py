import pytest


from jarbin_toolkit_console.Animation import Animation
from jarbin_toolkit_console.Animation import Spinner
from jarbin_toolkit_console import (init, quit)


init()


def test_spinner_stick(
    ) -> None:
    sp = Spinner.stick()
    assert isinstance(sp, Animation)
    assert len(sp.animation) > 0


def test_spinner_plus(
    ) -> None:
    sp = Spinner.plus()
    assert isinstance(sp, Animation)
    assert len(sp.animation) > 0


def test_spinner_cross(
    ) -> None:
    sp = Spinner.cross()
    assert isinstance(sp, Animation)
    assert len(sp.animation) > 0


def test_spinner_updates_correctly(
    ) -> None:
    sp = Spinner.stick()
    first = sp.render()
    sp.update()
    second = sp.render()
    assert first != second


quit(delete_log=True)
