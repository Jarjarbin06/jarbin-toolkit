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
__github__ = "https://github.com/Jarjarbin06/jarbin-toolkit"


from jarbin_toolkit_config.config import Config

from jarbin_toolkit_config.errors import (
    ConfigRuntimeJError,
    ConfigTypeJError,
    ConfigValueJError,
    ConfigFileNotFoundJError,
)


__all__ = [
    '__author__',
    '__email__',
    '__version__',
    '__license__',
    '__github__',

    'Config',

    'ConfigRuntimeJError',
    'ConfigTypeJError',
    'ConfigValueJError',
    'ConfigFileNotFoundJError',
]
