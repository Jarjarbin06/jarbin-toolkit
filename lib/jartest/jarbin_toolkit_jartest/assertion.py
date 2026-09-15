#############################
###                       ###
###     Jarbin-ToolKit    ###
###        JarTest        ###
### ----assertion.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


import contextvars
from typing import Any
import inspect
from pathlib import Path

from jarbin_toolkit_error import Error

from jarbin_toolkit_jartest.show import Show


_current_assertions = contextvars.ContextVar("current_assertions", default=None)


class AssertionResult:
    """
    Stores the result of a single assertion evaluation.
    """

    def __init__(
            self,
            *,
            name: str,
            passed: bool,
            values: tuple = (),
            expected: object = None,
            actual: object = None,
            error_message: list[tuple[str, Any]] | None = None,
            message: str | None = None,
            exception: Exception | None = None,
            meta: dict | None = None
        ) -> None:

        self.name: str = name
        self.passed: bool = passed

        self.values: tuple = values
        self.expected: object = expected
        self.actual: object = actual

        if not passed and message is None:
            message = name.upper()

        self.message: str | None = message
        self.error_message: list[tuple[str, Any]] = error_message or []

        self.exception: Exception | None = exception

        self.meta: dict | None = meta or {}

        self.location: tuple[str, int] | None = AssertionResult._get_caller_location()

        if not self.passed:
            Show.Assertion(self)


    @staticmethod
    def _get_caller_location(
        ) -> tuple[str, int] | None:

        current_file = Path(__file__).resolve()

        frame = inspect.currentframe()

        if frame is None:
            return None

        frame = frame.f_back

        while frame is not None:

            try:
                filename = Path(
                    inspect.getfile(frame)
                ).resolve()
            except (TypeError, OSError):
                frame = frame.f_back
                continue

            if filename != current_file:
                return (
                    str(filename),
                    frame.f_lineno
                )

            frame = frame.f_back

        return None


    def __repr__(
            self
        ) -> str:
        status = "PASS" if self.passed else "FAIL"
        return f"AssertionResult({self.name=!r}, {status=!r}, {self.expected=!r}, {self.actual=!r}, {self.values=!r}, {self.message=!r})"


class AssertionContext:


    def __enter__(
            self
        ) -> list:
        self._list = []
        self._token = _current_assertions.set(self._list)
        return self._list


    def __exit__(
            self,
            exc_type,
            exc,
            tb
        ) -> None:
        _current_assertions.reset(self._token)


class MetaAssertion(type):


    def __call__(
            cls,
            condition: Any,
            message: str | None = None
        ) -> AssertionResult:

        passed = bool(condition)

        result = AssertionResult(
            name="assertion",
            passed=passed,
            values=(condition,),
            expected=None,
            actual=condition,
            message=message,
            error_message=[
                ("text", "Expected the condition to be true"),
            ],
            meta={
                "operator": "truthy",
                "types": (type(condition).__name__,)
            }
        )

        Assertion._register(result)
        return result


class Assertion(metaclass=MetaAssertion):


    @staticmethod
    def _register(
            result
        ) -> None:
        lst = _current_assertions.get()
        if lst is not None:
            lst.append(result)


    @staticmethod
    def eq(
            a: object,
            b: object,
            message: str | None = None
        ) -> AssertionResult:

        if type(a) != type(b):
            raise Error.ErrorType("types mismatches (type(a) != type(b))")

        passed = (a == b)

        result = AssertionResult(
            name="eq",
            passed=passed,
            values=(a, b),
            expected=b,
            actual=a,
            message=message,
            error_message=[
                ("text", "Expected "),
                ("actual", a),
                ("text", " to be equal to "),
                ("expected", b),
            ],
            meta={
                "operator": "==",
                "types": (type(a).__name__, type(b).__name__)
            }
        )

        Assertion._register(result)
        return result


    @staticmethod
    def neq(
            a: object,
            b: object,
            message: str | None = None
        ) -> AssertionResult:

        if type(a) != type(b):
            raise Error.ErrorType("types mismatches (type(a) != type(b))")

        passed = (a != b)

        result = AssertionResult(
            name="neq",
            passed=passed,
            values=(a, b),
            expected=b,
            actual=a,
            message=message,
            error_message=[
                ("text", "Expected "),
                ("actual", a),
                ("text", " not to be equal to "),
                ("expected", b),
            ],
            meta={
                "operator": "!=",
                "types": (type(a).__name__, type(b).__name__)
            }
        )

        Assertion._register(result)
        return result


    @staticmethod
    def contain(
            a: object,
            b: object,
            message: str | None = None
        ) -> AssertionResult:

        passed = (b in a)

        result = AssertionResult(
            name="contain",
            passed=passed,
            values=(a, b),
            expected=a,
            actual=b,
            message=message,
            error_message=[
                ("text", "Expected "),
                ("actual", a),
                ("text", " to contain "),
                ("expected", b),
            ],
            meta={
                "operator": "contain",
                "types": (type(a).__name__, type(b).__name__)
            }
        )

        Assertion._register(result)
        return result


    @staticmethod
    def ncontain(
            a: object,
            b: object,
            message: str | None = None
        ) -> AssertionResult:

        passed = (b not in a)

        result = AssertionResult(
            name="ncontain",
            passed=passed,
            values=(a, b),
            expected=a,
            actual=b,
            message=message,
            error_message=[
                ("text", "Expected "),
                ("actual", a),
                ("text", " not to contain "),
                ("expected", b),
            ],
            meta={
                "operator": "not contain",
                "types": (type(a).__name__, type(b).__name__)
            }
        )

        Assertion._register(result)
        return result
