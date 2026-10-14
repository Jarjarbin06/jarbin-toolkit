__author__: str
__email__: str
__version__: str
__license__: str
__github__: str


from .base_error import BaseJError
from .enums import FormatType
from .exceptions import (
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
from . import enums as _Enums
from .empty_field import (
    _EmptyField as _EmptyFieldClass,
    EmptyField as _EmptyField,
)
from .error_link import ErrorLink as _ErrorLink


__all__: list[str] = [
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
