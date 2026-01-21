import pytest
from types import NoneType


from jarbin_toolkit_console.System import Setting, Log, Config
from jarbin_toolkit_console import (init, quit)


init()


def test_system_has_attributes(
    ) -> None:
    assert hasattr(Setting, "S_OS")
    assert hasattr(Setting, "S_CONFIG_FILE")
    assert hasattr(Setting, "S_LOG_FILE")
    assert hasattr(Setting, "S_PACKAGE_NAME")
    assert hasattr(Setting, "S_PACKAGE_VERSION")
    assert hasattr(Setting, "S_PACKAGE_DESCRIPTION")
    assert hasattr(Setting, "S_PACKAGE_REPOSITORY")
    assert hasattr(Setting, "S_SETTING_SHOW_BANNER")
    assert hasattr(Setting, "S_SETTING_AUTO_COLOR")
    assert hasattr(Setting, "S_SETTING_SAFE_MODE")
    assert hasattr(Setting, "S_SETTING_MINIMAL_MODE")
    assert hasattr(Setting, "S_SETTING_DEBUG_MODE")
    assert hasattr(Setting, "S_SETTING_LOG_MODE")


def test_system_types(
    ) -> None:
    assert isinstance(Setting.S_OS, str)
    assert isinstance(Setting.S_CONFIG_FILE, Config)
    assert isinstance(Setting.S_LOG_FILE, (Log, NoneType))
    assert isinstance(Setting.S_PACKAGE_NAME, str)
    assert isinstance(Setting.S_PACKAGE_VERSION, str)
    assert isinstance(Setting.S_PACKAGE_DESCRIPTION, str)
    assert isinstance(Setting.S_PACKAGE_REPOSITORY, str)
    assert isinstance(Setting.S_SETTING_SHOW_BANNER, bool)
    assert isinstance(Setting.S_SETTING_AUTO_COLOR, bool)
    assert isinstance(Setting.S_SETTING_SAFE_MODE, bool)
    assert isinstance(Setting.S_SETTING_MINIMAL_MODE, bool)
    assert isinstance(Setting.S_SETTING_DEBUG_MODE, bool)
    assert isinstance(Setting.S_SETTING_LOG_MODE, bool)


quit(delete_log=True)
