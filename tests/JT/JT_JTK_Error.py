from jarbin_toolkit_jartest import (
    JarTest,
    Get,
    Show,
    Assertion,
    Context,
    env,
    command,
    output
)

from jarbin_toolkit import Error


# ---------------------------------------------------------------------------
# Error
# ---------------------------------------------------------------------------

def JT_error_base():
    error = Error.Error.ErrorRuntime("msg")

    Assertion.contain(
        "msg",
        str(error),
        "message not an Exception"
    )


def JT_error_with_link():
    error = Error.Error.ErrorRuntime(
        "msg",
        link=("file.py", 10)
    )

    Assertion.contain(
        "file.py",
        str(error),
        "file not shown"
    )


def JT_error_types():
    error = Error.Special.ErrorSpecialConfig("config error")

    Assertion(
        isinstance(error, Exception),
        "error is not an Exception"
    )


def JT_error_logic():
    error = Error.Logic.ErrorLogicAssertion("logic error")

    Assertion.contain(
        "logic error",
        str(error),
        "logic error message invalid"
    )


def JT_error_file():
    error = Error.File.ErrorFileParse("file error")

    Assertion.contain(
        "file error",
        str(error),
        "file error message invalid"
    )


def JT_error_network():
    error = Error.Network.ErrorNetwork("network error")

    Assertion.contain(
        "network error",
        str(error),
        "network error message invalid"
    )


def JT_error_state():
    error = Error.State.ErrorState("state error")

    Assertion.contain(
        "state error",
        str(error),
        "state error message invalid"
    )


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

JTT_JTK_Error = JarTest()
JTT_JTK_Error.fetch()
