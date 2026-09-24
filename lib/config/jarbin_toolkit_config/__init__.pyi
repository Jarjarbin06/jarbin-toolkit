__author__: str
__email__: str
__version__: str
__license__: str


from .config import Config

from .errors import (
    ConfigRuntimeJError,
    ConfigTypeJError,
    ConfigValueJError,
    ConfigFileNotFoundJError,
)


__all__: list[str]
