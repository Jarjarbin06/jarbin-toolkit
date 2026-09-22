from .base_error import BaseJError
from .enums import FormatType

from .exceptions.exception import (
    JException,
)

from .exceptions.general import (
    JErrorRuntime,
    JErrorSystem,
    JErrorRecursion,
    JErrorNotImplemented,
)

from .exceptions.value import (
    JErrorType,
    JErrorValue,
    JErrorIndex,
    JErrorName,
    JErrorAttribute,
    JErrorKey,
)

from .exceptions.arithmetic import (
    JErrorArithmetic,
    JErrorFloatingPoint,
    JErrorOverflow,
    JErrorZeroDivision,
)

from .exceptions.module import (
    JErrorImport,
    JErrorModuleNotFound,
)

from . import enums as _Enums
from .empty_field import (
    _EmptyField as _EmptyFieldClass,
    EmptyField as _EmptyField,
)
from .error_link import ErrorLink as _ErrorLink


__author__: str
__email__: str
__version__: str
__license__: str


__all__: list[str]
