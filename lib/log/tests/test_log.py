import pytest


from jarbin_toolkit_log import Log


def test_log_log_reading(
    ) -> None:
    log = Log("tests", "log_test_log")
    log.log("INFO", "test", "this is a test")
    log.comment("this is a custom comment")
    log.close()
    s = log.read()
    assert "   date          time      | [TYPE]  title      | detail\n\n---START---\n" in s
    assert " | [INFO]  test       | this is a test\n>>> this is a custom comment\n----END----\n" in s


def test_log_log_str(
    ) -> None:
    log = Log("tests", "log_test_log")
    s = str(log)
    assert "[INFO]" in s
    assert "this is a test" in s
    assert "this is a custom comment" in s

def test_log_log_edit_after_closing(
    ) -> None:
    log = Log("tests", "log_test_log")
    s = str(log)
    log.comment("this is a custom comment")
    assert str(log) == s


def test_log_log_repr(
    ) -> None:
    log = Log("tests", "log_test_log")
    s = repr(log)
    assert s == "Log(\'tests/\', \'log_test_log\', False)"


def test_log_log_delete(
    ) -> None:
    log = Log("tests", "log_test_log")
    log.delete()

def test_log_json_reading(
    ) -> None:
    log = Log("tests", "log_test_json", json = True)
    log.log("INFO", "test", "this is a test")
    log.log("INFO", "test", "this is a second test")
    log.log("INFO", "test", "and a third")
    log.close()
    s = log.read()
    assert "{" in s and "}" in s


def test_log_json_str(
    ) -> None:
    log = Log("tests", "log_test_json", json = True)
    s = str(log)
    assert "INFO" in s
    assert "this is a test" in s

def test_log_json_edit_after_closing(
    ) -> None:
    log = Log("tests", "log_test_json", json = True)
    s = str(log)
    log.comment("this is a custom comment")
    assert str(log) == s


def test_log_json_repr(
    ) -> None:
    log = Log("tests", "log_test_json", json = True)
    s = repr(log)
    assert s == "Log(\'tests/\', \'log_test_json\', True)"


def test_log_json_delete(
    ) -> None:
    log = Log("tests", "log_test_json", json = True)
    log.delete()
