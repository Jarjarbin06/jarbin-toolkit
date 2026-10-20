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
__version__ = "1.0.0.2"
__license__ = "GPL"
__github__ = "https://github.com/Jarjarbin06/jarbin-toolkit"


from jarbin_toolkit_config.config import Config
from jarbin_toolkit_config.errors import (
    ConfigFileNotFoundJError,
    ConfigRuntimeJError,
    ConfigTypeJError,
    ConfigValueJError,
)

__all__ = [
    'Config',
    'ConfigFileNotFoundJError',
    'ConfigRuntimeJError',
    'ConfigTypeJError',
    'ConfigValueJError',
    '__author__',
    '__email__',
    '__github__',
    '__license__',
    '__version__',
]
