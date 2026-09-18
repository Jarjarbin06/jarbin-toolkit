import pytest

import jarbin_toolkit_error_python


def pytest_sessionstart(session):
    terminal = session.config.pluginmanager.get_plugin("terminalreporter")

    if terminal:
        terminal.write_sep(
            "=",
            f"Testing jarbin-toolkit-error:python {jarbin_toolkit_error_python.__version__}",
        )
