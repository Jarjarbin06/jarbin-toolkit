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
        str(error),
        "msg",
        "message not an Exception"
    )


def JT_error_with_link():
    error = Error.Error.ErrorRuntime(
        "msg",
        link=("file.py", 10)
    )

    Assertion.contain(
        str(error),
        "file.py",
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
        str(error),
        "logic error",
        "logic error message invalid"
    )


def JT_error_file():
    error = Error.File.ErrorFileParse("file error")

    Assertion.contain(
        str(error),
        "file error",
        "file error message invalid"
    )


def JT_error_network():
    error = Error.Network.ErrorNetwork("network error")

    Assertion.contain(
        str(error),
        "network error",
        "network error message invalid"
    )


def JT_error_state():
    error = Error.State.ErrorState("state error")

    Assertion.contain(
        str(error),
        "state error",
        "state error message invalid"
    )


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

JTT_JTK_Error = JarTest()
JTT_JTK_Error.fetch()
