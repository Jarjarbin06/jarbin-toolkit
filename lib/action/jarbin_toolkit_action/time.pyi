from typing import final

from jarbin_toolkit_time import StopWatch


@final
class ActionTimer(StopWatch):
    """
        Timer for action duration measurement
        (StopWatch)
    """


    def elapsed(
            self,
        ) -> float:
        """
            Get the elapsed time

            Return
            ----------
            float
                Elapsed time
        """
        ...


__all__: list[str]
