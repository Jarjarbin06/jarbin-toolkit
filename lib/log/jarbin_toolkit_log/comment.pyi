from typing import final

from .enums import LogType


@final
class LogComment:
    """
        Comment log entry
    
        Attributes
        ----------
        PREFIX : str
            Jar-Log prefix

        message : str
            Comment
    """


    PREFIX: str
    message: str


    def __init__(
            self,
            message: str,
            type: LogType | str
        ) -> None:
        """
            Initialize a comment entry

            Parameters
            ----------
            message : str
                Comment

            type : LogType
                Type of the log file

            Raises
            ----------
            LogTypeJError
                Message, type type invalid
        """
        ...


    def __repr__(
            self,
        ) -> str:
        """
            Representation of the comment (formated comment)

            Returns
            ----------
            str
                Formated comment
        """
        ...


    _type: LogType


__all__: list[str]
