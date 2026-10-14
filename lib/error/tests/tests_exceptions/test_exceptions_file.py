# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : test_exceptions_memory.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error import (
    JErrorIO,
    JErrorFileNotFound,
    JErrorFileExists,
    JErrorPermission,
    JErrorIsADirectory,
    JErrorNotADirectory,
    JErrorDirectoryNotEmpty,
)


def test_jerror_io():
    error = JErrorIO(
        "this is a message",
    )

    assert error.error == "JErrorIO"
    assert "this is a message" in error.message


def test_jerror_file_not_found():
    error = JErrorFileNotFound(
        "this is a message",
        path="/my/path",
    )

    assert error.error == "JErrorFileNotFound"
    assert "this is a message" in error.message
    assert "/my/path" in error.message


def test_jerror_file_exists():
    error = JErrorFileExists(
        "this is a message",
        path="/my/path",
    )

    assert error.error == "JErrorFileExists"
    assert "this is a message" in error.message
    assert "/my/path" in error.message


def test_jerror_permission():
    error = JErrorPermission(
        "this is a message",
        path="/my/path",
    )

    assert error.error == "JErrorPermission"
    assert "this is a message" in error.message
    assert "/my/path" in error.message


def test_jerror_is_a_directory():
    error = JErrorIsADirectory(
        "this is a message",
        path="/my/path",
    )

    assert error.error == "JErrorIsADirectory"
    assert "this is a message" in error.message
    assert "/my/path" in error.message


def test_jerror_not_a_directory():
    error = JErrorNotADirectory(
        "this is a message",
        path="/my/path",
    )

    assert error.error == "JErrorNotADirectory"
    assert "this is a message" in error.message
    assert "/my/path" in error.message


def test_jerror_directory_not_empty():
    error = JErrorDirectoryNotEmpty(
        "this is a message",
        path="/my/path",
    )

    assert error.error == "JErrorDirectoryNotEmpty"
    assert "this is a message" in error.message
    assert "/my/path" in error.message
