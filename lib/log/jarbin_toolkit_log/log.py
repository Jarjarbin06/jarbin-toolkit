# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Log
# File         : log.py
#
# Author       : Jarjarbin06
# ============================================================================


from pathlib import Path
from threading import Lock
from uuid import uuid4
from queue import Queue

from jarbin_toolkit_time import (
    Time,
    TimeFormat,
)

from jarbin_toolkit_log.entry import LogEntry
from jarbin_toolkit_log.comment import LogComment
from jarbin_toolkit_log.enums import (
    LogType,
    LogLevel,
)
from jarbin_toolkit_log.errors import (
    LogTypeJError,
    LogRuntimeJError,
)
from jarbin_toolkit_log.renderer import LogRenderer


class Log:


    def _create_entry(
            self,
            level,
            message,
            scope,
        ):
        with self._sequence_lock:
            sequence = self._sequence
            self._sequence += 1

        return LogEntry(
            sequence,
            level,
            message,
            self._entry_format,
            self.type,
            scope,
        )


    def _initialize_file(
            self,
            metadata,
        ):
        self.directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self.path.open(
            "w",
            encoding="utf-8",
        ) as file:
            file.write(
                LogRenderer.header(
                    self._run_id,
                    self._created_at,
                    metadata,
                )
            )


    def _insert_entries(
            self,
            entries,
        ):
        if not entries:
            return

        marker = LogRenderer.WAITING_MARKER
        marker_bytes = marker.encode("utf-8")

        rendered = "".join(
            f"{entry}\n"
            for entry in entries
        )

        rendered_bytes = rendered.encode("utf-8")

        with self.path.open(
            "rb+",
        ) as file:
            file.seek(
                -(len(marker_bytes) + 1),
                2,
            )

            current_marker = file.read(
                len(marker_bytes),
            )

            if current_marker != marker_bytes:
                raise LogRuntimeJError(
                    "Log waiting marker was not found"
                )

            file.seek(
                -len(marker_bytes),
                1,
            )

            file.write(
                rendered_bytes,
            )
            file.write(
                marker_bytes,
            )
            file.write(
                b"\n",
            )
            file.truncate()


    def _flush(
            self,
        ):
        entries = []

        while not self._queue.empty():
            entries.append(
                self._queue.get_nowait()
            )

        if not entries:
            return

        self._insert_entries(
            entries,
        )

        for _ in entries:
            self._queue.task_done()

        self._entries.extend(
            entry
            for entry in entries
            if isinstance(entry, LogEntry)
        )

        self._updated_at = Time(
            format=self._entry_format,
        )


    def _count_levels(
            self,
        ):
        errors = 0
        warnings = 0
        criticals = 0

        for entry in self._entries:
            if entry.level == LogLevel.ERROR:
                errors += 1

            elif entry.level == LogLevel.WARNING:
                warnings += 1

            elif entry.level == LogLevel.CRITICAL:
                criticals += 1

        return warnings, errors, criticals


    def __init__(
            self,
            directory,
            name,
            *,
            type = LogType.JAR_LOG,
            datetime_format = None,
            entry_datetime_format = None,
            metadata = None,
        ):

        if isinstance(type, str):
            type = LogType(type)

        if not isinstance(type, LogType):
            raise LogTypeJError(
                "Type must be of type LogType or str"
            )

        if datetime_format and not isinstance(datetime_format, TimeFormat | str):
            raise LogTypeJError(
                "Datetime format must be of type TimeFormat or str"
            )

        if entry_datetime_format and not isinstance(entry_datetime_format, TimeFormat | str):
            raise LogTypeJError(
                "Entry datetime format format must be of type TimeFormat or str"
            )

        self._run_id = uuid4()

        self._file_format = (
            entry_datetime_format
            or type.datetime_format
        )
        self._entry_format = (
            entry_datetime_format
            or type.datetime_format
        )

        self._created_at = Time(
            format=self._file_format,
        )
        self._updated_at = self._created_at
        self._closed_at = None

        self.directory = Path(directory)
        self.name = name
        self.type = type.name
        self.path = (
            self.directory
            / f"{name}_{self._created_at!r}.{type.name}"
        )

        self._sequence = 0
        self._sequence_lock = Lock()

        self._queue = Queue()
        self._entries = []

        self._initialize_file(
            metadata,
        )


    def log(
            self,
            level,
            message,
            *,
            scope = "",
        ):

        if self._closed_at is not None:
            raise LogRuntimeJError(
                "Cannot write to a closed log"
            )

        entry = self._create_entry(
            level,
            message,
            scope,
        )

        self._queue.put(
            entry,
        )


    async def log_async(
            self,
            level,
            message,
            *,
            scope = "",
        ):

        self.log(
            level,
            message,
            scope=scope,
        )


    def comment(
            self,
            message,
        ):

        if self._closed_at is not None:
            raise LogRuntimeJError(
                "Cannot write to a closed log"
            )

        comment = LogComment(
            message,
            self.type
        )

        self._queue.put(
            comment,
        )


    async def comment_async(
            self,
            message,
        ):

        self.comment(
            message,
        )


    def flush(
            self,
        ):
        if self._closed_at is not None:
            raise LogRuntimeJError(
                "Cannot flush a closed log"
            )

        self._flush()


    def close(
            self,
            *,
            result = "SUCCESS",
        ):
        if self._closed_at is not None:
            return

        self._flush()

        self._closed_at = Time(
            format=self._file_format,
        )

        duration = (
            self._closed_at.timestamp()
            - self._created_at.timestamp()
        ) * 1000

        warnings, errors, criticals = self._count_levels()

        marker = LogRenderer.WAITING_MARKER
        marker_bytes = marker.encode("utf-8")

        footer = LogRenderer.footer(
            self._run_id,
            self._closed_at,
            f"{duration:.2f}",
            result,
            warnings=warnings,
            errors=errors,
            criticals=criticals,
        )

        footer_bytes = footer.encode("utf-8")

        with self.path.open(
                "rb+",
        ) as file:
            file.seek(
                -(len(marker_bytes) + 1),
                2,
            )

            current_marker = file.read(
                len(marker_bytes),
            )

            if current_marker != marker_bytes:
                raise LogRuntimeJError(
                    "Log waiting marker was not found"
                )

            file.seek(
                -len(marker_bytes),
                1,
            )

            file.write(
                footer_bytes,
            )
            file.truncate()


__all__ = [
    'Log',
]
