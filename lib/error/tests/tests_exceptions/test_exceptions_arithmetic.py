# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : test_exceptions_arithmetic.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error import (
    JErrorArithmetic,
    JErrorZeroDivision,
    JErrorOverflow,
    JErrorFloatingPoint,
)


def test_jerror_arithmetic():
    error = JErrorArithmetic(
        "this is a message",
    )

    assert error.error == "JErrorArithmetic"
    assert "this is a message" in error.message


def test_jerror_zero_division():
    error = JErrorZeroDivision(
        "this is a message",
        dividend=20,
    )

    assert error.error == "JErrorZeroDivision"
    assert "this is a message" in error.message
    assert "Dividend: 20" in error.message


def test_jerror_overflow():
    error = JErrorOverflow(
        "this is a message",
    )

    assert error.error == "JErrorOverflow"
    assert "this is a message" in error.message


def test_jerror_floating_point():
    error = JErrorFloatingPoint(
        "this is a message",
    )

    assert error.error == "JErrorFloatingPoint"
    assert "this is a message" in error.message
