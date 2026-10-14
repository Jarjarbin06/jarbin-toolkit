__author__: str
__email__: str
__version__: str
__license__: str
__github__: str


from .log import Log

from .enums import (
    LogType,
    LogLevel,
)

from .errors import *

from .comment import LogComment as _LogComment
from .entry import LogEntry as _LogEntry
from .renderer import LogRenderer as _LogRenderer


__all__: list[str] = [
    '__author__',
    '__email__',
    '__version__',
    '__license__',
    '__github__',

    'Log',

    'LogType',
    'LogLevel',

    'LogTypeJError',
    'LogValueJError',
    'LogRuntimeJError',
    'LogStateJError',

    '_LogComment',
    '_LogEntry',
    '_LogRenderer',
]
