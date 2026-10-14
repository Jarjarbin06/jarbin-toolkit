# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : __init__.py
#
# Author       : Jarjarbin06
# ============================================================================


__author__ = 'Jarjarbin06'
__email__ = 'nathan.amaraggi@outlook.fr'
__version__ = "1.0.1.1"
__license__ = "GPL"
__github__ = "https://github.com/Jarjarbin06/jarbin-toolkit"


from jarbin_toolkit_error.base_error import BaseJError

from jarbin_toolkit_error.enums import FormatType

from jarbin_toolkit_error.exceptions import (
    JException,

    JErrorOS,
    JErrorRuntime,
    JErrorSystem,
    JErrorRecursion,
    JErrorNotImplemented,

    JErrorType,
    JErrorValue,
    JErrorIndex,
    JErrorName,
    JErrorAttribute,
    JErrorKey,

    JErrorArithmetic,
    JErrorFloatingPoint,
    JErrorOverflow,
    JErrorZeroDivision,

    JErrorImport,
    JErrorModuleNotFound,

    JErrorIO,
    JErrorFileNotFound,
    JErrorFileExists,
    JErrorPermission,
    JErrorIsADirectory,
    JErrorNotADirectory,
    JErrorDirectoryNotEmpty,

    JErrorAssertion,
    JErrorLookup,

    JErrorMemory,
    JErrorBuffer,
)

import jarbin_toolkit_error.enums as _Enums
from jarbin_toolkit_error.empty_field import (
    _EmptyField as _EmptyFieldClass,
    EmptyField as _EmptyField,
)
from jarbin_toolkit_error.error_link import ErrorLink as _ErrorLink


__all__ = [
    '__author__',
    '__email__',
    '__version__',
    '__license__',
    '__github__',

    'BaseJError',

    'FormatType',

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

    '_EmptyField',
    '_EmptyFieldClass',
    '_Enums',
    '_ErrorLink',
]
