__author__: str
__email__: str
__version__: str
__license__: str
__github__: str


from .config import Config

from .errors import (
    ConfigRuntimeJError,
    ConfigTypeJError,
    ConfigValueJError,
    ConfigFileNotFoundJError,
)


__all__: list[str] = [
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
