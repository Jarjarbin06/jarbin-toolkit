#############################
###                       ###
###     Jarbin-ToolKit    ###
###        console        ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from jarbin_toolkit_console.Animation.animation import Animation
from jarbin_toolkit_console.Animation.basepack import BasePack
from jarbin_toolkit_console.Animation.progressbar import ProgressBar
from jarbin_toolkit_console.Animation.style import Style
from jarbin_toolkit_console.Animation.spinner import Spinner


__all__ : list[str] = [
    'Animation',
    'BasePack',
    'ProgressBar',
    'Style',
    'Spinner'
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.amaraggi@epitech.eu'


BasePack.update()
