from os import PathLike
from types import FrameType
from typing import (
    final,
)

from jarbin_toolkit_error.enums import FormatType

@final
class ErrorLink:
    """
        Link to where the error comes from

        Attributes
        ----------
        file : Optional[str]
            File path

        line : Optional[int]
            Line number

        column : Optional[int]
            Column number

        function : Optional[str]
            Function name

        module : Optional[str]
            Module name

        class_name : Optional[str]
            Class name

        code : Optional[str]
            Code that triggered the error
    """


    file: str | None
    line: int | None
    column: int | None
    function: str | None
    module: str | None
    class_name: str | None
    code: str | None


    def __init__(
            self,
            *,
            file: PathLike | str | None = None,
            line: int | None = None,
            column: int | None = None,
            function: str | None = None,
            module: str | None = None,
            class_name: str | None = None,
            code: str | None = None
        ) -> None:
        """
            Initialize a link

            Parameters
            ----------
            file : Optional[PathLike | str]
                File path

            line : Optional[int]
                Line number

            column : Optional[int]
                Column number

            function : Optional[str]
                Function name

            module : Optional[str]
                Module name

            class_name : Optional[str]
                Class name

            code : Optional[str]
                Code that triggered the error

            Raises
            ----------
            TypeError
                File, line, column, function, module, class_name, code type invalid
        """




    def resolve(
            self
        ) -> None:
        """
            Resolve exception context
        """


    def display_link(
            self,
            format: FormatType | str
        ) -> str:
        """
            Get the string representation of the link with a format

            Parameters
            ----------
            format : FormatType | str
                Format to be displayed

            Returns
            ----------
            str
                Link ready to be printed

            Raises
            ----------
            TypeError
                Format type invalid
        """


    @staticmethod
    def _is_internal_frame(
            filename: str
        ) -> bool:
        ...


    @staticmethod
    def _resolve_column(
            frame: FrameType | None
        ) -> int | None:
        ...


    def _str_detailed(
            self,
        ) -> str:
        ...


    def _str_traceback(
            self,
        ) -> str:
        ...


    def _resolve_frame(
            self,
            frame: FrameType | None
        ) -> None:
        ...


__all__: list[str] = [
    'ErrorLink',
]
