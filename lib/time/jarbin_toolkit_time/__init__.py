#############################
###                       ###
###     Jarbin-ToolKit    ###
###         time          ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from jarbin_toolkit_time.time import Time
from jarbin_toolkit_time.stopwatch import StopWatch


def get_timestamp(
    ) -> float:
    """
        Get the current timestamp

        Returns:
            float : timestamp
    """

    from time import monotonic

    return monotonic()


__all__ : list[str] = [
    'get_timestamp',
    'Time',
    'StopWatch'
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.amaraggi@epitech.eu'
__version__ : str = "0.1.2.2"
__license__ : str = "GPL"
