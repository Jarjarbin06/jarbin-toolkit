# ============================================================================
# JARBIN-TOOLKIT
#
# Package      : Error
# File         : base_error.py
#
# Author       : Jarjarbin06
# ============================================================================


from jarbin_toolkit_error.enums import (
    ErrorColor,
    FormatType,
)
from jarbin_toolkit_error.error_link import ErrorLink


class BaseJError(Exception):


    def _str_compact(
            self
        ):

        result = self.error

        if self.message:
            result += f": {self.message!r}"

        return result


    def _str_pretty(
            self
        ):

        result = (
            f"{ErrorColor.ERROR_BACKGROUND} "
            f"{ErrorColor.RESET} "
            f"{ErrorColor.ERROR}"
            f"{self.error}"
            f"{ErrorColor.RESET}"
        )

        if self.message:
            for line in self.message.splitlines():
                result += (
                    f"\n{ErrorColor.ERROR_BACKGROUND} "
                    f"{ErrorColor.RESET} "
                    f"    {ErrorColor.TEXT}"
                    f"{line}"
                    f"{ErrorColor.RESET}"
                )

        return result


    def _str_detailed(
            self
        ):

        result = (
            f"{ErrorColor.ERROR_BACKGROUND} "
            f"{ErrorColor.RESET} "
            f"{ErrorColor.ERROR}"
            f"{self.error}"
            f"{ErrorColor.RESET}\n"
        )

        if self.message:
            result += (
                f"{ErrorColor.ERROR_BACKGROUND} "
                f"{ErrorColor.RESET}\n"
            )

            for line in self.message.splitlines():
                result += (
                    f"{ErrorColor.ERROR_BACKGROUND} "
                    f"{ErrorColor.RESET} "
                    f"{ErrorColor.TEXT}"
                    f"    {line}"
                    f"{ErrorColor.RESET}\n"
                )

        link = self._link.display_link(
            FormatType.DETAILED
        )

        result += (
            f"{ErrorColor.ERROR_BACKGROUND} "
            f"{ErrorColor.RESET} "
            f"\n{ErrorColor.MUTED}"
            f"{ErrorColor.ERROR_BACKGROUND} "
            f"{ErrorColor.RESET} "
            f"Location: "
            f"{ErrorColor.RESET}"
            f"{link}"
        )

        return result.strip()


    def _str_traceback(
            self
        ):

        result = (
            f"\n{ErrorColor.ERROR}"
            f"{self.error}"
            f"{ErrorColor.RESET}"
        )

        if self.message:
            message = self.message.replace(
                "\n",
                "\n    "
            )

            result += (
                f": {ErrorColor.TEXT}"
                f"\n    {message}"
                f"{ErrorColor.RESET}\n"
            )

        link = self._link.display_link(
            FormatType.TRACEBACK
        )

        result += f"\n    {link}"

        return result


    def __init__(
            self,
            message,
            *,
            error = None,
            format = FormatType.TRACEBACK,
            link = None,
            do_raise = False,
        ):

        if not isinstance(message, str):
            raise TypeError(
                "Message must be of type str"
            )

        message = message.strip()

        if error is None:
            error = type(self).__name__

        if not isinstance(error, str):
            raise TypeError(
                "Error must be of type str"
            )

        if isinstance(format, str):
            format = FormatType(format)

        if not isinstance(format, FormatType):
            raise TypeError(
                "Format must be of type FormatType or str"
            )


        if not link:
            link = ErrorLink()
        else:
            if len(link) > 7:
                raise ValueError(
                    f"Link can contain up to 7 fields, {len(link)} currently sent"
                )

            link = ErrorLink(**link)

        self.message = message
        self.error = error
        self._format = format
        self._link = link

        if do_raise:
            raise self


    def __str__(
            self
        ):

        if self._format == FormatType.COMPACT:
            return self._str_compact()
        elif self._format == FormatType.PRETTY:
            return self._str_pretty()
        elif self._format == FormatType.DETAILED:
            return self._str_detailed()
        elif self._format == FormatType.TRACEBACK:
            return self._str_traceback()

        return f"{self.error}: {self.message}"


    def __repr__(
            self
        ) -> str:

        return (
            f"<{type(self).__name__}("
            f"error={self.error!r}, "
            f"message={self.message!r}, "
            f")>"
        )


__all__ = [
    'BaseJError',
]
