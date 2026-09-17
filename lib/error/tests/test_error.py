import pytest

from jarbin_toolkit_error import (
    BaseError,
    FormatType,
)


def test_default_values():
    error = BaseError("Something went wrong")

    assert error.message == "Something went wrong"
    assert error.error == "BaseError"
    assert error._format == FormatType.TRACEBACK
    assert error._link is not None


def test_custom_error():
    error = BaseError(
        "Something went wrong",
        error="CustomError",
    )

    assert error.error == "CustomError"


def test_message_is_stripped():
    error = BaseError(
        "  Something went wrong  \n",
    )

    assert error.message == "Something went wrong"


def test_empty_message():
    error = BaseError("")

    assert error.message == ""


@pytest.mark.parametrize(
    "format",
    [
        FormatType.COMPACT,
        FormatType.PRETTY,
        FormatType.DETAILED,
        FormatType.TRACEBACK,
    ],
)
def test_format_enum(format):
    error = BaseError(
        "Something went wrong",
        format=format,
    )

    assert error._format == format


@pytest.mark.parametrize(
    "format",
    ["c", "compact", "p", "pretty", "d", "detailed", "t", "traceback"],
)
def test_format_string(format):
    error = BaseError(
        "Something went wrong",
        format=format,
    )

    assert isinstance(error._format, FormatType)


def test_invalid_message_type():
    with pytest.raises(TypeError, match="Message must be of type str"):
        BaseError(123)


def test_invalid_error_type():
    with pytest.raises(TypeError, match="Error must be of type str"):
        BaseError(
            "Something went wrong",
            error=123,
        )


def test_invalid_format_type():
    with pytest.raises(TypeError):
        BaseError(
            "Something went wrong",
            format=123,
        )


def test_compact():
    error = BaseError(
        "Something went wrong",
        error="CustomError",
        format="compact",
    )

    assert str(error) == (
        "CustomError: 'Something went wrong'"
    )


def test_compact_multiline():
    error = BaseError(
        "Something went wrong\nin the file",
        error="CustomError",
        format="compact",
    )

    assert str(error) == (
        "CustomError: 'Something went wrong\\nin the file'"
    )


def test_pretty():
    error = BaseError(
        "Something went wrong",
        error="CustomError",
        format="pretty",
    )

    result = str(error)

    assert "CustomError" in result
    assert "Something went wrong" in result


def test_pretty_multiline():
    error = BaseError(
        "Something went wrong\nin the file",
        error="CustomError",
        format="pretty",
    )

    result = str(error)

    assert "Something went wrong" in result
    assert "in the file" in result
    assert "\n" in result


def test_detailed():
    error = BaseError(
        "Something went wrong",
        error="CustomError",
        format="detailed",
    )

    result = str(error)

    assert "CustomError" in result
    assert "Something went wrong" in result
    assert "Location:" in result


def test_traceback():
    error = BaseError(
        "Something went wrong",
        error="CustomError",
        format="traceback",
    )

    result = str(error)

    assert "CustomError" in result
    assert "Something went wrong" in result


def test_traceback_multiline():
    error = BaseError(
        "Something went wrong\nin the file",
        error="CustomError",
        format="traceback",
    )

    result = str(error)

    assert "CustomError" in result
    assert "Something went wrong" in result
    assert "    in the file" in result


def test_traceback_does_not_duplicate_indentation():
    error = BaseError(
        "first\nsecond\nthird",
        format="traceback",
    )

    result = str(error)

    assert "\n    first\n    second\n    third" in result


def test_do_raise():
    with pytest.raises(BaseError) as raised:
        BaseError(
            "Something went wrong",
            do_raise=True,
        )

    assert raised.value.message == "Something went wrong"


def test_repr():
    error = BaseError(
        "Something went wrong",
        error="CustomError",
    )

    assert repr(error) == (
        "<BaseError("
        "error='CustomError', "
        "message='Something went wrong', "
        ")>"
    )


def test_is_exception():
    error = BaseError("Something went wrong")

    assert isinstance(error, Exception)
