# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : test_exceptions_assertion.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error import (
    JErrorAssertion,
    JErrorLookup,
)


def test_jerror_assertion():
    error = JErrorAssertion(
        "this is a message",
    )

    assert error.error == "JErrorAssertion"
    assert "this is a message" in error.message


def test_jerror_lookup():
    error = JErrorLookup(
        "this is a message",
    )

    assert error.error == "JErrorLookup"
    assert "this is a message" in error.message
