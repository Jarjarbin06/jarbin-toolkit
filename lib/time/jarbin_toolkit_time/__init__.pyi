__author__: str
__email__: str
__version__: str
__license__: str
__github__: str


from .enums import (
    StopWatchState,
    TimeFormat,
)
from .errors import (
    TimeStateJError,
    TimeTypeJError,
    TimeValueJError,
)
from .stopwatch import StopWatch
from .time import Time

__all__: list[str] = [
    'StopWatch',
    'StopWatchState',
    'Time',
    'TimeFormat',
    'TimeStateJError',
    'TimeTypeJError',
    'TimeValueJError',
    '__author__',
    '__email__',
    '__github__',
    '__license__',
    '__version__',
]
