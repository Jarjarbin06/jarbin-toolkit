# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/SGR
# File         : sgr.py
#
# Author       : Jarjarbin06
# ============================================================================


from ansi.screen.enums import (
    ScreenDisplayEraseMode,
    ScreenLineEraseMode,
)
from jarbin_toolkit_console.ansi.ansi import CSI


class ScreenErase(CSI):


    @classmethod
    def erase_display(
            cls,
            mode = ScreenDisplayEraseMode.ALL,
        ):

        if not isinstance(mode, ScreenDisplayEraseMode):
            raise ValueError("ScreenErase mode must be ScreenDisplayEraseMode")

        return cls(f"{mode}J")


    @classmethod
    def erase_line(
            cls,
            mode = ScreenLineEraseMode.ALL,
        ):

        if not isinstance(mode, ScreenLineEraseMode):
            raise ValueError("ScreenErase mode must be ScreenLineEraseMode")

        return cls(f"{mode}K")


class ScreenEdit(CSI):


    @classmethod
    def insert_characters(
            cls,
            n = 0,
        ):

        if not isinstance(n, int):
            raise ValueError("ScreenEdit n must be int")

        return cls(f"{n}@")


    @classmethod
    def delete_characters(
            cls,
            n = 0,
        ):

        if not isinstance(n, int):
            raise ValueError("ScreenEdit n must be int")

        return cls(f"{n}P")


    @classmethod
    def erase_characters(
            cls,
            n = 0,
        ):

        if not isinstance(n, int):
            raise ValueError("ScreenEdit n must be int")

        return cls(f"{n}X")


    @classmethod
    def repeat_character(
            cls,
            n = 0,
        ):

        if not isinstance(n, int):
            raise ValueError("ScreenEdit n must be int")

        return cls(f"{n}b")


    @classmethod
    def insert_lines(
            cls,
            n = 0,
        ):

        if not isinstance(n, int):
            raise ValueError("ScreenEdit n must be int")

        return cls(f"{n}L")


    @classmethod
    def delete_lines(
            cls,
            n = 0,
        ):

        if not isinstance(n, int):
            raise ValueError("ScreenEdit n must be int")

        return cls(f"{n}M")


class ScreenScroll(CSI):


    @classmethod
    def left(
            cls,
            n = 0,
        ):

        if not isinstance(n, int):
            raise ValueError("ScreenScroll n must be int")

        return cls(f"{n} @")


    @classmethod
    def right(
            cls,
            n = 0,
        ):

        if not isinstance(n, int):
            raise ValueError("ScreenScroll n must be int")

        return cls(f"{n} A")


    @classmethod
    def set_region(
            cls,
            top = 0,
            bottom = 20,
        ):

        if not isinstance(top, int) or not isinstance(bottom, int):
            raise ValueError("ScreenScroll top and bottom must be int")

        return cls(f"{top};{bottom}r")


    @classmethod
    def reset_region(
            cls,
        ):

        return cls("r")


class ScreenMargin(CSI):


    @classmethod
    def set(
            cls,
            left = 0,
            right = 20,
        ):

        if not isinstance(left, int) or not isinstance(right, int):
            raise ValueError("ScreenScroll left and right must be int")

        return cls(f"{left};{right}s")


    @classmethod
    def enable(
            cls,
        ):

        return cls("?69h")


    @classmethod
    def disable(
            cls,
        ):

        return cls("?69l")


class ScreenWriteMode(CSI):


    @classmethod
    def set_insert(
            cls,
        ):

        return cls("4h")


    @classmethod
    def set_replace(
            cls,
        ):

        return cls("4l")


class ScreenBuffer(CSI):


    @classmethod
    def use_alternate(
            cls,
        ):

        return cls("?47h")


    @classmethod
    def use_normal(
            cls,
        ):

        return cls("?47l")


    @classmethod
    def xterm_use_alternate(
            cls,
        ):

        return cls("?1047h")


    @classmethod
    def xterm_use_normal(
            cls,
        ):

        return cls("?1047l")


    @classmethod
    def xterm_use_alternate_with_cursor(
            cls,
        ):

        return cls("?1049h")


    @classmethod
    def xterm_use_normal_with_cursor(
            cls,
        ):

        return cls("?1049l")


__all__ = [
    'ScreenErase',
    'ScreenEdit',
    'ScreenScroll',
    'ScreenMargin',
    'ScreenWriteMode',
    'ScreenBuffer',
]
