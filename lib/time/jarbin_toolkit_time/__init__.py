# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Time
# File         : __init__.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_time.time import Time
from jarbin_toolkit_time.stopwatch import StopWatch
from jarbin_toolkit_time.enums import (
    TimeFormat,
    StopWatchState,
)
from jarbin_toolkit_time.errors import (
    TimeTypeJError,
    TimeValueJError,
    TimeStateJError,
)


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.amaraggi@epitech.eu'
__version__ : str = "1.0.0.0"
__license__ : str = "GPL"


__all__ : list[str] = [
    'Time',
    'StopWatch',
    'TimeFormat',
    'StopWatchState',
    'TimeTypeJError',
    'TimeValueJError',
    'TimeStateJError',
]
