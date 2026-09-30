# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/OSC
# File         : osc.py
#
# Author       : Jarjarbin06
# ============================================================================


import base64
from pathlib import Path

from jarbin_toolkit_console.ansi.query import Query
from jarbin_toolkit_console.ansi.osc.enums import OSCClipboardSelection
from jarbin_toolkit_console.ansi.ansi import OSC


ST = "\x1b\\"


class OSCTitle(OSC):


    @classmethod
    def set_name(
            cls,
            name,
        ):

        if not isinstance(name, str):
            raise TypeError("OSCTitle name must be string")

        return cls(f"0;{name}{ST}")


    @classmethod
    def set_icon(
            cls,
            icon,
        ):

        if not isinstance(icon, str):
            raise TypeError("OSCTitle name must be string")

        return cls(f"1;{icon}{ST}")


    @classmethod
    def set_title(
            cls,
            title,
        ):

        if not isinstance(title, str):
            raise TypeError("OSCTitle name must be string")

        return cls(f"2;{title}{ST}")


    @classmethod
    def set_property(
            cls,
            name,
            value,
        ):

        if not isinstance(name, str) or not isinstance(value, str):
            raise TypeError("OSCTitle name and value must be strings")

        return cls(f"3;{name}={value}{ST}")


class OSCColor(OSC):


    @classmethod
    def foreground(
            cls,
            color,
        ):

        return cls(f"10;#{color}{ST}")


    @classmethod
    def background(
            cls,
            color,
        ):

        return cls(f"11;#{color}{ST}")


    @classmethod
    def cursor(
            cls,
            color,
        ):

        return cls(f"12;#{color}{ST}")


    @classmethod
    def pointer_foreground(
            cls,
            color,
        ):

        return cls(f"13;#{color}{ST}")


    @classmethod
    def pointer_background(
            cls,
            color,
        ):

        return cls(f"14;#{color}{ST}")


    @classmethod
    def reset_foreground(
            cls,
        ):

        return cls(f"110{ST}")


    @classmethod
    def reset_background(
            cls,
        ):

        return cls(f"111{ST}")


    @classmethod
    def reset_cursor(
            cls,
        ):

        return cls(f"112{ST}")


    @classmethod
    def reset_pointer_foreground(
            cls,
        ):

        return cls(f"113{ST}")


    @classmethod
    def reset_pointer_background(
            cls,
        ):

        return cls(f"114{ST}")


class OSCWindow(OSC):


    @classmethod
    def set_directory(
            cls,
            path,
            force = False,
        ):

        if not isinstance(path, str):
            raise TypeError("OSCWindow path must be string")

        try:
            path = Path(path).resolve(strict=True)
        except FileNotFoundError:
            if not force:
                raise FileNotFoundError("OSCWindow path must exist")

        if not force and not path.is_dir():
            raise FileNotFoundError("OSCWindow path must be a directory")

        return cls(f"7;file://{path}{ST}")


class OSCHyperlink(OSC):


    @classmethod
    def open(
            cls,
            link,
        ):

        if not isinstance(link, str):
            raise TypeError("OSCHyperlink link must be string")

        return cls(f"8;;{link}{ST}")


    @classmethod
    def close(
            cls,
        ):

        return cls(f"8;;{ST}")


class OSCNotification(OSC):


    @classmethod
    def notify_simple(
            cls,
            message,
        ):

        if not isinstance(message, str):
            raise TypeError("OSCNotification message must be string")

        return cls(f"9;{message}{ST}")


    @classmethod
    def notify_advanced(
            cls,
            title,
            message,
        ):

        if not isinstance(title, str) or not isinstance(message, str):
            raise TypeError("OSCNotification title and message must be string")

        return cls(f"777;notify;{title};{message}{ST}")


class OSCClipboard(OSC):


    @classmethod
    def copy(
            cls,
            value,
            selection=OSCClipboardSelection.CLIPBOARD,
        ):

        if not isinstance(value, str):
            raise TypeError(
                "OSCClipboard value must be string"
            )

        if not isinstance(selection, OSCClipboardSelection):
            raise TypeError(
                "OSCClipboard selection must be "
                "OSCClipboardSelection"
            )

        value = base64.b64encode(
            value.encode(),
        ).decode()

        return cls(
            f"52;{selection};{value}{ST}"
        )


    @classmethod
    def paste(
            cls,
            selection=OSCClipboardSelection.CLIPBOARD,
        ):

        if not isinstance(selection, OSCClipboardSelection):
            raise TypeError(
                "OSCClipboard selection must be "
                "OSCClipboardSelection"
            )

        return Query.clipboard(selection)


    @classmethod
    def clear(
            cls,
            selection=OSCClipboardSelection.CLIPBOARD,
        ):

        if not isinstance(selection, OSCClipboardSelection):
            raise TypeError(
                "OSCClipboard selection must be "
                "OSCClipboardSelection"
            )

        return cls(
            f"52;{selection};{ST}"
        )


class OSCShell(OSC):


    @classmethod
    def prompt_start(
            cls,
        ):

        return cls(f"133;A{ST}")


    @classmethod
    def prompt_end(
            cls,
        ):

        return cls(f"133;B{ST}")


    @classmethod
    def command_output(
            cls,
        ):

        return cls(f"133;C{ST}")


    @classmethod
    def command_end(
            cls,
        ):

        return cls(f"133;D{ST}")


__all__ = [
    'OSCTitle',
    'OSCColor',
    'OSCWindow',
    'OSCHyperlink',
    'OSCNotification',
    'OSCClipboard',
    'OSCShell',
]
