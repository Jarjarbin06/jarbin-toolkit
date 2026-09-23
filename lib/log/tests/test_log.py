# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Log
# File         : test_log.py
#
# Author       : Jarjarbin06
# ============================================================================


from pathlib import Path

import pytest

from jarbin_toolkit_log import (
    Log,
    LogType,
    LogLevel,
    LogTypeJError,
    LogRuntimeJError,
)


def test_create(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    assert log.directory == tmp_path
    assert log.name == "test"
    assert log.type == LogType.JAR_LOG.name
    assert log.path.exists()
    assert log.path.is_file()


def test_create_with_metadata(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
        metadata={
            "cmd": "pytest",
            "host": "test-host",
            "pid": 1234,
        },
    )

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert 'cmd="pytest"' in content
    assert 'host="test-host"' in content
    assert "pid=1234" in content


def test_create_with_log_type(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
        type=LogType.LOG,
    )

    assert log.type == LogType.LOG.name
    assert log.path.suffix == ".log"


def test_create_with_log_type_string(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
        type="jar-log",
    )

    assert log.type == LogType.JAR_LOG.name


def test_create_with_invalid_type(
        tmp_path: Path,
    ):

    with pytest.raises(LogTypeJError):
        Log(
            tmp_path,
            "test",
            type=123,
        )


def test_create_with_invalid_datetime_format(
        tmp_path: Path,
    ):

    with pytest.raises(LogTypeJError):
        Log(
            tmp_path,
            "test",
            datetime_format=123,
        )


def test_create_with_invalid_entry_datetime_format(
        tmp_path: Path,
    ):

    with pytest.raises(LogTypeJError):
        Log(
            tmp_path,
            "test",
            entry_datetime_format=123,
        )


def test_initial_waiting_marker(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "[waiting for log...]" in content
    assert content.endswith(
        "[waiting for log...]\n"
    )


def test_log(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.log(
        LogLevel.INFO,
        "hello",
    )

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "hello" not in content

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "hello" in content
    assert "INFO" in content


def test_log_with_string_level(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.log(
        "info",
        "hello",
    )

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "INFO" in content
    assert "hello" in content


def test_all_log_levels(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    for level in LogLevel:
        log.log(
            level,
            f"message-{level.name.lower()}",
        )

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    for level in LogLevel:
        assert level.name in content
        assert f"message-{level.name.lower()}" in content


def test_log_with_scope(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.log(
        LogLevel.INFO,
        "hello",
        scope="generator",
    )

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "generator" in content
    assert "hello" in content


def test_comment(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.comment(
        "this is a comment",
    )

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "this is a comment" in content
    assert "    | this is a comment" in content


def test_multiline_comment(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.comment(
        "first line\nsecond line\nthird line",
    )

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "    | first line" in content
    assert "    | second line" in content
    assert "    | third line" in content


def test_multiple_flushes(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.log(
        LogLevel.INFO,
        "first",
    )

    log.flush()

    log.log(
        LogLevel.INFO,
        "second",
    )

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "first" in content
    assert "second" in content
    assert content.count("INFO") == 2


def test_flush_without_entries(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert content.endswith(
        "[waiting for log...]\n"
    )


def test_sequence_order(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    for index in range(10):
        log.log(
            LogLevel.INFO,
            f"message-{index}",
        )

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    positions = [
        content.index(
            f"message-{index}"
        )
        for index in range(10)
    ]

    assert positions == sorted(positions)

    for index in range(10):
        assert f"{index:05}" in content


def test_comment_does_not_increment_sequence(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.log(
        LogLevel.INFO,
        "first",
    )

    log.comment(
        "comment",
    )

    log.log(
        LogLevel.INFO,
        "second",
    )

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "00000" in content
    assert "00001" in content
    assert "comment" in content


def test_close(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.log(
        LogLevel.INFO,
        "hello",
    )

    log.close()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "hello" in content
    assert "[waiting for log...]" not in content
    assert "result=SUCCESS" in content
    assert "════════════════════════════════════════════════════════════════════════════" in content


def test_close_flushes_pending_entries(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.log(
        LogLevel.INFO,
        "pending message",
    )

    log.close()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "pending message" in content


def test_close_with_result(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.close(
        result="FAILED",
    )

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "result=FAILED" in content


def test_close_counts_levels(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.log(
        LogLevel.ERROR,
        "error",
    )

    log.log(
        LogLevel.ERROR,
        "another error",
    )

    log.log(
        LogLevel.WARNING,
        "warning",
    )

    log.log(
        LogLevel.CRITICAL,
        "critical",
    )

    log.close()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "errors=2" in content
    assert "warnings=1" in content
    assert "criticals=1" in content


def test_log_after_close(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.close()

    with pytest.raises(LogRuntimeJError):
        log.log(
            LogLevel.INFO,
            "invalid",
        )


def test_comment_after_close(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.close()

    with pytest.raises(LogRuntimeJError):
        log.comment(
            "invalid",
        )


def test_flush_after_close(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.close()

    with pytest.raises(LogRuntimeJError):
        log.flush()


def test_close_twice(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.close()
    log.close()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert content.count(
        "result=SUCCESS"
    ) == 1


def test_invalid_log_level(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    with pytest.raises(ValueError):
        log.log(
            "invalid-level",
            "message",
        )


def test_invalid_message_type(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    with pytest.raises(LogTypeJError):
        log.log(
            LogLevel.INFO,
            123,
        )


def test_invalid_comment_type(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    with pytest.raises(LogTypeJError):
        log.comment(
            123,
        )


@pytest.mark.asyncio
async def test_log_async(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    await log.log_async(
        LogLevel.INFO,
        "async message",
    )

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "async message" in content


@pytest.mark.asyncio
async def test_comment_async(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    await log.comment_async(
        "async comment",
    )

    log.flush()

    content = log.path.read_text(
        encoding="utf-8",
    )

    assert "async comment" in content


def test_marker_corruption_on_flush(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    log.log(
        LogLevel.INFO,
        "message",
    )

    content = log.path.read_text(
        encoding="utf-8",
    ).replace(
        "[waiting for log...]",
        "[corrupted marker]",
    )

    log.path.write_text(
        content,
        encoding="utf-8",
    )

    with pytest.raises(LogRuntimeJError):
        log.flush()


def test_marker_corruption_on_close(
        tmp_path: Path,
    ):

    log = Log(
        tmp_path,
        "test",
    )

    content = log.path.read_text(
        encoding="utf-8",
    ).replace(
        "[waiting for log...]",
        "[corrupted marker]",
    )

    log.path.write_text(
        content,
        encoding="utf-8",
    )

    with pytest.raises(LogRuntimeJError):
        log.close()
