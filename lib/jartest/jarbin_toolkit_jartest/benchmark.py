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

        self._time : list[Optional[float | int]] = []
        self._assertion : list[Optional[list[AssertionResult]]] = []
        self._error : list[Exception | None] = []
        self._traceback : list[Optional[list[Optional[TracebackType]]]] = []
        self._result : list[Optional[Any]] = []
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

        return self.time_to_str(self.time)


    @property
    def time(
            self
        ) -> Optional[float | int] :
        """
            Get latest time.
        """

        tmp_sum = 0.0
        for n in range(self.test_amount):
            tmp_sum += self._time[n]
        return tmp_sum / self._n


    @property
    def error(
            self
        ) -> Optional[Exception] :
        """
            Get latest error.
        """

        for n in range(self.test_amount):
            if self._error[n]:
                return self._error[n]
        return None


    @property
    def assertion(
            self
        ) -> Optional[list[AssertionResult]] :
        """
            Get latest error.
        """

        for n in range(self.test_amount):
            if self._assertion[n]:
                return self._assertion[n]
        return None


    @property
    def traceback(
            self
        ) -> Optional[list[Optional[TracebackType]]] :
        """
            Get latest error.
        """

        for n in range(self.test_amount):
            if self._traceback[n]:
                return self._traceback[n]
        return None


    @property
    def result(
            self
        ) -> Optional[Any] :
        """
            Get latest result.
        """

        for n in range(self.test_amount):
            if self._result[n]:
                return self._result[n]
        return None

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

        return self._test_name.split("/")[-1]

    @property
    def test_amount(
            self
        ) -> int :
        """
            Get number of times tested.
        """

        return self._n


    @property
    def tested(
            self
        ) -> bool :
        """
            Get tested.
        """

        return self.test_amount != 0


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
                f"test={self.name!r}, "
                f"tested={self.test_amount!r}"
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
            f"test={self.name!r}, "
            f"time={self.time_str}, "
            f"assertion={assertions}, "
            f"error={errors}, "
            f"result={self.result!r}, "
            f"tested={self.test_amount!r}"
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
