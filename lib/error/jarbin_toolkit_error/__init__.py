# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : __init__.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.base_error import BaseJError
from jarbin_toolkit_error.enums import FormatType

from jarbin_toolkit_error.exceptions.exception import (
    JException,
)

from jarbin_toolkit_error.exceptions.general import (
    JErrorRuntime,
    JErrorSystem,
    JErrorRecursion,
    JErrorNotImplemented,
)

from jarbin_toolkit_error.exceptions.value import (
    JErrorType,
    JErrorValue,
    JErrorIndexError,
    JErrorName,
    JErrorAttribute,
    JErrorKey,
)

from jarbin_toolkit_error.exceptions.logic import (
    JErrorArithmetic,
    JErrorFloatingPoint,
    JErrorOverflow,
    JErrorZeroDivision,
)

from jarbin_toolkit_error.exceptions.module import (
    JErrorImport,
    JErrorModuleNotFound,
)

import jarbin_toolkit_error.enums as _Enums
from jarbin_toolkit_error.empty_field import (
    _EmptyField as _EmptyFieldClass,
    EmptyField as _EmptyField,
)
from jarbin_toolkit_error.error_link import ErrorLink as _ErrorLink


__author__ = 'Jarjarbin06'
__email__ = 'nathan.amaraggi@outlook.fr'
__version__ = "1.0.0.0"
__license__ = "GPL"


__all__ = [
    '__author__',
    '__email__',
    '__version__',
    '__license__',
    'BaseJError',
    'FormatType',

    'JException',
    'JErrorRuntime',
    'JErrorSystem',
    'JErrorRecursion',
    'JErrorNotImplemented',

    'JErrorType',
    'JErrorValue',
    'JErrorIndexError',
    'JErrorName',
    'JErrorAttribute',
    'JErrorKey',

    'JErrorArithmetic',
    'JErrorFloatingPoint',
    'JErrorOverflow',
    'JErrorZeroDivision',

    'JErrorImport',
    'JErrorModuleNotFound',

    '_EmptyField',
    '_Enums',
    '_ErrorLink',
]
