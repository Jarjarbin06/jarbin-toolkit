# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console
# File         : conftest.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

import os

os.environ["JARBIN_CONSOLE_NO_BANNER"] = "1"

import jarbin_toolkit_console


def pytest_sessionstart(session):
    terminal = session.config.pluginmanager.get_plugin("terminalreporter")

    if terminal:
        terminal.write_sep(
            "=",
            f"Testing jarbin-toolkit-console {jarbin_toolkit_console.__version__}",
        )
