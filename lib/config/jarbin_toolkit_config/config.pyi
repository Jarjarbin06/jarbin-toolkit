from configparser import ConfigParser
from os import PathLike
from pathlib import Path
from typing import Any, Optional


class Config:
    """
        Config file

        Attributes
        ----------
        directory : Path
            Directory of the config

        name : Path
            Name of the config

        path : Path
            Path of the config
    """


    directory: Path
    name: str
    path: Path


    def __init__(
            self,
            directory: PathLike | str,
            name: str,
            *,
            metadata: Optional[dict[str, Any]] = None,
            has_extension: bool = True,
            _token: object = None,
        ) -> None:
        """
            Initialize a Config. Not to use as is, use 'Config.create(...)' or 'Config.open(...)'

            Parameters
            ----------
            directory : PathLike | str
                Directory of the config

            name : str
                Name of the config

            metadata : Optional[dict[str, Any]]
                Custom metadata to link to the file

            has_extension : bool
                Add config '.ini' extension to the file name

            Raises
            ----------
            ConfigRuntimeJError
                Config init used as is.
        """
        ...


    def section_add(
            self,
            name: str,
        ) -> None:
        """
            Add a section

            Parameters
            ----------
            name : str
                Section name

            Raises
            ----------
            ConfigValueJError
                Section exists
        """
        ...


    def section_remove(
            self,
            name: str,
        ) -> None:
        """
            Remove a section

            Parameters
            ----------
            name : str
                Section name

            Raises
            ----------
            ConfigValueJError
                Section doesn't exist
        """
        ...


    def section_rename(
            self,
            old_name: str,
            new_name: str,
        ) -> None:
        """
            Add a section

            Parameters
            ----------
            old_name : str
                Old section name

            new_name : str
                New section name

            Raises
            ----------
            ConfigValueJError
                Old section doesn't exist
                New section exists
        """
        ...


    def set(
            self,
            section: str,
            option: str,
            value: Any,
        ) -> None:
        """
            Store a value

            Parameters
            ----------
            section : str
                Section

            option : str
                Option

            value : Any
                Value

            Raises
            ----------
            ConfigValueJError
                Old section doesn't exist
        """
        ...


    def set_batch(
            self,
            data: dict[str, Any],
        ) -> None:
        """
            Store values in batch

            Parameters
            ----------
            data : dict[str, Any]
                Data dictionary
        """
        ...


    def option_remove(
            self,
            section: str,
            option: str,
        ) -> None:
        """
            Remove an option

            Parameters
            ----------
            section : str
                Section

            option : str
                Option

            Raises
            ----------
            ConfigValueJError
                Section, option doesn't exist
        """
        ...


    def section_exists(
            self,
            name: str,
        ) -> bool:
        """
            Check is a section exists

            Parameters
            ----------
            name : str
                Section name

            Returns
            ----------
            bool
                Section exists
        """
        ...


    def option_exists(
            self,
            section: str,
            option: str,
        ) -> bool:
        """
            Check is an option exists in the selected section
        
            Parameters
            ----------
            section : str
                Section

            option : str
                Option

            Returns
            ----------
            bool
                Option exists
        """
        ...


    def get(
            self,
            section: str,
            option: str,
        ) -> str:
        """
            Get an option's value

            Parameters
            ----------
            section : str
                Section

            option : str
                Option

            Returns
            ----------
            str
                Option's value

            Raises
            ----------
            ConfigValueJError
                Section, option doesn't exist
        """
        ...


    def get_int(
            self,
            section: str,
            option: str,
        ) -> int:
        """
            Get an option's value as integer

            Parameters
            ----------
            section : str
                Section

            option : str
                Option

            Returns
            ----------
            int
                Option's value

            Raises
            ----------
            ConfigValueJError
                Section, option doesn't exist
                Value is not an integer
        """
        ...


    def get_float(
            self,
            section: str,
            option: str,
        ) -> float:
        """
            Get an option's value as floating point number

            Parameters
            ----------
            section : str
                Section

            option : str
                Option

            Returns
            ----------
            float
                Option's value

            Raises
            ----------
            ConfigValueJError
                Section, option doesn't exist
                Value is not a floating point number
        """
        ...


    def get_bool(
            self,
            section: str,
            option: str,
        ) -> bool:
        """
            Get an option's value as boolean

            Parameters
            ----------
            section : str
                Section

            option : str
                Option

            Returns
            ----------
            boolean
                Option value

            Raises
            ----------
            ConfigValueJError
                Section, option doesn't exist
                Value is not a boolean
        """
        ...


    @classmethod
    def create(
            cls,
            directory: PathLike | str,
            name: str,
            *,
            metadata: Optional[dict[str, Any]] = None,
            has_extension: bool = True,
        ) -> Config:
        """
            Create a new config file

            Parameters
            ----------
            directory : PathLike | str
                Directory

            name : str
                Name

            metadata : Optional[dict[str, Any]]
                Metadata

            has_extension : bool
                Add '.ini' file extension

            Returns
            ----------
            Config
                New config object

            Raises
            ----------
            ConfigRuntimeJError
                Creation failed
        """
        ...


    @classmethod
    def open(
            cls,
            directory: PathLike | str,
            name: str,
            *,
            has_extension: bool = True,
        ) -> Config:
        """
            Open a config file

            Parameters
            ----------
            directory : PathLike | str
                Directory

            name : str
                Name

            has_extension : bool
                Config has '.ini' file extension

            Returns
            ----------
            Config
                Config object

            Raises
            ----------
            ConfigFileNotFoundJError
                File not found
        """
        ...


    _CONSTRUCTOR_TOKEN: object
    _METADATA_PREFIX: str
    _metadata: dict[str, Any]
    _config: ConfigParser


    def _write_metadata(
            self,
        ):
        ...


    def _read_metadata(
            self,
        ):
        ...


    def _write_config(
            self,
        ):
        ...


    def _read_config(
            self,
        ):
        ...


__all__: list[str]
