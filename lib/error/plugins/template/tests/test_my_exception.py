import pytest

from jarbin_toolkit_error_template import (
    JErrorMyException,
    FormatType,
)


def test_default_values():
    error = JErrorMyException("Something went wrong")

    assert "Something went wrong" in error.message
    assert error.error == "JErrorMyException"
    assert error._format == FormatType.TRACEBACK
    assert error._link is not None
