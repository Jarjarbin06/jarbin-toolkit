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
__version__ = "1.0.0.0"
__license__ = "GPL"


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


__all__ : list[str] = [
    '__author__',
    '__email__',
    '__version__',
    '__license__',

    'Time',
    'StopWatch',

    'TimeFormat',
    'StopWatchState',

    'TimeTypeJError',
    'TimeValueJError',
    'TimeStateJError',
]
