#############################
###                       ###
###     Jarbin-ToolKit    ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


import jarbin_toolkit_action as Action
import jarbin_toolkit_config as Config_parent
import jarbin_toolkit_console as Console
import jarbin_toolkit_error as Error
import jarbin_toolkit_log as Log_parent
import jarbin_toolkit_time as Time
from collections.abc import Callable
from typing import Any
import sys
import os
import platform


Config : object = Config_parent.Config
Log : object = Log_parent.Log


def __getattr__(
        name: str
    ) -> dict[str, str]:
    """
        Get the attribute corresponding to "name"
        Raise an AttributeError if the attribute is not found

        Parameters:
            name (str): name of the attribute

        Returns:
            dict[str, str]: attribute
    """

    if name in __all__:
        return globals()[name]
    raise AttributeError(name)


def get_info(
    ) -> dict[str, str]:
    """
        Get info about the Jarbin toolkit

        Returns:
            dict[str, str | dict[str, str]]: info
    """

    return {
        "name": "Jarbin-ToolKit",
        "version": __version__,
        "subversions": __version__,
        "author": __author__,
        "email": __email__,
        "license": __license__
    }


def benchmark(
        function: Callable,
        *args: Any,
        **kwargs: Any
    ) -> tuple[Any, float]:
    """
    Benchmark the function

    Parameters:
        function (Callable): function to benchmark
        *args (list[Any]): arguments
        **kwargs (dict[str, Any]): keyword arguments

    Returns:
        tuple[Any, float]: benchmark result and elapsed time
    """
    sw = Time.StopWatch(True)
    result = function(*args, **kwargs)
    return result, sw.elapsed()


def fail(
        message: str = "an error occurred"
    ) -> None:
    """
        Raise an Error Exception with a message

        Parameters:
            message (str, optional): message
    """
    raise Error.Error(message)


def text(
        *args: Any
    ) -> Console.Text.Text:
    return Console.Text.Text(list(args))


IS_TTY: bool = sys.stdout.isatty()
OS: str = platform.system()
TERM: str = os.environ.get("TERM", "")


## API Shortcuts ##
# Time #
sleep : Callable = Time.Time.wait
pause : Callable = Time.Time.pause

# Console #
print : Callable = Console.Console.print
input : Callable = Console.Console.input
flush : Callable = Console.Console.flush
stdin : Callable = Console.Console.stdin
stdout : Callable = Console.Console.stdout
stderr : Callable = Console.Console.stderr
critic : Callable = Console.Text.Format.critic
error : Callable = Console.Text.Format.error
warning : Callable = Console.Text.Format.warning
valid : Callable = Console.Text.Format.valid
debug : Callable = Console.Text.Format.debug
info : Callable = Console.Text.Format.info
bold : Callable = Console.Text.Format.bold
underline : Callable = Console.Text.Format.underline
color : Callable = Console.ANSI.Color.color
up : Callable = Console.ANSI.Cursor.up
down : Callable = Console.ANSI.Cursor.down
left : Callable = Console.ANSI.Cursor.left
right : Callable = Console.ANSI.Cursor.right
clear : Callable = Console.ANSI.Line.clear
clear_line : Callable = Console.ANSI.Line.clear_line


__all__ : list[str] = [
    'Action',
    'Config',
    'Console',
    'Error',
    'Log',
    'Time',
    'get_info',
    'benchmark',
    'fail',
    'text',
    'IS_TTY',
    'OS',
    'TERM',
    'sleep',
    'pause',
    'print',
    'input',
    'flush',
    'stdin',
    'stdout',
    'stderr',
    'critic',
    'error',
    'warning',
    'valid',
    'debug',
    'info',
    'bold',
    'underline',
    'color',
    'up',
    'down',
    'left',
    'right',
    'clear',
    'clear_line'
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.amaraggi@epitech.eu'
__version__ : str = "1.1"
__subversions__ : dict[str, str] = {
    "Action" : Action.__version__,
    "Config" : Config_parent.__version__,
    "Console" : Console.__version__,
    "Error" : Error.__version__,
    "Log" : Log_parent.__version__,
    "Time" : Time.__version__
}
__license__ : str = "GPL"
