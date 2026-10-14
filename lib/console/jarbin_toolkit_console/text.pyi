# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console
# File         : text.py
#
# Author       : Jarjarbin06
# ============================================================================


from typing import (
    Any,
    Optional
)

from .format.format import Format


class Text(str, Format):
    """
        Text object
        (str, Format)
    """


    def __len__(
            self,
        ) -> int:
        """
            Get the length of the Text (length don't count the ANSI sequences)

            Returns
            ----------
            int
                Length
        """
        ...


    def split(
            self,
            sep: Optional[str] = None,
            maxsplit: int = -1,
        ) -> list[Text]:
        """
            Split a string into multiple parts.

            Parameters
            ----------
            sep : str
                Splitter

            maxsplit : int
                Maximum number of parts to split

            Returns
            ----------
            list[Text]
                Splited text
        """
        ...


    def splitlines(
            self,
            keepends: bool = False
        ) -> list[Text]:
        """
            Split a string per line.

            Parameters
            ----------
            keepends : bool
                Keep ends of each line

            Returns
            ----------
            list[Text]
                Splited text
        """
        ...


    def __add__(
            self,
            other: str,
        ) -> Text:
        """
            Add 2 Text/strings together
        
            Parameters
            ----------
            other : str
                Other string
        
            Returns
            ----------
            Text
                New text
        """
        ...


    def __radd__(
            self,
            other,
        ) -> Text:
        """
            Add 2 Text/strings together

            Parameters
            ----------
            other : str
                Other string

            Returns
            ----------
            Text
                New text
        """
        ...


    def __mul__(
            self,
            other: int,
        ) -> Text:
        """
            Duplicate the Text.

            Parameters
            ----------
            other : int
                Duplication amount

            Returns
            ----------
            Text
                New text
        """
        ...


    def __rmul__(
            self,
            other: int,
        ) -> Text:
        """
            Duplicate the Text.

            Parameters
            ----------
            other : int
                Duplication amount

            Returns
            ----------
            Text
                New text
        """
        ...


    _can_format: bool = True


    def _new(
            self,
            value: Any,
        ) -> Text:
        ...


__all__: list[str]
