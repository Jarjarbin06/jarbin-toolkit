# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI/OSC
# File         : osc.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_console.ansi.ansi import OSC


ST = "\x1b\\"


class OSCTitle(OSC):


    @classmethod
    def set_name(
            cls,
            name,
        ):

        if not isinstance(name, str):
            raise TypeError("OSCTitle name must be sting")

        cls(f"0;{name}{ST}")


    @classmethod
    def set_icon(
            cls,
            icon,
        ):

        if not isinstance(icon, str):
            raise TypeError("OSCTitle name must be sting")

        cls(f"1;{icon}{ST}")


    @classmethod
    def set_title(
            cls,
            title,
        ):

        if not isinstance(title, str):
            raise TypeError("OSCTitle name must be sting")

        cls(f"2;{title}{ST}")


    @classmethod
    def set_property(
            cls,
            name,
            value,
        ):

        if not isinstance(name, str) or not isinstance(value, str):
            raise TypeError("OSCTitle name and value must be stings")

        cls(f"3;{name}={value}{ST}")


class OSCColor(OSC):


    @classmethod
    def foreground(
            cls,
            color,
        ):

        cls(f"10;#{color}{ST}")


    @classmethod
    def background(
            cls,
            color,
        ):

        cls(f"11;#{color}{ST}")


    @classmethod
    def cursor(
            cls,
            color,
        ):

        cls(f"12;#{color}{ST}")


    @classmethod
    def pointer_foreground(
            cls,
            color,
        ):

        cls(f"13;#{color}{ST}")


    @classmethod
    def pointer_background(
            cls,
            color,
        ):

        cls(f"14;#{color}{ST}")


    @classmethod
    def reset_foreground(
            cls,
        ):

        cls(f"110{ST}")


    @classmethod
    def reset_background(
            cls,
        ):

        cls(f"111{ST}")


    @classmethod
    def reset_cursor(
            cls,
        ):

        cls(f"112{ST}")


    @classmethod
    def reset_pointer_foreground(
            cls,
        ):

        cls(f"113{ST}")


    @classmethod
    def reset_pointer_background(
            cls,
        ):

        cls(f"114{ST}")


__all__ = [
    'OSCTitle',
    'OSCColor',
]
