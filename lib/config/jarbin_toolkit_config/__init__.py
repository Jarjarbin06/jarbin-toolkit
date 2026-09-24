# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Config
# File         : __init__.py
#
# Author       : Jarjarbin06
# ============================================================================


__author__ = 'Nathan Jarjarbin'
__email__ = 'nathan.amaraggi@epitech.eu'
__version__ = "1.0.0.0"
__license__ = "GPL"


from jarbin_toolkit_config.config import Config

from jarbin_toolkit_config.errors import (
    ConfigRuntimeJError,
    ConfigTypeJError,
    ConfigValueJError,
    ConfigFileNotFoundJError,
)


__all__ : list[str] = [
    '__author__',
    '__email__',
    '__version__',
    '__license__',
    'Config',
    'ConfigRuntimeJError',
    'ConfigTypeJError',
    'ConfigValueJError',
    'ConfigFileNotFoundJError',
]
