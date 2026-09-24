# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Config
# File         : config.py
#
# Author       : Jarjarbin06
# ============================================================================


from configparser import ConfigParser
from os import (
    setxattr,
    getxattr,
    listxattr,
)
from pathlib import Path

from jarbin_toolkit_config.errors import (
    ConfigRuntimeJError,
    ConfigFileNotFoundJError,
    ConfigValueJError,
)


class Config:


    _CONSTRUCTOR_TOKEN = object()
    _METADATA_PREFIX = "user.jarbin."


    def _write_metadata(
            self,
        ):

        for key, value in self._metadata.items():
            setxattr(
                self.path,
                f"{self._METADATA_PREFIX}{key}",
                value.encode("utf-8"),
            )


    def _read_metadata(
            self,
        ):

        self._metadata = {
            key.removeprefix(self._METADATA_PREFIX): getxattr(
                self.path,
                key,
            ).decode("utf-8")
            for key in listxattr(self.path)
            if key.startswith(self._METADATA_PREFIX)
        }


    def _write_config(
            self,
        ):

        try:
            with self.path.open("w", encoding="utf-8") as config_file:
                self._config.write(config_file)
        except OSError as error:
            raise ConfigRuntimeJError(
                f"Failed to write config file: '{self.path}'"
            ) from error


    def _read_config(
            self,
        ):

        try:
            self._config.read(
                self.path,
                encoding="utf-8",
            )
        except OSError as error:
            raise ConfigRuntimeJError(
                f"Failed to read config file: '{self.path}'"
            ) from error


    def __init__(
            self,
            directory,
            name,
            *,
            metadata = None,
            has_extension = True,
            _token = None,
        ):

        if _token is not self._CONSTRUCTOR_TOKEN:
            raise ConfigRuntimeJError(
                "Config objects must be created with Config.create() or opened with Config.open()"
            )

        self.directory = Path(directory)
        self.name = name
        self.path = (
            self.directory
            / f"{name}{'.ini' if has_extension else ''}"
        )
        self._metadata = metadata or {}
        self._config = ConfigParser()


    def section_add(
            self,
            name,
        ):

        if self._config.has_section(name):
            raise ConfigValueJError(
                f"Section already exists: '{name}'"
            )

        self._config.add_section(name)
        self._write_config()


    def section_remove(
            self,
            name,
        ):

        if not self._config.has_section(name):
            raise ConfigValueJError(
                f"Section doesn't exist: '{name}'"
            )

        self._config.remove_section(name)
        self._write_config()


    def section_rename(
            self,
            old_name,
            new_name,
        ):

        if not self._config.has_section(old_name):
            raise ConfigValueJError(
                f"Section doesn't exist: '{old_name}'"
            )

        if self._config.has_section(new_name):
            raise ConfigValueJError(
                f"Section already exists: '{new_name}'"
            )

        options = dict(self._config.items(old_name))

        self._config.remove_section(old_name)
        self._config.add_section(new_name)

        for option, value in options.items():
            self._config.set(
                new_name,
                option,
                value,
            )

        self._write_config()


    def set(
            self,
            section,
            option,
            value,
        ):

        if not self._config.has_section(section):
            raise ConfigValueJError(
                f"Section doesn't exist: '{section}'"
            )

        self._config.set(
            section,
            option,
            str(value),
        )

        self._write_config()


    def set_batch(
            self,
            data,
        ):

        for section, options in data.items():
            if not self._config.has_section(section):
                self._config.add_section(section)

            for option, value in options.items():
                self._config.set(
                    section,
                    option,
                    str(value),
                )

        self._write_config()


    def option_remove(
            self,
            section,
            option,
        ):

        if not self._config.has_section(section):
            raise ConfigValueJError(
                f"Section doesn't exist: '{section}'"
            )

        if not self._config.has_option(section, option):
            raise ConfigValueJError(
                f"Option doesn't exist: '{option}'"
            )

        self._config.remove_option(
            section,
            option,
        )

        self._write_config()


    def section_exists(
            self,
            name,
        ):

        return self._config.has_section(name)


    def option_exists(
            self,
            section,
            option,
        ):

        return self._config.has_option(
            section,
            option,
        )


    def get(
            self,
            section,
            option,
        ):

        if not self._config.has_section(section):
            raise ConfigValueJError(
                f"Section doesn't exist: '{section}'"
            )

        if not self._config.has_option(section, option):
            raise ConfigValueJError(
                f"Option doesn't exist: '{option}'"
            )

        return self._config.get(
            section,
            option,
        )


    def get_int(
            self,
            section,
            option,
        ):

        if not self._config.has_section(section):
            raise ConfigValueJError(
                f"Section doesn't exist: '{section}'"
            )

        if not self._config.has_option(section, option):
            raise ConfigValueJError(
                f"Option doesn't exist: '{option}'"
            )

        try:
            return self._config.getint(
                section,
                option,
            )
        except ValueError as error:
            raise ConfigValueJError(
                f"Option is not an integer: '{option}'"
            ) from error


    def get_float(
            self,
            section,
            option,
        ):

        if not self._config.has_section(section):
            raise ConfigValueJError(
                f"Section doesn't exist: '{section}'"
            )

        if not self._config.has_option(section, option):
            raise ConfigValueJError(
                f"Option doesn't exist: '{option}'"
            )

        try:
            return self._config.getfloat(
                section,
                option,
            )
        except ValueError as error:
            raise ConfigValueJError(
                f"Option is not a float: '{option}'"
            ) from error


    def get_bool(
            self,
            section,
            option,
        ):

        if not self._config.has_section(section):
            raise ConfigValueJError(
                f"Section doesn't exist: '{section}'"
            )

        if not self._config.has_option(section, option):
            raise ConfigValueJError(
                f"Option doesn't exist: '{option}'"
            )

        try:
            return self._config.getboolean(
                section,
                option,
            )
        except ValueError as error:
            raise ConfigValueJError(
                f"Option is not a boolean: '{option}'"
            ) from error


    @classmethod
    def create(
            cls,
            directory,
            name,
            *,
            metadata = None,
            has_extension = True,
        ):

        new_config = cls(
            directory,
            name,
            metadata=metadata,
            has_extension=has_extension,
            _token=cls._CONSTRUCTOR_TOKEN,
        )

        try:
            new_config.directory.mkdir(
                parents=True,
                exist_ok=True,
            )

            new_config.path.touch(
                exist_ok=False,
            )
        except OSError as error:
            raise ConfigRuntimeJError(
                f"Failed to create config file: '{new_config.path}'"
            ) from error

        new_config._write_config()
        new_config._write_metadata()

        return new_config


    @classmethod
    def open(
            cls,
            directory,
            name,
            *,
            has_extension = True,
        ):

        new_config = cls(
            directory,
            name,
            has_extension=has_extension,
            _token=cls._CONSTRUCTOR_TOKEN,
        )

        if not new_config.path.exists():
            raise ConfigFileNotFoundJError(
                f"Path doesn't exist: '{new_config.path}'"
            )

        new_config._read_config()
        new_config._read_metadata()

        return new_config


__all__ = [
    'Config',
]
