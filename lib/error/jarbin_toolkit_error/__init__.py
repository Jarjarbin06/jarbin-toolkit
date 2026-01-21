#############################
###                       ###
###    Epitech Console    ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from jarbin_toolkit_error.Error.error import (
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
