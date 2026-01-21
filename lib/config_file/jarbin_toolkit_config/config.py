#############################
###                       ###
###     Jarbin-ToolKit    ###
###        config         ###
###   ----config.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object, type
from typing import Any


class Config:
    """
        Config class.

        Config file tool.
    """


    def __init__(
            self,
            path : str,
            data : dict | None = None,
            *,
            file_name : str = "config.ini"
        ) -> None:
        """
            Create a new config file if 'path'/'file_name' does not exist, read otherwise.

            Parameters:
                path (str): path to folder which you want your config file to be in
                data (dict | None, optional): data to put in the config file
                file_name (str, optional): name of config file
        """

        from configparser import ConfigParser
        from platform import system

        if path[-1] != "/":
            path += "/"

        self.config : ConfigParser | None = ConfigParser()
        self.path : str | None = path
        self.file_name : str | None = file_name

        if system() == "Windows":

            ## cannot be tested with pytest ##

            self.path = self.path.replace("/", "\\") # pragma: no cover
            self.file_name = self.file_name.replace("/", "\\") # pragma: no cover

        elif system() == "Linux":

            ## cannot be tested with pytest ##

            self.path = self.path.replace("\\", "/") # pragma: no cover
            self.file_name = self.file_name.replace("/", "\\") # pragma: no cover

        if Config.exist(self.path):
            self.config.read(self.path + self.file_name)

        else:
            if not data and self.file_name == "config.ini":
                data = {}

            with open(str(self.path) + str(self.file_name), 'w') as config_file:
                for key in data:
                    self.config[key] = data[key]

                self.config.write(config_file)

            config_file.close()


    def set(
            self,
            section : str,
            option : str,
            data : Any
        ) -> None:
        """
            Set a new value in a config file.

            Parameters:
                section (str): section name
                option (str): option name
                data (Any): data to put in the config file
        """

        self.config.set(section, option, str(data))

        with open(str(self.path) + str(self.file_name), 'w') as config_file:
            self.config.write(config_file)

        config_file.close()


    def get(
            self,
            section : str,
            option : str,
            wanted_type : type = str
        ) -> Any:
        """
            Get a value from the config file.

            Parameters:
                section (str): section name
                option (str): option name
                wanted_type (type, optional): returned type

            Returns:
                Any: data retrieved from config file and of type 'wanted_type'
        """

        return wanted_type(self.config.get(section, option))


    def get_bool(
            self,
            section : str,
            option : str
        ) -> bool:
        """
            Get a value as a bool from the config file.

            Parameters:
                section (str): section name
                option (str): option name

            Returns:
                Any: data retrieved from config file and of type 'wanted_type'
        """

        return self.config.getboolean(section, option)


    def get_int(
            self,
            section : str,
            option : str
        ) -> Any:
        """
            Get a value as a int from the config file.

            Parameters:
                section (str): section name
                option (str): option name

            Returns:
                Any: data retrieved from config file and of type 'wanted_type'
        """

        return self.config.getint(section, option)


    def get_float(
            self,
            section : str,
            option : str
        ) -> Any:
        """
            Get a value as a float from the config file.

            Parameters:
                section (str): section name
                option (str): option name

            Returns:
                Any: data retrieved from config file and of type 'wanted_type'
        """

        return self.config.getfloat(section, option)


    def delete(
            self,
            cached : bool = False
        ) -> bool:
        """
            Delete the config file.

            Parameters:
                cached (bool, optional): keep the config file's data in memory

            Returns:
                bool: True if deleted else False
        """

        from os import remove

        remove(self.path + self.file_name)

        if not cached:
            self.config = None

        if not Config.exist(self.path, file_name=self.file_name):
            self.path = None
            self.file_name = None
            return True

        ## cannot be tested with pytest ##

        else:
            return False # pragma: no cover


    @staticmethod
    def exist(
            path : str,
            *,
            file_name : str = "config.ini"
        ) -> bool:
        """
            Check if a config file config.ini is empty or doesn't exist

            Returns:
                bool: False if empty or not existing, True otherwise
                file_name (str, optional): name of config file
        """

        if path[-1] != "/":
            path += "/"

        empty_config : bool = True

        try :
            with open(path + file_name, 'r') as config_file:
                if config_file.read() == "":
                    empty_config = False
            config_file.close()

        except FileNotFoundError:
            empty_config = False

        return empty_config


    def __repr__(
            self
        ) -> str:
        """
            Convert Config object to string.

            Returns:
                str: Config string
        """

        return f"Config({repr(self.path)}, ?, {repr(self.file_name)})"
