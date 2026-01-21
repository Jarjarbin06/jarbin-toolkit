import pytest


import jarbin_toolkit_console as EC
from jarbin_toolkit_console import (init, quit)


init()


def test_module_has_attributes(
    ) -> None:
    assert hasattr(EC, "init")
    assert hasattr(EC, "quit")
    assert hasattr(EC, "Animation")
    assert hasattr(EC, "ANSI")
    assert hasattr(EC, "System")
    assert hasattr(EC, "Text")
    assert hasattr(EC, "C_RESET")
    assert hasattr(EC, "C_BOLD")
    assert hasattr(EC, "C_ITALIC")
    assert hasattr(EC, "C_UNDERLINE")
    assert hasattr(EC, "C_FLASH_SLOW")
    assert hasattr(EC, "C_FLASH_FAST")
    assert hasattr(EC, "C_HIDDEN")
    assert hasattr(EC, "C_STRIKETHROUGH")
    assert hasattr(EC, "C_FG_DARK")
    assert hasattr(EC, "C_FG_DARK_GREY")
    assert hasattr(EC, "C_FG_DARK_RED")
    assert hasattr(EC, "C_FG_DARK_GREEN")
    assert hasattr(EC, "C_FG_DARK_YELLOW")
    assert hasattr(EC, "C_FG_DARK_BLUE")
    assert hasattr(EC, "C_FG_DARK_LAVANDA")
    assert hasattr(EC, "C_FG_DARK_CYAN")
    assert hasattr(EC, "C_FG_DARK_WHITE")
    assert hasattr(EC, "C_FG_GREY")
    assert hasattr(EC, "C_FG_RED")
    assert hasattr(EC, "C_FG_GREEN")
    assert hasattr(EC, "C_FG_YELLOW")
    assert hasattr(EC, "C_FG_BLUE")
    assert hasattr(EC, "C_FG_LAVANDA")
    assert hasattr(EC, "C_FG_CYAN")
    assert hasattr(EC, "C_FG_WHITE")
    assert hasattr(EC, "C_BG")
    assert hasattr(EC, "C_BG_DARK_GREY")
    assert hasattr(EC, "C_BG_DARK_RED")
    assert hasattr(EC, "C_BG_DARK_GREEN")
    assert hasattr(EC, "C_BG_DARK_YELLOW")
    assert hasattr(EC, "C_BG_DARK_BLUE")
    assert hasattr(EC, "C_BG_DARK_LAVANDA")
    assert hasattr(EC, "C_BG_DARK_CYAN")
    assert hasattr(EC, "C_BG_DARK_WHITE")
    assert hasattr(EC, "C_BG_GREY")
    assert hasattr(EC, "C_BG_RED")
    assert hasattr(EC, "C_BG_GREEN")
    assert hasattr(EC, "C_BG_YELLOW")
    assert hasattr(EC, "C_BG_BLUE")
    assert hasattr(EC, "C_BG_LAVANDA")
    assert hasattr(EC, "C_BG_CYAN")
    assert hasattr(EC, "C_BG_WHITE")


quit(delete_log=True)
