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

from jarbin_toolkit_error import Error

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

        self.exception: Exception | None = exception

        self.meta: dict | None = meta or {}

    def __repr__(self) -> str:
        status = "PASS" if self.passed else "FAIL"
        return f"AssertionResult({self.name=!r}, {status=!r}, {self.expected=!r}, {self.actual=!r}, {self.values=!r}, {self.message=!r})"


class AssertionContext:

    def __enter__(self):
        self._list = []
        self._token = _current_assertions.set(self._list)
        return self._list

    def __exit__(self, exc_type, exc, tb):
        _current_assertions.reset(self._token)


class Assertion:

    @staticmethod
    def _register(result):
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

        passed = (a in b)

        result = AssertionResult(
            name="contain",
            passed=passed,
            values=(a, b),
            expected=b,
            actual=a,
            message=message,
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

        passed = (a not in b)

        result = AssertionResult(
            name="ncontain",
            passed=passed,
            values=(a, b),
            expected=b,
            actual=a,
            message=message,
            meta={
                "operator": "not contain",
                "types": (type(a).__name__, type(b).__name__)
            }
        )

        Assertion._register(result)
        return result
