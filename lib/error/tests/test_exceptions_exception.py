from jarbin_toolkit_error import (
    JException,
)


def test_jexception():
    error = JException(
        "this is a message",
    )

    assert error.error == "JException"
    assert "this is a message" in error.message
