#############################
###                       ###
###    Epitech Console    ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from jarbin_toolkit_action import Action, Actions
from jarbin_toolkit_time import Time, StopWatch
import jarbin_toolkit_error as Error
import jarbin_toolkit_config as Config
import jarbin_toolkit_log as Log


from console.jarbin_toolkit_console.System.console import Console
from console.jarbin_toolkit_console.System.setting import Setting


from sys import (
    stdin,
    stdout,
    stderr
)


__all__ : list[str] = [
    'Time',
    'StopWatch',
    'Config',
    'Console',
    'Log',
    'Action',
    'Actions',
    'Error',
    'Setting',
    'stdin',
    'stdout',
    'stderr',
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.amaraggi@epitech.eu'
