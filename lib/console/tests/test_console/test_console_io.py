# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/Console
# File         : test_console_io.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest
import sys

from jarbin_toolkit_console.console import IO


def test_io_stdout():
    assert IO.stdout is sys.stdout


def test_io_stdin():
    assert IO.stdin is sys.stdin


def test_io_stderr():
    assert IO.stderr is sys.stderr
