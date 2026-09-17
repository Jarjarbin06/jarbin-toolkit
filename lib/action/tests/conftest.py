import pytest

import jarbin_toolkit_action


def pytest_sessionstart(session):
    terminal = session.config.pluginmanager.get_plugin("terminalreporter")

    if terminal:
        terminal.write_sep(
            "=",
            f"Testing jarbin-toolkit-action {jarbin_toolkit_action.__version__}",
        )
