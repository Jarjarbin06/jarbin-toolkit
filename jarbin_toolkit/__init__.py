#############################
###                       ###
###     Jarbin-ToolKit    ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from collections.abc import Callable
from typing import Any, TextIO, Optional
import sys
import os
import platform


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
        f"\033[103m \033[0m \033[93mjarbin_toolkit launched with fatal error\033[0m\n"
        "\033[103m \033[0m\n"
        "\033[103m \033[0m \033[93mPlease reinstall with :\033[0m\n"
        "\033[103m \033[0m \033[93m    'pip install --upgrade --force-reinstall jarbin_toolkit'\033[0m\n"
        "\033[103m \033[0m\n"
        "\033[103m \033[0m \033[93mPlease report the issue here : https://github.com/Jarjarbin06/jarbin-toolkit/issues\033[0m\n"
    )  # pragma: no cover
    exit(84)  # pragma: no cover


try:
    import jarbin_toolkit_action as Action
    import jarbin_toolkit_config as Config_parent
    import jarbin_toolkit_console as Console
    import jarbin_toolkit_error as Error
    import jarbin_toolkit_log as Log_parent
    import jarbin_toolkit_time as Time
    import jarbin_toolkit_jartest as JarTest


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
        ) -> dict[str, Any]:
        """
            Get info about the Jarbin toolkit

            Returns:
                dict[str, str | dict[str, Any]]: info
        """

        return {
            "name": "Jarbin-ToolKit",
            "version": __version__,
            "subversions": __subversions__,
            "author": __author__,
            "email": __email__,
            "license": __license__
        }


    def benchmark(
            function: Callable,
            *args: Any,
            **kwargs: Any
        ) -> tuple[Optional[Any], float, Optional[Exception]]:
        """
        Benchmark the function

        Parameters:
            function (Callable): function to benchmark
            *args (list[Any]): arguments
            **kwargs (dict[str, Any]): keyword arguments

        Returns:
            tuple[Optional[Any], float, Optional[Exception]]: benchmark result, elapsed time and exception
        """
        result = None
        exception = None
        sw = Time.StopWatch(True)
        try:
            result = function(*args, **kwargs)
        except Exception as err:
            exception = err
        return result, sw.elapsed(), exception


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
    print : Callable[[Any, str, str, str, Any, bool, bool, int | float | None], Any] = Console.Console.print
    input : Callable[[str, str, type], Any] = Console.Console.input
    flush : Callable[[TextIO], None] = Console.Console.flush
    stdin : TextIO = Console.Console.stdin
    stdout : TextIO = Console.Console.stdout
    stderr : TextIO = Console.Console.stderr
    critic : Callable[[Any], Any] = Console.Text.Format.critic
    error : Callable[[Any], Any] = Console.Text.Format.error
    warning : Callable[[Any], Any] = Console.Text.Format.warning
    valid : Callable[[Any], Any] = Console.Text.Format.valid
    debug : Callable[[Any], Any] = Console.Text.Format.debug
    info : Callable[[Any], Any] = Console.Text.Format.info
    bold : Callable[[Any], Any] = Console.Text.Format.bold
    underline : Callable[[Any], Any] = Console.Text.Format.underline
    color : Callable[[str | int | Any], Console.ANSI.ANSI] = Console.ANSI.Color.color
    up : Callable[[int], Console.ANSI.ANSI] = Console.ANSI.Cursor.up
    down : Callable[[int], Console.ANSI.ANSI] = Console.ANSI.Cursor.down
    left : Callable[[int], Console.ANSI.ANSI] = Console.ANSI.Cursor.left
    right : Callable[[int], Console.ANSI.ANSI] = Console.ANSI.Cursor.right
    clear : Callable[[], Console.ANSI.ANSI] = Console.ANSI.Line.clear
    clear_line : Callable[[], Console.ANSI.ANSI] = Console.ANSI.Line.clear_line


## cannot be tested with pytest ##

except Exception as error:  # pragma: no cover
    _fatal_error(error)  # pragma: no cover


__all__ : list[str] = [
    'Action',
    'Config',
    'Console',
    'Error',
    'JarTest',
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
    "JarTest" : JarTest.__version__,
    "Log" : Log_parent.__version__,
    "Time" : Time.__version__
}
__license__ : str = "GPL"
