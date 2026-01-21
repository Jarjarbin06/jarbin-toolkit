#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###   ----setting.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


class Setting:
    """
        Setting class.

        All module's settings imported.

        Attributes:
            S_OS (str): os mode.

            S_CONFIG_FILE (Config | None): module's config file.
            S_LOG_FILE (Log | None): log file.

            S_PACKAGE_NAME (str): package name.
            S_PACKAGE_VERSION (str): package version.
            S_PACKAGE_DESCRIPTION (str): package description.
            S_PACKAGE_REPOSITORY (str): package repository url.

            S_SETTING_SHOW_BANNER (bool): show banner.
            S_SETTING_AUTO_COLOR (bool): auto color.
            S_SETTING_SAFE_MODE (bool): safe mode.
            S_SETTING_MINIMAL_MODE (bool): minimal mode.
            S_SETTING_DEBUG_MODE (bool): debug mode.
            S_SETTING_LOG_MODE (bool): log mode.
    """


    from jarbin_toolkit_console.System import Log
    from jarbin_toolkit_console.System import Config


    S_OS : str | None = None

    S_CONFIG_FILE : Config | None = None
    S_LOG_FILE : Log | None = None

    S_PACKAGE_PATH : str = "null"
    S_PACKAGE_NAME : str = "null"
    S_PACKAGE_VERSION : str = "null"
    S_PACKAGE_DESCRIPTION : str = "null"
    S_PACKAGE_REPOSITORY : str = "null"

    S_SETTING_SHOW_BANNER : bool = False
    S_SETTING_AUTO_COLOR : bool = False
    S_SETTING_SAFE_MODE : bool = True
    S_SETTING_MINIMAL_MODE : bool = True
    S_SETTING_DEBUG_MODE : bool = False
    S_SETTING_LOG_MODE : bool = False
    S_SETTING_OPENED_LOG : str = "null"


    @staticmethod
    def update(
        ) -> None:
        """
            Initialize the BasePack class
        """

        from platform import system
        from jarbin_toolkit_console.System import Config
        from jarbin_toolkit_console.System import Log

        Setting.S_OS = system()

        if Setting.S_OS == "Windows":

            ## cannot be tested with pytest ##

            Setting.S_PACKAGE_PATH = __file__.removesuffix("System\\setting.py") # pragma: no cover

        elif Setting.S_OS == "Linux":

            ## cannot be tested with pytest ##

            Setting.S_PACKAGE_PATH = __file__.removesuffix("System/setting.py") # pragma: no cover

        else:

            ## cannot be tested with pytest ##

            Setting.S_PACKAGE_PATH = __file__.removesuffix("System/setting.py").removesuffix("System\\setting.py") # pragma: no cover

        Setting.S_CONFIG_FILE = Config(Setting.S_PACKAGE_PATH)

        Setting.S_PACKAGE_NAME = Setting.S_CONFIG_FILE.get("PACKAGE", "name")
        Setting.S_PACKAGE_VERSION = Setting.S_CONFIG_FILE.get("PACKAGE", "version")
        Setting.S_PACKAGE_DESCRIPTION = Setting.S_CONFIG_FILE.get("PACKAGE", "description")
        Setting.S_PACKAGE_REPOSITORY = Setting.S_CONFIG_FILE.get("PACKAGE", "repository")

        Setting.S_SETTING_SHOW_BANNER = Setting.S_CONFIG_FILE.get_bool("SETTING", "show-banner")
        Setting.S_SETTING_AUTO_COLOR = Setting.S_CONFIG_FILE.get_bool("SETTING", "auto-color")
        Setting.S_SETTING_SAFE_MODE = Setting.S_CONFIG_FILE.get_bool("SETTING", "safe-mode")
        Setting.S_SETTING_MINIMAL_MODE = Setting.S_CONFIG_FILE.get_bool("SETTING", "minimal-mode")
        Setting.S_SETTING_DEBUG_MODE = Setting.S_CONFIG_FILE.get_bool("SETTING", "debug")
        Setting.S_SETTING_LOG_MODE = Setting.S_CONFIG_FILE.get_bool("SETTING", "log")

        if Setting.S_SETTING_LOG_MODE:

            ## cannot be tested with pytest ##

            Setting.S_SETTING_OPENED_LOG = Setting.S_CONFIG_FILE.get("SETTING", "opened-log") # pragma: no cover

            if Setting.S_SETTING_OPENED_LOG == "null": # pragma: no cover
                Setting.S_LOG_FILE = Log(Setting.S_PACKAGE_PATH + "log") # pragma: no cover
                Setting.S_CONFIG_FILE.set("SETTING", "opened-log", Setting.S_LOG_FILE.log_file_name) # pragma: no cover
                Setting.S_SETTING_OPENED_LOG = Setting.S_CONFIG_FILE.get("SETTING", "opened-log") # pragma: no cover

            else: # pragma: no cover
                Setting.S_LOG_FILE = Log(Setting.S_PACKAGE_PATH + ("log\\" if system() == "Windows" else "log/"), file_name=Setting.S_SETTING_OPENED_LOG) # pragma: no cover

            if Setting.S_LOG_FILE is None: # pragma: no cover
                print('\x1b[101 \x1b[0m \x1b[91mAn error occured when updating setting S_LOG_FILE (currently equal \"None\"\x1b[0m') # pragma: no cover
            Setting.S_LOG_FILE.log("INFO", "function", "System.Setting.update(): setting updated") # pragma: no cover
