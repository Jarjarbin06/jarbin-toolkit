# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error/Exceptions
# File         : __init__.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.exceptions.arithmetics import (
    JErrorArithmetic,
    JErrorFloatingPoint,
    JErrorOverflow,
    JErrorZeroDivision,
)
from jarbin_toolkit_error.exceptions.assertion import (
    JErrorAssertion,
    JErrorLookup,
)
from jarbin_toolkit_error.exceptions.exceptions import (
    JException,
)
from jarbin_toolkit_error.exceptions.file import (
    JErrorDirectoryNotEmpty,
    JErrorFileExists,
    JErrorFileNotFound,
    JErrorIO,
    JErrorIsADirectory,
    JErrorNotADirectory,
    JErrorPermission,
)
from jarbin_toolkit_error.exceptions.generals import (
    JErrorNotImplemented,
    JErrorOS,
    JErrorRecursion,
    JErrorRuntime,
    JErrorSystem,
)
from jarbin_toolkit_error.exceptions.memory import (
    JErrorBuffer,
    JErrorMemory,
)
from jarbin_toolkit_error.exceptions.modules import (
    JErrorImport,
    JErrorModuleNotFound,
)
from jarbin_toolkit_error.exceptions.values import (
    JErrorAttribute,
    JErrorIndex,
    JErrorKey,
    JErrorName,
    JErrorType,
    JErrorValue,
)

__all__ = [
    'JErrorArithmetic',
    'JErrorAssertion',
    'JErrorAttribute',
    'JErrorBuffer',
    'JErrorDirectoryNotEmpty',
    'JErrorFileExists',
    'JErrorFileNotFound',
    'JErrorFloatingPoint',
    'JErrorIO',
    'JErrorImport',
    'JErrorIndex',
    'JErrorIsADirectory',
    'JErrorKey',
    'JErrorLookup',
    'JErrorMemory',
    'JErrorModuleNotFound',
    'JErrorName',
    'JErrorNotADirectory',
    'JErrorNotImplemented',
    'JErrorOS',
    'JErrorOverflow',
    'JErrorPermission',
    'JErrorRecursion',
    'JErrorRuntime',
    'JErrorSystem',
    'JErrorType',
    'JErrorValue',
    'JErrorZeroDivision',
    'JException',
]
