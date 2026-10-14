# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error/Exceptions
# File         : __init__.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.exceptions.exceptions import (
    JException,
)

from jarbin_toolkit_error.exceptions.generals import (
    JErrorOS,
    JErrorRuntime,
    JErrorSystem,
    JErrorRecursion,
    JErrorNotImplemented,
)

from jarbin_toolkit_error.exceptions.values import (
    JErrorType,
    JErrorValue,
    JErrorIndex,
    JErrorName,
    JErrorAttribute,
    JErrorKey,
)

from jarbin_toolkit_error.exceptions.arithmetics import (
    JErrorArithmetic,
    JErrorFloatingPoint,
    JErrorOverflow,
    JErrorZeroDivision,
)

from jarbin_toolkit_error.exceptions.modules import (
    JErrorImport,
    JErrorModuleNotFound,
)

from jarbin_toolkit_error.exceptions.file import (
    JErrorIO,
    JErrorFileNotFound,
    JErrorFileExists,
    JErrorPermission,
    JErrorIsADirectory,
    JErrorNotADirectory,
    JErrorDirectoryNotEmpty,
)

from jarbin_toolkit_error.exceptions.assertion import (
    JErrorAssertion,
    JErrorLookup,
)

from jarbin_toolkit_error.exceptions.memory import (
    JErrorMemory,
    JErrorBuffer,
)


__all__ = [
    'JException',

    'JErrorOS',
    'JErrorRuntime',
    'JErrorSystem',
    'JErrorRecursion',
    'JErrorNotImplemented',

    'JErrorType',
    'JErrorValue',
    'JErrorIndex',
    'JErrorName',
    'JErrorAttribute',
    'JErrorKey',

    'JErrorArithmetic',
    'JErrorFloatingPoint',
    'JErrorOverflow',
    'JErrorZeroDivision',

    'JErrorImport',
    'JErrorModuleNotFound',

    'JErrorIO',
    'JErrorFileNotFound',
    'JErrorFileExists',
    'JErrorPermission',
    'JErrorIsADirectory',
    'JErrorNotADirectory',
    'JErrorDirectoryNotEmpty',

    'JErrorAssertion',
    'JErrorLookup',

    'JErrorMemory',
    'JErrorBuffer',
]
