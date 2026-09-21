from jarbin_toolkit_error import (
    JErrorImport,
    JErrorModuleNotFound,
)


def test_jerror_import():
    error = JErrorImport(
        "this is a message",
        from_name="FROM",
        import_name="IMPORT",
    )

    assert error.error == "JErrorImport"
    assert "this is a message" in error.message
    assert "From: 'FROM'" in error.message
    assert "Import: 'IMPORT'" in error.message


def test_jerror_module_not_found():
    error = JErrorModuleNotFound(
        "this is a message",
        name="IMPORT",
    )

    assert error.error == "JErrorModuleNotFound"
    assert "this is a message" in error.message
    assert "Import: 'IMPORT'" in error.message
