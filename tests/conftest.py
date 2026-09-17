import pytest

import jarbin_toolkit


def pytest_sessionstart(session):
    terminal = session.config.pluginmanager.get_plugin("terminalreporter")

    if terminal:
        terminal.write_sep(
            "=",
            f"Testing jarbin-toolkit {jarbin_toolkit.__version__}",
        )
