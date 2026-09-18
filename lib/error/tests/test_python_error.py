from jarbin_toolkit_error import JErrorType
from jarbin_toolkit_error.enums import FormatType


def test_j_error_type_basic():
    error = JErrorType(
        obj=42,
        name="value",
        expected=str,
    )

    assert error.error == "JErrorType"
    assert "Invalid type for 'value'" in error.message
    assert "Expected: str" in error.message
    assert "Received: int" in error.message
    assert "Value: 42" in error.message


def test_j_error_type_without_name():
    error = JErrorType(
        obj=None,
        expected=str,
        format=FormatType.COMPACT,
    )

    assert error.message.startswith("Invalid type")
    assert "Expected: str" in error.message
    assert "Received: NoneType" in error.message
    assert "Value: None" in error.message
    assert str(error).startswith("JErrorType:")


def test_j_error_type_custom_message():
    error = JErrorType(
        message="This value is not valid.",
        obj=12,
        name="age",
        expected=str,
    )

    assert "Invalid type for 'age'" in error.message
    assert "Expected: str" in error.message
    assert "Received: int" in error.message
    assert "Value: 12" in error.message
    assert "→ This value is not valid." in error.message
