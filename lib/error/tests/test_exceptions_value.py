from jarbin_toolkit_error import (
    JErrorType,
    JErrorValue,
    JErrorIndex,
    JErrorName,
    JErrorAttribute,
    JErrorKey,
)


def test_jerror_type():
    error = JErrorType(
        "this is a message",
        expected=str,
        actual=5,
    )

    assert error.error == "JErrorType"
    assert "this is a message" in error.message
    assert "Expected: str" in error.message
    assert "Actual: int" in error.message
    assert "Value: 5" in error.message


def test_jerror_value():
    error = JErrorValue(
        "this is a message",
        value=5,
    )

    assert error.error == "JErrorValue"
    assert "this is a message" in error.message
    assert "Value: 5" in error.message


def test_jerror_attribute():
    error = JErrorAttribute(
        "this is a message",
        attribute="name",
    )

    assert error.error == "JErrorAttribute"
    assert "this is a message" in error.message
    assert "Attribute: 'name'" in error.message


def test_jerror_name():
    error = JErrorName(
        "this is a message",
        name="a_name",
    )

    assert error.error == "JErrorName"
    assert "this is a message" in error.message
    assert "Name: 'a_name'" in error.message


def test_jerror_index():
    error = JErrorIndex(
        "this is a message",
        index=5,
        obj=[0, 1, 2, 3, 4]
    )

    assert error.error == "JErrorIndex"
    assert "this is a message" in error.message
    assert "Index: 5" in error.message
    assert "Actual length: 5" in error.message
    assert "Last index: 4" in error.message


def test_jerror_key():
    error = JErrorKey(
        "this is a message",
        key='a_key',
    )

    assert error.error == "JErrorKey"
    assert "this is a message" in error.message
    assert "Key: 'a_key'" in error.message
