# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/Cursor
# File         : cursor.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.error import ConsoleJError
from jarbin_toolkit_console.ansi.cursor.enums import CursorStyles
from jarbin_toolkit_console.ansi.ansi import CSI


class CursorPosition(CSI):


    @classmethod
    def up(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("CursorPosition n must be a positive integer")

        return cls(f"{n}A")


    @classmethod
    def down(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("CursorPosition n must be a positive integer")

        return cls(f"{n}B")


    @classmethod
    def right(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("CursorPosition n must be a positive integer")

        return cls(f"{n}C")


    @classmethod
    def left(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("CursorPosition n must be a positive integer")

        return cls(f"{n}D")


    @classmethod
    def next_line(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("CursorPosition n must be a positive integer")

        return cls(f"{n}E")


    @classmethod
    def previous_line(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("CursorPosition n must be a positive integer")

        return cls(f"{n}F")


    @classmethod
    def column(
            cls,
            x = 1,
        ):

        if not isinstance(x, int) or x < 1:
            raise ConsoleJError("CursorPosition x must be a positive integer")

        return cls(f"{x}G")


    @classmethod
    def row(
            cls,
            y = 1,
        ):

        if not isinstance(y, int) or y < 1:
            raise ConsoleJError("CursorPosition y must be a positive integer")

        return cls(f"{y}d")


    @classmethod
    def position(
            cls,
            y = 1,
            x = 1,
        ):

        if not isinstance(y, int) or not isinstance(x, int) or y < 1 or x < 1:
            raise ConsoleJError("CursorPosition y and x must be a positive integer")

        return cls(f"{y};{x}H")


    @classmethod
    def tab(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("CursorPosition n must be a positive integer")

        return cls(f"{n}I")


    @classmethod
    def back_tab(
            cls,
            n = 1,
        ):

        if not isinstance(n, int) or n < 1:
            raise ConsoleJError("CursorPosition n must be a positive integer")

        return cls(f"{n}Z")


    @classmethod
    def column_relative(
            cls,
            x = 1,
        ):

        if not isinstance(x, int) or x < 1:
            raise ConsoleJError("CursorPosition x must be a positive integer")

        return cls(f"{x}a")


    @classmethod
    def row_relative(
            cls,
            y = 1,
        ):

        if not isinstance(y, int) or y < 1:
            raise ConsoleJError("CursorPosition y must be a positive integer")

        return cls(f"{y}e")


    @classmethod
    def position_relative(
            cls,
            y = 1,
            x = 1,
        ):

        if not isinstance(y, int) or not isinstance(x, int) or y < 1 or x < 1:
            raise ConsoleJError("CursorPosition y and x must be a positive integer")

        return cls(f"{y};{x}f")


    @classmethod
    def home(
            cls,
        ):

        return cls("H")


class CursorSave(CSI):


    @classmethod
    def save(
            cls,
        ):

        return cls("s")


    @classmethod
    def restore(
            cls,
        ):

        return cls("u")


class CursorStyle(CSI):


    @classmethod
    def set(
            cls,
            style = CursorStyles.DEFAULT,
        ):

        if not isinstance(style, CursorStyles):
            raise ConsoleJError("CursorStyle style must be CursorStyles")

        return cls(f"{style} q")


class CursorMode(CSI):


    @classmethod
    def application_keys(
            cls,
        ):

        return cls("?1h")


    @classmethod
    def normal_keys(
            cls,
        ):

        return cls("?1l")


    @classmethod
    def blink(
            cls,
        ):

        return cls("?12h")


    @classmethod
    def no_blink(
            cls,
        ):

        return cls("?12l")


    @classmethod
    def show(
            cls,
        ):

        return cls("?25h")


    @classmethod
    def hide(
            cls,
        ):

        return cls("?25l")


    @classmethod
    def origin(
            cls,
        ):

        return cls("?6h")


    @classmethod
    def absolute(
            cls,
        ):

        return cls("?6l")


    @classmethod
    def autowrap(
            cls,
        ):

        return cls("?7h")


    @classmethod
    def no_autowrap(
            cls,
        ):

        return cls("?7l")


    @classmethod
    def save_state(
            cls,
        ):

        return cls("?1048h")


    @classmethod
    def restore_state(
            cls,
        ):

        return cls("?1048l")


__all__ = [
    'CursorPosition',
    'CursorSave',
    'CursorStyle',
    'CursorMode',
]
