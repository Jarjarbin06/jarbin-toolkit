import pytest

from types import SimpleNamespace

from jarbin_toolkit_jartest import JarTest, Assertion


def test_jartest_execute_valid_test() -> None:
    def JT_math_test() -> None:
        Assertion.eq(1 + 1, 2)

    test = JarTest()

    test(
        module=type(
            "Module",
            (),
            {
                "JT_math_test": JT_math_test
            }
        )
    )

    assert len(test) == 1
    assert test.tests["JT_math_test"].tested is True
    assert test.tests["JT_math_test"].error is None


def test_jartest_detect_failed_assertion() -> None:
    def JT_failed_test() -> None:
        Assertion.eq(1, 2)

    test = JarTest()

    result = test(
        module=type(
            "Module",
            (),
            {
                "JT_failed_test": JT_failed_test
            }
        )
    )

    assert result is None
    assert test.tests["JT_failed_test"].tested is True
    assert test.tests["JT_failed_test"].assertion is not None
    assert test.run() == 1


def test_jartest_detect_runtime_error() -> None:
    def JT_crash_test() -> None:
        raise ValueError("failure")

    test = JarTest()

    test(
        module=type(
            "Module",
            (),
            {
                "JT_crash_test": JT_crash_test
            }
        )
    )

    benchmark = test.tests["JT_crash_test"]

    assert benchmark.error is not None
    assert isinstance(benchmark.error, ValueError)


def test_jartest_execute_multiple_tests() -> None:
    def JT_first() -> None:
        Assertion.eq(True, True)

    def JT_second() -> None:
        Assertion.eq("hello", "hello")

    test = JarTest()

    test(
        module=type(
            "Module",
            (),
            {
                "JT_first": JT_first,
                "JT_second": JT_second
            }
        )
    )

    assert len(test) == 2
    assert test.run() == 0


def test_jartest_ignore_non_tests() -> None:
    def normal_function() -> None:
        return None

    def JT_valid() -> None:
        Assertion.eq(5, 5)

    test = JarTest()

    test.fetch(
        module=type(
            "Module",
            (),
            {
                "normal_function": normal_function,
                "JT_valid": JT_valid
            }
        )
    )

    assert len(test) == 1
    assert "JT_valid" in test.tests
    assert "normal_function" not in test.tests
