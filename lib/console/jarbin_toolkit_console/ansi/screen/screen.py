# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/SGR
# File         : sgr.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.error import ConsoleJError
from jarbin_toolkit_console.ansi.screen.enums import (
    ScreenDisplayEraseMode,
    ScreenLineEraseMode,
)
from jarbin_toolkit_console.ansi.ansi import (
    CSI,
    ESC,
)


class ScreenErase(CSI):


    @classmethod
    def erase_display(
            cls,
            mode = ScreenDisplayEraseMode.ALL,
        ):

        if not isinstance(mode, ScreenDisplayEraseMode):
            raise ConsoleJError("ScreenErase mode must be ScreenDisplayEraseMode")

        return cls(f"{mode}J")


    @classmethod
    def erase_line(
            cls,
            mode = ScreenLineEraseMode.ALL,
        ):

        if not isinstance(mode, ScreenLineEraseMode):
            raise ConsoleJError("ScreenErase mode must be ScreenLineEraseMode")

        return cls(f"{mode}K")


class ScreenEdit(CSI):


    @classmethod
    def insert_characters(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("ScreenEdit n must be positive int")

        return cls(f"{n}@")


    @classmethod
    def delete_characters(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("ScreenEdit n must be positive int")

        return cls(f"{n}P")


    @classmethod
    def erase_characters(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("ScreenEdit n must be positive int")

        return cls(f"{n}X")


    @classmethod
    def repeat_character(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("ScreenEdit n must be positive int")

        return cls(f"{n}b")


    @classmethod
    def insert_lines(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("ScreenEdit n must be positive int")

        return cls(f"{n}L")


    @classmethod
    def delete_lines(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("ScreenEdit n must be positive int")

        return cls(f"{n}M")


class ScreenScroll(CSI):


    @classmethod
    def left(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("ScreenScroll n must be positive int")

        return cls(f"{n} @")


    @classmethod
    def right(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("ScreenScroll n must be positive int")

        return cls(f"{n} A")


    @classmethod
    def set_region(
            cls,
            top,
            bottom,
        ):

        if not isinstance(top, int) or not isinstance(bottom, int) or top < 1 or bottom < 1:
            raise ConsoleJError("ScreenScroll top and bottom must be positive int")

        if top >= bottom:
            raise ConsoleJError("ScreenScroll top must be strictly smaller than bottom")

        return cls(f"{top};{bottom}r")


    @classmethod
    def reset_region(
            cls,
        ):

        return cls("r")


class ScreenMargins(CSI):


    @classmethod
    def set(
            cls,
            left,
            right,
        ):

        if not isinstance(left, int) or not isinstance(right, int):
            raise ConsoleJError("ScreenMargins left and right must be int")

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
    def alternate(
            cls,
        ):

        return cls("?47h")


    @classmethod
    def normal(
            cls,
        ):

        return cls("?47l")


    @classmethod
    def xterm_alternate(
            cls,
        ):

        return cls("?1047h")


    @classmethod
    def xterm_normal(
            cls,
        ):

        return cls("?1047l")


    @classmethod
    def xterm_alternate_with_cursor(
            cls,
        ):

        return cls("?1049h")


    @classmethod
    def xterm_normal_with_cursor(
            cls,
        ):

        return cls("?1049l")


class ScreenTest(ESC):


    @classmethod
    def alignment_test(
            cls,
        ):

        return cls("#8")


class ScreenRectangle(CSI):


    @classmethod
    def erase(
            cls,
            top,
            left,
            bottom,
            right,
        ):

        if not isinstance(top, int) or not isinstance(left, int) or not isinstance(bottom, int) or not isinstance(right, int):
            raise ConsoleJError("ScreenRectangle top, left, bottom and right must be int")

        return cls(f"{top};{left};{bottom};{right}$z")


    @classmethod
    def fill(
            cls,
            char,
            top,
            left,
            bottom,
            right,
        ):

        if not isinstance(char, str) or len(char) != 1:
            raise ConsoleJError("ScreenRectangle char must be a single character")

        if not isinstance(top, int) or not isinstance(left, int) or not isinstance(bottom, int) or not isinstance(right, int):
            raise ConsoleJError("ScreenRectangle top, left, bottom and right must be int")

        return cls(f"{char};{top};{left};{bottom};{right}$x")


    @classmethod
    def copy(
            cls,
            src_top,
            src_left,
            src_bottom,
            src_right,
            src_page,
            dest_top,
            dest_left,
            dest_page,
        ):

        if not isinstance(src_top, int) or not isinstance(src_left, int) or not isinstance(src_bottom, int) or not isinstance(src_right, int) or not isinstance(src_page, int):
            raise ConsoleJError("ScreenRectangle src_top, src_left, src_bottom, src_right and src_page must be int")

        if not isinstance(dest_top, int) or not isinstance(dest_left, int) or not isinstance(dest_page, int):
            raise ConsoleJError("ScreenRectangle dest_top, dest_left and dest_page must be int")

        return cls(f"{src_top};{src_left};{src_bottom};{src_right};{src_page};{dest_top};{dest_left};{dest_page}$v")


class ScreenMode(CSI):


    @classmethod
    def enable_132_columns(
            cls,
        ):

        return cls(f"?3h")


    @classmethod
    def disable_132_columns(
            cls,
        ):

        return cls(f"?3l")


    @classmethod
    def disable_132_column_switching(
            cls,
        ):

        return cls(f"?40h")


    @classmethod
    def enable_132_column_switching(
            cls,
        ):

        return cls(f"?40l")


    @classmethod
    def preserve_screen_on_resize(
            cls,
        ):

        return cls(f"?95h")


    @classmethod
    def clear_screen_on_resize(
            cls,
        ):

        return cls(f"?95l")


    @classmethod
    def enable_reverse_video(
            cls,
        ):

        return cls(f"?5h")


    @classmethod
    def disable_reverse_video(
            cls,
        ):

        return cls(f"?5l")


    @classmethod
    def enable_smooth_scroll(
            cls,
        ):

        return cls(f"?4h")


    @classmethod
    def disable_smooth_scroll(
            cls,
        ):

        return cls(f"?4l")


class ScreenSize(CSI):


    @classmethod
    def set_columns(
            cls,
            columns,
        ):

        if not isinstance(columns, int) or columns < 1:
            raise ConsoleJError("ScreenSize columns must be a positive int")

        return cls(f"{columns}$|")


    @classmethod
    def set_lines(
            cls,
            lines,
        ):

        if not isinstance(lines, int) or lines < 1:
            raise ConsoleJError("ScreenSize lines must be a positive int")

        return cls(f"{lines}*|")


class ScreenControl(ESC):


    @classmethod
    def normal_index(
            cls,
        ):
        return cls("D")


    @classmethod
    def reverse_index(
            cls,
        ):
        return cls("M")


    @classmethod
    def next_line(
            cls,
        ):
        return cls("E")


__all__ = [
    'ScreenErase',
    'ScreenEdit',
    'ScreenScroll',
    'ScreenMargins',
    'ScreenWriteMode',
    'ScreenBuffer',
    'ScreenTest',
    'ScreenRectangle',
    'ScreenMode',
    'ScreenSize',
    'ScreenControl',
]
