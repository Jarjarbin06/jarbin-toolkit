#############################
###                       ###
###     Jarbin-ToolKit    ###
###         time          ###
###    ----time.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


class Time:
    """
        Time class.

        Time tool.
    """

    @staticmethod
    def wait(
            sleep : int | float
        ) -> float:
        """
            Wait for 'sleep' seconds and return the exact elapsed time during the wait function.

            Parameters:
                sleep (int | float) : Time to wait

            Returns:
                float : Exact elapsed time
        """

        from jarbin_toolkit_time.stopwatch import StopWatch

        watch = StopWatch(True)

        while watch.elapsed() < sleep:
            watch.update()

        return watch.elapsed()


    @staticmethod
    def pause(
            msg : str = "Press enter to continue..."
        ) -> float:
        """
            Pause the program and print a message and return the exact elapsed time during the pause function.

            Parameters:
                msg (str, optional) : Message to be displayed

            Returns:
                float : Exact elapsed time
        """

        ## cannot be tested with pytest ##

        from jarbin_toolkit_time.stopwatch import StopWatch # pragma: no cover

        watch = StopWatch(True) # pragma: no cover
        input(msg) # pragma: no cover

        return watch.elapsed(True) # pragma: no cover
