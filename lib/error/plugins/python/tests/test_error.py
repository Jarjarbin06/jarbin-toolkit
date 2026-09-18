import pytest

from jarbin_toolkit_error import (
    BaseJError,
    FormatType,
)


def test_default_values():
    error = BaseJError("Something went wrong")

    assert error.message == "Something went wrong"
    assert error.error == "BaseJError"
    assert error._format == FormatType.TRACEBACK
    assert error._link is not None
