import pytest


from jarbin_toolkit_console.Animation import BasePack, Style
from jarbin_toolkit_console import (init, quit)


init()


def test_basepack_has_attributes(
    ) -> None:
    assert hasattr(BasePack, "P_SLIDE_R")
    assert hasattr(BasePack, "P_SLIDE_L")
    assert hasattr(BasePack, "P_SLIDER_R")
    assert hasattr(BasePack, "P_SLIDER_L")
    assert hasattr(BasePack, "P_FILL_R")
    assert hasattr(BasePack, "P_FILL_L")
    assert hasattr(BasePack, "P_EMPTY_R")
    assert hasattr(BasePack, "P_EMPTY_L")
    assert hasattr(BasePack, "P_FULL")
    assert hasattr(BasePack, "P_EMPTY")


def test_basepack_types(
    ) -> None:
    assert isinstance(BasePack.P_SLIDE_R, list)
    assert isinstance(BasePack.P_SLIDE_L, list)
    assert isinstance(BasePack.P_SLIDER_R, list)
    assert isinstance(BasePack.P_SLIDER_L, list)
    assert isinstance(BasePack.P_FILL_R, list)
    assert isinstance(BasePack.P_FILL_L, list)
    assert isinstance(BasePack.P_EMPTY_R, list)
    assert isinstance(BasePack.P_EMPTY_L, list)
    assert isinstance(BasePack.P_FULL, list)
    assert isinstance(BasePack.P_EMPTY, list)


def test_basepack_update_with_style(
    ) -> None:
    style = Style(on="X", off="_", arrow_left="{", arrow_right="}", border_left="[", border_right="]")
    BasePack.update(style)

    assert any("X" in frame or "_" in frame for frame in BasePack.P_SLIDE_R)
    assert any("X" in frame or "_" in frame for frame in BasePack.P_SLIDE_L)
    assert any("X" in frame or "_" in frame for frame in BasePack.P_SLIDER_R)
    assert any("X" in frame or "_" in frame for frame in BasePack.P_SLIDER_L)
    assert any("X" in frame or "_" in frame for frame in BasePack.P_FILL_R)
    assert any("X" in frame or "_" in frame for frame in BasePack.P_FILL_L)
    assert any("X" in frame or "_" in frame for frame in BasePack.P_EMPTY_R)
    assert any("X" in frame or "_" in frame for frame in BasePack.P_EMPTY_L)
    assert any("X" in frame or "_" in frame for frame in BasePack.P_FULL)
    assert any("X" in frame or "_" in frame for frame in BasePack.P_EMPTY)


def test_basepack_update_without_style(
    ) -> None:
    BasePack.update()

    assert any("#" in frame or "-" in frame for frame in BasePack.P_SLIDE_R)
    assert any("#" in frame or "-" in frame for frame in BasePack.P_SLIDE_L)
    assert any("#" in frame or "-" in frame for frame in BasePack.P_SLIDER_R)
    assert any("#" in frame or "-" in frame for frame in BasePack.P_SLIDER_L)
    assert any("#" in frame or "-" in frame for frame in BasePack.P_FILL_R)
    assert any("#" in frame or "-" in frame for frame in BasePack.P_FILL_L)
    assert any("#" in frame or "-" in frame for frame in BasePack.P_EMPTY_R)
    assert any("#" in frame or "-" in frame for frame in BasePack.P_EMPTY_L)
    assert any("#" in frame or "-" in frame for frame in BasePack.P_FULL)
    assert any("#" in frame or "-" in frame for frame in BasePack.P_EMPTY)


quit(delete_log=True)
