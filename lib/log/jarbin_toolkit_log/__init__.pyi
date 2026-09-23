__author__: str
__email__: str
__version__: str
__license__: str


from .log import Log

from .enums import (
    LogType,
    LogLevel,
)

from .errors import *

from .comment import LogComment as _LogComment
from .entry import LogEntry as _LogEntry
from .renderer import LogRenderer as _LogRenderer


__all__: list[str]
