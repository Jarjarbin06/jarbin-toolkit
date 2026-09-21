# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : conftest.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

import jarbin_toolkit_error


def pytest_sessionstart(session):
    terminal = session.config.pluginmanager.get_plugin("terminalreporter")

    if terminal:
        terminal.write_sep(
            "=",
            f"Testing jarbin-toolkit-error {jarbin_toolkit_error.__version__}",
        )
