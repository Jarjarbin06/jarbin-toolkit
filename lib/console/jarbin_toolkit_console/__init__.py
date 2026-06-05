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

    import traceback  # pragma: no cover

    ## cannot be tested with pytest ##

    tb = err.__traceback__  # pragma: no cover
    filename = "<unknown>"  # pragma: no cover
    lineno = 0  # pragma: no cover

    if tb is not None:  # pragma: no cover
        last = traceback.extract_tb(tb)[-1]  # pragma: no cover
        filename = last.filename  # pragma: no cover
        lineno = last.lineno  # pragma: no cover

    print(f"\033[101m \033[0m \033[91m{repr(err)}\033[0m")  # pragma: no cover
    print(f"\033[101m \033[0m \033[91m\tFile: {repr(filename)}:{repr(lineno)})\033[0m")  # pragma: no covers
    print(
        f"\033[103m \033[0m \033[93mjarbin_toolkit_console launched with fatal error\033[0m\n"
        "\033[103m \033[0m\n"
        "\033[103m \033[0m \033[93mPlease reinstall with :\033[0m\n"
        "\033[103m \033[0m \033[93m    'pip install --upgrade --force-reinstall jarbin_toolkit_console'\033[0m\n"
        "\033[103m \033[0m\n"
        "\033[103m \033[0m \033[93mPlease report the issue here : https://github.com/Jarjarbin06/jarbin-toolkit/issues\033[0m\n"
    )  # pragma: no cover
    exit(84)  # pragma: no cover


##########
# Import #
##########


try:
    from jarbin_toolkit_console import (
        Animation,
        ANSI,
        System,
        Text
    )
    from jarbin_toolkit_console.console import Console

## cannot be tested with pytest ##

except Exception as error:  # pragma: no cover
    _fatal_error(error)  # pragma: no cover


#############
# Functions #
#############


def _banner(
    ) -> None:
    """
        Show a simple banner.
    """

    banner_size = 60

    epitech = ANSI.Color.epitech_fg()
    epitech_dark = ANSI.Color.epitech_dark_fg()
    reset = ANSI.Color(ANSI.Color.C_RESET)

    offset_title_t = Text.Text("  ")
    offset_desc_t = Text.Text("       ")
    title_t = epitech + Text.Text(f'{System.Setting.S_PACKAGE_NAME}').bold().underline() + reset + "  " + Text.Text.url_link(
        "https://github.com/Jarjarbin06/jarbin-toolkit", text="repository")
    version_t = Text.Text(" " * (10 - len(System.Setting.S_PACKAGE_VERSION))) + epitech_dark + Text.Text("version ").italic() + Text.Text(
        f'{System.Setting.S_PACKAGE_VERSION}').bold() + reset
    desc_t = Text.Text("   Text • Animation • ANSI • Error • System   ").italic()
    line_t = epitech + ("─" * banner_size) + reset

    Console.print(line_t, offset_title_t + title_t + Text.Text("    ") + version_t + offset_title_t, offset_desc_t + desc_t + offset_desc_t, line_t, separator="\n")


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
            Console.print(str(System.Setting.S_LOG_FILE)) # pragma: no cover

        if delete_log: # pragma: no cover
            System.Setting.S_LOG_FILE.close(delete=True) # pragma: no cover


__all__ : list[str] = [
    'Animation',
    'ANSI',
    'System',
    'Text',
    'Console',
    'init',
    'quit'
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.amaraggi@epitech.eu'
__version__ : str = "0.1.2.2"
__license__ : str = "GPL"
