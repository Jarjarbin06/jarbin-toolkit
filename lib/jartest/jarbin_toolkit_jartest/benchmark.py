#############################
###                       ###
###     Jarbin-ToolKit    ###
###        JarTest        ###
### ----benchmark.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from types import TracebackType
from typing import Callable, Any, Optional
from jarbin_toolkit_jartest.assertion import AssertionResult


class Benchmark:
    """
        Benchmark class.

        Benchmark object launch a test-function.
    """

    def __init__(
            self,
            test : Callable[[], None]
        ) -> None :

        self._time : list[Optional[float | int]] = [None]
        self._assertion : list[Optional[list[AssertionResult]]] = [None]
        self._error : list[Exception | None] = [None]
        self._traceback : list[Optional[list[Optional[TracebackType]]]] = [None]
        self._result : list[Optional[Any]] = [None]
        self._test : Callable[[], None] = test
        self._test_name : str = test.__name__
        self._n : int = 0


    @property
    def time_str(
            self
        ) -> Optional[str] :
        """
            Get latest time.
        """

        return self.time_to_str(self._time[-1])


    @property
    def time(
            self
        ) -> Optional[float] :
        """
            Get latest time.
        """

        if self._time is None or self._time == 0.0:
            return None
        return self._time[-1] / self._n


    @property
    def error(
            self
        ) -> Optional[Exception] :
        """
            Get latest error.
        """

        return self._error[-1]


    @property
    def assertion(
            self
        ) -> Optional[list[AssertionResult]] :
        """
            Get latest error.
        """

        return self._assertion[-1]


    @property
    def traceback(
            self
        ) -> Optional[list[Optional[TracebackType]]] :
        """
            Get latest error.
        """

        return self._traceback[-1]


    @property
    def result(
            self
        ) -> Optional[int] :
        """
            Get latest result.
        """

        return self._result[-1]

    @property
    def test(
            self
        ) -> Callable[[], None] :
        """
            Get test function.
        """

        return self._test


    @property
    def name(
            self
        ) -> str :
        """
            Get test function.
        """

        return self._test_name


    @property
    def tested(
            self
        ) -> bool :
        """
            Get number of times tested.
        """

        return self._n != 0


    def __call__(
            self,
            n: int
        ) -> None:

        for _ in range(n):

            self._traceback.append([])

            result, time, assertion, error, assertions = self.benchmark(self.test)

            self._result.append(result)
            self._n += 1
            self._time.append(time)

            # store list of AssertionResult
            self._assertion.append(assertions)

            self._error.append(error)

            if error is not None:
                tb = error.__traceback__
                while tb is not None:
                    self._traceback[-1].append(tb)
                    tb = tb.tb_next
                break


    def __repr__(
            self
        ) -> str:

        if self._n == 0:
            return (
                f"Benchmark("
                f"test={self._test_name!r}, "
                f"tested={self._n!r}"
                f")"
            )

        assertions = [
            type(a).__name__ if a is not None else None
            for a in self._assertion
        ]

        errors = [
            type(e).__name__ if e is not None else None
            for e in self._error
        ]

        return (
            f"Benchmark("
            f"test={self._test_name!r}, "
            f"time={self.time_to_str(self.time)}, "
            f"assertion={assertions}, "
            f"error={errors}, "
            f"result={self._result!r}, "
            f"tested={self._n!r}"
            f")"
        )

    @staticmethod
    def benchmark(
            function: Callable
        ) -> tuple[Any | None, float, AssertionError | None, Exception | None, list[AssertionResult]]:

        from jarbin_toolkit_time import StopWatch
        from jarbin_toolkit_jartest.assertion import AssertionContext, _current_assertions

        result = None
        assertion = None
        exception = None
        assertions: list = []

        sw = StopWatch(True)

        try:
            with AssertionContext() as collected:
                result = function()
                assertions = collected

        except AssertionError as err:
            assertion = err
            assertions = _current_assertions.get() or []

        except Exception as err:
            exception = err
            assertions = _current_assertions.get() or []

        return result, sw.elapsed(), assertion, exception, assertions


    @staticmethod
    def time_to_str(
            seconds: Optional[float]
        ) -> str:
        """
            Convert a time in seconds to a string.
            Auto unit.
        """

        if seconds is None:
            return "No tests done"

        if seconds < 1e-6:
            return f"{seconds * 1e9:.3f}ns"

        elif seconds < 1e-3:
            return f"{seconds * 1e6:.3f}µs"

        elif seconds < 1:
            return f"{seconds * 1e3:.3f}ms"

        elif seconds < 60:
            return f"{seconds:.3f}s"

        else:
            minutes = int(seconds // 60)
            secs = seconds % 60
            return f"{minutes}m {secs:.3f}s"
