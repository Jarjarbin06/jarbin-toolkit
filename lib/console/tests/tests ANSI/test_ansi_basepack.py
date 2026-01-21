import pytest


from jarbin_toolkit_console.ANSI import BasePack
from jarbin_toolkit_console.ANSI import ANSI
from jarbin_toolkit_console import (init, quit)


init()


def test_basepack_has_attributes(
    ) -> None:
    assert hasattr(BasePack, "P_ERROR")
    assert hasattr(BasePack, "P_WARNING")
    assert hasattr(BasePack, "P_VALID")
    assert hasattr(BasePack, "P_INFO")


def test_basepack_types(
    ) -> None:
    assert isinstance(BasePack.P_ERROR, tuple)
    assert isinstance(BasePack.P_WARNING, tuple)
    assert isinstance(BasePack.P_VALID, tuple)
    assert isinstance(BasePack.P_INFO, tuple)


def test_basepack_update(
    ) -> None:
    assert isinstance(BasePack.P_ERROR[0], ANSI)
    assert "\x1b[41m" == BasePack.P_ERROR[0].sequence


quit(delete_log=True)
