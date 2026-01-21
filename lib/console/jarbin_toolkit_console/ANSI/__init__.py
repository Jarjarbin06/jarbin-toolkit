#############################
###                       ###
###    Epitech Console    ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from lib.console.jarbin_toolkit_console.ANSI.ansi import ANSI
from lib.console.jarbin_toolkit_console.ANSI.cursor import Cursor
from lib.console.jarbin_toolkit_console.ANSI.line import Line
from lib.console.jarbin_toolkit_console.ANSI.color import Color
from lib.console.jarbin_toolkit_console.ANSI.basepack import BasePack


__all__ : list[str] = [
    'ANSI',
    'Cursor',
    'Line',
    'Color',
    'BasePack'
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.amaraggi@epitech.eu'
