# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console
# File         : text.py
#
# Author       : Jarjarbin06
# ============================================================================
from typing import LiteralString, SupportsIndex

from wcwidth import width

from jarbin_toolkit_console.format.format import Format


class Text(str, Format):


    _can_format = True


    def _new(
            self,
            value,
        ):
        return self.__class__(value)


    def __len__(
            self,
        ):
        return width(str(self))


    def split(
            self,
            sep = None,
            maxsplit = -1,
        ):
        splited = super().split(sep, maxsplit)

        return [Text(text) for text in splited]


    def splitlines(
            self,
            keepends = False
        ):
        splited = super().splitlines(keepends)

        return [Text(text) for text in splited]


    def __add__(
            self,
            other,
        ):
        if isinstance(other, str):
            return self._new(str.__add__(str(self), other))

        return NotImplemented


    def __radd__(
            self,
            other,
        ):
        if isinstance(other, str):
            return self._new(str.__add__(str(other), self))

        return NotImplemented


    def __mul__(
            self,
            other,
        ):
        if isinstance(other, int):
            return self._new(str.__mul__(str(self), other))

        return NotImplemented


    def __rmul__(
            self,
            other,
        ):
        if isinstance(other, int):
            return self._new(str.__rmul__(str(self), other))

        return NotImplemented


__all__ = [
    'Text',
]
