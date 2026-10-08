# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Console/ANSI
# File         : query.py
#
# Author       : Jarjarbin06
# ============================================================================


import base64
import re
import select
import sys
import termios
import time
import tty
import os
from typing import final

from jarbin_toolkit_console.error import ConsoleJError
from jarbin_toolkit_console.ansi.ansi import CSI, DCS
from jarbin_toolkit_console.ansi.osc.enums import OSCClipboardSelection


@final
class Query:


    @staticmethod
    def _read(
            terminator,
            timeout = 1.0,
        ):

        if not sys.stdin.isatty():
            return None

        fd = sys.stdin.fileno()

        try:
            settings = termios.tcgetattr(fd)
        except (OSError, termios.error):
            return None

        try:
            tty.setcbreak(fd)

            response = ""
            deadline = time.monotonic() + timeout

            while True:
                remaining = deadline - time.monotonic()

                if remaining <= 0:
                    return None

                ready, _, _ = select.select(
                    [fd],
                    [],
                    [],
                    remaining,
                )

                if not ready:
                    return None

                data = os.read(fd, 1)

                if not data:
                    return None

                response += data.decode(
                    "latin1",
                )

                if response.endswith(terminator):
                    return response

        except (OSError, UnicodeError, termios.error):
            return None

        finally:
            try:
                termios.tcsetattr(
                    fd,
                    termios.TCSADRAIN,
                    settings,
                )
            except (OSError, termios.error):
                pass


    @classmethod
    def _request(
            cls,
            sequence,
            terminator,
        ):

        if not sys.stdin.isatty() or not sys.stdout.isatty():
            return None

        try:
            sys.stdout.write(str(sequence))
            sys.stdout.flush()
        except (OSError, IOError):
            return None

        return cls._read(terminator)


    @staticmethod
    def _match(
            response,
            pattern,
        ):

        if response is None:
            return None

        return re.fullmatch(pattern, response)


    @classmethod
    def cursor_position(
            cls,
            private=False,
        ):

        prefix = "?" if private else ""

        response = cls._request(
            CSI(f"{prefix}6n"),
            "R",
        )

        pattern = (
            r"\x1b\[\?(\d+);(\d+)R"
            if private
            else r"\x1b\[(\d+);(\d+)R"
        )

        match = cls._match(
            response,
            pattern,
        )

        if match is None:
            return None

        return (
            int(match.group(1)),
            int(match.group(2)),
        )


    @classmethod
    def device_attributes(
            cls,
            secondary = False,
        ):

        sequence = CSI(">c" if secondary else "c")
        pattern = (
            r"\x1b\[>([\d;]*)c"
            if secondary
            else r"\x1b\[\?([\d;]*)c"
        )

        response = cls._request(
            sequence,
            "c",
        )

        match = cls._match(response, pattern)

        if match is None:
            return None

        return tuple(
            int(value)
            for value in match.group(1).split(";")
            if value
        )


    @classmethod
    def device_status(
            cls,
            status=5,
            private=False,
        ):

        if not isinstance(status, int) or status < 0:
            raise ConsoleJError(
                "Query status must be a non-negative integer"
            )

        if status == 6:
            return cls.cursor_position(private)

        prefix = "?" if private else ""

        response = cls._request(
            CSI(f"{prefix}{status}n"),
            "n",
        )

        pattern = (
            r"\x1b\[\?(\d+)n"
            if private
            else r"\x1b\[(\d+)n"
        )

        match = cls._match(
            response,
            pattern,
        )

        if match is None:
            return None

        return int(match.group(1))


    @classmethod
    def mode(
            cls,
            mode,
            private=False,
        ):

        if not isinstance(mode, int) or mode < 0:
            raise ConsoleJError(
                "Query mode must be a non-negative integer"
            )

        prefix = "?" if private else ""

        response = cls._request(
            CSI(f"{prefix}{mode}$p"),
            "y",
        )

        pattern = (
            r"\x1b\[\?(\d+);(\d+)\$y"
            if private
            else r"\x1b\[(\d+);(\d+)\$y"
        )

        match = cls._match(
            response,
            pattern,
        )

        if match is None:
            return None

        return (
            int(match.group(1)),
            int(match.group(2)),
        )


    @classmethod
    def status_string(
            cls,
            value,
        ):

        if not isinstance(value, str):
            raise ConsoleJError(
                "Query value must be a string"
            )

        response = cls._request(
            DCS(f"$q{value}\x1b\\"),
            "\x1b\\",
        )

        match = cls._match(
            response,
            r"\x1bP(\d+)\$r(.*)\x1b\\",
        )

        if match is None:
            return None

        return (
            int(match.group(1)),
            match.group(2),
        )


    @classmethod
    def version(
            cls,
        ):

        response = cls._request(
            CSI(">0q"),
            "\x1b\\",
        )

        match = cls._match(
            response,
            r"\x1bP>\|(.*)\x1b\\",
        )

        if match is None:
            return None

        return match.group(1)


    @classmethod
    def terminal_capability(
            cls,
            capability,
        ):

        if not isinstance(capability, str):
            raise ConsoleJError(
                "Query capability must be a string"
            )

        capability = capability.encode().hex()

        response = cls._request(
            DCS(f"+q{capability}\x1b\\"),
            "\x1b\\",
        )

        match = cls._match(
            response,
            r"\x1bP1\+r(.*)\x1b\\",
        )

        if match is None or "=" not in match.group(1):
            return None

        name, value = match.group(1).split("=", 1)

        try:
            name = bytes.fromhex(name).decode()
        except (ValueError, UnicodeDecodeError):
            return None

        return (
            name,
            value,
        )


    @classmethod
    def clipboard(
            cls,
            selection,
        ):

        if not isinstance(selection, OSCClipboardSelection):
            raise ConsoleJError("Query selection must be OSCClipboardSelection")

        response = cls._request(
            f"\x1b]52;{selection};?\x1b\\",
            "\x1b\\",
        )

        match = cls._match(
            response,
            rf"\x1b\]52;{selection};(.*)\x1b\\",
        )

        if match is None:
            return None

        try:
            return base64.b64decode(
                match.group(1),
            ).decode()
        except (
            ValueError,
            UnicodeDecodeError,
        ):
            return None


__all__ = [
    'Query',
]
