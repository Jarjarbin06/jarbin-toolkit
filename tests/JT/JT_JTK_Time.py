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

from jarbin_toolkit import Time


# ---------------------------------------------------------------------------
# Time
# ---------------------------------------------------------------------------

def JT_stopwatch_basic():
    sw = Time.StopWatch(True)

    Time.Time.wait(0.2)
    sw.stop()

    Assertion(
        sw.elapsed() >= 0.2,
        "invalid elapsed time"
    )


def JT_stopwatch_reset():
    sw = Time.StopWatch(True)

    sw.reset()

    Assertion(
        sw.elapsed() >= 0,
        "invalid elapsed time"
    )


def JT_time_wait():
    elapsed = Time.Time.wait(0.1)

    Assertion(
        elapsed >= 0.1,
        "invalid elapsed time"
    )


def JT_time_timestamp():
    timestamp = Time.get_timestamp()

    Assertion(
        isinstance(timestamp, (int, float)),
        "timestamp has invalid type"
    )


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

JTT_JTK_Time = JarTest()
JTT_JTK_Time.fetch()
