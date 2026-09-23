from typing import final

from jarbin_toolkit_time import (
    Time,
    TimeFormat,
)

from .enums import (
    LogType,
    LogLevel,
)


@final
class LogEntry:
    """
        Log entry
    
        Attributes
        ----------
        level : LogLevel
            Log level

        message : str
            Log message

        scope : str
            Log scope
    """


    level: LogLevel
    message: str
    scope: str


    def __init__(
            self,
            sequence: int,
            level: LogLevel,
            message: str,
            format: TimeFormat | str,
            type: LogType,
            scope: str = "",
        ) -> None:
        """
            Initialize a log entry
        
            Parameters
            ----------
            sequence : int
                Sequence index

            level : LogLevel
                Log level

            message : str
                Log message

            format : TimeFormat | str
                Log time format

            type : LogType
                Log file type

            scope : str
                Log scope

            Raises
            ----------
            LogTypeJError
                Level, type type invalid
        """
        ...


    def __repr__(
            self,
        ) -> str:
        """
            Representation of the entry (formated entry)

            Returns
            ----------
            str
                Formated entry
        """
        ...


    @property
    def sequence(
            self,
        ) -> int:
        """
            Get the sequence index of the current entry

            Returns
            ----------
            int
                Sequence index
        """
        ...


    _sequence: int
    _creation_time: Time
    _type = type


__all__: list[str]
