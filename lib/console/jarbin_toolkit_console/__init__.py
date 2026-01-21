#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


########################
# Fatal Error Printing #
########################


def _fatal_error(
        err : Exception
    ) -> None:
    """
        print an error message and exit (with code 84)
    """

    ## cannot be tested with pytest ##

    print(f"\033[101m \033[0m \033[91m{err}\033[0m")  # pragma: no cover
    print(
        f"\033[103m \033[0m \033[93mepitech_console launched with fatal error\033[0m\n"
        "\033[103m \033[0m\n"
        "\033[103m \033[0m \033[93mPlease reinstall with :\033[0m\n"
        "\033[103m \033[0m \033[93m    'pip install --upgrade --force-reinstall epitech_console'\033[0m\n"
        "\033[103m \033[0m\n"
        "\033[103m \033[0m \033[93mPlease report the issue here : https://github.com/Jarjarbin06/epitech_console/issues\033[0m\n"
    )  # pragma: no cover
    exit(84)  # pragma: no cover


##########
# Import #
##########


"""try:
    from jarbin_toolkit_console import (
        Animation,
        ANSI,
        System,
        Text
    )
    from jarbin_toolkit_console.console import Console

## cannot be tested with pytest ##

except Exception as error:  # pragma: no cover
    _fatal_error(error)  # pragma: no cover"""

from jarbin_toolkit_console import (
    Animation,
    ANSI,
    System,
    Text
)
from jarbin_toolkit_console.console import Console

#############
# Functions #
#############


def _banner(
    ) -> None:
    """
        Show a simple banner.
    """

    banner_size = 50

    epitech = ANSI.Color.epitech_fg()
    epitech_dark = ANSI.Color.epitech_dark_fg()
    reset = ANSI.Color(ANSI.Color.C_RESET)

    offset_t = Text.Text("  ")
    title_t = epitech + Text.Text(f'{System.Setting.S_PACKAGE_NAME}').bold().underline() + reset + "  " + Text.Text.url_link(
        "https://github.com/Jarjarbin06/epitech_console", text="repository")
    version_t = Text.Text(" " * (10 - len(System.Setting.S_PACKAGE_VERSION))) + epitech_dark + Text.Text("version ").italic() + Text.Text(
        f'{System.Setting.S_PACKAGE_VERSION}').bold() + reset
    desc_t = Text.Text("   Text • Animation • ANSI • Error • System   ").italic()
    line_t = epitech + ("─" * banner_size) + reset

    System.Console.print(line_t, offset_t + title_t + " " + version_t + offset_t, offset_t + desc_t + offset_t, line_t, separator="\n")


def init(
        banner: bool | None = None,
    ) -> None:
    """
        init() initializes the epitech console package and show a banner (if SETTING : show-banner = True in config.ini)

        Parameters:
            banner (bool | None, optional) : Override the show-banner setting
    """

    try:
        if (System.Setting.S_SETTING_SHOW_BANNER and banner is None) or banner == True:
            _banner()
        System.Setting.update()
        Animation.BasePack.update()
        ANSI.BasePack.update()
        if System.Setting.S_SETTING_LOG_MODE:
            System.Setting.S_LOG_FILE.log("INFO", "module", "epitech_console initialized") # pragma: no cover

    ## cannot be tested with pytest ##

    except System.Error.Error as error: # pragma: no cover
        print(error) # pragma: no cover
        print(System.Error.Error.lauch_error()) # pragma: no cover
        exit(84)

    except Exception as error: # pragma: no cover
        _fatal_error(error) # pragma: no cover


def quit(
        *,
        show : bool = False,
        delete_log: bool = False
    ) -> None:
    """
        quit() uninitializes the epitech console package

        Parameters:
            show (bool, optional) : show the log file on terminal
            delete_log (bool, optional) : delete the log file
    """

    if System.Setting.S_SETTING_LOG_MODE:

        ## cannot be tested with pytest ##

        System.Setting.S_LOG_FILE.log("INFO", "module", "epitech_console uninitialized") # pragma: no cover
        System.Setting.S_LOG_FILE.close() # pragma: no cover
        System.Setting.S_CONFIG_FILE.set("SETTING", "opened-log", "null") # pragma: no cover

        if show: # pragma: no cover
            System.Console.print(str(System.Setting.S_LOG_FILE)) # pragma: no cover

        if delete_log: # pragma: no cover
            System.Setting.S_LOG_FILE.close(delete=True) # pragma: no cover


######################
# Module's Variables #
######################


C_RESET : int = 0
C_BOLD : int = 1
C_ITALIC : int = 3
C_UNDERLINE : int = 4
C_FLASH_SLOW : int = 5
C_FLASH_FAST : int = 6
C_HIDDEN : int = 8
C_STRIKETHROUGH : int = 9

C_FG_DARK : int = 2
C_FG_DARK_GREY : int = 30
C_FG_DARK_RED : int = 31
C_FG_DARK_GREEN : int = 32
C_FG_DARK_YELLOW : int = 33
C_FG_DARK_BLUE : int = 34
C_FG_DARK_LAVANDA : int = 35
C_FG_DARK_CYAN : int = 36
C_FG_DARK_WHITE : int = 37
C_FG_GREY : int = 90
C_FG_RED : int = 91
C_FG_GREEN : int = 92
C_FG_YELLOW : int = 93
C_FG_BLUE : int = 94
C_FG_LAVANDA : int = 95
C_FG_CYAN : int = 96
C_FG_WHITE : int = 97

C_BG : int = 7
C_BG_DARK_GREY : int = 40
C_BG_DARK_RED : int = 41
C_BG_DARK_GREEN : int = 42
C_BG_DARK_YELLOW : int = 43
C_BG_DARK_BLUE : int = 44
C_BG_DARK_LAVANDA : int = 45
C_BG_DARK_CYAN : int = 46
C_BG_DARK_WHITE : int = 47
C_BG_GREY : int = 100
C_BG_RED : int = 101
C_BG_GREEN : int = 102
C_BG_YELLOW : int = 103
C_BG_BLUE : int = 104
C_BG_LAVANDA : int = 105
C_BG_CYAN : int = 106
C_BG_WHITE : int = 107


__version__ : str = 'v0.2.0'
__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.amaraggi@epitech.eu'


__all__ : list[str] = [
    'Animation',
    'ANSI',
    'System',
    'Text',
    'C_RESET',
    'C_BOLD',
    'C_ITALIC',
    'C_UNDERLINE',
    'C_FLASH_SLOW',
    'C_FLASH_FAST',
    'C_HIDDEN',
    'C_STRIKETHROUGH',
    'C_FG_DARK',
    'C_FG_DARK_GREY',
    'C_FG_DARK_RED',
    'C_FG_DARK_GREEN',
    'C_FG_DARK_YELLOW',
    'C_FG_DARK_BLUE',
    'C_FG_DARK_LAVANDA',
    'C_FG_DARK_CYAN',
    'C_FG_DARK_WHITE',
    'C_FG_GREY',
    'C_FG_RED',
    'C_FG_GREEN',
    'C_FG_YELLOW',
    'C_FG_BLUE',
    'C_FG_LAVANDA',
    'C_FG_CYAN',
    'C_FG_WHITE',
    'C_BG',
    'C_BG_DARK_GREY',
    'C_BG_DARK_RED',
    'C_BG_DARK_GREEN',
    'C_BG_DARK_YELLOW',
    'C_BG_DARK_BLUE',
    'C_BG_DARK_LAVANDA',
    'C_BG_DARK_CYAN',
    'C_BG_DARK_WHITE',
    'C_BG_GREY',
    'C_BG_RED',
    'C_BG_GREEN',
    'C_BG_YELLOW',
    'C_BG_BLUE',
    'C_BG_LAVANDA',
    'C_BG_CYAN',
    'C_BG_WHITE',
    'init',
    'quit',
    '__version__',
    '__author__',
    '__email__'
]


##################
# Initialization #
##################


init(banner=False)
quit(delete_log=True)
