# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Log
# File         : conftest.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

import jarbin_toolkit_log


def pytest_sessionstart(session):
    terminal = session.config.pluginmanager.get_plugin("terminalreporter")

    if terminal:
        terminal.write_sep(
            "=",
            f"Testing jarbin-toolkit-log {jarbin_toolkit_log.__version__}",
        )
