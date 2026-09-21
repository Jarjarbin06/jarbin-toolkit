from jarbin_toolkit_error import (
    JErrorRuntime,
    JErrorNotImplemented,
    JErrorRecursion,
    JErrorSystem,
)


def test_jerror_runtime():
    error = JErrorRuntime(
        "this is a message",
    )

    assert error.error == "JErrorRuntime"
    assert "this is a message" in error.message


def test_jerror_not_implemented():
    error = JErrorNotImplemented(
        "this is a message",
    )

    assert error.error == "JErrorNotImplemented"
    assert "this is a message" in error.message


def test_jerror_recursion():
    error = JErrorRecursion(
        "this is a message",
    )

    assert error.error == "JErrorRecursion"
    assert "this is a message" in error.message


def test_jerror_system():
    error = JErrorSystem(
        "this is a message",
    )

    assert error.error == "JErrorSystem"
    assert "this is a message" in error.message
