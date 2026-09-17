# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : __init__.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.base_error import BaseError
from jarbin_toolkit_error.enums import FormatType

import jarbin_toolkit_error.enums as _Enums
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
    'BaseError',
    'FormatType',
    '_Enums',
    '_ErrorLink',
]
