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
from typing import Callable, Any
from jarbin_toolkit_error import ErrorAttribute


class Benchmark:
    """
        Benchmark class.

        Benchmark object launch a test-function.
    """

    def __init__(
            self,
            test : Callable[[], None]
        ) -> None :

        self._time : list[float | None] = [None]
        self._assertion : list[AssertionError | None] = [None]
        self._error : list[Exception | None] = [None]
        self._traceback : list[list[TracebackType | None]] = [None]
        self._result : list[Any | None] = [None]
        self._test : Callable[[], None] = test
        self._test_name : str = test.__name__
        self._n : int = 0


    @property
    def time_str(
            self
        ) -> str :
        """
            Get latest time.
        """

        return self.time_to_str(self._time[-1])


    @property
    def time(
            self
        ) -> float :
        """
            Get latest time.
        """

        if self._time is None or self._time == 0.0:
            return None
        return self._time[-1] / self._n


    @time.setter
    def time(
            self,
            new_value
        ) -> None :

        raise ErrorAttribute("time value is read-only")


    @property
    def error(
            self
        ) -> Exception | None :
        """
            Get latest error.
        """

        return self._error[-1]


    @error.setter
    def error(
            self,
            new_value
        ) -> None :

        raise ErrorAttribute("error value is read-only")


    @property
    def assertion(
            self
        ) -> AssertionError | None :
        """
            Get latest error.
        """

        return self._assertion[-1]


    @assertion.setter
    def assertion(
            self,
            new_value
        ) -> None :

        raise ErrorAttribute("assertion value is read-only")


    @property
    def traceback(
            self
        ) -> list[TracebackType | None] :
        """
            Get latest error.
        """

        return self._traceback[-1]


    @traceback.setter
    def traceback(
            self,
            new_value
        ) -> None :

        raise ErrorAttribute("traceback value is read-only")


    @property
    def result(
            self
        ) -> int | None :
        """
            Get latest result.
        """

        return self._result[-1]


    @result.setter
    def result(
            self,
            new_value
        ) -> None :

        raise ErrorAttribute("result value is read-only")


    @property
    def test(
            self
        ) -> Callable[[], None] :
        """
            Get test function.
        """

        return self._test


    @test.setter
    def test(
            self,
            new_value
        ) -> None :

        raise ErrorAttribute("test value is read-only")


    @property
    def name(
            self
        ) -> str :
        """
            Get test function.
        """

        return self._test_name


    @name.setter
    def name(
            self,
            new_value
        ) -> None :

        raise ErrorAttribute("test_name value is read-only")


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
            Get number of times tested.
        """

        return self._n != 0


    @tested.setter
    def tested(
            self,
            new_value
        ) -> None :

        raise ErrorAttribute("tested value is read-only")


    def __call__(
            self,
            n : int
        ) -> None :

        for _ in range(n):
            self._traceback.append([])
            result, time, assertion, error = self.benchmark(self.test)

            self._result.append(result)
            self._n += 1
            self._time.append(time)
            self._assertion.append(assertion)
            self._error.append(error)

            if self._error[-1] is not None:
                tb = self._error[-1].__traceback__
                while tb is not None:
                    self._traceback[-1].append(tb)
                    tb = tb.tb_next


    def __repr__(
            self
        ) -> str:

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
            f"test={self._test_name}, "
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
        ) -> tuple[Any | None, float, AssertionError | None, Exception | None]:
        """
        Benchmark the function

        Parameters:
            function (Callable): function to benchmark

        Returns:
            tuple[Any | None, float, AssertionError | None, Exception | None]: benchmark result, elapsed time, assertion and exception
        """

        from jarbin_toolkit_time import StopWatch

        result = None
        assertion = None
        exception = None
        sw = StopWatch(True)

        try:
            result = function()

        except AssertionError as err:
            assertion = err

        except Exception as err:
            exception = err

        return result, sw.elapsed(), assertion, exception


    @staticmethod
    def time_to_str(seconds: float) -> str:
        """
            Convert a time in seconds to a string.
            Auto unit.
        """
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
