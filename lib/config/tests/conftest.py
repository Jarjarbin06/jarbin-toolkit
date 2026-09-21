# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Config
# File         : conftest.py
#
# Author       : Jarjarbin06
# ============================================================================


import pytest

import jarbin_toolkit_config


def pytest_sessionstart(session):
    terminal = session.config.pluginmanager.get_plugin("terminalreporter")

    if terminal:
        terminal.write_sep(
            "=",
            f"Testing jarbin-toolkit-config {jarbin_toolkit_config.__version__}",
        )
