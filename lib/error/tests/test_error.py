import pytest


from jarbin_toolkit_error import *


def test_error_default_constructor(
    ) -> None:
    err = Error()
    assert err.message == "an error occurred"
    assert err.error == "Error"
    assert err.link is None
    assert isinstance(err, Error)


def test_error_full_constructor(
    ) -> None:
    err = Error("Something broke", error="SystemError", link=("path/file.py", 42))
    assert err.message == "Something broke"
    assert err.error == "SystemError"
    assert not err.link is None
    assert str(err.link) == 'File "path/file.py", line 42'
    #assert 'file=path/file.py&line=42' in str(err.link)
    #assert '"path/file.py", line 42' in str(err.link)


def test_error_str_without_link(
    ) -> None:
    err = Error("Broken", error="RuntimeError")
    s = str(err)

    assert "RuntimeError" in s
    assert "Broken" in s
    assert "File" not in s
    assert "line" not in s


def test_error_str_with_link_no_line(
    ) -> None:
    err = Error("Crash detected", error="FatalError", link=("engine.py", None))
    s = str(err)

    assert "FatalError" in s
    assert "Crash detected" in s
    assert "engine.py" in s
    assert "File" in s


def test_error_repr(
    ) -> None:
    err = Error("Crash detected", error="FatalError", link=("engine.py", None))

    assert repr(err) == "Error(\'Crash detected\', error=\'FatalError\', link=(\'engine.py\', None))"


def test_error_str_with_link_with_line(
    ) -> None:
    err = Error("Crash detected", error="FatalError", link=("engine.py", 88))
    s = str(err)

    assert "FatalError" in s
    assert "Crash detected" in s
    assert "engine.py" in s
    assert "88" in s
    assert "File" in s
    assert "line" in s


def test_error_str_formatting_clean(
    ) -> None:
    err = Error("X", error="Y", link=("a.py", 5))
    output = str(err).replace("\n", " ").strip()

    assert "Y" in output
    assert "X" in output
    assert "a.py" in output
    assert "5" in output


def test_link_negative_line_number_disallowed(
    ) -> None:
    err = Error("msg", error="Err", link=("file.py", -1))
    assert not err.link


def test_empty_message_and_error_are_allowed(
    ) -> None:
    err = Error("", error="")
    assert err.message == ""
    assert err.error == ""


def test_error_error_launch(
    ) -> None:
    err = ErrorLaunch()

    assert err.error == "ErrorLaunch"


def test_error_error_import(
    ) -> None:
    err = ErrorImport()

    assert err.error == "ErrorImport"


def test_error_error_log(
    ) -> None:
    err = ErrorLog()

    assert err.error == "ErrorLog"


def test_error_error_config(
    ) -> None:
    err = ErrorConfig()

    assert err.error == "ErrorConfig"


def test_error_error_setting(
    ) -> None:
    err = ErrorSetting()

    assert err.error == "ErrorSetting"


def test_error_error_type(
    ) -> None:
    err = ErrorType()

    assert err.error == "ErrorType"


def test_error_error_value(
    ) -> None:
    err = ErrorValue()

    assert err.error == "ErrorValue"
