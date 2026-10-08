# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console
# File         : text.py
#
# Author       : Jarjarbin06
# ============================================================================


from typing import Any

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
