from typing import (
    final,
    Any,
    Optional,
)

from jarbin_toolkit_time import Time


@final
class LogRenderer:
    """
        Log header and footer renderer

        Attributes
        ----------
        WAITING_MARKER : str
            Marker at the end of file when still opened

        SEPARATOR : str
            Bloc separator

        BORDER : str
            Bloc border
    """


    WAITING_MARKER: str
    SEPARATOR: str
    BORDER: str


    @staticmethod
    def header(
            run_id: str,
            start: Time,
            metadata: Optional[dict[str, Any]] = None,
        ) -> str:
        """
            Get the log header

            Parameters
            ----------
            run_id : str
                UUID of the current run

            start : str
                Datetime when the log was created

            metadata : Optional[dict[str, Any]]
                Metadata to show at log start

            Returns
            ----------
            str
                Formated header
        """
        ...


    @staticmethod
    def footer(
            run_id: str,
            end: Time,
            duration: str,
            result: str,
            warnings: int = 0,
            errors: int = 0,
            criticals: int = 0,
        ) -> str:
        """
            Get the log footer

            Parameters
            ----------
            run_id : str
                UUID of the current run

            end : str
                Datetime when the log was closed

            duration : str
                Pre-formated duration

            result : str
                Program status/result

            warnings : int
                Warning count

            errors : int
                Error count

            criticals : int
                Critical count

            Returns
            ----------
            str
                Formated footer
        """
        ...


__all__: list[str]
