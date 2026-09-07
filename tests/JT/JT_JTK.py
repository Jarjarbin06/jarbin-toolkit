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

import jarbin_toolkit as JTK


# ---------------------------------------------------------------------------
# Jarbin-ToolKit
# ---------------------------------------------------------------------------

def JT_get_info():
    info = JTK.get_info()

    Assertion(isinstance(info, dict), "invalid info type")
    Assertion.contain("version", info, "version is not in info")


def JT_benchmark_success():
    def sample():
        return 123

    result, elapsed, err = JTK.benchmark(sample)

    Assertion.eq(result, 123, "result invalid")
    Assertion(err is None, "an error occured")
    Assertion(elapsed >= 0, "elapsed time == 0")


def JT_benchmark_exception():
    def sample():
        raise RuntimeError("fail")

    result, elapsed, err = JTK.benchmark(sample)

    Assertion(result is None, "not suppose to get result")
    Assertion(isinstance(err, Exception), "err of the wrong type")


def JT_fail():
    try:
        JTK.fail("test error")
    except Exception as e:
        Assertion.contain("test error", str(e), "invalid string")


def JT_text():
    t = JTK.text("Hello", "World")

    Assertion(hasattr(t, "bold"), "text not working properly")


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

JTT_JTK = JarTest()
JTT_JTK.fetch()
