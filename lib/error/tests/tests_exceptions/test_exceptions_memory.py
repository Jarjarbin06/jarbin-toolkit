# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : test_exceptions_memory.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error import (
    JErrorMemory,
    JErrorBuffer,
)


def test_jerror_memory():
    error = JErrorMemory(
        "this is a message",
    )

    assert error.error == "JErrorMemory"
    assert "this is a message" in error.message


def test_jerror_buffer():
    error = JErrorBuffer(
        "this is a message",
    )

    assert error.error == "JErrorBuffer"
    assert "this is a message" in error.message
