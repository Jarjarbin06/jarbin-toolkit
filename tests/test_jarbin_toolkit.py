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
    assert hasattr(jarbin_toolkit, "get_info")
    assert hasattr(jarbin_toolkit, "benchmark")
    assert hasattr(jarbin_toolkit, "fail")
    assert hasattr(jarbin_toolkit, "text")
    assert hasattr(jarbin_toolkit, "IS_TTY")
    assert hasattr(jarbin_toolkit, "OS")
    assert hasattr(jarbin_toolkit, "TERM")
    assert hasattr(jarbin_toolkit, "sleep")
    assert hasattr(jarbin_toolkit, "pause")
    assert hasattr(jarbin_toolkit, "print")
    assert hasattr(jarbin_toolkit, "input")
    assert hasattr(jarbin_toolkit, "flush")
    assert hasattr(jarbin_toolkit, "stdin")
    assert hasattr(jarbin_toolkit, "stdout")
    assert hasattr(jarbin_toolkit, "stderr")
    assert hasattr(jarbin_toolkit, "critic")
    assert hasattr(jarbin_toolkit, "error")
    assert hasattr(jarbin_toolkit, "warning")
    assert hasattr(jarbin_toolkit, "valid")
    assert hasattr(jarbin_toolkit, "debug")
    assert hasattr(jarbin_toolkit, "info")
    assert hasattr(jarbin_toolkit, "bold")
    assert hasattr(jarbin_toolkit, "underline")
    assert hasattr(jarbin_toolkit, "color")
    assert hasattr(jarbin_toolkit, "up")
    assert hasattr(jarbin_toolkit, "down")
    assert hasattr(jarbin_toolkit, "left")
    assert hasattr(jarbin_toolkit, "right")
    assert hasattr(jarbin_toolkit, "clear")
    assert hasattr(jarbin_toolkit, "clear_line")
