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
__version__ = "1.0.1.2"
__license__ = "GPL"
__github__ = "https://github.com/Jarjarbin06/jarbin-toolkit"


import jarbin_toolkit_error.enums as _Enums
from jarbin_toolkit_error.base_error import BaseJError
from jarbin_toolkit_error.empty_field import (
    EmptyField as _EmptyField,
)
from jarbin_toolkit_error.empty_field import (
    _EmptyField as _EmptyFieldClass,
)
from jarbin_toolkit_error.enums import FormatType
from jarbin_toolkit_error.error_link import ErrorLink as _ErrorLink
from jarbin_toolkit_error.exceptions import (
    JErrorArithmetic,
    JErrorAssertion,
    JErrorAttribute,
    JErrorBuffer,
    JErrorDirectoryNotEmpty,
    JErrorFileExists,
    JErrorFileNotFound,
    JErrorFloatingPoint,
    JErrorImport,
    JErrorIndex,
    JErrorIO,
    JErrorIsADirectory,
    JErrorKey,
    JErrorLookup,
    JErrorMemory,
    JErrorModuleNotFound,
    JErrorName,
    JErrorNotADirectory,
    JErrorNotImplemented,
    JErrorOS,
    JErrorOverflow,
    JErrorPermission,
    JErrorRecursion,
    JErrorRuntime,
    JErrorSystem,
    JErrorType,
    JErrorValue,
    JErrorZeroDivision,
    JException,
)

__all__ = [
    'BaseJError',
    'FormatType',
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
    '_EmptyField',
    '_EmptyFieldClass',
    '_Enums',
    '_ErrorLink',
    '__author__',
    '__email__',
    '__github__',
    '__license__',
    '__version__',
]
