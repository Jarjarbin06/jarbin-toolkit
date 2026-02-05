import pytest


import jarbin_toolkit


def test_jarbin_toolkit_attributes(
    ) -> None:
    assert hasattr(jarbin_toolkit, "Action")
    assert hasattr(jarbin_toolkit, "Config")
    assert hasattr(jarbin_toolkit, "Console")
    assert hasattr(jarbin_toolkit, "Error")
    assert hasattr(jarbin_toolkit, "Log")
    assert hasattr(jarbin_toolkit, "Time")
