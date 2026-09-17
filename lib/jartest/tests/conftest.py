import pytest

import jarbin_toolkit_jartest


def pytest_sessionstart(session):
    terminal = session.config.pluginmanager.get_plugin("terminalreporter")

    if terminal:
        terminal.write_sep(
            "=",
            f"Testing jarbin-toolkit-jartest {jarbin_toolkit_jartest.__version__}",
        )
