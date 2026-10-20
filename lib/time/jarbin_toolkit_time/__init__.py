# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Time
# File         : __init__.py
#
# Author       : Jarjarbin06
# ============================================================================


__author__ = 'Nathan Jarjarbin'
__email__ = 'nathan.amaraggi@epitech.eu'
__version__ = "1.0.0.2"
__license__ = "GPL"
__github__ = "https://github.com/Jarjarbin06/jarbin-toolkit"


from jarbin_toolkit_time.enums import (
    StopWatchState,
    TimeFormat,
)
from jarbin_toolkit_time.errors import (
    TimeStateJError,
    TimeTypeJError,
    TimeValueJError,
)
from jarbin_toolkit_time.stopwatch import StopWatch
from jarbin_toolkit_time.time import Time

__all__ = [
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
