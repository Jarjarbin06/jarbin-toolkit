# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Log
# File         : __init__.py
#
# Author       : Jarjarbin06
# ============================================================================


__author__ = 'Nathan Jarjarbin'
__email__ = 'nathan.amaraggi@epitech.eu'
__version__ = "1.0.0.0"
__license__ = "GPL"


from jarbin_toolkit_log.log import Log

from jarbin_toolkit_log.enums import (
    LogType,
    LogLevel,
)

from jarbin_toolkit_log.errors import *

from jarbin_toolkit_log.comment import LogComment as _LogComment
from jarbin_toolkit_log.entry import LogEntry as _LogEntry
from jarbin_toolkit_log.renderer import LogRenderer as _LogRenderer


__all__ = [
    '__author__',
    '__email__',
    '__version__',
    '__license__',

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
