# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Config
# File         : test_config.py
#
# Author       : Jarjarbin06
# ============================================================================


from os import getxattr
from pathlib import Path

import pytest

from jarbin_toolkit_config import (
    Config,
    ConfigRuntimeJError,
    ConfigFileNotFoundJError,
    ConfigValueJError,
)


def test_create(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    assert isinstance(config, Config)
    assert config.directory == tmp_path
    assert config.name == "config"
    assert config.path == tmp_path / "config.ini"
    assert config.path.exists()


def test_create_without_extension(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
        has_extension=False,
    )

    assert config.path == tmp_path / "config"
    assert config.path.exists()


def test_create_nested_directory(
        tmp_path: Path,
    ):
    directory = tmp_path / "nested" / "directory"

    config = Config.create(
        directory,
        "config",
    )

    assert config.directory == directory
    assert config.path.exists()


def test_create_with_metadata(
        tmp_path: Path,
    ):
    metadata = {
        "description": "Test configuration",
        "environment": "test",
    }

    config = Config.create(
        tmp_path,
        "config",
        metadata=metadata,
    )

    assert config._metadata == metadata

    opened = Config.open(
        tmp_path,
        "config",
    )

    assert opened._metadata == metadata


def test_create_existing_file(
        tmp_path: Path,
    ):
    Config.create(
        tmp_path,
        "config",
    )

    with pytest.raises(ConfigRuntimeJError):
        Config.create(
            tmp_path,
            "config",
        )


def test_open(
        tmp_path: Path,
    ):
    created = Config.create(
        tmp_path,
        "config",
    )

    opened = Config.open(
        tmp_path,
        "config",
    )

    assert isinstance(opened, Config)
    assert opened.path == created.path
    assert opened.directory == created.directory
    assert opened.name == created.name


def test_open_without_extension(
        tmp_path: Path,
    ):
    Config.create(
        tmp_path,
        "config",
        has_extension=False,
    )

    config = Config.open(
        tmp_path,
        "config",
        has_extension=False,
    )

    assert config.path == tmp_path / "config"


def test_open_missing_file(
        tmp_path: Path,
    ):
    with pytest.raises(
        ConfigFileNotFoundJError,
        match="Path doesn't exist",
    ):
        Config.open(
            tmp_path,
            "config",
        )


def test_open_metadata(
        tmp_path: Path,
    ):
    metadata = {
        "description": "Test configuration",
        "environment": "test",
    }

    Config.create(
        tmp_path,
        "config",
        metadata=metadata,
    )

    config = Config.open(
        tmp_path,
        "config",
    )

    assert config._metadata == metadata


def test_constructor_is_not_public(
        tmp_path: Path,
    ):
    with pytest.raises(
        ConfigRuntimeJError,
        match="Config objects must be created with Config.create",
    ):
        Config(
            tmp_path,
            "config",
        )


def test_initial_config_is_empty(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    assert config._config.sections() == []


def test_section_add(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")

    assert config.section_exists("server")


def test_section_add_persists(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")

    opened = Config.open(
        tmp_path,
        "config",
    )

    assert opened.section_exists("server")


def test_section_add_duplicate(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")

    with pytest.raises(
        ConfigValueJError,
        match="Section already exists",
    ):
        config.section_add("server")


def test_section_remove(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")
    config.section_remove("server")

    assert not config.section_exists("server")


def test_section_remove_persists(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")
    config.section_remove("server")

    opened = Config.open(
        tmp_path,
        "config",
    )

    assert not opened.section_exists("server")


def test_section_remove_missing(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    with pytest.raises(
        ConfigValueJError,
        match="Section doesn't exist",
    ):
        config.section_remove("server")


def test_section_rename(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")

    config.section_rename(
        "server",
        "backend",
    )

    assert not config.section_exists("server")
    assert config.section_exists("backend")


def test_section_rename_preserves_options(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")
    config.set("server", "host", "localhost")
    config.set("server", "port", 8080)

    config.section_rename(
        "server",
        "backend",
    )

    assert config.get("backend", "host") == "localhost"
    assert config.get_int("backend", "port") == 8080


def test_section_rename_persists(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")
    config.set("server", "host", "localhost")

    config.section_rename(
        "server",
        "backend",
    )

    opened = Config.open(
        tmp_path,
        "config",
    )

    assert not opened.section_exists("server")
    assert opened.section_exists("backend")
    assert opened.get("backend", "host") == "localhost"


def test_section_rename_missing(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    with pytest.raises(
        ConfigValueJError,
        match="Section doesn't exist",
    ):
        config.section_rename(
            "server",
            "backend",
        )


def test_section_rename_to_existing(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")
    config.section_add("backend")

    with pytest.raises(
        ConfigValueJError,
        match="Section already exists",
    ):
        config.section_rename(
            "server",
            "backend",
        )


def test_set(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")
    config.set(
        "server",
        "host",
        "localhost",
    )

    assert config.option_exists(
        "server",
        "host",
    )
    assert config.get(
        "server",
        "host",
    ) == "localhost"


@pytest.mark.parametrize(
    "value, expected",
    [
        (123, "123"),
        (12.5, "12.5"),
        (True, "True"),
        (False, "False"),
    ],
)
def test_set_value_conversion(tmp_path, value, expected):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("test")
    config.set(
        "test",
        "value",
        value,
    )

    assert config.get(
        "test",
        "value",
    ) == expected


def test_set_updates_option(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")

    config.set(
        "server",
        "port",
        8080,
    )

    config.set(
        "server",
        "port",
        9090,
    )

    assert config.get_int(
        "server",
        "port",
    ) == 9090


def test_set_persists(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")
    config.set(
        "server",
        "host",
        "localhost",
    )

    opened = Config.open(
        tmp_path,
        "config",
    )

    assert opened.get(
        "server",
        "host",
    ) == "localhost"


def test_set_missing_section(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    with pytest.raises(
        ConfigValueJError,
        match="Section doesn't exist",
    ):
        config.set(
            "server",
            "host",
            "localhost",
        )


def test_option_remove(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")
    config.set(
        "server",
        "host",
        "localhost",
    )

    config.option_remove(
        "server",
        "host",
    )

    assert not config.option_exists(
        "server",
        "host",
    )


def test_option_remove_persists(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")
    config.set(
        "server",
        "host",
        "localhost",
    )
    config.option_remove(
        "server",
        "host",
    )

    opened = Config.open(
        tmp_path,
        "config",
    )

    assert not opened.option_exists(
        "server",
        "host",
    )


def test_option_remove_missing_section(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    with pytest.raises(
        ConfigValueJError,
        match="Section doesn't exist",
    ):
        config.option_remove(
            "server",
            "host",
        )


def test_option_remove_missing_option(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")

    with pytest.raises(
        ConfigValueJError,
        match="Option doesn't exist",
    ):
        config.option_remove(
            "server",
            "host",
        )


def test_section_exists(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    assert not config.section_exists("server")

    config.section_add("server")

    assert config.section_exists("server")


def test_option_exists(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")

    assert not config.option_exists(
        "server",
        "host",
    )

    config.set(
        "server",
        "host",
        "localhost",
    )

    assert config.option_exists(
        "server",
        "host",
    )


def test_option_exists_missing_section(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    assert not config.option_exists(
        "server",
        "host",
    )


def test_get(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")
    config.set(
        "server",
        "host",
        "localhost",
    )

    assert config.get(
        "server",
        "host",
    ) == "localhost"


def test_get_missing_section(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    with pytest.raises(
        ConfigValueJError,
        match="Section doesn't exist",
    ):
        config.get(
            "server",
            "host",
        )


def test_get_missing_option(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")

    with pytest.raises(
        ConfigValueJError,
        match="Option doesn't exist",
    ):
        config.get(
            "server",
            "host",
        )


@pytest.mark.parametrize(
    "value, expected",
    [
        ("0", 0),
        ("1", 1),
        ("-1", -1),
        ("42", 42),
        ("999999", 999999),
    ],
)
def test_get_int(tmp_path, value, expected):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("test")
    config.set(
        "test",
        "value",
        value,
    )

    assert config.get_int(
        "test",
        "value",
    ) == expected


def test_get_int_invalid_value(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("test")
    config.set(
        "test",
        "value",
        "not an integer",
    )

    with pytest.raises(
        ConfigValueJError,
        match="Option is not an integer",
    ):
        config.get_int(
            "test",
            "value",
        )


def test_get_int_missing_section(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    with pytest.raises(
        ConfigValueJError,
        match="Section doesn't exist",
    ):
        config.get_int(
            "test",
            "value",
        )


def test_get_int_missing_option(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("test")

    with pytest.raises(
        ConfigValueJError,
        match="Option doesn't exist",
    ):
        config.get_int(
            "test",
            "value",
        )


@pytest.mark.parametrize(
    "value, expected",
    [
        ("0", 0.0),
        ("1", 1.0),
        ("-1", -1.0),
        ("1.5", 1.5),
        ("-3.14", -3.14),
        ("1e3", 1000.0),
    ],
)
def test_get_float(tmp_path, value, expected):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("test")
    config.set(
        "test",
        "value",
        value,
    )

    assert config.get_float(
        "test",
        "value",
    ) == pytest.approx(expected)


def test_get_float_invalid_value(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("test")
    config.set(
        "test",
        "value",
        "not a float",
    )

    with pytest.raises(
        ConfigValueJError,
        match="Option is not a float",
    ):
        config.get_float(
            "test",
            "value",
        )


def test_get_float_missing_section(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    with pytest.raises(
        ConfigValueJError,
        match="Section doesn't exist",
    ):
        config.get_float(
            "test",
            "value",
        )


def test_get_float_missing_option(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("test")

    with pytest.raises(
        ConfigValueJError,
        match="Option doesn't exist",
    ):
        config.get_float(
            "test",
            "value",
        )


@pytest.mark.parametrize(
    "value, expected",
    [
        ("true", True),
        ("True", True),
        ("TRUE", True),
        ("yes", True),
        ("on", True),
        ("1", True),
        ("false", False),
        ("False", False),
        ("FALSE", False),
        ("no", False),
        ("off", False),
        ("0", False),
    ],
)
def test_get_bool(tmp_path, value, expected):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("test")
    config.set(
        "test",
        "value",
        value,
    )

    assert config.get_bool(
        "test",
        "value",
    ) is expected


def test_get_bool_invalid_value(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("test")
    config.set(
        "test",
        "value",
        "not a boolean",
    )

    with pytest.raises(
        ConfigValueJError,
        match="Option is not a boolean",
    ):
        config.get_bool(
            "test",
            "value",
        )


def test_get_bool_missing_section(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    with pytest.raises(
        ConfigValueJError,
        match="Section doesn't exist",
    ):
        config.get_bool(
            "test",
            "value",
        )


def test_get_bool_missing_option(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("test")

    with pytest.raises(
        ConfigValueJError,
        match="Option doesn't exist",
    ):
        config.get_bool(
            "test",
            "value",
        )


def test_set_batch(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.set_batch({
        "server": {
            "host": "localhost",
            "port": 8080,
        },
        "database": {
            "host": "localhost",
            "port": 5432,
            "enabled": True,
        },
    })

    assert config.section_exists("server")
    assert config.section_exists("database")

    assert config.get(
        "server",
        "host",
    ) == "localhost"

    assert config.get_int(
        "server",
        "port",
    ) == 8080

    assert config.get(
        "database",
        "host",
    ) == "localhost"

    assert config.get_int(
        "database",
        "port",
    ) == 5432

    assert config.get_bool(
        "database",
        "enabled",
    ) is True


def test_set_batch_updates_existing_section(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.section_add("server")
    config.set(
        "server",
        "host",
        "old",
    )

    config.set_batch({
        "server": {
            "host": "new",
            "port": 8080,
        },
    })

    assert config.get(
        "server",
        "host",
    ) == "new"

    assert config.get_int(
        "server",
        "port",
    ) == 8080


def test_set_batch_persists(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.set_batch({
        "server": {
            "host": "localhost",
            "port": 8080,
        },
    })

    opened = Config.open(
        tmp_path,
        "config",
    )

    assert opened.get(
        "server",
        "host",
    ) == "localhost"

    assert opened.get_int(
        "server",
        "port",
    ) == 8080


def test_set_batch_empty(
        tmp_path: Path,
    ):
    config = Config.create(
        tmp_path,
        "config",
    )

    config.set_batch({})

    assert config._config.sections() == []


def test_complete_configuration_persistence(
        tmp_path: Path,
    ):
    metadata = {
        "description": "Complete test",
        "environment": "testing",
    }

    config = Config.create(
        tmp_path,
        "config",
        metadata=metadata,
    )

    config.set_batch({
        "server": {
            "host": "localhost",
            "port": 8080,
            "enabled": True,
        },
        "database": {
            "host": "db.local",
            "port": 5432,
        },
    })

    config.section_rename(
        "server",
        "backend",
    )

    config.option_remove(
        "database",
        "host",
    )

    opened = Config.open(
        tmp_path,
        "config",
    )

    assert opened._metadata == metadata

    assert opened.section_exists("backend")
    assert not opened.section_exists("server")

    assert opened.get(
        "backend",
        "host",
    ) == "localhost"

    assert opened.get_int(
        "backend",
        "port",
    ) == 8080

    assert opened.get_bool(
        "backend",
        "enabled",
    ) is True

    assert opened.section_exists("database")
    assert not opened.option_exists(
        "database",
        "host",
    )

    assert opened.get_int(
        "database",
        "port",
    ) == 5432
