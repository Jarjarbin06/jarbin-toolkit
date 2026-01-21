#############################
###                       ###
###     Jarbin-ToolKit    ###
###         time          ###
###  ----wtopwatch.py---- ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


class StopWatch:
    """
        StopWatch class.

        StopWatch tool.
    """


    def __init__(
            self,
            start : bool = False,
        ) -> None:
        """
            Create a stopwatch.

            Parameters:
                start (bool, optional) : If True, start the stopwatch at creation time.
        """

        self._start : float = 0.0
        self._elapsed : float = 0.0

        if start:
            self.start()


    def __str__(
            self
        ) -> str :
        """
            Convert StopWatch object to string.

            Returns:
                str: StopWatch string
        """

        return str(self.elapsed())


    def __eq__(
            self,
            other : float
        ) -> bool:
        """
            Compare elapsed time with float.

            Parameters:
                other (float) : time

            Returns:
                bool: True if equal to other, False otherwise
        """

        return self._elapsed == other


    def __gt__(
            self,
            other : float
        ) -> bool:
        """
            Compare elapsed time with float.

            Parameters:
                other (float) : time

            Returns:
                bool: True if greater than other, False otherwise
        """

        return self._elapsed > other


    def __ge__(
            self,
            other : float
        ) -> bool:
        """
            Compare elapsed time with float.

            Parameters:
                other (float) : time

            Returns:
                bool: True if greater or equal to other, False otherwise
        """

        ## cannot be tested with pytest ##

        return self > other or self == other # pragma: no cover


    def __lt__(
            self,
            other : float
        ) -> bool:
        """
            Compare elapsed time with float.

            Parameters:
                other (float) : time

            Returns:
                bool: True if less than other, False otherwise
        """

        return self._elapsed < other


    def __le__(
            self,
            other : float
        ) -> bool:
        """
            Compare elapsed time with float.

            Parameters:
                other (float) : time

            Returns:
                bool: True if greater or equal to other, False otherwise
        """

        ## cannot be tested with pytest ##

        return self < other or self == other # pragma: no cover


    def start(
            self
        ) -> None:
        """
            Start the stopwatch.
        """

        from time import time

        self.reset()
        self._start = time()


    def stop(
            self
        ) -> None:

        self.update()
        self._start = 0.0


    def update(
            self
        ) -> None:
        """
            Update the stopwatch.
        """

        from time import time

        if self._start:
            self._elapsed = time() - self._start


    def elapsed(
            self,
            auto_update : bool = True
        ) -> float:
        """
            Get elapsed time.

            Parameters:
                auto_update (bool, optional): Auto update. Defaults to True.

            Returns:
                float: Elapsed time.
        """

        if auto_update:
            self.update()

        return self._elapsed


    def reset(
            self
        ) -> None:
        """
            Reset the stopwatch.
        """

        self._start = 0.0
        self._elapsed = 0.0


    def __repr__(
            self
        ) -> str:
        """
            Convert StopWatch object to string.

            Returns:
                str: StopWatch string
        """

        return f"StopWatch(?)"
