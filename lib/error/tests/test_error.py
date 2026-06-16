import pytest


import jarbin_toolkit_error as Error


def test_error_default_constructor(
    ) -> None:
    err = Error.BaseError()
    assert err.message == "an error occurred"
    assert err.error == "Error"
    assert err.link is None
    assert isinstance(err, Error.BaseError)


def test_error_full_constructor(
    ) -> None:
    err = Error.BaseError("Something broke", error="SystemError", link=("path/file.py", 42))
    assert err.message == "Something broke"
    assert err.error == "SystemError"
    assert not err.link is None
    assert str(err.link) == 'File "path/file.py", line 42'
    #assert 'file=path/file.py&line=42' in str(err.link)
    #assert '"path/file.py", line 42' in str(err.link)


def test_error_str_without_link(
    ) -> None:
    err = Error.BaseError("Broken", error="RuntimeError")
    s = str(err)

    assert "RuntimeError" in s
    assert "Broken" in s
    assert "File" not in s
    assert "line" not in s


def test_error_str_with_link_no_line(
    ) -> None:
    err = Error.BaseError("Crash detected", error="FatalError", link=("engine.py", None))
    s = str(err)

    assert "FatalError" in s
    assert "Crash detected" in s
    assert "engine.py" in s
    assert "File" in s


def test_error_repr(
    ) -> None:
    err = Error.BaseError("Crash detected", error="FatalError", link=("engine.py", None))

    assert repr(err) == "BaseError(\'Crash detected\', error=\'FatalError\', link=(\'engine.py\', None))"


def test_error_str_with_link_with_line(
    ) -> None:
    err = Error.BaseError("Crash detected", error="FatalError", link=("engine.py", 88))
    s = str(err)

    assert "FatalError" in s
    assert "Crash detected" in s
    assert "engine.py" in s
    assert "88" in s
    assert "File" in s
    assert "line" in s


def test_error_str_formatting_clean(
    ) -> None:
    err = Error.BaseError("X", error="Y", link=("a.py", 5))
    output = str(err).replace("\n", " ").strip()

    assert "Y" in output
    assert "X" in output
    assert "a.py" in output
    assert "5" in output


def test_link_negative_line_number_not_allowed(
    ) -> None:
    err = Error.BaseError("msg", error="Err", link=("file.py", -1))
    assert not err.link


def test_empty_message_and_error_are_allowed(
    ) -> None:
    err = Error.BaseError("", error="")
    assert err.message == ""
    assert err.error == ""


def test_error_error(
    ) -> None:
    err = Error.Error.ErrorImport()

    assert err.error == "Error(ErrorImport)"


def test_error_error_file(
    ) -> None:
    err = Error.File.ErrorFileParse()

    assert err.error == "Error File(ErrorFileParse)"


def test_error_error_logic(
    ) -> None:
    err = Error.Logic.ErrorLogicAssertion()

    assert err.error == "Error Logic(ErrorLogicAssertion)"


def test_error_error_network(
    ) -> None:
    err = Error.Network.ErrorNetworkHTTP()

    assert err.error == "Error Network(ErrorNetworkHTTP)"


def test_error_special(
    ) -> None:
    err = Error.Special.ErrorSpecialLaunch()

    assert err.error == "Error Special(ErrorSpecialLaunch)"


def test_error_state(
    ) -> None:
    err = Error.State.ErrorStateNotInitialized()

    assert err.error == "Error State(ErrorStateNotInitialized)"


def test_error_system(
    ) -> None:
    err = Error.System.ErrorSystemTimeout()

    assert err.error == "Error System(ErrorSystemTimeout)"
