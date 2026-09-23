from os import PathLike
from pathlib import Path
from threading import Lock
from typing import (
    Any,
    Optional,
)
from queue import Queue

from jarbin_toolkit_time import (
    Time,
    TimeFormat,
)

from .enums import (
    LogType,
    LogLevel,
)


class Log:
    """
        Log

        Attributes
        ----------
        directory : Path
            Directory

        name : str
            File name

        type : str
            File type

        path : Path
            Full file path
    """


    directory: Path
    name: str
    type: str
    path: Path


    def __init__(
            self,
            directory: PathLike | str,
            name: str,
            *,
            type: LogType = LogType.JAR_LOG,
            datetime_format: Optional[TimeFormat | str] = None,
            entry_datetime_format: Optional[TimeFormat | str] = None,
            metadata: dict[str, Any] = None,
        ):
        """
            Initialize and create the log file
        
            Parameters
            ----------
            directory : PathLike | str
                
        
            Returns
            ----------
            
                
        
            Raises
            ----------
            LogTypeJError
                Type, datetime, entry datetime type invalid
        """
        ...


    def log(
            self,
            level: LogLevel | str,
            message: str,
            *,
            scope: str = "",
        ):
        """
            Log

            Parameters
            ----------
            level : LogLevel | str
                Log level

            message : str
                Log

            scope : str
                Log scope

            Raises
            ----------
            LogRuntimeJError
                Log status invalid
        """
        ...


    async def log_async(
            self,
            level,
            message,
            *,
            scope = "",
        ):
        """
            Log [ASYNC]

            Parameters
            ----------
            level : LogLevel | str
                Log level

            message : str
                Log

            scope : str
                Log scope

            Raises
            ----------
            LogRuntimeJError
                Log status invalid
        """
        ...


    def comment(
            self,
            message,
        ):
        """
            Comment

            Parameters
            ----------
            message : str
                Comment

            Raises
            ----------
            LogRuntimeJError
                Log status invalid
        """
        ...


    async def comment_async(
            self,
            message :str,
        ) -> None:
        """
            Comment [ASYNC]
        
            Parameters
            ----------
            message : str
                Comment

            Raises
            ----------
            LogRuntimeJError
                Log status invalid
        """
        ...


    def flush(
            self,
        ) -> None:
        """
            Save all entries and comment into the log file

            Raises
            ----------
            LogRuntimeJError
                File status invalid
        """
        ...


    def close(
            self,
            *,
            result: str = "SUCCESS",
        ) -> None:
        """
            Close the log file

            Parameters
            ----------
            result : str
                Program status/result

            Raises
            ----------
            LogRuntimeJError
                Marker not found
        """
        ...


    def _create_entry(
            self,
            level: LogLevel,
            message: str,
            scope: str,
        ):
        ...


    def _initialize_file(
            self,
            metadata: dict[str, Any],
        ):
        ...


    def _insert_entries(
            self,
            entries: list,
        ):
        ...


    def _flush(
            self,
        ):
        ...


    def _count_levels(
            self,
        ):
        ...


    _run_id: str
    _file_format: TimeFormat
    _entry_format: TimeFormat
    _created_at: Time
    _updated_at: Time
    _closed_at: Optional[Time]
    _sequence: int
    _sequence_lock: Lock
    _queue: Queue
    _entries: list


__all__: list[str]
