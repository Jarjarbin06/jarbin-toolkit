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

from jarbin_toolkit import Config


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

TEST_PATH = "./tests/JT/"
TEST_NAME = "config_tmp"


def JT_config_set_get():
    cfg = Config(
        TEST_PATH,
        file_name=TEST_NAME,
        data={"App": {"x": "10"}}
    )

    cfg.set("App", "y", 20)

    Assertion.eq(cfg.get("App", "x"), "10", "invalid x")
    Assertion.eq(cfg.get_int("App", "y"), 20, "invalid y")


def JT_config_types():
    cfg = Config(
        TEST_PATH,
        file_name=TEST_NAME,
        data={
            "T": {
                "i": "1",
                "f": "1.5",
                "b": "true"
            }
        }
    )

    Assertion(
        isinstance(cfg.get_int("T", "i"), int),
        "invalid i type"
    )
    Assertion(
        isinstance(cfg.get_float("T", "f"), float),
        "invalid f type"
    )
    Assertion(
        isinstance(cfg.get_bool("T", "b"), bool),
        "invalid b type"
    )


def JT_config_delete():
    cfg = Config(TEST_PATH, file_name=TEST_NAME)
    cfg.delete()

    Assertion(
        not os.path.exists(TEST_PATH + "/config.ini"),
        "config file not deleted"
    )

def JT_config_missing():
    cfg = Config(
        TEST_PATH,
        data={
            "A Section": {
                "a_value": "10"
            }
        },
        file_name="missing_config.ini"
    )

    try:
        cfg.get("Missing", "value")
    except Exception as ex:
        Show.Exception(ex)


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

JTT_JTK_Config = JarTest(
    context=Context(
        output={"show_output": True},
        command=[(None, "rm tests/JT/missing_config.ini")]
    )
)
JTT_JTK_Config.fetch()
