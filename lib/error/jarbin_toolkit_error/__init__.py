#############################
###                       ###
###     Jarbin-ToolKit    ###
###         error         ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from jarbin_toolkit_error.base_error import BaseError
import jarbin_toolkit_error.error as Error
import jarbin_toolkit_error.file as File
import jarbin_toolkit_error.logic as Logic
import jarbin_toolkit_error.network as Network
import jarbin_toolkit_error.special as Special
import jarbin_toolkit_error.state as State
import jarbin_toolkit_error.system as System


__all__ : list[str] = [
    "BaseError",
    "Error",
    "File",
    "Logic",
    "Network",
    "Special",
    "State",
    "System"
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.amaraggi@epitech.eu'
__version__ : str = "0.1.6.1"
__license__ : str = "GPL"
