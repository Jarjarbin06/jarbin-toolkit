from os import PathLike
from types import FrameType
from typing import Optional

from jarbin_toolkit_error.enums import FormatType


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


    file: Optional[str]
    line: Optional[int]
    column: Optional[int]
    function: Optional[str]
    module: Optional[str]
    class_name: Optional[str]
    code: Optional[str]


    def __init__(
            self,
            *,
            file: Optional[PathLike | str] = None,
            line: Optional[int] = None,
            column: Optional[int] = None,
            function: Optional[str] = None,
            module: Optional[str] = None,
            class_name: Optional[str] = None,
            code: Optional[str] = None
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
        ...


    def __repr__(
            self
        ) -> str:
        """
            Representation of the link

            Returns
            ----------
            str
                Link's representation
        """
        ...


    def resolve(
            self
        ) -> None:
        """
            Resolve exception context
        """
        ...


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
        ...


    @staticmethod
    def _is_internal_frame(
            filename: str
        ) -> bool:
        ...


    @staticmethod
    def _resolve_column(
            frame: Optional[FrameType]
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
            frame: Optional[FrameType]
        ) -> None:
        ...


__all__: list[str]
