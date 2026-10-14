__author__: str
__email__: str
__version__: str
__license__: str
__github__: str


from .time import Time
from .stopwatch import StopWatch
from .enums import (
    TimeFormat,
    StopWatchState,
)
from .errors import (
    TimeTypeJError,
    TimeValueJError,
    TimeStateJError,
)


__all__: list[str] = [
    '__author__',
    '__email__',
    '__version__',
    '__license__',
    '__github__',

    'Time',
    'StopWatch',

    'TimeFormat',
    'StopWatchState',

    'TimeTypeJError',
    'TimeValueJError',
    'TimeStateJError',
]
