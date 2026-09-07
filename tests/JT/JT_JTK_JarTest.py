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


# ---------------------------------------------------------------------------
# JarTest Context / decorators
# ---------------------------------------------------------------------------

@env(JT_Test="123")
def JT_context_env():
    Assertion.eq(
        os.environ.get("JT_Test"),
        "123",
        "invalid JT_Test"
    )


@env(
    JT_Test="123",
    JT_Second="456"
)
def JT_context_multiple_env():
    Assertion.eq(
        os.environ.get("JT_Test"),
        "123",
        "invalid JT_Test"
    )
    Assertion.eq(
        os.environ.get("JT_Second"),
        "456",
        "invalid JT_Second"
    )


@command("echo 'hello world'")
@output(show_context=True)
def JT_context_command():
    Assertion(True)


@env(JT_Test="123")
def JT_context_override():
    Assertion.eq(
        os.environ["JT_Test"],
        "123",
        "test context did not override JarTest context"
    )


def JT_context_restore():
    original = os.environ.get("JT_Restore_Test")

    with Context(
        env={
            "JT_Restore_Test": "123"
        }
    ):
        Assertion.eq(
            os.environ.get("JT_Restore_Test"),
            "123",
            "context environment was not applied"
        )

    Assertion.eq(
        os.environ.get("JT_Restore_Test"),
        original,
        "context environment was not restored"
    )


def JT_context_enter_exit():
    context = Context(
        env={
            "JT_EnterExit": "123"
        }
    )

    with context:
        Assertion.eq(
            os.environ.get("JT_EnterExit"),
            "123",
            "context __enter__ failed"
        )

    Assertion(
        os.environ.get("JT_EnterExit") != "123",
        "context __exit__ failed"
    )


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

JTT_JTK_JarTest = JarTest(
    context=Context(
        env={
            "JT_Test": "312"
        }
    )
)
JTT_JTK_JarTest.fetch()
