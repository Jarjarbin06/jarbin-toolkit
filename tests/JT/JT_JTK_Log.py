import os

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

from jarbin_toolkit import Log


# ---------------------------------------------------------------------------
# Log
# ---------------------------------------------------------------------------

TEST_PATH = "./tests/JT/"
TEST_NAME = "test_logs"


def JT_log_write():
    log = Log(TEST_PATH, TEST_NAME)

    log.log("INFO", "title", "message")
    log.comment("comment")

    log.close()

    Assertion(
        os.path.exists(TEST_PATH + TEST_NAME + ".jar-log"),
        "failed to create log"
    )

    log.delete()

    Assertion(
        not os.path.exists(TEST_PATH + TEST_NAME + ".jar-log"),
        "failed to delete log"
    )


def JT_log_filter():
    log = Log(TEST_PATH, TEST_NAME)

    log.log("INFO", "t1", "m1")
    log.log("ERROR", "t2", "m2")

    log.close()

    result = log.str_filtered("ERROR")

    Assertion(
        "m2" in result and "m1" not in result,
        "failed to filter log"
    )

    log.close()
    log.delete()


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

JTT_JTK_Log = JarTest()
JTT_JTK_Log.fetch()
