import pytest


from jarbin_toolkit_log import Log


def test_log_reading(
    ) -> None:
    log = Log("tests", "log_test")
    log.log("INFO", "test", "this is a test")
    log.comment("this is a custom comment")
    log.close()
    s = log.read()
    assert "   date          time      | [TYPE]  title      | detail\n\n---START---\n" in s
    assert " | [INFO]  test       | this is a test\n>>> this is a custom comment\n----END----\n" in s


def test_log_str(
    ) -> None:
    log = Log("tests", "log_test")
    s = str(log)
    assert "[INFO]" in s
    assert "this is a test" in s
    assert "this is a custom comment" in s


def test_log_repr(
    ) -> None:
    log = Log("tests", "log_test")
    s = repr(log)
    assert s == "Log(\'tests/\', \'log_test\')"


def test_log_delete(
    ) -> None:
    log = Log("tests", "log_test")
    log.close(delete=True)
