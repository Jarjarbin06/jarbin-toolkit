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


quit(delete_log=True)
