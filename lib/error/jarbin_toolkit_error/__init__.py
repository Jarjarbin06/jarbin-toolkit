#############################
###                       ###
###     Jarbin-ToolKit    ###
###         error         ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from jarbin_toolkit_error.error import (
    Error,
    ErrorType,
    ErrorValue,
    ErrorImport,
    ErrorLaunch,
    ErrorLog,
    ErrorSetting,
    ErrorConfig
)


__all__ : list[str] = [
    'Error',
    'ErrorType',
    'ErrorValue',
    'ErrorImport',
    'ErrorLaunch',
    'ErrorLog',
    'ErrorSetting',
    'ErrorConfig'
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.amaraggi@epitech.eu'
__version__ : str = "0.1.2.0"
__license__ : str = "GPL"
