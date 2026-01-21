#############################
###                       ###
###    Epitech Console    ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from console.jarbin_toolkit_console.Animation.animation import Animation
from console.jarbin_toolkit_console.Animation.basepack import BasePack
from console.jarbin_toolkit_console.Animation.progressbar import ProgressBar
from console.jarbin_toolkit_console.Animation.style import Style
from console.jarbin_toolkit_console.Animation.spinner import Spinner


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
